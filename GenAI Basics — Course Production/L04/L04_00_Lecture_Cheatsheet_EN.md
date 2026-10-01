# Speaker Cheatsheet (1 Page) • Lesson 04 (21 Slides • 90 Minutes)
*Speaker: Igor Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: Image Generation and Editing APIs: From Random Pixels to Controlled Production Pipelines (2026 Standard)*

---

### Part 1: Diffusion Physics, Primitives & Controlled Prompting (00:00 — 50:00)

* **Slide 01 (00–04 min) • Title Cover:** Image Generation and Editing APIs. Core thesis: "Image generation becomes useful when it stops being a slot machine." Anyone can generate pretty art in Midjourney. Engineering begins when results are reproducible, protect product geometry, and integrate into automated pipelines. Chat check: who has called Image APIs programmatically (1) vs browser UI only (2)?
* **Slide 02 (04–07 min) • Speaker Bio:** Igor Rubanovich (Engineering Manager II & AI Ambassador @ EPAM). Hands-on AI R&D: creator and architect of Creator Tools — a suite of AI tools for YouTube creators (pet-project). Homework submission email: `ihar_rubanovich@epam.com`.
* **Slide 03 (07–10 min) • Curriculum Roadmap:** Moving into **Module 2: Multimodality (Lessons 04–06)** marked as **"YOU ARE HERE"**. Moving beyond text tokens into visual modalities: images (L04), video (L05), speech & audio (L06).
* **Slide 04 (10–13 min) • GitHub Workflow:** Directory structure in `genai-homeworks/L04/`. Required files: `brief.md`, `references/`, `prompt_v1.txt`, `prompt_v2.txt`, `candidates/`, `qa.md`, `selected/`. Invite instructor `ihar_rubanovich@epam.com` as collaborator.
* **Slide 05 (13–17 min) • The Trap: Pretty ≠ Usable:** In text, flaws are obvious. In graphics, an image can look stunning yet be completely useless for business: mug shape morphed, brand logo distorted, label proportions drifted, extra fingers hallucinated, unclear IP rights, zero reproducibility.
* **Slide 06 (17–21 min) • Modality Shift: Diffusion Physics & Latent Space:** Why images are not BPE tokens. Autoregressive LLMs predict the next token, whereas Diffusion Models and Visual Transformers (DiT) operate in latent space (VAE): forward Gaussian noise injection and reverse iterative denoising steps guided by CLIP/T5 text embeddings.
* **Slide 07 (21–25 min) • Mental Model: Generation as a Pipeline (C4 Diagram):** The model is only one node. Production pipeline: `Source Assets (Product Photo + Alpha Mask)` ➔ `API Gateway (quotas, 16:9 ratio, seed)` ➔ `Inference Cluster` ➔ `Base64 Decoder` ➔ `Cloud Storage (S3/GCS)` ➔ `Metadata DB (prompt, hash, seed, model, cost)` ➔ `Human Review Gate`.
* **Slide 08 (25–29 min) • The 6 Visual Primitives:**
  1. *Text-to-Image* — generation from scratch via text brief.
  2. *Image-to-Image* — transformation of an input reference image.
  3. *Inpainting* — targeted editing strictly inside a mask.
  4. *Outpainting* — expanding the canvas beyond existing borders.
  5. *Reference Conditioning* — guiding style, composition, or object identity.
  6. *Negative Constraints* — strictly prohibiting unwanted artifacts.
* **Slide 09 (29–33 min) • Prompt Anatomy: An Engineering Brief, Not a Poem:** Image API prompts are structured specifications: Subject ➔ Composition & Camera Angle ➔ Environment & Lighting ➔ Style ➔ Sacred Attributes ➔ Acceptance Criteria. The most critical line: **what must NEVER change**.
* **Slide 10 (33–37 min) • Before / After: Weak Prompt vs Production Brief:** Side-by-side contrast. Weak: *"Make a nice ad for this mug"* ➔ distorted handle, hallucinated extra mugs. Production: *"Use photo as protected reference. Preserve mug shape, glaze, and handle geometry 100%. Replace background only with pale sunlit travertine. Eye-level, 16:9, no text, no people. Return 3 variants"*.
* **Slide 11 (37–41 min) • Reference Signals & Multimodal Control (C4 Diagram):** A reference is a control vector, not vague inspiration. Decoupling: 1) *Identity Reference* (IP-Adapter — facial features, exact product geometry); 2) *Style Reference* (color palette, lighting tone); 3) *Layout/Pose Reference* (ControlNet — Depth Map, OpenPose wireframes, Canny edge detection).
* **Slide 12 (41–45 min) • Inpainting & Masking Mechanics (Diagram):** Under the hood of inpainting. Binary alpha mask divides canvas into two zones: Black (0) = frozen pixels, White (255) = active denoising zone. Mask edge feathering for natural light and shadow blending.
* **Slide 13 (45–48 min) • API Lifecycle & Network Payloads:** What traverses the wire. Request: Multipart form-data or JSON payload with `data:image/png;base64`. Response: raw Base64 bytes or ephemeral CDN URL. Synchronous responses vs Asynchronous job queues (Job ID + Webhook/Polling for heavy generation batches).
* **Slide 14 (48–50 min) • Provider Landscape Without Hype:**
  - *OpenAI*: GPT-Image-2 / DALL-E (generation and editing via Images / Responses API).
  - *Google*: Gemini 3.1 Flash Image / Imagen 3/4 (multimodal conversational editing in single context).
  - *Adobe Firefly*: Image5 / Photoshop API v2 (commercial indemnity, production-grade inpainting, vector support).
  - *Open Source*: FLUX.1 / SDXL (self-hosted inference on RunPod/ComfyUI with full weight control).

---

### ☕ Equator: Midpoint Break 5 Minutes (50:00 — 55:00)

* **Slide 15 • Midpoint Break:**  
  *Click "Start 5 Min" button on slide.* Say: "Colleギes, 5 minutes for coffee and rest. In the second half, we will explore the 10/90 Computer Vision iceberg, Blast Radius governance, run live code, and unpack the homework assignment." *(Zero work discussion in chat — full cognitive rest).*

---

### Part 2: Production Iceberg, Blast Radius, Live Demo & Homework (55:00 — 90:00)

* **Slide 16 (55–60 min) • The 10/90 Iceberg in Computer Vision (C4 Diagram):** The 10% tip of the iceberg is `client.images.generate()`. The 90% submerged engineering is Base64 decoding, S3/GCS bucket uploads with CDN signed URLs, PII & NSFW moderation gates, concurrency rate limits, async polling workers, and audit metadata (hash, seed, prompt, latency, cost).
* **Slide 17 (60–65 min) • Blast Radius Governance in Image AI (Traffic Light):**
  - 🟢 **Green Zone (Autonomous):** Internal moodboards, synthetic test data, concept art, exploratory sketches.
  - 🟡 **Yellow Zone (Human-in-the-Loop):** E-commerce product backgrounds, marketing banners, YouTube thumbnails. Model generates 3–4 candidates, human grants final sign-off.
  - 🔴 **Red Zone (Taboo for AI Autonomy):** Legal evidence, medical diagnostics, direct packaging printing with certified claims, official brand trademark modifications.
* **Slide 18 (65–73 min) • Live Demo: From Chaos to Control (Code):**
  - Round 1: `01_generate.py` — hero generation from text spec, Base64 decoding, saving to `out/`.
  - Round 2: `02_edit.py --mode vague` vs `--mode controlled` — side-by-side demonstration: vague prompt destroys mug proportions; controlled prompt preserves 100% geometry while seamlessly swapping background.
  - Round 3: `03_build_prompt.py` — assembling structured visual prompts from `visual_spec.json`.
* **Slide 19 (73–78 min) • Decision Framework: GenAI vs Classical CV vs Deterministic Tools:**
  - Need exact vector logos or crisp typography? ➔ **Figma / Adobe Illustrator / SVG ($0 cost, 0ms latency, 100% accuracy)**.
  - Need barcode detection, defect inspection, or edge alignment? ➔ **Classical Computer Vision (OpenCV, YOLO, Canny)**.
  - Need scene replacement, visual variation, and concept generation? ➔ **Generative AI Image APIs**.
* **Slide 20 (78–85 min) • Homework Assignment: Reproducible Image Workflow Pack:**
  - Select a concrete business scenario (E-commerce catalog item, YouTube thumbnail, Event announcement banner).
  - Fill Visual Generation Canvas (`brief.md`): business objective, sacred attributes, negative constraints, QA criteria.
  - Generate 2 candidates, evaluate via rubric in `qa.md`, select final approved asset into `selected/`.
  - Push repository to `genai-homeworks/L04/`.
* **Slide 21 (85–90 min) • Wrap-up, Q&A & Lesson 05 Teaser:** Core takeaways: 1) Image generation is a specification, not roulette; 2) References and masks provide hardware-level control; 3) The 90% iceberg demands storage, metadata, and review. Next session: **Lesson 05 — Video Generation Models & APIs (Runway Gen-3, Kling, Sora, Pika)**. Microphones open!
