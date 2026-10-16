# Lesson 14 • Cheatsheet: rapid AI app prototype

**In one sentence:** a one-day prototype answers “what will it look like”; Streamlit is a Python web page that reruns on every click, so memory goes in session_state and keys in secrets; a coding agent writes the code and you check it; sometimes AI Studio Build is enough.

## Slides (17, 90 min)
01 Cover (2) · 02 Why a prototype (5) · 03 Streamlit, screenshot (5) · 04 Code (6) · 05 Reruns (5) · 06 session_state / cache / secrets (5) · 07 Agent prompt (5) · 08 Running (5) · 09 Publishing (5) · 10 No-code builders (6) · 11 What to choose (5) · 12 Break (5) · 13 Hands-on (10) · 14 Security (5) · 15 Prototype → product (5) · 16 Homework (6) · 17 Summary (5)

## Key facts (16.10.2026)
| What | Fact |
|---|---|
| Streamlit | 1.66 (14.10.2026), Apache-2.0, Python 3.11+ |
| Running | `pip install streamlit`, `streamlit run app.py`, localhost:8501 |
| Agent | `streamlit skills` — official skills for Claude Code, Codex, Cursor |
| Community Cloud | free, from GitHub, public by default, one private app; sleeps after 12 h |
| HF Spaces | no longer free for Streamlit |
| AI Studio Build | an app from a description, private by default, key server-side |

## Terms
session_state — a visitor’s memory · cache — a shared cache for everyone · secrets — keys outside the code · localhost — this computer · .gitignore — a list of files kept out of the repo

## Recheck within 24 hours
1. Streamlit version and Python requirement. 2. Whether llm-examples.streamlit.app works. 3. Community Cloud rules. 4. AI Studio Build.
