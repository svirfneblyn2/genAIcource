# Lesson 03: LLM API with Python

## Status: READY (facts checked 2026-10-02)

## Overview
Hands-on lesson on calling an LLM from code with Google's official `google-genai` SDK in Google Colab: the first call and its token receipt, generation settings (`temperature`, `max_output_tokens`, `thinking_level`), errors and a reliable client (timeout + retries), API-key hygiene, streaming (TTFT), structured output via `response_schema` + Pydantic, then prompt patterns in code (Few-Shot, Chain-of-Thought, XML delimiters against prompt injection) checked by code, and a real YouTube creator's assistant case with a cost estimate.

## Source of Truth
- **Colab notebook:** `notebooks/L03_First_API_Call_and_Prompt_Patterns.ipynb` ([open in Colab](https://colab.research.google.com/github/svirfneblyn2/genAIcource/blob/main/notebooks/L03_First_API_Call_and_Prompt_Patterns.ipynb)); copy in this folder. Part A = Steps 0–1.4, Part B = Steps 2–4, Part C = Steps 5.1–5.2, Step 6 (your turn), Step 7 (`result.json` for homework). Split versions: `L03_Part1_First_API_Call.ipynb` (Part A), `L03_Part2_Prompt_Patterns_in_Code.ipynb` (Parts B + C). Model: `gemini-3.5-flash-lite`.
- **Slide decks (25 slides, RU/EN):** `presentation_L03_LLM_API.html` / `presentation_L03_LLM_API_EN.html` + PDFs. All diagrams are native HTML (no raster images except `assets/streaming_vs_blocking_timeline.png` and `assets/structured_outputs_mechanics.png`). Keys: ←/→, N — speaker notes, G — grid, `#N` in the URL opens slide N.
- **Lecture text (slide-by-slide speech):** `L03_01_Lecture_Text_READY.md` / `L03_01_Lecture_Text_READY_EN.md`.
- **Instructor script (timing, live-demo checklist, actions):** `L03_02_Full_Instructor_Script_READY.md` / `L03_02_Full_Instructor_Script_READY_EN.md`.
- **One-page cheatsheet:** `L03_00_Lecture_Cheatsheet.md` / `L03_00_Lecture_Cheatsheet_EN.md`.

## Volatile facts (re-check before each delivery)
Checked against official docs on 2026-10-02:

| Fact | Value used | Source |
|---|---|---|
| Lesson model | `gemini-3.5-flash-lite` (stable), $0.30 / $2.50 per 1M in/out, thinking billed as output, free tier | ai.google.dev/gemini-api/docs/pricing |
| Thinking levels | Flash-Lite: minimal/low/medium/high; `gemini-3.8-flash`: low/medium/high only | ai.google.dev/gemini-api/docs/thinking |
| SDK | `google-genai` 2.27.0; `HttpOptions.timeout` in ms; no retries unless `retry_options` | pypi.org/project/google-genai, github.com/googleapis/python-genai |
| `generate_content` | labeled legacy but fully supported; new features ship in the Interactions API | ai.google.dev/gemini-api/docs/interactions |
| Invalid key | docs: `401`; in practice often `400 API_KEY_INVALID` — slides say `400/401` | ai.google.dev/gemini-api/docs/api-errors |
| OpenAI | Responses API; GPT-6 (`gpt-6-luna` $0.10/$0.50, `gpt-6-astra` $10/$50); timeout in seconds, 2 retries by default | developers.openai.com/api/docs/models |
| Anthropic | Claude 5.5 (`claude-sonnet-5-5` $2/$10, `claude-opus-5-5` $4/$20); adaptive thinking + `effort` | platform.claude.com/docs |
| Open models | DeepSeek-V4, OpenAI-compatible `base_url=https://api.deepseek.com` | api-docs.deepseek.com |

Free-tier rate limits are not published in the docs; AI Studio → Rate Limit (aistudio.google.com/rate-limit) showed on 2026-10-02: `gemini-3.5-flash-lite` 15 RPM / 250K TPM / 500 RPD, `gemini-3.8-flash` 5 RPM / 20 RPD. A full notebook run is ≈ 25 requests — run cells one by one in the demo; "Run all" exceeds 15 RPM and returns `429 RESOURCE_EXHAUSTED` from Step 4 on.

## Slide map
| # | Part | Slides |
|---|---|---|
| 1–2 | Intro | title, course roadmap |
| 3–5 | How an LLM API works | architecture, HTTP request anatomy, why an SDK |
| 6–10 | Part A | first call (Steps 0–1), response object, generation settings (1.1), errors and reliable client (0, 1.4), key security |
| 11–14 | Part A | streaming physics, streaming in code (1.2), constrained decoding, email ➔ JSON (1.3); then live run of Part A |
| 15 | Break | 5-minute timer |
| 16–18 | Part B | Zero-Shot vs Few-Shot (2), Chain-of-Thought (3), XML delimiters (4) |
| 19–20 | Part C | YouTube publishing package (5.1), comment triage + cost (5.2) |
| 21–25 | Wrap-up | library landscape, providers (Oct 2026), checklist, homework (1.3, 6, 7), Q&A |
