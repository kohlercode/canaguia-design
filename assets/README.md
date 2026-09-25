# Canaguia asset library

**Rules live in `DESIGN.md` → *Logo & Brand Assets* and *Social Media*, and in
`THUMBNAIL.md` for YouTube thumbnails.** This file is the inventory and naming
spec. If inventory and rules disagree, `DESIGN.md` / `THUMBNAIL.md` win.

Scope: **canaguia.com + public social/ads only** (YouTube, Instagram, Facebook and
shares). No TYPO3 backend, no internal admin screenshots.

---

## 1. Naming grammar

```
canaguia-<asset>[-<variant>][_<size>][@<scale>].<ext>
```

| Part | Values | Rules |
|---|---|---|
| `canaguia-` | fixed prefix | Always `canaguia-`, never `cg-` alone as a file prefix. |
| `<asset>` | `logo`, `mark`, `og-default`, `favicon`, `apple-touch`, `icon`, `frame`, `thumbnail`, plus platform names | What the artwork *is*. |
| `-<variant>` | `-mono-white`, `-mono-ink` | Names the **ink**, never the surface. The two-tone mark is the default (no suffix). |
| `_<size>` | `_140w`, `_1200x630` | Vector masters carry no size suffix. |
| `@<scale>` | `@2x`, `@3x` | Raster only. |
| `.<ext>` | `svg`, `png`, `webp`, `ico`, `pdf`, `json` | Lowercase. No `jpg`. |

| Suffix | Artwork | Goes on |
|---|---|---|
| (none) | two-tone: amber + blue | Light surfaces and photo veils |
| `-mono-white` | single white fill | Dark surfaces, forced single-colour |
| `-mono-ink` | single `#212529` fill | Light surfaces, print |

The two-tone rule is fixed: amber (`#ffae2a`) stays amber, blue (`#007ed4`) stays blue.
Do not invent a third logo colour.

---

## 2. Directory layout

```
assets/
├── README.md
├── brand/
│   ├── logo/
│   │   ├── master/     SVG masters (source of truth)
│   │   ├── web/        Width-scaled PNG / WebP
│   │   ├── print/      PDF / EPS if required
│   │   └── watermark/  Transparent overlays
│   ├── icons/          Favicon, app icons, PWA manifest
│   └── social/         OG cards, platform avatars/banners
└── video/
    ├── 16x9/ 9x16/ 1x1/ 4x5/ 21x9/
    ├── safeareas/
    └── spec/video-templates.json   # sizes, safe areas, thumbnail machine spec
```

YouTube thumbnail **rules** → root `THUMBNAIL.md`. Finished thumbnail exports may
land under `brand/social/` as `canaguia-thumbnail_<slug>[_1920x1080].jpg` (or
`.png`), under 2 MB, sRGB.

---

## 3. Masters currently shipped

| File | Role |
|---|---|
| `canaguia-logo.svg` | Lockup — two-tone mark + blue wordmark (for light surfaces) |
| `canaguia-mark.svg` | Mark only — amber over blue (for avatars, favicons) |
| `canaguia-logo-mono-ink.svg` | Lockup — single `#212529` fill |
| `canaguia-logo-mono-white.svg` | Lockup — single white fill |
| `canaguia-mark-mono-ink.svg` | Mark — single `#212529` fill |
| `canaguia-mark-mono-white.svg` | Mark — single white fill |

Native lockup viewBox: `0 0 79.374998 26.458333` (≈3:1). Native mark viewBox:
`3.512 3.274 92.861 72.823` (≈1.27:1). Header lockup is displayed at 120 × 40.

### Video frames (aspect overlays)

| File pattern | Role |
|---|---|
| `video/<aspect>/canaguia-frame-<aspect>-white.png` | Light frame overlay for that aspect |
| `video/<aspect>/canaguia-frame-<aspect>-black.png` | Dark frame overlay for that aspect |

Shipped aspects with frames: `16x9`, `9x16`, `1x1`, `4x5`. These are video/safe-area
helpers, not YouTube thumbnail masters — thumbnail composition follows `THUMBNAIL.md`.

---

## 4. Public-repo rules

- Do not commit admin UI screenshots, TYPO3 chrome, or internal analytics.
- Marketing photography is fine when it tells the Tenerife story without exposing
  private implementation detail.
- Partners should pull marks from `logo/master/` and follow clear-space rules in
  `DESIGN.md`.
- Raster packs (PNG/WebP/ICO) are generated from `logo/master/`, never hand-redrawn.
