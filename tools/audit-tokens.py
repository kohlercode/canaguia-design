"""Audit DESIGN.md / theme.css / tokens.json / tailwind.theme.json color parity."""
from __future__ import annotations

import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]

dm = (root / "DESIGN.md").read_text(encoding="utf-8")
fm = dm.split("---", 2)[1]

design_hex = {
    k: v.lower()
    for k, v in re.findall(r'^  ([a-z0-9-]+):\s*"(#[0-9A-Fa-f]{6,8})"', fm, re.M)
}

RGBA = re.compile(
    r'^  ([a-z0-9-]+):\s*"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)"',
    re.M,
)


def rgba_to_hex8(r: str, g: str, b: str, a: str) -> str:
    # round-half-up so rgba(0,0,0,0.3) -> 0x4d, matching the exports
    alpha = int(float(a) * 255 + 0.5)
    return "#{:02x}{:02x}{:02x}{:02x}".format(
        int(r), int(g), int(b), alpha
    )


design = dict(design_hex)
for k, r, g, b, a in RGBA.findall(fm):
    design[k] = rgba_to_hex8(r, g, b, a)

css = (root / "theme.css").read_text(encoding="utf-8")
theme = {
    k: v.lower()
    for k, v in re.findall(r"--color-([a-z0-9-]+):\s*(#[0-9a-fA-F]+)", css)
}

tj = json.loads((root / "tokens.json").read_text(encoding="utf-8"))
tokens = {
    k: v["$value"]["hex"].lower()
    for k, v in tj["color"].items()
    if isinstance(v, dict) and "$value" in v and "hex" in v.get("$value", {})
}

tw = json.loads((root / "tailwind.theme.json").read_text(encoding="utf-8"))
twc = {k: v.lower() for k, v in tw["theme"]["extend"]["colors"].items()}

keys = sorted(set(design) | set(theme) | set(tokens) | set(twc))
bad = 0
for k in keys:
    vals = {design.get(k, ""), theme.get(k, ""), tokens.get(k, ""), twc.get(k, "")}
    vals.discard("")
    if len(vals) > 1:
        bad += 1
        print(
            f"MISMATCH {k}: design={design.get(k)} theme={theme.get(k)} "
            f"tokens={tokens.get(k)} tw={twc.get(k)}"
        )
    elif not (k in design and k in theme and k in tokens and k in twc):
        print(
            f"MISSING {k}: design={k in design} theme={k in theme} "
            f"tokens={k in tokens} tw={k in twc}"
        )
        bad += 1
print(f"checked {len(keys)} keys, {bad} issues")
raise SystemExit(1 if bad else 0)
