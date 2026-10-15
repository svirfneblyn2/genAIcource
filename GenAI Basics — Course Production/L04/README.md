# Lesson 04: Image Generation — Services, Prompt Techniques and Control Patterns

## Status: DONE — deck v2 (27 slides, facts as of October 2026), 2026-10-12

## Overview
Practical lesson on AI image generation for engineers. Begins with an interactive historical hook ("Real Human vs AI?", a reconstruction of each era's style 2014–2025), explains the ecosystem in 3 layers (Layer 1 foundation models & APIs, Layer 2 creative studios such as Leonardo.ai and Kling, Layer 3 multimodal chat such as ChatGPT, Gemini / Nano Banana and Grok), shows how models draw (diffusion vs autoregression) and the October 2026 market, contrasts canvas editing with editing by instruction, covers the 6-slot prompt, must-have acceptance checklists and photographer's vocabulary, and demonstrates four control patterns: targeted edits ("change only X"), a consistent character (Glovo delivery courier case study, incl. a real person as reference), product photoshoot, and multi-reference composition. Ends with batch generation via the `google-genai` SDK, risks (copyright, SynthID / C2PA) and a teaser for L05 (video).

## Source of Truth
- **Slide decks (27 slides, RU/EN):** `presentation_L04_Image_Generation_Services_and_Prompts_v2.html` / `_EN_v2.html` + PDFs with the same basenames (`_v2.pdf`, `_EN_v2.pdf`). Self-contained HTML (inline CSS/JS, speaker notes on `N`, slide grid on `G`, break timer on slide 16). Fix list: `L04_09_Deck_Fix_Plan_v2.md`; fact source: `L04_08_Source_Notes_Research_2026-10.md`.
- The v1 decks (25 slides, outdated model names) were removed on 2026-10-15; they are in git history (tag `archive/pre-cleanup-2026-10-15`). `deck/*.py` is stale (2026-10-02) and does not reproduce either version — edit the v2 HTML directly.
- **Visual Assets:**
  - `assets/hook/`: 6 portraits in the style of each era (GAN 2014, StyleGAN 2018, Stable Diffusion 2022, Midjourney v5 2023, FLUX.1 2024, Nano Banana Pro 2025), all generated in 2026.
  - `assets/examples/web/*.jpg`: control-pattern generations (A–E series, V1–V6 lexicon, `denoise_0–3` diffusion steps, reference photos).
  - `assets/v2/ar_0–3.jpg`: autoregressive patch-by-patch schematic (built with PIL from `denoise_3.jpg`) for slide 06.
  - Ecosystem diagram (slide 05), studio / chat workflow schematics (slides 09–10) are HTML/CSS inside the deck, labeled as schematics.
  - `assets/ui/chatgpt_logo.jpg` is still read by `deck/slides_v3.py`; the other v1-only UI mock-ups and diagrams were removed on 2026-10-15.
- **Colab:** `notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb` ([open in Colab](https://colab.research.google.com/github/svirfneblyn2/genAIcource/blob/main/notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb)); copy in this folder. Model: `gemini-3.1-flash-image` (Nano Banana 2). Steps 1–6 = lesson patterns, Step 7 = prompt template, Step 8 = homework export (`prompts.md` + images zip).
- **Instructor materials:** `L04_00_Lecture_Cheatsheet.md` / `_EN.md` (1-page speaker reference, v2 numbering), `L04_02_Instructor_Script_90MIN.md` / `_EN.md` (90-minute script, aligned to the v2 deck: 27 slides, v2 numbering and October 2026 facts).
- **Homework:** `L04_05_Homework.md` / `_EN.md` — Track A (product photo shoot) or Track B (Glovo courier character, L01 benchmark), comparing a creative studio (Leonardo.ai) with a multimodal chat (ChatGPT / Gemini).

## Slide map (27 slides, 90 minutes)
| # | Part | Topic |
|---|---|---|
| 01 | Cover | Title, subtitle, navigation keys |
| 02 | Interactive hook | "Real human vs AI?" — 6 portraits |
| 03 | Hook reveal | All 6 are AI — style reconstruction 2014–2025; SynthID can tell |
| 04 | Roadmap | Module 2: L04 images, L05 video, L06 audio |
| 05 | Ecosystem | 3 layers (HTML diagram): foundation models & APIs → creative studios → multimodal chat |
| 06 | How models draw (new) | Diffusion (denoising) vs autoregression (patch tokens) |
| 07 | Layer 1 providers | Nano Banana 2 / Pro / 2 Lite, GPT Image 2 / 2.5, FLUX.2 → FLUX 3, SD 3.5, Midjourney V8.2 + Edit Model |
| 08 | Market Oct 2026 (new) | GPT Image, Nano Banana, Grok Imagine 2.0, MJ V8.2, FLUX.2/3, Kling IMAGE 3.0, Seedream 5, Ideogram 4, Recraft V4; Arena ranks |
| 09 | Layer 2 creative studios | Own + third-party models, canvas, masks, presets (interface schematic) |
| 10 | Canvas vs chat | Same edit (mug → iced latte) as a mask workflow vs a dialogue (schematics with frames A2 → B1) |
| 11 | Selection matrix | Studio vs chat vs API, per-model prices |
| 12 | Free prompt | `A1_free` — the model fills the gaps |
| 13 | Six slots | `A2_structured`; positive phrasing for Gemini/GPT vs `--no` / negative prompt |
| 14 | Must-have details | `A3_details` + honest acceptance checklist |
| 15 | Photographer's vocabulary | 6 lens/light terms |
| 16 | Break | 5-minute timer |
| 17 | Edit loop | One change per step; drift visible after ~5–8 edits |
| 18 | Pattern 1 | Edit by instruction (B1, B2, E2); inpainting = mask in Leonardo |
| 19 | Pattern 2 | Courier character sheet `C1`; Midjourney via Edit Model |
| 20 | Pattern 2B | A real person as reference (2–3 photos → sheet) |
| 21 | Scenes & video bridge | `C2`–`C4`; `C2` as first frame (t₀) for Kling / Veo |
| 22 | Pattern 3 | Product photoshoot `D0` → `D1`–`D4` |
| 23 | Pattern 4 | Multi-reference composition `E1` |
| 24 | Code | Batch generation with `google-genai` (loop over `parts`, `inline_data`); ~50 cards in ~10 min for ~$2–3 |
| 25 | Risks & blast radius | Drift, Thaler (02.03.2026), Disney/Universal v. Midjourney, SynthID + C2PA |
| 26 | Homework | Track A / Track B, submission structure |
| 27 | Summary & L05 teaser | 4 rules; L05 = video generation (Kling, Veo, Runway) |

## Production Package (cleaned 2026-10-11, deck v2 added 2026-10-12)
The folder contains the canonical deliverables: v2 HTML decks and PDFs (RU/EN), 90-minute scripts, speaker cheatsheets, live demo prompt copybooks, homework guides, research notes, the fix plan and the Colab notebook.
