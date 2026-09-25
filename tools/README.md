# Tools

Utility scripts for regenerating brand deliverables. Marketing assets only —
nothing here compiles TYPO3 or product UI.

| Script | Purpose |
|---|---|
| `clean-mark.py` | Extract the two-tone mark from the lockup master; emit mono variants + `favicon.svg` |
| `clean-logo-lockup.py` | Normalise the lockup master (explicit fills); emit mono-ink / mono-white lockups |
| `audit-tokens.py` | Compare colour hexes across `DESIGN.md`, `theme.css`, `tokens.json`, `tailwind.theme.json` |

---

## Source masters

The scripts read the shipped masters under `assets/brand/logo/master/`. To re-derive
the mark from a fresh export of the header SVG, drop the raw lockup as
`canaguia-logo.svg` first, then run `clean-logo-lockup.py` and `clean-mark.py` in that
order.

## Audit

```bash
python3 tools/audit-tokens.py
```

Exits non-zero on any colour mismatch or missing key across the four token sources.
