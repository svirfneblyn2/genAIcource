# Master Build and PDF Export Automation Script for Module 02
import os
import re
import sys
import shutil
import subprocess
import fitz

from .slides import ALL_SLIDES
from .template import render_deck

BANNED_SLOP = [
    r"\bdelve\b", r"\btestament\b", r"\btapestry\b", r"\bunleash\b",
    r"\bseamless\b", r"\bgame-changer\b", r"\brevolutionary\b", r"\bpivotal\b",
    r"\bbeacon\b", r"\bcornerstone\b", r"\bfoster\b", r"\bembark\b",
    r"\bfurthermore\b", r"it is important to note", r"in conclusion", r"let us explore"
]

def build():
    print("================================================================================")
    print("STARTING ADVANCED GENAI MODULE 02 BUILD & EXPORT PIPELINE")
    print("================================================================================")

    total = len(ALL_SLIDES)
    print(f"Step 1: Loaded {total} modular slides.")
    if total != 27:
        raise ValueError(f"Expected exactly 27 slides, but found {total}!")

    # Step 2: Render standalone HTML
    print("Step 2: Rendering standalone HTML presentation...")
    html_content = render_deck(ALL_SLIDES)
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_output_path = os.path.join(MODULE_DIR, "presentation_M02_Agent_Frameworks.html")

    # Step 3: Strict Regex Validation for zero em-dashes and en-dashes
    print("Step 3: Validating editorial punctuation integrity...")
    em_dash_matches = [m.start() for m in re.finditer(r"\u2014|—|&mdash;|&#8212;", html_content)]
    en_dash_matches = [m.start() for m in re.finditer(r"\u2013|–|&ndash;|&#8211;", html_content)]

    if em_dash_matches:
        for pos in em_dash_matches[:5]:
            snippet = html_content[max(0, pos-40):min(len(html_content), pos+40)]
            print(f"  [ERROR] Em-dash found at pos {pos}: ...{snippet}...")
        raise ValueError(f"Punctuation check failed: {len(em_dash_matches)} em-dashes found!")

    if en_dash_matches:
        for pos in en_dash_matches[:5]:
            snippet = html_content[max(0, pos-40):min(len(html_content), pos+40)]
            print(f"  [ERROR] En-dash found at pos {pos}: ...{snippet}...")
        raise ValueError(f"Punctuation check failed: {len(en_dash_matches)} en-dashes found!")

    print("  [SUCCESS] Zero em-dashes and zero en-dashes confirmed.")

    # Step 3B: Anti-slop vocabulary check
    print("Step 3B: Validating anti-slop vocabulary rules...")
    slop_violations = []
    for pattern in BANNED_SLOP:
        matches = list(re.finditer(pattern, html_content, re.IGNORECASE))
        if matches:
            for m in matches[:3]:
                snippet = html_content[max(0, m.start()-30):min(len(html_content), m.end()+30)]
                slop_violations.append(f"Pattern '{pattern}': ...{snippet}...")

    if slop_violations:
        for v in slop_violations:
            print(f"  [ERROR] Banned AI-slop vocabulary found: {v}")
        raise ValueError(f"Anti-slop check failed: {len(slop_violations)} violations found!")

    print("  [SUCCESS] Anti-slop check passed cleanly.")

    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [SUCCESS] Wrote HTML deliverable to: {html_output_path} ({len(html_content)} bytes)")

    # Step 4: Execute Headless Chrome for 16:9 Vector PDF Export
    pdf_output_path = os.path.join(MODULE_DIR, "presentation_M02_Agent_Frameworks.pdf")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    if not os.path.exists(chrome_path):
        raise FileNotFoundError(f"Chrome executable not found at: {chrome_path}")

    print(f"Step 4: Launching Headless Chrome to export vector PDF...")
    chrome_cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_output_path}",
        "--no-pdf-header-footer",
        html_output_path
    ]
    res = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Chrome PDF export failed with code {res.returncode}: {res.stderr}")
    print(f"  [SUCCESS] Chrome exported PDF to: {pdf_output_path}")

    # Step 5: Verify with PyMuPDF (fitz)
    print("Step 5: Verifying PDF dimensions and page count using PyMuPDF...")
    doc = fitz.open(pdf_output_path)
    page_count = len(doc)
    print(f"  Total Pages: {page_count} (Expected: 27)")
    if page_count != 27:
        doc.close()
        raise ValueError(f"PDF page count mismatch: Expected 27, got {page_count}")

    for i, page in enumerate(doc):
        w = round(page.rect.width, 1)
        h = round(page.rect.height, 1)
        ratio = round(w / h, 4)
        if abs(w - 1440.0) > 2.0 or abs(h - 810.0) > 2.0:
            doc.close()
            raise ValueError(f"Page {i+1} dimension mismatch: {w} x {h} pt (Expected: 1440.0 x 810.0 pt)")
    doc.close()
    print("  [SUCCESS] All 27 pages verified at exact 1440x810 pt (16:9 vector ratio).")

    # Step 6: Deploy to Google Drive Production Folder
    dest_dir = r"G:\My Drive\Advanced GenAI — Course Production\M02 — Agent Frameworks and Orchestration — DONE"
    print(f"Step 6: Copying deliverables to Google Drive folder:\n  {dest_dir}")
    if os.path.exists(dest_dir):
        dest_html = os.path.join(dest_dir, os.path.basename(html_output_path))
        dest_pdf = os.path.join(dest_dir, os.path.basename(pdf_output_path))
        shutil.copy2(html_output_path, dest_html)
        shutil.copy2(pdf_output_path, dest_pdf)
        print(f"  [SUCCESS] Copied HTML: {dest_html} ({os.path.getsize(dest_html)} bytes)")
        print(f"  [SUCCESS] Copied PDF:  {dest_pdf} ({os.path.getsize(dest_pdf)} bytes)")
    else:
        print(f"  [WARNING] Destination directory {dest_dir} does not exist. Skipping copy.")

    print("================================================================================")
    print("MODULE 02 BUILD & EXPORT COMPLETE: ALL CRITERIA SATISFIED!")
    print("================================================================================")

if __name__ == "__main__":
    build()
