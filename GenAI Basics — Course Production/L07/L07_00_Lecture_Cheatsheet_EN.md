# 1-Page Speaker Cheatsheet • Lesson 07 (v2: 21 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: GitHub, Microsoft 365 and Windows Copilot. One feature, three Copilots • facts as of 2026-10-13*  
*Presentation: `presentation_L07_Copilot_Ecosystem_EN_v2.html` (PDF: same basename) • source: `deck_v2/build.py` • full script: `L07_02_Instructor_Script_90MIN_EN.md`*  
*Demo: `L07_04_Live_Demo_Runbook_READY_EN.md` • Homework: `L07_05_Homework_EN.md` • Homework repo: `courier-copilot-week` • Reviewer: `ihar_rubanovich@epam.com`*

---

### Before you start (Teams)
* Share your **whole screen**: you need a browser, VS Code, a terminal and Notepad. A day before, go through `demo_courier_copilot/surface_preflight.md`.
* Three live demos: **sl. 6** brief (3 min) • **sl. 10–11** code (8 min) • **sl. 17** Windows (3 min). Timer: **sl. 15**.
* Rule: **“the button moved, the rule did not”**. No button after 90 seconds → the ready result on the slide or in `fallback_outputs/`, move on.
* Part 1 (00:00–57:00) → break (57:00–62:00) → part 2 (62:00–90:00). Prices and product names on **sl. 8** only.

---

### Three places, three Copilots (sl. 3)
| Where the information lives | Which Copilot | What it sees | Our example |
|---|---|---|---|
| **Repository** | GitHub Copilot | code, history, issues, pull requests | issue #12, pull request #13 |
| **Work documents** | Copilot in Word, Teams (Outlook, Excel) | the mail, files and meetings open to you | Teams meeting, brief in Word |
| **Your PC** | Copilot in Windows | the window you shared, and your files | `release_checklist.txt` |

One question for every case: **where does the information live?** Inside is the same model as in L03; what matters is what it was shown.

### 10 terms in plain words
1. **Context:** everything the assistant can see when it answers: the open file, the chat, the repository, the shared window.
2. **Repository (repo):** the project folder with its history, kept on GitHub.
3. **Issue:** a task written down on GitHub, with a number.
4. **Pull request (PR):** “please take my change”. The page where the change is shown, discussed and approved.
5. **Diff:** the exact lines added and removed.
6. **Unit test:** a small script that checks one rule (74.99 pays 7.50). Green = passed.
7. **Completion:** the grey text the editor proposes as you type. Tab accepts it.
8. **Agent (mode):** the assistant edits several files and runs commands itself; you check the result. Depth in L16.
9. **Custom instructions:** a short file of team rules the assistant reads every time (`.github/copilot-instructions.md`).
10. **Copilot key / Vision:** the Windows key that opens Copilot (or Win+C). Vision looks at the window you share.

Do not use: grounding, tenant, Graph, Entra, EDP, control plane, MCP (say “connectors, L12”), governance, policy. Copilot+ PC and Recall: one line at most.

### 6 checks (sl. 18 = homework rubric)
1. **The brief** marks what is from the notes and what is invented (our effect line) • 2. **The issue** has numbers and what must not change ($75 · $100 · $18.00) • 3. **The change is small** (+2 lines of logic) • 4. **Tests are green** and check the boundary (7 of 7; 75 and 74.99) • 5. **The review was read and answered** (1 Copilot comment) • 6. **Evidence is kept** (3 screenshots + `checklist.md`).

### What is free (sl. 8; October 2026, US prices)
* **GitHub Copilot Free:** $0, 2,000 completions a month, limited chat and agent usage, automatic model choice only. No cloud agent. CLI included.
* **Copilot Student:** free for verified students. Teachers and maintainers of popular open-source projects “may be eligible” for free Pro.
* **Copilot Chat** (web, Edge, Windows app) and **Microsoft Copilot Chat** with a Microsoft 365 work account: free, sees the web and what you paste or open.
* Paid: GitHub Pro $10 / Pro+ $39 / Business $19 / Enterprise $39; Microsoft Copilot licence $23.50 (Business) / $30 (Enterprise), paid yearly.
* No licence or no button: **paste the text into free chat**. It is the same trick: show it the right thing.

### 5 rules of the lesson (sl. 21)
1. First ask: **where does the information live?** • 2. Copilot sees only what is open to **you** • 3. Look at the **diff and the tests**, not at “done” • 4. Keep **evidence**: screenshots, a checklist • 5. **No secrets or customer data** in a request.

---

### Key demo numbers
2 lines of logic, +3 tests, 7 tests green (the base had 4) • boundaries 75 / 74.99 / non-Prime • fees 0.00 / 7.50 / 18.00 • checklist item 6: “Roll back the flag if outside-zone fees change unexpectedly”.
**Training on your data:** work accounts (Microsoft 365, GitHub Business and Enterprise) are not used. Personal GitHub (Free, Pro, Pro+, Max): since 2026-04-24 on by default; switch off “Allow GitHub to use my data for AI model training”.

### Recheck within 24 hours of class
GitHub and Microsoft plan names and prices (slide 8), “AI credits”, what Free includes • the rename “Microsoft 365 Copilot” → “Microsoft Copilot” • the wording and path of the “training on your data” setting • VS Code mode names (Ask / Edit / Agent / Plan) • whether cloud agent and code review exist on your plan • the Copilot key, Vision and “Hey Copilot” on the demo PC • Recall and Click to Do (regions) • demo GitHub account sign-in and VS Code sign-in. Full list: end of `L07_08_Source_Notes_Research_2026-10.md`.
