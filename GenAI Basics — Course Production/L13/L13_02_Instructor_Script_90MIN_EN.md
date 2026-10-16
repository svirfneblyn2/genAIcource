# Instructor Script • Lesson 13: Your Own AI Assistant — Projects, Plugins, Responses API, Agents SDK (90 Minutes)

**Course:** GenAI Basics • Module 5 (Agents, Tools and MCP) • Lesson 13 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language; code only as reference (slides 10–11).
**Format:** 17 slides (`presentation_L13_Custom_Assistants_and_Agents_SDK_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 13 • 10-minute hands-on on slide 14
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).
**Facts:** as of 16.10.2026, sources in `L13_08_Source_Notes_Research_2026-10.md`.

> **Important:** the lesson used to be about Custom GPTs, but OpenAI retires GPTs on 11 December 2026 (moving them to plugins), and Gemini Gems become skills (personal accounts from 17 November 2026, Workspace from March 2027). The lesson teaches the general principle “instructions + knowledge + tools + model”. Before class check the paths in ChatGPT (Plugins → Add → Create plugin; checked on Business, may be missing on Free/Plus — then use Claude) and Claude (Projects).

**Lesson objective:** students build their own assistant without code in Claude or ChatGPT, write short, testable instructions, test the assistant with four kinds of questions, understand the risks of sharing, and know how the same is done in code (Responses API, Agents SDK).

---

## Timing (17 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Your own AI assistant | 00:00–02:00 | 2 |
| **02** | Every new chat starts from zero: you repeat the role, the rules and the files | 02:00–07:00 | 5 |
| **03** | GPTs in ChatGPT retire on 11 December 2026 — they move into plugins | 07:00–12:00 | 5 |
| **04** | A Claude project: instructions and files Claude remembers in every chat of the project | 12:00–17:00 | 5 |
| **05** | A good instruction: role, answer format, limits and where the data comes from | 17:00–22:00 | 5 |
| **06** | In ChatGPT you now build an assistant as a plugin — by talking to Plugin Creator | 22:00–27:00 | 5 |
| **07** | Every major product has its own assistant builder, under a different name | 27:00–32:00 | 5 |
| **08** | Before sharing an assistant, test it with four kinds of questions | 32:00–38:00 | 6 |
| **09** | When buttons are not enough: four steps from a project to your own agent in code | 38:00–43:00 | 5 |
| **10** | The Responses API: instructions and a conversation in a few lines of code | 43:00–48:00 | 5 |
| **11** | The Agents SDK: several agents, one hands the task to another | 48:00–53:00 | 5 |
| **12** | Tokens (the bits of text you pay for) cost pennies; the built-in tools cost money | 53:00–58:00 | 5 |
| **13** | 5 minutes: think which assistant you will build for yourself | 58:00–63:00 | 5 |
| **14** | 10-minute hands-on: build your assistant in Claude or ChatGPT | 63:00–73:00 | 10 |
| **15** | Four questions before you hand an assistant to colleagues | 73:00–79:00 | 6 |
| **16** | Homework: your own assistant for a repetitive work task | 79:00–85:00 | 6 |
| **17** | The assistant formula stays; only product names change | 85:00–90:00 | 5 |

Part 1 (slides 01–12, 00:00–58:00): why your own assistant, GPTs retire, Claude projects, instructions, ChatGPT plugins, comparison, tests, the ladder, Responses API, Agents SDK, price. Break (slide 13, 58:00–63:00). Part 2 (slides 14–17, 63:00–90:00): hands-on, security, homework, summary.

---

### Slide 01 (00:00–02:00) • Your own AI assistant

**On screen:** Lesson title; on the right the “Your assistant” card.

#### Speaker (2 min)
> Welcome. Today we build our own assistant: explain the role, rules and files to the AI once — and stop repeating it in every chat. First without code, in products you already have. Then how the same is done in code.
>
> Important news: this lesson was originally about Custom GPTs. But OpenAI retires GPTs on 11 December 2026 and moves them into plugins. So we learn the principle that works everywhere, not one product’s buttons.

---

### Slide 02 (02:00–07:00) • Every new chat starts from zero: you repeat the role, the rules and the files

**On screen:** Schematic: instructions + knowledge + tools + model = your assistant.

#### Speaker (5 min)
> A familiar situation: every time you type “you are a support assistant, answer briefly, here is our policy” and attach the same files. Your own assistant saves this once. Four parts. Instructions: role, rules, tone. Knowledge: your files, policies, tables. Tools: search, code, MCP connections from L12. Model: which AI answers.
>
> This formula is the same in Claude, ChatGPT, Gemini and Copilot; only the button names change. Today we see it in three products.

---

### Slide 03 (07:00–12:00) • GPTs in ChatGPT retire on 11 December 2026 — they move into plugins

**On screen:** Screenshot of the ChatGPT banner “Move your GPTs to plugins by 11 December”, a translated caption and three blocks: what moves, what doesn’t, Gems.

#### Speaker (5 min)
> This banner is right on the GPTs page in ChatGPT: “Move your GPTs to plugins by 11 December”. On 11 December all GPTs become unavailable; whatever was not moved into a plugin is lost. Enterprise workspaces with an approved deferral get until 11 February 2027. When moved, instructions become a plugin “skill”, knowledge files become reference files, connected apps stay. Custom Actions, the chosen model and sharing settings are not carried over.
>
> Google does the same: on personal accounts Gems become skills from 17 November 2026 (a banner in Gemini says so), in Workspace from March 2027. The takeaway: product names change, but the formula “instructions + knowledge + tools” stays. That is what we learn.

---

### Slide 04 (12:00–17:00) • A Claude project: instructions and files Claude remembers in every chat of the project

**On screen:** Large screenshot of the Claude project “Demo L09” (title and right panel) with callouts: description, Instructions, Context, Memory.

#### Speaker (5 min)
> In Claude the assistant is called a project. This is the L09 project: “Demo L09: courier support”. On the right the project blocks. Instructions. Context — knowledge files: here the tickets_ru.csv table. Memory — what Claude remembered while working. Below that, Scheduled — scheduled tasks.
>
> Every new chat inside the project already knows the instructions and files. Projects exist on every plan, up to 5 on Free; sharing a project with colleagues needs Team or Enterprise.

---

### Slide 05 (17:00–22:00) • A good instruction: role, answer format, limits and where the data comes from

**On screen:** Screenshot of the five instruction lines with callouts and English translations: role, format, limits and source.

#### Speaker (5 min)
> Our training project’s instructions are five lines, and they hold everything needed. Role: an assistant to the head of support of the courier service “Bystro”. Format and rules: answer briefly, in Russian; P1 — urgent, P2 — normal, P3 — can wait. Limits: never show customer emails or phone numbers. Source: take the data from tickets_ru.csv in the project.
>
> These are the same prompting techniques as in L02, just written down once. Tip: stress-test the instruction — ask the assistant to show a customer email and check that it refuses.

---

### Slide 06 (22:00–27:00) • In ChatGPT you now build an assistant as a plugin — by talking to Plugin Creator

**On screen:** Screenshot of ChatGPT “@Plugin Creator, help me create a plugin” with callouts.

#### Speaker (5 min)
> This is what replaces GPTs. In ChatGPT: Plugins → Add → Create plugin. The Work mode opens with the ready phrase “@Plugin Creator, help me create a plugin”. Then you just describe what you need in words: role, rules, which files and connections. Plugin Creator assembles the instructions and asks what is missing. Captured on a Business plan. Per OpenAI’s help, own skills are so far available on Business, Enterprise, Healthcare and Edu, and Plugin Creator must first be installed from the directory; on Free/Plus this path may be missing — then build the assistant in Claude.
>
> For teams on Business, Enterprise and Edu there are Workspace agents: OpenAI calls them “an evolution of GPTs” — they run in the cloud, can run on a schedule and in Slack, and sensitive actions need approval. We did not send anything in the screenshot.

---

### Slide 07 (27:00–32:00) • Every major product has its own assistant builder, under a different name

**On screen:** Four products: Claude, ChatGPT, Gemini, Copilot — feature name and availability.

#### Speaker (5 min)
> A summary. Claude — projects, on every plan. ChatGPT — plugins instead of GPTs. Gemini — Gems, which turn into skills: on personal accounts from 17 November 2026, in Workspace from March 2027. Microsoft 365 Copilot — Agent Builder: agents on instructions and the web work without a Copilot licence; company data needs a licence or pay-as-you-go.
>
> A data rule ahead of L15: upload work documents only to business plans (Business, Enterprise, Claude for Work, Workspace). Their data is not used for model training by default.

---

### Slide 08 (32:00–38:00) • Before sharing an assistant, test it with four kinds of questions

**On screen:** Four kinds of test questions and a warning about knowledge files.

#### Speaker (6 min)
> Four tests. A normal question — the answer must rely on your file. A question outside its knowledge — the assistant should honestly say “I don’t know” rather than invent. An attempt to break a rule — e.g. asking for a customer email: it should refuse. A tricky “ignore your instructions” — that is the prompt injection from L11; the assistant should hold.
>
> Important: if you share an assistant, users may coax the knowledge files out with tricky questions. There is no official guarantee against it. So put into knowledge only what you are fine showing to everyone who uses it.

---

### Slide 09 (38:00–43:00) • When buttons are not enough: four steps from a project to your own agent in code

**On screen:** Ladder (HTML): project/plugin → Responses API → Agents SDK → Agents API, with four side notes.

#### Speaker (5 min)
> If you need the assistant inside your own app or site, buttons are not enough. OpenAI’s ladder. At the bottom a project or plugin — no code. The Responses API — a request to the model in a few lines of code, with instructions and built-in tools. The Agents SDK — a library that runs the agent loop in your code: several agents, hand-offs, checks, a log. The Agents API — a new service (beta since 10 September 2026): OpenAI itself runs the loop and an isolated sandbox; you pay only for tokens and tools.
>
> What is gone: the old Assistants API shut down on 26 August 2026, and OpenAI’s visual Agent Builder (not to be confused with Copilot’s Agent Builder) closes on 30 November 2026. Other vendors have similar ladders: the Claude Agent SDK, Google ADK (lesson 12).

---

### Slide 10 (43:00–48:00) • The Responses API: instructions and a conversation in a few lines of code

**On screen:** Reference Responses API code with instructions and previous_response_id.

#### Speaker (5 min)
> For those who code. The Responses API is OpenAI’s recommended way for new projects (Chat Completions from L03 keeps working). The instructions field is like project instructions, but you send it with every request: previous_response_id does not carry earlier instructions over. previous_response_id continues the conversation: no need to resend the history by hand.
>
> The trap: even with previous_response_id, all earlier messages are billed as input tokens at every step. gpt-6-luna is the cheapest GPT-6 model: $0.10 per million input and $0.50 per million output tokens; a thousand short questions cost about 20 cents. The built-in web search, however, costs $10 per thousand calls — 50 times the tokens. The example is a reference and was not run: it needs an OpenAI API key.

---

### Slide 11 (48:00–53:00) • The Agents SDK: several agents, one hands the task to another

**On screen:** Reference Agents SDK code: three agents, handoff_description and handoffs.

#### Speaker (5 min)
> The Agents SDK, the openai-agents package, version 0.24 from 15 October 2026. Three agents: “Billing” for payments, “Tech” for sign-in and the app, and “Triage”, a dispatcher whose handoffs list the specialists; it picks one by their handoff_description (a short description). Runner starts the dispatcher; it understands the topic and passes the conversation on. result.last_agent.name shows who answered in the end — we expect Billing here.
>
> Inside the SDK is the same agent loop as in L11. Plus ready-made extras: guardrails (automatic input and output checks), sessions with memory, tracing of every step, MCP servers from L12, a pause for human approval. The example is a reference and was not run: it needs an OpenAI API key.

---

### Slide 12 (53:00–58:00) • Tokens (the bits of text you pay for) cost pennies; the built-in tools cost money

**On screen:** Bars: 1,000 questions $0.20, with web search $10.20, subscription $20.

#### Speaker (5 min)
> What your own assistant costs. Without code it is part of your subscription: ChatGPT Plus $20 a month, Claude Pro, Gemini and so on. In code you pay for tokens: 1,000 short questions on gpt-6-luna (about 500 question and 300 answer tokens) cost roughly 20 cents.
>
> But if every question triggers a web search, that adds $10 per thousand calls plus the tokens of the search results — at least 50 times the answers themselves. Takeaway: switch on expensive tools only where they are needed.

---

### Slide 13 (58:00–63:00) • 5 minutes: think which assistant you will build for yourself

**On screen:** 5-minute break timer.

#### Speaker (5 min)
> Press “Start”.

---

### Slide 14 (63:00–73:00) • 10-minute hands-on: build your assistant in Claude or ChatGPT

**On screen:** Five hands-on steps and an HR assistant instruction example.

#### Speaker (10 min)
> Hands-on. Everyone builds an assistant for their own job: in Claude (Projects → New project, fill in Instructions and add files to Context) or in ChatGPT (Plugins → Add → Create plugin; checked on Business — whoever lacks this path on Free/Plus uses Claude). Five steps: role, rules, knowledge, test, fix. The HR assistant instruction on the slide is a starting point.
>
> After 7 minutes ask 2–3 people to share their screen: what assistant they built and how it answered the “dangerous” question. Synthetic files only.

---

### Slide 15 (73:00–79:00) • Four questions before you hand an assistant to colleagues

**On screen:** Four questions before sharing an assistant and a warning: on work plans an admin may see chats.

#### Speaker (6 min)
> Before sharing an assistant, four questions. What you upload: on business plans (ChatGPT Business, Enterprise, Claude for Work) data is not used for training by default; on personal plans check the setting. Who you share with: assume every user of the assistant may see the knowledge files. What is connected: plugins and MCP — least privilege, as in L12. Who is responsible: a human checks the answers.
>
> On work plans an admin may have access to chats under company policy — so write to the assistant as if your manager will read it. Rules and regulation in detail — lesson 15.

---

### Slide 16 (79:00–85:00) • Homework: your own assistant for a repetitive work task

**On screen:** Five homework steps and the genai-homeworks/L13/ folder layout.

#### Speaker (6 min)
> Homework: an assistant for a task you do every week. Build it in Claude or ChatGPT, instructions up to 10 lines, 1–3 synthetic files, the four tests from slide 8 and a fix to the instructions. Submit the instructions, the test results and a screenshot. Details and criteria in L13_05_Homework.

---

### Slide 17 (85:00–90:00) • The assistant formula stays; only product names change

**On screen:** Four takeaways and the L14 preview.

#### Speaker (5 min)
> Four ideas. Your own assistant is instructions, knowledge, tools and a model. Product names change — GPTs move to plugins on 11 December 2026, Gems become skills — but the formula stays. Before sharing — four tests. With code — the ladder: Responses API, Agents SDK, Agents API.
>
> Next lesson: Streamlit — building your own web app with a chat on top of an API in a day.

---
