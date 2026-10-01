Lecture 04 - Image Generation and Editing APIs

GenAI Basics. Production package READY candidate. Audience: students with basic LLM concepts, not necessarily design or API experience.

# Purpose

This lecture teaches students how image generation and editing APIs fit into real product and content workflows. The point is not to make pretty pictures on demand. The point is to turn visual tasks into controlled, testable workflows: inputs, references, constraints, model call, output review, storage, rights, and iteration.

# Learning outcomes

• Explain the difference between text-to-image, image-to-image, inpainting, outpainting, variation, and image understanding.

• Describe the API workflow for generating and editing images, including input files, masks, prompts, outputs, metadata, and asynchronous job handling where needed.

• Write a practical image prompt/spec that includes subject, composition, style, constraints, reference strategy, and acceptance criteria.

• Choose between a conversational image model, a dedicated image model, and a creative-suite API based on product needs.

• Identify risks: privacy, copyright, brand consistency, misleading content, provenance, safety filters, cost, latency, and uncontrolled variation.

# Core story

Image generation becomes useful when it stops being a slot machine. A weak workflow says: generate a cool poster. A professional workflow says: use this product photo, keep the product shape unchanged, replace the background with a warm kitchen scene, preserve brand colors, create three variants, return transparent PNGs, store the prompt and seed if available, and send outputs to human review before publishing.

The model is only one component. A production workflow also needs source assets, references, masks, prompts, model choice, output handling, review gates, and audit metadata.

# Plain vocabulary


# Mental model: image API workflow

Input assets plus prompt plus controls go into the model. The API returns one or more images and metadata. The application stores the output, records the prompt/configuration, runs safety and quality checks, and asks a human to approve when the asset affects brand, money, trust, or legal risk.

• Inputs: text prompt, reference image, mask, style guide, product photo, target aspect ratio.

• Controls: model, size, quality, number of variants, safety settings, format, optional seed if the provider supports it.

• Output handling: decode or download image bytes, save to storage, write metadata, create thumbnails, link result to the original request.

• Review: check visual quality, factuality, brand match, policy compliance, rights, and publication readiness.

# API task types


# Provider landscape without brand worship

Do not teach model names as a permanent ranking. Names, limits, and endpoints change. Teach capability questions that survive product churn: Does the API generate and edit? Does it accept multiple image references? Does it support masks? Is the workflow synchronous or asynchronous? What are the file formats, size limits, safety restrictions, usage rights, provenance metadata, price, latency, and enterprise controls?

As of the current source check, OpenAI documents image generation and editing through GPT Image models and the Images/Responses API paths; Google documents image generation and conversational image editing in the Gemini API/Nano Banana family; Adobe Firefly Services documents creative APIs for generation, alteration, upscaling and production creative workflows. Use provider docs on the day of teaching because this area changes quickly.

# Prompt anatomy for image APIs

• Subject: what must be in the image.

• Composition: camera angle, framing, distance, aspect ratio, foreground/background.

• Scene: environment, light, season, materials, atmosphere.

• Style: photo, illustration, editorial, ecommerce, diagram, comic, UI mockup.

• References: what should stay the same from each input image.

• Constraints: what must not change, what must not appear, output format expectations.

• Acceptance criteria: the checklist used to decide whether the image can be used.

# Example: weak vs professional prompt


# Live demo concept

The demo shows three rounds: first a weak prompt, then a structured prompt, then a controlled edit workflow with reference image, mask concept, acceptance criteria, and review checklist. The best teaching moment is not the prettiest picture. The best teaching moment is when students see how vague instructions cause random outputs and controlled instructions create assets that can enter a real workflow.

# Risk map

• Privacy: do not upload faces, student data, customer documents, private interiors, or unreleased products unless the environment allows it.

• Rights and copyright: do not ask for protected characters, living artists styles, trademarks, or copied campaign assets unless rights and policy allow it.

• Brand drift: generated assets can subtly change product shape, logos, packaging, colors, or claims.

• Misleading content: generated images can imply evidence, locations, people, quality, or events that are not real.

• Provenance: store prompts, inputs, model/provider, date, output hash, review status, and usage context.

• Cost and latency: image calls are heavier than text calls; design caching, retries, queues, and variant limits.

# Decision rule

Use an image generation API when the task benefits from visual variation, creative exploration, controlled asset production, or personalized content. Prefer normal design tools when the output needs exact layout, exact text, strict brand typography, or deterministic geometry. Use AI for exploration; use deterministic tools for final production when exactness matters.

# Student practice

Students create an Image Generation Workflow Spec for one real or realistic use case. The spec includes business goal, source assets, prompt, references, controls, acceptance criteria, review rules, metadata to store, and what must not be automated. This artifact can later become part of their capstone.

# Takeaways

• Image generation is workflow design, not magic prompt guessing.

• Reference images and masks are control tools, not decoration.

• Prompt quality matters, but acceptance criteria matter more.

• Generated images need review when they affect brand, trust, safety, rights, or revenue.

• APIs turn creative work into repeatable systems: request, generate, review, store, publish.



| Term | Plain meaning | Beginner example |
| --- | --- | --- |
| Text-to-image | Generate an image from a text instruction. | Create a hero image for a blog post. |
| Image-to-image | Use an existing image as input and transform it. | Turn a sketch into a polished product concept. |
| Inpainting | Edit a selected region inside an image. | Replace the background behind a mug. |
| Outpainting | Extend an image beyond its current borders. | Make a vertical poster from a square product photo. |
| Reference image | An image used to guide identity, style, layout, or composition. | Keep the same mug but change the scene. |
| Mask | A selected area that tells the model where it may or may not change pixels. | Protect the product, edit only the background. |
| Negative constraint | A clear instruction about what must not appear. | No extra fingers, no text, no logo changes. |
| Acceptance criteria | The rules used to decide whether the output is good enough. | Product unchanged, label readable, background natural. |



| Task | Best fit | Watch-outs |
| --- | --- | --- |
| Concept generation | Fast ideation, mood boards, thumbnail concepts. | Outputs vary; do not treat the first result as final. |
| Product-background editing | E-commerce, ads, marketplace images. | Product geometry and label integrity must be checked. |
| Style transfer | Campaign variants and creative exploration. | Brand consistency can drift. |
| Character or object consistency | Storyboards, educational visuals, game assets. | Harder than one-off generation; use references and acceptance checks. |
| Diagram or text-heavy graphics | Sometimes useful, but often safer with deterministic design tools. | Generated text can be wrong or ugly; use editable slides/design tools for critical labels. |
| Bulk generation | A/B testing and personalization. | Cost, latency, review queue, deduplication, and asset tracking matter. |



| Weak prompt | Professional workflow prompt |
| --- | --- |
| Make a nice image of this mug. | Using the uploaded product photo as the protected product reference, keep the mug shape, handle, ceramic texture, and visible logo unchanged. Replace only the background with a warm morning kitchen scene. Use soft natural light from the left, 16:9 crop, no text, no hands, no extra mugs. Return three variants. Acceptance: product must remain identical enough for ecommerce approval. |

