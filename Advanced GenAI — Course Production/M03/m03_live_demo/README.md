# Module 03: Live Demo Kit — Vector Stores & Enterprise RAG

A 100% local, transparent, zero-cost reference implementation designed for classroom and workshop demonstration.

## Features
- **Zero API keys required**: Runs completely offline without OpenAI, AWS, Azure, or Pinecone credits.
- **Zero heavy dependencies**: Pure Python standard library + NumPy.
- **Microsecond execution**: Entire 4-step pipeline completes in under 2 seconds.

## File Map
- `01_chunking.py`: Contrasts naive character chunking against structure-aware markdown parsing with security metadata.
- `02_vector_search.py`: Demonstrates L2-normalized dense embeddings and vectorized cosine similarity matrix multiplication.
- `03_hybrid_and_filter.py`: Demonstrates role-based access control (ACL) pre-filtering and Reciprocal Rank Fusion (RRF) between Dense Vector and BM25 Sparse Lexical search.
- `04_grounded_generation.py`: Demonstrates context assembly, anti-hallucination prompt guardrails, and inline citation synthesis (`[Source: doc_id § section]`).
- `run_demo.py`: One-click master script that orchestrates the entire pipeline for the live audience.

## Quickstart
```bash
python run_demo.py
```
