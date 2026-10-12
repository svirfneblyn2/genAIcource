"""Builds the L04 decks (RU + EN) from one source of truth.

    python deck/build_deck.py            # writes presentation_L04_*.html (RU/EN)
    python deck/build_deck.py --pdf      # + PDFs via headless Edge

Slides live in slides_v2.py (layout + short on-slide text); speaker notes are reused
from the v1 modules (slides*.py). Images come from assets/examples/*.png
(examples/build_examples.py) and are down-scaled to assets/examples/web/*.jpg.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from slides import set_lang
from slides_v3 import SLIDES

HERE = Path(__file__).resolve().parent
L04 = HERE.parent
SRC = L04 / "assets" / "examples"
WEB = SRC / "web"
NAME = "presentation_L04_Image_Generation_Services_and_Prompts"

UI = {
    "ru": dict(start="СТАРТ 5 МИН", pause="ПАУЗА", done="ВРЕМЯ ВЫШЛО", notes="ЗАМЕТКИ СПИКЕРА",
               title="Урок 04: Генерация изображений | GenAI Basics", foot="GenAI Basics • Урок 04 • Генерация изображений",
               hint="← → • N заметки • G слайды"),
    "en": dict(start="START 5 MIN", pause="PAUSE", done="TIME'S UP", notes="SPEAKER NOTES",
               title="Lesson 04: Image Generation | GenAI Basics", foot="GenAI Basics • Lesson 04 • Image Generation",
               hint="← → • N notes • G slides"),
}


def build_web_images() -> None:
    import numpy as np
    from PIL import Image

    WEB.mkdir(parents=True, exist_ok=True)
    for png in sorted(SRC.glob("*.png")):
        out = WEB / (png.stem + ".jpg")
        if out.exists() and out.stat().st_mtime >= png.stat().st_mtime:
            continue
        im = Image.open(png).convert("RGB")
        im.thumbnail((1400, 1400))
        im.save(out, "JPEG", quality=84, optimize=True, progressive=True)

    # diffusion illustration for slide 4: A2_structured blended with Gaussian noise
    base = np.asarray(Image.open(SRC / "A2_structured.png").convert("RGB").resize((640, 360))).astype(float) / 255
    noise = np.random.default_rng(7).normal(0.5, 0.28, base.shape).clip(0, 1)
    for i, level in enumerate([1.0, 0.75, 0.45, 0.0]):
        frame = (1 - level) * base + level * noise
        Image.fromarray((frame * 255).astype("uint8")).save(WEB / f"denoise_{i}.jpg", quality=85)


def render(lang: str) -> str:
    set_lang(lang)
    ui = UI[lang]
    css = (HERE / "deck_v2.css").read_text(encoding="utf-8")
    js = (HERE / "deck_v2.js").read_text(encoding="utf-8")
    total = len(SLIDES)
    pages = []
    for i, fn in enumerate(SLIDES, 1):
        s = fn()
        if s.get("raw"):
            inner = s["body"]
        else:
            k = f' style="--k:{s["k"]}"' if s.get("k") else ""
            lead = f'<p class="lead">{s["lead"]}</p>' if s.get("lead") else ""
            inner = f'<div class="kicker"{k}>{s["kicker"]}</div><h2 class="title">{s["title"]}</h2>{lead}<div class="body">{s["body"]}</div>'
        foot = "" if s.get("cls") == "cover" else f'<div class="foot"><span>{ui["foot"]}</span><span>{i:02d} / {total}</span></div>'
        pages.append(f'\n<section class="slide {s.get("cls", "")}" data-n="{i}">{inner}{foot}<template class="notes">{s["notes"]}</template></section>')

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ui['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<main class="stage" id="stage">{''.join(pages)}
</main>
<aside class="drawer" id="drawer"><div class="hd"></div><div class="tx"></div></aside>
<div class="grid" id="grid"></div>
<script>
const T = {{start: {ui['start']!r}, pause: {ui['pause']!r}, done: {ui['done']!r}, notes: {ui['notes']!r}}};
{js}
</script>
</body>
</html>
"""


def find_edge() -> str:
    for c in [shutil.which("msedge"),
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]:
        if c and Path(c).exists():
            return c
    sys.exit("msedge not found")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true")
    args = ap.parse_args()
    build_web_images()
    for lang, suffix in (("ru", ""), ("en", "_EN")):
        out = L04 / f"{NAME}{suffix}.html"
        out.write_text(render(lang), encoding="utf-8")
        print("wrote", out.name)
        if args.pdf:
            pdf = out.with_suffix(".pdf")
            subprocess.run([find_edge(), "--headless", "--disable-gpu", "--no-margins",
                            "--no-pdf-header-footer", "--virtual-time-budget=10000",
                            f"--print-to-pdf={pdf}", out.as_uri()], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("wrote", pdf.name)


if __name__ == "__main__":
    main()
