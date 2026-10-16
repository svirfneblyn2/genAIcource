# L13 Source Notes: Your Own AI Assistant (research 2026-10-16)

Primary sources checked on 2026-10-16. The lesson was rebuilt from the September 2026 Drive package "Custom GPTs, Responses API and Agents SDK": GPTs retire on 11 December 2026, so the deck teaches projects/plugins instead.

## Images used in the deck (own captures, 2026-10-16)

| File | What |
|---|---|
| `assets/v2/img/chatgpt_gpts_retire.png` | chatgpt.com/gpts banner: "Перенесите свои GPT в плагины до 11 декабря" (RU slide 3); recaptured in the final screenshot round with the banner block zoomed to 160 % in the page (real UI, larger), so its text is ≥ 24 px on the slide |
| `assets/v2/img/chatgpt_gpts_retire_en.png` | the same banner in the English UI (`?locale=en-US`): "Migrate your GPTs to plugins by December 11" (EN slide 3) |
| `assets/v2/img/chatgpt_plugin_creator.png` | ChatGPT Plugins → Add → Create plugin: "@Plugin Creator, помоги мне создать плагин" (nothing sent) |
| `assets/v2/img/claude_project_panel.png` | slide 4: recrop (Pillow) of the claude.ai project "Демо L09: поддержка курьеров" capture: title strip + right-hand panel (Instructions / Context / Memory / Scheduled) scaled ×2.2; the original captures `claude_project.png` / `claude_instructions.png` and the English schematics `assistant_recipe*.png`, `ladder.png`, `cover_right.png` were removed from the folder (git history) |
| `assets/v2/img/claude_instructions_crop.png` | slide 5: the project instructions dialog cut just below the last instruction line (dialog closed with Cancel) |
| `assets/v2/img/icons/ic_r1…ic_r5.png`, `ic_l1…ic_l4.png` | outline icons cut (text-free) from the two genai-assets schematics; slide 2 recipe, slide 9 ladder and the cover card are now drawn in HTML with RU/EN labels |

Observed but not used on a slide: gemini.google.com/gems/view banner (in another account and language) stating that from 17 November 2026 Gems become skills.

**Fix round 2026-10-16 (final audit):** ChatGPT plugin path flagged as "checked on Business; on Free/Plus fall back to Claude" (slides 6, 14, 16, homework); Gems dates now "personal from 17.11.2026, Workspace from March 2027"; slide 15 plaque no longer claims anything about GPT authors or file extraction (now: on work plans an admin may see chats); knowledge-file wording softened to "assume every user may see the knowledge files".

The Responses API and Agents SDK code on slides 10–11 was not executed (no OpenAI API key on the build machine).

---


Scope: rebuild of "L13: Custom GPTs, Responses API and Agents SDK" (beginner).
All items checked 2026-10-16 unless noted. help.openai.com and openai.com block plain fetchers;
they were read through the user's Chrome. "UNVERIFIED" = only secondary sources found.

---

## 0. HEADLINE CHANGES vs the Sept 2026 package (read first)

| # | Old package said (checked 2026-09-08) | Today (2026-10-16) | Source |
|---|---|---|---|
| A | Custom GPTs = current product; Business/Enterprise/Edu can create | **OpenAI is retiring custom GPTs. Standard retirement: Dec 11, 2026** (Feb 11, 2027 only for Enterprise workspaces with an approved deferral). Replacement = **Plugins** (skills + apps). Applies to **all ChatGPT plans**. | https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq |
| B | — | Enterprise: **creation of new custom GPTs ends Oct 26, 2026 (planned)** — 10 days after this check. **CONFLICTING:** a 2026-10-16 web-search summary of the same FAQ gives **Sep 25, 2026 (planned)** and a Sep 17 migration target; the FAQ (help.openai.com/en/articles/20001519) returns 403 to plain fetchers, so it could not be rechecked in the fix round. Not used on any slide. | same FAQ |
| C | Demo model `gpt-5.6-luna` | New generation: **gpt-6-astra / gpt-6.1-sol / gpt-6-sol / gpt-6-luna**. `gpt-6-luna` is cheaper than 5.6-luna ($0.10 / $0.50 vs $0.20 / $1.20 per 1M) | https://developers.openai.com/api/docs/pricing |
| D | Assistants API not discussed | **Assistants API was shut down on Aug 26, 2026** (already gone) | https://developers.openai.com/api/docs/deprecations |
| E | Agent Builder wind-down after Nov 30, 2026 | Confirmed: **Agent Builder shutdown Nov 30, 2026**; Evals read-only Oct 31, shutdown Nov 30. ChatKit stays. | deprecations page |
| F | — | NEW: **Agents API** (hosted, public beta, Sep 10, 2026): `client.beta.agents.sessions.create(...)`, built on the Codex harness | https://openai.com/index/introducing-the-agents-api/ |
| G | Agents SDK version not pinned | `openai-agents` **0.24.0** (PyPI, 2026-10-15); `@openai/agents` **0.20.0** (npm, 2026-10-08) | PyPI / npm registry |
| H | Gemini Gems = stable equivalent | Google help page: **"Starting in November 2026, Gems will go away on personal Google accounts and automatically transition to skills."** | https://support.google.com/gemini/answer/15146780 |

**Teaching implication:** a lesson delivered now that teaches "build a Custom GPT" teaches something that goes away for everyone on Dec 11, 2026.
Option: frame it as "a configured assistant = instructions + knowledge + tools" and show GPTs → Plugins/skills (ChatGPT), Projects (Claude),
Gems → skills (Gemini), Agent Builder (M365 Copilot). The configuration skill carries over; the product names don't.

---

## 1. Custom GPTs in ChatGPT (today)

- **Name:** still "GPTs" / "custom GPTs" in Help Center. Definition: "versions of ChatGPT configured for a specific purpose", combining instructions, knowledge and selected capabilities.
  https://help.openai.com/en/articles/8554407-gpts-in-chatgpt (checked 2026-10-16, page "updated 17 days ago")
- **Retirement banner on all GPT help articles:** "We're planning to retire custom GPTs … we recommend moving your workflows to Plugins." The banner on these articles says the migration experience is "targeted for Sep 17, 2026". The FAQ says Sep 22, 2026 (Oct 1 for workspaces that opted into delayed banners). **The two pages disagree; use the FAQ.**
- **Retirement timeline (FAQ):** Sep 11, 2026 admin notice → Sep 22 migration target → Oct 26, 2026 (planned) Enterprise creation freeze → **Dec 11, 2026 standard retirement** ("custom GPTs and their GPT pages become inaccessible") → Feb 11, 2027 for approved deferrals only. "The transition affects all ChatGPT plans."
  Existing conversations with GPTs stay accessible after retirement.
  https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- **What migrates (FAQ + learn page):** instructions → a **skill**; knowledge files → plugin **reference files**; connected apps → plugin apps. **Not migrated:** custom **Actions** (rebuild via an app or custom MCP server), selected model, sharing settings (plugin starts private), drafts. The original GPT becomes read-only after migration. Path: My GPTs → "Migrate to plugin".
  https://learn.chatgpt.com/docs/migrate-custom-gpts
- **Who can create:** "New GPT creation and publishing are not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro." Business/Enterprise/Edu: create/edit/publish per workspace settings and permissions. Existing GPTs can still be used everywhere (users must be signed in). Creation and editing happen on the web only; the mobile apps can use GPTs but can't create them.
  https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- **Where created:** Explore GPTs in sidebar or https://chatgpt.com/gpts → **Create** → Conversational builder or Configuration view.
- **Builder fields:** Name, Description, Conversation starters, **Instructions**, **Knowledge** (files), **Recommended model**, **Capabilities**: Web search, Image generation, Canvas, Code Interpreter & Data Analysis, Apps; **Actions** (external APIs you define). "A GPT can use either apps or actions, but not both at the same time." Preview, auto-saved draft, Create/Update, Version history (••• menu).
- **Limits:** "You can attach up to 20 files to a GPT. Each file can be up to 512 MB." (unchanged). Some file types require Code Interpreter & Data Analysis.
- **Memory:** "GPTs do not use saved memory, custom instructions, or previous conversations." You can bring a GPT into a normal chat with @ (web only).
- **Embedding:** "GPTs are designed to work in ChatGPT. They are not a way to embed ChatGPT in an external website … To build an assistant into a product, use the API." (good line for the slide that separates GPTs from the API)
- **GPT Store:** still described in Help ("Publishing to the GPT Store makes your GPT publicly available"). Personal accounts can't publish new GPTs, and retired GPTs "leave the GPT directory". So the Store goes away with retirement (inferred; no dedicated GPT Store shutdown notice found). A public plugin needs "a separate plugin submission process".
  https://help.openai.com/en/articles/8798878-sharing-and-publishing-gpts
- **Projects / ChatGPT Work:** GPTs did **not** move into Projects. The successors are **Plugins** (Chat/Work/Codex) and, for teams, **Workspace agents** (see below). The Business help page still lists "GPTs, Projects, Apps, Company Knowledge, ChatGPT Agent, Deep Research" as Standard-seat features.
  https://help.openai.com/en/articles/8792828-chatgpt-business-overview
- **Plugins (successor):** a plugin can bundle skills, connected apps, app templates and extensions. "The plugin directory is available on all ChatGPT plans"; whether a specific plugin can be installed depends on the plan. To create one: install **Plugin Creator** from the directory, then chat with `@plugin-creator`. Plugins can include MCP apps (local MCP = desktop only). Business/Enterprise users can share plugins inside their workspace. "Personal skills are generally available to ChatGPT Business, Enterprise, Healthcare and Edu users."
  https://help.openai.com/articles/20001256 (RU page "Плагины в ChatGPT", updated 2 hours before the check)
- **Workspace agents:** announced 2026-04-22. "Workspace agents are an evolution of GPTs." Codex-powered, run in the cloud, shareable in ChatGPT and Slack, scheduled runs, approvals for sensitive actions. GA in Business, Enterprise, Edu (+ ChatGPT for Teachers). Free until May 6, 2026, then credit-based billing.
  https://openai.com/index/introducing-workspace-agents-in-chatgpt/
  (Secondary search summary: credit pricing moved to July 6, 2026. **UNVERIFIED**)

## 2. Equivalent no-code assistants (one line each)

- **Claude Projects** (Anthropic): workspace with its own chats + knowledge base + project instructions. **Available to all users including Free (Free max 5 projects)**; RAG expansion only on paid plans (Pro, Max, Team, Enterprise); sharing (Can view / Can edit) only on Team/Enterprise. A new beta version is rolling out (starts in Claude Code). https://support.claude.com/en/articles/9517075-what-are-projects (page "updated yesterday")
- **Gemini Gems** (Google): custom Gemini with a name, instructions and optional Knowledge files (device, Drive, NotebookLM notebook). Personal accounts need to be 13+. **"Starting in November 2026, Gems will go away on personal Google accounts and automatically transition to skills."** https://support.google.com/gemini/answer/15146780
  Dates **CONFIRMED** (fix round 2026-10-16): Nov 17, 2026 for personal accounts (in-app Gemini notice observed on gemini.google.com/gems/view; Android Central / Android Authority / TechRepublic), March 2027 for Workspace business/enterprise (Google blog "Let skills in Gemini tackle your most repetitive tasks", blog.google; Workspace help "About the transition from Gems to skills", knowledge.workspace.google.com/p/gems-migration), June 2027 for education. Skills requiring 18+ and Keep Activity remains secondary only.
  https://www.androidcentral.com/apps-software/ai/google-outlines-timeline-to-phase-out-gemini-gems-in-favor-of-skills ; https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
- **Microsoft 365 Copilot – Agent Builder** (builds "declarative agents"): in microsoft365.com/chat, office.com/chat, Teams desktop/web; not on mobile. Instructions + knowledge (SharePoint, Copilot connectors, web) + capabilities (code interpreter, image generator). It can't author actions, so "copy the agent to Microsoft Copilot Studio" for actions/workflows. Skills are in preview (Frontier Program).
  **Licensing:** Copilot Chat users (no license) get agents grounded on instructions or the web. Org data (SharePoint, connectors) needs pay-as-you-go Copilot Credits or a Microsoft 365 Copilot license. Email, People and Teams knowledge need the full license.
  https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder (updated 2026-10-12); https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/prerequisites (2026-09-30)
- **Microsoft Copilot Studio:** "available to all Microsoft 365 users"; org-data grounding needs pay-as-you-go or a Copilot Studio license. (same prerequisites page)

## 3. OpenAI Responses API

- **What it is:** "our new API primitive", an evolution of Chat Completions. "While Chat Completions remains supported, Responses is recommended for all new projects." Benefits include hosted tools, an agentic loop (several tool calls in one request), better caching ("40% to 80%" cache improvement in internal tests) and stateful context.
  https://developers.openai.com/api/docs/guides/migrate-to-responses
- **Built-in tools (Tools guide):** Function calling, Web search, Remote MCP servers, Skills, Shell, Computer use, Image generation, File search, Tool search, Programmatic Tool Calling. The model page for gpt-6-luna also lists Code interpreter, Hosted shell and Apply patch.
  https://developers.openai.com/api/docs/guides/tools ; https://developers.openai.com/api/docs/models/gpt-6-luna
- **Conversation state (4 options):** (1) resend history manually; (2) `previous_response_id`; (3) **Conversations API**, which passes a `conversation` ID (a durable object, not subject to the 30-day TTL); (4) `store` parameter: "Response objects are saved for 30 days by default", and `store=false` disables saving. Server-side compaction is available (`context_management`, `/responses/compact`).
  **Cost catch for beginners:** "Even when using previous_response_id, all previous input tokens for responses in the chain are billed as input tokens."
  The old package's note that `previous_response_id` can't be combined with `conversation` was not rechecked today. It is still plausible.
  https://developers.openai.com/api/docs/guides/conversation-state
- **Assistants API:** "officially sunset on August 26, 2026, and is no longer available". Replacement: Responses API + Conversations API.
  https://developers.openai.com/api/docs/deprecations ; migrate-to-responses page
- **Current models (models page):** featured = GPT-6 Astra (flagship; "If you're not sure where to start, use GPT-6 Astra"), GPT-6.1 Sol (near-Astra performance, lower cost), GPT-6 Luna ("most efficient model for focused, high-volume tasks").
  gpt-6-luna: 1,050,000 context, 128K max output, knowledge cutoff May 18, 2026, text+image in, supports Responses + Chat Completions + Batch.
  https://developers.openai.com/api/docs/models ; .../models/gpt-6-luna
- Minimal code (unchanged API shape; swap the model):
  ```python
  from openai import OpenAI
  client = OpenAI()
  r = client.responses.create(model="gpt-6-luna", instructions="Answer briefly.", input="My laptop cannot connect to the VPN.")
  print(r.output_text)
  r2 = client.responses.create(model="gpt-6-luna", previous_response_id=r.id, input="And if I'm on hotel Wi-Fi?")
  ```
  `openai` Python SDK is **3.31.0** on PyPI (checked 2026-10-16).

## 4. OpenAI Agents SDK, Agents API, Agent Builder

- **Package:** `pip install openai-agents`. Latest **0.24.0** (released 2026-10-15; 0.23.1 came out 2026-10-02). JS/TS: `@openai/agents` **0.20.0** (2026-10-08). https://pypi.org/project/openai-agents/ ; https://www.npmjs.com/package/@openai/agents
  Python version requirement: not stated on the docs index page. **UNVERIFIED**
- **Core concepts (docs index):** Agents, Agents as tools / Handoffs, Guardrails, Sandbox agents, Realtime agents, Voice agents, Function tools, MCP server tool calling, Sessions, Human in the loop, Tracing, plus Runner. https://openai.github.io/openai-agents-python/
- **Hello world (verbatim from docs):**
  ```python
  from agents import Agent, Runner
  agent = Agent(name="Assistant", instructions="You are a helpful assistant")
  result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
  print(result.final_output)
  ```
- **Handoff example (quickstart):** `Agent(name=..., handoff_description=..., instructions=...)` specialists; `triage_agent = Agent(..., handoffs=[history_tutor_agent, math_tutor_agent])`; `result = await Runner.run(triage_agent, "...")`; `result.last_agent.name` shows who answered. The demo pattern in the old package (`result.last_agent.name`) still works.
  https://openai.github.io/openai-agents-python/quickstart/
- **Agents API (NEW, hosted):** announced 2026-09-10, **public beta**, "a simple and flexible API" that gives developers the same harness and infrastructure as Codex, run by OpenAI. Call `client.beta.agents.sessions.create({agent:{model, tools:[mcp…], multi_agent:{…}}, environment:{type:"openai_hosted"}, input})`. Features: OpenAI-hosted sandboxes or partner sandboxes (Cloudflare, E2B, Modal, Vercel…), auto context compaction, tool search, subagents, MCP. **No extra fee**: you pay only for tokens and tools. https://openai.com/index/introducing-the-agents-api/
  Secondary: computer use added Sep 29, 2026; US-only data residency; no ZDR. **UNVERIFIED**
- **Agent Builder (AgentKit visual canvas):** deprecation announced June 3, 2026, **shutdown Nov 30, 2026**. Migrate to the Agents SDK or ChatGPT Workspace Agents (guide: "Migrate from Agent Builder"). **Evals platform:** read-only Oct 31, 2026, shutdown Nov 30, 2026 (the page suggests Promptfoo). **ChatKit remains available.** https://developers.openai.com/api/docs/deprecations
  The original AgentKit post (2025-10-06) has no shutdown note in its RU localized version. The deprecations page is the source to cite.
- Simple ladder for beginners: GPT/Plugin (no code, inside ChatGPT) → Responses API (you own the loop) → Agents SDK (library runs the loop in your code) → Agents API (OpenAI hosts the loop and sandbox).

## 5. Pricing points

**ChatGPT (USD/month):**
- Free $0; **Go $8** (US) https://openai.com/index/introducing-chatgpt-go/ (via search snippet; learn.chatgpt.com/docs/pricing also lists $8)
- **Plus $20**, monthly billing only. https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
- **Pro: three tiers, $100 / $200 / $500**. Ultrafast only on Pro 500. Monthly billing only. https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
- **Business:** Standard seat **$25** monthly / **$20** annual per user; Premium seat **$125** / **$100**; minimum 2 seats. Includes ChatGPT, ChatGPT Work, Codex. (Team was renamed Business on Aug 29, 2025.) https://help.openai.com/en/articles/8792828-chatgpt-business-overview
- Enterprise/Edu: contact sales.
- ChatGPT models now: GPT-6 rolled out Oct 7, 2026 (paid plans on GPT-6 Sol, Free/Go on GPT-6 Luna). https://openai.com/index/gpt-6-for-everyone/ (via search summary; **page not opened**, treat tier split as UNVERIFIED)

**API, standard per 1M tokens (input / cached / output), short context ≤272K:**
| Model | Input | Cached | Output |
|---|---|---|---|
| gpt-6-astra | $10.00 | $1.00 | $50.00 |
| gpt-6.1-sol | $2.00 | $0.10 | $10.00 |
| gpt-6-luna | $0.10 | $0.01 | $0.50 |
| gpt-5.6-luna (old demo default) | $0.20 | $0.02 | $1.20 |
| gpt-5-nano (cheapest listed) | $0.05 | $0.005 | $0.40 |
Batch/Flex about 50% off. Prompts over 272K input cost more (gpt-6-luna: 2x input, 1.5x output).
https://developers.openai.com/api/docs/pricing ; https://developers.openai.com/api/docs/models/gpt-6-luna

**Tools:** Web search **$10 per 1K calls** + search content tokens at model rates (the web search preview for non-reasoning models costs $25/1K calls, content free). File search: $2.50 per 1K calls + storage $0.10/GB/day (1 GB free). Containers (Code Interpreter / Hosted Shell): from $0.03 per 20-min session (1 GB).
Beginner example: 1,000 short Q&As on gpt-6-luna at about 500 input + 300 output tokens each ≈ 0.5M×$0.10 + 0.3M×$0.50 ≈ **$0.20** (my arithmetic). Adding a web search to every question adds about **$10**, so the search tool costs far more than the tokens.

## 6. Safety / policy

- **Training on data:** Business/Enterprise/Edu: "data is not used for training by default". Consumer plans (Free, Plus, Go, Pro) "may be used for training depending on whether you have opted out" (Data Controls). https://help.openai.com/en/articles/8554407-gpts-in-chatgpt
- **Builder can't see chats:** "GPT builders cannot view individual conversations that users have with their GPTs." (same page)
- **Third parties:** with apps/actions, "relevant parts of your input may be sent to the third-party service … OpenAI does not audit or control how those services use or store your data." (same page)
- **Knowledge files privacy:** the current Help pages give **no explicit statement** that users of a GPT can't read or download its knowledge files. The old "Knowledge in GPTs" article (8843948) now redirects to "Creating and editing GPTs". Teaching rule (pedagogical, not an OpenAI quote): treat anything uploaded to a shared GPT as readable by its users, and don't upload secrets. Whether file contents can be extracted is **UNVERIFIED** as an official statement.
- **Builder profile / verification:** publishing to everyone may require a completed builder profile (name, website from a **verified domain**, verified social profiles). For personal accounts, verification can use billing details or proof of owning a domain. Public actions need a valid **Privacy Policy URL**. GPTs are automatically checked against sharing and policy requirements, and blocked publishes can be appealed. Direct sharing goes to up to 100 recipients. https://help.openai.com/en/articles/8798878-sharing-and-publishing-gpts
- **Plugins:** installing a plugin "does not bypass" app authorization or workspace permissions. The "Verified by OpenAI" badge "does not replace" your org's own security review. (Plugins help page)
- **Usage Policies:** effective **Oct 29, 2025** (single universal policy). Four pillars: protect people, respect privacy, keep minors safe, empower people. Relevant for GPT builders: no automating high-stakes decisions without human review (employment, credit, education, housing, legal, medical…), no licensed (legal/medical) advice without a professional involved. https://openai.com/policies/usage-policies/
- **API data:** "data sent to the OpenAI API is not used to train or improve OpenAI models" unless you opt in. Abuse-monitoring logs are kept up to 30 days. Responses application state is kept 30 days by default. ZDR needs approval, and Conversations/Files/Vector Stores aren't ZDR-eligible. https://developers.openai.com/api/docs/guides/your-data

## 7. Other relevant notes

- ChatGPT changelog: GPT-5.5 retired from ChatGPT/Work/Codex on Oct 14, 2026. GPT-6 Sol and Luna in Work/Codex from Sep 22, 2026. GPT-6.1 Sol on Sep 29. https://learn.chatgpt.com/docs/changelog
- Demo asset change needed: `OPENAI_MODEL=gpt-5.6-luna` still exists and has no shutdown date on the deprecations page, but `gpt-6-luna` is cheaper. Recommend `gpt-6-luna`.
- Help Center pages show relative dates ("updated 17 days ago" ≈ 2026-09-29; FAQ "12 days ago" ≈ 2026-10-04).

## UNVERIFIED list
1. ~~Gemini Gems → skills exact dates~~ — **confirmed** 2026-10-16 (in-app notice + Google blog/Workspace help for March/June 2027; Android Central/TechRepublic for Nov 17). Only the 18+/Keep Activity requirement stays unverified.
2. Workspace agents credit billing start July 6, 2026 (official post says after May 6, 2026).
3. Agents API computer use (Sep 29), US-only residency, no ZDR.
4. GPT-6 tier split in ChatGPT (Sol for paid, Luna for Free/Go): from search summary of openai.com/index/gpt-6-for-everyone, page not opened.
5. Official statement on whether GPT users can extract knowledge files.
6. Agents SDK minimum Python version.
7. Exact non-Enterprise (Free/Plus/Business) GPT migration dates. The FAQ says all plans are affected, gives Dec 11 as the standard date, and says "follow your in-product notice".
8. A dedicated GPT Store shutdown announcement (inferred only from "retired GPTs leave the GPT directory").
9. Enterprise GPT creation cutoff: Oct 26, 2026 (FAQ read via Chrome) vs Sep 25, 2026 (web-search summary of the FAQ). Conflicting; not on any slide.
