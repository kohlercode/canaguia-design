"""Extract the two-tone mark from the lockup; emit mono variants + favicon.svg.

The mark is the abstract sun-and-sea symbol (amber over blue). The wordmark is
discarded. The tight viewBox was computed from the mark's local bounding box.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "assets" / "brand" / "logo" / "master"
ICONS = ROOT / "assets" / "brand" / "icons"
SRC = MASTER / "canaguia-logo.svg"

AMBER = "#ffae2a"
BLUE = "#007ed4"
INK = "#212529"
WHITE = "#ffffff"

MARK_VIEWBOX = "3.512 3.274 92.861 72.823"


def extract(src: str) -> list[tuple[str, str]]:
    inner = re.search(r'<g transform="matrix\([^"]*\)">(.*?)</g>', src, re.S)
    if not inner:
        raise SystemExit("mark <g> not found in source lockup")
    return re.findall(r'<path fill="(#[0-9a-fA-F]+)" d="([^"]+)"', inner.group(1))


def emit(paths: list[tuple[str, str]], inks: dict[str, str], dest: Path) -> None:
    body = "\n".join(f'  <path fill="{inks.get(f, f)}" d="{d}"/>' for f, d in paths)
    dest.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{MARK_VIEWBOX}" role="img" aria-label="Canaguia">\n'
        f"{body}\n"
        '</svg>\n',
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    paths = extract(SRC.read_text(encoding="utf-8"))
    if len(paths) < 6:
        raise SystemExit(f"expected 6 mark paths, got {len(paths)}")
    paths = [(AMBER if f.upper() == "#FFAE2A" else BLUE if f.upper() == "#007ED4" else f, d) for f, d in paths]

    emit(paths, {}, MASTER / "canaguia-mark.svg")
    emit(paths, {AMBER: INK, BLUE: INK}, MASTER / "canaguia-mark-mono-ink.svg")
    emit(paths, {AMBER: WHITE, BLUE: WHITE}, MASTER / "canaguia-mark-mono-white.svg")
    emit(paths, {}, ICONS / "favicon.svg")
    print(f"extracted mark: {[f for f, _ in paths]} -> mark + mono + favicon")


if __name__ == "__main__":
    main()
