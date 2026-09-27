# GenAI Course Production — Rules & Tools

## Image Generation Policy (Vertex AI / Nano Banana Pro)

When generating images, concept art, diagrams, slides, or visuals:
- Do NOT use the built-in IDE `generate_image` tool due to tight free-tier quota limits (429 Quota Exhausted).
- ALWAYS generate images via Vertex AI (`gemini-3-pro-image` / Nano Banana Pro) using our connected Google Cloud service account.
- Service Account Credentials: `GOOGLE_VERTEX_CREDENTIALS` (`D:\Repos\dark-factory\dark-factory-lab\secrets\vertex-sa.json`, project `eatzy-503209`, location `global`).
- CLI tool:
  ```bash
  python tools/image_generator.py --prompt "<PROMPT>" --output "<OUTPUT_PATH>" [--aspect-ratio 16:9|1:1|4:3|9:16] [--ref "<REF_IMAGE>"]
  ```
- Or global tool: `python D:\tools\image_generator.py ...`
- In Python:
  ```python
  from tools.image_generator import generate_vertex_image
  generate_vertex_image(prompt="...", output_path="...", aspect_ratio="16:9")
  ```
