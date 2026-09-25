"""Normalise the Canaguia lockup master and emit mono ink/white variants.

The two-tone rule is fixed: amber stays amber (#ffae2a), blue stays blue (#007ed4),
wordmark is blue. Mono variants recolor everything to a single ink.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "assets" / "brand" / "logo" / "master"
SRC = MASTER / "canaguia-logo.svg"

AMBER = "#ffae2a"
BLUE = "#007ed4"
INK = "#212529"
WHITE = "#ffffff"

VIEWBOX = "0 0 79.374998 26.458333"


def parse(src: str) -> tuple[list[tuple[str, str]], str]:
    """Return [(fill, d), ...] for the mark paths plus the wordmark d string."""
    inner = re.search(r'<g transform="matrix\([^"]*\)">(.*?)</g>', src, re.S)
    if not inner:
        raise SystemExit("mark <g> not found in source lockup")
    mark = re.findall(r'<path fill="(#[0-9a-fA-F]+)" d="([^"]+)"', inner.group(1))
    # wordmark is the first path after the mark's closing </g>
    rest = src[inner.end():]
    word = re.search(r'<path[^>]*d="([^"]+)"', rest)
    if not word:
        raise SystemExit("wordmark path not found in source lockup")
    return mark, word.group(1)


def normalize(fill: str) -> str:
    f = fill.upper()
    if f == "#FFAE2A":
        return AMBER
    if f == "#007ED4":
        return BLUE
    return fill


def emit(mark: list[tuple[str, str]], word: str, mark_inks: dict[str, str], word_fill: str, dest: Path) -> None:
    mark_body = "\n".join(
        f'      <path fill="{mark_inks.get(f, f)}" d="{d}"/>' for f, d in mark
    )
    dest.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VIEWBOX}" role="img" aria-label="Canaguia">\n'
        '  <g transform="translate(0.514224,0.19583525)">\n'
        '    <g transform="matrix(0.27809094,0,0,0.27809094,3.1858172,1.8574537)">\n'
        f"{mark_body}\n"
        '    </g>\n'
        f'    <path fill="{word_fill}" d="{word}"/>\n'
        '  </g>\n'
        '</svg>\n',
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    mark, word = parse(SRC.read_text(encoding="utf-8"))
    if len(mark) < 6:
        raise SystemExit(f"expected 6 mark paths, got {len(mark)}")
    mark = [(normalize(f), d) for f, d in mark]

    emit(mark, word, {}, BLUE, MASTER / "canaguia-logo.svg")
    emit(mark, word, {AMBER: INK, BLUE: INK}, INK, MASTER / "canaguia-logo-mono-ink.svg")
    emit(mark, word, {AMBER: WHITE, BLUE: WHITE}, WHITE, MASTER / "canaguia-logo-mono-white.svg")
    print(f"cleaned lockup: {[f for f, _ in mark]} -> color + mono ink/white")


if __name__ == "__main__":
    main()
