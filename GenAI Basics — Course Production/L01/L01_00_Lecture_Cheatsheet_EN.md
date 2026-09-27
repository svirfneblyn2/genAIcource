# Speaker Cheatsheet (1-Page) • Lesson 01 (21 Slides • 90 Minutes)
*Instructor: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*

---

### Part 1: Foundations, Taxonomy & Model Physics (00:00 — 55:00)

* **Slide 01 (00-03 min) • Title Cover:** Engineering sobriety. Chat poll: who has integrated LLMs in code (1 or 2)? Model = 10%, engineering = 90%.
* **Slide 02 (03-06 min) • Instructor:** Ihar Rubanovich (EM II & AI Ambassador @ EPAM; R&D Creator Tools — AI tools for YouTube creators; email: `ihar_rubanovich@epam.com`).
* **Slide 03 (06-09 min) • Roadmap:** 16 lessons, 6 modules. *Positioning:* foundational track — systemic vision, mental models, baseline practice. No false overpromising.
* **Slide 04 (09-12 min) • GitHub:** Folder tree (`genai-homeworks/` ➔ `L01/`, `L02/`), invite `ihar_rubanovich@epam.com` as Collaborator.
* **Slide 05 (12-16 min) • Real-World AI:** FaceID (CV), Gmail (ML), YouTube (embeddings), GPS (graphs), Copilot (LLM), Creator Tools (AI tools for creators).
* **Slide 06 (16-19 min) • Taxonomy:** Matryoshka doll: AI (umbrella) ➔ ML (data patterns) ➔ DL (neural nets) ➔ GenAI (synthesis). 80% tasks solved in outer layers.
* **Slide 07 (19-24 min) • Classical ML (Diagram):** X (table) + Y (target) ➔ Training (XGBoost) ➔ P(churn)=0.84 (2-5ms, $0, calibrated probability).
* **Slide 08 (24-29 min) • Generative AI (Diagram):** Prompt + Foundation Model ➔ Autoregression token by token (seconds latency, token costs, hallucination risk).
* **Slide 09 (29-33 min) • Karpathy Paradigms:** Software 1.0 (logic code) ➔ 2.0 (weights from data) ➔ 3.0 (prompts in natural language). Wrap 1.0 around 3.0!
* **Slide 10 (33-37 min) • The Hype Trap:** 2ms free deterministic SQL vs 3s $0.03 LLM with 5% arithmetic errors. "Problem First" mindset.
* **Slide 11 (37-42 min) • 4 Tasks & 4 Worlds:** VAT calc (code, $0) | Churn prediction (ML) | 50-ticket summary (LLM) | k8s rollback (Agent + Human-in-the-Loop).
* **Slide 12 (42-46 min) • Tokenization (Infographic):** Models see subword tokens and IDs via BPE. Billed per 1M tokens. Non-English text fragments more.
* **Slide 13 (46-50 min) • Autoregression & Probabilities:** Next-token probability distribution. Temp=0.0 (strict JSON/code) vs Temp=0.8 (creative variety).
* **Slide 14 (50-55 min) • Hallucinations vs RAG:** Ungrounded generation from weights vs Grounded synthesis from authoritative knowledge chunks.

---

### ☕ Midpoint: 5-Minute Break (55:00 — 60:00)

* **Slide 15 • Live Timer:**  
  *Click '▶ Start 5 Min' button on slide.* Prompt: "Grab coffee and stretch for 5 minutes before Part 2." *(No chat task—routine task belongs in homework!)*

---

### Part 2: Production Engineering, Case Studies & Homework (60:00 — 90:00)

* **Slide 16 (60-65 min) • Architectural Iceberg:** 10% above waterline (API call) vs 90% below (Pydantic, 429 retries, PII, token budget, UX).
* **Slide 17 (65-70 min) • Blast Radius (Traffic Light):** 🟢 Green (drafts, 0 risk) ➔ 🟡 Yellow (Co-pilot, one-tap approval) ➔ 🔴 Red (financial/DB, no direct autonomy).
* **Slide 18 (70-76 min) • 4 Failures vs 4 Wins:** Air Canada (court ruling); Tahoe for $1; DPD (curses); fake precedents vs **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration), Copilot, Stripe, Morgan Stanley.
* **Slide 19 (76-80 min) • Decision Tree:** 4 questions: Deterministic? Meaning? Error cost? Source of truth? *Walkthrough with standard examples.*
* **Slide 20 (80-85 min) • Homework Assignment #1:** Use-Case Memo (300-500 words in Markdown). *Audit a real routine from your daily work.* **Benchmark: Glovo Courier** (routing = graph/ML, messaging = GenAI, one-tap courier confirmation, taboo = no refunds/cancellations). Add `ihar_rubanovich@epam.com`.
* **Slide 21 (85-90 min) • Q&A & Lesson 02 Teaser:** In Lesson 02 — BPE tokenization, context window, embeddings, and structured prompting. Open mic!
