"""
Step 2: Vector Embedding & Similarity Search Engine.

Demonstrates:
1. Converting text chunks into dense L2-normalized vector embeddings.
2. The mathematics of Cosine Similarity using vectorized matrix operations.
3. Top-k nearest-neighbor candidate ranking with confidence scoring.
"""

import numpy as np
import math
import re
import os
import sys
import importlib.util
from typing import List, Tuple, Dict
from dataclasses import dataclass

# Load chunking module dynamically
spec = importlib.util.spec_from_file_location("chunking_module", os.path.join(os.path.dirname(__file__), "01_chunking.py"))
chunking_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chunking_mod)
structure_aware_chunking = chunking_mod.structure_aware_chunking
SAMPLE_DOCUMENTS = chunking_mod.SAMPLE_DOCUMENTS
DocumentChunk = chunking_mod.DocumentChunk

class LightweightEmbeddingModel:
    """
    Deterministic semantic text embedder using subword n-grams and hashing.
    Outputs 128-dimensional dense float32 vectors normalized to unit length (L2 norm = 1.0).
    Requires ZERO external API calls, ZERO downloads, and runs in microseconds.
    """
    def __init__(self, dim: int = 128, seed: int = 42):
        self.dim = dim
        self.rng = np.random.default_rng(seed)
        self.projection = self.rng.standard_normal((1024, self.dim), dtype=np.float32)
        self.bucket_size = 1024

    def _tokenize(self, text: str) -> List[str]:
        tokens = re.findall(r'[a-zA-Z0-9_\$]+', text.lower())
        features = list(tokens)
        for t in tokens:
            if len(t) >= 4:
                for i in range(len(t) - 2):
                    features.append(t[i:i+3])
        return features

    def embed(self, text: str) -> np.ndarray:
        tokens = self._tokenize(text)
        if not tokens:
            return np.zeros(self.dim, dtype=np.float32)

        bow = np.zeros(self.bucket_size, dtype=np.float32)
        for tok in tokens:
            h = abs(hash(tok)) % self.bucket_size
            bow[h] += 1.0

        dense_vec = np.dot(bow, self.projection)
        norm = np.linalg.norm(dense_vec)
        if norm > 1e-9:
            dense_vec = dense_vec / norm
        return dense_vec

    def embed_batch(self, texts: List[str]) -> np.ndarray:
        return np.vstack([self.embed(t) for t in texts])

class InMemoryVectorStore:
    def __init__(self, embedding_model: LightweightEmbeddingModel):
        self.model = embedding_model
        self.chunks: List[DocumentChunk] = []
        self.matrix: np.ndarray = np.empty((0, self.model.dim), dtype=np.float32)

    def add_chunks(self, chunks: List[DocumentChunk]):
        self.chunks.extend(chunks)
        contents = [c.content for c in chunks]
        new_vectors = self.model.embed_batch(contents)
        if self.matrix.shape[0] == 0:
            self.matrix = new_vectors
        else:
            self.matrix = np.vstack([self.matrix, new_vectors])

    def search(self, query: str, top_k: int = 3) -> List[Tuple[DocumentChunk, float]]:
        query_vec = self.model.embed(query) # Shape: (128,)
        similarities = np.dot(self.matrix, query_vec) # Cosine similarity
        top_indices = np.argsort(-similarities)[:top_k]
        results = [(self.chunks[idx], float(similarities[idx])) for idx in top_indices]
        return results

if __name__ == "__main__":
    print("=" * 70)
    print("DEMO STEP 2: VECTOR EMBEDDING & COSINE SIMILARITY SEARCH")
    print("=" * 70)

    chunks = structure_aware_chunking(SAMPLE_DOCUMENTS)
    embedder = LightweightEmbeddingModel(dim=128)
    vstore = InMemoryVectorStore(embedder)
    vstore.add_chunks(chunks)

    print(f"Indexed {len(chunks)} chunks into {vstore.matrix.shape[1]}-dimensional vector matrix.")
    print(f"Memory footprint of vectors: {vstore.matrix.nbytes} bytes (pure float32).")

    test_queries = [
        "How many days can I borrow an emergency replacement laptop?",
        "What is the maximum reimbursement for home office chair and monitor?",
        "Who do I call if my computer is stolen at the airport?"
    ]

    for q in test_queries:
        print(f"\nQUERY: \"{q}\"")
        results = vstore.search(q, top_k=2)
        for rank, (chunk, score) in enumerate(results, 1):
            print(f"  Rank #{rank} [Cosine Score: {score:0.4f}]")
            print(f"    Target: {chunk.doc_id} § {chunk.section}")
            lines = [l for l in chunk.content.splitlines() if l.strip() and not l.startswith("Document:") and not l.startswith("Section:")]
            preview = lines[0] if lines else ""
            print(f"    Excerpt: {preview[:75]}...")
        print("-" * 70)
