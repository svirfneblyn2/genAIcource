# Research Brief — Lesson 04: AI Image Generation (state as of 2026-10-02)

Method: web search + fetch of public pages, 2026-10-02. Primary (vendor) sources are preferred; where only aggregators/reviews were reachable, the item is marked **[secondary]**. Items that could not be verified or where sources conflict are marked **[UNCERTAIN]**. Several vendor pages (openai.com, docs.midjourney.com, udemy.com, netology.ru) returned HTTP 403 to the fetcher; facts about those were taken from secondary reports and are flagged.

---

## 0. TL;DR for the lesson designer

- The 2026 market has converged on **"conversational, reference-driven, reasoning image models"**: GPT Image 2/2.5 (OpenAI), Nano Banana 2 / Pro / 2 Lite (Google), Grok Imagine Image 2.0 (xAI/SpaceXAI), Kling IMAGE 3.0 / O1 (Kuaishou), Seedream 5.0 (ByteDance), FLUX.2 (BFL). They all do: text→image, edit-by-instruction, multi-reference composition (4–16 images), legible text, 2K–4K.
- **Midjourney** remains the aesthetics-first, parameter-driven outlier (V8.2 default since 2026-07-24), and in Aug 2026 replaced Omni Reference / Character Reference / Retexture with a single **Edit Model** (up to 4 references, inpaint/outpaint).
- Teachable common core across vendors: **structured prompt (scene → subject → details → constraints)**, **photographic vocabulary**, **"change only X, keep everything else"** edit pattern, **reference images for consistency**, **iterate one change at a time**.
- Provenance is now a default: **C2PA + SynthID** on OpenAI (since May 2026) and Google outputs.
- Legal anchor points: US Supreme Court denied cert in *Thaler* (2026-03-02) — purely AI-generated output not copyrightable in the US; *Disney/Universal/WBD v. Midjourney* in discovery.

---

## 1. What popular image-generation courses teach

### 1.1 Course examples (public pages only)

| # | Course | Provider | URL | Module list (as published) |
|---|---|---|---|---|
| 1 | Prompt Engineering for AI Image Generation | Coursera / Logical Operations (~5 h) | https://www.coursera.org/learn/prompt-engineering-ai-image-generation-lo095035 | M1 Using AI to Generate an Image (choosing tools, first generation) · M2 Getting the Image You Want (subject, art style, camera angle, lighting, color, aspect ratio) · M3 Implementing Image Generation in a Business Setting (variability, deepfakes, copyright/IP) · M4 graded assessment |
| 2 | Prompt Engineering for Vision Models | DeepLearning.AI + Comet (1 h 32 m) | https://www.deeplearning.ai/courses/prompt-engineering-for-vision-models | Overview · Image Segmentation (SAM, point/box prompts) · Object Detection · Image Generation (strength, guidance scale, inference steps; inpainting) · Fine-tuning (DreamBooth-style) · Quiz. Code-first. |
| 3 | AI Prompting for Everyone | DeepLearning.AI (7 h) | https://learn.deeplearning.ai/courses/ai-prompting-for-everyone/lesson/k2cchl/image-generation | Module 3 "multimedia": image understanding, image generation (8 min), building apps, final project |
| 4 | Image Generation with AI Training Course | Coursera / Simplilearn | https://www.coursera.org/learn/image-generation-with-ai-training-course | M1 Stable Diffusion & denoising (+demo text→image) · M2 Autoencoders, contrastive learning, shared embedding spaces (theory-heavy) |
| 5 | Next 2026 — Image Generation with Gemini (Nano Banana) lab | Google Skills | https://www.skills.google/focuses/155778?parent=catalog&path=3940 | Hands-on lab: `genai.Client`, call `gemini-2.5-flash-image`, send prompt, save image (Python) |
| 6 | Creating AI-Generated Visuals for Creative Inspiration (Ben Mornin) | Domestika (4 units, 3 h 52 m) | https://www.domestika.org/en/courses/5560-creating-ai-generated-visuals-for-creative-inspiration/course | U2 Midjourney basics, how generation works, limitations · U3 first image, commands & parameters, editing tools, prompt tips · U4 styles/Niji, style consistency, **consistent characters**, blending styles, advanced params, **copyright & commercial use** |
| 7 | Unlock Creative Inspiration: Rapid Concept Generation with AI (Víctor Mollá) | Domestika (5 units) | https://www.domestika.org/en/courses/5541-unlock-creative-inspiration-rapid-concept-generation-with-ai-assistance/course | How generative AI works · Midjourney account · commands, prompt tips, parameters, visual styles · **Vary, Remix, Upscale, Vary Region, Zoom** · character consistency, style consistency, own style, copyright |
| 8 | MidJourney Masterclass: The Art of AI-Driven Image Creation (updated 3/2026) | Udemy **[secondary — page 403]** | https://www.udemy.com/course/midjourney-masterclass-the-art-of-ai-driven-image-creation/ | How MJ interprets prompts; lighting & style; `--ar --stylize --seed --chaos`; consistent characters; product photography; website mockups; children's book illustration; freelancing assets |
| 9 | «ИИ в дизайне» | Skillbox (1 month, 11 h practice) | https://skillbox.ru/course/ai-for-designers/ | ChatGPT for ideation → Midjourney prompting & image work → branding/identity, infographics, UX/UI analysis. 2 practicals + diploma (concept + logo/identity visuals) |
| 10 | «Нейросети для дизайна» | Яндекс Практикум (2 months) **[secondary — page truncated; via Habr 2026-06-30]** | https://practicum.yandex.ru/ai-tools-for-designers/ · https://habr.com/ru/articles/1052816/ | Image generation, retouching, sound/video, typography & composition with AI; 10+ tools; portfolio projects "from concept art to final visuals" |
| 11 | «Нейросети для дизайнеров» | BangBang Education (2 months, 7 HW) | https://bangbangeducation.ru/course/neural-networks | Intro → prompting basics → **controlling generations** → working with images → video → voice/music → 3D → (opt.) extending AI, key visuals, portfolio case |
| 12 | «Нейросети для дизайнеров» | Нетология **[secondary — page 403]** | https://netology.ru/programs/nejroseti-dlya-dizajnerov | "AI pipeline of a designer": research → concept → production; Midjourney, Magnific.ai (upscale), Immersity AI (2D→3D/parallax) |

Popular YouTube formats (examples, not view-verified): "FULL 2026 Midjourney AI Tutorial (for Beginners)" (V8.1) https://www.youtube.com/watch?v=aodE4be2t-g ; "Nano Banana Full Guide and Best Practices" (built on Google's official guide) https://www.youtube.com/watch?v=XZALWN0wv48 ; tool-comparison videos "Nano Banana vs Flux vs Midjourney" https://www.youtube.com/watch?v=U7zSzLo-I9c. **[UNCERTAIN: popularity/view counts not verified]**

### 1.2 Recurring module list (synthesis)

1. **How it works (light theory)**: diffusion/denoising, text–image embeddings; why outputs vary (seed). Present in #2, #4, #6, #7.
2. **Tool landscape & choosing a tool** (#1, #6, #11, comparison videos).
3. **Prompt anatomy**: subject, style, camera angle/framing, lighting, color, aspect ratio (#1 M2, #6 U3, #7 U3, #8).
4. **Parameters/controls**: Midjourney `--ar --s --c --seed --no`, or API knobs (guidance, strength, steps) (#2, #6, #7, #8).
5. **Iteration tools**: variations, remix, upscale, vary region/inpaint, zoom/outpaint (#7 U4, #6 U3, #2).
6. **Consistency**: consistent characters & style (sref, cref/oref, references) — appears in almost every applied course (#6, #7, #8, BangBang "управление генерациями").
7. **Applied cases**: product photography, mockups, branding/logo, infographics, book illustrations, key visuals (#8, #9, #11).
8. **Post-processing pipeline**: upscalers (Magnific), 2D→3D/video (#12, #11).
9. **Ethics/legal**: deepfakes, copyright, commercial use (#1 M3, #6, #7).
10. **Final project / portfolio piece** (#9 diploma, #11 portfolio case, #1 graded assessment).

Typical exercises/homework formats: (a) recreate a reference image by prompt only; (b) produce N variations varying one factor (light, lens, style); (c) consistent character / brand-asset series (3–5 images); (d) product shot set for a fictional brand; (e) logo/identity concept; (f) mini-portfolio case with prompts documented.

Gap relevant to an engineering audience: almost no consumer course teaches **API usage, reproducibility (seed/prompt logging), cost per image, or provenance (C2PA/SynthID)** — a natural differentiator for an EPAM engineering track.

---

## 2. Current state of services (Oct 2026)

### 2.1 OpenAI — ChatGPT Images / GPT Image

| Item | Fact | Source |
|---|---|---|
| Lineage | gpt-image-1 (2025-03-25) → gpt-image-1-mini (2025-10-06) → gpt-image-1.5 "ChatGPT Images" (2025-12-16) → **gpt-image-2** (API 2026-04-21; ChatGPT "Images 2.0" 2026-04-22) → **GPT Image 2.5 / ChatGPT Images 2.5** (2026-09-08) | https://en.wikipedia.org/wiki/GPT_Image ; https://www.mindstudio.ai/blog/what-is-gpt-image-2 [secondary] |
| Current model | **ChatGPT Images 2.5**; API variants **`gpt-image-2.5-flare`** (fast default) and **`gpt-image-2.5-sunburst`** (slower, precise editing) | https://www.datacamp.com/blog/chatgpt-images-2-5 [secondary]; https://datanorth.ai/news/openai-launches-chatgpt-images-2-5 [secondary] |
| Signature features 2.0 | "Thinking" (reasoning before generation: plans layout/text/object relations), up to 2K, up to 8 images per prompt, strong multilingual text incl. non-Latin | https://www.mindstudio.ai/blog/what-is-gpt-image-2 [secondary] |
| New in 2.5 | `@Sketch` (draw → image), templates (posters, merch), **comment on a region of the image for focused edits**, better multi-turn consistency, ~50% lower latency, up to 16 reference images and 4K **[UNCERTAIN: 16 refs / 4K from Picsart & Wikipedia-style summaries; DataCamp lists 1024/1536 sizes — conflicting]** | https://www.datacamp.com/blog/chatgpt-images-2-5 ; https://picsart.com/ai-models/gpt-image-2-5/ [secondary] |
| Access | ChatGPT (all tiers incl. Free, with limits), ChatGPT Work, Codex, OpenAI API | DataCamp (above) [secondary] |
| API price | ~$30 / 1M image output tokens, $8 / 1M image input, $5 / 1M text input (same as GPT Image 2) | DataCamp (above) [secondary] |
| Strengths | #1 on Text-to-Image and Image-Edit Arena at Grok 2.0 launch (Aug 2026); text/UI/infographics; instruction following; conversational editing | https://x.ai/news/grok-imagine-image-2 ; https://www.unite.ai/xai-ships-grok-imagine-image-2-0-with-precise-editing-and-a-top-arena-ranking/ |
| Weaknesses | Dense typography and complex layout restructuring can still break global consistency; trails Midjourney on pure aesthetics (reviewer opinion) | DataCamp; MindStudio [secondary] |
| Provenance | C2PA Content Credentials + (since 2026-05-20) **Google SynthID** invisible watermark; public checker openai.com/verify (preview) | https://www.resultsense.com/news/2026-05-20-openai-c2pa-synthid-content-provenance/ [secondary, cites openai.com/index/advancing-content-provenance/] |
| Preferred prompt style | Natural language, ordered **scene/background → subject → key details → constraints**; literal text in "quotes" or ALL CAPS; for edits "change only X … keep everything else the same", repeat the preserve-list each turn | https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide |

### 2.2 Google — Nano Banana family (Gemini image models)

| Marketing name | Model ID | Date | Notes | Source |
|---|---|---|---|---|
| Nano Banana (legacy) | `gemini-2.5-flash-image` | Aug 2025 | ~$0.039/image API; migration recommended | https://ai.google.dev/gemini-api/docs/image-generation ; https://www.aifreeapi.com/en/posts/nano-banana-ai-image-generator [secondary] |
| **Nano Banana Pro** | `gemini-3-pro-image` (was `-preview`) | 2025-11-20 | Premium: reasoning, Search grounding, 4K, infographics; up to 6 object + 5 character refs (API) | https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/ ; https://9to5google.com/2025/11/20/gemini-3-nano-banana-pro/ ; ai.google.dev |
| **Nano Banana 2** (default in Gemini app) | `gemini-3.1-flash-image` | 2026-02-26 | Pro-level knowledge at Flash speed; 512px–4K; consistency "up to 5 characters and 14 objects" (blog) vs "up to 10 object + 4 character images" (API docs) **[UNCERTAIN: surface-dependent]**; web-search grounding | https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/ ; ai.google.dev |
| **Nano Banana 2 Lite** | `gemini-3.1-flash-lite-image` | 2026-06-30 | Fastest/cheapest, ~4 s, $0.034 per 1K image; no Search grounding | https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/ |

- **No newer Gemini image model found as of 2026-10-02** (Gemini 4 "Argon" LLM announced 2026-09-30; no image-model news found) — https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/ **[UNCERTAIN: check before class]**
- Access: Gemini app (web/mobile), Google Search AI Mode, Lens, Photos, Flow, Google Ads, AI Studio, Gemini API, Vertex AI. Gemini-app daily caps reported: Basic 20 / Plus 50 / Pro 100 / Ultra 1000 images **[secondary, aifreeapi]**. Google Pics (Workspace) announced at I/O 2026 **[secondary]**.
- Signature features: multi-image blending ("up to 6 to 14 … unconnected images", varies by surface — Google blog), character/subject consistency, conversational editing (multi-turn, `previous_interaction_id` in API), thinking (`thinking_level`), Search grounding, text rendering & translation/localization, aspect ratios 1:1…21:9.
- Provenance: SynthID on all outputs + C2PA Content Credentials; Gemini app can check SynthID ("Was this created with Google AI?") — blog.google Nano Banana 2 post; https://c2paviewer.com/articles/verify-ai-generated-image-c2pa-synthid [secondary].
- **Official prompting guidance** (Google Cloud blog, 2026-03-06, https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana):
  - Text→image formula: **[Subject] + [Action] + [Location/context] + [Composition] + [Style]**
  - With references: **[Reference images] + [Relationship instruction] + [New scenario]**
  - Grounded: [Source/Search request] + [Analytical task] + [Visual translation]
  - Tips: be specific; **positive framing** ("empty street" not "no cars"); control the camera (low angle, aerial); iterate conversationally; **start with a strong verb**; text in quotes + font spec.
  - "Creative director" levers: lighting, camera/lens/focus, color grading, materiality/texture.
  - API docs: "describe the scene, don't just list keywords" — https://ai.google.dev/gemini-api/docs/image-generation
  - Caveat from Google: "verify the factual accuracy of data-driven visuals like diagrams and infographics" (Nano Banana Pro tips post).

### 2.3 Midjourney

| Item | Fact | Source |
|---|---|---|
| Versions | V7 (2025) → V8 Alpha 2026-03-17 → V8.1 (2026-04-30; default from 2026-06-10) → **V8.2 default since 2026-07-24** | https://releasebot.io/updates/midjourney [secondary aggregator of MJ notes]; https://wavespeed.ai/blog/posts/what-is-midjourney-v8-features-pricing-how-to-use-2026/ [secondary] |
| Edit Model | 2026-08-27: "our first V8.2 image edit model" — instruction edits, up to **4 image references**, inpainting/outpainting, works with personalization/moodboards/srefs. Access: drag images to prompt bar, "edit" in lightbox, Edit tab, `--edit <urls>` on Discord. Replaces Omni Reference (and per third-party guides also Character Reference and Retexture) | https://updates.midjourney.com/edit-model-for-v8/ (primary); https://blakecrosley.com/guides/midjourney [secondary] |
| Access | Web (midjourney.com) + Discord; **no official public API**; no free trial (Niji app exception) | https://aiweekly.co/learning-ai/generative-ai/how-to-use-midjourney [secondary] |
| Price | Basic $10 / Standard $30 / Pro $60 / Mega $120 per month; Relax (unlimited slow) from Standard | blakecrosley guide [secondary] |
| Strengths | Aesthetics, style exploration, personalization; native 2K (`--hd`); improved text in V8.1+ | as above |
| Weaknesses | Weaker literal instruction following & text vs GPT/Gemini (one benchmark: MJ ~30% text accuracy vs ~90% Ideogram/FLUX **[secondary, methodology unknown]**); no API; legal exposure (Disney/Universal/WBD suit) | https://tech-insider.org/how-to-write-ai-image-prompts-2026/ [secondary] |

**Parameters (V8.2 status per blakecrosley.com guide updated 2026-09-22 [secondary]; MJ docs returned 403):**
- `--ar W:H` aspect (max 14:1; 4:1 in HD) ✓ · `--stylize/--s 0–1000` (default 100) ✓ · `--chaos/--c 0–100` ✓ · `--weird/--w 0–3000` ✓ · `--raw` (less MJ aesthetic, more literal) ✓ · `--sref <url|code>` + `--sw 0–1000` ✓ · `--p` personalization / moodboard profiles ✓ · `--no <thing>` (negative) ✓ · `--seed` ✓ · `--iw 0–2` ✓ · `--hd` native 2K ✓ · `--edit` ✓
- **Not on V8:** `--oref`/`--ow` (Omni Reference, V7-only → use Edit Model), `--cref`/`--cw` (Character Reference, V6-era legacy), `--q` (V7-only). `--draft`: Draft Mode exists (June 2026: 24 low-res images, cheaper) but V8.2 support is reported as **[UNCERTAIN/disputed]**.
- Moodboards = personalization profiles built from uploaded images (https://updates.midjourney.com/profiles-and-moodboards/). Personalization profile needs ~40 ratings minimum [secondary].
- Legacy editor tools (Vary Region, Zoom, Pan, Retexture) are what most 2024–25 courses teach (Domestika #7); in V8.2 they are consolidated into the Edit Model **[UNCERTAIN: whether old Vary Region UI still exists for V7 jobs]**.
- `/describe` (image → 4 suggested prompts) still exists **[secondary]**.
- Prompt style: short, concrete, most important subject first; text in "quotes"; MJ docs "Prompt Basics": fewer details = more variety, more details = more control — https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics (403 to fetcher; content via search snippet).

### 2.4 Kling (Kuaishou) — images

| Item | Fact | Source |
|---|---|---|
| Models | **Kling O1 / Image O1** (2025-12-01/02): unified multimodal model; image editing with **up to 10 reference images** | https://ir.kuaishou.com/news-releases/news-release-details/kling-o1-launches-worlds-first-unified-multimodal-video-model-0 ; https://www.prnewswire.com/news-releases/kling-o1-launches-as-the-worlds-first-unified-multimodal-video-model-302630630.html |
| | **Kling IMAGE 3.0** (2026-02-04): feature retention, precise detail edits, style control; extracts features from up to 10 refs; lock "subject contours, core elements, and tonal qualities" | https://kling.ai/quickstart/klingai-image-3-model-user-guide |
| | **Kling IMAGE 3.0 Omni** (2026-02-06): cinematic/narrative control, **Image Series mode** (coherent sets/storyboards), native 2K/4K, virtual try-on, multi-view, shot size/angle/focal-length/aperture changes | https://kling.ai/quickstart/klingai-image-3-omni-user-guide |
| Legacy | Kolors (Kuaishou's earlier open image model) **[not re-verified in this pass]** | — |
| Access | kling.ai web/app (credits-based subscription, free daily credits) + API; third-party hosts (fal, Krea, Artlist) **[pricing UNCERTAIN; ~$0.04/image for Image O1 via third party — https://vibedex.ai/blog/kling-image-o1-review]** | |
| Strengths | Reference-heavy consistency feeding directly into Kling video (image→video pipeline); cinematic framing vocabulary | |
| Prompt style | Cinematic/technical terms (over-the-shoulder, 24mm/85mm, aperture); edit formula: **"Keep everything else unchanged, modify [target] to [desired effect]."** e.g. "Keep everything else unchanged, change the cat into a dog." | Kling IMAGE 3.0 guide |

### 2.5 Grok Imagine (xAI → SpaceXAI)

| Item | Fact | Source |
|---|---|---|
| Corporate | SpaceX acquired xAI 2026-02-02; models now listed under "SpaceXAI" | https://x.ai/news/xai-joins-spacex ; https://en.wikipedia.org/wiki/SpaceXAI |
| Engine | Aurora (xAI's own autoregressive MoE image model, replaced earlier FLUX dependency) | https://www.artificialstudio.ai/create/grok-imagine-model [secondary] |
| Current | **Grok Imagine Image 2.0** (2026-08-07), "Quality Mode" on grok.com/imagine + iOS/Android; API id `grok-imagine-image-2.0` | https://x.ai/news/grok-imagine-image-2 |
| Features | Magic-wand region selection, segmentation, background removal w/ transparency, **multi-reference up to 5 images**, Smart Resize (9 aspect ratios), templates (product shots, headshots, icons, game assets), consistent characters/locations/props | x.ai (above) |
| Rank | #2 on Text-to-Image and Image-Edit Arena at launch (Edit Elo 1,439 vs GPT-Image-2 1,463) | https://datanorth.ai/news/spacexai-releases-grok-imagine-image-2-0 [secondary] |
| Price | Included in Grok app; API ~$0.02–0.06/image depending on mode/resolution **[UNCERTAIN: sources disagree]** | datanorth; layer.ai [secondary] |
| Content policy | Distinctive: "Spicy Mode" (adult content) since Aug 2025 → Jan 2026 deepfake/"undressing" scandal; Indonesia & Malaysia temporary blocks; California AG investigation; EU criticism; xAI then banned sexual images of real people in all modes | https://www.fortune.com/2026/01/06/elon-musks-grok-chatbot-deepfakes-nude-images-women-children ; https://www.yahoo.com/news/articles/malaysia-indonesia-become-first-block-052233588.html ; https://aiforensics.org/uploads/Grok_Unleashed_Updated.pdf |

### 2.6 Others (one line each)

- **FLUX (Black Forest Labs)**: FLUX.1 Kontext (2025, in-context editing) → **FLUX.2** (2025-11-25; Pro/Flex/Dev open-weights 32B/Klein Apache-2.0; up to 10 refs, 4MP, hex-color control) → **FLUX 3** multimodal (2026-07-23) **[secondary]** — https://docs.bfl.ml/release-notes ; https://en.wikipedia.org/wiki/Flux_(text-to-image_model) ; https://kie.ai/blog/what-is-flux-3
- **Ideogram 4.0** (2026-06-03): open-weight (Apache 2.0) 9.3B, native 2K, multilingual text, **structured JSON prompt interface**, layer-oriented — https://ideogram.ai/news/ideogram-4.0/
- **Recraft V4 / V4.1** (Feb 2026+): design taste, **native editable SVG vector output**, brand style sets — https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation
- **Adobe Firefly Image 5** (Oct 2025): native 4MP, layered editing, custom models trained on own portfolio; positioned as commercially safe (licensed training data) — https://en.wikipedia.org/wiki/Adobe_Firefly
- **Seedream 5.0 (ByteDance)**: Lite (2026-02-13, thinking + web search, 4K), Pro (2026-07, splits renders into 10+ transparent PNG layers), Flash (2K, 10 refs) **[secondary]** — https://www.buildfastwithai.com/blogs/seedream-5-0-pro-review-bytedance-multimodal-image-model-2026

---

## 3. Prompt techniques widely taught

1. **Free-form vs structured prompt.**
   - Google: [Subject]+[Action]+[Location]+[Composition]+[Style]; "describe the scene, don't just list keywords" (Cloud blog; ai.google.dev).
   - OpenAI: "background/scene → subject → key details → constraints"; for long prompts use labeled segments/line breaks (OpenAI Cookbook).
   - Midjourney: short and concrete, key subject first; parameters at the end (MJ Prompt Basics).
   - Canonical teaching template (synthesis): **Subject · Action · Setting · Composition/framing · Camera & lens · Lighting · Style/medium · Mood/color · Details/materials · Text (in quotes) · Constraints (what must not change) · Output (aspect, resolution)**.
2. **Photographic vocabulary**: shot size (close-up, wide), angle (low angle, aerial, over-the-shoulder), lens (24mm wide, 85mm portrait, macro), aperture/depth of field (f/1.8 bokeh), lighting setups ("three-point softbox setup", golden hour, rim light), film stock/color grade (e.g. Kodak Portra look), materials ("brushed aluminum" not "shiny metal"). Sources: Google Cloud guide ("Three-point softbox setup", "Wide-angle lens"); OpenAI Cookbook (material specificity); Kling 3.0 Omni guide (focal length/aperture).
3. **Negative prompts**: Midjourney `--no`; FLUX/SD negative prompt fields. Google advises the opposite for Gemini — **positive framing** ("empty street" instead of "no cars"). Teach both and the reason (language models attend to mentioned tokens).
4. **Weights**: Midjourney multi-prompt `::` weights, `--iw`, `--sw`, `--stylize`; Gemini/GPT have no weights — emphasis via ordering and repetition.
5. **Iterative refinement**: start with clean base prompt, then "small, single-change follow-ups" (OpenAI Cookbook); conversational iteration (Google); seed locking/variations (MJ `--seed`, Vary).
6. **Describe / image-to-prompt**: Midjourney `/describe`; with GPT/Gemini ask the chat model to describe an image as a prompt, then edit.
7. **JSON / structured prompts** — **viral 2025–26 community trend** (Nano Banana JSON prompts: fields for subject, camera, lighting, materials, composition, negative constraints) — e.g. https://miraflow.ai/blog/nano-banana-json-prompting-2026 ; https://github.com/ZeroLu/awesome-nanobanana-pro. **Note:** Google's official guide recommends narrative descriptions, not JSON; the benefit is mostly *discipline/reproducibility* (template variables), not a model-level feature. Exception: Ideogram 4.0 ships a structured JSON prompting interface officially (ideogram.ai). Good engineering angle: treat prompt as a config object with a renderer.
8. **Text in images**: put exact text in "quotes" (Google, OpenAI, MJ), specify font/weight/placement; OpenAI also suggests ALL CAPS for literal text; keep strings short.
9. **Edit-instruction templates** (short quotes):
   - OpenAI: "change only X" + "keep everything else the same" (Cookbook).
   - Kling: "Keep everything else unchanged, modify [target] to [desired effect]." (Kling IMAGE 3.0 guide)
   - Google: start with a strong verb — "Remove the man from the photo" (Cloud blog).

---

## 4. Practical patterns — how-to per service

| Pattern | ChatGPT (GPT Image 2.5) | Nano Banana (Gemini) | Midjourney V8.2 | Kling IMAGE 3.0 / O1 | Grok Imagine 2.0 |
|---|---|---|---|---|---|
| **Object replacement / inpainting** | Instruction edit "replace X with Y, keep everything else the same"; 2.5 lets you **comment on a region** for focused edit | Upload + "Change only the [object] to …" (semantic masking by language, no mask needed) | Edit Model: select area (inpaint) + prompt | "Keep everything else unchanged, change …" | **Magic Wand** select region → prompt |
| **Background replacement** | "Place the product on … keep product identical" | Same; positive description of new scene | Edit Model inpaint background / outpaint | Background change listed in guide | Background removal (transparent) + regenerate |
| **Consistent object/product/character** | Multiple reference images in one turn; repeat preserve-list; continue same chat | Up to 4–5 character + 6–14 object refs (model-dependent); provide 3+ angles of the subject (API docs) | Edit Model with up to 4 refs (replaces `--oref`/`--cref`); `--sref` + `--p`/moodboard for style; `--seed` | Up to 10 refs; Elements/subject lock; Image Series mode | Multi-ref up to 5; "consistent style" across related images |
| **AI photo shoot (product)** | Templates; "studio product shot, softbox, seamless background" | Google example: "high-end, glossy commercial beauty shot of …" | Strong aesthetics; product refs via Edit | E-commerce use cases in Omni guide | **Product-shot & headshot templates** |
| **Portrait shoot from selfies** | Real-person photo edits restricted in some cases **[UNCERTAIN — policy reports conflict]** | Works with own photos; consistency from 3+ angles | Edit Model refs | Portrait/expression edits in guide | Headshot template |
| **Virtual try-on** | Covered in OpenAI Cookbook use cases | Google Shopping "Try it on" from a selfie (Doppl app shut 2026-04-30; moved into Search) — https://blog.google/products-and-platforms/products/shopping/studio-quality-digital-try-on/ | — | Virtual try-on in Omni guide | — |
| **Style transfer** | "Render this photo in the style of [medium]" (living-artist styles may be refused) | Reference image of style + description | `--sref` / moodboards | Style control | Templates |
| **Outpainting / aspect change** | Change size/aspect in request | Choose aspect ratio 1:1–21:9 when regenerating | Edit Model outpaint; `--ar` | Framing techniques | **Smart Resize** (9 ratios) |
| **Text in image** | Best-in-class; quotes, font spec | Strong, incl. translation/localization | Improved in V8.1+; quotes | — | "Sharper typography" claim |
| **Upscaling** | Choose higher quality/size | 2K/4K output on Flash/Pro | `--hd` native 2K; upscalers | 2K/4K | 2K |

Sources for table: per-service rows in §2; OpenAI Cookbook use-case list (product extraction, virtual try-on, infographics, UI mockups, character consistency, object removal, compositing).

---

## 5. Limitations and risks

1. **Text rendering**: largely solved for short strings on GPT Image 2/2.5, Nano Banana 2, Seedream 5 Pro; dense/long text, small text and complex layouts still fail; Midjourney weaker **[secondary benchmark]** — https://tech-insider.org/how-to-write-ai-image-prompts-2026/ ; DataCamp 2.5 limitations.
2. **Hands/anatomy**: single clear hands mostly fine on flagships; crowds, interlocking hands, small background hands still fail **[secondary]** — same source.
3. **Identity drift in multi-turn editing**: errors accumulate across turns (color shift, face change); combining several edits per prompt worsens it. Mitigation: one change per turn, restate preserve-list, re-anchor with original reference. Research: https://arxiv.org/pdf/2512.01755 (FreqEdit); OpenAI Cookbook advice.
4. **Factual errors in infographics/diagrams**: Google explicitly warns to verify data visuals.
5. **Copyright**:
   - US: prompts alone insufficient for authorship (Copyright Office); Supreme Court denied cert in *Thaler v. Perlmutter* 2026-03-02 — https://www.cnbc.com/2026/03/02/us-supreme-court-declines-to-hear-dispute-over-copyrights-for-ai-generated-material.html ; https://ipwatchdog.com/2026/03/02/supreme-court-denies-thalers-latest-attempt-register-copyright-ai-generated-image/
   - *Disney & Universal (+WBD Sept 2025) v. Midjourney*: in discovery/mediation, expert disclosures Oct 2026 — https://www.hollywoodreporter.com/business/business-news/disney-universal-midjourney-1236262563/ ; https://www.theartnewspaper.com/2026/07/09/midjourney-demands-hollywood-AI-secrets
   - Style imitation controversy (Ghibli trend, 2025) — https://en.wikipedia.org/wiki/GPT_Image
6. **Likeness / deepfakes**: OpenAI allows some public-figure depictions with opt-out (Mar 2025 policy shift — https://www.techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation); photoreal deceptive use banned; Grok 2026 scandal shows regulatory risk. **[UNCERTAIN: exact current OpenAI rules on editing uploaded photos of real people]**
7. **Watermarks/provenance**: SynthID (Google; also OpenAI since May 2026) = invisible, survives some edits; C2PA = signed metadata, easily stripped by re-upload/screenshot. Verify via Gemini app, openai.com/verify, C2PA viewers. — https://c2paviewer.com/articles/openai-google-c2pa-synthid-2026 [secondary]
8. **Content policies differ**: OpenAI/Google conservative; Grok more permissive (adult "Spicy" mode with hard limits after Jan 2026); Midjourney community guidelines + public gallery by default on lower plans **[UNCERTAIN: Stealth mode is Pro/Mega only — not re-verified]**.
9. **Enterprise/data**: uploading client photos/brand assets to consumer apps — check data-use terms; API/enterprise tiers typically exclude training **[general, not re-verified per vendor]**.

---

## 6. Open items to re-check right before delivery
- Whether Google ships a Gemini-4-era image model (post Gemini 4 Argon, 2026-09-30).
- Exact GPT Image 2.5 resolution/reference limits (sources conflict: 1536px vs 4K; 16 refs).
- Midjourney Draft Mode on V8.2 and whether Vary Region still exists in UI.
- Grok Imagine API pricing.
- Kling consumer pricing / free credits.
