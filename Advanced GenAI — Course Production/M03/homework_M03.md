# Module 03 Homework Assignment: Enterprise RAG Architecture & Grounded Retrieval Engine

**Course:** Advanced Generative AI for Engineers  
**Module 03:** Vector Stores and RAG: From Embeddings and Indexes to Grounded, Measurable Retrieval  
**Format:** 1 Architecture Specification Document (PDF or Markdown) OR 1 Local Python Repository with Runnable Demo  
**Cost Guarantee:** **$0.00 (Zero financial cost guaranteed)**. No paid cloud accounts, GPUs, or vector DB subscriptions required.

---

## Business Scenario

You are the Lead Retrieval Engineer for **Apex Global Logistics**. The organization operates across 14 countries with 18,000 employees. Currently, employees struggle to find accurate company policies regarding travel expenses, equipment loans, remote work, and incident reporting.

A previous naive prototype built with standard character-count chunking and pure vector search suffered from critical failures:
1. **Security Leakage**: Regular interns received answers citing confidential C-suite executive hardware compensation policies.
2. **Hallucination on Unanswered Questions**: When asked about pet policies or tuition reimbursement, the model fabricated plausible-sounding allowances instead of refusing.
3. **Keyword Misses**: Searching for specific room numbers or policy identifiers (such as `"Room B12"` or `"POL-SEC-402"`) returned irrelevant paragraphs because semantic embeddings blurred exact alphanumeric codes.
4. **Unverifiable Claims**: Answers contained fluent advice but omitted exact document IDs, section headers, or revision dates.

Your mission is to design (Track A) or implement (Track B) a production-grade, grounded RAG solution that resolves these four failure modes.

---

## Choose Your Track (Equal Weight: 100 Points)

Students may choose **Track A** (Architecture & Evaluation) or **Track B** (Python Implementation). Both tracks receive equal grading weight.

---

### Track A: Architecture & Evaluation Design (No Coding Required)
*Target Audience: System Architects, Technical Product Managers, Solution Consultants.*

#### Deliverables:
1. **End-to-End System Topology Diagram (Mermaid or Draw.io)**:
   - Must explicitly separate the **Offline Ingestion Lane** (document parsing, structure-aware chunking, metadata extraction, embedding generation, vector/lexical index storage) from the **Online Request Lane** (user query, auth identity lookup, pre-filtering, hybrid retrieval, fusion/reranking, context assembly, LLM inference, citation verifier).
2. **Chunking & Metadata Strategy Matrix**:
   - Define your chunking algorithm for complex policies containing tables and bullet lists.
   - Specify the exact metadata schema attached to each chunk (`doc_id`, `section_id`, `version`, `effective_date`, `allowed_roles`).
   - Detail whether metadata filtering occurs **Pre-Retrieval** (in index query) or **Post-Retrieval**, and justify the latency/recall trade-off.
3. **Hybrid Search & Fusion Specification**:
   - Formulate the mathematical scoring method: Dense Bi-Encoder + Sparse BM25 combined via Reciprocal Rank Fusion (RRF) with constant $k=60$.
   - Explain why pure vector search fails on alphanumeric codes and how lexical indexing mitigates this.
4. **Context Window & Citation Guardrails Protocol**:
   - Define how chunks are positioned in the prompt (Primacy vs Recency) to mitigate the "Lost in the Middle" attention degradation.
   - Specify the exact prompt system instructions that enforce `[Source: DOC-ID § Section]` citations and require deterministic refusal on out-of-domain queries.
5. **Ragas / TruLens Evaluation Plan**:
   - Provide a 10-question evaluation dataset containing:
     - 4 standard factual queries.
     - 2 role-restricted queries (testing ACL filtering).
     - 2 exact-match alphanumeric queries (testing BM25 keyword recall).
     - 2 out-of-domain unanswerable queries (testing anti-hallucination refusal).
   - Define the pass/fail thresholds for **Context Recall**, **Faithfulness**, and **Answer Relevance**.

---

### Track B: Working Local Python Prototype (Coding Track)
*Target Audience: Software Engineers, Machine Learning Engineers, Backend Developers.*

#### Deliverables:
1. **Runnable Python Project**:
   - Clean, modular repository (`chunking.py`, `vector_store.py`, `retriever.py`, `generator.py`, `main.py`).
   - Runs 100% locally with zero external API fees (using pure NumPy, SQLite, ChromaDB, or free-tier local embeddings via Ollama or Hugging Face).
2. **Key Capabilities Demonstrated in Code**:
   - **Structure-Aware Chunking**: Preserves markdown section headers and associates metadata tags with every chunk.
   - **Security Pre-Filtering**: Simulates user role access checks before retrieval.
   - **Hybrid Retrieval**: Combines semantic similarity scores with keyword matching (BM25 or token overlap) using RRF.
   - **Grounded Prompt Assembly**: Injects retrieved evidence with explicit citation anchors into a formatted prompt.
   - **Refusal Test**: Demonstrates that unsupported queries return an explicit "Insufficient evidence" message rather than hallucinating.
3. **Execution Script & README**:
   - One-command execution verifying both supported and out-of-scope query paths.

---

## 100-Point Grading Rubric

| Assessment Criterion | Weight | Excellent (Full Credit) | Developing (Partial Credit) | Inadequate (Zero) |
| :--- | :---: | :--- | :--- | :--- |
| **1. Chunking & Ingestion Quality** | **20 pts** | Preserves heading paths and table structure; prevents mid-sentence breaks; attaches full metadata schema. | Chunks arbitrary character counts with fixed overlap; loses section headings. | Dumps raw entire documents into context without chunking. |
| **2. Security & Metadata Filtering** | **20 pts** | Implements hard pre-retrieval access control; verifies confidential documents never leak to unauthorized roles. | Post-retrieval filtering only, risking empty result sets; partial ACL schema. | No access control boundary; all documents readable by all users. |
| **3. Hybrid Search & Ranking** | **20 pts** | Correctly combines Dense vector search with BM25 keyword matching using RRF or convex weighting; handles exact codes. | Pure dense vector search only; fails on alphanumeric queries like room/code numbers. | Simple substring matching or random vector scoring. |
| **4. Context Assembly & Citations** | **20 pts** | Formats evidence items with unique IDs; positions evidence to mitigate Lost-in-the-Middle; enforces strict `[Source: ID § Section]` inline tags. | Citations present but vague (e.g. mentions policy name without section or chunk ID); loose prompt rules. | Generates prose answers with zero citations or evidence attribution. |
| **5. Anti-Hallucination & Evaluation** | **20 pts** | Explicit refusal path on out-of-domain questions; defines concrete evaluation dataset with recall and faithfulness metrics. | Weak refusal instructions; model occasionally speculates on ungrounded queries; minimal evaluation plan. | Model invents answers to out-of-scope questions; zero evaluation metrics defined. |
| **TOTAL** | **100 pts** | **Passing Benchmark: 80 / 100** | | |

---

## Submission Guidelines
- Submit a single ZIP archive or public GitHub repository link.
- Include a 2-page design PDF (Track A) or a runnable README with terminal execution output (Track B).
- Deadline: 7 calendar days from session delivery.
