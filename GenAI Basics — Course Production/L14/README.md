# Lesson 14: Rapid AI App Prototype — Streamlit and No-Code Builders

## Status: deck v2 (17 slides, 90 min incl. a 10-minute hands-on), facts as of 2026-10-16, audits applied

Rebuilt from the September 2026 Drive package (`14 — Streamlit and Rapid AI Prototyping — DONE`). The v2 deck is for beginners who let a coding agent write the code: why a one-day prototype, Streamlit on the official demo chat (own capture, cropped), a 14-line reference chat that runs as is (with an `ask_llm` stub), the rerun loop and session_state, memory/cache/secrets, a coding-agent prompt with `streamlit skills`, running locally, publishing (a Community Cloud app from a public repo is public, only one private app; Hugging Face Spaces is no longer free for Streamlit), no-code builders (Google AI Studio Build capture, Claude Artifacts, Lovable/Bolt/v0), a choice grid, hands-on, safety, prototype → product, homework (prototype + feedback from three people). Diagrams (cover window, idea → prototype → feedback → product, rerun loop) are drawn in HTML/SVG with RU/EN labels.

## Source of truth
- **Generator:** `deck_v2/build.py` + `style.css` + `deck.js`. `python deck_v2/build.py` or `--no-pdf`.
- **Instructor scripts** `L14_02_*`: `python deck_v2/make_docs.py`.
- **Decks:** `presentation_L14_Streamlit_Rapid_Prototyping_v2.html` / `_EN_v2.html` + PDFs.
- **Facts:** `L14_08_Source_Notes_Research_2026-10.md`. Companion docs: cheatsheets `L14_00_*`, homework `L14_05_*`.

## Before class
Open llm-examples.streamlit.app (may need a minute to wake) and AI Studio Build. Streamlit needs Python 3.11+.
