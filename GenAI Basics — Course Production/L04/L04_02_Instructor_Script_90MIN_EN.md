# Lecture 04: Image Generation and Editing APIs — Full Instructor Script (90 Minutes)
**Course:** GenAI Basics • Module 2 (Multimodality)  
**Instructor:** Igor Rubanovich (`ihar_rubanovich@epam.com`)  
**Format:** 21 slides • 90 minutes with 5-minute break • No fluff, no AI-ness, engineering peer-to-peer

---

## Pedagogical Manifesto

1. **Central Engineering Thesis:** "Image generation becomes useful when it stops being a slot machine." Anyone can generate pretty pictures in Midjourney via a web prompt. Production engineering begins when outputs are deterministic, preserve exact product geometry, leverage binary alpha masks, and integrate into automated enterprise pipelines.
2. **Shift to Module 2 (Multimodality):** Moving beyond text strings and discrete BPE tokens (Lessons 01–03). Computer vision and diffusion architectures demand working with latent vector spaces (VAE), binary masks, multimodal conditioning signals (Identity, Style, Layout), and network streaming of Base64 binary bytes.
3. **The 10/90 Axiom in Computer Vision:** Calling the model API (`client.images.generate()`) is only 10% of the solution. The remaining 90% is Base64 decoding, uploading to S3/GCS, CDN signed URL distribution, PII/NSFW pre-flight moderation, async job polling workers, cost governance, and metadata provenance audit trails (hash, seed, prompt, reviewer).
4. **Time Budget:**
   - **Part 1 (Slides 01–14):** 00:00 — 50:00 (Diffusion physics, 6 primitives, prompt anatomy, references, masks, API lifecycle)
   - **Equator (Slide 15):** 50:00 — 55:00 (5-minute coffee break with interactive countdown timer)
   - **Part 2 (Slides 16–21):** 55:00 — 90:00 (The 10/90 iceberg, Blast Radius, live demo, decision tree, homework memo, Q&A)

---

# PART 1: DIFFUSION PHYSICS, PRIMITIVES & CONTROLLED PROMPTING (00:00 — 50:00)

---

### Slide 01 (00:00 — 04:00) • Title Cover
**On Screen:** Clean hero layout: *"Image Generation and Editing APIs: From Random Pixels to Controlled Production Pipelines"*. Subtitle: *"GenAI Basics • Module 2: Multimodality • Lesson 04"*. Core axiom callout: *"The 10/90 Axiom: The model API call is only 10% of the system. 90% of production reality is masks, geometric preservation, asset object storage, metadata audit trails, and moderation review gates"*.  
**Progress Indicator:** `01 / 21` • 5%

#### What the Speaker Says:
> "Good afternoon, colleagues. Welcome to Lesson 04 of our GenAI Basics course. Today, we officially enter our second major curriculum milestone — **Module 2: Multimodality**.
>
> In our first three sessions, we explored large language models from first principles: BPE tokenization, attention context windows, autoregressive sampling, and establishing your first Python API client returning strict, database-ready JSON schemas. We mastered text as an HTTP microservice.
>
> Today, we take an architectural leap: shifting from discrete text tokens to pixels, visual features, and multimodal conditioning.
>
> Let's anchor our session on an essential engineering reality: **image generation becomes useful for enterprise software only when it stops being a slot machine**.
>
> Typing *'draw a beautiful futuristic car'* into Midjourney or ChatGPT and admiring the result is entertainment. In enterprise production, our requirements are fundamentally different: take an authentic product photo from our catalog, replace the warehouse background with a modern sunlit kitchen, but **preserve the mug shape, ceramic glaze, handle ergonomics, and brand logo down to the exact millimeter**, receive the binary bytes over an API, decode Base64, persist to S3 storage, and log an audit trail for legal compliance.
>
> Quick calibration in the chat: type **1** if you have already triggered image generation through code or APIs, and type **2** if you have only interacted with visual models via web UIs so far.
>
> Excellent, I see your responses. Let's move into our operational setup."

---

### Slide 02 (04:00 — 07:00) • Instructor Profile
**On Screen:** Instructor card: Igor Rubanovich (Engineering Manager II & AI Ambassador @ EPAM Systems). Photo, professional engineering background. Highlight card: *"Hands-on AI R&D: Creator and architect of Creator Tools — a suite of AI tools for YouTube creators designed to save production time, streamline content workflows, and increase earnings (pet-project)"*. Official homework submission email: `ihar_rubanovich@epam.com`.  
**Progress Indicator:** `02 / 21` • 10%

#### What the Speaker Says:
> "A brief note on background for anyone joining us for the first time. I am Igor Rubanovich, Engineering Manager II and AI Ambassador at EPAM Systems.
>
> Alongside enterprise delivery programs, I lead an active AI R&D pet-project called Creator Tools — a specialized suite of AI microservices for YouTube creators. Within Creator Tools, we automate real-world media workflows: video transcript extraction, automated script structuring, and programmatic thumbnail composition with strict constraints on typography safety zones and facial fidelity.
>
> Everything we discuss today is forged in practical production engineering: the exact roadblocks you face when automating visual media, why generated imagery morphs, and how to enforce determinism in non-deterministic models.
>
> For code reviews, homework submissions, and architectural questions, reach me directly at: `ihar_rubanovich@epam.com`."

---

### Slide 03 (07:00 — 10:00) • Curriculum Roadmap
**On Screen:** 6-module curriculum stepper:  
`Module 1: Foundations & Core API (L01–L03)` [Completed] ➔ `Module 2: Multimodality (L04–L06)` [YOU ARE HERE — L04: Images, L05: Video, L06: Audio] ➔ `Module 3: Developer Tooling (L07–L09)` ➔ `Module 4: Local AI (L10)` ➔ `Module 5: Agents & MCP (L11–L13)` ➔ `Module 6: Production Engineering (L14–L16)`. Bottom callout: *"Multimodality is an API contract expansion: advancing from text tokens to high-dimensional tensors and latent diffusion spaces"*.  
**Progress Indicator:** `03 / 21` • 14%

#### What the Speaker Says:
> "Let's review our curriculum navigation. Having concluded Module 1 with structured JSON APIs, we now cross into **Module 2: Multimodality**.
>
> Enterprise systems do not live on text alone. End-users upload machinery damage photos, architectural blueprints, invoices, security camera footage, and voice logs.
>
> Module 2 delivers comprehensive coverage of these modalities:
> - Today, **Lesson 04**: Image generation, programmatic inpainting, masks, and integrating Image APIs into backend pipelines.
> - **Lesson 05**: Video generation models and APIs (Runway Gen-3, Kling, OpenAI Sora, Pika).
> - **Lesson 06**: Audio, speech-to-text, and voice synthesis (Whisper, ElevenLabs).
>
> This visual foundation is foundational: when we construct autonomous agents and Model Context Protocol servers in Module 5, your agents must be capable of inspecting application UI screenshots, creating diagrams, and reviewing graphical assets autonomously."

---

### Slide 04 (10:00 — 13:00) • GitHub Workflow & Homework Setup
**On Screen:** Folder hierarchy in `genai-homeworks/`:  
`├── L01/`  
`├── L02/`  
`├── L03/`  
`└── L04/`  
`    ├── brief.md                 # Visual Generation Canvas (requirements & constraints)`  
`    ├── references/               # Source reference assets`  
`    ├── prompt_v1.txt             # Initial unstructured prompt`  
`    ├── prompt_v2.txt             # Revised production prompt with sacred constraints`  
`    ├── candidates/               # Generated candidate variants`  
`    ├── qa.md                     # Defect audit scorecard`  
`    └── selected/                 # Final accepted production asset`  
Bottom callout: *"No private customer data or recognizable faces without consent. Use synthetic or open-source assets"*.  
**Progress Indicator:** `04 / 21` • 19%

#### What the Speaker Says:
> "As with all previous lessons, all artifacts are submitted via your personal GitHub repository.
>
> For Lesson 04, create a feature branch `lesson-04` and directory `genai-homeworks/L04/`.
>
> Take note of the artifact requirements. We do not submit random generated pictures. We submit an engineering package:
> 1. `brief.md` — your formal Visual Generation Canvas specifying business targets and sacred immutable attributes.
> 2. `references/` — the exact input imagery fed into the model.
> 3. Your prompt iteration history: comparing naive `prompt_v1.txt` against structured `prompt_v2.txt`.
> 4. `qa.md` — an objective evaluation matrix grading candidates against failure modes.
> 5. `selected/` — the final accepted deliverable accompanied by recorded execution metadata (model, seed, latency).
>
> Confirm that `ihar_rubanovich@epam.com` is invited as a Collaborator."

---

### Slide 05 (13:00 — 17:00) • The Trap: Pretty ≠ Usable
**On Screen:** Contrast layout. Left: "Toy Generation" (Visually striking, cinematic graphic). Right: "Silent Production Failures" (5 fatal enterprise flaws):  
1. *Product geometry distortion* (handle moved, proportions drifted).  
2. *Brand logo hallucination* (trademark mutated into gibberish).  
3. *Factual misrepresentation* (features or dimensions that do not exist).  
4. *Copyright & privacy exposure* (unlicensed likenesses, unvetted training artifacts).  
5. *Zero reproducibility* (unrepeatable output causing pipeline paralysis).  
**Progress Indicator:** `05 / 21` • 24%

#### What the Speaker Says:
> "Here lies the central danger in Generative Computer Vision. In text LLMs, a bad generation is immediately evident upon reading: syntax errors, factual contradictions, or hallucinations.
>
> In visual generation, **an unusable image can look stunningly beautiful**.
>
> Consider this real scenario: an e-commerce marketing pipeline tasks an image API with generating lifestyle imagery for a ceramic mug. The model returns a breathtaking, magazine-quality render bathed in golden hour sunlight. To an untrained eye, it looks ready to publish.
>
> But when evaluated against the physical product:
> - The ergonomic handle curvature has shifted by 15%. Customers purchasing this mug will receive an entirely different physical object.
> - The printed company emblem has hallucinated into stylized pseudo-text.
> - The power outlet on the kitchen wall reflects an EU socket standard for a US marketplace campaign.
>
> In e-commerce, publishing that image triggers customer returns, regulatory penalties for false advertising, and brand devaluation.
>
> In production, aesthetics are secondary. **Geometric fidelity, contractual accuracy, and legal compliance are non-negotiable**."

---

### Slide 06 (17:00 — 21:00) • Modality Shift: Diffusion Physics & Latent Space
**On Screen:** Architecture diagram comparing text vs visual physics.  
Top: "Text LLMs" (Discrete BPE tokens $w_1 \to w_2 \to w_3$, autoregressive categorical next-token probability).  
Bottom: "Diffusion Models & Diffusion Transformers (DiT)":  
`Pixel Space Image` ➔ `VAE Encoder` ➔ `Latent Space z (8x to 16x compression)` ➔ `Forward Process: Gaussian noise injection` ➔ `Reverse Process: Iterative denoising steps` guided via `Cross-Attention` from `CLIP / T5 Text Encoder` ➔ `VAE Decoder` ➔ `Synthesized Image`.  
**Progress Indicator:** `06 / 21` • 29%

#### What the Speaker Says:
> "Let's inspect what happens beneath the hood of image models and how their physics diverge from LLMs.
>
> Large language models operate over discrete token vocabularies. They predict one integer token ID at a time in sequence.
>
> An image, by contrast, is a continuous high-dimensional matrix of millions of RGB values. Generating pixels autoregressively one by one is computationally prohibitive for high-resolution graphics.
>
> Modern production systems rely on **Latent Diffusion Models** and **Diffusion Transformers (DiT)** — the architecture powering FLUX.1, Stable Diffusion 3, Imagen 3, and OpenAI Sora:
> 1. A Variational Autoencoder (VAE) compresses the raw pixel canvas into a compact latent space, reducing dimensionality by a factor of 8 to 16.
> 2. During training, structured images are corrupted with Gaussian noise until pure entropy remains.
> 3. The neural network is trained to reverse this corruption: predicting and subtracting noise step by step. Your text prompt passes through an encoder (like T5 or CLIP), steering this denoising trajectory through cross-attention layers.
>
> This explains why the **Seed parameter** is critical in image engineering. The seed determines the initial Gaussian noise distribution. Pinning the seed is your primary lever for achieving reproducibility."

---

### Slide 07 (21:00 — 25:00) • Mental Model: Image Generation as a Production Workflow
**On Screen:** C4 diagram `image_generation_workflow_pipeline.png`. Left to right:  
1. *Input Assets:* Product photo, binary alpha mask, `visual_spec.json`.  
2. *API Gateway:* Quota validation, timeouts, 16:9 aspect ratio, seed constraints.  
3. *Inference Cluster:* Cloud GPU execution.  
4. *Binary Handling:* Base64 decoding, checksum verification.  
5. *Storage & Audit DB:* S3 bucket upload, logging prompt, model version, latency, and cost.  
6. *Human Review Gate:* Moderation approval queue before release.  
**Progress Indicator:** `07 / 21` • 33%

#### What the Speaker Says:
> "Study the C4 pipeline on Slide 07. This is how enterprise computer vision actually operates.
>
> Notice that the foundation model occupies just one isolated node in the center. Everything flanking it is standard software engineering:
> 1. We prepare clean source assets: uncompressed product references, alpha masks protecting immutable zones, and machine-readable JSON specs.
> 2. The request traverses an API gateway enforcing aspect ratios and safety filters.
> 3. The response arrives not as a browser link, but as raw Base64 bytes.
> 4. Our backend decodes the payload, performs integrity hashing, and uploads optimized assets to AWS S3 or Google Cloud Storage with CDN signed URLs.
> 5. Simultaneously, our audit database registers the digital provenance: exact prompt string, model hash, seed, and execution cost.
> 6. Finally, the asset enters a Human Review Gate. If you omit storage, metadata, and review gates, you do not have an enterprise system — you have a playground script."

---

### Slide 08 (25:00 — 29:00) • The 6 Visual Primitives
**On Screen:** 6-card architectural matrix:  
1. **Text-to-Image:** Synthesizing visual scenes from text instructions from scratch (Concept art, background plates).  
2. **Image-to-Image:** Transforming an input image while maintaining spatial layout (Rough wireframe to high-fidelity UI).  
3. **Inpainting:** Modifying pixels strictly inside a defined mask boundary (Replacing catalog background behind an item).  
4. **Outpainting:** Extending the canvas beyond existing image borders (Expanding a 1:1 square photo into a 16:9 banner).  
5. **Reference Conditioning:** Enforcing identity, stylistic, or pose constraints via reference embeddings.  
6. **Negative Constraints:** Explicit elimination of unwanted artifacts (No text, no watermarks, no extra fingers).  
**Progress Indicator:** `08 / 21` • 38%

#### What the Speaker Says:
> "Let's formalize our primitives. All production computer vision pipelines are built from combinations of six core operations:
>
> First: **Text-to-Image**. Generating visual pixels from scratch using text alone. Best suited for broad conceptual exploration where strict adherence to an existing physical object is unnecessary.
>
> Second: **Image-to-Image**. Conditioning the generation on an existing source image plus a transformation prompt. Ideal for converting sketches or 3D block-outs into polished scenes.
>
> Third: **Inpainting**. The workhorse of commercial e-commerce. You define a mask and instruct the model: *'denoise pixels under the white mask according to this prompt, but preserve every pixel outside the mask bit-for-bit'*.
>
> Fourth: **Outpainting**. Expanding the canvas. Taking a vertical 9:16 mobile photo and generating consistent environment on the left and right to fit a 16:9 desktop banner.
>
> Fifth: **Reference Conditioning**. Supplying visual anchors to pin identity, color palettes, or human poses.
>
> Sixth: **Negative Constraints**. Deterministic negative prompts stripping out distorted text, watermarks, and anatomical glitches."

---

### Slide 09 (29:00 — 33:00) • Prompt Anatomy: An Engineering Brief, Not a Poem
**On Screen:** Structured specification breakdown:  
• `Subject:` Precise focal entity (single hero object, materials, surface glaze).  
• `Composition & Camera:` Framing (eye-level, product macro), focal length, shallow depth of field, presentation-safe negative space.  
• `Environment & Lighting:` Supporting surface, directionality of light (warm side light), natural shadows.  
• `Style:` Commercial studio photography (explicit prohibition of 3D renders or illustrations).  
• `Sacred Attributes:` Inviolable features (mug handle curvature, glaze texture, logo placement).  
• `Acceptance Criteria:` Explicit test criteria required for release.  
**Progress Indicator:** `09 / 21` • 43%

#### What the Speaker Says:
> "A frequent rookie mistake is treating image prompts like poetry: *'stunning, breathtaking, hyperrealistic, award-winning 8k masterpiece'*.
>
> These decorative adjectives are noise. Modern foundation models largely ignore them, and they consume conditioning bandwidth.
>
> In production, an image prompt is an **engineering specification**:
> 1. **Subject:** Exactly what exists in focus. One speckled ceramic mug.
> 2. **Composition:** Camera perspective, depth of field, and dedicated negative space for downstream UI typography.
> 3. **Lighting:** Coherent physical lighting. Soft lateral morning light from the left casting realistic contact shadows.
> 4. **Style:** Defined photographic aesthetic. Commercial editorial photography.
> 5. **Sacred Attributes:** The immutable boundaries. What the model is strictly forbidden to alter.
> 6. **Acceptance Criteria:** Objective criteria for acceptance or rejection.
>
> The most consequential line in any production prompt is not what to create, but **what must remain untouched**."

---

### Slide 10 (33:00 — 37:00) • Before / After: Weak Prompt vs Production Spec
**On Screen:** Side-by-side contrast table.  
Left (Weak Prompt): *"Make a beautiful advertisement for this mug in a cozy studio"*. Result: Random noisy backdrop, morphed handle, distorted logo, unsolicited croissants and props, zero reproducibility in automated pipelines.  
Right (Production Spec): *"Using input_product.png as the protected product reference, preserve mug shape, ceramic glaze, handle position, and proportions 100%. Replace only background and surface with pale travertine in natural morning light. 16:9 crop, 2K resolution. No text, no people, no extra props. Return 3 variants. Acceptance: zero geometric drift against catalog master"*.  
**Progress Indicator:** `10 / 21` • 48%

#### What the Speaker Says:
> "Examine the contrast on Slide 10.
>
> On the left is the naive user prompt: *'Make a beautiful ad for this mug'*. The model assumes 99% creative freedom. It alters the mug handle, invents props, and adds unreadable text labels. You cannot ship this.
>
> On the right is an engineering specification. Every parameter is isolated and bounded. We pin the geometry, define the surface material, mandate 16:9, and explicitly ban people and text.
>
> This specification can be parameterized in Python, mapped to a database dictionary, and run systematically across 10,000 SKUs. That is the dividing line between prompt roulette and scalable software."

---

### Slide 11 (37:00 — 41:00) • Reference Signals & Multimodal Control
**On Screen:** C4 infographic `multimodal_reference_control.png`. 3 independent input conditioning channels converging on the central diffusion core:  
1. *Identity Reference (IP-Adapter):* Extracted feature vectors preserving faces, characters, or physical product geometry.  
2. *Style Reference:* Color palettes, textural grain, and cinematic mood vectors.  
3. *Layout / Structural Reference (ControlNet):* Depth Maps, OpenPose skeletons, and Canny edge wireframes.  
Bottom callout: *"References are mathematical conditioning vectors injected into Cross-Attention layers, not vague inspiration"*.  
**Progress Indicator:** `11 / 21` • 52%

#### What the Speaker Says:
> "How do we constrain diffusion when text alone is too imprecise?
>
> Modern multimodal pipelines rely on **Reference Conditioning Signals**. It is vital to decouple the different types of reference:
>
> 1. **Identity References (IP-Adapter):** Specialized adapters extract facial or geometric embeddings from source photos, enforcing product or character consistency across multiple generations.
> 2. **Style References:** Supplying an aesthetic reference image from which the model extracts only the chromatic palette and lighting atmosphere without duplicating objects.
> 3. **Structural / Layout References (ControlNet):** Injecting explicit geometric constraints — Depth Maps for spatial depth, OpenPose for human skeleton alignment, or Canny Edge detectors for architectural boundaries.
>
> When you combine these three signals with a structured prompt, randomness drops dramatically."

---

### Slide 12 (41:00 — 45:00) • Inpainting & Masking Mechanics
**On Screen:** Technical schematic `inpainting_mask_mechanics.png`. 3 inpainting stages:  
1. *Input Setup:* Source Photo + Binary Alpha Mask (Black `0` = Protected Product Latents, White `255` = Active Denoising Region).  
2. *Noise Injection:* White masked region receives Gaussian noise and is denoised via UNet/DiT conditioned on prompt; black pixels remain frozen in latent space.  
3. *Edge Blending & Harmonization:* Boundary feathering algorithm (4–8px blur) ensuring natural shadow casting and optical reflections without seam artifacts.  
**Progress Indicator:** `12 / 21` • 57%

#### What the Speaker Says:
> "Let's inspect the exact mechanics of Inpainting on Slide 12.
>
> How does a diffusion model know where it is allowed to modify pixels? Through a **binary alpha mask**.
>
> The mask is a single-channel image with matching resolution:
> - Black pixels (value 0) indicate frozen latents. The model is mathematically forbidden from altering these values. The product geometry remains pristine.
> - White pixels (value 255) denote the active editing zone. Noise is injected exclusively here, and iterative denoising reconstructs the background per your prompt.
>
> Notice the crucial engineering detail at the border: **Edge Feathering**. If you use a knife-sharp binary boundary, the composite will exhibit artificial cut-out edges. A slight boundary blur of 4 to 8 pixels allows the model to compute realistic contact shadows and optical reflections across the seam."

---

### Slide 13 (45:00 — 48:00) • API Lifecycle & Network Payloads
**On Screen:** Network protocol flow. Top: "Request Payload" (`multipart/form-data` or JSON with `model`, `prompt`, `image_base64`, `mask_base64`, `aspect_ratio`, `seed`, `n`). Bottom: "Response Handling":  
- *Synchronous Pattern (Fast APIs):* Direct Base64 data string returned in HTTP response within 2–5 seconds.  
- *Asynchronous Queue Pattern (Heavy Studio APIs):* Immediate `202 Accepted` returning `job_id: "img_98765"` ➔ Status polling loop (`GET /jobs/{id}`) or Webhook callback ➔ Secure signed CDN download URL.  
**Progress Indicator:** `13 / 21` • 62%

#### What the Speaker Says:
> "What traverses the wire when invoking an Image API from backend code?
>
> There are two dominant architectural patterns:
>
> **Pattern 1: Synchronous Base64 (Google Gemini, OpenAI).**  
> You POST a JSON payload containing the prompt and Base64-encoded reference images. The connection remains open for 3 to 6 seconds, returning the generated image directly in the response payload. This is ideal for interactive conversational flows.
>
> **Pattern 2: Asynchronous Job Queues (Adobe Firefly, Midjourney API, local ComfyUI).**  
> 4K rendering and multi-stage pipelines take 30 to 60 seconds. Holding HTTP sockets open risks gateway timeouts. The API immediately returns an HTTP 202 with a `job_id`. Your backend either polls the job status endpoint or listens for a webhook, followed by downloading the asset from an ephemeral signed S3 URL."

---

### Slide 14 (48:00 — 50:00) • Provider Landscape Without Hype
**On Screen:** Capabilities matrix for 2026:  
- **OpenAI (GPT-Image / DALL-E):** Streamlined API, superior prompt comprehension, conversational editing via Images and Responses endpoints.  
- **Google Cloud (Gemini 3.1 Flash Image / Imagen 3/4):** Native multimodal dialog context, low-latency Base64 streaming, enterprise Vertex AI integration.  
- **Adobe Firefly Services / Photoshop API v2:** Enterprise gold standard for commercial copyright indemnity, advanced generative fill, and PSD layer workflows.  
- **Open Source (FLUX.1 / SDXL):** Self-hosted GPU deployment (RunPod/ComfyUI), zero external data transmission, full ControlNet and LoRA customization.  
**Progress Indicator:** `14 / 21` • 67%

#### What the Speaker Says:
> "Let's review the vendor landscape objectively. As engineers, we do not engage in brand tribalism; we match technical requirements to capabilities.
>
> For rapid application prototyping with deep prompt reasoning, **OpenAI** and **Google Gemini** are excellent choices. Google delivers Base64 bytes directly, simplifying microservice integration.
>
> When operating in regulated enterprise environments with stringent legal requirements, **Adobe Firefly Services** is the market benchmark. Adobe trains exclusively on licensed stock and provides enterprise copyright indemnity.
>
> For strict data sovereignty (on-premise deployment) or custom fine-tuning via LoRA and ControlNet, open-weights models like **FLUX.1** hosted on your own GPU infrastructure provide total autonomy.
>
> We have now reached our midpoint. Time for our scheduled break."

---

# ☕ EQUATOR: MIDPOINT BREAK 5 MINUTES (50:00 — 55:00)

---

### Slide 15 (50:00 — 55:00) • Midpoint Break
**On Screen:** Break screen featuring an interactive 5-minute countdown timer: `05:00`. Controls: `▶ Start 5 Min`, `⏸ Pause`, `↺ Reset`. Callout: *"Step away, hydrate, and stretch. Cognitive rest only — no chat crowdsourcing. In 5 minutes, we examine the 10/90 Computer Vision iceberg, Blast Radius governance, run live demo code, and review homework"*.  
**Progress Indicator:** `15 / 21` • 71%

#### What the Speaker Says:
> *(Speaker clicks "Start 5 Min" button on slide)*
>
> "Colleagues, 50 minutes completed. We take our 5-minute break now. Step away from your workstations, grab water or coffee, and let your minds rest. We keep the chat clear of work topics so everyone recharges.
>
> In exactly five minutes, we return to explore the 10/90 iceberg, Blast Radius governance, execute live demo scripts, and review the homework memo. Enjoy the break!"

---

# PART 2: PRODUCTION ICEBERG, BLAST RADIUS, LIVE DEMO & HOMEWORK (55:00 — 90:00)

---

### Slide 16 (55:00 — 60:00) • The 10/90 Iceberg in Computer Vision
**On Screen:** C4 systems iceberg `image_api_10_90_iceberg.png`.  
Above Water (10% Visible Tip): *`Model API Call: prompt ➔ client.images.generate() ➔ bytes`*.  
Below Water (90% Hidden Infrastructure):  
- `Binary Base64 Decoder & MIME Sanitizer`  
- `S3 / GCS Storage Bucket & CDN Signed URLs`  
- `PII & NSFW Moderation Gate`  
- `Async Job Queue & Rate-Limit Concurrency Control`  
- `Audit & Provenance DB (hash, seed, prompt, latency, cost)`  
- `Human-in-the-Loop Review Dashboard`  
**Progress Indicator:** `16 / 21` • 76%

#### What the Speaker Says:
> "Let's resume. We now arrive at our central architectural rule: **The 10/90 Axiom applied to Computer Vision**.
>
> Look at the iceberg on Slide 16. Academic tutorials show only the 10% above water: calling `generate()` and rendering an image in a notebook.
>
> In enterprise engineering, that single line of code is trivial. 90% of your system is submerged infrastructure:
> 1. Binary payloads weigh 2 to 5 megabytes. You cannot store raw blobs in relational databases. You need immediate ingestion pipelines into S3 or Cloud Storage, paired with signed CDN access URLs.
> 2. Content Moderation. If an end-user uploads PII or inappropriate media, your service must intercept it before it hits external models or public feeds.
> 3. Cost Governance. Image generation costs 2 to 8 cents per invocation. An unthrottled loop generating 10,000 variants will burn $800 in 15 minutes. Concurrency limiting and response caching are vital.
> 4. Provenance Auditing. You must record an immutable digital footprint: which prompt generated the asset, what model version ran, what seed was used, and which human reviewer signed off."

---

### Slide 17 (60:00 — 65:00) • Blast Radius Governance in Image AI
**On Screen:** Three-tier risk governance matrix (Traffic Light):  
- 🟢 **Green Zone (Autonomous):** Internal moodboards, synthetic test data for QA, exploratory concept sketches. Failure cost is zero.  
- 🟡 **Yellow Zone (Human-in-the-Loop):** E-commerce catalog backgrounds, editorial blog headers, YouTube thumbnails. Model generates 3–4 candidates; human editor holds publishing veto.  
- 🔴 **Red Zone (Taboo for AI Autonomy):** Legal evidence, medical diagnostics, certified packaging labels, direct brand logo modifications. AI autonomy strictly prohibited.  
**Progress Indicator:** `17 / 21` • 81%

#### What the Speaker Says:
> "How does an enterprise determine where Generative AI can be deployed safely today versus where it must be strictly forbidden?
>
> We use the **Blast Radius Framework**, segregating workloads into three security tiers:
>
> **Green Tier (Autonomous):** Zero risk. Designers brainstorming visual themes, developers generating synthetic profile avatars to load-test staging databases. Here, full automation is appropriate.
>
> **Yellow Tier (Human-in-the-Loop):** Moderate risk. E-commerce background replacement, social media banners, marketing materials. The model acts strictly as a copilot, generating 3 to 4 candidates. **No pixel reaches production without a human click**.
>
> **Red Tier (Absolute Taboo):** Zero AI autonomy permitted. Never use diffusion models for legal evidence, medical imaging, or direct-to-print packaging with certified ingredients. Hallucinations in the red zone result in regulatory fines, product recalls, and severe liability."

---

### Slide 18 (65:00 — 73:00) • Live Demo: From Chaos to Control
**On Screen:** Demo walkthrough from `demo_repo`:  
1. `01_generate.py` — Hero generation from structured prompt, Base64 decoding, writing to `out/generated_product_hero.png`.  
2. `02_edit.py --mode vague` vs `--mode controlled` — Side-by-side editing: vague prompt breaks mug geometry; controlled prompt preserves 100% of product while replacing background with travertine.  
3. `03_build_prompt.py` — Programmatic prompt compilation from `visual_spec.json`.  
**Progress Indicator:** `18 / 21` • 86%

#### What the Speaker Says:
> "Let's turn to code in our `demo_repo`.
>
> **Round 1:** Running `01_generate.py`. We connect via the official `google-genai` SDK using `gemini-3.1-flash-image`. Notice the request format: we specify a 16:9 aspect ratio and structured photographic constraints. The response returns Base64 data, which we decode and persist to disk in `out/`.
>
> **Round 2:** Our most critical demonstration. Running `02_edit.py --mode vague`. We pass our product mug and ask: *'make it look premium in a warm studio'*. Observe the output: the mug handle has mutated, and the glaze pattern has morphed. This asset is unusable for e-commerce.
>
> Now, we run `02_edit.py --mode controlled`. Using the exact same source asset, our prompt explicitly commands: *'Replace only background and surface with travertine studio. Preserve mug shape, speckled glaze, handle position, and proportions'*. Opening the result: the mug geometry is 100% identical to the source, seamlessly integrated into a new studio environment.
>
> **Round 3:** Inspecting `03_build_prompt.py`. In enterprise backends, prompts are not hardcoded strings. They are assembled deterministically from validated schemas (`visual_spec.json`), ensuring consistent compliance across millions of runs."

---

### Slide 19 (73:00 — 78:00) • Decision Matrix: GenAI vs Classical CV vs Deterministic Tools
**On Screen:** Architectural decision tree:  
- `Task: Vector logos, crisp typography, UI layouts?` ➔ **Deterministic Software: Figma / Adobe Illustrator / SVG ($0 cost, 0ms latency, 100% accuracy)**.  
- `Task: Defect detection, barcode scanning, edge tracking?` ➔ **Classical Computer Vision: OpenCV, YOLO, Canny Edge ($0 inference cost, 2-5ms latency)**.  
- `Task: Environment replacement, aesthetic variation, concept art?` ➔ **Generative AI Image APIs (OpenAI, Gemini, Firefly, FLUX)**.  
**Progress Indicator:** `19 / 21` • 90%

#### What the Speaker Says:
> "How do senior engineers choose the right tool? Always adhere to the principle: **'Problem first, not AI first'**.
>
> If you need to render a corporate logo, format text labels, or align banner layouts — **never use a diffusion model**. Text generated by diffusion models is probabilistic and prone to typographic errors. Deterministic tools like Figma, CSS, SVG, or Python's Pillow library cost zero dollars, run in zero milliseconds, and guarantee 100% accuracy.
>
> If you need industrial quality inspection, license plate recognition, or barcode scanning, use classical Computer Vision like OpenCV. They run locally on CPU in 3 milliseconds.
>
> Reserve Generative AI for tasks requiring semantic synthesis: complex lighting integration, photorealistic texture generation, and creative variations."

---

### Slide 20 (78:00 — 85:00) • Homework Assignment: Reproducible Image Workflow Pack
**On Screen:** Homework specification.  
**Select One Production Scenario:**  
1. *E-commerce:* Product background replacement with strict geometry preservation.  
2. *YouTube / Media:* Video thumbnail plate with clean negative space for typography (Creator Tools benchmark).  
3. *Tech Event:* Conference announcement banner with presentation-safe zones.  
**Deliverable Checklist in `genai-homeworks/L04/`:**  
- `brief.md` — completed Visual Generation Canvas.  
- `references/` — source assets used.  
- `prompt_v1.txt` & `prompt_v2.txt` — prompt iteration audit trail.  
- `candidates/` — at least 2 generated candidate outputs.  
- `qa.md` — defect audit scorecard.  
- `selected/` — final approved asset with recorded metadata.  
- Feature branch `lesson-04`, PR to `main`, invite `ihar_rubanovich@epam.com`.  
**Progress Indicator:** `20 / 21` • 95%

#### What the Speaker Says:
> "Let's review Homework Assignment 04.
>
> Your objective is to engineer a **Reproducible Image Workflow Pack**.
>
> You select one realistic business use case: an e-commerce catalog update, a YouTube thumbnail plate adhering to Creator Tools guidelines, or a tech conference banner.
>
> You complete `brief.md`, formulate your initial prompt, generate candidates, evaluate them in `qa.md` for geometry drift or artifacts, iterate your prompt in `prompt_v2.txt`, and store the final approved candidate in `selected/`.
>
> Evaluation is based on **pipeline reproducibility and constraint enforcement**, not subjective beauty.
>
> Submit via Pull Request on branch `lesson-04` by our next session."

---

### Slide 21 (85:00 — 90:00) • Wrap-up, Q&A & Lesson 05 Teaser
**On Screen:**  
*Three Core Takeaways:*  
1. *Production imagery is a technical specification, not a gamble:* Pinning geometry and constraints outweighs decorative adjectives.  
2. *Masks and reference signals provide hardware-level control:* Decouple style, identity, and layout conditioning.  
3. *The 90% iceberg governs production reliability:* Object storage, Base64 decoding, audit metadata, and Human-in-the-Loop gates.  
*Next Session Teaser:* **Lesson 05 — Video Generation Models & APIs (Runway Gen-3, Kling, Sora, Pika)**.  
*Open Mic:* 🎙️ Microphones open — questions welcome in voice and chat!  
**Progress Indicator:** `21 / 21` • 100%

#### What the Speaker Says:
> "To conclude our fourth session:
>
> Today, we debunked the myth that AI image generation is an uncontrollable toy. We demonstrated that with disciplined engineering — binary masks, geometric preservation constraints, and metadata logging — Image APIs become dependable components of enterprise systems.
>
> Next week, we expand our pipeline into the temporal domain. **Lesson 05 is entirely dedicated to Video Generation**: analyzing models like Runway Gen-3, Kling, and OpenAI Sora, mastering Camera Motion Control, and frame interpolation.
>
> The floor is now open for Q&A. Feel free to unmute or drop your questions in the chat!"
