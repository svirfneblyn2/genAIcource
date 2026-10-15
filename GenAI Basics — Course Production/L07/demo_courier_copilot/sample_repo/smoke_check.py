from pathlib import Path
import subprocess
import sys

root = Path(__file__).parent
required = ["delivery_fee.py", "test_delivery_fee.py", "ISSUE.md", ".github/copilot-instructions.md"]
for f in required:
    p = root / f
    if not p.exists():
        raise SystemExit(f"Missing fixture: {p}")
print("FIXTURES OK")
r = subprocess.run([sys.executable, "-m", "unittest", "-q"], cwd=root, text=True, capture_output=True)
print(r.stdout.strip() or r.stderr.strip())
if r.returncode:
    raise SystemExit(r.returncode)
print("BASELINE TESTS PASS")
