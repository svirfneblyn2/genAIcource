# 1-Page Speaker Cheatsheet • Lesson 07 (v3: 22 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: The Microsoft Copilot ecosystem, an overview • facts as of 2026-10-13*  
*Presentation: `presentation_L07_Copilot_Ecosystem_EN_v3.html` (PDF: same basename) • source: `deck_v3/build.py` • full script: `L07_02_Instructor_Script_90MIN_v3_EN.md`*  
*Demo: `L07_04_Live_Demo_Runbook_v3_EN.md` • Homework: `L07_05_Homework_v3_EN.md` • Facts: `L07_12_Research_MS_Ecosystem_2026-10-13.md`, `L07_13_Research_Windows_AgentBuilder_2026-10-13.md`*

---

### Before you start (Teams)
* Share your **whole screen**: the Copilot app (personal and IT Park school sign-in), Teams, Word, Notepad. Keep `meeting_notes.md`, `release_checklist.txt`, `orders.csv` open.
* Live parts: **sl. 7** the Copilot app, briefly (3 min: what is in it + the brief) • **sl. 8** demo B: Vision over the checklist (≈3 min) • **sl. 10** Teams (6 min) and **sl. 11** Word (5 min): the main live demos • optional **sl. 17** demo D: your own agent in Agent Builder. Teams polls: **sl. 2** and **sl. 20**. Timer: **sl. 14**.
* **Licence!** Copilot in Teams meetings and the Copilot pane in Word need a **Microsoft 365 Copilot licence**. Our IT Park account = **Copilot Chat (Basic)**, no licence; the EPAM account does not work on this PC. Without a licence Teams has only the Copilot Chat app and Word has no Copilot pane → fallback in the runbook (the slide with official screenshots / Copilot Chat in the sidebar if present / paste the text into Copilot Chat).
* Rule: **“the button moved, the rule did not”**. 90 seconds of searching → the slide with the ready result, move on.
* Part 1 (00:00–52:00) → break (52:00–57:00) → part 2 (57:00–90:00). Prices on **sl. 6** only.

---

### The map: the Microsoft AI family (sl. 2)
One question for every case: **whose information is it and where does it live?**

| Zone | Account | What Copilot sees | Tiles on the slide |
|---|---|---|---|
| **A · For you** | personal, free | the web and what you give it: text, a file, a window on screen | Copilot, Windows 11, Edge, Paint and Photos, Bing |
| **B · Microsoft 365** | work / school | Copilot Chat for free: the web and what you paste; with a licence: your mail, files, meetings, chats (only what is open to you) | Word, Excel, PowerPoint, Outlook, Teams, OneNote, OneDrive, SharePoint, Loop and Pages + **agents**: Researcher, Analyst, Cowork, Facilitator, Agent Builder |
| **C · For developers** | GitHub / Azure | the repository, issues, code | GitHub Copilot, VS Code, Microsoft Foundry, Copilot Studio |
| **D · For the company** | IT turns it on | company data: sales, processes, reports, security | Dynamics 365, Power Apps, Power Automate, Power BI and Fabric, Security Copilot, Agent 365, Dragon Copilot |

**The core inside them all:** OpenAI GPT • Anthropic Claude • Microsoft MAI + what Copilot can see (web, file, mail, screen). The icons on the slide are simplified tiles, not logos.  
Badge colour: green = free • blue = work licence • yellow = preview • violet = Microsoft 365 home subscription.

### New words (sl. 3)
A nesting doll, read from the inside out: each layer = the previous one **+ one new ability**.
* **Model (LLM)**: text in → text out; sees nothing and does nothing by itself (GPT, Claude, MAI: what you called from Python in L03).
* **Chat**: a model + a conversation window and chat memory: question → answer, you do the rest (Copilot Chat: “explain the delivery rule”).
* **Assistant (Copilot)**: lives inside an app and **sees context**: file, email, screen (Copilot in Word: “shorten this paragraph”).
* **Agent**: an assistant that is allowed to act: plans the steps, acts with skills and connectors, **asks “ok?”** (Cowork: “prepare the meeting” → email, file, invite).

Building blocks: **context and knowledge**: what Copilot sees when it answers (the open file, an email, a website, the screen) • **instructions (prompt)**: what and how: role, rules, format; an agent keeps them permanently • **skill**: a ready ability: a Word file, an image, computing with code • **connector**: a “cable” to another service: Gmail, Google Drive, SharePoint (more in L12, MCP).  
Formula: **agent = model + instructions + knowledge + skills + connectors + permission to act**; it confirms important steps with you. On sl. 16–17 we build an agent from these parts.

### Three levels (sl. 4)
Copilot = **a model + what it can see + what it is allowed to do**. **Auto** picks the model for you. Remember the levels, not the model names.
1. **Answers**: chat, question → text, you copy it yourself.
2. **Edits the document**: Word, Excel, PowerPoint change the file, you see what changed.
3. **Does the work (agent)**: plans the steps itself, **asks for approval** before anything important (Cowork, Researcher, Autopilot).

### What is free (sl. 6; US prices as of 13 Oct 2026)
* **Free:** personal Copilot $0 • Copilot Chat on a work / school account $0 • GitHub Copilot Free $0 • GitHub gives students **Copilot Student**. Enough for the lesson and the homework.
* **Home, per month:** Microsoft 365 Personal $9.99 • Family $12.99 • Premium $19.99 (includes Researcher and Analyst).
* **Work, per user per month, annual:** Copilot Business $21 • Microsoft 365 Copilot $30 • GitHub Copilot Business $19.
* **Agents** (Cowork, Code, Autopilot, newest models): pay as you go, in credits; GitHub AI Credits $0.01.
* Expect changes after Microsoft Ignite (17–20 Nov 2026). Copilot Chat ≠ Microsoft 365 Copilot: the first is free and sees the web and what you paste; the second is a paid licence and sees your work data.

### Copilot in Windows (sl. 9; personal account, official as of 13 Oct 2026)
* **Free on any Windows 11 PC:** chat and voice (the Copilot key or **Win+C**; “Hey Copilot” is an optional setting) • screenshot and **Vision**: highlights **but does not click** • files: upload or find on the PC • create an image or a Word / Excel / PowerPoint file from an answer • connectors to OneDrive, Outlook.com, Gmail, Google Drive, Calendar: on copilot.com and mobile.
* **Official limits:** **20 files** per chat • **50 MB** per file (PDF, DOCX, XLSX, PPTX, PNG, JPEG, TXT, CSV, MD) • chat history kept **18 months**.
* **Not published:** message, prompt-length, image and voice-minute limits. Numbers like “15 fast images” are unofficial. A Microsoft 365 subscription gives “more”, without numbers.
* **Copilot+ PCs only** (with an NPU): Click to Do, Recall, the Settings agent. Copilot Actions: Insiders only for now.
* **Privacy:** in a personal account training on your chats is **on by default**. Turn it off: profile → Settings → Privacy → **Training on conversation activity**. Work and school accounts are never used for training.
* **Edge:** questions about open tabs and history, Journeys. The separate Copilot Mode closed in May 2026; browser actions: Premium, US only.

### Your own agent: Agent Builder (sl. 16–17)
**Agent = Copilot + your instructions + your knowledge.** Where: the Copilot app, school / work account → **Agents → New agent**. Available **even in free Copilot Chat** (checked on 13 Oct 2026 on the IT Park account); IT can switch it off. No official confirmation for personal accounts. Not in the mobile app.

| Part of the agent | What it is | In free Copilot Chat |
|---|---|---|
| **Instructions** | who you are, how you answer, what you never do | ✅ |
| **Knowledge** | where the agent looks for answers | ✅ the web and **up to 4 public sites** (up to two path levels, no query parameters) • ❌ uploaded files, SharePoint, connectors: only if the organisation enabled **pay-as-you-go** billing • ❌ mail, Teams, people: only with a **licence** |
| **Skills** | code (documents, charts) and images | ✅ on by default |
| **Starter prompts** | suggestion buttons for the user | ✅ |

**Field limits:** name **up to 30 characters** • description **up to 1,000** • instructions **up to 8,000** characters • icon PNG 192×192, up to 1 MB.  
**Steps (our run, 13 Oct 2026):** describe it in words (“Courier support helper”, the Prime rules) → Agent Builder writes the name, description, instructions and 4 starter prompts → **Preview**: “Prime, $80, outside the city” → **$18.00** (correct); “delivery for $70?” → **asked back for the zone and Prime** → **Create** → the agent is **private**; share with the **Share** button (by link or with the organisation if IT allows). Edits after creation go live only after **Update**.  
Agent Builder agents do not work in Teams group or 1:1 chats. For workflows, system connections and publishing to a website: **Copilot Studio** (L12).

### 5 lesson rules (sl. 22)
1. First ask: **whose information is it and where does it live?** • 2. Same models inside; the difference is **what Copilot sees and is allowed to do** • 3. Free: personal Copilot, Copilot Chat, GitHub Copilot Free • 4. An agent does the work but **asks for your “yes”** • 5. Every answer is a draft: **check the numbers**.

Plus the safety rules (sl. 20): Copilot sees only what you can open • work data is protected by contract (the green shield); in a personal account **turn training off** • **no passwords, keys or customer data in chat** • an answer is a draft.

### Name dictionary (sl. 5)
| Was | Now |
|---|---|
| Office app → Microsoft 365 Copilot app | **Microsoft Copilot** (one app, since September 2026) |
| Bing Chat | **Copilot** |
| Copilot Pro | retired → **Microsoft 365 Premium** |
| Designer | the image editor inside Copilot |
| Copilot Mode in Edge | closed 13 May 2026, features moved into regular Edge |
| `=COPILOT()` in Excel | removed 14 Sep 2026; use the Copilot pane (edit / plan / chat only) |
| Azure AI Foundry | **Microsoft Foundry** |
| Scout | **Autopilot** (preview) |

---

### Key demo numbers
Brief: **$75 Prime in the city only • $100 for all stays • outside the zone unchanged • flag owner is an open question** • checklist: **item 6** “Roll back the flag if outside-zone fees change unexpectedly” • orders (`orders.csv`, 12 rows): city Prime from $75 = **1001, 1004, 1006, 1009** (4, all free); outside the zone **only 1011** is free ($130, the “from $100” rule). On 13 Oct 2026 free Copilot Chat, with no rule in the prompt, twice counted “3 free outside the zone”: wrong.  
Agent (sl. 17): city $7.50 • outside $18.00 • “Prime, $80, outside the city” → **$18.00** • “$70?” → ask for the zone and Prime.  
**Game (sl. 20):** 1-B • 2-A • 3-C • 4-A.

### Verify before recording
Plan names and prices (sl. 6), Copilot Business promo dates • Autopilot, Code, @Copilot in Teams (preview, may change at Ignite 17–20 Nov) • Vision for work accounts • the model list in the menu (sl. 4) • Windows limits (sl. 9) and Agent Builder button labels (sl. 16–17) • both sign-ins work on the demo PC and the school account shows **New agent** • whether you have a licence for live Teams and Word. Full list: `README_v3.md`, section “Verify before recording”.
