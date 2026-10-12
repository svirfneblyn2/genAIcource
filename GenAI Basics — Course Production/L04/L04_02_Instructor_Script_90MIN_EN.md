# Instructor Script • Lesson 04: Image Generation — Services, Prompt Techniques, and Control Patterns (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 04 of 16  
**Instructor:** Igor Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems  
**Hands-on AI R&D:** Creator and architect of Creator Tools — a suite of AI tools for YouTube creators designed to save production time, streamline content workflows, and increase earnings (Hands-on AI R&D pet-project)  
**Target Audience:** Software developers, QA engineers, DevOps, tech leads, architects  
**Format:** 27 slides (`presentation_L04_Image_Generation_Services_and_Prompts_EN_v2.html` / `_EN_v2.pdf`) • Live demos in Leonardo.ai, ChatGPT Images, Google Gemini / AI Studio • 5-minute interactive break timer on Slide 16  
**Materials:** Prompts and raw assets — `examples/prompts.json` + `assets/examples/` • Colab Notebook — `notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb` • Homework Guide — `L04_05_Homework_EN.md` • Facts — `L04_08_Source_Notes_Research_2026-10.md` (state as of October 2026)  
**Slide Models:** Nano Banana 2 / Pro / 2 Lite (`gemini-3.1-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-lite-image`), GPT Image 2 / 2.5, FLUX.2 / FLUX 3, Midjourney V8.2 (+ Edit Model), Kling IMAGE 3.0, Grok Imagine 2.0, Leonardo.ai. Pattern examples (A–E series, V1–V6) are real generations without retouching. The hook portraits on Slides 02–03 are reconstructions of each era's style generated in 2026 (not historical model outputs). Slides 05, 09, and 10 are HTML schematics, not product screenshots.

**Lesson Goal:** The student understands the three layers of the image generation ecosystem (Layer 1 — foundation models & APIs, Layer 2 — creative studios like Leonardo and Kling, Layer 3 — multimodal chat); knows how diffusion differs from autoregression; contrasts canvas masking with edits by instruction in a chat; writes structured 6-slot prompts with a must-have block and accepts frames against a checklist; executes targeted edits by instruction; and maintains cross-scene character consistency (Glovo Courier benchmark) and product fidelity (master packshot).

---

## Lecture Timing & Session Map

| Slide | Block | Timestamp | Format | Demo / Focus | Core Principle |
|---|---|---|---|---|---|
| **01** | Cover | 00:00 — 02:00 | Intro | — | Opening Module 2. Practical engineering craft & controllability. |
| **02** | Hook Quiz | 02:00 — 04:00 | Interactive | Chat Poll (6 Portraits A–F) | Guess who is real and who is AI. Engaging the audience immediately. |
| **03** | Reveal & Evolution | 04:00 — 07:00 | Reconstruction | Era styles 2014–2025 (generated in 2026) | All 6 are AI! Indistinguishable by eye, SynthID can tell. The challenge is control. |
| **04** | Course Roadmap | 07:00 — 09:00 | Stepper | Skill Transfer from L02 | Prompt laws transfer; visual references replace text few-shots. |
| **05** | Three Ecosystem Layers | 09:00 — 12:00 | HTML diagram | Layer 1 ➔ Layer 2 ➔ Layer 3 | Model ≠ service. Foundation models & APIs ➔ creative studios ➔ multimodal chat. |
| **06** | How Models Draw *(new)* | 12:00 — 14:00 | Theory, no formulas | `denoise_0–3` vs patches | Diffusion: from noise, everywhere at once; autoregression: patch by patch, like text. |
| **07** | Layer 1 Providers | 14:00 — 17:00 | Cards | Google, OpenAI, BFL, Stability, MJ | Who trains weights and exposes APIs. Python SDK access like L03. |
| **08** | Market: October 2026 *(new)* | 17:00 — 20:00 | Handout table | 9 models, Arena 08.2026 | A market map, not a ranking: strength, references, price. |
| **09** | Layer 2 Creative Studios | 20:00 — 23:00 | Interface schematic | Leonardo, Kling, Krea, Sintx | Own + third-party models, canvas, masks, presets — a workflow. |
| **10** | Canvas vs. Words | 23:00 — 26:00 | Two schematics | Frames A2 ➔ B1 | Brush mask (inpainting) vs. edit by instruction in a chat. |
| **11** | Selection Matrix | 26:00 — 29:00 | Table | Studio / chat / API, per-model prices | Concepts ➔ Chat; hand mask ➔ Studio; 500+ batch ➔ API script. |
| **12** | Freeform Prompt | 29:00 — 32:00 | Image + Demo | `A1_free.jpg` | Model fills voids: rain, patrons, cat, fireplace, barista. |
| **13** | Six Slots | 32:00 — 37:00 | Prompt + frame | `A2_structured.jpg` | 6 slots. Positive phrasing for Gemini/GPT; `--no` for MJ/SD. |
| **14** | Must-Have & Acceptance | 37:00 — 41:00 | Checklist | `A3_details.jpg` | Quotes + `exactly`; accept against a ✅ ⚠️ ❌ checklist. |
| **15** | Photographer's Vocabulary | 41:00 — 44:00 | Cheatsheet | `V1`–`V6` | 85mm f/1.8, flat lay, low angle, golden hour. Aspect ratio via parameter. |
| **16** | **Equator: Break** | **44:00 — 49:00** | **5-Min Timer** | **Pure Rest** | **Zero chat chores. Complete attention recharge.** |
| **17** | The Edit Loop | 49:00 — 52:00 | 5-step loop | The Edit Loop | Avoid rerolls. One edit per step; drift visible after ~5–8 edits. |
| **18** | Pattern 1: Edit by Instruction | 52:00 — 57:00 | 4 Frames | `B1_replace`, `B2`, `E2` | Object ➔ latte, light ➔ rainy evening, style ➔ vector. Inpainting = mask. |
| **19** | Pattern 2: Courier Master Sheet | 57:00 — 61:00 | Sheet + prompt | `C1_sheet` | 4 angles + 5 textual anchors. Midjourney via Edit Model. |
| **20** | Pattern 2B: Real Person | 61:00 — 64:00 | References + prompt | 2–3 photos ➔ sheet | `do not beautify`; own photos or with consent only. |
| **21** | Scenes & Video Bridge | 64:00 — 68:00 | 3 scenes + pipeline | `C2`, `C3`, `C4` ➔ Kling / Veo | `C2` as first frame (t₀): noticeably more stable, still check drift. |
| **22** | Pattern 3: E-Commerce | 68:00 — 72:00 | Gallery | `D0_packshot` ➔ `D1`–`D4` | Packshot on white ➔ lifestyle, flat lay, in hands, banner. Human acceptance. |
| **23** | Pattern 4: Composition | 72:00 — 75:00 | Role Mapping | `E1_compose` | Explicit roles: Image 1 = hero, Image 2 = product. |
| **24** | Code & Automation | 75:00 — 79:00 | Python SDK | CSV loop, `parts` / `inline_data` | ~50 cards in ~10 min for ~$2–3. 10% API, 90% templating & QA. |
| **25** | Risks & Blast Radius | 79:00 — 84:00 | Traffic Light | Green / Yellow / Red Zones | Drift, Thaler (02.03.2026), Disney/Universal v. Midjourney, SynthID + C2PA. |
| **26** | Homework #4 | 84:00 — 87:00 | Two Tracks | Track A (Product) / Track B (Courier) | Submit to `genai-homeworks/L04/`. Compare 2 tools in `qa.md`. |
| **27** | Summary & L05 Teaser | 87:00 — 90:00 | Open Mic | Video Generation Teaser | 4 rules. Courier frames come alive in L05: Kling, Veo, Runway! |

**Time budget:** Part 1 (Slides 01–15) — 44 min • break (Slide 16) — 5 min • Part 2 (Slides 17–27) — 41 min • total 90 min. New Slides 06 and 08 take 2 and 3 minutes; the time came from the hook, roadmap, layers, and the studio/chat pair. If you run behind, trim Slide 08 (handout) and Slide 15 (cheatsheet), not the Part 2 patterns.

---

## Detailed Section-by-Section Script (Slides 01 — 27)

### Part 1: Interactive Hook, Ecosystem, How Models Draw & Prompting (00:00 — 44:00)

---

### Slide 01 (00:00 — 02:00) • Title Cover: Image Generation
**On Screen:** Cover title with a mosaic of lesson generations. Kicker: `GenAI Basics • Lesson 04 • Module 2: Multimodality`. Title: `Image Generation: Services, Prompt Techniques, and Control Patterns`. Subtitle: ChatGPT, Nano Banana, Leonardo.ai, Midjourney, Kling, and FLUX.

#### Speaker Script:
> "Hello everyone. Welcome to Lesson 04. Today, we officially open Module 2: Multimodality.
> 
> Throughout Module 1, we built a solid engineering foundation: BPE tokenization, temperature and decoding, and programmatic API pipelines. Today, we move from tokens to pixels. But let me be clear: this lecture is not about generating random digital art for fun. Our perspective is engineering: how models draw, who powers the ecosystem, why creative studios exist, and how to get controllable, repeatable results.
> 
> Every pattern example you will see in this deck is a real generation without manual Photoshop touch-ups. All prompts and parameters are published in our repository. Let's begin with a quick calibration of our visual instincts."

---

### Slide 02 (02:00 — 04:00) • Interactive Hook: Real Human or AI?
**On Screen:** A horizontal gallery of six portraits labeled [A] through [F]. Question: *"Guess: Which is a real human, and which is AI?"*. Chat poll prompt below.

#### Speaker Script:
> "Take a close look at these six portraits: A, B, C, D, E, and F.
> 
> Right now in the chat, post your hypotheses: which letters are real people captured through a camera lens, and which ones were generated by a neural network?
> 
> For instance, type: *'A and B are definitely AI, E and F are real people'* or *'Only F is an authentic photo'*. I will give you 30 to 45 seconds.
> 
> Inspect the details: skin microtexture, pupil symmetry, reflections in the eyes, hairline, background, ear anatomy, and jewelry. Keep your guesses coming... I see a wave of votes saying E and F are definitely real photographs, while A and B are obviously old AI. Let's test your intuition."

---

### Slide 03 (04:00 — 07:00) • The Reveal: A Decade of Evolution
**On Screen:** The same six portraits with year/architecture badges (2014 GAN ➔ 2018 StyleGAN ➔ 2022 SD 1.5 ➔ 2023 MJ v5 ➔ 2024 FLUX.1 ➔ 2025 Nano Banana Pro). Caption: "A reconstruction of each era's style (all frames generated in 2026)". Engineering takeaway banner.

#### Speaker Script:
> "The correct answer: **all six portraits are AI generated**. There is not a single real photograph on this screen.
> 
> An honest caveat: these are not archival outputs of old models. They are a **reconstruction of each era's style** — all six frames were generated in 2026 to show the signature look of each generation. Still, they show well how generative models crossed the uncanny valley in about a decade:
> - **2014 (Frame A):** The style of the first GANs from Ian Goodfellow's work. A blurry 64×64 grayscale blob — back then, a breakthrough.
> - **2018 (Frame B):** The NVIDIA StyleGAN look. Convincing at first glance, but the earlobe melts, the earring dissolves, and the background shows rainbow noise.
> - **2022 (Frame C):** The open-source diffusion explosion — Stable Diffusion 1.5. Correct proportions, but plastic skin and a glassy stare.
> - **2023 (Frame D):** The Midjourney v5 aesthetic. Cinematic rim light, tactile tweed, dramatic chiaroscuro.
> - **2024 (Frame E):** The FLUX.1 era from Black Forest Labs. Natural microtexture: pores, crow's feet, gray hair, uneven tan.
> - **2025 (Frame F):** Google's Nano Banana Pro. Smartphone optics, imperfect cafe light, bokeh, sensor grain, even a date stamp. **By eye you can no longer tell it from a real photo. But SynthID — an invisible watermark in the pixels — can tell;** we will come back to it in the risks block.
> 
> Our engineering takeaway? **Photorealistic 'beauty' now comes out of the box.** The problem of 2026 is not beauty — it is **controllability**: making the model deliver exactly what the spec says and repeat the same courier or product across ten scenes."

---

### Slide 04 (07:00 — 09:00) • Course Roadmap: Entering Multimodality
**On Screen:** 6-module stepper. Module 1 completed, Module 2 highlighted (L04 images, L05 video, L06 audio). Callout on transferring prompt laws from L02.

#### Speaker Script:
> "Let's review our roadmap. Module 1 (L01–L03) is done: tokens, prompts, and APIs are in your toolbelt. Today we enter Module 2: Lesson 04 on images, Lesson 05 on video, and Lesson 06 on speech and audio.
> 
> The good news: the prompt principles from Lesson 02 transfer to image models almost unchanged:
> - Specificity beats vague adjectives.
> - Splitting the task into slots prevents hallucinations.
> - Constraints must be stated explicitly.
> 
> The key shift: in text we gave few-shot examples as text; in image generation our 'examples' are **reference images**."

---

### Slide 05 (09:00 — 12:00) • Three Layers of the Image Generation Ecosystem
**On Screen:** HTML diagram, bottom to top: Layer 1 "Foundation Models & APIs" (OpenAI GPT Image 2 / 2.5, Google Nano Banana, BFL FLUX.2 / FLUX 3, Stability SD 3.5 / SDXL, ByteDance Seedream 5.0) ➔ Layer 2 "Creative Studios" (Leonardo.ai — own Phoenix / Lucid + third-party, Kling — own IMAGE 3.0 / O1, Midjourney — own V8.2 without API, Krea / Sintx — aggregators) ➔ Layer 3 "Multimodal Chat" (ChatGPT, Gemini, Grok). Legend: "service on its own models" vs "aggregator of third-party models". Banner: "Model ≠ service".

#### Speaker Script:
> "Let's clear up a common confusion. People say: *'I generate in Leonardo'*, *'I use Midjourney'*, *'I call the API'*. How do these fit together? The key message: **a model is not a service**. The same model lives in an API, in a creative studio, and in a chat.
> 
> The ecosystem has three layers — from here on we use only these terms:
> 
> 1. **Layer 1: Foundation Models & APIs.** Companies with huge GPU/TPU clusters that train the weights and expose REST / Python APIs: OpenAI (GPT Image 2 and 2.5), Google (the Nano Banana family via the Gemini API and Vertex), Black Forest Labs (FLUX.2 and the new FLUX 3), Stability AI (SD 3.5 / SDXL), ByteDance (Seedream 5.0).
> 
> 2. **Layer 2: Creative Studios.** Leonardo.ai, Kling, Krea, Sintx. Don't oversimplify: **Leonardo and Kling are not 'just proxies'**. Leonardo has its own Phoenix and Lucid models plus third-party ones; Kling has its own IMAGE 3.0 and O1 with a direct bridge to video. Krea and Sintx mostly aggregate other vendors' models. Midjourney is special: its own V8.2 model, but Web and Discord only, no public API. The studio value is the canvas, masks, layers, upscaling, and presets.
> 
> 3. **Layer 3: Multimodal Chat.** ChatGPT on GPT Image, Gemini on Nano Banana 2 / Pro, and Grok on its own Aurora model (Grok Imagine 2.0). The model reasons in text, draws, and remembers the dialogue — the best place for edits and in-image text.
> 
> Note the footnote: one vendor can sit on several layers. Google is both an API (Layer 1) and the Gemini chat (Layer 3).
> 
> Remember our 10/90 axiom: the model is only 10% of the system. The other 90% is the control interface, masking, session state, and workflow."

---

### Slide 06 (12:00 — 14:00) • Under the Hood: Diffusion vs. Autoregression *(new slide)*
**On Screen:** Two columns. Left, "Diffusion: from noise, everywhere at once" — four frames `denoise_0–3` (noise ➔ shapes ➔ details ➔ final), seed / guidance / steps / negative prompt; who: SD / SDXL, FLUX, Midjourney, most studio models. Right, "Autoregression: patch by patch, like text" — schematic `ar_0–3` (first patches ➔ 40% ➔ 70% ➔ done); who: GPT Image, Grok Aurora; Nano Banana — architecture not disclosed. "In practice" banner.

#### Speaker Script:
> "Two minutes of theory — no formulas, but it explains half of what we see next.
> 
> **On the left is diffusion.** The model starts from pure noise and removes it over 20–50 steps across the whole image at once: shapes first, then details. The prompt steers every step. Consequence: a different seed means different starting noise, which means a different image. That is why studios expose seed, guidance, steps, and negative prompt. This is how Stable Diffusion, FLUX, Midjourney, and most studio models work.
> 
> **On the right is autoregression.** The image is a sequence of patch tokens, and the model predicts the next patch like the next word in a sentence. The same multimodal LLM that reads your prompt does the drawing — that is why chat models follow instructions, edits, and in-image text so well. Per public information, GPT Image and Grok Aurora work this way.
> 
> Honest caveat: GPT Image and Nano Banana architectures are not fully disclosed, and many current models are hybrids. The right-hand visual is a schematic, not the real generation order of any specific model.
> 
> Practical takeaway at the bottom: with diffusion we work with sliders and seed; with chat models — a prompt as a spec and edits in words. All of today's techniques work for both."

---

### Slide 07 (14:00 — 17:00) • Layer 1: Foundation Providers & APIs
**On Screen:** Six cards: Google (Nano Banana 2 / Pro / 2 Lite), OpenAI (GPT Image 2 / 2.5), Black Forest Labs (FLUX.2 Pro / Flex / Dev ➔ FLUX 3), Stability AI (SD 3.5 / SDXL), Midjourney (V8.2 + Edit Model), and a "Programmatic Access" box with price and latency.

#### Speaker Script:
> "Let's examine the Layer 1 providers we call from code. Current line-ups as of October 2026:
> 
> - **Google — Nano Banana 2 / Pro / 2 Lite:** in code, `gemini-3.1-flash-image`, `gemini-3-pro-image`, and `gemini-3.1-flash-lite-image`. Same `google-genai` SDK as L03. Strengths: speed, world knowledge and Search grounding, multi-reference input.
> - **OpenAI — GPT Image 2 / 2.5:** `gpt-image-2`, the fast `gpt-image-2.5-flare`, and `gpt-image-2.5-sunburst` for precise edits. Strengths: in-image text, strict instruction following, conversational edits.
> - **Black Forest Labs — FLUX.2 (Pro / Flex / Dev) and FLUX 3:** APIs at BFL, Replicate, fal.ai. FLUX.2 Dev and Klein are open weights with up to 10 references; FLUX 3 shipped in July 2026 and is multimodal. Strengths: photorealism, exact hex colors, local hosting.
> - **Stability AI — SD 3.5 and SDXL:** the open-source backbone, thousands of community LoRAs. Weights can be self-hosted — we cover that in Lesson 10.
> - **Midjourney V8.2 + Edit Model:** a special case. Web and Discord only, no public REST API — you cannot wire it into an enterprise pipeline. Since August 2026, edits, inpaint / outpaint, and references (up to 4 images) go through the Edit Model.
> 
> In code: `POST /v1/images/generations` at OpenAI or `client.models.generate_content` at Google, requesting `IMAGE` in `response_modalities`. Indicative cost: about $0.02–0.06 per 1K image on fast models; Pro and 4K cost more. Latency: 3 to 15 seconds."

---

### Slide 08 (17:00 — 20:00) • The Image Generation Market: October 2026 *(new slide)*
**On Screen:** Handout table: model / vendor, strength, references, access & price — GPT Image 2 / 2.5, Nano Banana 2 / Pro / 2 Lite, Grok Imagine Image 2.0, Midjourney V8.2, FLUX.2 / FLUX 3, Kling IMAGE 3.0 / O1, Seedream 5.0, Ideogram 4.0, Recraft V4. Footnote: Arena, 08.2026 — GPT-Image-2 #1, Grok Imagine 2.0 #2; prices change monthly.

#### Speaker Script:
> "This is a handout map of the market as of October 2026. It is **not a 'best model' ranking**. Read it by column: what each model is for and how many references it accepts.
> 
> - **GPT Image 2 / 2.5 and Nano Banana 2 / Pro** are all-rounders: in-image text, infographics, conversational edits. Nano Banana 2 takes up to 14 objects and 5 characters as references, plus Search and 4K.
> - **Grok Imagine 2.0** is not 'a chat on someone else's engine' — it is its own model, with Magic Wand selection and templates.
> - **Midjourney V8.2** is aesthetics and style (`--sref`, moodboards), but no API; references go through the Edit Model, up to 4.
> - **FLUX and Ideogram** ship open weights; Ideogram 4 also has official JSON prompts.
> - **Recraft V4** is the one with native editable SVG.
> - **Kling IMAGE 3.0** if you need video next; **Seedream 5.0** for 4K and splitting a render into PNG layers.
> 
> Footnote: on the Arena in August 2026, GPT-Image-2 is #1 and Grok Imagine 2.0 is #2, for both generation and editing. Reference counts depend on the surface (app vs API), and prices change monthly — I re-check them before every class, and so should you."

---

### Slide 09 (20:00 — 23:00) • Layer 2: Creative Studios
**On Screen:** Interface schematic of a creative studio (generic, not a screenshot): model picker on the left (Phoenix — the studio's own model; FLUX.2 Pro, GPT Image 2, Nano Banana 2 — via API; SDXL + LoRA — open weights), canvas with a mask over the mug and "Mask brush / Outpaint / Layers" tools in the middle, parameters (Guidance, Steps, Seed 🔒, Style, Negative) on the right. Benefits list and studio definition.

#### Speaker Script:
> "A fair question: if API generation costs a few cents, why do designers and marketers pay $20 to $50 a month for Leonardo.ai or Kling?
> 
> First, about the picture: it is a **schematic**, not a screenshot of a real product — this is what a typical creative studio looks like. The answer is the workflow:
> 1. **Own + third-party models:** Leonardo (Phoenix, Lucid) and Kling (IMAGE 3.0) run their own models, with FLUX, GPT Image, Nano Banana, and SDXL in the same menu. One subscription instead of five API keys. Midjourney cannot be officially plugged into such aggregators — it has no public API.
> 2. **Canvas:** lay out frames, work in layers, extend the frame (outpainting).
> 3. **Brush mask (inpainting):** a deformed finger or extra button? No paragraphs of text — paint a mask over it and regenerate only that area.
> 4. **Presets & LoRAs:** a brand style or a 'product shoot' in one click.
> 5. **Diffusion knobs:** guidance, seed, ControlNet by pose or edges — the ones from Slide 06.
> 
> The definition at the bottom: a creative studio is a visual shell over models, its own and third-party, that turns generation into a workflow."

---

### Slide 10 (23:00 — 26:00) • Canvas & Sliders vs. Editing in Words
**On Screen:** One task — swap the mug for an iced latte — in two schematics. Left: creative studio schematic (e.g. Leonardo): frame A2 ➔ brush mask, prompt for the area, negative prompt, seed 🔒 ➔ frame B1. Right: ChatGPT / Gemini dialogue schematic: "Replace only the mug with a tall glass of iced latte. Keep the light, counter and background." ➔ "Done" with frame B1.

#### Speaker Script:
> "Let's compare two paradigms on one task. Both panels are workflow schematics; frames A2 and B1 inside them are our real generations from this lesson.
> 
> **On the left — a creative studio.** The graphics-editor paradigm. You drive the process: paint a mask over the mug — that is inpainting — write a prompt for that area only, lock seed and guidance. Pixel-level control at the cost of manual work.
> 
> **On the right — a chat model, talking to a director.** You attach the frame and write: *'Replace only the mug with a tall glass of iced latte. Keep the light, counter and background.'* No mask needed: the model finds the object from the description. This is called **edit by instruction**. Fast, but precision depends on your wording — and on checking the result.
> 
> Rule of thumb: pixel-level control and a hand-drawn mask — studio. Fast semantic object swaps and text work — chat model.
> 
> *(Optional speaker demo: show Leonardo.ai with a mask and the Guidance slider, and the Gemini window with Nano Banana 2.)*"

---

### Slide 11 (26:00 — 29:00) • Selection Matrix: Studio vs. Chat vs. API
**On Screen:** Matrix comparing creative studio (Leonardo, Krea), multimodal chat (ChatGPT, Gemini), and API (Python SDK / Vertex / fal) across entry barrier, targeted edits, in-image text, character consistency, and batch generation (with per-model prices). Engineering rule at the bottom.

#### Speaker Script:
> "Keep this handout for architecture decisions:
> 
> - For **concept art, posters with text, or quick brainstorming**, choose **multimodal chat (ChatGPT / Gemini)**: minimal barrier, edits by instruction, excellent text with GPT Image 2.x and Nano Banana.
> - For **commercial art with pixel-level fixes and a hand mask**, choose a **creative studio (Leonardo.ai / Krea)**: character reference, seed lock, brush, layers.
> - For **500+ catalog banners**, never click buttons in a browser. Write a Python script against the **API** — we will see it on Slide 24.
> 
> Look at the last row: Nano Banana 2 Lite ≈ $0.034 per 1K image, legacy Nano Banana ≈ $0.039, Grok ≈ $0.02–0.06. Indicative as of October 2026; prices differ several-fold between models. Prototype in the chat, fix details with a mask in a studio, ship with a script."

---

### Slide 12 (29:00 — 32:00) • Freeform Prompt: The Model Fills the Gaps
**On Screen:** Generation `A1_free.jpg` with numbered callouts 1–5 (rain, patrons, cat, fireplace, barista). Prompt: `"a cozy coffee shop in the morning"`.

#### Speaker Script:
> "Now let's examine prompt mechanics.
> 
> Here is a 6-word prompt: *'a cozy coffee shop in the morning'*. The result looks charming.
> 
> But let's audit it against the spec: outside, it is raining — despite asking for morning. The cafe has strangers in it. A cat sleeps on the windowsill. A fireplace burns in the corner. A barista works behind the counter. **None of these were requested.**
> 
> The model cannot leave blank space. Whatever you don't decide, it fills with averages from its training data. In production, that randomness is a bug."

---

### Slide 13 (32:00 — 37:00) • Six Slots: What Controls What
**On Screen:** Left: runnable slot prompt (copy & run) with a "high scene control" badge, a "Negatives depend on the model" callout, and the hint "Instead of cozy, 4k, masterpiece — physical details". Right: frame `A2_structured.jpg` with pins 1–4 (subject, setting, camera: soft blur, light from left) and the 6-slot breakdown (`Subject`, `Setting`, `Camera`, `Lighting`, `Style`, `Constraints`).

#### Speaker Script:
> "Here is the engineering version of the same task. We decompose the frame into six slots — and the pins on the frame show where each one worked:
> 1. **Subject:** semantic anchor, texture, rule of thirds — `speckled cream ceramic mug of black coffee with steam, on worn oak counter in right third`.
> 2. **Setting:** time and geometry — `empty Scandinavian coffee shop at 7 a.m., chairs up on tables, brass espresso machine on left`. '7 a.m., chairs up' removes random people — and note we said it positively: `empty`.
> 3. **Camera:** `eye-level, 35mm lens, f/2.0, shallow depth of field`. 35mm is a natural, moderately wide angle; f/2.0 gives soft bokeh.
> 4. **Lighting:** `low warm morning sunlight from left window, long soft shadows` — volume and long shadows.
> 5. **Style:** `realistic editorial photography` — editorial photo instead of a glossy 3D render.
> 6. **Constraints:** `no text, no logos` — what to exclude.
> 
> A 2026 nuance — the 'Negatives depend on the model' callout. Google explicitly recommends positive phrasing for Gemini, and GPT Image behaves the same: `empty coffee shop` instead of `no people`, `empty street` instead of `no cars`. Negations via `--no` and negative prompts are a Midjourney and SD / FLUX studio tool.
> 
> Three typical beginner mistakes: adjectives instead of details ('cozy' — and you get a fireplace and a cat); filler tags like `4k, masterpiece, trending`, which are noise; and forgotten constraints. This is high scene control, not a guarantee — the final word is always the check."

---

### Slide 14 (37:00 — 41:00) • Critical Details & Text: Must-Have Block and Acceptance Checklist
**On Screen:** Frame `A3_details.jpg` (chalkboard, croissant, lavender). Must-Have block (text `exactly "FLAT WHITE 3.50"` and `"OPEN 7:00"`, one croissant behind the mug, lavender vase to the left, no other text) and "Acceptance checklist for frame A3": ✅ text without typos, ✅ one croissant behind the mug, ⚠️ lavender is there but on the right, ❌ extra text — menu board at the top.

#### Speaker Script:
> "When a scene needs exact text and key props, isolate them into a **Must-Have block**:
> - Wrap text in quotes with the word `exactly`: *'FLAT WHITE 3.50'* and *'OPEN 7:00'*.
> - Quantities as numbers: `one fresh croissant`, not `croissants`.
> - Positions stated explicitly: `behind the mug`, `to the left of the mug`.
> - And add `no other text`.
> 
> Most importantly, we check the frame **against a checklist, not 'by eye'**. Honestly, for A3:
> - ✅ The text is rendered without typos — a strength of current models like GPT Image 2.x and Nano Banana.
> - ✅ One croissant, behind the mug.
> - ⚠️ The lavender is there, but on the right, not the left.
> - ❌ A menu board with extra text appeared at the top, despite `no other text`.
> 
> This is normal. Must-have is an acceptance checklist; open items are fixed with a targeted edit — the topic of Part 2 — not by regenerating the whole frame."

---

### Slide 15 (41:00 — 44:00) • Photographer's Vocabulary
**On Screen:** Six examples with one subject (`V1`–`V6`): low angle, top-down, 24mm wide, 85mm f/1.8, golden hour, softbox studio.

#### Speaker Script:
> "Image models were trained on photo stock and film frames, so photographer's vocabulary is dense, unambiguous code for them. This is a handout; the essentials:
> - Heroic pose or building scale? `low angle`.
> - Catalog flat lay? `top-down shot, flat lay`.
> - Portrait with a blurred background? `85mm f/1.8 lens, shallow depth of field`.
> - Warm backlight? `golden hour, warm rim light`.
> - Even, clean light? `softbox studio lighting`.
> 
> Remember: aspect ratio (16:9, 4:5, 1:1) is a parameter — `--ar` in Midjourney or the format selector in ChatGPT and Gemini — not words in the prompt."

---

### Slide 16 (44:00 — 49:00) • Lecture Equator: 5-Minute Break
**On Screen:** Break screen with a large `05:00` timer and "START 5 MIN" / "RESET" buttons. Preview of Part 2.

#### Speaker Script:
> "We have reached the lecture equator. Exactly 5 minutes of rest: starting the timer now.
> 
> As per our course policy, no chat exercises during breaks. Stand up, stretch, grab some water or coffee. In the second half: targeted edits by instruction, a consistent courier character across scenes, and a product photoshoot. See you in five minutes."

---

### Part 2: Control Patterns, Code Automation, Risks & Homework (49:00 — 90:00)

---

### Slide 17 (49:00 — 52:00) • The Edit Loop
**On Screen:** 5-step loop: Draft (2–4 candidates) ➔ Select (by must-haves) ➔ Single Edit ("only X to Y") ➔ Diff Check (what drifted?) ➔ Finalize (save prompt). Refinement template and three rules.

#### Speaker Script:
> "Welcome back. Let's move to practical control patterns.
> 
> The novice habit is hitting 'regenerate' 20–30 times and wondering why everything changes. An engineer works in **The Edit Loop**:
> 1. Generate 2 to 4 drafts from a structured prompt.
> 2. Select the best one against the must-have checklist — as we did with A3.
> 3. Apply **exactly one edit per step**, like an atomic git commit.
> 4. Diff check: what changed, and what drifted?
> 5. Finalize and save the exact prompt.
> 
> Template: *'Edit this image. Modify only object X to Y. Preserve: angle, lighting, background, and shadows. Do not change: surrounding room geometry.'* Name what to preserve explicitly — the model protects those zones.
> 
> Practical rule: **after ~5–8 consecutive edits, drift becomes visible** — faces, logos, and small details start to wander. At that point, take your best frame and start a fresh chat."

---

### Slide 18 (52:00 — 57:00) • Pattern 1: Edit by Instruction
**On Screen:** Left: 4 frames of one scene: original `A2` (morning coffee shop, mug), object `B1` (mug ➔ iced latte), lighting `B2` (rainy evening), style `E2` (flat vector illustration). Right: formula "Frame A2 + one edit per step", copyable prompts `B1` and `B2`, and a tools hint: ChatGPT / Gemini / Kling — edit by instruction; Leonardo — inpainting with a mask.

#### Speaker Script:
> "Look at the left column: four frames of the same scene:
> - In `B1`, we swapped the ceramic mug for a tall glass of iced latte. The counter, the espresso machine on the left, the chairs, and the shadows barely changed — that is control.
> - In `B2`, we changed only the time of day and weather: rainy evening outside, raindrops on the glass, warm pendant lamps on — composition and objects stay put.
> - In `E2`, we turned the same composition into a flat vector illustration.
> 
> On the right is the formula: **Frame A2 + one edit per step**. We tell the model: *'Edit this photo. Replace only the ceramic mug with a tall glass of iced latte... Keep everything else exactly the same: camera angle, counter, espresso machine, background, light direction and shadows.'*
> 
> And the terminology at the bottom right. In chat models (ChatGPT, Gemini) and in Kling this is **edit by instruction**: we describe the change in words and the model builds the mask itself. **Inpainting** in the strict sense is when we paint the mask ourselves, as in Leonardo, and prompt only that area.
> 
> Use cases: product variants for a store, seasonal banner changes, porting to a brand style."

---

### Slide 19 (57:00 — 61:00) • Pattern 2: Courier Master Sheet
**On Screen:** Left: character sheet `C1_sheet` (4 angles on light grey: front, 3/4, profile, back) and 5 fixed anchors. Right: "Naive" vs "Engineering" cards, the full master sheet prompt (C1), and "Where to use it: Gemini, ChatGPT, Leonardo, Kling. In Midjourney — via the Edit Model (up to 4 references; replaced --cref / --oref in 08.2026)".

#### Speaker Script:
> "Now the hardest problem in visual storytelling: the same person in ten different scenes. Our running benchmark is the **food delivery courier**.
> 
> The 'Naive' card: if you just type *'food courier cycling in the rain'* in every scene, you get a new person every time — different age, face, jacket. No consistency.
> 
> The engineering protocol has two steps:
> 1. **Character sheet first (frame `C1`).** No story scene yet! A full-body figure in a neutral pose on light grey, in four angles: front view, three-quarter view, side profile, back view.
> 2. **Lock 5 contrast anchors**, written into the prompt:
>    - *short curly dark-brown hair*,
>    - *small silver hoop earring in left ear*,
>    - *bright yellow waterproof jacket with reflective grey stripe*,
>    - *square turquoise thermal backpack*,
>    - *white sneakers*.
> 
> Copy the prompt from the slide and run it in Gemini, ChatGPT, Leonardo, or Kling. For anyone who learned Midjourney from older courses: `--cref` and `--oref` are gone in V8 — since August 2026 references go through the **Edit Model**, up to 4 images. Save the result as `C1_sheet.png` — the character's master passport for every later scene and video."

---

### Slide 20 (61:00 — 64:00) • Pattern 2B: A Real Person as Reference
**On Screen:** Input 1 — 2–3 real face photos (front in studio, emotion, daylight). Input 2 — prompt (Gemini / ChatGPT / Leonardo) with a "holds the face" badge: preserve facial identity, `Do not beautify, rejuvenate or stylize`, 4 angles, courier outfit. Result — a 4-angle sheet. "Anti-pattern" and "Bridge to production" cards.

#### Speaker Script:
> "What if the hero must be a specific person — you, an actor, a brand ambassador? Here is a real case using my own photos.
> 
> Input: 2–3 real photos with different light and expression. Prompt: *'Create a photorealistic character reference sheet based on the attached photos... Preserve facial identity: face shape, eyes, nose, lips, jawline, hairline, skin tone. Do not beautify, rejuvenate or stylize his face.'* Then the same 4 angles and the same courier outfit.
> 
> Anti-pattern: without `do not beautify`, the model smooths the skin and 'improves' the face into a stock one.
> 
> Be honest about the result: the face is recognizable in all four angles, but it is not a guarantee — small features can drift, so always check by eye. In a chat, attach the photos to the prompt; in code, pass the files in `contents`.
> 
> Ethics: **only your own photos or with the person's explicit consent**. This sheet then goes into scenes and into Kling / Veo for video."

---

### Slide 21 (64:00 — 68:00) • Courier in Scenes & the First Video Frame (Kling / Veo)
**On Screen:** Top: three scenes: `C2_rain` (cycling in the rain, 16:9 — base for video), `C3_door` (doorstep handover, 35mm), `C4_break` (park bench break, 85mm). Bottom: scene transfer prompt, formats (16:9 / 9:16), and the bridge-to-video pipeline for Kling 3.0 / Veo 3.1. "In tools" line: Gemini / ChatGPT, Leonardo, Midjourney (Edit Model), Kling / Veo (First Frame).

#### Speaker Script:
> "How do we move this character into a story?
> Look at the transfer prompt: we attach `C1_sheet.png` as a reference and repeat the text anchors: *'Use attached character sheet (C1) as identity reference: The same courier (same face, curly hair, silver hoop earring, yellow jacket with grey stripe, turquoise backpack) is riding a city bicycle through a rainy evening street...'*.
> 
> The resulting frames:
> - In `C2`, she cycles through wet cobblestone streets.
> - In `C3`, she hands over the order at a door.
> - In `C4`, she takes a break on a park bench.
> Format is set by the selector: 16:9 for YouTube and landscape video, 9:16 for Reels and Shorts.
> 
> Now the bottom-right card — **our direct bridge to Lesson 05 (Video Generation)**. The biggest problem in video models is faces morphing in motion. How do we fight it?
> 1. Take the still frame `C2_rain.png` (16:9).
> 2. Upload it to Kling 3.0 or Google Veo 3.1 in the **First Frame slot — the first frame (t₀)**.
> 3. Add a short motion prompt: *'courier starts pedaling, wheels splash puddles, camera tracks along'*.
> 4. Result: face and outfit are **noticeably more stable** than generating video from scratch. Not perfect, though — still check video frames for face and outfit drift."

---

### Slide 22 (68:00 — 72:00) • Pattern 3: E-Commerce Product Photoshoot
**On Screen:** Left: master packshot `D0_packshot` on white with the studio prompt. Right: 4 catalog frames (`D1` kitchen lifestyle, `D2` flat lay, `D3` in hands, `D4` 1:1 promo banner), the catalog scene prompt with reference `D0`, and the "Engineering control" card.

#### Speaker Script:
> "The most in-demand business scenario: marketplaces, online stores, social media.
> 
> On the left is master packshot `D0`: a real product photographed once on white (or generated from the first prompt on the slide).
> 
> Then, attaching `D0` as a reference, we generate a product shoot without renting a studio:
> - `D1`: morning kitchen lifestyle with window light.
> - `D2`: flat lay, top-down.
> - `D3`: in hands — buyers instantly read the real scale.
> - `D4`: promo banner with room for typography.
> 
> Prompt #2 always includes the anti-drift constraint: *'Do not change mug shape, clay glaze, or proportions'*. Reference D0 plus this constraint keep the mug **noticeably more stable**. Honestly, though, the speckle pattern and handle proportions can still wander — so every frame gets human acceptance. That is the yellow zone from the risks block."

---

### Slide 23 (72:00 — 75:00) • Pattern 4: Multi-Reference Composition
**On Screen:** Left: two references: Image 1 (courier `C1_sheet`) + Image 2 (mug `D0_packshot`). Right: final frame `E1_compose`: the courier drinks from that exact mug in a morning café. "Role rule" card and composition prompt (Nano Banana / ChatGPT).

#### Speaker Script:
> "What if you upload two images and naively say *'Combine them'*? You get mush — a mug with a face or a ceramic backpack.
> 
> The rule is **explicit role assignment**:
> *'Image 1 is the courier character, Image 2 is the exact ceramic mug. The courier from Image 1, in her yellow jacket with grey stripe, sits at a coffee shop window counter on her break and drinks from exactly the mug from Image 2...'*.
> Image 1 = identity reference (hero), Image 2 = product reference (item). Add a third — say, a lighting reference — and name its role too.
> 
> In `E1`, the face and jacket come from Image 1, the mug's glaze and shape from Image 2, and the scene is unified by consistent morning light.
> 
> And remember the reference limits from the market table: Nano Banana 2 — up to 14 objects and 5 characters; the Midjourney Edit Model — up to 4."

---

### Slide 24 (75:00 — 79:00) • Batch Generation via Code — Same SDK as L03
**On Screen:** Python code: `google-genai`, reference `packshot.png`, loop `for row in csv.DictReader(open("catalog.csv"))`, call to `gemini-3.1-flash-image` with `response_modalities=["IMAGE"]` and `ImageConfig(aspect_ratio="16:9")`, then `for part in resp.parts: if part.inline_data: part.as_image().save(f"{row['sku']}.png")`. Callouts: "~50 cards in ~10 min for ~$2–3", "Don't take parts[0] blindly", "10/90 in code".

#### Speaker Script:
> "How does this work in production, when you need cards for a whole catalog?
> 
> We use the same official `google-genai` SDK as in Lesson 03:
> 1. Read `catalog.csv` and loop over rows — one product per row.
> 2. In `contents`, pass the `PIL.Image` reference and the text built from the `PROMPT_SPEC` template for that row.
> 3. In `GenerateContentConfig`, set `response_modalities=['IMAGE']` and `aspect_ratio='16:9'`.
> 4. Key detail: **the response is a list of `parts`** that can hold both text and images. Don't take `parts[0]` blindly — loop and save the part that has `inline_data`, named by the product SKU.
> 
> Realistic estimate: **about 50 cards in about 10 minutes for $2–3** — roughly 10 seconds and 4–6 cents per image, excluding retries and human acceptance. Instead of a day of manual browser work.
> 
> And 10/90 again: the model call is 5 lines. The rest is catalog parsing, prompt templating, retries, and automated artifact checks."

---

### Slide 25 (79:00 — 84:00) • Risks & Blast Radius
**On Screen:** Four risks: anatomy & small text; detail drift after ~5–8 edits; copyright (Thaler, US Supreme Court declined on 02.03.2026; Disney / Universal v. Midjourney); provenance (SynthID + C2PA). Blast Radius traffic light: Green (autonomous), Yellow (human-in-the-loop), Red (prohibited).

#### Speaker Script:
> "Let's cover safety and limits. First, four risks:
> - **Anatomy & small text:** fingers in crowds and long paragraphs still fail.
> - **Detail drift:** same number as in the Edit Loop — after ~5–8 consecutive edits, drift in faces and logos becomes visible.
> - **Copyright:** in the US, a purely AI-generated image without human authorship is not copyrightable. On March 2, 2026, the Supreme Court declined to hear Thaler, so that position stands. Meanwhile, Disney and Universal v. Midjourney is ongoing — training on others' characters is still an open question.
> - **Provenance:** remember the opening hook? Photorealism can no longer be told apart by eye, but **SynthID** can tell — an invisible watermark in the pixels, embedded by Google and, since May 2026, by OpenAI. **C2PA** is signed provenance metadata, but a screenshot strips it.
> 
> Now the Blast Radius matrix from L01:
> - **Green (autonomous):** moodboards, concept art, internal slides, storyboards. Six fingers on a background passer-by won't sink the project.
> - **Yellow (Human-in-the-Loop):** product cards, marketing banners, YouTube thumbnails. Generation is allowed, but **human sign-off is mandatory** before publishing.
> - **Red (prohibited):** legal documents, medical instructions, third-party trademarks, and real people's faces without consent."

---

### Slide 26 (84:00 — 87:00) • Homework Assignment #4
**On Screen:** Two tracks (Track A: Product Photoshoot, Track B: Glovo Delivery Courier) and the `genai-homeworks/L04/` submission structure (`images/`, `prompts.md`, `qa.md`).

#### Speaker Script:
> "Homework Assignment #4. Pick one of two tracks:
> - **Track A (Product Photoshoot):** photograph any object on your desk against white and generate 4 commercial frames: lifestyle, flat lay, in hands, banner.
> - **Track B (Glovo Delivery Courier):** generate a character sheet, take the courier through 3 scenes with anchor keywords, and make 1 targeted edit by instruction.
> 
> **Mandatory for everyone:** run one identical prompt in two different tools (e.g., Leonardo.ai vs. ChatGPT or Gemini) and document the differences in `qa.md`: what held, what drifted, how each model behaved.
> 
> The main grading criterion is not perfect beauty but deliberateness: a visible move from freeform to structure, and drift recorded honestly. Submit to `genai-homeworks/L04/` and invite me as a collaborator: `ihar_rubanovich@epam.com`."

---

### Slide 27 (87:00 — 90:00) • Summary & Lesson 05 Teaser
**On Screen:** Four principles of visual AI engineering and a teaser of the courier in the rain for Lesson 05: Video Generation.

#### Speaker Script:
> "Let's summarize today's four principles:
> 1. **Tool to match task:** chat for concepts and text, studio for canvas and masks, API for batch automation.
> 2. **Structure over freeform:** 6 slots (subject, setting, camera, light, style, constraints) plus a must-have block that doubles as an acceptance checklist.
> 3. **Surgical edits over rerolls:** atomic 'modify only X, preserve Y' commands beat regenerating from scratch.
> 4. **Consistency via anchors:** a master reference plus 4–6 distinctive textual anchors hold the character in any scene.
> 
> And a teaser for next time. Look at our courier on the bicycle. In **Lesson 05**, these frames become first frames for video models — Kling, Google Veo, and Runway: our courier will pedal off through the evening city.
> 
> Thank you for your focus. Unmute your microphones, and let's take your questions."
