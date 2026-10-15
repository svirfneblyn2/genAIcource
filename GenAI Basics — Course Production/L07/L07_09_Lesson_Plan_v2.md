# L07 — GitHub, Microsoft 365 and Windows Copilot ecosystem: Lesson Plan v2 (overview deck, 21 slides, 90 min)

Written 2026-10-13 against the old Sep-2026 package (`l07_old/`), the L05/L06 v2 standard and `course-deck-design/SKILL.md`.
Facts: `L07_08_Source_Notes_Research_2026-10.md` (checked 2026-10-13). Rule for the deck: volatile names and prices (Microsoft rename "Microsoft 365 Copilot" → "Microsoft Copilot", GitHub "AI credits", "Max" plan, all $ figures) appear on **slide 08 only**, never in titles; other slides use stable words ("Copilot in Word", "GitHub Copilot Free"). Items marked **(verify)** are in the notes' "Could not verify" list.
Depth boundaries: coding agents / IDEs → L16; MCP → L12; data analysis → L08 (slide 07 only previews it); Claude → L09.

## A. Critique of the old lesson

1. It is an enterprise-governance lecture, not an overview: 8 tables, 0 images, 0 diagrams, no screens. A beginner never sees what any Copilot *looks like* or what it *returns*.
2. Jargon to drop entirely: "authoritative context", "control plane / data plane", "trust boundary", "identity boundary", "grounding", "Microsoft Graph / Work IQ", "Entra", "tenant", "enterprise data protection (EDP)", "content exclusion", "blast radius", "audit debt", "metered capacity", "policy dependency", "Copilot Operating Map".
3. Jargon to keep but explain in one plain line (see G): context, repository, issue, pull request, diff, unit test, completion, agent, custom instructions.
4. Windows section is 60 % caveats (Copilot+ PC, Recall, Click to Do, EEA region differences). For an overview: one slide on the Copilot key / app / Vision / file search (notes §9, §11), one line "some features need a Copilot+ PC; Recall is off by default and removed on work devices" (notes §10); no regional policy discussion.
5. "Project Northstar" is abstract: no product, no users, no screens, no numbers a student can picture. It also breaks course continuity: the rest of the course lives in the Glovo-style courier case (Ihar, L04–L06).
6. The learning outcome "choose the surface by where authoritative context lives" is correct but phrased for architects. Beginner version: "Copilot can only use what it can see; show it the right thing."
7. Missing: the link to L03 (all Copilots are the same kind of model the students already called from Python; the difference is what is fed in). This is the one idea that makes the family name make sense.
8. Missing: what is free. Students cannot do the old homework without a licensed M365 tenant and an org GitHub account. GitHub Copilot Free, Copilot Student, the consumer Copilot app on Windows/web and Copilot Chat included with M365 (notes §6, §9) are enough for an overview homework.
9. Missing: the real result. The old deck never shows the actual 2-line diff or the test output, although the demo kit contains both. Those are the strongest visuals we can produce in the container.
10. Missing: GitHub Copilot code review on a PR as a *picture* (the one surface most juniors will meet first), and the `copilot-instructions.md` file as "a README for the robot".
11. Workshop/homework ("Copilot Operating Map", 20-point rubric, 250–400-word decision memo) is a compliance exercise; replace with a hands-on task that produces artifacts (brief, diff, PR, checklist) and a ≤6-check rubric like L05/L06.
12. Boring structure: concept → table → concept → table. Replace with a story told in the order the work happens (meeting → brief → issue → code → PR → release).
13. Keep: the three-places model (repo / work documents / your PC) as the only mental model; the sample repo (`shipping.py`, ISSUE.md, instructions, tests, expected solution); `meeting_notes.md`; `release_checklist.txt`; the rule "look at the diff and tests, not at the word done"; the line "the button moved, the rule did not"; synthetic data only; the 90-second troubleshooting limit.
14. Keep (one slide, plain words): "Copilot sees what you are allowed to open, nothing more; work accounts (M365 work sign-in, GitHub Business/Enterprise) are not used for training; on personal GitHub plans training is on by default since 2026-04-24, switch it off in Copilot settings" (notes §5, §8).
15. The 2026-09 facts (surfaces, free tiers, Windows features) are volatile; every slide with a product fact gets a "(verify)" tag until the research notes land.

## B. Audience promise: three things a student can do tomorrow

1. Turn a messy meeting into a one-page brief with Copilot in Teams/Word (or free Copilot Chat with the notes pasted) and check it against the source.
2. Get GitHub Copilot (Free tier) to implement a small, well-described change in VS Code, then judge it by the diff and the tests, not by the chat.
3. Explain in one sentence which Copilot to open for a task ("where does the information live: repo, documents, or my screen?") and what each one cannot see.

## C. Through-line case: "Free delivery for Prime customers from $75"

The courier app from L04–L06 (Ihar's company) has a small product team: **Anna** (product manager), **Pavel** (junior developer, 3 months in), **Ola** (support lead). On Monday the team meets in Teams and decides one feature: **Prime subscribers get free delivery from a $75 order inside the city zone; the existing free delivery from $100 for everyone stays; deliveries outside the zone do not change** (= the old VIP rule re-skinned onto the courier case: `country` → `zone` "CITY"/"OUTSIDE", `is_vip` → `is_prime`, fees 7.50 / 18.00 kept). The whole week fits on one strip:

Mon Teams meeting (recap + 3 action items) → Mon Word brief (one page, Anna) → Tue GitHub issue #12 (Anna → Pavel) → Wed VS Code with Copilot: **2-line change in `delivery_fee.py` + 3 new tests, 7 tests green** → Thu pull request #13 with a Copilot review comment ("74.99 boundary test present; consider `Decimal` for money") and Ola's approval → Fri release checklist opened on Windows, Copilot points at item 6 ("roll back if outside-zone fees change").

Numbers we can show for real: 7 tests, 2 changed lines, 3 new tests, boundary values 75 / 74.99 / 100, fees 0.00 / 7.50 / 18.00. Everything is synthetic; no real customer data.

## D. Slide map (21 slides, 90 minutes incl. break)

| # | min | Title RU | Title EN | Main visual (buildable) | Key points | Speaker hook |
|---|---|---|---|---|---|---|
| 01 | 2 | Один Copilot? Нет — семья из трёх | One Copilot? No: a family of three | reused-image: `L05/assets/v2/img/cover_shot2.jpg` (courier) + lesson scope line | 3 Copilots, 1 team, 1 feature, 1 week | "Today nobody calls an API. We watch a team ship a feature with Copilot at every step." |
| 02 | 4 | Одна фича, пять инструментов, неделя | One feature, five tools, one week | svg: horizontal journey strip Mon–Fri with 6 stations (Teams, Word, GitHub issue, VS Code, PR, Windows), each with the real artifact excerpt (recap line, brief line, issue title, 2-line diff, review comment, checklist item 6) | The story we follow; same output at every step: a text you must check | "Here is the whole lesson on one slide; we zoom into each station." |
| 03 | 4 | Три Copilot — три места, где лежит ваша информация | Three Copilots, three places where your information lives | svg: three big circles (repo / work documents / your PC) with 2 icons each; the feature's artifacts sorted into them | GitHub Copilot = code; M365 Copilot = mail, docs, meetings; Windows Copilot = screen and files | "The only question you need: where does the information live?" |
| 04 | 4 | Внутри — та же модель, что в L03; разница в том, что она видит | Inside is the same model as in L03; the difference is what it sees | svg: model box in the middle, left = your question + "what Copilot can see" (file / chat / repo / screen chips), right = answer; small L03 `client.chat(...)` snippet in a corner | Same kind of model you called in L03; context = what it is shown; show more, get better | "You already did this in Colab. Copilot is that call with your file attached." |
| 05 | 5 | Teams: встреча превращается в решения и задачи | Teams: a meeting becomes decisions and action items | html-mockup "schematic": Teams meeting window, right pane "Recap" with the real `meeting_notes.md` content (decisions / open questions / actions) | Recap, action items, "what did I miss"; needs a transcribed meeting and the licensed Copilot (verify) | "Anna did not take notes. Copilot did." |
| 06 | 5 | Word: из заметок — одностраничный бриф | Word: from notes to a one-page brief | html-mockup: Word page with the brief (from `fallback_outputs/m365_expected_brief.md`, re-skinned) + Copilot side pane showing the prompt; 2 callouts: "from notes" vs "Copilot's wording" | Give the source, ask for structure, demand "mark what you invented" | "Her prompt ends with: list which lines are yours." |
| 07 | 3 | Outlook и Excel: та же кнопка, другой контекст | Outlook and Excel: the same button, different context | html-mockup split: Outlook thread "Summarize" (Ola's support thread) and Excel table of 8 orders with a Copilot column "zone with most Prime orders ≥ $75" | One button, the open item is the context; Excel analysis is L08 | "Same model, different window. L08 is a whole lesson on the Excel half." |
| 08 | 4 | Что бесплатно, а что по подписке (октябрь 2026) | What is free and what is paid (October 2026) | svg: two concentric rings around a person: inner "what you paste or open" (free: Copilot Chat included with M365, GitHub Copilot Free), outer "your mail, files, meetings, chats" (licensed Microsoft Copilot) + a 6-row price strip under it: GitHub Free $0 / Pro $10 / Business $19; Microsoft Copilot Chat included / Business $23.50 / Enterprise $30 (notes §1, §6; the only volatile slide, dated) | Free: web + what you give it; licensed: your work data within your permissions; names are mid-rename (notes §6) | "If it cannot find your file, it is not broken; it just cannot see it." |
| 09 | 3 | GitHub issue: бриф становится задачей для разработчика | GitHub issue: the brief becomes a task for the developer | html-mockup: GitHub issue #12 page with the re-skinned ISSUE.md (5 bullets + acceptance), labels, assignee Pavel; "Assign to Copilot" entry greyed (cloud agent: paid and Student plans, notes §2), badge "L16" | A good issue = numbers + what must not change + tests wanted | "This issue is the prompt. Copilot reads it word for word." |
| 10 | 6 | В редакторе Copilot помогает тремя способами: подсказка, чат, агент | In the editor Copilot helps three ways: completion, chat, agent | html-mockup "schematic": VS Code window, `delivery_fee.py` with ghost-text completion of the Prime line, right chat panel with Pavel's 2 prompts (plan, implement), bottom terminal | Completion = autocomplete; chat = ask about open file; agent = edits files and runs tests; depth in L16 | "Pavel types `if order.zone` and the grey text finishes the rule." |
| 11 | 6 | Результат: 2 строки diff и 7 зелёных тестов | The result: a 2-line diff and 7 green tests | real-artifact: `git diff` of `delivery_fee.py` + `test_delivery_fee.py` (coloured) and real `python -m unittest -v` output (7 ok) side by side | Judge by diff and tests, not by "Done!"; boundary tests 75 / 74.99 / non-Prime | "Nothing on this slide was written by me. This is the actual run." |
| 12 | 5 | Pull request: Copilot-ревью — вторая пара глаз, не судья | Pull request: Copilot review is a second pair of eyes, not the judge | html-mockup: GitHub PR #13 "Files changed" with the real diff, a Copilot review comment on the money line ("consider Decimal; 74.99 test present"), Ola's green "Approved", CI check green | Review comment = suggestion; a human approves; tests are the gate | "Copilot found one thing worth thinking about and one thing it already saw covered." |
| 13 | 3 | copilot-instructions.md — README для робота | copilot-instructions.md: a README for the robot | real-artifact: the 5-line `.github/copilot-instructions.md` rendered in a file card, arrows to where each rule showed up in the diff/tests | Team rules in one file; Copilot reads it every time; keep it short | "Rule 4 'add boundary tests' is why the 74.99 test exists." |
| 14 | 3 | Где живёт GitHub Copilot: редактор, github.com, терминал, облако — глубже в L16 | Where GitHub Copilot lives: editor, github.com, terminal, cloud; depth in L16 | svg: map with 4 pins (editor: VS Code / JetBrains / Visual Studio; github.com: PR review + issues; terminal: Copilot CLI; cloud agent: opens a PR by itself) with a small "Free: yes / yes / yes / no" tick row (notes §2) | Four doors to the same assistant; today we used two; L16 opens the rest | "Remember the map; L16 walks every room." |
| 15 | 5 | Перерыв | Break | timer | — | — |
| 16 | 6 | Windows: клавиша Copilot, приложение и Vision — помощник, который видит экран | Windows: the Copilot key, the app and Vision: the assistant that sees your screen | svg keyboard with the Copilot key highlighted + html-mockup Windows desktop with the Copilot app window; chips: chat and voice, Vision (shares the chosen window), file search (docx/xlsx/pptx/txt/pdf), screenshots (notes §9); footnote "key or Win+C; work accounts open the web chat instead" (notes §9, §11) | Press the key, ask about what is on screen; it sees only the window you share | "Pavel presses one key and asks about the window he is looking at." |
| 17 | 3 | День релиза: чек-лист открыт, Copilot читает его | Release day: the checklist is open, Copilot reads it | html-mockup: Notepad with the real `release_checklist.txt` + Copilot answer "item 6 catches an outside-zone change" | Local file as context; same rule as slide 04; fallback = paste the text | "Which item saves us if outside-zone fees break? Item 6, and it quotes it." |
| 18 | 5 | Чек-лист приёмки: 6 проверок (= рубрика ДЗ) | Acceptance checklist: 6 checks (= homework rubric) | svg checklist with our real results: brief marks sources; issue has numbers; diff small; tests green; review read; evidence kept | 6 checks, the same for every Copilot | "If any of these is missing, you did not use Copilot, you trusted it." |
| 19 | 4 | Границы: Copilot видит только то, что можете открыть вы | Limits: Copilot sees only what you can open | svg: person with a key; three traps as icons: wrong account, pasted secret, "it said done" | Your permissions = its permissions; never paste keys/customer data; work accounts: not used for training; personal GitHub plans: switch training off in settings (notes §5, §8) | "Copilot is not a colleague with admin rights. It is you, faster." |
| 20 | 7 | Домашнее задание: проведите фичу курьерского приложения через три Copilot | Homework: take a courier-app feature through three Copilots | html: deliverables list + repo tree (brief.md, delivery_fee.py, tests, PR link, checklist.md) | Free tiers only; the 6 checks of slide 18 are the rubric | "Same feature, your repo, your screenshots." |
| 21 | 3 | Итог: три места, одна привычка — проверяй результат | Summary: three places, one habit: check the result | svg: the slide-02 strip compressed + 5 rules; L08 preview tile (Excel from slide 07) | 3 Copilots by place; context; diff+tests; evidence; L08 = data | "Next week Copilot opens a spreadsheet and we do real analysis." |

Minutes: 2+4+4+4+5+5+3+4+3+6+6+5+3+3+5 = 62 (part 1 incl. break), 6+3+5+4+7+3 = 28 (part 2), total 90.

## E. Live demo plan and homework

**Demo (14 min total, inside slides 05–06, 10–11, 17).** All files synthetic, from the re-skinned demo kit.
- A. Brief (slide 06, 3 min): Copilot in Word, or free Copilot Chat in Edge with `meeting_notes.md` pasted. Prompt: "Using only these notes, write a one-page brief: decisions, open questions, owners. At the end list which sentences are yours." Check: $75 Prime, $100 stays, outside-zone unchanged, flag owner still open.
- B. Code (slides 10–11, 8 min): VS Code + GitHub Copilot Free. Prompt 1 (chat): "Read ISSUE.md and .github/copilot-instructions.md, propose a plan, do not edit." Prompt 2 (agent mode if available, else chat + manual paste): "Implement it and add boundary tests, run the tests." Then `git diff` and `python -m unittest -v` in the terminal, on screen.
- C. Windows (slide 17, 3 min): open `release_checklist.txt`, press the Copilot key, Vision or paste: "Which item catches an outside-zone fee change?"
- No-licence / UI-changed fallback: slides 06, 11, 17 already carry the deterministic result (expected brief, real diff + real test output, checklist answer). Say "the button moved, the rule did not", switch to the slide, max 90 s of troubleshooting.

**Homework (slide 20).** Deliverable: a public GitHub repo `courier-copilot-week` with `brief.md`, `delivery_fee.py`, `test_delivery_fee.py`, one merged PR, `checklist.md`, and a `README.md` with 3 screenshots (brief, Copilot in editor, PR). Feature: the same Prime rule or a sibling rule (e.g. "rain surcharge $2 outside the zone", any number of the student's choice). Tools: GitHub Copilot Free in VS Code, Copilot Chat (web, Edge or Windows app), optional M365 if the student has it. Copilot code review on the PR costs AI credits outside paid plans (notes §1–2), so a human review comment is accepted. Students on personal GitHub plans switch off "Allow GitHub to use my data for AI model training" before starting (notes §5). No real customer data.
Rubric (6 checks, = slide 18): (1) brief marks which lines come from the notes and which were invented; (2) issue states numbers and what must not change; (3) diff ≤ 10 lines of logic; (4) tests cover the boundary (value, value − 0.01, non-member) and are green in a screenshot or CI; (5) PR has a review comment (Copilot or human) that was answered; (6) `checklist.md` names one check that would stop the release.

## F. Visual production list

| Slide | Type | What the builder needs |
|---|---|---|
| 01 | reused-image | `L05/assets/v2/img/cover_shot2.jpg`, scope line, instructor title per AGENTS.md §1.5 |
| 02, 21 | svg | 6-station strip Mon–Fri; excerpts: recap line from `meeting_notes.md`, brief first line, issue title, 2-line diff, review comment text, checklist item 6; tool glyphs drawn as simple shapes (no logos needed) |
| 03 | svg | three circles with labels and 2 example artifacts each (issue/PR; mail/doc/meeting; file/screen) |
| 04 | svg + code | model box, chips "file / chat / repo / screen", L03 snippet (take the 3-line call from L03 deck) |
| 05 | html-mockup | Teams-like window (dark), meeting title "Prime delivery rule", right "Recap" pane rendering `meeting_notes.md` re-skinned; label "schematic" |
| 06 | html-mockup | Word-like white page (brief text from `fallback_outputs/m365_expected_brief.md`, re-skinned), side pane with the prompt from E.A; 2 callouts; label "schematic"; screenshot slot (optional) |
| 07 | html-mockup | Outlook pane: 3-message support thread + "Summary" box; Excel pane: 8-row table (order_id, zone, is_prime, subtotal) + Copilot answer; data invented by builder, consistent with the rule |
| 08 | svg | two concentric rings, labels, 6-row price strip with "October 2026" date tag; all figures from notes §1 and "Prices" table; nothing else in the deck carries a price or a plan name |
| 09 | html-mockup | GitHub issue page: title, 5 bullets + acceptance from re-skinned `ISSUE.md`, labels `feature`, assignee Pavel; screenshot slot (optional) |
| 10 | html-mockup | VS Code-like window: file tree (4 files), editor with `delivery_fee.py` and ghost-text line, chat panel with 2 prompts, terminal; label "schematic"; screenshot slot (optional) |
| 11 | real-artifact | run in container: re-skin repo, `git init`, commit base, apply expected solution, `git diff --no-color`, `python -m unittest -v`; render both as coloured code blocks (≥16px mono) |
| 12 | html-mockup | GitHub PR "Files changed": real diff from slide 11, Copilot review comment (text in C), "Approved" by Ola, green check "tests 7/7" |
| 13 | real-artifact | `.github/copilot-instructions.md` (5 lines) + 3 arrows to diff lines / test names |
| 14 | svg | 4-pin map (editor, github.com, terminal, cloud agent) with one-line "what you type there"; Free yes/yes/yes/no ticks (notes §2); "L16" badge |
| 16 | svg + html-mockup | keyboard SVG with highlighted Copilot key; Windows-like desktop with Copilot app window and 4 feature chips (notes §9); label "schematic"; screenshot slot (optional) |
| 17 | html-mockup | Notepad-like window with `release_checklist.txt` (re-skinned) + Copilot answer card |
| 18 | svg | 6-row checklist with green ticks and our real values |
| 19 | svg | person + key, three trap icons with one-line captions |
| 20 | html | deliverables list + repo tree block |

Re-skin of the demo kit (builder task, ~30 min): copy `l07_old/demo_assets/` → `L07/demo_courier_copilot/`, rename `shipping.py` → `delivery_fee.py`, `country` → `zone` ("CITY"/"OUTSIDE"), `is_vip` → `is_prime`, "VIP" → "Prime", "international" → "outside the zone", "US store" → "the courier app"; keep 75 / 100 / 7.50 / 18.00; update ISSUE.md, tests, expected_solution, meeting_notes.md, release_checklist.txt, fallback brief; run the tests (7 ok) before building slide 11.

## G. Jargon budget (max 10 new terms; everything else in plain words)

1. **Context** — what the assistant can see when it answers: the open file, the chat, the repo, the shared screen.
2. **Repository (repo)** — the project folder with its history, kept on GitHub.
3. **Issue** — a task written down on GitHub, with a number.
4. **Pull request (PR)** — "please take my change": the page where the change is shown, discussed and approved.
5. **Diff** — the exact lines added and removed.
6. **Unit test** — a small script that checks one rule (e.g. 74.99 pays 7.50); green = passed.
7. **Completion** — the grey text the editor proposes as you type.
8. **Agent (mode)** — the assistant edits several files and runs commands itself; you review the result (depth in L16).
9. **Custom instructions** — a short file of team rules the assistant reads every time.
10. **Copilot key / Vision** — the Windows key that opens Copilot; Vision = it looks at the window you choose to share.
Avoid: grounding, tenant, Graph, Entra, EDP, control plane, trust boundary, MCP (say "connectors, L12"), Copilot+ PC (one line max), Recall (one line max), governance, policy.
