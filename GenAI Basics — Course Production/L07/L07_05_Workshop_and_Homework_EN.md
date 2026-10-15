# Lesson 07: Workshop & Homework Guide
**Course:** GenAI Basics • Module 3 • Lesson 07  
**Submission Artifact:** `copilot_operating_map.md` (inside `L07/` of `genai-homeworks`)  
**Git Branch:** `feat/L07-copilot-operating-map`  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  

---

## 1. Assignment Mission & Objective

The objective of this assignment is to **transition AI assistant usage from casual exploratory chats into governed systems engineering**.

Engineers encounter dozens of recurring tasks every day: writing unit tests, refactoring classes, drafting release announcements, triaging customer incidents, and auditing staging configs. Your task is to design a **Copilot Operating Map** that establishes explicit context boundaries, defines permitted actions, and specifies mandatory human verification checkpoints.

---

## 2. Deliverable Requirements (`copilot_operating_map.md`)

In your repository, create the file `genai-homeworks/L07/copilot_operating_map.md` containing two mandatory sections:

### Section 1: The Copilot Operating Map Matrix
Select **3 real-world tasks** from your daily engineering workflow (or use the reference Glovo Courier / Project Northstar benchmark) and populate the matrix:

| Field | Requirement | Reference Example (Glovo Courier Benchmark) |
| :--- | :--- | :--- |
| **1. Task** | Concrete atomic process (specific action, not generic "write code") | Implement a night-time surge multiplier in courier dispatch fee calculator |
| **2. Surface** | Exact tool family and operational mode | GitHub Copilot in VS Code (Agent Mode / Copilot Edits) |
| **3. Context Source** | Where the source of truth physically resides | Jira ticket `GLV-402`, dispatch fee file `pricing.py`, test suite `test_pricing.py` |
| **4. Allowed Action** | Permitted actions granted to the assistant | Propose edit plan, modify local source files, execute pytest in IDE terminal |
| **5. Human Checkpoint** | Concrete verification required before accepting | Side-by-side git diff inspection in `pricing.py` (checking for zero-division guards) + green pytest |
| **6. Durable Evidence** | Persistent audit artifact proving completion | Pull Request with passing CI test pipeline run logs attached |
| **7. Policy Dependency** | Organizational policy or security constraints | Enterprise restriction against unvetted third-party MCP servers in the IDE |

### Section 2: Production 4-Ingredient Prompt (Microsoft Learn Standard)
For one of the three tasks analyzed above, formulate a production-grade prompt structured strictly into the 4 official Microsoft Learn ingredients:
* `[Goal]`: Unambiguous action verb and clear definition of desired output;
* `[Context]`: Business rationale, intended audience, and delivery lifecycle stage;
* `[Source]`: Explicit link to authoritative file, ticket, or transcript;
* `[Expectations]`: Precise constraints on length, structure, tone, and mandatory source citations.

---

## 3. Calibration Benchmark: Glovo Food Delivery Courier

If confidentiality prevents you from using internal project data, use our canonical course benchmark — **Glovo Courier Delivery Platform**:
* **Task A (Software Delivery):** Implement heavy rain compensation bonus logic in the dispatch service repo (GitHub Copilot Agent Mode). Checkpoint: 100% unit test coverage, boundary edge-cases verified (0 km, negative bonus values).
* **Task B (Knowledge Work):** Draft severe weather safety guidelines for courier onboarding based on operations documentation (Microsoft 365 Copilot in Word). Checkpoint: fact-check policy rules, ensure zero fabricated insurance clauses.
* **Task C (Local Preflight):** Pre-shift dispatch workstation checklist verification (Windows local checklist). Checkpoint: validate telephony and CRM connectivity.

---

## 4. Grading Rubric (100-Point Scale)

| Criterion | Points | Evaluation Standard |
| :--- | :---: | :--- |
| **1. Surface Selection Accuracy** | 25 | Surfaces mapped strictly to the source of truth (code ➔ GitHub, docs ➔ M365). Zero logo confusion. |
| **2. Blast Radius & Action Boundaries** | 25 | Zero autonomy illusions. Financial transactions and unreviewed production deploys strictly forbidden. |
| **3. Rigorous Human Checkpoints** | 25 | Concrete engineering verification specified: diff review, pytest run, citation fact-check (not "looks fine"). |
| **4. 4-Ingredient Prompt Quality** | 25 | Prompt cleanly organized across Goal, Context, Source, and Expectations with strict constraints. |

---

## 5. Submission Instructions

1. Create git branch `feat/L07-copilot-operating-map` in your `genai-homeworks` repo.
2. Commit `copilot_operating_map.md` under directory `L07/`.
3. Open a Pull Request targeting branch `main`.
4. Invite `ihar_rubanovich@epam.com` as a repository Collaborator.
5. The instructor will provide code review feedback on your PR within 7 days.
