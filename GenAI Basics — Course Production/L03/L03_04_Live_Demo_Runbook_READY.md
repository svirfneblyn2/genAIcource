# Lecture 03 — Live Demo Runbook

Exact setup, run order, teaching points and fallback path

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Demo objective

Show the same task evolve from a minimal text request into a streamed interaction, a typed structured result, and an observable production boundary. The demo is successful if students can explain the contract at each step; a live API response is optional evidence, not the lesson itself.

# Instructor workstation preparation

- Use Python 3.10+ in a clean virtual environment.
- Install `requirements.txt` before class. Prepared SDK range is openai>=3.13,<4, refreshed against PyPI on 2026-09-14.
- Copy .env.example to .env. Insert a teaching key locally. Confirm .env is ignored by Git.
- Keep OPENAI_MODEL configurable. Prepared default is gpt-5.6-terra; verify account access and feature support before class.
- Run `python 00_preflight.py` and `python tests/test_contract.py` before any live API call.
- Run each live script once before the lecture and capture expected output privately as fallback evidence.
- Close unrelated terminals, notifications and any file containing real credentials.
# Tabs / windows to prepare

# Run order

# Teaching script around the live calls

Before step 1 ask: “Where does the model run?” After step 1 ask: “Which three fields would help us investigate this call tomorrow?”

Before streaming ask: “What changes: compute, transport, or both?” After streaming ask: “Would you let a workflow trigger a side effect from a partial stream?”

Before structured output show the raw ticket and ask students to choose fields. After the clear ticket, switch the input to sample_ticket_ambiguous.txt and ask why review=true is a better contract than forced certainty.

# Failure and recovery policy

- Credential/model access failure: do not debug live for more than two minutes. Switch to expected outputs and keep teaching.
- Network interruption: explain APIConnectionError; do not repeatedly hammer the service.
- Rate limit: explain backoff/concurrency control; do not intentionally trigger rate limiting in class.
- Timeout: point to the explicit 20-second client timeout; explain that the value is a demo policy, not a universal recommendation.
- Structured-output mismatch or SDK behavior drift: use the official current structured-output example plus expected fixture; mark the demo for post-class refresh rather than improvising unsupported code.
# Reset path


Never include `.env`, shell history with keys, screenshots of credentials or provider dashboards with account identifiers in student materials.


| Window | Open |
| --- | --- |
| Editor 1 | README.md + .env.example + .gitignore |
| Editor 2 | 01_first_call.py → 02_stream.py → 03_structured.py → 04_observability.py |
| Editor 3 | contracts.py + sample_ticket.txt + sample_ticket_ambiguous.txt |
| Terminal | Activated venv at demo_repo root |
| Slides | Architecture, streaming, structured output, failure taxonomy, telemetry slides |


| Step | Command | Expected teaching point | Fallback |
| --- | --- | --- | --- |
| 0 Preflight | python 00_preflight.py | Environment/config visible; no network call. | Show prepared output. |
| Local contract | python tests/test_contract.py | Deterministic schema checks can run without a model. | This should always run; if dependencies missing, use captured PASS. |
| 1 First call | python 01_first_call.py | output_text + request ID + usage. | Show captured output; continue after 2-minute limit. |
| 2 Stream | python 02_stream.py | Text delta events arrive progressively. | Use slide event timeline or captured terminal GIF/screenshot. |
| 3 Structured | python 03_structured.py | Pydantic-typed output; output_parsed. | Use expected_structured_output.json and local validation. |
| 4 Observe | python 04_observability.py | Latency, usage, request ID + typed failure categories. | Explain from code; no forced production error required. |


| # reset local configuration rm -f .env cp .env.example .env  # deterministic check python tests/test_contract.py  # verify repository is clean git status --short |
| --- |
