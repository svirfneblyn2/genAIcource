# -*- coding: utf-8 -*-
"""Produce the real artifacts for slides 11-13: git diff and unittest output.

    python make_artifacts.py

Copies demo_courier_copilot/sample_repo to a temp dir, commits the base, applies
expected_solution/, captures `git diff --no-color` and `python -m unittest -v`,
and writes artifacts.json next to this file. build.py reads that file only.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent / "demo_courier_copilot" / "sample_repo"


def run(cmd, cwd, **kw):
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, encoding="utf-8", **kw)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="l07_art_"))
    try:
        work = tmp / "repo"
        shutil.copytree(REPO, work, ignore=shutil.ignore_patterns("expected_solution", "__pycache__"))
        git = ["git", "-c", "user.name=Demo", "-c", "user.email=demo@example.com"]
        run(["git", "init", "-q"], work)
        run(git + ["add", "-A"], work)
        run(git + ["commit", "-q", "-m", "base"], work)
        base = run([sys.executable, "-m", "unittest", "-v"], work)
        for f in (REPO / "expected_solution").glob("*.py"):
            shutil.copy(f, work / f.name)
        diff = run(["git", "diff", "--no-color", "--no-ext-diff"], work).stdout
        diff_u1 = run(["git", "diff", "--no-color", "--no-ext-diff", "-U1"], work).stdout
        res = run([sys.executable, "-m", "unittest", "-v"], work)
        out = res.stderr  # unittest writes to stderr
        m = re.search(r"Ran (\d+) tests?", out)
        base_m = re.search(r"Ran (\d+) tests?", base.stderr)
        assert res.returncode == 0 and "OK" in out, out
        files, cur = {}, None
        for line in diff.splitlines():
            if line.startswith("diff --git"):
                cur = line.split(" b/")[-1]
                files[cur] = {"added": 0, "removed": 0}
            elif cur and line.startswith("+") and not line.startswith("+++"):
                files[cur]["added"] += 1
            elif cur and line.startswith("-") and not line.startswith("---"):
                files[cur]["removed"] += 1
        art = {
            "diff": diff,
            "diff_u1": diff_u1,
            "tests": [{"name": n, "result": r} for n, r in re.findall(r"^(test_\w+) \(.*\) \.\.\. (\w+)$", out, flags=re.M)],
            "test_output": out,
            "tests_total": int(m.group(1)),
            "tests_baseline": int(base_m.group(1)),
            "tests_ok": res.returncode == 0,
            "tests_new": int(m.group(1)) - int(base_m.group(1)),
            "files": files,
            "logic_added": files["delivery_fee.py"]["added"],
            "logic_removed": files["delivery_fee.py"]["removed"],
            "tests_added_lines": files["test_delivery_fee.py"]["added"],
            "ok_lines": len(re.findall(r"\.\.\. ok$", out, flags=re.M)),
        }
        (HERE / "artifacts.json").write_text(json.dumps(art, ensure_ascii=False, indent=2), encoding="utf-8")
        print("tests:", art["tests_total"], "ok" if art["tests_ok"] else "FAIL", "| baseline", art["tests_baseline"],
              "| logic +%d -%d" % (art["logic_added"], art["logic_removed"]), "| test lines +%d" % art["tests_added_lines"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
