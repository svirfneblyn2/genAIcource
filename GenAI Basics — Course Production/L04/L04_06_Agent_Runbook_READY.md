Lecture 04 — Agent Preparation Runbook

Pre-class source, demo, asset and visual verification


# Source/freshness gate

- Re-check OpenAI model catalog for the current image model name and image-generation/editing guidance.
- Re-check Google Gemini image-generation docs for the current recommended model and code surface.
- Re-check Microsoft Foundry image-generation guidance; do not resurrect retired DALL-E 3 examples.
- Re-check Adobe Firefly Image5 / Photoshop API v2 guidance if those provider examples remain in the deck.
- If any provider changes a model ID, update Source Notes, demo config and slide vendor map before class.
# Demo preparation

- Create a clean venv in L04_demo_repo and install requirements.
- Set GEMINI_API_KEY in a local shell/environment. Never write the real key into .env.example or screenshots.
- Run 00_smoke_check.py and then one 01_generate.py call if budget/access permits.
- Run 02_edit.py with the controlled prompt and verify input/output files are not corrupted.
- Keep prepared input_product.png and expected_edit_example.png as fallback evidence.
- Reset out/ before class so students can distinguish new outputs from prepared assets.
# Visual audit

- Render all slides at 16:9 and inspect every slide, not only the content-heavy ones.
- Block if any image is distorted, low-resolution, irrelevant, or contains accidental generated gibberish presented as factual UI.
- Block if diagrams are replaced by generic text cards where a flow or comparison teaches better.
- Check code at projector size; minimum body text must remain readable.
- Use provider-specific color cues only for sections that compare providers; keep the overall course shell coherent.
- Verify no internal QA labels, prompt fragments or source-citation tokens leak into student-facing slides.
# Student-safety / rights check

- No student or private person photos are required for the workshop.
- Use supplied demo product assets or user-owned/licensed references only.
- Do not teach identity preservation as a guarantee. Make output inspection mandatory.
- Do not ask students to bypass provider safety restrictions or provenance mechanisms.
# Completion rule

Module 04 may be marked DONE only after source freshness, content, code, timing, practice, artifact completeness, slide render, visual QA and an independent second-pass audit are all PASS. Any unresolved visual or API correctness issue returns the module to QA FIXES.

