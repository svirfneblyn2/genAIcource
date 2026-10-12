import sys
import os
from pathlib import Path

sys.path.append(r"tools")
from image_generator import generate_vertex_image

out_dir = Path(r"GenAI Basics — Course Production/L04/assets/hook")
out_dir.mkdir(parents=True, exist_ok=True)

prompts = [
    (
        "hook_1_gan2014.png",
        "Early 2014 computer vision GAN generated portrait face, Ian Goodfellow generative adversarial network style, low resolution, 64x64 pixelated blurry face, noisy gray artifacts, historical AI milestone",
    ),
    (
        "hook_2_stylegan2018.png",
        "2018 StyleGAN AI generated portrait of a person, realistic face but distinct early AI artifacts, asymmetrical melting ear and earring, distorted wavy background texture, uncanny valley",
    ),
    (
        "hook_3_sd2022.png",
        "2022 Stable Diffusion 1.5 portrait of a person, smooth plastic airbrushed skin, slightly unnatural specular eye reflections, early text-to-image diffusion aesthetic",
    ),
    (
        "hook_4_mj2023.png",
        "2023 Midjourney v5 cinematic portrait of a person, warm rim lighting, dramatic studio chiaroscuro, stylized color grading, sharp focus, magazine editorial aesthetic",
    ),
    (
        "hook_5_flux2024.png",
        "2024 FLUX.1 hyper-realistic portrait of a real person, visible skin pores, natural imperfections, authentic hair strands, soft natural daylight, photorealism",
    ),
    (
        "hook_6_banana2026.png",
        "2026 Nano Banana Pro candid smartphone portrait of a person in a bright coffee shop, natural optical bokeh, authentic imperfections, indistinguishable from a real photograph",
    ),
]

for filename, prompt in prompts:
    dest = out_dir / filename
    if not dest.exists():
        print(f"Generating {filename}...")
        try:
            generate_vertex_image(prompt=prompt, output_path=str(dest), aspect_ratio="1:1")
            print(f"Saved {dest}")
        except Exception as e:
            print(f"Failed {filename}: {e}")
    else:
        print(f"Already exists: {dest}")
