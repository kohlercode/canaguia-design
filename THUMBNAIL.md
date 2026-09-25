---
version: alpha
name: Canaguia YouTube Thumbnails
description: >-
  Production rules for Canaguia YouTube thumbnails. Energetic, sun-drenched,
  photo-led frames that stay recognizable in mobile feeds. Anchored to the
  Canaguia brand (ocean blue, sun amber, Poppins watermark) with intentional
  thumbnail-only exceptions for condensed display type, CTR gold fill, stroke,
  and the Golden Vortex. Complements DESIGN.md — when site UI and thumbnail
  rules conflict, DESIGN.md wins for canaguia.com; this file wins for YouTube
  thumbnails.

colors:
  # Shared brand (from DESIGN.md)
  primary: "#007ed4"
  secondary: "#ffae2a"
  ink: "#212529"
  on-dark: "#f8f9fa"
  dark: "#343a40"
  hero-veil: "rgba(0, 0, 0, 0.3)"
  # Thumbnail-only (CTR / FX — never use as site UI fills)
  thumbnail-gold: "#ffcc00"
  thumbnail-gold-hi: "#ffd700"
  vortex-hi: "#ffe066"
  vortex-lo: "#ffaa00"
  stroke: "#000000"
  watermark: "#ffffff"

typography:
  thumbnail-display:
    fontFamily: "Anton, Bebas Neue, Impact, \"DIN Condensed Bold\", sans-serif"
    fontWeight: 700
    letterSpacing: "0.01em"
    textTransform: uppercase
    note: "Thumbnail CTR only — never on canaguia.com UI"
  thumbnail-line2-scale: "0.5–0.7 × line 1"
  watermark:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    letterSpacing: "0em"
    textTransform: lowercase

canvas:
  recommended: { w: 1920, h: 1080 }
  minimum: { w: 1280, h: 720 }
  aspect: "16:9"
  colorSpace: sRGB
  formats: ["jpg", "png"]
  maxBytes: 2097152
  safeExcludeBottomRight: { w: 180, h: 100 }
  watermarkPadding: 40px
  titleZone: top-third

components:
  thumbnail-title:
    textColor: "{colors.thumbnail-gold}"
    strokeColor: "{colors.stroke}"
    strokeWidth: "10–18px"
    shadow: "rgba(0,0,0,0.8–1) blur 12–20px offset 0–8px"
    typography: "{typography.thumbnail-display}"
    placement: "{canvas.titleZone}"
  thumbnail-vortex:
    colorHigh: "{colors.vortex-hi}"
    colorLow: "{colors.vortex-lo}"
    blendMode: "Screen or Linear Dodge (Add)"
    placement: "behind subject / landmark"
  thumbnail-watermark:
    text: "canaguia.com"
    textColor: "{colors.watermark}"
    opacity: "0.9–1"
    typography: "{typography.watermark}"
    placement: bottom-left
    padding: "{canvas.watermarkPadding}"
---

# Canaguia YouTube Thumbnails

Every Canaguia YouTube thumbnail must feel **energetic, sun-drenched, authentic**,
and immediately recognizable in feeds. Partners, agents, and designers follow this
file. Shared brand tokens live in `DESIGN.md`; machine sizes and safe areas also
live in `assets/video/spec/video-templates.json`.

**Scope:** YouTube thumbnails only. Site UI, cards, and marketing pages stay on
`DESIGN.md` (Poppins, light-first, no condensed display, no vortex FX).

## Visual Theme & Atmosphere

Photo-first Tenerife travel energy. A real place and a real person carry the frame;
sun-amber light (the Golden Vortex) opens a “portal” behind the subject; condensed
ALL-CAPS gold type sits in the top third. The brand stamp is a quiet
`canaguia.com` in Poppins at the bottom-left — not a second headline.

**Key Characteristics:**
- Full-bleed location photography with a human subject in frame.
- Golden Vortex behind the subject — signature Canaguia thumbnail FX.
- CTR title in `{colors.thumbnail-gold}` (#ffcc00) with heavy black stroke —
  readable at mobile feed size.
- `{colors.secondary}` (#ffae2a) anchors the vortex low end; do not invent a third
  brand hue for the site.
- Watermark is Poppins lowercase `canaguia.com`, never Inter/Roboto.
- Bottom-right timestamp pocket stays empty.

## Canvas & Export

| Property | Value | Notes |
|---|---|---|
| Recommended | `{canvas.recommended}` — 1920 × 1080 | 16:9 production canvas |
| Minimum | `{canvas.minimum}` — 1280 × 720 | YouTube HD floor |
| Color space | sRGB | Web profile |
| Format | JPG / PNG | Under 2 MB (`{canvas.maxBytes}`) |
| Safe exclude | Bottom-right 180 × 100 px | YouTube timestamp badge — no faces, text, or logos |

Export naming (see `assets/README.md`):

```
canaguia-thumbnail_<slug>[_1920x1080].jpg
```

Examples live in `assets/video/16x9/` (`canaguia-thumbnail_aeropuerto-sur.jpg`,
`canaguia-thumbnail_cateo-barraquitos.jpg`, `canaguia-thumbnail_parque-anaga.jpg`).

## Typography

### Thumbnail display (CTR only)

| Token | Rule |
|---|---|
| Family | Extra-bold **condensed** sans: Anton, Bebas Neue, Impact, or DIN Condensed Bold |
| Case | Always ALL CAPS |
| Line 1 | Destination, activity, or attraction (`PARQUE RURAL ANAGA`, `PLAYA JARDÍN`) |
| Line 2 (optional) | Island/region tag (`TENERIFE`) at ~50–70% of Line 1 size |
| Fill | `{colors.thumbnail-gold}` (#ffcc00); `{colors.thumbnail-gold-hi}` (#ffd700) allowed |
| Stroke | `{colors.stroke}` (#000000), 10–18 px on the 1920 canvas |
| Shadow | Deep black, opacity 80–100%, blur 12–20 px, offset 0–8 px |
| Placement | Top third, spanning horizontally |

Optional subtle metallic or grunge texture on the gold fill is allowed if contrast
stays high at 10% zoom.

**Do not** use this condensed stack on canaguia.com. Site type remains Poppins per
`DESIGN.md`.

### Watermark

`canaguia.com` — `{typography.watermark}` (Poppins 500), solid
`{colors.watermark}` at 90–100% opacity, bottom-left, ≥ 40 px from edges.

## Signature Element: The Golden Vortex

Every **standard** thumbnail includes the Golden Vortex / portal light:

- Circular or elliptical swirling arcs in `{colors.vortex-hi}` → `{colors.vortex-lo}`
  (#ffe066 → #ffaa00), hugging `{colors.secondary}` at the warm end.
- Placement: encircling or radiating **behind** the main subject or landmark.
- Accents: subtle warm sparks, embers, bokeh along the trails.
- Blend: Screen or Linear Dodge (Add); keep opacity balanced so the subject stays
  sharp and high-contrast.

This FX is **thumbnail-only**. Do not port the vortex into site heroes or UI.

## Photography & Human Focus

- **Real people:** Hosts, locals, or travelers with genuine emotion (smile, eye
  contact, gesture, tasting food/drink).
- **Styling:** Authentic travel/vlog attire (e.g. white Canaguia / yacht polo,
  outdoor jackets, sunglasses); visible wireless lav mics reinforce guide
  credibility when present.
- **Grade:** Warm (+5 to +10 toward amber/gold); punchy midtone contrast;
  saturated sky/ocean blues and landscape greens; subtle golden rim light on the
  subject matching the vortex.

## Layering Architecture

Back → front:

1. **Background plate** — High-res location shot (light depth-of-field blur).
2. **Ambient radial glow & vortex** — Golden rings and warm atmospheric wash.
3. **Typography** — Gold title + black stroke + shadow (may tuck partly behind
   the subject for depth).
4. **Subject cutout** — Presenter/subjects with clean edges.
5. **Foreground FX & watermark** — Embers, flare streaks, rim light;
   `canaguia.com` bottom-left.

## Branding

| Element | Rule |
|---|---|
| URL watermark | `canaguia.com`, bottom-left, Poppins, white |
| Mark / lockup | Optional small mark if needed; prefer URL watermark. Mono-white mark only on dark regions. |
| Timestamp pocket | Keep bottom-right 180 × 100 clear |
| Site lockup colours | Amber stays amber, blue stays blue — never recolour the mark |

## Pre-Export Checklist

- [ ] Headline legible at ~10% scale (mobile feed).
- [ ] Bottom-right 180 × 100 clear of faces, text, logos.
- [ ] Golden Vortex integrated naturally (standard thumbnails).
- [ ] Subject sharp, well-lit, expressive, separated from background.
- [ ] `canaguia.com` present bottom-left (≥ 40 px padding).
- [ ] sRGB JPG/PNG under 2 MB; 1920 × 1080 preferred (1280 × 720 minimum).

## Do's and Don'ts

### Do
- Lead with real Tenerife photography and a human subject.
- Use gold fill + black stroke so type survives tiny feed previews.
- Keep the vortex behind the subject; grade toward sun amber.
- Reserve the bottom-right for YouTube’s timestamp.
- Watermark with Poppins `canaguia.com`.

### Don't
- Don't place type, faces, or logos in the timestamp pocket.
- Don't use flat colour posters or stock-illustration backgrounds.
- Don't set thumbnail titles in Poppins (too soft at feed size) or watermark in
  Inter/Roboto/Montserrat.
- Don't put white text on amber/gold fills for the main title.
- Don't ship the vortex, condensed display stack, or CTR gold as site UI tokens.
- Don't exceed 2 MB or leave the canvas below 1280 × 720.

## Relationship to DESIGN.md

| Concern | Source of truth |
|---|---|
| Site UI, colors, Poppins, cards, heroes | `DESIGN.md` |
| YouTube thumbnail composition & CTR type | **This file** |
| Pixel sizes, platform safe areas | `assets/video/spec/video-templates.json` |
| Asset inventory & naming | `assets/README.md` |

Shared hexes (`{colors.primary}`, `{colors.secondary}`, ink, dark) must stay
aligned with `DESIGN.md`. Thumbnail-only tokens
(`thumbnail-gold`, `vortex-*`, condensed display) must **not** leak into site CSS
or `theme.css`.

## Iteration Guide

1. Start from a real location plate + subject cutout.
2. Add vortex behind the subject; grade warm.
3. Set Line 1 (and optional Line 2) in the top third; run the 10% zoom test.
4. Clear the timestamp pocket; place `canaguia.com` bottom-left.
5. Export sRGB under 2 MB.

## Known Gaps

- **No PSD / Affinity master template** shipped yet — layer order above is the
  production contract until a layered master lands in `assets/video/`.
- **Golden Vortex artwork** is not a reusable SVG asset; recreate per thumbnail
  with the colour and blend rules above.
- **Condensed webfonts** are not part of the site font kit; license and load them
  only in design tools for thumbnail production.
