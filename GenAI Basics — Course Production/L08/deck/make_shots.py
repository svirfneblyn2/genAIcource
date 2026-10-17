# -*- coding: utf-8 -*-
"""Crop the real ChatGPT run screenshots (assets/v2/chat/) into slide-sized frames (assets/v2/shots/).

    python make_shots.py

Source frames: real run on demo_v2/northstar_2025.xlsx, October 2026. Crops only, no retouching.
"""
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "assets" / "v2" / "chat"
OUT = HERE.parent / "assets" / "v2" / "shots"
OUT.mkdir(parents=True, exist_ok=True)

# name: (source file, (left, top, right, bottom))
CROPS = {
    "p1_problems": ("gpt_p1_problems.jpg", (400, 40, 1180, 515)),
    "p1_questions": ("gpt_p1_questions.jpg", (400, 215, 1180, 495)),
    "p2_roas_chat": ("gpt_p2_roas_chart_sheet.jpg", (60, 50, 528, 568)),
    "p2_roas_sheet": ("gpt_p2_roas_table.jpg", (533, 55, 1536, 435)),
    "p2_sales_sheet": ("gpt_p2_roas_chart_sheet.jpg", (533, 55, 1340, 695)),
    "p3_heatmap": ("gpt_p3_heatmap.jpg", (512, 185, 1076, 512)),
    "p3_themes_before": ("gpt_p3_themes_before.jpg", (425, 148, 1163, 462)),
    "p3_caveat": ("gpt_p3_examples_caveat.jpg", (400, 165, 1180, 530)),
    "p4_themes_after": ("gpt_p4_themes_after.jpg", (64, 64, 1508, 628)),
    "p4_what_changed": ("gpt_p4_what_changed.jpg", (400, 185, 1180, 600)),
    "p5_fake_preview": ("gpt_p5_fake_report_preview.jpg", (230, 52, 1306, 662)),
    "p5_report_top": ("gpt_p5_report_top_script.jpg", (622, 96, 1438, 695)),
    "p5_report_bottom": ("gpt_p5_report_bottom.jpg", (622, 180, 1438, 320)),
    "p5_script": ("gpt_p5_report_top_script.jpg", (60, 290, 530, 590)),
    "p5_answer": ("gpt_p5_report_answer_small.jpg", (200, 80, 640, 305)),
}

# bad / good runs, ChatGPT, 2026-10-17 (assets/v2/chat_badgood/)
BG = {
    "b0_paste": ("b0_nocode_paste.jpg", (640, 40, 1180, 495)),
    "b0_answer": ("b0_nocode_answer.jpg", (400, 40, 1180, 420)),
    "b1_top": ("b1_insights_top.jpg", (250, 90, 1030, 505)),
    "b1_chart": ("b1_insights_chart.jpg", (250, 150, 1030, 505)),
    "b1_mid": ("b1_insights_mid.jpg", (250, 130, 1030, 380)),
    "b1_dup": ("b1_insights_dup.jpg", (250, 225, 1030, 305)),
    "b3_bad": ("b3_growth_both.jpg", (250, 118, 1030, 215)),
    "b3_goodq": ("b3_growth_both.jpg", (480, 225, 1030, 355)),
    "b3_good": ("b3_growth_both.jpg", (250, 395, 1030, 540)),
    "b3_table": ("b3_growth_good_table.jpg", (250, 40, 1030, 565)),
    "b5_top": ("b5_social_top.jpg", (250, 80, 1030, 370)),
    "b5_reco": ("b5_social_reco.jpg", (250, 60, 1030, 560)),
}
BGSRC = HERE.parent / "assets" / "v2" / "chat_badgood"
CROPS.update({k: (str(BGSRC / f), b) for k, (f, b) in BG.items()})

for name, (src, box) in CROPS.items():
    im = Image.open(SRC / src).convert("RGB").crop(box)
    if name == "p5_answer":
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    im.save(OUT / f"{name}.jpg", quality=88)
    print(name, im.size)
