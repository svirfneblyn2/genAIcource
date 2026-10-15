# Lesson 07: The Microsoft Copilot ecosystem, an overview

## Status: deck v3 (24 slides, 90 min, facts as of 13 Oct 2026), companion documents updated 2026-10-13

v3 is a beginner overview of the whole Microsoft AI family for IT Park University students (90 minutes live in Microsoft Teams). Students get an ecosystem map (for you / Microsoft 365 apps and agents / for developers / for the company, with the shared core models) and one question to pick a zone: *whose information is it and where does it live?* A “new words” slide separates model, chat, assistant and agent (plus context and knowledge, instructions, skill, connector). Inside are the same models as in L03; what differs is what Copilot sees and what it may do (answers → edits the document → agent). The lesson covers the one Microsoft Copilot app with two sign-ins, what is free and what is paid (one slide, dated), a short live look at the Copilot app (brief from meeting notes), Vision over a release checklist, Copilot in Windows (what is free, the official limits, Copilot+ PC features, the training toggle), Teams and Word as the instructor's main live demos, Excel (with our real Copilot mistake on an orders table), PowerPoint and Outlook, a break, agents (Researcher, Analyst, Cowork, Autopilot), two slides on building your own agent in Agent Builder (our real build in the free IT Park school account), GitHub Copilot on one slide (depth in L16), Copilot for companies, a “where does this question go?” game with safety rules, homework and a summary. The courier team from L04–L06 (Anna, Pavel, Ola; the Prime rule “free delivery from $75 in the city”) is a thread through the product slides, not the lesson itself.

## Why v3 replaced v2
1. **Wrong goal.** v2 (`deck_v2/`, 21 slides) was a GitHub-centric lesson: issue, editor, diff, tests, pull request, a code-based rubric and a repository homework. The L07 goal is an **overview** of the Microsoft family; GitHub Copilot is one part of it (depth moves to L16).
2. **Mockups instead of real pictures.** 8 of v2's slides were hand-drawn HTML “windows” labelled “schematic”. Every product picture in v3 is a real screenshot: our own captures, official Microsoft / GitHub images or frames from YouTube videos, each credited on the slide.
3. **Out of date after August–September 2026.** The personal and work Copilot were merged into one **Microsoft Copilot** app (Home / Code / Autopilot tabs, 25 Sep 2026); agents became the main story (Cowork GA 16 Jun 2026, Researcher, Analyst, Facilitator, Autopilot preview); Mico, Groups, Podcasts, Deep Research and Copilot Labs were retired (18 Aug 2026), Edge Copilot Mode closed (13 May 2026), Excel `=COPILOT()` removed (14 Sep 2026); agentic work is billed in credits; Copilot runs OpenAI, Anthropic and Microsoft MAI models.
4. **Missing beginner basics:** what I already have for free, where the button is, how not to get lost in the names. v3 adds availability badges on every product slide, a name dictionary and a terms slide.

The v2 files were removed on 2026-10-15; they are in git history (tag `archive/pre-cleanup-2026-10-15`). `make_artifacts.py` moved from `deck_v2/` to `deck_v3/`.

## Source of truth
- **Generator:** `deck_v3/build.py` (RU/EN strings side by side, `t("ru", "en")`; slide order in `SLIDES`; minutes per slide in `MINUTES`, asserted to sum to 90; speaker notes in `notes(...)`; image credits in the `SRC` dict) + `deck_v3/style.css` + `deck_v3/deck.js`. Edit the generator, not the HTML.
- **Rebuild:** `python deck_v3/build.py` (HTML + PDF for both languages; needs Edge or Chrome for the PDF) or `python deck_v3/build.py --no-pdf`.
- **Slide decks (RU/EN):** `presentation_L07_Copilot_Ecosystem_v3.html` / `presentation_L07_Copilot_Ecosystem_EN_v3.html` + PDFs with the same basenames. Self-contained HTML (images from `assets/v3/img/`): `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 15.
- **Instructor scripts** `L07_02_Instructor_Script_90MIN_v3.md` / `_v3_EN.md` are generated: `python deck_v3/make_docs.py` (timing from `MINUTES`, titles and speaker text from `build.py`; the short “On screen” lines live in the `SCREEN` dict of `make_docs.py`). Re-run after any deck change.
- **Real diff on slide 20:** `deck_v3/artifacts.json` (the `git diff` of the Prime rule and the 7-test run from `demo_courier_copilot/sample_repo`). Regenerate with `python deck_v3/make_artifacts.py`.
- **Plan:** `L07_11_Lesson_Plan_v3_Ecosystem.md`. **Facts:** `L07_12_Research_MS_Ecosystem_2026-10-13.md` (every fact with a source and date; volatile list in section 7) and **`L07_13_Research_Windows_AgentBuilder_2026-10-13.md`** (free Copilot on Windows: features, official and unpublished limits, privacy toggles; Agent Builder: who can build, capability by licence, step by step, field and knowledge limits, templates, Copilot Studio; Copilot APIs; sources for slides 10, 18 and 19). **Video frame sources:** `assets/v3/VISUAL_SOURCES_youtube.md`.
- **Demo kit:** `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv` with 12 synthetic orders, `fallback_outputs/`; `sample_repo/` kept as the backup example for slide 20 and the bridge to L16).
- **Companion documents (v3):** cheatsheets `L07_00_Lecture_Cheatsheet_v3*.md`, instructor scripts `L07_02_*_v3*.md`, demo runbook `L07_04_Live_Demo_Runbook_v3*.md`, homework `L07_05_Homework_v3*.md` (with an optional bonus step 5 and an instructor-only answer key).

## Slide map (24 slides, 90 minutes incl. 5-minute break)
Times follow `MINUTES` in `deck_v3/build.py`.

| # | Min | Time | Slide | Main picture (credit) |
|---|---|---|---|---|
| 01 | 2 | 00:00–02:00 | Copilot is not a button, it is a family | `ms_copilot_hero.jpg`: hero of the new Copilot (Microsoft blog, 25 Sep 2026) |
| 02 | 5 | 02:00–07:00 | The Microsoft AI family: who lives where (+ Teams poll) | ecosystem map with app tiles: for you / Microsoft 365 apps + agents / for developers / for the company + core models (simplified tiles, not official logos; no photo) |
| 03 | 2 | 07:00–09:00 | Model → chat → assistant → agent | `own_dia_agent_stages_en.png` (our diagram, 13 Oct 2026) |
| 04 | 2 | 09:00–11:00 | Assistant or agent: who drives the work | `own_dia_assistant_vs_agent_en.png` (our diagram, 13 Oct 2026) |
| 05 | 3 | 11:00–14:00 | Inside are the same models you called in L03 | `own_work_model_picker.jpg`: model menu of the IT Park work Copilot (our capture) + three-level ladder |
| 06 | 4 | 14:00–18:00 | One Microsoft Copilot app, two doors | `own_account_switcher.jpg` (our capture); `ms_app_home.jpg` Home · Code · Autopilot (Microsoft blog, 25 Sep 2026); name dictionary |
| 07 | 3 | 18:00–21:00 | What is free and what is paid | price ladder as of 13 Oct 2026 (no photo) |
| 08 | 3 | 21:00–24:00 | Demo A: meeting notes → brief → launch picture (the Copilot app, briefly) | `own_work_chat_brief_1.jpg` brief in Copilot Chat (Basic); `own_prime_poster.jpg` picture from personal Copilot (our captures) |
| 09 | 3 | 24:00–27:00 | Demo B: Copilot Vision sees the window you share | `yt_vision_picker.jpg` (Kevin Stratvert, YouTube, 22 Oct 2025) |
| 10 | 5 | 27:00–32:00 | Copilot in Windows: what it can do and where the limits are | `yt_ask_copilot_taskbar.jpg` (Microsoft Mechanics, YouTube, 18 Feb 2026); limits panel: 20 files/chat, 50 MB/file, 18-month history, unpublished limits, Copilot+ PC only; training toggle; Edge line |
| 11 | 6 | 32:00–38:00 | Teams: a meeting becomes a recap and tasks (**live demo**) | `ms_teams_facilitator.jpg`, `ms_teams_recap_copilot.jpg` (Microsoft Support, 2026) |
| 12 | 5 | 38:00–43:00 | Word: a draft from a file and edits right in the document (**live demo**) | `yt_word_edit.jpg` (Microsoft Copilot, YouTube, 9 Jul 2026) |
| 13 | 5 | 43:00–48:00 | Excel: ask the table in words, then check the numbers | `ms_excel_modes.jpg` (Microsoft Support, 2026); `own_orders_crop.jpg` our free Copilot Chat run with the outside-zone mistake (our capture) |
| 14 | 4 | 48:00–52:00 | PowerPoint and Outlook: the same button, a different document | `ms_ppt_visualize.jpg`, `ms_outlook_summary.jpg` (Microsoft Support, 2026) |
| 15 | 5 | 52:00–57:00 | Break: 5 minutes | timer |
| 16 | 4 | 57:00–61:00 | Agents: Copilot does the work, not just answers | `yt_researcher_report.jpg` (Mike Tholfsen, YouTube, 13 Apr 2026); `yt_cowork_workspace.jpg` (Kevin Stratvert, YouTube, 16 Jul 2026); `own_work_agent_store.jpg` (our capture) |
| 17 | 2 | 61:00–63:00 | Anatomy of an agent: model + harness + five parts | `own_dia_agent_anatomy_en.png` (our diagram, 13 Oct 2026) |
| 18 | 3 | 63:00–66:00 | Agent Builder: an agent is Copilot with your instructions and your knowledge | `own_ab_01_start_crop.jpg` Agent Builder start screen in the IT Park school account (our capture) + four parts of an agent, six agent ideas |
| 19 | 5 | 66:00–71:00 | We built a support agent in 5 minutes: a real run | `own_ab_03_configure_instructions_crop.jpg`, `own_ab_04_knowledge_prompts_crop.jpg`, `own_ab_05_preview_test_crop.jpg`, `own_ab_07_created_crop.jpg` (our captures) + our prompt |
| 20 | 4 | 71:00–75:00 | GitHub Copilot: Copilot for code (more in L16) | `gh_code_review.jpg` (GitHub blog, 2 Jun 2026) + our real 2-line diff from `artifacts.json` |
| 21 | 2 | 75:00–77:00 | Copilot for the company: three examples | `yt_foundry_models.jpg` (Microsoft Mechanics, 3 Dec 2025); `yt_security_copilot.jpg` (Microsoft Security, 3 Feb 2026); `yt_studio_workflow.jpg` (Microsoft Mechanics, 5 Oct 2026) |
| 22 | 5 | 77:00–82:00 | Game: where does this question go? (+ safety rules, Teams poll) | question cards (no photo) |
| 23 | 5 | 82:00–87:00 | Homework: the courier team's week with Copilot | `own_work_home.jpg` IT Park school account in Copilot Chat (our capture) |
| 24 | 3 | 87:00–90:00 | Summary: for you · for work · for code · for the company | reused `own_prime_poster`, `ms_teams_facilitator`, `gh_code_review`, `yt_security_copilot` |

**Live parts:** slide 8, the Copilot app shown briefly (school account: tour + the brief; the picture comes from the slide); slide 9, Vision over `release_checklist.txt` in Notepad; **slides 11–13, Teams / Word / Excel: screenshots on the slide, then the same task live in free Copilot Chat (IT Park)**; optional demo D on slide 19, building the courier support agent in Agent Builder with the exact prompt and two Preview test questions. Details: `L07_04_Live_Demo_Runbook_v3_EN.md`.

## How the lesson is demoed
**Decision (verified 13 Oct 2026, the instructor has no Microsoft 365 Copilot licence: personal account without Microsoft 365, IT Park = Copilot Chat (Basic) with no Word/Excel, EPAM account unusable on this PC):** no video clips in the lesson; Teams, Word and Excel Copilot are shown with the screenshots on slides 11–13 (official Microsoft images and video frames), and the live part is done in free Copilot Chat on the IT Park account, which students also have (meeting_notes.md as a “transcript” → recap; upload meeting_notes → one-page brief + Word file → shorten Decisions; orders.csv → slide question, then add the CITY-only Prime rule and compare). See runbook sections 5–7.

## Asset provenance (`assets/v3/img/`)
- **`own_*`: our captures**, taken on 2026-10-13 from the Microsoft Copilot app on this PC (personal account and the IT Park school account, Copilot Chat (Basic)), with synthetic courier data only (`meeting_notes.md`, `orders.csv`). Avatars, e-mails and names are blurred. Credit on the slide: “Our capture, 13 Oct 2026”.
- **`own_ab_*`: our Agent Builder run**, 13 Oct 2026, IT Park school account (Copilot Chat (Basic), no licence): Agents → New agent → described “Помощник поддержки курьеров” → Agent Builder generated the instructions and 4 starter prompts → Preview tests (Prime, $80, outside → $18.00, correct; “$70?” → asked for the zone and Prime) → Create → private. Files: `own_ab_00_store_new_agent.jpg` (Agent Store with New agent), `own_ab_01_start.jpg` + `_crop` (start screen), `own_ab_02_whatsnew.jpg` (“What's new”: default skills), `own_ab_03_configure_instructions.jpg` + `_crop` (our prompt and the generated instructions), `own_ab_04_knowledge_prompts.jpg` + `_crop` (knowledge, web search, starter prompts), `own_ab_05_preview_test.jpg` + `_crop` (the $18.00 test), `own_ab_06_preview_clarify.jpg` (the $70 clarifying question), `own_ab_07_created.jpg` + `_crop` (created, private), `own_ab_08_agent_in_use.jpg` (the agent in chat). The `_crop` versions are used on slides 18–19; the rest are spares.
- **`ms_*` / `gh_*`: official Microsoft and GitHub images** from support.microsoft.com, blogs.microsoft.com, the Microsoft Edge blog, Microsoft Learn, microsoft.ai and github.blog (URLs and dates in the Visual sources table of `L07_12_Research_MS_Ecosystem_2026-10-13.md`). © Microsoft / GitHub, used for educational illustration with attribution.
- **`yt_*`: frames from YouTube videos**, credited with channel and upload date on the slide. Channels used in the current build: **Microsoft Copilot**, **Microsoft Mechanics**, **Microsoft Security** (official Microsoft channels), **Kevin Stratvert** and **Mike Tholfsen** (independent reviewers; not presented as official). The `SRC` dict also has a **Microsoft Teams** channel credit for an unused frame. Video titles, URLs and timestamps: `assets/v3/VISUAL_SOURCES_youtube.md`; Agent Builder video picks: `L07_13_Research_Windows_AgentBuilder_2026-10-13.md`, section B5 and “Frames and screenshots”.
- The folder holds 61 images; 28 are used by the current `build.py`. The rest (for example `ms_mai_build.jpg`, `ms_pages.jpg`, `ms_edge_history.jpg`, `own_work_teach.jpg`, `own_work_orders_answer.jpg`, the non-crop `own_ab_*` files) are spares for edits.

## Verify before recording
From section 7 of `L07_12_Research_MS_Ecosystem_2026-10-13.md` and “Unverified / volatile” of `L07_13_Research_Windows_AgentBuilder_2026-10-13.md` (state of 13 Oct 2026). Expect changes at **Microsoft Ignite, 17–20 Nov 2026**.
1. **Prices on slide 7** (US list prices): Microsoft 365 Personal / Family / Premium, Copilot Business $21, Microsoft 365 Copilot $30, GitHub Copilot plans. The Copilot Business promo end date differs between sources; Microsoft 365 Pro price ($99.99) was not re-read directly.
2. **Copilot Credit unit price** for agents: not stated on the October 2026 pages.
3. **Previews:** Autopilot, Code, “Today”, automatic model routing, @Copilot in Teams; all dated “coming weeks”.
4. **Vision for work accounts:** release notes (23 Sep 2026) say rolling out; the support page (26 Jun 2026) says not for commercial customers. Slide 9 badge: “preview”.
5. **Mico:** removed from the main app; the “Learn Live” continuation is from 3rd-party sources only.
6. **Windows Copilot pullback:** mostly anonymous-source reporting; Recall may be renamed.
7. **Model names change monthly** (slide 5 shows Auto and GPT-5.6 in our menu). Keep the talk model-agnostic: OpenAI + Anthropic + Microsoft MAI.
8. **E7 price and promotions:** mostly 3rd-party analyses (not on the slides).
9. **`=COPILOT()`:** retired 14 Sep 2026; any old material showing it is outdated.
10. **Facilitator:** still turned on per meeting.
11. **Clipchamp / Paint / Photos AI:** not re-verified for 2026 (not on the slides).
12. **GitHub “Agent HQ”** branding not found on the 2026 plans page; say “third-party agents / Copilot app”.
13. **Windows limits (slide 10):** only 20 files/chat, 50 MB/file and 18-month history are official; message, prompt-length, image and voice limits are unpublished. Connector eligibility for free accounts and the training-toggle menu path may change (the privacy page describes the older app).
14. **Agent Builder (slides 18–19):** UI labels drift (Learn says Describe / Configure / Try it; the app shows Configure / Preview); capability by licence (free Copilot Chat: instructions, web, up to 4 public sites, code, images; files / SharePoint need pay-as-you-go; mail / Teams need a licence); field limits (name 30, description 1,000, instructions 8,000 characters); tenant admins can switch Agent Builder off; no official confirmation for personal accounts.
15. **On the demo PC:** both sign-ins (personal and IT Park) work, the image limit is not used up, Vision and voice work during a Teams call, the school account shows **Agents → New agent**, and whether a Microsoft 365 Copilot licence is available for the live Teams and Word demos (otherwise use the runbook fallback).
