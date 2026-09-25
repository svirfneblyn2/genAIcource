# Lecture 03 demo — LLM API with Python

Prepared for GenAI Basics, refreshed 2026-09-14.

## What this repo demonstrates
1. Preflight without a network call.
2. A minimal Responses API request.
3. Streaming `response.output_text.delta` events.
4. Pydantic structured output with `responses.parse` and `output_parsed`.
5. Request IDs, usage, timeout and typed error handling.
6. A local contract test that works without an API key.

## Setup
Requires Python 3.10+.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
# edit .env and set OPENAI_API_KEY
```

Run `python 00_preflight.py` first. It performs no network request.
Run `python tests/test_contract.py` next. It validates the local schema only.
Then run the live scripts in numeric order.

## Model configuration
The prepared default is `gpt-5.6-terra` because, when checked on 2026-09-14, its official model page lists Responses API, streaming, and structured outputs as supported. Do not hard-code a model assumption into application logic: override `OPENAI_MODEL` in `.env` if your account or delivery environment needs another compatible model.

## Reset / fallback
Delete `.env` and recreate it from `.env.example` to reset local config. If the live API is unavailable, teach from `05_local_validation.py`, `expected_structured_output.json`, and the runbook’s expected-output path. Never paste a real API key into slides, chat, or source control.
