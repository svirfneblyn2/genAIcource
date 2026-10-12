# -*- coding: utf-8 -*-
"""Prepare media for the L05 v2 decks (run once; safe to re-run).

    python make_media.py

Inputs : ../demo_veo_showcase/*.mp4 (Veo 3.1 clips, 1280x720, with audio) and a few
         existing images from ../assets/.
Outputs: ../assets/v2/video/*.mp4  (960x540, H.264 CRF 27, no audio, faststart)
         ../assets/v2/img/*.jpg    (posters, failure-gallery frames, QA frames, schematics)
Needs ffmpeg on PATH and Pillow. No generation, no network.
"""
import random
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter

L05 = Path(__file__).resolve().parent.parent
SRC = L05 / "demo_veo_showcase"
VID = L05 / "assets" / "v2" / "video"
IMG = L05 / "assets" / "v2" / "img"
VID.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

CLIPS = {  # out name -> source file
    "final": "courier_delivery_final.mp4",
    "trainwreck": "trainwreck_naive_t2v.mp4",
    "shot1": "shot1.mp4",
    "shot2": "shot2.mp4",
    "shot3": "shot3.mp4",
}

# (out jpg, clip, second, width)
FRAMES = [
    ("cover_shot2", "shot2", 2.0, 1600),
    ("poster_final", "final", 1.0, 960),
    ("poster_trainwreck", "trainwreck", 1.5, 960),
    ("poster_shot1", "shot1", 1.0, 960),
    ("poster_shot2", "shot2", 2.0, 960),
    ("poster_shot3", "shot3", 3.0, 960),
    ("tl_shot1", "shot1", 1.0, 480),
    ("tl_shot2", "shot2", 3.0, 480),
    ("tl_shot3", "shot3", 4.0, 480),
    ("fail_02_4", "trainwreck", 2.4, 960),
    ("fail_05_0", "trainwreck", 5.0, 960),
    ("qa_shot3_a", "shot3", 4.75, 960),
    ("qa_shot3_b", "shot3", 6.25, 960),
    ("qa_shot2_sign", "shot2", 6.25, 960),
]


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def grab(clip, sec, out, width=None):
    vf = ["-vf", f"scale={width}:-2"] if width else []
    run(["ffmpeg", "-y", "-ss", str(sec), "-i", str(SRC / CLIPS[clip]), "-frames:v", "1", *vf,
         "-q:v", "3", str(out)])


def encode():
    for name, src in CLIPS.items():
        run(["ffmpeg", "-y", "-i", str(SRC / src), "-vf", "scale=960:540", "-c:v", "libx264",
             "-preset", "slow", "-crf", "27", "-pix_fmt", "yuv420p", "-profile:v", "high",
             "-an", "-movflags", "+faststart", str(VID / f"{name}.mp4")])


def frames():
    for name, clip, sec, w in FRAMES:
        grab(clip, sec, IMG / f"{name}.jpg", w)
    tmp = IMG / "_tmp.jpg"
    # failure 2: details drift across the cut (backpack before / after), side by side
    grab("trainwreck", 1.5, tmp)
    a = Image.open(tmp).crop((40, 200, 440, 700))
    grab("trainwreck", 2.6, tmp)
    b = Image.open(tmp).crop((900, 150, 1260, 600))
    h = 500
    a = a.resize((round(a.width * h / a.height), h))
    b = b.resize((round(b.width * h / b.height), h))
    canvas = Image.new("RGB", (889, h), (5, 8, 14))
    gap = 889 - a.width - b.width
    canvas.paste(a, (0, 0))
    canvas.paste(b, (a.width + gap, 0))
    canvas.save(IMG / "fail_02_6_pair.jpg", quality=86)
    # failure 4: pseudo-text on the phone map, cropped
    grab("trainwreck", 7.0, tmp)
    Image.open(tmp).crop((328, 200, 968, 560)).resize((960, 540)).save(IMG / "fail_07_0.jpg", quality=86)
    tmp.unlink()


def schematic():
    """noise -> half-denoised (with patch grid) -> clean, 3 frames each (shot2 at 0/3/6 s)."""
    random.seed(7)
    tmp = IMG / "_tmp.jpg"
    for i, sec in enumerate([0.5, 3.5, 6.5]):
        grab("shot2", sec, tmp, 480)
        clean = Image.open(tmp).convert("RGB")
        w, hh = clean.size
        noise = Image.effect_noise((w, hh), 90).convert("RGB")
        tint = Image.merge("RGB", [Image.effect_noise((w, hh), 70) for _ in range(3)])
        noise = Image.blend(noise, tint, 0.5)
        half = Image.blend(clean.filter(ImageFilter.GaussianBlur(6)), noise, 0.55)
        noise.save(IMG / f"how_noise_{i}.jpg", quality=80)
        half.save(IMG / f"how_half_{i}.jpg", quality=80)
        clean.save(IMG / f"how_clean_{i}.jpg", quality=84)
    tmp.unlink()


def stills():
    a = L05 / "assets"
    jobs = [
        (a / "showcase" / "courier_sheet.png", "courier_sheet", 1376),
        (a / "showcase" / "motion_brush_demo.png", "motion_brush", 1280),
        (a / "workflow" / "knight_2d_sprite.png", "knight_sprite", None),
        (a / "workflow" / "knight_draft_render.png", "knight_draft", None),
        (a / "workflow" / "knight_approved_render.png", "knight_approved", None),
        (a / "showcase" / "d0_packshot.png", "packshot", 700),
    ]
    for src, name, w in jobs:
        im = Image.open(src).convert("RGB")
        if w and im.width > w:
            im = im.resize((w, round(im.height * w / im.width)))
        im.save(IMG / f"{name}.jpg", quality=86)


if __name__ == "__main__":
    encode()
    frames()
    schematic()
    stills()
    total = sum(p.stat().st_size for p in VID.glob("*.mp4"))
    for p in sorted(VID.glob("*.mp4")):
        print(f"{p.name:16s} {p.stat().st_size / 1e6:6.2f} MB")
    print(f"video total     {total / 1e6:6.2f} MB")
    print("images:", len(list(IMG.glob('*.jpg'))))
