# Lesson 07: GitHub, Microsoft 365 and Windows Copilot. One feature, three Copilots

## Status: deck v2 (21 slides, 90 min, facts as of October 2026), companion documents written 2026-10-13

Deck structure: a team of the courier app ships one feature in a week (Prime subscribers get free delivery from $75 inside the city), with Copilot at every step. Three Copilots by place (repository, work documents, your PC), why they are the same kind of model as in L03 (context = what it sees), then the week step by step (Teams, Word, Outlook and Excel, free vs paid, GitHub issue, editor, a real 2-line diff with 7 green tests, pull request review, `copilot-instructions.md`, four doors to GitHub Copilot), break, Windows (Copilot key, app, Vision), the release checklist, six checks (= homework rubric), limits and privacy, homework (`courier-copilot-week`), summary. Three live demos: brief (slide 6), code (slides 10–11), Windows (slide 17). Lesson graph: `L07_10_Lesson_Graph.md`. PDFs are in this folder (21 pages each); rebuild after any deck change with `python deck_v2/build.py` on a machine with Edge or Chrome.

The old Drive package (`07 — GitHub, Microsoft 365 and Windows Copilot Ecosystem — DONE`, Sep 2026: docx/pptx, enterprise-governance focus, a licensed tenant and an organisation GitHub account) is replaced by this folder. What was kept: the demo kit idea (a small repo with an issue, instructions and tests; meeting notes; a release checklist; fallback outputs; the pre-class check), re-skinned onto the courier case (`shipping.py` → `delivery_fee.py`, VIP → Prime, country → zone); the rules “look at the diff and the tests, not at the word done”, “the button moved, the rule did not”, the 90-second troubleshooting limit, synthetic data only; and the privacy point (work accounts are not used for training, switch it off on personal GitHub plans). What was dropped: the enterprise vocabulary (tenant, Entra, EDP, grounding, control plane), eight reference tables, “Project Northstar”, the “Copilot Operating Map” workshop and the 20-point decision-memo rubric.

## Source of truth
- **Generator:** `deck_v2/build.py` (RU/EN strings side by side, `t("ru", "en")`; slide order in `SLIDES`; minutes per slide in `MINUTES`) + `deck_v2/style.css` + `deck_v2/deck.js`. Run `python deck_v2/build.py` (HTML + PDF) or `--no-pdf`. Edit the generator, not the HTML.
- **Real artifacts:** `python deck_v2/make_artifacts.py` copies `demo_courier_copilot/sample_repo` to a temp folder, commits the base, applies `expected_solution/`, and captures `git diff` and `python -m unittest -v` into `deck_v2/artifacts.json`. Slides 11–13 and 18 read their numbers from that file (2 lines of logic, +3 tests, 7 of 7 ok). Needs only Python 3 and git.
- **Instructor scripts** `L07_02_*` are generated from the deck: `python deck_v2/make_docs.py` (timing table and speaker text come from `build.py`; the short “On screen” lines live in `make_docs.py`).
- **Slide decks (RU/EN):** `presentation_L07_Copilot_Ecosystem_v2.html` / `presentation_L07_Copilot_Ecosystem_EN_v2.html` + PDFs with the same basenames. Self-contained HTML: `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 15. Slides 5–7, 9, 10, 12, 16 and 17 are labelled “schematic” (mockups, not screenshots).
- **Demo kit:** `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`). Check before class: `cd sample_repo && python smoke_check.py` (baseline: 4 tests pass).
- **Facts:** `L07_08_Source_Notes_Research_2026-10.md` (research notes merged with the independent verification of 2026-10-13; corrections log and volatile list inside). Plan and critique of the old lesson: `L07_09_Lesson_Plan_v2.md`.
- **Companion documents:** instructor scripts (`L07_02_*`), cheatsheets (`L07_00_*`), demo runbook (`L07_04_*`), homework (`L07_05_*`), research notes (`L07_08_*`), lesson graph (`L07_10_*`).

## Slide map (21 slides, 90 minutes incl. 5-minute break)
| # | Min | Time | Slide | Main visual |
|---|---|---|---|---|

| 01 | 2 | 00:00–02:00 | Cover: one Copilot? a family of three | Frame of L05 shot 2 |
| 02 | 4 | 02:00–06:00 | The week: one feature, six steps | Mon–Fri strip, six stations with real excerpts |
| 03 | 4 | 06:00–10:00 | Three Copilots, three places | Three circles: repository / work documents / your PC |
| 04 | 4 | 10:00–14:00 | Same model as L03: context | Question + context chips → model → answer; L03 call snippet |
| 05 | 5 | 14:00–19:00 | Teams: meeting to tasks | Teams window mockup with Copilot Recap |
| 06 | 5 | 19:00–24:00 | Word: notes to brief (demo A) | Word mockup: brief + prompt pane, source vs invented marks |
| 07 | 3 | 24:00–27:00 | Outlook and Excel | Outlook summary + Excel 8-row table (schematic) |
| 08 | 4 | 27:00–31:00 | Free and paid, October 2026 | Two rings (free vs licensed) + plan price strip |
| 09 | 3 | 31:00–34:00 | GitHub issue | GitHub issue #12 mockup |
| 10 | 6 | 34:00–40:00 | Editor: completion, chat, agent (demo B) | VS Code mockup: ghost text, chat, terminal |
| 11 | 6 | 40:00–46:00 | Result: diff and tests | Real `git diff` + real `unittest -v` output (7 ok) |
| 12 | 5 | 46:00–51:00 | Pull request and Copilot review | Pull request #13 mockup: real diff, Copilot review comment, Approved |
| 13 | 3 | 51:00–54:00 | copilot-instructions.md | `copilot-instructions.md` with arrows to the result |
| 14 | 3 | 54:00–57:00 | Four doors to GitHub Copilot | Map of four doors to GitHub Copilot |
| 15 | 5 | 57:00–62:00 | Break | Timer |
| 16 | 6 | 62:00–68:00 | Windows: key, app, Vision | Windows mockup: Copilot key, app, Vision, five features |
| 17 | 3 | 68:00–71:00 | Release day: checklist (demo C) | Notepad mockup with the checklist + Copilot answer |
| 18 | 5 | 71:00–76:00 | Six checks (= rubric) | Six checks with our real results (= homework rubric) |
| 19 | 4 | 76:00–80:00 | Limits and privacy | Person with a key, three traps, training-on-data note |
| 20 | 7 | 80:00–87:00 | Homework: courier-copilot-week | Repo tree `courier-copilot-week`, deliverables |
| 21 | 3 | 87:00–90:00 | Summary | Compressed week strip, 5 rules, L08 tile |
