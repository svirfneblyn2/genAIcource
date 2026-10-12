# 1-Page Speaker Cheatsheet • Lesson 04 (27 Slides • 90 Minutes)
*Speaker: Igor Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: Image Generation — Services, Prompt Techniques, and Control Patterns*  
*Presentation: `presentation_L04_Image_Generation_Services_and_Prompts_EN_v2.html` (PDF: `presentation_L04_Image_Generation_Services_and_Prompts_EN_v2.pdf`)*  
*Models (October 2026): Nano Banana 2 / Pro (`gemini-3.1-flash-image`, `gemini-3-pro-image`), GPT Image 2 / 2.5 (ChatGPT Images), Midjourney V8.2, FLUX.2, Leonardo.ai, Kling IMAGE 3.0*  
*Colab: `notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb` • Homework: `L04_05_Homework_EN.md` • Live Demo Copybook: `L04_04_Live_Demo_Runbook_READY_EN.md`*

---

### Part 1: Hook, Market Map & Prompting (00:00 — 47:00)

* **Slide 01 (00–02 min) • Cover:** Opening Module 2 (Multimodality). Practical craft, how the tools are built, and controllable results. All slide images are real generations without retouching; interface panels are schematics, not screenshots.
* **Slide 02 (02–05 min) • Hook Quiz (6 Portraits):** Portraits [A]–[F]. Chat question: *"Which are real humans, and which are AI generated?"*. Give 30–45 seconds. Ears in B, plastic skin in C, rim light in D, wrinkles in E, date stamp in F.
* **Slide 03 (05–07 min) • The Reveal 2014–2025:** All 6 are AI — reconstructions of each era's style, all generated in 2026. GAN 2014 (64×64) ➔ StyleGAN 2018 ➔ SD 1.5 2022 ➔ MJ v5 2023 ➔ FLUX.1 2024 ➔ Nano Banana Pro 2025. Indistinguishable by eye — but SynthID can tell. The 2026 challenge is **controllability**.
* **Slide 04 (07–09 min) • Course Roadmap:** Module 1 (L01–L03) completed. L04 Images, L05 Video, L06 Audio. Prompting fundamentals from L02 transfer; reference images replace text few-shots.
* **Slide 05 (09–12 min) • Three Layers of the Ecosystem:** Layer 1 — foundation models & APIs (OpenAI, Google, BFL, Stability, ByteDance) ➔ Layer 2 — creative studios (Leonardo and Kling run their own models + third-party; Krea, Sintx aggregate; Midjourney: own model, no API) ➔ Layer 3 — multimodal chat (ChatGPT, Gemini, Grok). Model ≠ service.
* **Slide 06 (12–16 min) • How Models Draw:** Diffusion (from noise in 20–50 steps; seed / guidance / negative prompt) vs autoregression (patch by patch, like text; strong at text and edits). GPT Image / Nano Banana architectures are not fully disclosed; many are hybrids.
* **Slide 07 (16–19 min) • Layer 1: Foundation Providers & APIs:** Nano Banana 2 / Pro / 2 Lite (`gemini-3.1-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-lite-image`), GPT Image 2 / 2.5 (`gpt-image-2`, `gpt-image-2.5-flare` / `-sunburst`), FLUX.2 → FLUX 3, Stability SD 3.5, Midjourney V8.2 + Edit Model (no API). ≈ $0.02–0.06 per 1K image on fast models.
* **Slide 08 (19–22 min) • Market, October 2026:** Table: GPT Image 2/2.5, Nano Banana 2/Pro, Grok Imagine 2.0, Midjourney V8.2, FLUX.2/3, Kling IMAGE 3.0, Seedream 5, Ideogram 4 (JSON prompts), Recraft V4 (SVG). Arena 08.2026: GPT-Image-2 #1, Grok 2.0 #2.
* **Slide 09 (22–25 min) • Layer 2: Why a Creative Studio:** Own + third-party models (FLUX, GPT Image, Nano Banana, SDXL) in one subscription, canvas, brush masks (inpainting), outpainting, LoRAs, guidance / seed. The left panel is an interface schematic, not a screenshot.
* **Slide 10 (25–28 min) • Canvas vs Editing in Words:** One task (mug ➔ iced latte). Studio: mask + area prompt + seed. Chat: "replace only the mug" — the model finds the object itself (edit by instruction).
* **Slide 11 (28–31 min) • Selection Matrix:** Entry barrier, targeted edits, text, consistency, 500+ batch. Per image: Nano Banana 2 Lite ≈ $0.034, legacy Nano Banana ≈ $0.039, Grok ≈ $0.02–0.06. Concepts/text ➔ chat; mask retouching ➔ studio; catalog ➔ API script (slide 24).
* **Slide 12 (31–34 min) • Freeform Prompt (`A1_free`):** "a cozy coffee shop in the morning" ➔ the model fills the gaps with averages: rain, patrons, a cat, a fireplace.
* **Slide 13 (34–39 min) • Six Slots (`A2_structured`):** Subject, Setting, Camera, Lighting, Style, Constraints; pins 1–4 on the frame. 35mm = natural, moderately wide angle. Negatives depend on the model: Gemini/GPT prefer positive phrasing ("empty coffee shop" instead of "no people"); `--no` / negative prompt are for MJ and SD/FLUX.
* **Slide 14 (39–43 min) • Details & Text (`A3_details`):** Must-have block + an honest acceptance checklist: ✅ text "FLAT WHITE 3.50 / OPEN 7:00", ✅ croissant, ⚠️ lavender on the right, not the left, ❌ extra text on the menu board. Failed ➔ targeted edit, not a reroll.
* **Slide 15 (43–47 min) • Photographer's Lexicon:** 85mm f/1.8 (portrait bokeh), top-down/flat lay, low-angle, golden hour. Aspect ratio via service parameter, not words.

---

### Lecture Equator: 5-Minute Break (47:00 — 52:00)

* **Slide 16 (47–52 min) • Coffee Break:** Click "START 5 MIN". "In Part 2 — targeted edits by instruction, the courier, and the product shoot." *(Pure rest, no chat tasks!)* Verify Leonardo/ChatGPT/Gemini tabs.

---

### Part 2: Control Patterns, Code, Risks & Homework (52:00 — 90:00)

* **Slide 17 (52–55 min) • The Edit Loop:** Draft ➔ select by must-haves ➔ one edit ("only X") ➔ check "what drifted?" ➔ finalize. After ~5–8 edits drift becomes visible — fresh chat from the best frame.
* **Slide 18 (55–60 min) • Pattern 1: Edit by Instruction (`B1`, `B2`, `E2`):** From `A2`: `B1` mug ➔ iced latte; `B2` light ➔ rainy evening; `E2` style ➔ vector. No mask needed in ChatGPT/Gemini/Kling; inpainting (hand-painted mask) is the Leonardo way.
* **Slide 19 (60–64 min) • Pattern 2: Courier Master Sheet (`C1_sheet`):** 4 angles on grey, 5 locked anchors, runnable prompt. In Midjourney references go through the Edit Model (up to 4; replaced `--cref`/`--oref` in 08.2026).
* **Slide 20 (64–67 min) • Pattern 2B: A Real Person as Reference:** 2–3 photos + "do not beautify" ➔ 4-angle sheet. The face is recognizable, but small features can drift — check by eye. Own photos or with consent only.
* **Slide 21 (67–71 min) • Courier in Scenes & Bridge to Video:** `C2` rain 16:9, `C3` door, `C4` bench. Frame `C2` becomes the First Frame (t₀) in Kling 3.0 / Veo 3.1: face and outfit noticeably more stable than from scratch; still check frames for drift.
* **Slide 22 (71–74 min) • Pattern 3: Product Photoshoot (`D0`–`D4`):** Packshot ➔ lifestyle, flat lay, in hands, banner. Reference `D0` + "do not change the shape" keep the mug noticeably more stable; a human signs off.
* **Slide 23 (74–77 min) • Pattern 4: Multi-Reference Composition (`E1`):** "Combine these" creates mush. Image 1 = hero, Image 2 = mug.
* **Slide 24 (77–80 min) • Batch Generation via SDK:** Same `google-genai` SDK, loop over a CSV; take the part with `inline_data` (loop over `parts`, not `parts[0]`). Estimate: ~50 cards in ~10 minutes for ~$2–3.
* **Slide 25 (80–84 min) • Risks & Blast Radius:** Hands and small text; drift after ~5–8 edits; US: Thaler (Supreme Court declined to hear it on 02.03.2026), Disney/Universal v. Midjourney; SynthID (Google, OpenAI since 05.2026) + C2PA. Traffic light: green / yellow / red zones.
* **Slide 26 (84–87 min) • Homework Assignment #4:** Track A — product photoshoot (4 shots); Track B — Glovo courier (sheet + 3 scenes + 1 edit by instruction). Compare 1 prompt across 2 tools ➔ `genai-homeworks/L04/` (`prompts.md`, `qa.md`). Invite: `ihar_rubanovich@epam.com`.
* **Slide 27 (87–90 min) • Summary & Lesson 05 (Video) Teaser:** 4 engineering principles. Today's courier frames become the first frames for Kling and Veo — our courier will start riding! Q&A.

---
**Pre-flight Checklist:** Log in to Leonardo.ai, ChatGPT, and Google AI Studio / Gemini • open `L04_04_Live_Demo_Runbook_READY_EN.md` (for instant prompt copy-pasting) • open presentation in fullscreen (F) • countdown timer ready on Slide 16.
