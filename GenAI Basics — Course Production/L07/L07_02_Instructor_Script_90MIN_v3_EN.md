# Instructor Script • Lesson 07 (v3): The Microsoft Copilot Ecosystem, an Overview (90 Minutes)

**Course:** GenAI Basics • Lesson 07 of 16 • Module 3: AI assistants at work
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** IT Park University students, GenAI beginners from many roles. Plain language, no formulas, no code.
**Format:** 24 slides (`presentation_L07_Copilot_Ecosystem_EN_v3.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v3/build.py` (slide text, minutes in `MINUTES`, speaker notes). This script is generated from it (`deck_v3/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the demo kit `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv`, `fallback_outputs/`; `sample_repo/` is the backup example for slide 20 and the bridge to L16), runbook `L07_04_Live_Demo_Runbook_v3_EN.md`, homework `L07_05_Homework_v3_EN.md`, cheatsheet `L07_00_Lecture_Cheatsheet_v3_EN.md`, plan `L07_11_Lesson_Plan_v3_Ecosystem.md`.
**Facts:** as of 13 Oct 2026, sources in `L07_12_Research_MS_Ecosystem_2026-10-13.md`. Prices on slide 7 only. The “verify before recording” list is in `README.md`.

> **Before you start (Teams):** two live demos: A (slide 8, Copilot Chat on the IT Park school account + a picture in the personal account) and B (slide 9, Vision over `release_checklist.txt`). Teams polls on slides 2 and 22. Share your **whole screen**: you need the Copilot app and Notepad. Our IT Park account is **Copilot Chat (Basic)**, with no Microsoft 365 Copilot licence, so Teams, Word and Excel (slides 11–13) are shown from the slides. Rule: “the button moved, the rule did not”, at most 90 seconds of searching, then the slide with the ready result.

**Lesson objective:** students draw the map of the Microsoft AI family in four zones (for you, for work, for developers, for the company) and pick a zone by asking “whose information is it and where does it live?”; understand that inside are the same models as in L03 and the difference is what Copilot sees and is allowed to do (answers → edits the document → agent); tell free Copilot Chat from the Microsoft 365 Copilot licence; make a brief and a picture in free Copilot themselves and check the answer against the source; keep passwords, keys and customer data out of the chat.

---

## Timing (24 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Copilot is not a button, it is a family | 00:00–02:00 | 2 |
| **02** | The Microsoft AI family: who lives where | 02:00–07:00 | 5 |
| **03** | Model → chat → assistant → agent | 07:00–09:00 | 2 |
| **04** | Assistant or agent: who drives the work | 09:00–11:00 | 2 |
| **05** | Inside are the same models you called in L03 | 11:00–14:00 | 3 |
| **06** | One Microsoft Copilot app, two doors | 14:00–18:00 | 4 |
| **07** | What is free and what is paid | 18:00–21:00 | 3 |
| **08** | Meeting notes → brief → launch picture | 21:00–24:00 | 3 |
| **09** | Copilot Vision: the assistant sees the window you share | 24:00–27:00 | 3 |
| **10** | Copilot in Windows: what it can do and where the limits are | 27:00–32:00 | 5 |
| **11** | Teams: a meeting becomes a recap and tasks | 32:00–38:00 | 6 |
| **12** | Word: a draft from a file and edits right in the document | 38:00–43:00 | 5 |
| **13** | Excel: ask the table in words, then check the numbers | 43:00–48:00 | 5 |
| **14** | The same button, a different document | 48:00–52:00 | 4 |
| **15** | 5 minutes: coffee and a rest from the screen | 52:00–57:00 | 5 |
| **16** | Agents: Copilot does the work, not just answers | 57:00–61:00 | 4 |
| **17** | Anatomy of an agent | 61:00–63:00 | 2 |
| **18** | An agent is Copilot with your instructions and your knowledge | 63:00–66:00 | 3 |
| **19** | We built a support agent in 5 minutes: a real run | 66:00–71:00 | 5 |
| **20** | GitHub Copilot: Copilot for code (more in L16) | 71:00–75:00 | 4 |
| **21** | Copilot for the company: three examples | 75:00–77:00 | 2 |
| **22** | Where does this question go? | 77:00–82:00 | 5 |
| **23** | Homework: the courier team's week with Copilot | 82:00–87:00 | 5 |
| **24** | The Copilot family in one line: for you · for work · for code · for the company | 87:00–90:00 | 3 |

Part 1 (slides 01–14, 00:00–52:00): the family map, new words (model, chat, assistant, agent), levels, one app, prices, Copilot app overview, Vision, Copilot in Windows (limits), Teams and Word live, Excel, PowerPoint and Outlook. Break (slide 15, 52:00–57:00). Part 2 (slides 16–24, 57:00–90:00): agents, your own agent, GitHub Copilot, Copilot for the company, game and rules, homework, summary.

---

### Slide 01 (00:00–02:00) • Copilot is not a button, it is a family

**On screen:** Background: the official picture of the new Microsoft Copilot (25 Sep 2026). Title “Copilot is not a button, it is a family”, the lesson plan, “facts as of 13 Oct 2026”, key hints.

#### Speaker (2 min)
> “You have seen the word Copilot everywhere: Windows, Edge, Teams, Word, GitHub. Today we sort out what this family is, how its members differ, and what you can open today for free.”
>
> In the background is Microsoft's official picture of 25 September 2026: in September the personal and work Copilot were merged into one app. This is the news of the season; we come back to it on slide 6.
>
> Running example: our courier team from L04–L06: Anna (product), Pavel (developer), Ola (support) and one feature: Prime subscribers get free delivery from $75 in the city. All data is made up.
>
> Before class: open Copilot (personal and work sign-in), prepare the Teams poll for slide 2, keep demo_courier_copilot/meeting_notes.md and release_checklist.txt open.

---

### Slide 02 (02:00–07:00) • The Microsoft AI family: who lives where

**On screen:** Teams poll “which Copilot do you already have?” and a map of four zones: for you, for work, for developers, for the company. Each zone has a “Sees” line and products with an availability dot; the colour legend below.

#### Speaker (5 min)
> Poll first (1 min): “Which Copilot do you already have?” “None” is almost always wrong: Copilot ships with Windows 11 and Edge, and IT Park students have a school account with Copilot Chat.
>
> Walk the map. For you: the Copilot app, Copilot in Windows 11 and Edge, images in Paint and Photos, Bing search: personal account, free. In the centre is Microsoft 365, the work and school suite: Word, Excel, PowerPoint, Outlook, Teams, OneNote, OneDrive, SharePoint, Loop and Pages. Every app has a Copilot button; with free Copilot Chat it answers from the web and pasted text, with a Microsoft 365 Copilot licence it sees your mail, files and meetings. Here too are the agents: Researcher, Analyst, Cowork, Facilitator in Teams and Agent Builder for your own agents.
>
> On the right, developers: GitHub Copilot in VS Code and on github.com, Microsoft Foundry for models and agents in your own apps, Copilot Studio for building agents and workflows. Below, company products, turned on by IT: Dynamics 365, Power Apps, Power Automate, Power BI and Fabric, Security Copilot, Agent 365, Dragon Copilot for doctors. And the common core: OpenAI, Anthropic and Microsoft's own MAI models. Only what Copilot sees and is allowed to do differs.
>
> The icons on the slide are simplified tiles, not official logos.

---

### Slide 03 (07:00–09:00) • Model → chat → assistant → agent

**On screen:** Our four-stage diagram: model → chat → assistant → agent. Each stage has a mini interface, a Copilot example and one line on what it adds.

#### Speaker (2 min)
> “On the map we saw words like Copilot, agents, Agent Builder. Before we go on, let's agree on what they mean.”
>
> Read left to right. A model is the LLM, the large language model you called from Python in L03: text in, text out. By itself it sees nothing and does nothing. A chat is a model plus a conversation window: you ask, it answers and remembers this conversation. Example: Copilot Chat. An assistant lives inside an app and sees your file: Copilot in Word highlights a paragraph and suggests an edit, but you decide and do the work. An agent gets a goal, “prepare Friday's client meeting”, and runs the loop plan → act → check by itself: drafts the email, books the meeting, prepares the file. It reaches email, calendar and files through connectors. You approve the result. Example: Copilot Cowork.

---

### Slide 04 (09:00–11:00) • Assistant or agent: who drives the work

**On screen:** Our “assistant or agent” diagram: left “you drive” (request → answer in Word → you take the next step), right “it drives, you approve” (goal → loop plan → act → check over email, calendar, files → your approval).

#### Speaker (2 min)
> “This is the most important difference in today's lesson. Remember: either you drive, or it drives.”
>
> On the left is the assistant. You ask “shorten this paragraph”, Copilot answers right in Word, you accept the edit and take the next step yourself. One request, one answer. On the right is the agent. You set a goal: “prepare Friday's client meeting”. The agent plans, acts and checks by itself: looks at the calendar, drafts the email, builds the file. Before important actions such as sending the email it asks for your “yes”. One goal, many steps, then your OK.

---

### Slide 05 (11:00–14:00) • Inside are the same models you called in L03

**On screen:** A three-step ladder: answers → edits the document → does the work (agent). Two lines on models (OpenAI GPT, Anthropic Claude, Microsoft MAI, Auto). On the right our capture of the model menu in the IT Park work Copilot.

#### Speaker (3 min)
> “In L03 you called a model from Python yourself. Copilot makes the same call for you and adds your context to the request: a file, an email, the screen.”
>
> Three levels keep the names apart. One: answers, an ordinary chat. Two: edits the document: Copilot in Word or Excel changes the file itself. Three: an agent: you describe the result and it plans and runs the steps, asking before anything important.
>
> On the right is our real capture: the IT Park work Copilot, model menu. You see Auto and GPT-5.6. With a paid licence the menu also shows Claude. At Build 2026 Microsoft showed seven of its own MAI models. Takeaway: Copilot is not one model but several, chosen for the task.

---

### Slide 06 (14:00–18:00) • One Microsoft Copilot app, two doors

**On screen:** Our capture of the account switcher (personal and IT Park work in one app), two cards “Personal / Work”, the official picture of the Home · Code · Autopilot tabs and the name dictionary.

#### Speaker (4 min)
> “If the names confuse you, you are not alone. Microsoft renamed these products several times in two years.”
>
> On the left is our capture: one Microsoft Copilot app with the account switcher. The personal account and the IT Park work account sit side by side, but data does not flow between them. E-mails and photos are hidden.
>
> The key difference at work. Copilot Chat is free for work and school accounts: it answers from the web and from what you paste or upload, with enterprise data protection (the green shield). Microsoft 365 Copilot is a paid licence: Copilot sees your mail, files, meetings and chats. Our IT Park account has Copilot Chat (Basic), no licence. Yours most likely too.
>
> On the right is the official picture: the new app with three tabs. Home: chat and the Cowork agent. Code: build a small app by describing it. Autopilot: a background agent, still in preview. The dictionary below: the Office app became the Microsoft 365 Copilot app, now simply Microsoft Copilot; Bing Chat is Copilot; Copilot Pro was retired and replaced by Microsoft 365 Premium.

---

### Slide 07 (18:00–21:00) • What is free and what is paid

**On screen:** Four price columns as of 13 Oct 2026 (US): free, home, work, agents. An “OCTOBER 2026” badge and a line for IT Park students. The only slide with prices.

#### Speaker (3 min)
> The only slide with prices. “Prices change, so plan names and numbers live only here, with a date.”
>
> Left to right is a ladder. Free: personal Copilot, work Copilot Chat and GitHub Copilot Free. Home: Microsoft 365 Personal, Family and Premium; Premium includes the Researcher and Analyst agents. Copilot Pro is no longer sold. Work: Copilot Business for small companies at $21 and Microsoft 365 Copilot at $30 per user per month.
>
> Agents are a separate story: Cowork, Code, Autopilot and the newest models are billed by usage, in credits. This is new in 2026. Nothing paid is needed for the homework.

---

### Slide 08 (21:00–24:00) • Meeting notes → brief → launch picture

**On screen:** Demo A. Left: our capture of the brief from meeting_notes.md in Copilot Chat on the IT Park school account (no licence). Right: our launch picture from personal Copilot and the three demo steps with the prompt.

#### Speaker (3 min)
> Briefly show what the app has; the live demo is optional. Open the Copilot app with the school account (Copilot Chat), exactly as students will.
>
> Step 1. Paste the meeting notes and the prompt from the slide. The key part is “list what you added yourself”. A simple guard against invention. In our run on 13 Oct, once Copilot said “nothing added”, another time it honestly listed the section structure and an explanation that rollout means a staged launch. The same prompt gives different answers; that is normal, which is why we check.
>
> Step 2. Check against the source out loud with the group: $75 only for Prime and only in the city; free from $100 for everyone stays; nothing changes outside the zone; who owns the flag is an open question.
>
> Step 3. Personal account: “Draw a launch picture…”. On the right is our result. Open the picture: there is a built-in editor: Erase, Upscale, Edit object, Background, Crop. This used to be called Designer. If the network or account fails: this slide is the result; do not troubleshoot for more than 90 seconds.

---

### Slide 09 (24:00–27:00) • Copilot Vision: the assistant sees the window you share

**On screen:** Demo B. A frame from Kevin Stratvert's video: the Copilot window in Windows with the Share screen / Share app choice. Right: the three demo steps with release_checklist.txt and three Vision rules.

#### Speaker (3 min)
> The wow moment. “So far we pasted text into chat. Now Copilot looks at the window itself.”
>
> On the left is a frame from a review: the Copilot window in Windows and the choice of what to share, the whole screen or one app. Choose one app: then Copilot sees nothing extra.
>
> Live demo: open the release checklist, turn on Vision, pick Notepad and ask by voice. The right answer is item 6: “Roll back the flag if outside-zone fees change unexpectedly.” Vision for personal accounts works in 170+ markets; for work accounts it is only rolling out, hence the preview badge.
>
> Fallback without a microphone: paste the checklist text into chat and ask the same question. Same rule as slide 5: Copilot sees only what you show it.

---

### Slide 10 (27:00–32:00) • Copilot in Windows: what it can do and where the limits are

**On screen:** Left: what is free in Windows (chat, voice, Vision, files, file creation, connectors) and the Ask Copilot frame. Right: official limits (20 files, 50 MB, 18 months), what is not published, Copilot+ PC features, how to turn training off in a personal account, a line on Edge.

#### Speaker (5 min)
> “Copilot is already on everyone's Windows. Let's see what it does for free and where it stops.”
>
> What works on a normal Windows 11 PC with a personal account: chat and voice; open with the Copilot key or Win+C; “Hey Copilot” is an optional setting. Screenshot or Vision: you share a window, Copilot highlights where to click but clicks nothing itself. Files: upload one or ask it to find a file on the PC and ask about it. Create an image or a Word, Excel or PowerPoint file from an answer. Connectors to OneDrive, Outlook.com, Gmail and Google Drive work on copilot.com and mobile; Microsoft lists a Microsoft 365 subscription for them.
>
> The only official numbers: up to 20 files per chat, up to 50 MB per file, history kept 18 months. Microsoft does not publish message, prompt-length, image or voice limits for the free tier; numbers like “15 fast images” online are unofficial. Microsoft 365 Personal, Family and Premium give “more”, also without numbers.
>
> Copilot+ PCs with an NPU only: Click to Do, Recall and the Settings agent. Copilot Actions, where an agent works inside apps, is still Insider-only. Privacy: in a personal account training on your conversations is on by default; show where to turn it off: profile, Settings, Privacy, Training on conversation activity. Work and school accounts are never used for training.

---

### Slide 11 (32:00–38:00) • Teams: a meeting becomes a recap and tasks

**On screen:** Official Microsoft screenshots: Facilitator in a meeting and the Recap tab after it. Three points “during / after / needs the transcript” and the team line: 3 decisions, 2 open questions, 3 tasks.

#### Speaker (6 min)
> Live. “This lesson runs in Teams, so you are already sitting inside one of the Copilots.”
>
> On the left is Microsoft's official screenshot: the Facilitator agent in a meeting. It runs the agenda with a timer per topic, writes shared notes participants can edit, and answers questions in the meeting chat. After the meeting it can produce a Word document.
>
> On the right is Recap, the tab after the meeting: AI notes, tasks, chapters, who said what. Inside you can ask Copilot: “which questions are still open?”. All of this needs the transcript turned on and a Microsoft 365 Copilot licence. Without a licence Teams has Copilot Chat and suggested replies.
>
> Wow option if the instructor has a licence: turn on Facilitator for this lesson and show the recap at the end. No licence: show this slide and the rule “the button moved, the rule did not”.
>
> How we show it in this course: Copilot in Teams needs a Microsoft 365 Copilot licence and the IT Park school account has none. So Teams is shown with the screenshots. Live, do the same thing: open Copilot Chat (IT Park), paste meeting_notes.md as a “transcript” and ask “What was decided? What is open? Who does what?”: you get the same recap.

---

### Slide 12 (38:00–43:00) • Word: a draft from a file and edits right in the document

**On screen:** A frame from an official Microsoft video: Copilot in Word with a prompt that points to a file and the “What I updated in the document” report. Right: three moves: draft, edit, check.

#### Speaker (5 min)
> Live. “The same brief we made in chat, only right inside the document.”
>
> A frame from an official Microsoft video (July 2026). The user writes a prompt that points to a file. Copilot works in a few steps and reports on the right: “What I updated in the document”. That is level 2 from slide 5: Copilot edits the file and you see the list of changes.
>
> Three moves: a draft from a file; editing selected text; checking: Copilot highlights the words it changed and adds citations. Needs a work licence; without one, Copilot Chat with pasted text gives the same result, as in demo A.
>
> How we show it: Copilot inside Word needs a licence (without one the Word ribbon only shows “Buy Microsoft 365”, checked 13 Oct 2026). Live in IT Park Copilot Chat: upload meeting_notes (+ → file) and ask “Write a one-page brief and create a Word file”. Then “shorten the Decisions section to three bullets”: that is document editing.

---

### Slide 13 (43:00–48:00) • Excel: ask the table in words, then check the numbers

**On screen:** Left: the official screenshot of the three Copilot modes in Excel. Right: our capture: free Copilot Chat on 12 orders got the outside zone wrong; a plaque with the right answer (only #1011).

#### Speaker (5 min)
> “Excel is where Copilot is strongest and most dangerous: numbers look convincing.”
>
> On the left is the official screenshot: Copilot in Excel now has three modes. Edit changes the workbook directly. Plan shows the steps first and you approve. Chat only changes nothing. If an old video shows =COPILOT() in a cell, it was removed in September 2026.
>
> On the right is our real run in free Copilot Chat: 12 made-up orders, the question “which zone has the most Prime orders from $75 and how many are free now?”. Copilot counted 4 in the city (right) and 3 free outside the zone (wrong). The Prime rule applies only in the city; outside the zone only order 1011 for $130 is free, under the general “from $100” rule. We ran it twice; the mistake repeated.
>
> Takeaway: Copilot did not know the rule because we did not write it, and honestly marked its assumption with an asterisk, but the conclusion is still wrong. Put the rule into the prompt and check a row or two by hand. L08 covers data analysis in depth.
>
> How we show it: Copilot inside Excel via the screenshot on the left. Live in IT Park Copilot Chat: upload orders.csv or paste it as text and ask the slide question; then add the rule “Prime is free only in CITY” and compare the answers. Free, and every student can do it.

---

### Slide 14 (48:00–52:00) • The same button, a different document

**On screen:** Official screenshots: PowerPoint “Visualize this slide” and an Outlook thread summary with citations [1] [2]. The team line: Ola's complaint summary, Anna's 5 slides.

#### Speaker (4 min)
> “Same model, same context rule, only a different document is open.”
>
> PowerPoint. Copilot builds a deck from a Word file and first asks clarifying questions: for whom, which style. In the screenshot is the “Visualize this slide” skill: Copilot turns a text slide into a picture with a diagram. Check numbers and names on every slide: Copilot likes to add nice but invented details.
>
> Outlook. A summary of a long thread with citations to specific emails, the numbers in square brackets. A reply draft and tone. Inbox sorting: “move all newsletters into a folder”; Copilot asks for confirmation if more than five emails are affected.
>
> Without a licence: paste the email text into Copilot Chat and ask for a summary: a similar result.

---

### Slide 15 (52:00–57:00) • 5 minutes: coffee and a rest from the screen

**On screen:** 5-minute timer, Start and Reset buttons, a “next” line.

#### Speaker (5 min)
> Press “Start”. Rest only, no chat tasks.

---

### Slide 16 (57:00–61:00) • Agents: Copilot does the work, not just answers

**On screen:** Three pictures: Researcher (Mike Tholfsen frame, “Generated by GPT — Refined by Claude”), Cowork (Kevin Stratvert frame: plan, an email waiting for “yes”, files), our capture of the Agent Store. Four agents in one line each below.

#### Speaker (4 min)
> “The big trend of 2026: from an assistant that answers to an agent that does.”
>
> Researcher. A frame from Mike Tholfsen's review (April 2026): a market research report, 112 reasoning steps, labelled “Generated by GPT — Refined by Claude”. Microsoft uses two models: one writes, the other checks. That answers why Copilot has several models.
>
> Cowork. A frame from Kevin Stratvert's review (July 2026): on the right the step plan, in the centre an email draft waiting for your approval, below finished PowerPoint, Excel and Word files. The key agent rule: it asks before important actions such as sending an email or a meeting invite. Cowork was built with Anthropic and is billed by usage.
>
> On the right is our capture: the Agent Store exists even in the free IT Park Copilot Chat: Prompt Coach, Writing Coach, Learning. Try Prompt Coach in the homework: it teaches better prompts.

---

### Slide 17 (61:00–63:00) • Anatomy of an agent

**On screen:** Our agent anatomy diagram: the harness around the model with its loop, five parts (instruction, context, tool, skill, connector) and connectors to mail, files and the customer database.

#### Speaker (2 min)
> “We are about to build our own agent. First, let's see which parts it is made of.”
>
> In the centre is the model, the same LLM. Around it is the harness: the program that runs the loop plan → act → check and plugs in five parts. Instruction: role, rules and goal. Context: what the agent sees right now: the conversation, the open file, the results of its steps. Tool: one action, such as “send an email”. Skill: a ready recipe of several steps, such as “build a report”. Connector: access to a company system: mail, files, the customer database (CRM). Connectors and MCP in detail come in L12.
>
> Bridge: on the next two slides we fill these parts in Agent Builder (instructions, knowledge, skills) and get a working agent.

---

### Slide 18 (63:00–66:00) • An agent is Copilot with your instructions and your knowledge

**On screen:** The four parts of an agent (instructions, knowledge, skills, starter prompts), six agent ideas, our capture of the Agent Builder start screen in IT Park Copilot Chat.

#### Speaker (3 min)
> “An agent is not magic: it is Copilot that was told its role once and given the right files. Then it follows those rules every time.”
>
> The four parts of an agent in Agent Builder. Instructions: who you are, how you answer, what you never do. Knowledge: files, websites, SharePoint folders; web search is a toggle. Skills: since autumn 2026 every agent can write code, create Word, Excel and PowerPoint files and generate images by default; we saw this in the “What's new” window. Starter prompts: buttons the user starts with.
>
> An important finding: we checked on 13 Oct 2026, the IT Park school account with free Copilot Chat has the New agent button and the agent gets created. So students can build an agent themselves. Knowledge from SharePoint and Teams is limited on the free tier; IT can switch the feature off in an organisation.
>
> Offer the ideas as homework options. For an agent for a whole company with workflows and system connections, use Copilot Studio; that is L12.

---

### Slide 19 (66:00–71:00) • We built a support agent in 5 minutes: a real run

**On screen:** Four of our captures step by step: description → instructions; knowledge and starter prompts; Preview test ($18.00); agent created, private. Our prompt below.

#### Speaker (5 min)
> Show it live (school account, Agents → New agent) or with these captures: our real run of 13 Oct 2026.
>
> Step 1. Write the description in plain words, the same move as a prompt in L02: role, rules, format, what not to do. Agent Builder invents the name and description and splits the instructions into “Purpose” and “Main rules”. Step 2. The Configure tab: add knowledge (files, sites), toggle web search; it also wrote four starter prompts.
>
> Step 3. Preview: test before publishing. We asked a tricky one: Prime, $80, an address outside the city. The agent answered $18.00 and explained that Prime only applies in the city. The second question had missing data, “how much is delivery for $70?”, and it did not guess but asked for the zone and Prime. That is what good instructions buy you. A detail: in preview the answer was duplicated; the interface is still rough.
>
> Step 4. Create: the agent exists and is private. Share it with the Share button, by link or with the organisation if IT allows. Compare with slide 13: there Copilot got it wrong because it did not know the rule; here the rule is in the instructions, and the answer is right.

---

### Slide 20 (71:00–75:00) • GitHub Copilot: Copilot for code (more in L16)

**On screen:** The official GitHub picture: Copilot reviewing a pull request. Right: four places of GitHub Copilot and our real diff: the Prime rule in 2 lines, 7 tests green.

#### Speaker (4 min)
> “GitHub Copilot is the oldest family member, since 2021. One slide today; all of L16 is about AI for code.”
>
> Where it lives: in the editor it suggests lines, answers in chat, and in agent mode edits files and runs tests itself. On github.com it reviews pull requests (in the picture it finds a problem and suggests a fix) and, as a cloud agent, takes an issue and opens a pull request itself. In the terminal and a separate app. And since October 2026 as an agent in Teams.
>
> Our example: Pavel asked for the Prime rule. The real diff is two lines of logic plus three tests, all seven tests green (demo_courier_copilot/sample_repo). Same rule as everywhere: look at the changes and tests, not at the word “done”. GitHub Copilot Free is enough; GitHub gives students Copilot Student.

---

### Slide 21 (75:00–77:00) • Copilot for the company: three examples

**On screen:** Three tiles with video frames: Microsoft Foundry (model catalogue), Security Copilot (12 of 12), workflows in Copilot Studio. Below a line about Dynamics 365, Power BI / Fabric, Dragon Copilot, Agent 365.

#### Speaker (2 min)
> “You will not open these yourself; IT turns them on. But it helps to know them: you will meet them in interviews and at work.”
>
> Microsoft Foundry (formerly Azure AI Foundry) is the developer platform: thousands of models from many vendors, building your own agents and apps. This is where what you did in L03 lives at company scale.
>
> Security Copilot is the security team's assistant. In the frame the phishing triage agent handled 12 of 12 suspicious emails itself. Since September 2026 it is included in Microsoft 365 E5 and E7.
>
> Workflows: in Copilot Studio and Power Platform people build chains: an email arrives, it is classified, an agent evaluates it, a person approves. Name the others in one line: Dynamics for sales and service, Power BI and Fabric for reports, Dragon Copilot for doctors' notes, Agent 365 for inventory and protection of all agents in a company.

---

### Slide 22 (77:00–82:00) • Where does this question go?

**On screen:** The A–D zone key, four question cards for the Teams poll and four safety rules.

#### Speaker (5 min)
> Run a Teams poll per question or ask for answers in chat: “1-B, 2-A…”. 3 minutes for the game, 3 for the rules.
>
> Answers. 1: B, for work: Recap in Teams (licence) or paste the transcript into Copilot Chat. 2: A, for you: Copilot Vision or a screenshot into chat. 3: C, for developers: GitHub Copilot in the pull request or editor. 4: A, for you: an image in the Copilot app. Arguable answers are good: discuss where the information lives.
>
> Rules. Copilot sees only what you can access yourself: if a folder is not shared with you, Copilot cannot see it either. Work and school accounts are covered by an enterprise agreement: the green shield in the app. No passwords, keys or customer data in chat in any account. And every answer is a draft: check numbers and names, as on slide 13.

---

### Slide 23 (82:00–87:00) • Homework: the courier team's week with Copilot

**On screen:** The four homework steps, our capture of the IT Park school account in Copilot Chat and the 6-check rubric. Free Copilot only, synthetic data only.

#### Speaker (5 min)
> “The whole assignment works in free Copilot, personal or school. Nothing to buy.”
>
> Step 1 repeats demo A: the brief and what Copilot added, plus one mistake or invention you found. Step 2 repeats slide 13 with the rule in the prompt: “Prime is free from $75 only in the city; free from $100 for everyone”. Compare with your hand count. Step 3: text for three slides or a launch picture. Step 4 matters most: your map of five tasks and the Copilot for each.
>
> The rubric is six checks on the right. An important one: screenshots must show no names, e-mails or secrets. Correct answer for step 2 with the rule: 4 Prime orders from $75 in the city (1001, 1004, 1006, 1009); outside the zone only 1011 is free.

---

### Slide 24 (87:00–90:00) • The Copilot family in one line: for you · for work · for code · for the company

**On screen:** Four zone pictures in a row (for you, for work, for code, for the company), five rules, the chat question and the L08 teaser.

#### Speaker (3 min)
> Five rules out loud. Then the chat question: “which Copilot will you try this week, and for what?” Read 3–4 answers.
>
> Next lesson L08: data analysis with AI. Chatting with a file, code that does the maths, and checking the conclusion on a practice sales table; Copilot in Excel is one of the options.

---
