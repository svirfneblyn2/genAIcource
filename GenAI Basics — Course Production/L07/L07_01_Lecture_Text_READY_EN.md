# Lesson 07: The Copilot Ecosystem — GitHub, Microsoft 365 & Local Context
**Course:** GenAI Basics • Module 3 (Engineer's Environment & Analytics) • Lesson 07 of 16  
**Instructor:** Ihar Rubanovich (Engineering Manager II & AI Ambassador, EPAM Systems • `ihar_rubanovich@epam.com`)  
**Slide Deck:** `presentation_L07_Copilot_Ecosystem_EN.html` / `presentation_L07_Copilot_Ecosystem_EN.pdf`  
**Sources Verified:** 2026-10-06  

---

## 1. Conceptual Mental Model: Copilot is a Portfolio, Not a Single Runtime

In 2026, the statement *"I do this using Copilot"* is architecturally underspecified until three parameters are defined:
1. **Where does the authoritative source of truth live (Source of Truth)**;
2. **What are the permitted assistant action boundaries (Action Boundary)**;
3. **Who validates the outcome before persistence (Human Checkpoint)**.

The Copilot brand represents a portfolio of distinct systems operating across independent data planes:
* **GitHub Copilot:** Software Delivery context. Truth is derived from the git tree, open buffer tabs, abstract syntax trees (AST), commit history, and test runners. Control plane: GitHub Enterprise organization policies and branch protection rules.
* **Microsoft 365 Copilot:** Knowledge Work context. Truth is retrieved via **Microsoft Graph** and **Semantic Index** from Outlook emails, Teams threads, SharePoint sites, and Office documents. Control plane: Microsoft Entra ID, Microsoft Purview DLP, and ACL security groups.
* **Windows Copilot & Copilot+ PC:** Local Device context. Truth resides on the active display, OS clipboard, local file systems, and hardware NPUs. Control plane: Windows Group Policies and local user privileges.

### The 10/90 Axiom in Developer Assistants
Direct foundation model inference accounts for **no more than 10%** of the system's business value. The remaining **90%** comprises:
* Authoritative grounding pipelines (*Grounding*);
* Security trimming mechanisms (*Permission Trimming*);
* Context engineering inside IDE editors;
* Execution guardrails and terminal authorization gates;
* Retention of verifiable audit artifacts (*Audit Evidence*).

---

## 2. Grounding Architecture: How Enterprise Data Reaches LLMs

Foundation models have no inherent knowledge of your organization's internal roadmaps, repositories, or executive decisions. Models are not fine-tuned on company files in real-time. Instead, interaction relies on a dynamic Retrieval-Augmented Generation (**Dynamic RAG**) pipeline:

1. **User Request Interception:**
   The employee inputs a prompt in Teams, Word, or Copilot Chat. The orchestrator captures active application context, injects Entra ID user security tokens, and cleanses the query.
2. **Semantic Search via Microsoft Graph & Semantic Index:**
   The orchestrator queries **Microsoft Graph** — the unified graph of user relationships, messages, and files. **Semantic Index for Copilot** runs vector similarity searches against indexed document chunks in SharePoint and OneDrive.
   *Crucial Security Boundary:* Search executes strictly within the **User Security Context**. If an employee lacks permissions to a folder or file, Semantic Index trims it from results (*Permission Trimming*).
3. **Metaprompt Enrichment:**
   The orchestrator combines:
   * Microsoft safety guidelines and style instructions;
   * The user's prompt;
   * Retrieved authoritative document chunks (including version and author metadata);
   * Required output schemas and citation constraints.
4. **Foundation LLM Inference:**
   The foundation model generates an autoregressive response grounded entirely in the supplied document context.
5. **Post-Processing & Enterprise Data Protection (EDP):**
   Before the response is presented, it passes through Microsoft Purview DLP compliance filters, formats precise source citations, and logs audit events. Customer data is strictly never used to train foundation models.

---

## 3. Microsoft Learn Prompting Standard: The 4 Prompt Ingredients

Official Microsoft Learn curriculum (MS-4004 / MS-4005) discourages vague single-line requests. To ensure repeatable enterprise results, prompts must assemble four essential ingredients:

$$\text{Production Prompt} = \text{Goal} + \text{Context} + \text{Source} + \text{Expectations}$$

### 1. Goal
A precise action verb defining the operation: *"Draft a summary table"*, *"Synthesize an onboarding brief"*, *"Identify policy contradictions"*.

### 2. Context
The business rationale: intended audience, project phase, and why this artifact is needed (*"For Tier-1 customer support agents ahead of our weekend release"*).

### 3. Source
Explicit links to authoritative files or transcripts. In M365 Copilot, sources are specified using the `/` reference symbol or explicit attachments: *"Rely strictly on attached meeting_notes_fixture.docx"*. Explicit sources eliminate up to 95% of model hallucinations.

### 4. Expectations
Strict format constraints: word count, header structure, tone, required sections, and mandatory paragraph citations (*"Markdown format, under 300 words, include an 'Open Questions' section"*).

---

## 4. Security & Access Model: The Oversharing Dilemma

The primary paradox of enterprise AI deployment: **Copilot is secure by design, but ruthless against poor data hygiene**.

* **Feature (Zero Trust by Default):** The model holds no superuser privileges; it sees only what the user is authorized to read.
* **Chief Enterprise Risk (Oversharing):** Prior to semantic indexing, an executive compensation spreadsheet left open to "All Company" remained hidden because nobody knew its file path. Semantic Index, however, indexes by conceptual meaning: an employee asking *"What are planned compensation changes?"* surfaces the document immediately.
* **Engineering Mandate:** Copilot deployment must be preceded by access audits across SharePoint and Teams, Purview Sensitivity Labels, and restricted channel policies.

---

## 5. GitHub Copilot: 4 Operating Modes

GitHub Copilot extends far beyond simple line autocomplete:

1. **Inline Ghost Text:**
   Grey predictive text accepted via `Tab`. Best for boilerplate functions, loop constructs, and standard API invocations.
2. **IDE Chat (Sidebar & Slash Commands):**
   Conversational drawer in VS Code or JetBrains. Connects with specialized participants:
   * `@workspace` — indexes repository structure and class dependencies;
   * `@terminal` — explains build failures and CLI errors;
   * Commands: `/explain`, `/fix`, `/tests`, `/doc`.
3. **Copilot Edits & Agent Mode:**
   Multi-file autonomous agent in the IDE. The developer sets an objective; the agent drafts an implementation plan, modifies multiple project files simultaneously, and executes terminal test commands.
   *Key governance rule:* Every file change and terminal command requires human inspection and manual confirmation!
4. **Copilot CLI & Cloud PR Agents:**
   Terminal-native `copilot` CLI and GitHub.com background agents that generate Pull Request summaries and perform automated initial code reviews.

### Context Engineering in the IDE
Copilot gathers context through an engineered stack:
1. Active file prefix and suffix surrounding cursor;
2. Neighbor tabs open in the current editor session;
3. Project instructions `.github/copilot-instructions.md`;
4. Workspace embedding vector index;
5. Configured Model Context Protocol (MCP) servers.

---

## 6. Windows Copilot vs On-Device AI (Copilot+ PC)

In Windows, maintain a clear distinction between two technical tiers:
* **Cloud Copilot App (PWA):** Remote desktop application routing requests, voice, and screenshots to cloud Azure datacenters.
* **Hardware Copilot+ PC Features (40+ TOPS NPU):** Operating system capabilities executing locally on hardware neural processing units with zero network latency and enhanced privacy:
  * **Recall:** local photographic semantic activity timeline;
  * **Click to Do:** contextual on-screen actions;
  * **Live Captions:** real-time on-device audio translation.

*Regulatory Notice:* Due to regional compliance frameworks (e.g., EU Digital Markets Act) and enterprise group policies, certain Copilot+ PC features may be restricted. Always verify device feature availability before designing workflows.

---

## 7. Cross-Surface Scenario: Project Northstar

Project Northstar (implementing VIP Free Shipping) illustrates how work flows sequentially across tools:
1. **Phase 1 (M365 Copilot):** Decisions captured during an executive meeting are synthesized into a Support Rollout Brief using the 4-ingredient prompt standard.
2. **Phase 2 (GitHub Copilot Agent Mode):** An engineer implements the logic in `shipping.py` and creates unit tests in `test_shipping.py`. The engineer inspects diffs and verifies via `pytest`.
3. **Phase 3 (Windows / Local Context):** The engineer completes the pre-release checklist in `release_checklist.txt` before toggling staging feature flags.

---

## 8. Production Chronicles: 4 Failures vs Enterprise Success

### Catastrophic Industry Incidents
1. **Executive Compensation Leak via Semantic Search:** Permissive HR folder permissions exposed salary details to junior staff during routine bonus inquiries.
2. **Destructive CLI Flag Execution:** An engineer executed a hallucinated command flag suggested by a CLI tool that wiped staging environment state.
3. **Package Hallucination Exploit:** A coding assistant recommended a nonexistent npm package, which threat actors subsequently registered with malicious code.
4. **Blind PR Merge:** An engineer accepted an autonomous agent's pull request without running tests; code failed immediately in production with syntax errors.

### Enterprise Delivery Success: EPAM CodeMie @ Dawn Foods
Across Dawn Foods delivery streams, structured AI assistance powered by EPAM CodeMie achieved **35% SDLC acceleration** in feature velocity, unit testing, and architectural documentation.
**Success Factors:** Rigid task templates, context isolation rules, and mandatory human peer review before main branch integration.

---

## 9. Decision Matrix & Homework Assignment

### 4 Questions of the Copilot Operating Map
1. **Where is the source of truth?** (Git repository, Microsoft Graph, or local OS).
2. **What are the permitted actions?** (Advise, draft file, execute test suite, create branch).
3. **What is the human checkpoint?** (Diff review, test pass log, citation verification).
4. **What durable evidence artifact is retained?** (Pull Request, SharePoint versioned doc, CI log).

### Homework Assignment
Students submit `copilot_operating_map.md` to folder `L07/` of `genai-homeworks`, defining the operating map for 3 real-world tasks and crafting 1 production prompt adhering to Microsoft Learn's 4-ingredient standard. Benchmark reference: Glovo Food Delivery Courier or Project Northstar.
