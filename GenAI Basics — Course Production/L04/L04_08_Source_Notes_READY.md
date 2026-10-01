Lecture 04 — Source Notes

Official sources checked 08 Sep 2026; volatile facts isolated here


# OpenAI

OpenAI API model catalog — current specialized image family includes GPT-Image-2.
https://platform.openai.com/docs/models

# Google Gemini API

Image generation and editing documentation. Current examples use Gemini 3.1 Flash Image for text-to-image and text+image editing with the Interactions API.
https://ai.google.dev/gemini-api/docs/image-generation

# Google Cloud / Vertex AI

Generative AI release notes. February 26, 2026 notes Gemini 3.1 Flash Image public preview and recommends it for image generation; older image preview endpoints were deprecated/replaced. Imagen 4 GA endpoints are also documented.
https://cloud.google.com/vertex-ai/generative-ai/docs/release-notes

# Microsoft Foundry / Azure OpenAI

Image generation how-to. Important current note: DALL-E 3 was retired March 4, 2026; guidance says to use gpt-image-series models for image generation instead.
https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e

# Adobe Firefly Services

Image5 generation guide: Image5 supports text-to-image and image-to-image instruct edit through the Generate Image API.
https://developer.adobe.com/firefly-services/docs/firefly-api/guides/how-tos/cm-generate-image/feature-guide

Style reference concept: style references guide look/feel; the docs expose a provider-specific strength control.
https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/

Firefly API changelog: current API evolution, including async image operations and later Image5 changes.
https://developer.adobe.com/firefly-services/docs/firefly-api/getting-started/changelog/

Photoshop API overview: v1 reached end of life July 31, 2026; v2 is the current platform.
https://developer.adobe.com/firefly-services/docs/photoshop/

# Volatile facts deliberately kept out of the core teaching

- Exact per-image prices and rate limits are not embedded in student slides. They change faster than the conceptual lesson.
- Model IDs are examples checked on 08 Sep 2026 and must be re-verified before a future delivery.
- Provider-specific controls (for example reference “strength”) are taught as examples, not universal API fields.
- No permanent “best model” ranking is asserted. Provider comparison is framed around workflow capability and integration needs.
