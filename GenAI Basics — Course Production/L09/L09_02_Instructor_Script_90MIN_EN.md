# L09 — Claude Ecosystem and Artifacts: 90-minute script

Generated from the speaker notes (`deck/build.py`, key N in the deck). Edit the notes in the generator, then run `python make_docs.py`.

Before class: in claude.ai → Settings → Capabilities make sure Artifacts (and AI-powered artifacts for slide 14) are on; open a new chat, `demo_assets/tickets_en.csv` and `demo_assets/prompts_en.md`; in Teams share the browser window, with no personal history on screen. If the live demo is slow, the slides show the real results.

## Slide 01 · 0–2 min · Claude Ecosystem and Artifacts

⏱ 2 min. Welcome. In L07 we looked at the Microsoft Copilot ecosystem. Today it is the second big assistant, Claude by Anthropic, and its signature feature: artifacts.

Plan: where Claude lives → what an artifact is → how to order and check one (live demo) → break → the artifact as an app, projects, connectors, skills → safety → homework.

## Slide 02 · 2–6 min · Six working things — one sentence each

⏱ 4 min. Show the gallery and ask: “How long would any of these take you by hand?” All six were made while preparing the lesson, each from one or two sentences (prompts in demo_assets/prompts_en.md).

Today: where Claude lives, how the window works, what artifacts exist, a live demo “table → dashboard → slides”, projects and connectors, and what is safe to share.

## Slide 03 · 6–9 min · Six words you will need today

⏱ 3 min. Go through each word with one sentence and one example. Later these words appear without explanation.

The artifact is the main one. A project is like a desktop folder, except Claude reads everything in it. Memory is short notes about you that you can view and erase. A connector is a “key” to one service and uses your permissions. A skill is instructions plus files that Claude opens when the task fits. An agent is Claude that doesn’t just answer but carries out steps itself: opens files and sites, assembles the result.

## Slide 04 · 9–13 min · Where Claude lives

⏱ 4 min. Key idea: Claude is not a single chat window but one model reached through different “doors”. The doors differ in how much Claude does by itself.

Talk: the normal chat on claude.ai, in the Windows/Mac app and on the phone; projects are a folder of files and rules for one topic.

Make things: artifacts — today’s main topic; plus Claude right inside Excel and PowerPoint.

Act for you: Claude carries out long multi-step tasks itself and works in the browser — more on slide 19. For developers: Claude Code and the API.

At the bottom is the shared layer: the models are the same, connectors and skills plug in everywhere. Analogy with L07: Microsoft also has one Copilot across different apps.

## Slide 05 · 13–19 min · The main window: what is where

⏱ 6 min. A tour of the claude.ai window (the same in the Windows/Mac app). Left sidebar: New — a new chat; Projects; Artifacts — everything you made; below — pinned projects and chat history (blurred on the screenshot).

Top left — the chat / Code toggle: Code is the programmers’ mode (slide 19). In the centre — the input box; “+” opens files, skills, connectors, Research, memory. Under the box — the model picker (next slide).

Live: open claude.ai and point at these 7 places on your own screen. In Teams share the browser window, not the whole screen, and open a new chat so your history isn’t visible.

## Slide 06 · 19–22 min · One menu — four models

⏱ 3 min. The menu opens by clicking the model name under the input box. The captions are the official ones (in quotes on the slide). Names change several times a year; the principle doesn’t.

For learning, the default model is enough. Fable is for very hard tasks. The free plan offers fewer models.

## Slide 07 · 22–25 min · The free plan is enough for this lesson

⏱ 3 min. Prices from claude.com/pricing as of 13 Oct 2026. Key point for students: artifacts, the Docs/Slides/Design templates, search and memory are free. Claude Code, Research, Chrome and the Office add-ins start at Pro.

The limit isn’t counted in messages but in “amount of work”: long files and powerful models use it faster. Paid plans also have a weekly cap.

## Slide 08 · 25–28 min · An artifact is something you would put in front of another person

⏱ 3 min. Anthropic’s help-centre definition: an artifact is anything Claude makes for you that you’d put in front of someone — a design, a deck, a document, a dashboard or a small tool. It opens beside the conversation.

The four signs are when Claude decides by itself. If you want one for sure, say so: “make a document / deck / dashboard”. “Artifacts” must be on in Settings → Capabilities.

## Slide 09 · 28–32 min · All your artifacts in one place

⏱ 4 min. The Artifacts tab in the sidebar. At the top — “Make something new”: start from Docs, Slides, Design or Dashboard. Below — everything you made, from any chat (the screenshot shows artifacts made for this lesson).

Docs, Slides and Design are on all plans, Dashboards is beta from Pro. A template isn’t required: you can just write “make a deck…” in a chat — that’s how we did it.

## Slide 10 · 32–37 min · A deck from one sentence

⏱ 5 min. Live: new chat → “Make a 5-slide deck for new couriers of the «Bystro» delivery service: how to accept an order, how to talk to the customer, what to do if the address isn’t found, road safety, summary.” Takes about 2 minutes.

While Claude works, explain: the result opens on the right, slide thumbnails at the bottom, tools at the top. Fix any text by clicking on the slide, or ask Claude: “make slide 3 shorter”.

Share → Export: PDF, PowerPoint (.pptx), PNG, Google Slides. Tip from the menu: when sending to a colleague, a link is better — they always get the latest version.

## Slide 11 · 37–41 min · A document you write together with Claude

⏱ 4 min. Prompt: “Make a document: a guide for a new courier-service support agent — 5 rules for answering a customer and reply templates for 3 common complaints.” You get a living document (Claude Docs).

Show it: select a paragraph — a formatting toolbar and a comment button appear. Edit the document by hand like any other, or ask Claude to change a specific place. Invite colleagues via Share — they can comment and edit.

Export: Word, PDF, Markdown, Google Docs.

## Slide 12 · 41–45 min · A website mockup — without a designer

⏱ 4 min. Design — mockups, prototypes, landing pages, one-pagers. The result opens on a canvas: move elements, change colours (Tweaks), ask for edits in words.

Point at the “What I assumed” paragraph: Claude listed what it made up (plan names) and left prices and phones as placeholders. A good habit — always ask “what did you make up?” and check.

## Slide 13 · 45–49 min · Draw a process and show the data

⏱ 4 min. Diagram: Claude draws the process steps with decision points (“urgent?”, “is the complaint valid?”). Good for guides and explanations. Dashboard: upload a table — get a screen with numbers and a “what first” list. We’ll walk through it in the live demo after the break.

An interesting moment during preparation: for the diagram Claude first offered to use the connected Figma — and asked for permission (slide 18). We declined, and it drew the diagram right in the artifact — the slide shows the no-Figma result.

## Slide 14 · 49–53 min · An artifact with Claude working inside

⏱ 4 min. A mini app is an artifact with buttons and fields that calls Claude itself: coaches, flashcard generators, quizzes. No API key needed.

Who pays: requests count against the person using the app, not the author. On first use the artifact asks for permission. If the button doesn’t work, check the AI-powered artifacts toggle in settings (it was off in the course author’s account).

Before class, check on a free account that such an artifact can be created and run — homework track B depends on it.

## Slide 15 · 53–58 min · 5 minutes

⏱ 5 min. Break. Start the timer.

## Slide 16 · 58–65 min · Table → dashboard → stand-up slides

⏱ 7 min. Live, file demo_assets/tickets_en.csv (made-up courier-support tickets; it deliberately contains customer emails and empty owners). 1) New chat → “+” → Add files → tickets_en.csv. Text: “Make a dashboard for the support lead: what should we tackle first at the morning stand-up? Don’t show customer emails.”

2) After 2–3 minutes — the dashboard. Check the three things on the slide aloud. During preparation Claude put T-110 first by itself — a P1 with no owner, a customer seeing other people’s orders. 3) In the same chat: “Make 3 slides for stand-up from this” — a deck with the same numbers.

If the network or Claude fails, show this slide: these are real results. No real customer data — only this file.

## Slide 17 · 65–69 min · A project is a folder Claude remembers in every chat

⏱ 4 min. Projects → New project → name and goal. On the right: Instructions — rules for every chat in the project; Context — files Claude reads every time; Memory — what Claude remembered in this project.

The example is the lesson’s demo project: the instruction “answer briefly, never show emails or phone numbers” and the tickets file. Any new chat in the project already knows the rules and the data. On Team you can share a project with colleagues.

## Slide 18 · 69–73 min · Claude knows only what you gave it

⏱ 4 min. Three ways to give Claude information: attach a file (“+” → Add files: PDF, Excel, CSV, photos), connect a service (connectors: Gmail, Google Drive, Calendar, GitHub, Figma and hundreds more) and turn on web search.

A connector uses your permissions: what you can’t see, Claude can’t either. Before acting in another service Claude asks — on the screenshot it wanted to draw the diagram in Figma. If in doubt — Decline or Allow once.

## Slide 19 · 73–77 min · When Claude doesn’t just answer but acts

⏱ 4 min. A short preview. Since 16 September 2026 the former Cowork is part of the normal chat (“One Claude”): Claude decides when long multi-step work is needed — e.g. opening sites and building a price comparison. Pro and Max first.

Claude Code — the “Code” toggle at the top of the sidebar: Claude reads a project, writes code, runs tests. This deck was built with it. Skills are folders with instructions and files (e.g. the built-in Word/Excel/PowerPoint/PDF ones), which is why Claude hands you real files.

## Slide 20 · 77–83 min · A public link is a publication

⏱ 6 min. Share: by default “Only people invited” — you and the people you invite. “Anyone with the link” — the link can be forwarded, treat it like publishing on the internet. On Team/Enterprise public links are enabled by the admin. On your plan the labels may differ slightly — the idea is the same: “only you” → “anyone with the link”.

Privacy: the “Help improve our AI models” toggle. On — chats and coding sessions may be used to train models and are kept up to 5 years; off — 30 days. Team and Enterprise are not used for training by default. Show where it is — let everyone decide.

The most common leak is a beautiful artifact everyone wants to share before anyone checked what data is inside. That’s why in the demo we asked “don’t show emails” right away.

## Slide 21 · 83–90 min · Make two things of different types

⏱ 7 min. Homework: two things of different types. First — a deck or a document. Second — a dashboard, diagram or mini app from your own data, anonymised (replace names, emails, phones). The free plan is enough.

Hand in the prompts, links (only if there’s no personal data inside) or screenshots, and one precise fix after checking: what you didn’t like → what you asked to change. Template in L09_05_Homework.

Summary — four rules. Questions. Bridge: in L10 we move from cloud assistants to open models — LM Studio, local inference, RunPod.

**Total: 90 min.**
