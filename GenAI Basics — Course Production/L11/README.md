# Lesson 11: Function Calling and Your First Agent

## Status: deck v2 (21 slides, 90 min), facts as of 2026-10-16, audits applied

Rebuilt from the September 2026 Drive package (`11 — Function Calling and Building Your First Agent — DONE`: engineering-heavy pptx with JSON Schema, wire formats of three vendors, idempotency). The v2 deck is a beginner tour built around one real, free demo in Google AI Studio: the model proposes `get_order_status(order_id="417")`, you return synthetic data, the model answers the customer.

Arc: the problem (a model invents live data) → you have seen tools already (Claude web search) → what a tool is (name, description, parameters) → the model proposes, your program executes (trust boundary) → demo in two steps → built-in tools → writing descriptions → the agent loop with a step limit → reference code (google-genai) → local models with tools (bridge from L10) → a coding agent builds the first agent → market → break → risks (prompt injection) → reliability (τ²/τ³-bench) → four rules → exercise → homework → summary.

## Source of truth
- **Generator:** `deck_v2/build.py` (RU/EN `t("ru", "en")`, slide order in `SLIDES`, minutes in `min=`) + `deck_v2/style.css` + `deck_v2/deck.js` (same engine as L06 and L10). `python deck_v2/build.py` (HTML + PDF) or `--no-pdf`.
- **Instructor scripts** `L11_02_*`: `python deck_v2/make_docs.py`.
- **Decks:** `presentation_L11_Function_Calling_First_Agent_v2.html` / `_EN_v2.html` + PDFs.
- **Facts:** `L11_08_Source_Notes_Research_2026-10.md` (checked 2026-10-16, image credits).
- **Companion documents:** cheatsheets with the 24 h recheck list (`L11_00_*`), homework (`L11_05_*`).

## Before class
Open AI Studio, switch to Gemini 3.8 Flash (a new chat defaults to the paid Gemini 4 Argon), enable Function calling and pre-fill `get_order_status`. The slide 11 code is a reference example and was not executed for this build; run it once with your own Gemini API key before showing it.

## Slide map (21 slides, 90 minutes incl. 5-minute break)
| # | Min | Slide | Main visual |
|---|---|---|---|
| 01 | 2 | Cover | Schematic fragment |
| 02 | 4 | The model does not know where your order is | Invented answer vs AI Studio screenshot |
| 03 | 4 | Chat assistants already call tools | Claude web-search screenshot, callouts 1–3 |
| 04 | 5 | A tool = name, description, parameters | AI Studio Function declarations screenshot |
| 05 | 5 | The model proposes, your program runs it | Trust-boundary schematic |
| 06 | 5 | Demo step 1: the model asks for a function call | AI Studio screenshot |
| 07 | 4 | Demo step 2: return the result | AI Studio screenshot + JSON |
| 08 | 4 | Built-in tools | AI Studio Tools panel + three tool kinds |
| 09 | 4 | The model picks a tool by its description | Weak vs good description |
| 10 | 5 | Agent = model + tools + loop | Agent-loop schematic |
| 11 | 5 | Code (reference) | google-genai example |
| 12 | 4 | Local models call functions too | Tool-capable models list |
| 13 | 4 | A coding agent builds your first agent | Prompt |
| 14 | 4 | Where agents live | Three columns |
| 15 | 5 | Break | Timer |
| 16 | 5 | Risks: someone else’s text gives orders | Risk list + defences |
| 17 | 4 | Even the best agents fail | τ²/τ³-bench bars |
| 18 | 4 | Four rules | 4 cards (= homework rubric) |
| 19 | 5 | Exercise: which tool? | 4 questions with answers |
| 20 | 5 | Homework | Steps + folder tree |
| 21 | 3 | Summary | 4 takeaways + L12 preview |
