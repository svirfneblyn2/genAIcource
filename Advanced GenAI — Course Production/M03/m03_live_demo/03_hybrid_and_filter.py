"""
Step 3: Metadata Pre-Filtering & Hybrid Search (Dense + BM25 Fusion).

Demonstrates:
1. Hard Security Pre-Filtering: User role ACL check BEFORE vector search.
2. Sparse Lexical Search (BM25 token inverted index) for exact identifiers (e.g. "Room B12", "POL-IT-101").
3. Dense Vector Search for conceptual and semantic match.
4. Reciprocal Rank Fusion (RRF) combining both signals into an optimal ranking.
"""

import numpy as np
import re
import math
import os
import sys
import importlib.util
from typing import List, Tuple, Dict, Set
from collections import Counter, defaultdict

# Load modules
spec1 = importlib.util.spec_from_file_location("chunking_module", os.path.join(os.path.dirname(__file__), "01_chunking.py"))
chunking_mod = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(chunking_mod)
structure_aware_chunking = chunking_mod.structure_aware_chunking
SAMPLE_DOCUMENTS = chunking_mod.SAMPLE_DOCUMENTS
DocumentChunk = chunking_mod.DocumentChunk

spec2 = importlib.util.spec_from_file_location("vstore_module", os.path.join(os.path.dirname(__file__), "02_vector_search.py"))
vstore_mod = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(vstore_mod)
LightweightEmbeddingModel = vstore_mod.LightweightEmbeddingModel
InMemoryVectorStore = vstore_mod.InMemoryVectorStore

class SimpleBM25:
    """Lightweight in-memory BM25 lexical ranker for keyword retrieval."""
    def __init__(self, chunks: List[DocumentChunk], k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks
        self.k1 = k1
        self.b = b
        self.doc_len = [len(c.content.lower().split()) for c in chunks]
        self.avg_doc_len = sum(self.doc_len) / max(len(self.doc_len), 1)
        self.doc_freqs = defaultdict(int)
        self.tf = []

        for c in chunks:
            tokens = re.findall(r'[a-zA-Z0-9_\$]+', c.content.lower())
            counts = Counter(tokens)
            self.tf.append(counts)
            for tok in counts:
                self.doc_freqs[tok] += 1

        self.N = len(chunks)
        self.idf = {}
        for tok, df in self.doc_freqs.items():
            self.idf[tok] = math.log((self.N - df + 0.5) / (df + 0.5) + 1.0)

    def score(self, query: str) -> np.ndarray:
        q_tokens = re.findall(r'[a-zA-Z0-9_\$]+', query.lower())
        scores = np.zeros(self.N, dtype=np.float32)

        for i in range(self.N):
            doc_len = self.doc_len[i]
            tf_dict = self.tf[i]
            score = 0.0
            for qt in q_tokens:
                if qt in tf_dict:
                    freq = tf_dict[qt]
                    idf = self.idf.get(qt, 0.1)
                    denom = freq + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avg_doc_len))
                    score += idf * (freq * (self.k1 + 1.0)) / denom
            scores[i] = score
        return scores

def reciprocal_rank_fusion(dense_ranks: Dict[str, int], sparse_ranks: Dict[str, int], k: int = 60) -> Dict[str, float]:
    """
    RRF Formula: RRF_score(d) = 1/(k + rank_dense(d)) + 1/(k + rank_sparse(d))
    k=60 is standard in enterprise search (Elasticsearch / Azure AI Search).
    """
    all_chunk_ids = set(dense_ranks.keys()).union(set(sparse_ranks.keys()))
    rrf_scores = {}
    for cid in all_chunk_ids:
        r_dense = dense_ranks.get(cid, 999)
        r_sparse = sparse_ranks.get(cid, 999)
        score = (1.0 / (k + r_dense)) + (1.0 / (k + r_sparse))
        rrf_scores[cid] = score
    return rrf_scores

class HybridSearchEngine:
    def __init__(self, chunks: List[DocumentChunk]):
        self.all_chunks = chunks
        self.embedder = LightweightEmbeddingModel(dim=128)
        self.vstore = InMemoryVectorStore(self.embedder)
        self.vstore.add_chunks(chunks)
        self.bm25 = SimpleBM25(chunks)
        self.chunk_by_id = {c.chunk_id: c for c in chunks}

    def search_with_filter(self, query: str, user_role: str, top_k: int = 3) -> List[Tuple[DocumentChunk, float, str]]:
        """
        1. Pre-filter by user_role (Security Access Control Boundary).
        2. Compute BM25 Lexical scores.
        3. Compute Dense Cosine Vector scores.
        4. Fuse using RRF (Reciprocal Rank Fusion).
        """
        # Step 1: Filter eligible indices
        allowed_indices = []
        for idx, chunk in enumerate(self.all_chunks):
            if "all" in chunk.allowed_roles or user_role in chunk.allowed_roles:
                allowed_indices.append(idx)

        if not allowed_indices:
            return []

        # Step 2: Dense retrieval
        query_vec = self.embedder.embed(query)
        dense_matrix = self.vstore.matrix[allowed_indices]
        dense_sims = np.dot(dense_matrix, query_vec)
        dense_sorted_local_indices = np.argsort(-dense_sims)

        dense_ranks = {}
        for rank, local_idx in enumerate(dense_sorted_local_indices, 1):
            global_idx = allowed_indices[local_idx]
            cid = self.all_chunks[global_idx].chunk_id
            dense_ranks[cid] = rank

        # Step 3: Sparse BM25 retrieval
        all_bm25_scores = self.bm25.score(query)
        filtered_bm25 = all_bm25_scores[allowed_indices]
        sparse_sorted_local_indices = np.argsort(-filtered_bm25)

        sparse_ranks = {}
        for rank, local_idx in enumerate(sparse_sorted_local_indices, 1):
            global_idx = allowed_indices[local_idx]
            cid = self.all_chunks[global_idx].chunk_id
            sparse_ranks[cid] = rank

        # Step 4: Reciprocal Rank Fusion
        rrf = reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=60)
        sorted_rrf = sorted(rrf.items(), key=lambda x: x[1], reverse=True)[:top_k]

        results = []
        for cid, score in sorted_rrf:
            chunk = self.chunk_by_id[cid]
            d_rank = dense_ranks.get(cid, "N/A")
            s_rank = sparse_ranks.get(cid, "N/A")
            breakdown = f"Dense #{d_rank}, BM25 #{s_rank}"
            results.append((chunk, score, breakdown))

        return results

if __name__ == "__main__":
    print("=" * 70)
    print("DEMO STEP 3: METADATA ACL PRE-FILTERING & HYBRID SEARCH (DENSE + BM25)")
    print("=" * 70)

    chunks = structure_aware_chunking(SAMPLE_DOCUMENTS)
    engine = HybridSearchEngine(chunks)

    print("\n--- TEST CASE A: Security Boundary Pre-Filtering ---")
    query_exec = "What are the rules for Tier-4 priority executive cellular routers?"

    print(f"Query: \"{query_exec}\"")
    print("\n[Scenario 1] User Role: 'intern' (Cannot view Executive Confidential chunks)")
    results_intern = engine.search_with_filter(query_exec, user_role="intern", top_k=2)
    for c, score, breakdown in results_intern:
        print(f"  Result: [{c.doc_id}] § {c.section} (RRF: {score:.5f}) - {breakdown}")

    print("\n[Scenario 2] User Role: 'executive' (Has access to Executive Confidential chunks)")
    results_exec = engine.search_with_filter(query_exec, user_role="executive", top_k=2)
    for c, score, breakdown in results_exec:
        print(f"  Result: [{c.doc_id}] § {c.section} (RRF: {score:.5f}) - {breakdown}")

    print("\n--- TEST CASE B: Hybrid RRF Fusion for Exact Match ('Room B12') ---")
    query_hybrid = "Where do I pick up the emergency loan in Room B12?"
    print(f"Query: \"{query_hybrid}\"")
    results_hybrid = engine.search_with_filter(query_hybrid, user_role="employee", top_k=2)
    for rank, (c, score, breakdown) in enumerate(results_hybrid, 1):
        print(f"  Rank #{rank} [RRF Score: {score:.5f}] ({breakdown})")
        print(f"    Target: {c.doc_id} § {c.section}")
        lines = [l for l in c.content.splitlines() if "Room B12" in l or "Collection" in l]
        if lines:
            print(f"    Evidence Span: \"{lines[0].strip()}\"")
