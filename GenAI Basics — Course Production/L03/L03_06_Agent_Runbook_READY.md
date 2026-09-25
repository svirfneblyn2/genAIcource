# Lecture 03 — Agent / Preparation Runbook

Pre-lecture verification checklist for the instructor-prep agent

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Goal

Prepare a deterministic, low-risk teaching environment. The prep agent verifies package/runtime drift, demo resetability, slide/demo consistency and secret hygiene. It does not create new lecture content during class preparation.

# T-24h checks

- Re-read current official OpenAI model and SDK sources in Source Notes. Record check date.
- Confirm the prepared model supports Responses API, streaming and structured outputs. If not, update OPENAI_MODEL and all examples consistently.
- Create a clean Python 3.10+ environment and install requirements.txt.
- Run `python -m compileall .` and `python tests/test_contract.py`.
- With an instructor-owned teaching key, run 01_first_call.py, 02_stream.py, 03_structured.py and 04_observability.py once. Capture expected output without credentials or personal data.
- Open the deck and verify code snippets match the repository API surface.
- Run a secret scan: .env is ignored; no key-shaped strings in source, docs, slides or screenshots.
- Confirm the workshop starter can be copied/reset in under two minutes.
# T-30 min checks

- Run 00_preflight.py; verify package versions and OPENAI_MODEL.
- Run local contract tests before any provider call.
- Confirm network access and one live first-call smoke test only; avoid burning time/quota on repeated tests.
- Open the exact demo files in order and pre-position the terminal.
- Close environment/key files before screen sharing.
- Keep expected outputs and the failure taxonomy slide one click away as fallback.
# Decision rules

# Evidence to save after prep

- Check date and official source URLs
- Python + package versions
- Model ID used
- Local test result
- Live smoke result or reason skipped
- Known provider/SDK risks
- Confirmation that no secrets appear in materials

| Condition | Action |
| --- | --- |
| SDK minor release changed but APIs still pass smoke tests | Update Source Notes check date; no class-time explanation needed. |
| Structured-output helper changed | Update demo code and deck together; rerun local tests + one live structured call. |
| Prepared model unavailable | Select a compatible model from official docs; update OPENAI_MODEL only if code is otherwise compatible. |
| Live API unavailable | Use local contract + captured outputs; teach the boundary without provider dependence. |
| Any credential exposed | Stop, rotate/revoke credential, sanitize artifacts, then continue. |
| Deck code differs from repo | Block delivery until corrected; screenshot/code drift teaches the wrong contract. |
