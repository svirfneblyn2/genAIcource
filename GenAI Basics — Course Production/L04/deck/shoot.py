"""Screenshots every slide of a deck (headless Edge, 1540x866) for visual QA.

    python deck/shoot.py [EN] [--slides 5 6 7] --out <dir>
"""

import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from build_deck import L04, NAME, find_edge


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("lang", nargs="?", default="RU")
    ap.add_argument("--slides", nargs="*", type=int)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    html = L04 / f"{NAME}{'_EN' if args.lang.upper() == 'EN' else ''}.html"
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    total = html.read_text(encoding="utf-8").count('<section class="slide')
    nums = args.slides or range(1, total + 1)
    edge = find_edge()

    def shot(n: int) -> None:
        subprocess.run([edge, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,900",
                        "--virtual-time-budget=4000", f"--user-data-dir={out / ('prof%d' % n)}",
                        f"--screenshot={out / f's{n:02d}.png'}", f"{html.as_uri()}#{n}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with ThreadPoolExecutor(6) as ex:
        list(ex.map(shot, nums))
    print("done", len(list(nums)))


if __name__ == "__main__":
    main()
