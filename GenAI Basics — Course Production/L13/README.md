# Lesson 13: Your Own AI Assistant — Projects, Plugins, Responses API, Agents SDK

## Status: deck v2 (17 slides, 90 min incl. a 10-minute hands-on), facts as of 2026-10-16, audits applied

Rebuilt from the September 2026 Drive package (`13 — Custom GPTs, Responses API and Agents SDK — DONE`). OpenAI retires custom GPTs on **11 December 2026** (they move into ChatGPT plugins; the banner is on chatgpt.com/gpts), and Gemini Gems become skills (personal accounts from 17 November 2026, Workspace from March 2027), so the v2 lesson teaches the product-independent recipe "instructions + knowledge + tools + model" with real captures of a Claude project and the ChatGPT Plugin Creator, four tests before sharing, and the code ladder Responses API → Agents SDK → Agents API.

## Source of truth
- **Generator:** `deck_v2/build.py` (17 slides; minutes only in `_MIN`; slides 02 and 09 diagrams are HTML with RU/EN labels) + `style.css` + `deck.js`. `python deck_v2/build.py` or `--no-pdf`.
- **Instructor scripts** `L13_02_*`: `python deck_v2/make_docs.py`.
- **Decks:** `presentation_L13_Custom_Assistants_and_Agents_SDK_v2.html` / `_EN_v2.html` + PDFs.
- **Facts:** `L13_08_Source_Notes_Research_2026-10.md`. Companion docs: cheatsheets `L13_00_*`, homework `L13_05_*`.

## Before class
Check the ChatGPT path (Plugins → Add → Create plugin; captured on Business, may be missing on Free/Plus, where students fall back to Claude) and the Claude Projects panel. Slides 10–11 code is a reference and was not executed.
