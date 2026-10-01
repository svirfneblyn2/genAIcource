import subprocess, os, sys
from pathlib import Path
import fitz

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
work_dir = Path(r"d:\Repos\genAIcource\GenAI Basics — Course Production\L04")

def to_file_url(p: Path, hash_tag=""):
    url = p.as_uri()
    if hash_tag:
        url += f"#{hash_tag}"
    return url

# 1. Export Russian PDF
pdf_ru = work_dir / "presentation_L04_Image_Generation_APIs.pdf"
html_ru = work_dir / "presentation_L04_Image_Generation_APIs.html"
print("Exporting Russian PDF via Chrome...")
subprocess.run([chrome, "--headless=new", "--disable-gpu", f"--print-to-pdf={pdf_ru}", "--no-pdf-header-footer", html_ru.as_uri()], check=True)
doc_ru = fitz.open(pdf_ru)
print(f"[OK] RU PDF: {pdf_ru.name} - {len(doc_ru)} pages, {pdf_ru.stat().st_size:,} bytes")
doc_ru.close()

# 2. Export English PDF
pdf_en = work_dir / "presentation_L04_Image_Generation_APIs_EN.pdf"
html_en = work_dir / "presentation_L04_Image_Generation_APIs_EN.html"
print("Exporting English PDF via Chrome...")
subprocess.run([chrome, "--headless=new", "--disable-gpu", f"--print-to-pdf={pdf_en}", "--no-pdf-header-footer", html_en.as_uri()], check=True)
doc_en = fitz.open(pdf_en)
print(f"[OK] EN PDF: {pdf_en.name} - {len(doc_en)} pages, {pdf_en.stat().st_size:,} bytes")
doc_en.close()

# 3. Capture Screenshots (RU and EN key slides)
screenshots = [
    ("screenshot_slide01.png", html_ru, "1"),
    ("screenshot_slide07.png", html_ru, "7"),
    ("screenshot_slide11.png", html_ru, "11"),
    ("screenshot_slide12.png", html_ru, "12"),
    ("screenshot_slide15.png", html_ru, "15"),
    ("screenshot_slide16.png", html_ru, "16"),
    ("screenshot_en_slide01.png", html_en, "1"),
    ("screenshot_en_slide05.png", html_en, "5"),
    ("screenshot_en_slide07.png", html_en, "7"),
    ("screenshot_en_slide18.png", html_en, "18"),
]

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
for out_name, html_file, hash_tag in screenshots:
    out_file = work_dir / out_name
    target_url = to_file_url(html_file, hash_tag)
    subprocess.run([edge, "--headless", "--disable-gpu", "--window-size=1540,866", f"--screenshot={out_file}", target_url], check=True)
    print(f"[OK] Screenshot {out_name}: {out_file.stat().st_size:,} bytes")

print("[COMPLETED] All PDFs and screenshots exported and verified!")
