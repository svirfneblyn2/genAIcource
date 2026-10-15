# -*- coding: utf-8 -*-
"""Crops of the real claude.ai screenshots (assets/screens/*.jpg) for the deck.

    python make_screens.py

Screens were captured 2026-10-13 in the author's claude.ai account (Max plan, Opus 5.5),
with chat history and personal items blurred. Output: assets/img/scr_*.jpg.
"""
from pathlib import Path

from PIL import Image

L09 = Path(__file__).resolve().parent.parent
SRC = L09 / "assets" / "screens"
OUT = L09 / "assets" / "img"

# name: (source file, crop box or None)
CROPS = {
    "main": ("01_main.jpg", (0, 0, 1250, 490)),
    "models": ("02_models.jpg", (560, 140, 1260, 490)),
    "connectors": ("04_connectors.jpg", (592, 200, 1100, 720)),
    "code": ("05_code.jpg", (0, 0, 1310, 730)),
    "prompt_csv": ("06_prompt_csv.jpg", (592, 318, 1232, 562)),
    "permission": ("07_connector_permission.jpg", (526, 170, 1298, 240)),
    "permission_btn": ("07_connector_permission.jpg", (526, 480, 1298, 528)),
    "privacy": ("08_privacy.jpg", (448, 60, 1280, 450)),
    "capabilities": ("09_capabilities.jpg", (448, 370, 1280, 620)),
    "slides": ("10_slides.jpg", (288, 0, 1536, 674)),
    "design": ("11_design.jpg", (288, 0, 1536, 674)),
    "docs": ("13_docs_edit.jpg", (288, 0, 1536, 674)),
    "diagram": ("14_diagram.jpg", (718, 0, 1530, 674)),
    "share": ("15_share.jpg", (1082, 52, 1517, 465)),
    "export": ("16_export.jpg", (1082, 52, 1517, 660)),
    "app": ("17_app.jpg", (288, 0, 1536, 674)),
    "dashboard": ("18_dashboard.jpg", (718, 0, 1530, 674)),
    "dashboard_chat": ("18b_dashboard_building.jpg", (288, 0, 1536, 730)),
    "project": ("19_project.jpg", (288, 0, 1536, 500)),
    "dash_slides": ("20_dashboard_slides.jpg", (718, 0, 1530, 674)),
    "artifacts_tab": ("21_artifacts_tab.jpg", (288, 40, 1536, 674)),
    "gallery": ("22_gallery.jpg", (400, 180, 1410, 674)),
}

if __name__ == "__main__":
    for name, (src, box) in CROPS.items():
        im = Image.open(SRC / src).convert("RGB")
        if box:
            im = im.crop(box)
        im.save(OUT / f"scr_{name}.jpg", quality=90)
        print(name, im.size)
