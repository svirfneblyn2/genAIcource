# GenAI Courses Production Status Tracker

This document tracks all production assets, delivery statuses, slide decks, instructor scripts, and demo kits across both courses.

---

## 1. GenAI Basics (`GenAI Basics — Course Production`)

| Lesson | Title | Status | Slide Deck | Script / Text | Demo / Workshop | Notes |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **L01** | AI, ML and Generative AI Overview | ✅ READY (DELIVERED) | HTML (16 slides RU/EN) / Vector PDF | MD 90-Min Script & Cheatsheet (RU/EN) | Git Homework & Use-Case Memo | Complete 90-min production package with break & cases; legacy Office package removed |
| **L02** | LLM Fundamentals: Tokens, Prompting, N-shot, Context, Embeddings and Grounding | ✅ READY (DELIVERED) | HTML (25 slides RU/EN) / Vector PDF | MD 90-Min Script & Cheatsheets (RU/EN) | In-Chat Prompting Lab & Glovo Classifier Homework | 25 slides with textbook C4 diagrams, timer, homework guide & answer key; draft assets removed |
| **L03** | LLM API with Python: first call, settings, streaming, structured output, prompt patterns in code | ✅ READY (facts checked 2026-10-02) | HTML (25 slides RU/EN) / Vector PDF | MD Lecture Text, Instructor Script & Cheatsheets (RU/EN) | Colab `notebooks/L03_First_API_Call_and_Prompt_Patterns.ipynb` (+ Part1/Part2) | Colab is the source of truth; legacy OpenAI-based package (docx/pptx/demo_repo) removed 2026-10-02 |
| **L04** | Image Generation: Services, Prompt Techniques and Control Patterns | ✅ READY (SERVICES & PROMPTS REBUILD) | HTML (25 slides RU/EN) / Vector PDF | MD 90-Min Script & Cheatsheets (RU/EN), Homework (RU/EN), Research notes | Colab `notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb` + `examples/prompts.json` gallery | ChatGPT, Nano Banana, Midjourney, Kling, Grok; free-form ➔ structured prompts; edits, consistent character, product photo shoot, multi-reference; all slide images are real Nano Banana Pro generations |
| **L05** | Video Generation Models and APIs | ✅ READY (deck v3, 3 reviewers, facts checked 2026-10-12) | HTML (21 slides RU/EN) / Vector PDF | MD 90-Min Script, Cheatsheets, Demo Runbook & Homework (RU/EN) | Colab `notebooks/L05_Video_Generation_API_Pipeline.ipynb` (real Veo 3.1, paid calls off) + `demo_veo_showcase/` clips | Generator `L05/deck_v2/build.py`; lesson graph `L05_10_Lesson_Graph.md`; recheck volatile facts 24 h before class; PDFs rebuilt locally (Edge) |
| **L06** | Speech and Audio AI | ✅ READY (deck v2, 3 reviewers, facts checked 2026-10-12) | HTML (21 slides RU/EN) / Vector PDF | MD 90-Min Script (generated from deck), Cheatsheets, Homework (RU/EN), Research notes | `L06/deck_v2/make_audio.py`: real voice-over of the L05 courier video with open-weight models (Kokoro, Piper, MusicGen) + Whisper check, `demo_courier_audio/report.json` | Generator `L06/deck_v2/build.py`; lesson graph `L06_10_Lesson_Graph.md`; old Drive package (STT-only docx/pptx) superseded; recheck volatile facts 24 h before class; PDFs built locally (Edge) |
| **L07** | The Microsoft Copilot Ecosystem: an Overview | ✅ READY (deck v3, overview rebuild, facts as of 2026-10-13) | HTML (20 slides RU/EN) / Vector PDF | MD 90-Min Script (generated from deck), Cheatsheets, Demo Runbook & Homework with answer key (RU/EN), Research notes | `L07/demo_courier_copilot/`: meeting notes, release checklist, `orders.csv` (12 synthetic orders), fallbacks; live demos in free Copilot Chat (IT Park school account) + personal Copilot (image, Vision) | Generator `L07/deck_v3/build.py` (+ `make_docs.py`); replaces GitHub-centric v2 (kept in folder); four-zone map, real screenshots (own captures 2026-10-13, official Microsoft/GitHub, credited YouTube frames) instead of mockups; free tools only, synthetic data; recheck volatile facts before recording (`README_v3.md`); expect changes after Ignite 17–20 Nov 2026 |
| **L08** | AI for Data Analysis | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L09** | Claude Ecosystem and Artifacts | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L10** | Open Models, LM Studio, Local Inference & RunPod | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L11** | Function Calling and Building Your First Agent | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L12** | MCP, Tools and Agent Frameworks | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L13** | Custom GPTs, Responses API and Agents SDK | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L14** | Streamlit and Rapid AI Prototyping | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L15** | Responsible AI, Security and Regulation | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |
| **L16** | Agentic Software Development: Coding Agents, IDEs | ⏳ PLANNED | Google Drive | Google Drive | — | On G: Drive |

---

## 2. Advanced GenAI (`Advanced GenAI — Course Production`)

| Module | Title | Status | Slide Deck | Script / Text | Demo / Code | Notes |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **M01** | Cloud AI Capabilities Overview | ✅ READY | HTML / Vector PDF (Deck Builder) | DOCX / MD Click-Guide & Homework | — | 27 slides, strict validation |
| **M02** | Agent Frameworks and Orchestration | ✅ READY | HTML / Vector PDF (Deck Builder) | DOCX / MD Click-Guide & Homework | `m02_live_demo_package/` + Zip | State machines, multi-agent topologies |
| **M03** | Vector Stores and RAG | ✅ READY | HTML / Vector PDF (Deck Builder) | DOCX / MD Lecture Text & Full Script | `m03_live_demo/` + Zip | 26 slides, HNSW, BM25 hybrid search |
| **M04** | Agentic Development Tools and Coding Workflows | ⏳ READY (Drive) | Google Slides | Google Docs | Demo Assets on Drive | On G: Drive |
| **M05** | LLM Evaluation, Tracing and Observability | ⏳ READY (Drive) | Google Slides | Google Docs | Drive | On G: Drive |
| **M06** | Building Production Agents | ⏳ READY (Drive) | Google Slides | Google Docs | Drive | On G: Drive |
| **M07** | MCP Deep Dive | ⏳ IN PROGRESS | Google Slides | Google Docs | Drive | In progress on G: Drive |
