# Lesson 03: LLM API with Python: Streaming and Structured Output

## Status: DONE

## Overview
Hands-on engineering lecture and live workshop on integrating frontier LLMs using modern Python SDKs. Focuses on streaming responses, strict JSON Schema / Pydantic structured output, observability, error handling, and local integration testing.

## Canonical Cloud Links
- **Slide Deck (Google Slides / PPTX):** [L03 Slide Deck READY](https://docs.google.com/presentation/d/18INIziBaeZ9mhUW_29eqT6Dx7GpAZ1Ak/edit)
- **Full Instructor Script (Google Docs):** [Full Instructor Script READY](https://docs.google.com/document/d/1Cp8WTCnvP-dGaHl1fbjS43ip2wsbtOf4/edit)

## Production Deliverables
- `L03_01_Lecture_Text_READY.docx` — Complete lecture narrative and theory
- `L03_02_Full_Instructor_Script_READY.docx` — Word-by-word instructor delivery script
- `L03_03_Slide_Deck_READY.pptx` — 16:9 Presentation slide deck
- `L03_04_Live_Demo_Runbook_READY.docx` — Live demo step-by-step instructions
- `L03_05_Workshop_and_Homework_READY.docx` — Practical exercises and student assignment
- `L03_06_Agent_Runbook_READY.docx` — Automated generation and execution guide
- `L03_07_QA_Review_Report_READY.docx` — QA audit and verification report
- `L03_08_Source_Notes_READY.docx` — Source references and citations
- `L03_09_Demo_Repo_READY.zip` — Packaged live code demo
- `demo_repo/` — Unpacked runnable Python demo suite:
  - `00_preflight.py` — Environment and API key verification
  - `01_first_call.py` — Baseline non-streaming chat completion
  - `02_stream.py` — Token streaming with latency / TTFT tracking
  - `03_structured.py` — Pydantic typed schema enforcement
  - `04_observability.py` — Request/response logging and usage tracking
  - `05_local_validation.py` — Local validation without burning cloud credits
  - `contracts.py` — Data models and validation schemas
  - `tests/test_contract.py` — Unit test suite
