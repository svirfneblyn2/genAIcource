# Instructor Script • Lesson 14: Rapid AI App Prototype — Streamlit and No-Code Builders (90 Minutes)

**Course:** GenAI Basics • Module 6 (Idea to Product) • Lesson 14 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. A coding agent writes the code; students learn to understand and check it (slide 4 is a reference).
**Format:** 17 slides (`presentation_L14_Streamlit_Rapid_Prototyping_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 12 • 10-minute hands-on on slide 13
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).
**Facts:** as of 16.10.2026, sources in `L14_08_Source_Notes_Research_2026-10.md`.

> **Before class:** open llm-examples.streamlit.app (the official demo chat; it may be asleep and take up to a minute to wake) and aistudio.google.com/apps (Build). If you run Streamlit live — Python 3.11+, `pip install streamlit`, `streamlit run app.py`.

**Lesson objective:** students understand why a rapid prototype helps, how Streamlit works (Python, reruns, session_state, cache, secrets), can brief a coding agent and run the prototype, know where to publish it and the risks, and when a no-code builder is enough.

---

## Timing (17 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Rapid AI app prototype | 00:00–02:00 | 2 |
| **02** | A prototype answers “what will it look like?” in a day, not a quarter | 02:00–07:00 | 5 |
| **03** | Streamlit is a web page in Python: no HTML, no JavaScript | 07:00–12:00 | 5 |
| **04** | The whole chat is 14 lines: show history, take the question, ask the model, show the answer | 12:00–18:00 | 6 |
| **05** | On every click Streamlit reruns the whole file — that is why memory is needed | 18:00–23:00 | 5 |
| **06** | Memory, cache and secrets — three things not to mix up | 23:00–28:00 | 5 |
| **07** | A coding agent writes the code; you set the task and check the result | 28:00–33:00 | 5 |
| **08** | Four steps: install, run, edit, show | 33:00–38:00 | 5 |
| **09** | Where to show a prototype: your computer, the free Streamlit cloud or your company cloud | 38:00–43:00 | 5 |
| **10** | Sometimes a builder is enough: an app from a description, no code at all | 43:00–49:00 | 6 |
| **11** | Choose by two questions: what you are showing and whether you will read code | 49:00–54:00 | 5 |
| **12** | 5 minutes: think which prototype you will show colleagues | 54:00–59:00 | 5 |
| **13** | 10-minute hands-on: a helper prototype for your FAQ | 59:00–69:00 | 10 |
| **14** | Four prototype rules: keys, data, money, sign-in | 69:00–74:00 | 5 |
| **15** | What changes when a prototype becomes a product | 74:00–79:00 | 5 |
| **16** | Homework: a prototype and feedback from three real people | 79:00–85:00 | 6 |
| **17** | A prototype in a day, memory in session_state, keys in secrets, you check the code | 85:00–90:00 | 5 |

Part 1 (slides 01–11, 00:00–54:00): why a prototype, Streamlit, code, reruns, memory/cache/secrets, the agent, running, publishing, builders, choosing. Break (slide 12, 54:00–59:00). Part 2 (slides 13–17, 59:00–90:00): hands-on, security, the path to a product, homework, summary.

---

### Slide 01 (00:00–02:00) • Rapid AI app prototype

**On screen:** Lesson title; a chat-window sketch on the right.

#### Speaker (2 min)
> Welcome. So far we have used other people’s windows: ChatGPT, Claude, AI Studio. Today we build our own AI web app that we can show colleagues and clients. The tool is Streamlit: a web page in plain Python, no HTML. A coding agent writes the code; we learn to understand and check it.

---

### Slide 02 (02:00–07:00) • A prototype answers “what will it look like?” in a day, not a quarter

**On screen:** Schematic: idea → prototype (1 day) → feedback (3 people) → product; a “this lesson” bracket.

#### Speaker (5 min)
> A typical story: the idea “a bot that answers staff from our policy” is discussed for months. A one-day prototype changes the conversation: people open a link, ask their own questions, see the mistakes and say what they really need. That feedback is worth more than another model comparison.
>
> Four stages: the idea in one sentence, a prototype in a day, feedback from three real people, and only then a product that engineers take on: security, scale, support. Today we cover the first three.

---

### Slide 03 (07:00–12:00) • Streamlit is a web page in Python: no HTML, no JavaScript

**On screen:** Excerpt of the official llm-examples.streamlit.app chat screenshot with callouts: key field, messages, input box.

#### Speaker (5 min)
> This is the official example from the Streamlit team at llm-examples.streamlit.app. On the left a sidebar with a field for the API key, in the middle the chat messages, at the bottom the input box. This whole interface is about twenty-five lines of Python, no HTML or JavaScript. Streamlit is free and open source; the current version is 1.66 from 14 October 2026, and it needs Python 3.11 or newer.
>
> Note the key field in the example: the user types the key in. For your own prototypes, do not do that — keys and secrets are on slide 6.

---

### Slide 04 (12:00–18:00) • The whole chat is 14 lines: show history, take the question, ask the model, show the answer

**On screen:** Reference 14-line chat code (with an ask_llm stub, runs as is) with session_state, chat_input and ask_llm highlighted.

#### Speaker (6 min)
> The code behind the chat on the previous slide, simplified. You do not need to be able to write it — an agent will. But you should understand four parts. One: session_state — memory. Without it the chat history would be wiped after every message (why — next slide).
>
> Two: the loop that shows the whole history with st.chat_message. Three: st.chat_input — the input box; when someone sends a question we add it to the history and show it. Four: ask_llm — your model call. At the top of the file it is a stub that just echoes the question, so the code runs at once; later it is replaced with the L03 API call: Gemini, OpenAI or the local model from L10. The answer goes into the history and is shown too. To run: streamlit run app.py — a page opens in the browser.

---

### Slide 05 (18:00–23:00) • On every click Streamlit reruns the whole file — that is why memory is needed

**On screen:** Loop schematic: click → the file reruns → memory restored → page redrawn.

#### Speaker (5 min)
> Streamlit’s key feature. An ordinary program runs once. Streamlit reruns the whole app.py from top to bottom on every user action — a click, typed text — and redraws the page. That keeps the code simple, but anything held in ordinary variables is lost.
>
> That is why session_state exists — memory that survives the rerun, separate for each visitor. If a student complains “my chat gets wiped”, the history is almost always not in session_state.

---

### Slide 06 (23:00–28:00) • Memory, cache and secrets — three things not to mix up

**On screen:** Three cards: session_state, cache_data, secrets.

#### Speaker (5 min)
> Three ideas beginners confuse. session_state — one visitor’s memory. cache_data (the st.cache_data command) — a shared cache for every visitor: for example, faq.md is read once, not on every click. That is why you never put personal data or keys in the cache: everyone would see them.
>
> secrets — API keys. They live in .streamlit/secrets.toml and are read through st.secrets. The file goes into .gitignore, otherwise the key ends up on GitHub. GitHub blocks pushing detected keys to public repos by default, but do not rely on that.

---

### Slide 07 (28:00–33:00) • A coding agent writes the code; you set the task and check the result

**On screen:** Coding-agent prompt: a Streamlit chat over faq.md with a demo mode and secrets.

#### Speaker (5 min)
> How it is done in practice. You do not write the code by hand — you give a coding agent (Codex, Antigravity, Claude Code) a good task. It says what to build, with what, where the key is, what to do without a key, where to keep the history, how not to leak the key and, most importantly, asks to explain the code. What a coding agent is and how to choose one: L16.
>
> New since spring 2026: Streamlit has an official streamlit skills command. It plugs skills into the agent — instructions from the Streamlit authors on building apps properly. Claude Code, Codex and Cursor understand them. A demo mode without a key is a good habit: you can show the prototype at a meeting even before you have a key.

---

### Slide 08 (33:00–38:00) • Four steps: install, run, edit, show

**On screen:** Four steps: install, run, edit, show.

#### Speaker (5 min)
> Four steps. Install: pip install streamlit, Python 3.11 or newer. Run: streamlit run app.py — a browser opens at localhost:8501; localhost, as in L10, means “this computer”. Edit: save the file, Streamlit offers Rerun, the page refreshes. Show: via screen share or by publishing to Community Cloud.

---

### Slide 09 (38:00–43:00) • Where to show a prototype: your computer, the free Streamlit cloud or your company cloud

**On screen:** Three places to publish and the warning “a public link = public data”.

#### Speaker (5 min)
> Three places. Your own computer: free; you see it, and so can colleagues on the office network via the Network URL; everyone else sees it when you share your screen in Teams. Streamlit Community Cloud: free, the app is published from a GitHub repo. An app from a public repo is public; you may have only one private app. It sleeps after 12 hours without visitors, and the first visitor wakes it. The key goes into the app settings, the Secrets section.
>
> Inside a company — Snowflake (the company that owns Streamlit) or your own cloud with role-based access; engineers decide. Hugging Face Spaces, once a popular free option for Streamlit, are no longer free for such apps. The main rule: a public link means public data and your API bill.

---

### Slide 10 (43:00–49:00) • Sometimes a builder is enough: an app from a description, no code at all

**On screen:** Google AI Studio Build screenshot and three no-code builders.

#### Speaker (6 min)
> You do not always need Streamlit. Google AI Studio, the Build section: you write “an app that...” and get a working web app with a preview; you can push it to GitHub or deploy it to Google’s cloud. Apps are private by default, and the Gemini key stays on the server. If you share it, other people’s requests count against your limits.
>
> Claude Artifacts from L09 — small apps right in the chat. Lovable, Bolt and v0 build a whole site from a description; all have a free tier with a small daily allowance: a few requests a day on Lovable and v0, a token budget on Bolt. Streamlit wins when you need Python data work, your own files and full control over the code.

---

### Slide 11 (49:00–54:00) • Choose by two questions: what you are showing and whether you will read code

**On screen:** 2×2 grid: show an idea / work with data × code / no code.

#### Speaker (5 min)
> A simple choice table. To show an idea quickly without coding — AI Studio Build or Claude Artifacts. To work with data without your own app — Claude or ChatGPT with files, as in L08. If you are ready to read code with an agent — Streamlit: your own UI and rules, and with pandas, tables and charts from your files.

---

### Slide 12 (54:00–59:00) • 5 minutes: think which prototype you will show colleagues

**On screen:** 5-minute break timer.

#### Speaker (5 min)
> Press “Start”.

---

### Slide 13 (59:00–69:00) • 10-minute hands-on: a helper prototype for your FAQ

**On screen:** Five hands-on steps: an FAQ helper prototype; two paths and a 7 + 3 minute timing.

#### Speaker (10 min)
> Hands-on. Everyone builds a helper prototype for their own FAQ: 10 questions and answers, made up or anonymised. Without code — via AI Studio Build. With code — the slide 7 prompt to a coding agent. After 7 minutes 2–3 people share their screen: what they asked and what the prototype answered.

---

### Slide 14 (69:00–74:00) • Four prototype rules: keys, data, money, sign-in

**On screen:** Four rules: keys, data, money, sign-in.

#### Speaker (5 min)
> Four rules. Keys: only in secrets; do not paste a key into the chat with a coding agent — it may end up in logs. Data: a public prototype gets synthetic data only. Money: set a spending limit in the API console and add a demo mode with no key. Sign-in: if the prototype is not for everyone, make it private in Community Cloud and invite people by email. For engineers: Streamlit also has built-in sign-in with st.login.

---

### Slide 15 (74:00–79:00) • What changes when a prototype becomes a product

**On screen:** “Prototype → product” comparison on four points.

#### Speaker (5 min)
> The prototype has done its job: it showed the idea and gathered feedback. Then it goes to engineers, and much changes. The code lives in a repo with reviews and tests. The data is real, so access rights and logs are needed. The key is not your personal one but a service key with limits and monitoring. And the app must work for everyone, around the clock. Agentic product development — lesson 16.

---

### Slide 16 (79:00–85:00) • Homework: a prototype and feedback from three real people

**On screen:** Five homework steps and the folder layout.

#### Speaker (6 min)
> Homework: a prototype for your work and, above all, feedback from three colleagues. Build it any way — Streamlit with an agent or AI Studio Build. Synthetic data only. Show it to three people, record what they said and three changes you would make. Grading looks not at polish but at how much the prototype helped you understand the task. Details in L14_05_Homework.

---

### Slide 17 (85:00–90:00) • A prototype in a day, memory in session_state, keys in secrets, you check the code

**On screen:** Four takeaways and the L15 preview; the title is the lesson’s main point.

#### Speaker (5 min)
> Four ideas. A prototype in a day is more useful than a month of meetings. Streamlit is Python plus a rerun on every click, so memory lives in session_state. Keys only in secrets; a public link means public data. The agent writes the code, and you check it and ask for explanations. Next lesson — responsible AI, security and law.

---
