# Canaguia — DESIGN.md

Design system specification for **canaguia.com** and public Canaguia social content
(YouTube, Instagram, Facebook and shares), in the
[Google DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) format.

Drop `DESIGN.md` into a project root and any design-capable coding agent reads it as
the source of truth for how a page or creatives should look.

| File | Purpose |
|---|---|
| `DESIGN.md` | The specification. YAML front matter = normative tokens; markdown body = rationale and rules. |
| `preview.html` | Token and component catalog on the white canvas, plus a photo hero and social frame sample. |
| `theme.css` | Tailwind v4 `@theme` block. |
| `tailwind.theme.json` | Tailwind v3 theme JSON. |
| `tokens.json` | W3C DTCG (Design Tokens Format Module) export. |
| `assets/` | Brand asset library — lockup, mark, icons, video templates. See `assets/README.md`. |

## Assets

`assets/` holds the artwork. `DESIGN.md` keeps the **rules**; `assets/README.md` holds
the **inventory**. The split keeps `DESIGN.md` portable when copied alone into a
project.

## Use

1. Copy `DESIGN.md` into your project root.
2. Tell the agent: *"Build this page / ad using DESIGN.md as the design source of truth."*
3. For Tailwind, import `theme.css` or merge `tailwind.theme.json` into your config.

## Validate

```bash
npx -y @google/design.md lint DESIGN.md
npx -y @google/design.md export --format css-tailwind DESIGN.md
npx -y @google/design.md export --format dtcg DESIGN.md
python3 tools/audit-tokens.py
```

## Where the tokens came from

Extracted from the shipped canaguia.com stylesheet (Bootstrap 5 custom theme:
`--bs-primary: #007ed4`, `--bs-secondary: #ffae2a`, `--bs-body-font-family: "Poppins"`,
`--bs-border-radius: 1rem`, and the header logo SVG) and reconciled into this
normative document. Where the live site and this file disagree, the resolution is
recorded in **Known Gaps**.

## Scope

**In scope:** canaguia.com marketing surfaces, landing pages, article cards, and the
YouTube / Instagram / Facebook / share creatives that must stay on-brand.

**Out of scope (and must not appear in this public repo):** TYPO3 backend, editor
chrome, admin UI, analytics internals, or any hosting/theming specifics. Those live in
private repositories.

**Light-first** — the default canvas is white. Dark is reserved for the footer and the
photo-veiled hero, not a second full theme.

## Note before implementing

- **The brand is a photo-first travel guide.** Lead every surface with full-bleed
  Tenerife photography; never a flat colour poster.
- **Blue is action and brand.** Primary CTAs fill with `{colors.primary}` (#007ed4);
  amber (`{colors.secondary}` — #ffae2a) is a spark, not a button fill.
- **One lockup system.** Amber stays amber, blue stays blue in the mark. Do not invent
  a third logo colour for marketing.
- **No TYPO3 admin chrome or backend screenshots** in public creatives unless
  deliberately approved and cropped to the product story only.
