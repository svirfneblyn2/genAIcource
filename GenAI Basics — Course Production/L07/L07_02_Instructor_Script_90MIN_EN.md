# Instructor Script • Lesson 07: GitHub, Microsoft 365 and Windows Copilot. One Feature, Three Copilots (90 Minutes)

**Course:** GenAI Basics • Lesson 07 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language, no formulas; code only as one short example.
**Format:** 21 slides (`presentation_L07_Copilot_Ecosystem_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the demo kit `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`), the real diff and test output in `deck_v2/artifacts.json` (made by `deck_v2/make_artifacts.py`), runbook `L07_04_Live_Demo_Runbook_READY_EN.md`, homework `L07_05_Homework_EN.md`.
**Facts:** as of October 2026, sources in `L07_08_Source_Notes_Research_2026-10.md`. Prices and product names appear on slide 8 only. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before you start (Teams):** the lesson has three live demos (slides 6, 10–11, 17). Share your **whole screen**, not one window: you need a browser, VS Code, a terminal and Notepad. Run through `demo_courier_copilot/surface_preflight.md` beforehand (10 minutes). If a Copilot button is missing or the interface changed, the rule is: “the button moved, the rule did not”, at most 90 seconds of searching, then the slide with the ready result.

**Lesson objective:** students know that Copilot comes in three kinds by the place where the information lives (repository, work documents, your PC), understand that inside is the same model as in L03 and the result depends on what it sees; can take a small feature through a meeting, a brief, an issue, code, a pull request and a checklist; accept the result with 6 checks (the diff and the tests, not the word “done”); know what is free, and keep secrets and customer data out of every request.

---

## Timing (21 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | One Copilot? No: a family of three | 00:00–02:00 | 2 |
| **02** | One feature goes through six steps in a week | 02:00–06:00 | 4 |
| **03** | Three Copilots, three places where your information lives | 06:00–10:00 | 4 |
| **04** | Same model as in L03: what matters is what it sees | 10:00–14:00 | 4 |
| **05** | Teams: a meeting becomes decisions and action items | 14:00–19:00 | 5 |
| **06** | Word: from notes to a one-page brief | 19:00–24:00 | 5 |
| **07** | Outlook and Excel: the same button, a different context | 24:00–27:00 | 3 |
| **08** | What is free and what is paid | 27:00–31:00 | 4 |
| **09** | GitHub issue: the brief becomes a task for the developer | 31:00–34:00 | 3 |
| **10** | In the editor Copilot helps in three ways | 34:00–40:00 | 6 |
| **11** | The result: a 2-line diff and 7 green tests | 40:00–46:00 | 6 |
| **12** | Copilot review: a second pair of eyes, not the judge | 46:00–51:00 | 5 |
| **13** | copilot-instructions.md: a README for the robot | 51:00–54:00 | 3 |
| **14** | Four doors to one GitHub Copilot; today we used two | 54:00–57:00 | 3 |
| **15** | 5 minutes: coffee and a rest from the screen | 57:00–62:00 | 5 |
| **16** | Windows: Copilot sees only the window you shared | 62:00–68:00 | 6 |
| **17** | Release day: Copilot reads the open checklist | 68:00–71:00 | 3 |
| **18** | Six checks are the same for any Copilot | 71:00–76:00 | 5 |
| **19** | Copilot sees only what you can open | 76:00–80:00 | 4 |
| **20** | Homework: take your feature through three Copilots | 80:00–87:00 | 7 |
| **21** | Summary: three places, one habit: check the result | 87:00–90:00 | 3 |

Part 1 (slides 01–14, 00:00–57:00): three places, how Copilot works, Teams, Word, Outlook and Excel, prices, issue, editor, result, pull request, instructions, doors of GitHub Copilot. Break (slide 15, 57:00–62:00). Part 2 (slides 16–21, 62:00–90:00): Windows, release checklist, six checks, limits, homework, summary.

---

### Slide 01 (00:00–02:00) • One Copilot? No: a family of three

**On screen:** Background: a frame from L05 shot 2 (the courier in the rain). Title, subtitle, “3 Copilots • 1 team • 1 feature • 1 week”, key hints.

#### Speaker (2 min)
> Welcome. “Today nobody calls an API. We watch a team ship a feature, with Copilot at every step.”
>
> One feature: Prime subscribers get free delivery from $75 inside the city. The team: Anna (product), Pavel (junior developer), Ola (support). Everything is made up, there are no real customers.
>
> Plan: 4 slides on what the Copilot family is, then step by step Teams, Word, GitHub, the editor, review, then a break and Windows. Homework at the end. Before class, go through demo_courier_copilot/surface_preflight.md.

---

### Slide 02 (02:00–06:00) • One feature goes through six steps in a week

**On screen:** A Monday–Friday strip with six stations: Teams, Word, GitHub issue, VS Code, pull request, Windows. Each station shows a line from the real result.

#### Speaker (4 min)
> “Here is the whole lesson on one slide. Next we zoom into each station.”
>
> Monday: a Teams meeting where the rule is decided. Then a brief in Word. On Tuesday Anna turns the brief into a GitHub task. An issue is a task on GitHub, with a number. A pull request is the page where a change is shown and accepted. On Wednesday Pavel makes the change in VS Code with Copilot. On Thursday the pull request and review. On Friday the release, with the checklist on a Windows PC.
>
> Look at the quotes under the icons: they are real fragments of the files we open in class. And the common point: at every step Copilot gives a text, and the responsibility for checking stays with the person.

---

### Slide 03 (06:00–10:00) • Three Copilots, three places where your information lives

**On screen:** Three circles: repository (GitHub Copilot), work documents (Copilot in Word and Teams), your PC (Copilot in Windows). Each has two artifacts of the feature and a “Sees” line.

#### Speaker (4 min)
> “The only question you need: where does the information live?”
>
> If it is code and tasks, open GitHub Copilot. If it is mail, documents and meetings, use Copilot in Word, Teams, Outlook. If it is what is on your screen or in a folder on your PC, use Copilot in Windows.
>
> This week's files fall into three circles: the issue and pull request into the repository, the meeting and brief into work documents, the checklist onto the PC. The circles do not overlap: each Copilot sees only its own place.

---

### Slide 04 (10:00–14:00) • Same model as in L03: what matters is what it sees

**On screen:** Diagram: question + what it sees (file, chat, repository, screen) → model → answer. In the corner, the L03 call with the file text added.

#### Speaker (4 min)
> “You already did this in Colab. Copilot is that call with your file attached.”
>
> On the left is what goes into the request: your question and the context. Context is everything the assistant sees when it answers: the open file, the chat, the repository, the window on screen. In the centre is the same kind of model we called from Python in L03. On the right is the answer.
>
> From this comes a simple rule for the whole lesson: if it did not work, show the assistant the right thing. Name the file, open the window, paste the text. The model is not lazy and does not hide anything; it just cannot see what it was not shown.

---

### Slide 05 (14:00–19:00) • Teams: a meeting becomes decisions and action items

**On screen:** Teams window mockup (schematic): meeting “Prime delivery rule”, Copilot Recap pane on the right: decisions, open questions, action items. Below: no access? paste meeting_notes.md into free Copilot Chat.

#### Speaker (5 min)
> “Anna took no notes. Copilot did.”
>
> The pane on the right is what Copilot builds from the transcript: three decisions, two open questions, three tasks with names. The same text is in our file meeting_notes.md. Show it to the students and compare with the slide. A flag (feature flag) is a switch in the code: the rule can be turned on and off without changing the program. Staging is a test server.
>
> What to know: the recap works only if the meeting is recorded and transcribed and you have licensed Copilot. Without it, use free Copilot Chat and paste the notes yourself. It is the same trick: show the assistant the right thing. Check before class: the recap depends on the licence and recording settings.
>
> If the button is not where the schematic shows it: “the button moved, the rule did not.” No more than 90 seconds of searching, then paste the text into the chat.

---

### Slide 06 (19:00–24:00) • Word: from notes to a one-page brief

**On screen:** Word mockup (schematic): the brief page and the Copilot pane with the prompt. Sentences from the notes and Copilot’s own words (the effect line) are marked differently.

#### Speaker (5 min)
> “Her prompt ends with: list which lines are yours.”
>
> Live part, 3 minutes: Copilot in Word, or free Copilot Chat in Edge with meeting_notes.md pasted in. The prompt is on the right of the slide. Three moves: give the source, ask for a structure, demand a mark on what was invented.
>
> Check: $75 for Prime, $100 stays, nothing changes outside the zone, the flag owner is open. On the slide green marks what is in the notes, yellow what Copilot added. The last line about repeat orders is not in the notes: delete it or verify it.
>
> If there is no access: show fallback_outputs/brief_expected.md. It is a prepared text, not AI output.

---

### Slide 07 (24:00–27:00) • Outlook and Excel: the same button, a different context

**On screen:** Two mockups: an Outlook thread with a summary, and an Excel table of 8 orders with a Copilot answer (“3 of 5”). Data analysis comes in L08.

#### Speaker (3 min)
> “Same model, different window. The Excel half is a whole lesson, L08.”
>
> On the left is a mail thread in Outlook: Copilot writes a summary. The context here is the open mail. On the right is a table of eight orders in Excel: Copilot answers a question about the table. The context here is the open file.
>
> The number on the slide is counted from these eight rows: five Prime orders from $75, 3 of them in zone CITY. The data is made up. We cover spreadsheet analysis next lesson.

---

### Slide 08 (27:00–31:00) • What is free and what is paid

**On screen:** October 2026, US prices. Two rings: free (what you give it) and licensed (mail, files, meetings). A strip of GitHub Copilot and Microsoft plans. The only slide with prices.

#### Speaker (4 min)
> “If it cannot find your file, it is not broken. It just cannot see it.”
>
> This is the only slide with prices and plan names, which is why it carries a date: October 2026. Everything else in the lesson uses stable words. Before class, open the plan pages and check the numbers.
>
> The inner ring: what you paste or open. You can get this for free: Copilot Chat with a Microsoft 365 work account and GitHub Copilot Free. The outer ring: your mail, files, meetings and chats. It needs a licence, and Copilot sees only what you have access to. GitHub also has a separate free plan for verified students, Copilot Student.
>
> About names: Microsoft is renaming Microsoft 365 Copilot to Microsoft Copilot; you will see both names. It is not a new product. Prices on the right: GitHub by plan, Microsoft per licence billed yearly, Business $23.50, Enterprise $30.

---

### Slide 09 (31:00–34:00) • GitHub issue: the brief becomes a task for the developer

**On screen:** GitHub issue #12 page mockup (schematic): five bullets and acceptance, assignee Pavel, label feature; the “Assign to Copilot” button is grey (cloud agent, L16).

#### Speaker (3 min)
> “This issue is the prompt. Copilot reads it word for word.”
>
> An issue is a task on GitHub, with a number. Anna rewrote the brief as a task: numbers, what must not change, which tests are needed. A good issue contains exactly this: numbers, boundaries and a list of checks.
>
> On the right is the grey “Assign to Copilot” entry. That is the cloud agent: it takes the task itself and opens a pull request. It is on paid plans, not on Free. We do not use it today; details in L16.

---

### Slide 10 (34:00–40:00) • In the editor Copilot helps in three ways

**On screen:** VS Code mockup (schematic): delivery_fee.py with grey ghost text (completion), chat with Pavel’s two prompts, terminal. Three ways: completion, chat, agent.

#### Speaker (6 min)
> “Pavel types if order.zone and the grey text finishes the rule.”
>
> Three ways. First: completion. The grey text in the line is the editor’s proposal; Tab accepts it. Second: the chat on the right, where you ask about the open file. Third: an agent, which edits several files and runs commands itself while you check the result. Mode names in the app change; look at what the button does.
>
> Live part, 8 minutes together with the next slide: VS Code and GitHub Copilot Free. Prompt 1 in chat: “Read ISSUE.md and the instructions, propose a plan, do not edit.” Prompt 2: “Implement it, add boundary tests, run the tests.” If there is no agent, paste the code from the chat by hand.
>
> Depth: agents and editors come in L16. Today we need one thing: to see what exactly changed.

---

### Slide 11 (40:00–46:00) • The result: a 2-line diff and 7 green tests

**On screen:** A real run: git diff (2 lines of logic and 3 tests) and python -m unittest -v output (7 ok). Taken from deck_v2/artifacts.json.

#### Speaker (6 min)
> “Nothing on this slide was written by me. This is the actual run.”
>
> A diff is the exact lines that were added and removed. Green pluses: the Prime rule, two lines. Below are three new tests. A test is a small script that checks one rule: for example, that a 74.99 Prime order pays 7.50.
>
> On the right is the test run: seven tests, all green. Compare with the base: there were four. The three new ones check the 75 boundary, a value just below it, and a customer without Prime. This is how we see that nothing else broke.
>
> These are the same numbers you get in VS Code with expected_solution. If Copilot does it differently in class, compare its diff with this one.

---

### Slide 12 (46:00–51:00) • Copilot review: a second pair of eyes, not the judge

**On screen:** Pull request #13 mockup (schematic): Files changed with the real diff, a Copilot review comment, “Approved: Ola”, checks “tests 7/7”.

#### Speaker (5 min)
> “Copilot found one thing worth thinking about and one thing it already saw covered.”
>
> A pull request is the page where a change is shown, discussed and accepted: “please take my change.” On the left is the real diff from slide 11. Under the changed line is Copilot’s comment: the 74.99 test is already there, and money is better counted in Decimal.
>
> On the right are three statuses. Ola approved: a person decides. Checks are green: tests are the gate. Copilot’s comment is a suggestion, not an order. Copilot review works on github.com in a pull request, not in the editor. Without paid access, a human review comment is fine.

---

### Slide 13 (51:00–54:00) • copilot-instructions.md: a README for the robot

**On screen:** The .github/copilot-instructions.md file (5 rules); arrows to where each rule shows up in the result.

#### Speaker (3 min)
> “Rule 4, ‘add boundary tests’, is why the 74.99 test exists.”
>
> These are custom instructions: a file of rules the assistant reads before every request. It lives in the .github folder at the start of the project. Five lines on the left, and on the right where each one shows in our result.
>
> Tip: keep the file short. Nobody follows a long rulebook, neither people nor robots. Write rules you can check in the diff or in the tests.

---

### Slide 14 (54:00–57:00) • Four doors to one GitHub Copilot; today we used two

**On screen:** A map of four doors to GitHub Copilot: editor, github.com, terminal (CLI), cloud agent; tags for what is on Free.

#### Speaker (3 min)
> “Remember the map. In L16 we walk through every room.”
>
> The same assistant lives in four places. The editor: completion, chat, agent. github.com: issues and pull requests, and the review there. The terminal: Copilot CLI. The cloud: an agent that takes a task itself and opens a pull request. Today we worked in the editor and in a pull request.
>
> What is available on the free level depends on the plan and changes, so there are no numbers here. The editor and the terminal are on Free. The cloud agent is not on Free. Check the plans page before class.

---

### Slide 15 (57:00–62:00) • 5 minutes: coffee and a rest from the screen

**On screen:** 5-minute timer, Start and Reset buttons.

#### Speaker (5 min)
> Press “Start”. Rest only, no chat tasks.

---

### Slide 16 (62:00–68:00) • Windows: Copilot sees only the window you shared

**On screen:** Windows desktop mockup (schematic): a window with the checklist, the Copilot window with Vision, a keyboard with the Copilot key highlighted; five features. Below: work accounts open the web chat.

#### Speaker (6 min)
> “Pavel presses one key and asks about the window he is looking at.”
>
> Many new laptops have a Copilot key. If yours does not, press Win+C or open the app. The app does chat and voice, search over your files (docx, xlsx, pptx, txt, pdf), screenshots and Vision: the assistant looks at the window you chose yourself.
>
> The main point: it sees only the window you shared. If you did not share it, it does not see it. Microsoft work accounts open the web chat instead of the app, which is normal. Feature availability depends on the device, region and Windows version.
>
> One line on Copilot+ PCs, not for the slide: some features, for example Recall, need exactly such a computer. Recall has been rolled out gradually since April 2025 and is off by default. You may not have it, and our lesson does not need it.

---

### Slide 17 (68:00–71:00) • Release day: Copilot reads the open checklist

**On screen:** Notepad mockup with release_checklist.txt (6 items) and the Copilot answer: item 6. No button? paste the text into the chat.

#### Speaker (3 min)
> “Which item saves us if outside-zone fees break? Item 6, and it quotes it.”
>
> Live part, 3 minutes: open release_checklist.txt, press the Copilot key, share the window with Vision or paste the text. The question is on the slide. The answer should quote item 6.
>
> This is the same rule as slide 4: a local file became the context. The fallback is always one thing: paste the text. If nothing opens, show fallback_outputs/checklist_answer.md and move on: the button moved, the rule did not.

---

### Slide 18 (71:00–76:00) • Six checks are the same for any Copilot

**On screen:** A 6-check list with the result of our week ($75 · $100 · $18.00, +2 lines, 7 of 7, 1 comment, 3 screenshots). This is the homework rubric.

#### Speaker (5 min)
> “If any of these is missing, you did not use Copilot, you trusted it.”
>
> The six checks work for any Copilot: in Word, in the editor, on Windows. Let us go down the list. The brief marks its sources. The issue has numbers. The change is small. Tests are green and check the boundary. The review was read. The evidence is kept.
>
> The right column shows our week’s results: plus 2 lines of logic, 7 of 7 tests, the 75 and 74.99 boundary. These numbers come from the real run on slide 11. The same six checks are the homework rubric.

---

### Slide 19 (76:00–80:00) • Copilot sees only what you can open

**On screen:** A person with a key and three traps: wrong account, a secret in the chat, “Done!”. Below: training on your data (work accounts no; personal GitHub since 24 April 2026, switch it off in settings).

#### Speaker (4 min)
> “Copilot is not a colleague with admin rights. It is you, faster.”
>
> Copilot’s permissions equal yours: what you can open, it can see. Three traps follow. First: you signed in to the wrong account. Second: you pasted a password, a key or customer data into the chat. Third: you believed the word “done”.
>
> About data. Microsoft 365 work accounts and GitHub Business and Enterprise are not used to train models. On personal GitHub plans, since 24 April 2026 interactions may be used for training by default. You can turn it off in Copilot settings: “Allow GitHub to use my data for AI model training”. Check this switch before the homework.

---

### Slide 20 (80:00–87:00) • Homework: take your feature through three Copilots

**On screen:** The courier-copilot-week repository card (file tree), the feature, tools (free only), grading by the six checks of slide 18.

#### Speaker (7 min)
> “Same feature, your repo, your screenshots.”
>
> The task: a public repository courier-copilot-week. Inside: a brief, the code, tests, one merged pull request, a checklist and a README with three screenshots: the brief, Copilot in the editor, the pull request. The rule: your number and your boundary, any rule you like.
>
> Tools: free GitHub Copilot Free in VS Code, plus Copilot Chat on the web, in Edge or in the Windows app. Microsoft 365 is optional. Copilot review on a pull request may be paid; then a human comment that you answered is enough.
>
> Criteria: the six checks of slide 18. Before you start, switch off training on your data in your personal GitHub settings. No real customer data.

---

### Slide 21 (87:00–90:00) • Summary: three places, one habit: check the result

**On screen:** The compressed week strip, five rules and the L08 tile (the table from slide 7).

#### Speaker (3 min)
> “Next week Copilot opens a spreadsheet and we do real analysis.”
>
> At the top is our whole week: Teams, Word, issue, editor, pull request, Windows. Five rules. Ask where the information lives. Copilot sees only what is open to you. Look at the diff and the tests. Keep evidence. Do not paste secrets.
>
> Next lesson, L08: data analysis with AI. We take that table from slide 7 and go from a question to a checked conclusion. Questions.

---
