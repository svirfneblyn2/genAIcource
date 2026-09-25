"""
Master Demo Runner: End-to-End Enterprise RAG Pipeline in 4 Acts.

Usage:
    python run_demo.py
"""

import sys
import os
import time

def banner(title: str, step_num: int):
    print("\n" + "=" * 75)
    print(f"  ACT {step_num}: {title.upper()}")
    print("=" * 75)

def main():
    print("""
===========================================================================
  ADVANCED GENAI - MODULE 03 LIVE DEMO: VECTOR STORES & ENTERPRISE RAG
  A zero-cost, transparent, local reference implementation in Python
===========================================================================
    """)

    # ACT 1
    banner("Structure-Aware Parsing vs Naive Chunking", 1)
    print("Demonstrating how splitting text without heading awareness destroys context...")
    time.sleep(0.5)
    from importlib import import_module
    import importlib.util

    spec1 = importlib.util.spec_from_file_location("c_mod", os.path.join(os.path.dirname(__file__), "01_chunking.py"))
    c_mod = importlib.util.module_from_spec(spec1)
    spec1.loader.exec_module(c_mod)

    chunks = c_mod.structure_aware_chunking(c_mod.SAMPLE_DOCUMENTS)
    print(f"[OK] Parsed {len(c_mod.SAMPLE_DOCUMENTS)} enterprise policies into {len(chunks)} structure-aware chunks.")
    print("Each chunk is enriched with doc_id, section title, and access control tags (ACL).")

    # ACT 2
    banner("Vector Embedding & Cosine Similarity Matrix", 2)
    print("Projecting text into 128-dimensional L2-normalized dense space...")
    time.sleep(0.5)
    spec2 = importlib.util.spec_from_file_location("v_mod", os.path.join(os.path.dirname(__file__), "02_vector_search.py"))
    v_mod = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(v_mod)

    embedder = v_mod.LightweightEmbeddingModel(dim=128)
    vstore = v_mod.InMemoryVectorStore(embedder)
    vstore.add_chunks(chunks)
    print(f"[OK] In-memory vector store populated: {vstore.matrix.shape[0]} vectors x {vstore.matrix.shape[1]} dims.")
    print(f"[OK] Memory footprint: {vstore.matrix.nbytes} bytes. Similarity is computed via single matrix dot-product.")

    # ACT 3
    banner("Security Boundary Filtering + Hybrid RRF Fusion", 3)
    print("Executing query under role-based security filters and combining Dense + BM25...")
    time.sleep(0.5)
    spec3 = importlib.util.spec_from_file_location("h_mod", os.path.join(os.path.dirname(__file__), "03_hybrid_and_filter.py"))
    h_mod = importlib.util.module_from_spec(spec3)
    spec3.loader.exec_module(h_mod)

    engine = h_mod.HybridSearchEngine(chunks)
    query = "Where do I pick up the emergency loan in Room B12?"
    print(f"Query: \"{query}\"")
    results = engine.search_with_filter(query, user_role="employee", top_k=2)

    print("\n[Retrieval Results after Reciprocal Rank Fusion]:")
    for r, (c, score, bdown) in enumerate(results, 1):
        print(f"  #{r}: [{c.doc_id}] § {c.section} (RRF: {score:.5f}) [{bdown}]")

    # ACT 4
    banner("Context Assembly & Grounded Citation Generation", 4)
    print("Packing evidence into prompt context with anti-hallucination guardrails...")
    time.sleep(0.5)
    spec4 = importlib.util.spec_from_file_location("g_mod", os.path.join(os.path.dirname(__file__), "04_grounded_generation.py"))
    g_mod = importlib.util.module_from_spec(spec4)
    spec4.loader.exec_module(g_mod)

    ans = g_mod.simulate_grounded_inference(query, results)
    print("\n[Synthesized Grounded Response]:")
    print(ans)

    print("\n" + "=" * 75)
    print("  DEMO COMPLETE: All 4 enterprise RAG stages executed successfully!")
    print("===========================================================================\n")

if __name__ == "__main__":
    main()
