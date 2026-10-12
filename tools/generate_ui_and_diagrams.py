import sys
import os
from pathlib import Path

sys.path.append(r"tools")
from image_generator import generate_vertex_image

ui_dir = Path(r"GenAI Basics — Course Production/L04/assets/ui")
assets_dir = Path(r"GenAI Basics — Course Production/L04/assets")

tasks = [
    (
        ui_dir / "leonardo.jpg",
        "Modern clean UI screenshot of Leonardo.ai creative suite web application, dark engineering theme #0b0f17, left control sidebar with Prompt Generation, Guidance Scale, Negative Prompt input, style presets, center canvas with high quality generated image, crisp interface",
        "4:3"
    ),
    (
        ui_dir / "sintx.jpg",
        "Modern clean UI screenshot of Sintx creative AI aggregator platform, dark engineering theme, multi-model switcher dropdown showing FLUX.1, Midjourney, Stable Diffusion, prompt bar and gallery cards, sleek SaaS dashboard",
        "4:3"
    ),
    (
        assets_dir / "visual_ai_ecosystem_layers.png",
        "Technical C4 architecture diagram showing three tiers of Visual Generative AI: Tier 1 Foundation Providers & Raw APIs (Google Imagen, OpenAI DALL-E, Black Forest Labs FLUX, Stability SD), Tier 2 Creative SaaS Aggregators & Proxies (Leonardo.ai, Kling, Sintx, Krea), Tier 3 Multimodal Conversational UI (ChatGPT, Gemini). Dark engineering theme #0b0f17, cyan and emerald node borders, crisp English labels, system architecture flow",
        "16:9"
    )
]

for dest, prompt, ar in tasks:
    if not dest.exists():
        print(f"Generating {dest.name}...")
        try:
            generate_vertex_image(prompt=prompt, output_path=str(dest), aspect_ratio=ar)
            print(f"Saved {dest}")
        except Exception as e:
            print(f"Failed {dest.name}: {e}")
    else:
        print(f"Already exists: {dest}")
