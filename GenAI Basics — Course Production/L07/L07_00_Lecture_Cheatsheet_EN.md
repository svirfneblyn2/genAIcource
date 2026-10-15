# 1-Page Speaker Cheatsheet • Lesson 07 (21 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: The Copilot Ecosystem — GitHub, Microsoft 365 & Local Context*  
*Slide Deck: `presentation_L07_Copilot_Ecosystem_EN.html` (PDF: `presentation_L07_Copilot_Ecosystem_EN.pdf`)*  
*Toolchain: GitHub Copilot (VS Code Agent Mode, Edits, CLI), Microsoft 365 Copilot (Word, Teams, Graph), Windows Copilot & Copilot+ PC*  
*Demo Assets: `demo_assets/` (Project Northstar: `meeting_notes_fixture.docx`, `sample_repo/`, `release_checklist.txt`)*  
*Homework: `copilot_operating_map.md` submitted to branch `feat/L07-copilot-operating-map` in `genai-homeworks`*

---

### Part 1: Ecosystem Architecture, Grounding & Trust Boundaries (00:00 — 52:00)

* **Slide 01 (00–02 min) • Title Cover:** Launching Module 3 ("Engineer's Environment"). Thesis: Copilot is not one chat bot, but an umbrella family over different data sources and runtimes. The 10/90 Axiom: model inference is 10%, grounding via Graph/Git, access trimming, and verification is 90%.
* **Slide 02 (02–05 min) • Instructor Profile:** Ihar Rubanovich (EM II & AI Ambassador @ EPAM). Verified enterprise win: **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration). Hands-on AI R&D: **Creator Tools** (AI suite for YouTube creators). Review contact: `ihar_rubanovich@epam.com`.
* **Slide 03 (05–08 min) • Curriculum Roadmap:** 16 lessons across 6 modules. Module 1 (Foundations) and Module 2 (Multimodality) are complete. Station 3: "YOU ARE HERE" — engineer workflows (L07 Copilot, L08 Data Analysis, L09 Claude & Artifacts).
* **Slide 04 (08–10 min) • Homework Protocol:** Repo structure in `genai-homeworks/L07/`. Deliverable template `copilot_operating_map.md`. Branch `feat/L07-copilot-operating-map`, Pull Request, add collaborator `ihar_rubanovich@epam.com`.
* **Slide 05 (10–14 min) • Evolution 2021–2026:** 2021 Ghost Text (Codex, local buffer) ➔ 2023 Sidebar Chat & Semantic Index (enterprise document search) ➔ 2026 Agentic Workbenches (VS Code Agent Mode, autonomous tests, MCP, Copilot Studio, on-device NPUs 40+ TOPS).
* **Slide 06 (14–18 min) • Taxonomy of Surfaces (3 Worlds):** Taxonomy table. Software Delivery (GitHub Copilot: git tree, AST, tests) ➔ Knowledge Work (M365 Copilot: mail, Teams, SharePoint) ➔ Local Device (Windows: screen, NPU, local files). Rule: select by source of truth, not brand logo.
* **Slide 07 (18–22 min) • Grounding Architecture:** C4 pipeline: Request Intercept ➔ Orchestrator ➔ Microsoft Graph & Semantic Index (vector retrieval scoped by ACL) ➔ Enriched metaprompt to LLM ➔ Enterprise Data Protection (EDP) filtering and source citations.
* **Slide 08 (22–27 min) • Microsoft 365 Boundaries:** Web / Work toggle in Copilot Chat. Office application envelopes: Outlook (email threads), Teams (meeting transcripts), Word (multi-doc synthesis), Excel (requires formatted Excel Table), PowerPoint (slide structures).
* **Slide 09 (27–31 min) • The 4 Prompt Ingredients (Microsoft Learn):** Official standard: **Goal** (action verb) + **Context** (purpose and audience) + **Source** (explicit document link via `/`) + **Expectations** (length, tone, mandatory citations).
* **Slide 10 (31–35 min) • Security & Permission Trimming:** Zero Trust by default: assistant strictly inherits user access rights. Primary deployment risk — **oversharing in SharePoint**: hidden sensitive files become instantly discoverable via Semantic Index. EDP guarantee: customer data never trains foundation models.
* **Slide 11 (35–40 min) • 4 Modes of GitHub Copilot:** 1. Inline Ghost text (`Tab`); 2. IDE Chat (`@workspace`, `@terminal`, `/fix`, `/test`); 3. Agent Mode & Copilot Edits (multi-file changes, terminal test execution with approvals); 4. Copilot CLI & Cloud PR Agents (GitHub.com reviews).
* **Slide 12 (40–44 min) • Context Engineering in IDE:** Context retrieval stack: cursor prefix/suffix ➔ open neighbor tabs ➔ repository instructions `.github/copilot-instructions.md` ➔ workspace index ➔ MCP servers.
* **Slide 13 (44–48 min) • Windows Copilot vs Copilot+ PC:** Cloud web app (PWA, datacenter processing) vs on-device NPU features (Recall — local photographic activity history, Click to Do, Studio Effects). Regional constraints (EEA vs US).
* **Slide 14 (48–52 min) • Cross-Surface Scenario (Project Northstar):** Launching VIP Free Shipping. Step 1: executive meeting decision (M365) ➔ Step 2: logic and unit tests in code (GitHub) ➔ Step 3: local workstation release checklist (Windows).

---

### Midpoint Break: 5-Minute Recharge (52:00 — 57:00)

* **Slide 15 (52–57 min) • Coffee Break:** Click "START 5 MIN". Mute microphone. *(Strictly: rest, zero chat polling!)* Prepare VS Code with `sample_repo` and Word/Markdown fixture notes.

---

### Part 2: Live Demo, Disaster Chronicles, Decision Matrix & Homework (57:00 — 90:00)

* **Slide 16 (57–63 min) • Live Demo Part 1 (M365 Copilot):** Open `meeting_notes_fixture.docx`. Apply 4-ingredient prompt. Extract VIP shipping criteria ($50 threshold), highlight open questions, verify source citations.
* **Slide 17 (63–70 min) • Live Demo Part 2 (GitHub Agent Mode):** Open `sample_repo` in VS Code. Prompt: read `ISSUE.md` and instructions, plan edits, update `shipping.py`, add tests in `test_shipping.py`. **Human Checkpoint:** inspect side-by-side diff, approve terminal command, ensure green `pytest`.
* **Slide 18 (70–75 min) • Production Chronicles (Failures vs Wins):** 4 disasters: executive salary leak via Semantic Index, destructive CLI flag execution, hallucinated npm package exploit, blind PR merge without CI. Enterprise win: **EPAM CodeMie @ Dawn Foods** (35% SDLC acceleration through standard instructions and peer review).
* **Slide 19 (75–80 min) • Decision Matrix (4 Questions):** 1. Where is the source of truth? 2. What is the permitted action? 3. What is the human checkpoint? 4. What durable evidence artifact is retained? Red Zone Blast Radius: financial transactions and unverified deployments strictly forbidden.
* **Slide 20 (80–85 min) • Homework Assignment (Copilot Operating Map):** Map 3 real-world tasks from your daily job across the matrix (Task, Surface, Context Source, Allowed Action, Human Checkpoint, Evidence, Policy). Add 1 production prompt following Microsoft's 4-ingredient standard. Benchmark: Glovo Delivery Courier or Project Northstar.
* **Slide 21 (85–90 min) • Summary & Lesson 08 Teaser:** 4 core takeaways. Open mic for Q&A. Teaser for Lesson 08 ("AI for Data Analysis & Code Interpreter"): why language models are not calculators, sandboxed Python execution, and data contract validation.
