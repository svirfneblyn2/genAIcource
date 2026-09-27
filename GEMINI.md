# GenAI Course Production — Engineering Rules & Architecture Standards

This repository houses the production materials for the **GenAI Basics** and **Advanced GenAI** enterprise curricula. All content is engineered for technical professionals: software developers, QA engineers, DevOps, technical leads, and solutions architects.

---

## 1. Core Engineering Philosophy

* **The 10/90 Axiom:** The foundation model is only 10% of a production system. The remaining 90% is data contracts, schema validation, rate-limiting, PII filtering, fallback orchestration, and observability.
* **Problem First, Not AI First:** If a problem can be solved deterministically with SQL, code, or mathematics (Software 1.0), solve it there ($0 cost, 0ms latency, 100% accuracy). If it is structured tabular data, use Classical ML (Software 2.0). Only introduce Generative AI (Software 3.0) for unstructured semantic reasoning.
* **Wrap 1.0 around 3.0:** Production GenAI systems wrap the strict deterministic guardrails of Software 1.0 around the probabilistic core of Software 3.0.

---

## 2. Voice, Tone & Content Policy ("No Fluff, No AI-ness")

* **Target Audience:** EPAM Systems engineers and senior technologists.
* **Strictly Prohibited:** Marketing fluff, generic buzzwords, robotic excitement ("In today's fast-paced digital era...", "AI is revolutionizing everything...").
* **Required Standard:** Direct, dense, technical, and objective (style of OpenAI Developer Guides and Andrej Karpathy's lectures).
* **Technical Rigor:** Always explain the physical mechanism:
  - Models see **BPE tokens** and integer IDs, not words or characters.
  - Inference is **autoregressive** and metered per 1M tokens.
  - **Temperature = 0.0** (Greedy Decoding) is mandatory for JSON schemas, code generation, and structured outputs.
  - Hallucination is standard probabilistic sampling in the absence of authoritative context; accuracy requires **RAG grounding**.
  - Enforce **Blast Radius** boundaries: Green (autonomous drafts), Yellow (Human-in-the-Loop co-pilots), Red (financial/DB actions strictly forbidden for direct LLM execution).

---

## 3. Instructor Profile & Corporate Compliance

* **Instructor Name:** Igor Rubanovich / Ihar Rubanovich (`ihar_rubanovich@epam.com`).
* **Title:** Engineering Manager II & AI Ambassador @ EPAM Systems.
* **Creator Tools Phrasing (CRITICAL):**
  - **DO NOT** describe him as "Founder" or "Co-Founder" of Creator Tools. As a corporate engineering manager, external founder titles create IP, moonlighting, and employment compliance conflicts.
  - **ALWAYS** describe it as **Hands-on AI R&D / Engineering Pet-Project**:
    - *RU:* `Практический AI R&D: Архитектор и разработчик Creator Tools — AI-пайплайн перевода и локализации видео на 140+ языков мира.`
    - *EN:* `Hands-on AI R&D: Creator and architect of Creator Tools — AI platform for video translation and localization across 140+ languages.`
* **Authentic Case Studies:** Always anchor enterprise wins on the instructor's verified delivery track record: **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration in feature development, unit testing, and architectural documentation).

---

## 4. Slide Deck Architecture (21-Slide Standard)

Every 90-minute lecture deck must follow this battle-tested 21-slide flow:
1. **Slide 01 (Title Cover):** Clean, commanding, centered hero. Pure topic title, subtitle, lead, and the 10/90 axiom quote box. **DO NOT** place instructor cards or logistics on Slide 01.
2. **Slide 02 (Instructor Profile):** Photo, professional credentials, hands-on R&D experience, and official homework email.
3. **Slide 03 (Curriculum Roadmap):** Full 16-lesson roadmap across 6 modules.
4. **Slide 04 (GitHub Workflow):** Repository tree (`genai-homeworks/` ➔ `L01/`, `L02/`), branch rules, and collaborator invitation.
5. **Slide 05 (Real-World Systems):** Everyday consumer systems demonstrating diverse underlying math (CV, classical ML, graph algorithms, embeddings, transformers).
6. **Slide 06 (Taxonomy):** Matryoshka doll hierarchy: AI ➔ ML ➔ DL ➔ GenAI.
7. **Slide 07 (Classical ML):** C4 architecture: tabular $X 	o Y$, XGBoost, 2-5ms latency, $0 cost, calibrated probability.
8. **Slide 08 (Generative AI):** C4 architecture: prompt + Foundation Model, autoregression, latency, token costs, hallucination risk.
9. **Slide 09 (Software Paradigms):** Karpathy 1.0 (code) ➔ 2.0 (weights) ➔ 3.0 (prompts).
10. **Slide 10 (Hype Trap):** Anti-pattern of using LLMs for deterministic SQL/math. Problem-First principle.
11. **Slide 11 (Task Spectrum):** 4 real-world problems mapped to 4 technology worlds (Deterministic, ML, GenAI, MCP Agent).
12. **Slide 12 (Tokenization):** BPE mechanics, vocabulary IDs, Unicode/Cyrillic fragmentation, cost per 1M tokens.
13. **Slide 13 (Model Physics):** Next-token probability distribution, greedy decoding vs temperature sampling.
14. **Slide 14 (Hallucinations vs RAG):** Parametric memory fabrication vs authoritative retrieval grounding.
15. **Slide 15 (Midpoint Break):** 5-minute interactive countdown timer, coffee recharge, and chat crowdsourcing.
16. **Slide 16 (Architectural Iceberg):** 10% API call vs 90% production engineering (Pydantic, 429 retries, PII, latency).
17. **Slide 17 (Blast Radius):** Green / Yellow / Red traffic light governance matrix.
18. **Slide 18 (Production Chronicles):** 4 catastrophic industry failures vs 4 enterprise wins (EPAM CodeMie @ Dawn Foods).
19. **Slide 19 (Decision Tree):** 4-question evaluation framework + live analysis of student submissions from the break.
20. **Slide 20 (Homework Assignment):** 300-500 word Use-Case Memo + concrete relatable benchmark (e.g. Glovo Food Delivery Courier).
21. **Slide 21 (Q&A & Next Session):** Key takeaways, open mic, and teaser for next lesson.

---

## 5. Visuals & Zero-Clipping Layout Rules

* **Color Palette:** C4 Architectural Theme (`#0b0f17` background, `#1e293b` surfaces, `#38bdf8` cyan primary, `#10b981` emerald, `#f59e0b` amber, `#ef4444` red).
* **Image Generation:** NEVER use the IDE default tool. ALWAYS use Vertex AI (`gemini-3-pro-image` / Nano Banana Pro) via `tools/image_generator.py`.
* **Diagram Typography:** Always render schematics and infographics with English typography to prevent rendering artifacts and maintain international presentation standards.
* **Flexbox Layout (Anti-Clipping):**
  - Slides with full-height diagrams must use `.slide-page.visual-slide`.
  - `.slide-page` and `.slide-content-arena` must enforce `min-height: 0; max-height: 100%; overflow: hidden;`.
  - Images must use `object-fit: contain; max-height: 100%; max-width: 100%;`.

---

## 6. Bilingual Deliverable Standard

Every lesson must maintain 100% parity across two language suites:
* **Interactive HTML Decks:** `presentation_LXX_*.html` (RU) and `presentation_LXX_*_EN.html` (EN) with native keyboard controls (`←`/`→`, `Space`, `N`, `G`, `F`), notes drawer, and timer.
* **Multi-page Vector PDFs:** Compiled via headless Edge with zero margins.
* **90-Minute Instructor Scripts:** `LXX_02_Instructor_Script_90MIN.md` and `_EN.md`.
* **1-Page Speaker Cheatsheets:** `LXX_00_Lecture_Cheatsheet.md` and `_EN.md`.
