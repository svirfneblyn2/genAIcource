# Lesson 07: Comprehensive 90-Minute Instructor Script (21 Slides)
**Course:** GenAI Basics • Module 3: Engineer's Environment & Analytics • Lesson 07 of 16  
**Instructor:** Ihar Rubanovich (Engineering Manager II & AI Ambassador, EPAM Systems)  
**Homework Review Email:** `ihar_rubanovich@epam.com`  
**Slide Deck:** `presentation_L07_Copilot_Ecosystem_EN.html` (21 Interactive Slides)  

---

## 90-Minute Lesson Schedule

| Section | Timing | Slides | Thematic Focus |
| :--- | :---: | :---: | :--- |
| **Block 1: Welcome & Logistics** | 00:00 — 10:00 (10 min) | 01 – 04 | Engineering sobriety, instructor background, 16-lesson roadmap (launching Module 3), Git rules |
| **Block 2: Copilot Architecture** | 10:00 — 27:00 (17 min) | 05 – 08 | Evolution 2021–2026, 3-world taxonomy, C4 Grounding, M365 envelopes (Web vs Work) |
| **Block 3: Prompting, Security & IDE** | 27:00 — 52:00 (25 min) | 09 – 14 | Microsoft Learn 4 Ingredients, Permission Trimming, GitHub 4 Modes, IDE context stack, Project Northstar |
| **Midpoint Break** | 52:00 — 57:00 (5 min) | 15 | 5-minute interactive timer, cognitive recharge, coffee refill (strictly zero chat polling!) |
| **Block 4: Hands-On Live Demos** | 57:00 — 70:00 (13 min) | 16 – 17 | Demo 1: M365 Copilot (4-ingredient brief); Demo 2: VS Code Agent Mode (code, unit tests, diff) |
| **Block 5: Production Reality & Decisions** | 70:00 — 80:00 (10 min) | 18 – 19 | 4 industry disasters vs EPAM CodeMie @ Dawn Foods win (35% SDLC acceleration), Decision Matrix |
| **Block 6: Homework & Wrap-Up** | 80:00 — 90:00 (10 min) | 20 – 21 | Operating Map deliverable walkthrough, Glovo benchmark, open mic Q&A, Lesson 08 teaser |

---

## Slide-by-Slide Instructor Spoken Script

### Slide 01: Title Cover (The Copilot Ecosystem)
- **Timing:** 00:00 — 02:00 (2 min)
- **Objective:** Strip away marketing buzzwords and establish a rigorous architectural perspective.
- **Spoken Script:**
  > "Welcome, everyone! Today we inaugurate Module 3 of GenAI Basics.  
  > Lesson 07 is titled: 'The Copilot Ecosystem: GitHub, Microsoft 365 & Local Context'.  
  > We will not be treating Copilot as a conversational chatbot for writing poetry. Today, we inspect Copilot strictly through the lens of systems engineering.  
  > Notice the 10/90 Axiom displayed on your screen: calling the large language model is only 10% of the architecture. The remaining 90% is where authoritative context lives, how permissions are trimmed, and how humans verify outputs before persistent commits.  
  > Our mission today is to equip you with an infallible mental model: how to choose the right surface for the right task and enforce strict trust boundaries."

---

### Slide 02: Instructor Profile (Ihar Rubanovich)
- **Timing:** 02:00 — 05:00 (3 min)
- **Objective:** Reiterate delivery credentials and official homework submission contacts.
- **Spoken Script:**
  > "Briefly introducing myself: I am Ihar Rubanovich, Engineering Manager II and AI Ambassador at EPAM Systems.  
  > My core focus is AI-assisted software engineering. On our delivery engagements for global manufacturer Dawn Foods, systemic deployment of our coding platform EPAM CodeMie achieved 35% SDLC acceleration across feature implementation, unit testing, and architectural documentation.  
  > In my hands-on AI R&D lab, I build and architect Creator Tools — an engineering suite of AI tools for YouTube creators designed to optimize production workflows.  
  > Please note the official address on your screen: `ihar_rubanovich@epam.com`. This is the email you will invite as a GitHub collaborator when opening Pull Requests for homework reviews."

---

### Slide 03: Curriculum Roadmap (16 Lessons • 6 Modules)
- **Timing:** 05:00 — 08:00 (3 min)
- **Objective:** Mark curriculum milestone: Module 1 & 2 complete, entering Module 3.
- **Spoken Script:**
  > "Looking across our 16-lesson roadmap:  
  > • Module 1 gave us foundation mechanics: tokens, greedy decoding, prompt patterns, and Python SDK calls;  
  > • Module 2 covered multimodality across images, video diffusion, and neural audio.  
  > Today we reach Station 3: 'Engineer's Environment'. Module 3 centers on tools integrated directly into your daily developer workflow.  
  > Today is the Copilot ecosystem. In Lesson 08, we dive into AI for Data Analysis and Code Interpreter. In Lesson 09, we master the Claude workbench and interactive Artifacts. Ahead lie local open-source LLMs in Module 4 and autonomous agents with MCP in Module 5."

---

### Slide 04: Homework Protocol & Git Process
- **Timing:** 08:00 — 10:00 (2 min)
- **Objective:** Outline the required homework structure and pull request flow.
- **Spoken Script:**
  > "All homework submissions follow standard engineering practices:  
  > In your `genai-homeworks` repository, create directory `L07/`.  
  > Work inside dedicated branch `feat/L07-copilot-operating-map`.  
  > Your primary deliverable is `copilot_operating_map.md` — an Operating Map where you analyze 3 real-world tasks across our governance matrix.  
  > We evaluate rigorous human checkpoints and durable evidence artifacts, not conversational claims."

---

### Slide 05: Evolution of Copilot (2021 — 2026)
- **Timing:** 10:00 — 14:00 (4 min)
- **Objective:** Show the technical transition from inline autocomplete to agentic workbenches.
- **Spoken Script:**
  > "Let's trace how developer assistants transformed over five years.  
  > In 2021, GitHub Copilot was Codex predicting grey inline text accepted by pressing Tab. It was a high-speed typist.  
  > In 2023–2024, sidebar chat appeared alongside Semantic Index in Microsoft Graph. The assistant became a conversational advisor.  
  > By 2026, Copilot has evolved into an agentic orchestration workbench: VS Code Agent Mode executes multi-file edits and terminal tests; MCP servers connect private databases; on-device NPUs in Copilot+ PCs process real-time tasks locally.  
  > Stating 'I do this in Copilot' means nothing without specifying the context boundary and runtime permissions."

---

### Slide 06: Taxonomy of Surfaces (Three Worlds)
- **Timing:** 14:00 — 18:00 (4 min)
- **Objective:** Cement the primary architectural rule: select by source of truth.
- **Spoken Script:**
  > "Here is our core taxonomy. Memorize this golden rule: select your assistant surface by where authoritative truth lives, never by brand logo.  
  > World 1 is Software Delivery: GitHub Copilot. Its source of truth is the git repository, code AST, and test suites.  
  > World 2 is Knowledge Work: Microsoft 365 Copilot. Its source of truth is Microsoft Graph — emails, Teams channels, and SharePoint documents.  
  > World 3 is Local Device: Windows Copilot and Copilot+ PC. Its truth is the screen frame, clipboard, and local NPU.  
  > If your goal is refactoring a class, opening M365 Copilot is useless — it cannot see your git repository. If your goal is extracting executive meeting decisions, GitHub Copilot is blind — it cannot access Teams transcripts."

---

### Slide 07: Grounding Architecture (C4 Diagram)
- **Timing:** 18:00 — 22:00 (4 min)
- **Objective:** Explain Dynamic RAG and the Microsoft Graph pipeline.
- **Spoken Script:**
  > "How does enterprise data safely enter the model?  
  > Foundation models are never trained on your company's data. Every query is a Dynamic RAG pipeline:  
  > Step 1: The user submits a prompt. The orchestrator intercepts it and injects Entra ID authentication tokens.  
  > Step 2: The orchestrator queries Microsoft Graph. Semantic Index vector-searches relevant document chunks strictly within the user's ACL access rights.  
  > Step 3: An augmented metaprompt is constructed: user prompt + retrieved authoritative document excerpts + strict formatting instructions.  
  > Step 4: The model infers an answer, passes Purview DLP checks, attaches source citations, and returns to the user. Enterprise Data Protection guarantees customer data never trains public foundation models."

---

### Slide 08: Microsoft 365 Boundaries & In-App Envelopes
- **Timing:** 22:00 — 27:00 (5 min)
- **Objective:** Highlight the Web/Work toggle and application-specific constraints.
- **Spoken Script:**
  > "Pay close attention to the Web versus Work toggle in Copilot Chat.  
  > When set to Web, the model searches the open public internet. It cannot see a single byte of company files! Inquiries about internal projects in Web mode trigger hallucinations.  
  > Set to Work, it grounds in your tenant's Graph data.  
  > Furthermore, applications impose unique prerequisites: Teams meeting recaps require enabled transcription; Excel data analysis requires tabular data explicitly formatted as an official Excel Table."

---

### Slide 09: The 4 Prompt Ingredients (Microsoft Learn)
- **Timing:** 27:00 — 31:00 (4 min)
- **Objective:** Teach the Microsoft Learn four-ingredient prompting formula.
- **Spoken Script:**
  > "Microsoft Learn formalizes enterprise prompting into four mandatory ingredients:  
  > 1. Goal: An unambiguous action verb — 'Draft a structured brief', not 'Help me with this'.  
  > 2. Context: Business rationale and target audience — 'For Tier-1 customer support agents ahead of our weekend release'.  
  > 3. Source: Explicit authoritative documents referenced via `/` — 'Rely strictly on attached meeting_notes_fixture.docx'. Specifying the source eliminates 95% of hallucinations!  
  > 4. Expectations: Format, tone, length constraints, and mandatory paragraph citations.  
  > Omitting any of these four degrades output consistency."

---

### Slide 10: Security & Permission Trimming (The Oversharing Risk)
- **Timing:** 31:00 — 35:00 (4 min)
- **Objective:** Explain how Permission Trimming exposes poor data hygiene.
- **Spoken Script:**
  > "Copilot operates under strict Zero Trust: it inherits the user's existing permissions (Permission Trimming). If you cannot open a folder, Copilot cannot read it.  
  > However, this reveals the #1 risk of enterprise rollouts: oversharing.  
  > Before AI, an executive compensation spreadsheet set to 'Everyone in Company' sat undisturbed for years because nobody had the direct URL.  
  > But semantic search finds files by meaning! If a junior employee asks Copilot 'What compensation changes are planned?', the model retrieves the file immediately.  
  > The lesson is clear: deploying Copilot requires auditing SharePoint access controls and configuring Purview Sensitivity Labels beforehand."

---

### Slide 11: 4 Operating Modes of GitHub Copilot
- **Timing:** 35:00 — 40:00 (5 min)
- **Objective:** Classify developer tools from inline typing to agentic workflows.
- **Spoken Script:**
  > "In software delivery, GitHub Copilot provides 4 modes:  
  > 1. Ghost Text: Grey inline completions accepted with Tab. Best for repetitive boilerplate.  
  > 2. IDE Chat: Sidebar conversation with specialized participants like `@workspace` and commands `/fix` and `/tests`.  
  > 3. Agent Mode & Copilot Edits: The modern breakthrough. The agent generates a plan, alters multiple files simultaneously, and executes terminal test runs.  
  > 4. Copilot CLI and GitHub.com Cloud PR Agents that draft summaries and perform initial static reviews.  
  > Notice the engineer's evolving role: from typing raw syntax to orchestrating changes and conducting rigorous diff reviews."

---

### Slide 12: Context Engineering in the IDE
- **Timing:** 40:00 — 44:00 (4 min)
- **Objective:** Demystify the context retrieval stack and highlight copilot-instructions.md.
- **Spoken Script:**
  > "How does Copilot in VS Code know what to write?  
  > It is an engineered context stack:  
  > 1. Active cursor prefix and suffix;  
  > 2. Open neighbor tabs! Practical tip: if Copilot hallucinates types or method signatures, open the source file in an adjacent tab;  
  > 3. The `.github/copilot-instructions.md` configuration file in project root. Define code standards once: 'use pytest', 'strict type hints', 'preserve existing API contracts';  
  > 4. Workspace vector indexing and configured MCP servers."

---

### Slide 13: Windows Copilot vs Copilot+ PC
- **Timing:** 44:00 — 48:00 (4 min)
- **Objective:** Distinguish cloud desktop apps from local on-device NPU processing.
- **Spoken Script:**
  > "At the OS level, distinguish two distinct architectures:  
  > First, the cloud Copilot application. This is a desktop Progressive Web App routing queries to Azure datacenters.  
  > Second, on-device Copilot+ PC features running on dedicated 40+ TOPS NPUs. Capabilities like Recall (local photographic semantic timeline), Click to Do, and Live Captions process frames directly on local silicon with zero network latency.  
  > Be mindful of regional and corporate policies: in jurisdictions like the EU or on managed corporate fleets, some NPU features may be administratively disabled."

---

### Slide 14: Cross-Surface Scenario (Project Northstar)
- **Timing:** 48:00 — 52:00 (4 min)
- **Objective:** Set up the end-to-end case study before the break.
- **Spoken Script:**
  > "Before taking our break, inspect our end-to-end case: Project Northstar.  
  > Business goal: roll out VIP Free Shipping for orders above $50.  
  > Notice how this work flows across three distinct tools:  
  > 1. Executive meeting decisions are converted into a customer support brief in M365 Copilot with verified citations;  
  > 2. An issue is logged in GitHub. Copilot Agent Mode modifies `shipping.py` and creates unit tests verified by pytest;  
  > 3. The engineer verifies local preflight checklist `release_checklist.txt` before enabling feature flags.  
  > We will execute these live after the break!"

---

### Slide 15: Midpoint Break (5 Minutes)
- **Timing:** 52:00 — 57:00 (5 min)
- **Objective:** Cognitive reset and physical rest.
- **Spoken Script:**
  > "We have reached our lecture midpoint! Taking our mandatory 5-minute break.  
  > I am activating the 5-minute countdown timer. Our strict policy: absolutely zero work tasks or chat polling during this rest period. Step away from your monitor, relax your eyes, and grab a coffee.  
  > I will mute my microphone and return 30 seconds before time expires."

---

### Slide 16: Live Demo Part 1 — Microsoft 365 Copilot
- **Timing:** 57:00 — 63:00 (6 min)
- **Objective:** Demonstrate grounded synthesis from fixture notes using 4 prompt ingredients.
- **Spoken Script:**
  > "Welcome back! Entering the practical demonstration block.  
  > I open `meeting_notes_fixture.docx` — raw notes from an executive leadership meeting.  
  > We apply our 4-ingredient prompt: Goal is drafting a support brief; Context is the upcoming release; Source is this attached file; Expectations include paragraph citations.  
  > Observe the output: Copilot extracts the $50 threshold, flags unaddressed edge cases regarding delivery failure refunds, and anchors claims with bracketed citations.  
  > This is true grounding: verifiable output linked directly to authoritative sources."

---

### Slide 17: Live Demo Part 2 — GitHub Copilot Agent Mode
- **Timing:** 63:00 — 70:00 (7 min)
- **Objective:** Demonstrate VS Code Agent Mode, multi-file edits, and diff verification.
- **Spoken Script:**
  > "Switching to VS Code with `sample_repo`.  
  > In `ISSUE.md`, the task is defined. In `.github/copilot-instructions.md`, our constraints are specified.  
  > Prompting Agent Mode: `@workspace Read ISSUE.md and instructions. Implement VIP free shipping in shipping.py and write unit tests in test_shipping.py`.  
  > The agent drafts a plan and modifies both files.  
  > Notice the agent requesting terminal execution permission: `python smoke_check.py`. I review the command and approve. All tests pass!  
  > Before clicking Accept, I inspect the side-by-side diff. This is the mandatory human checkpoint: ensuring existing tier checks weren't deleted. Verified and committed!"

---

### Slide 18: Production Chronicles (Disasters vs Dawn Foods Win)
- **Timing:** 70:00 — 75:00 (5 min)
- **Objective:** Review enterprise failure modes and contrast with Dawn Foods success.
- **Spoken Script:**
  > "Let's review what occurs when governance boundaries fail.  
  > 4 catastrophic industry incidents:  
  > 1. Executive salary exposure due to open HR directories queried via Semantic Index;  
  > 2. Destructive CLI command execution with hallucinated flags that cleared staging state;  
  > 3. Package hallucination exploitation where attackers registered a suggested npm library;  
  > 4. Merging code without running CI based on AI conversational claims.  
  > Now contrast this with our verified win: EPAM CodeMie @ Dawn Foods. Accelerating SDLC by 35% succeeded because every single change passed human peer review and automated CI pipelines. AI drafts fast; humans ensure durability."

---

### Slide 19: Decision Matrix (4 Questions)
- **Timing:** 75:00 — 80:00 (5 min)
- **Objective:** Reinforce the four-question evaluation checklist before tool invocation.
- **Spoken Script:**
  > "Before touching any assistant, answer these 4 questions:  
  > 1. Where does the source of truth live? (Repository, Graph, or Local OS?)  
  > 2. What actions are permitted? (Advise only, edit files, or execute tests?)  
  > 3. What is the mandatory human checkpoint? (Diff review, pytest run, or citation fact-check?)  
  > 4. What durable evidence artifact is retained? (PR link, commit, or SharePoint version?)  
  > And remember the Red Zone: autonomous financial transactions or direct production deployments without human approval remain strictly forbidden."

---

### Slide 20: Homework Assignment (Copilot Operating Map)
- **Timing:** 80:00 — 85:00 (5 min)
- **Objective:** Detail homework instructions and deliverable expectations.
- **Spoken Script:**
  > "Here is your homework assignment.  
  > You will build your personal Copilot Operating Map.  
  > Select 3 real-world tasks from your day-to-day job (or use our reference Glovo Courier / Project Northstar benchmark) and populate the matrix: Task, Surface, Context Source, Allowed Action, Human Checkpoint, Evidence, and Policy.  
  > Part 2: Write one production prompt following Microsoft's 4-ingredient standard.  
  > Save your deliverable in `copilot_operating_map.md` under `L07/` in `genai-homeworks` and submit your Pull Request."

---

### Slide 21: Summary, Q&A & Lesson 08 Teaser
- **Timing:** 85:00 — 90:00 (5 min)
- **Objective:** Summarize 4 takeaways, open microphones, and teaser Lesson 08.
- **Spoken Script:**
  > "To wrap up Lesson 07:  
  > 1. Copilot is a portfolio, not a single tool;  
  > 2. Context location determines surface selection;  
  > 3. The 4 prompt ingredients eliminate hallucinations;  
  > 4. Human checkpoints and diff reviews are mandatory.  
  > Next time in Lesson 08, we explore AI for Data Analysis: why LLMs must never perform arithmetic in their heads and how sandboxed Code Interpreters ensure deterministic calculations.  
  > Microphones are open — questions are welcome!"
