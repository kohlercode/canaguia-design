---
version: alpha
name: Canaguia
description: >-
  The visual identity for canaguia.com, the online tour guide for Tenerife.
  A light-first, photo-led travel system: white canvases carry a deep warm ink,
  a confident ocean blue drives the brand name and every primary action, and a
  sun-amber accent marks the island spark. Hero surfaces are full-bleed
  photography under a dark veil with white type. Poppins only — friendly,
  geometric, legible. Generous 16px radii, no hard shadows, nothing corporate.
  The register is warm and tourist-friendly, not luxury-travel, not startup-tech.

colors:
  # Brand & accent
  primary: "#007ed4"
  primary-hover: "#0065aa"
  secondary: "#ffae2a"
  # Surfaces
  bg: "#ffffff"
  surface: "#ffffff"
  light: "#f8f9fa"
  dark: "#343a40"
  # Text
  ink: "#212529"
  ink-dim: "#6c757d"
  on-primary: "#ffffff"
  on-dark: "#f8f9fa"
  # Line
  line: "#dee2e6"
  # Hero photography veil
  hero-veil: "rgba(0, 0, 0, 0.3)"
  # Semantic
  success: "#198754"
  error: "#dc3545"
  # Social (content creator palette — do not use as UI fills)
  youtube: "#ff0000"
  instagram: "#e1306c"
  facebook: "#1877f2"
  x: "#000000"
  linkedin: "#0077b5"
  whatsapp: "#25d366"
  telegram: "#229ed9"
  reddit: "#ff4500"
  pinterest: "#e60023"

typography:
  brand:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  display-lg:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  display-md:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  h2:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0em"
  h3:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0em"
  lead:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  body-md:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  body-sm:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "0em"
  caption:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0em"
  label:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.02em"
  button:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0em"

rounded:
  none: 0px
  sm: 4px
  md: 8px
  xl: 16px
  xxl: 32px
  full: 800px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  section: 64px

components:
  page-shell:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  nav-header:
    backgroundColor: "{colors.light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: 68px
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
  nav-link-hover:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
  hero-band:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
  hero-title:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
  eyebrow-label:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  section-head:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  section-lead:
    backgroundColor: "transparent"
    textColor: "{colors.ink-dim}"
    typography: "{typography.lead}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 16px 16px
  card-title:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.h3}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 20px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 20px
  link-inline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  badge:
    backgroundColor: "{colors.light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  divider:
    backgroundColor: "{colors.line}"
    height: 1px
  cta-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 0 32px
  footer-copy:
    backgroundColor: "transparent"
    textColor: "{colors.ink-dim}"
    typography: "{typography.caption}"
---

# Canaguia

## Visual Theme & Atmosphere

Canaguia is a warm, tourist-friendly travel guide. The default canvas is **white**
(`{colors.bg}` — #ffffff), not grey, not dark. Deep warm ink (`{colors.ink}` — #212529)
carries all text. The brand's most recognisable surface is the **photo hero**:
a full-bleed photograph of Tenerife dimmed by a dark veil (`{colors.hero-veil}`) with
white type over it. Ocean blue (`{colors.primary}` — #007ed4) is brand and primary
action; sun amber (`{colors.secondary}` — #ffae2a) is the accent that lights the mark
and highlights moments — never a full button.

**Key Characteristics:**
- Light-first white canvas. Dark is reserved for the footer and photo-veiled hero.
- Ocean blue `{colors.primary}` (#007ed4) drives brand name, links, and primary CTAs.
- Sun amber `{colors.secondary}` (#ffae2a) is a spark — the mark's upper half, small
  highlights, secondary buttons. Text on amber is always `{colors.ink}`, never white.
- "CANAGUIA" in Poppins 700 at brand scale outranks any supporting headline.
- Poppins only. Headlines 700, body 400. Friendly and geometric, never condensed.
- Generous 16px radii on cards and images. Depth comes from white-on-white bands and
  hairline borders, not heavy drop shadows (the header's `shadow-lg` is the exception).
- No purple, no neon gradient, no cold "AI default" palette. Sun and sea.

## Colors

### Brand & Accent
- **Primary / Ocean Blue** (`{colors.primary}` — #007ed4): Brand name, links, primary
  CTAs, labels. White text (`{colors.on-primary}`) on top.
- **Primary Hover** (`{colors.primary-hover}` — #0065aa): Pressed/hover blue.
- **Secondary / Sun Amber** (`{colors.secondary}` — #ffae2a): The mark's upper shapes,
  secondary buttons, small highlights. Dark ink text on top.

### Surfaces
- **Background / Surface** (`{colors.bg}` / `{colors.surface}` — #ffffff): Page floor
  and cards. Light-first.
- **Light** (`{colors.light}` — #f8f9fa): Soft bands, header background, badges.
- **Dark** (`{colors.dark}` — #343a40): Footer and photo-veiled hero base.

### Text
- **Ink** (`{colors.ink}` — #212529): All body and heading text.
- **Ink Dim** (`{colors.ink-dim}` — #6c757d): Captions, metadata, quiet labels.
- **On Primary** (`{colors.on-primary}` — #ffffff): Text on blue fills.
- **On Dark** (`{colors.on-dark}` — #f8f9fa): Text on footer and hero veils.

### Semantic
- **Success** (`{colors.success}` — #198754) and **Error** (`{colors.error}` — #dc3545):
  validation and status only.

### Social (creator palette)
`{colors.youtube}`, `{colors.instagram}`, `{colors.facebook}`, `{colors.x}`,
`{colors.linkedin}`, `{colors.whatsapp}`, `{colors.telegram}`, `{colors.reddit}`,
`{colors.pinterest}` are platform-brand colours for **share buttons and social
creatives only**. Never use them as UI fills on canaguia.com.

## Typography

Poppins is the only family (self-hosted, weights 400 and 700 shipped; 500/600/800 are
available weights if added). Body runs 400, headings 700, buttons 500.

| Token | Size | Weight | Use |
|---|---|---|---|
| `{typography.brand}` | 28px | 700 | "CANAGUIA" set as live text (the logo wordmark is vector, not text) |
| `{typography.display-lg}` | 40px | 700 | Hero headline over photos |
| `{typography.display-md}` | 32px | 700 | Page h1 / section lead title |
| `{typography.h2}` | 28px | 700 | Section headings |
| `{typography.h3}` | 24px | 600 | Card titles |
| `{typography.lead}` | 20px | 400 | Intro paragraphs |
| `{typography.body-md}` | 16px | 400 | Body copy (default) |
| `{typography.body-sm}` | 14px | 400 | Compact copy, meta |
| `{typography.caption}` | 12px | 400 | Captions, footnotes |
| `{typography.label}` | 12px | 700 | Eyebrow labels / badges |
| `{typography.button}` | 20px | 500 | Buttons (large and thumb-friendly) |

Fluid behaviour: headings scale with the viewport via `clamp()` (see preview.html).
Body copy stays at a fixed 16px.

## Layout

- **Section rhythm:** `{spacing.section}` (64px) vertical padding.
- **Max content width:** 1320px (Bootstrap `container-xxl`); 1140px is the typical
  `container` width on large screens.
- **Hero:** full-bleed photo (≈1500×400 source, `min-height` 400px) under
  `{colors.hero-veil}`; white title, one optional subline, left-aligned.
- **Cards:** white surface, 1px `{colors.line}`, `{rounded.xl}`, image on top at
  416×200 (≈16:9) with the same radius.
- **Container gutter:** Bootstrap default (0.75rem at mobile → 1.5rem at xl).

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Page | `{colors.bg}` (white) | Default floor |
| Band | `{colors.light}` | Alternating sections, header |
| Raised | `{colors.surface}` + 1px `{colors.line}` | Cards |
| Header | `{colors.light}` + `shadow-lg` | Sticky nav only |
| Hero | Photo + `{colors.hero-veil}` | Full-bleed hero, CTA bands |
| Dark | `{colors.dark}` | Footer |

Prefer tonal banding (white / light / white) over shadows for separating sections.

## Shapes

- UI chrome and buttons: `{rounded.md}` (8px).
- Cards, images, media frames: `{rounded.xl}` (16px).
- Large media / panels: `{rounded.xxl}` (32px).
- Labels, badges, chips: `{rounded.full}` (pill).
- Buttons are rounded rectangles, never pills.

## Logo & Brand Assets

The logo is a **two-tone lockup**: an abstract sun-and-sea mark (amber over blue) plus
the "CANAGUIA" wordmark set in blue. All artwork is outlined paths — no live-text
dependency.

| Variant | Asset | Use on |
|---|---|---|
| Lockup | `assets/brand/logo/master/canaguia-logo.svg` | Default; light/white surfaces |
| Mark | `assets/brand/logo/master/canaguia-mark.svg` | Small favicons, avatars, app icons |
| Mono ink | `canaguia-logo-mono-ink.svg` / `canaguia-mark-mono-ink.svg` | Forced single-colour, light/print |
| Mono white | `canaguia-logo-mono-white.svg` / `canaguia-mark-mono-white.svg` | Forced single-colour, dark |

Native lockup viewBox: **79.375 × 26.458** (≈3:1). Native mark viewBox:
**92.861 × 72.823** (≈1.27:1). Displayed lockup in the header is 120 × 40.

**Rules:** Scale by width only. Clear space ≥ 0.5 × mark height. Do not recolour the
amber to blue or vice-versa; the two-tone mark is fixed. Below ~80px lockup width
prefer the mark alone. Do not rebuild "CANAGUIA" from a random font — use the lockup
asset, or set it in Poppins 700 only to demonstrate `{typography.brand}`.

## Components

**`hero-band` + `hero-title`** — Full-bleed photo hero. Title in white at
`{typography.display-lg}`, one subline, primary CTA. The photo carries the dark veil.

**`eyebrow-label`** — Pill badge: blue fill, white text, `{typography.label}`.

**`button-primary`** — Blue fill, white text, `{rounded.md}`, 20px type, comfortable
padding. Large and thumb-friendly (≥44px target).

**`button-secondary`** — Amber fill, dark ink text. Use sparingly as an accent action.

**`card`** — White, 1px `{colors.line}`, `{rounded.xl}`, image 416×200 on top. This is
the workhorse for activities, experiences, gastronomy, and news.

**`footer`** — Dark band reusing `{colors.dark}`; links in `{colors.on-dark}`, copy in
`{colors.ink-dim}`.

## Social Media

### Video
YouTube (16:9, 1920×1080) is the primary channel; Shorts/Reels (9:16, 1080×1920) and
square posts (1:1, 1080×1080) reuse the same brand kit. Safe-area and end-screen rules
live in `assets/video/spec/video-templates.json`.

### Stills
Use photo-led frames: full-bleed Tenerife photography, dark veil if text sits on it,
white or amber type, and the mark or lockup in a corner. Never a flat colour poster.

### YouTube thumbnails
Thumbnails are a **deliberate exception** to the quiet site UI. They stay photo-led and
sun-amber anchored, but use condensed ALL-CAPS gold type, a black stroke, and the
**Golden Vortex** light FX so titles survive mobile feeds. Full production rules,
layer order, and checklist live in **`THUMBNAIL.md`** (same DESIGN.md format).

| Spec | Value |
|---|---|
| Canvas | 1920 × 1080 preferred; 1280 × 720 minimum; sRGB; under 2 MB |
| Title | Condensed display, ALL CAPS, gold `#ffcc00` + black stroke, top third |
| Signature FX | Golden Vortex behind subject (`#ffe066` → `#ffaa00`, near `{colors.secondary}`) |
| Watermark | Poppins `canaguia.com`, bottom-left, ≥ 40 px padding |
| Safe exclude | Bottom-right 180 × 100 px (YouTube timestamp) — no faces, text, or logos |

Do **not** port condensed display type, CTR gold fills, or the vortex into site CSS /
`theme.css`. Site surfaces remain Poppins + `{colors.primary}` / `{colors.secondary}`
per this file.

### Brand presence
- **YouTube:** lockup (mono-white) over dark end-screens; thumbnails per `THUMBNAIL.md`.
- **Instagram:** mark for the avatar; 1:1 and 4:5 feed, 9:16 stories/reels.
- **Facebook:** lockup for the page profile; 16:9 cover at 820×312.

## Do's and Don'ts

### Do
- Lead with full-bleed Tenerife photography — it is the brand.
- Use ocean blue for links and primary actions; amber only as a spark.
- Keep type Poppins, friendly and generous; white type on photo veils.
- Round media and cards at 16px.
- Put the two-tone mark (amber over blue) where a small brand stamp is needed.

### Don't
- Don't dark-mode the whole site — white is the default canvas.
- Don't use amber as a full primary button or put white text on amber.
- Don't use the social platform colours as UI fills.
- Don't add neon gradients or purple/teal accents on the **site** (the thumbnail
  Golden Vortex is allowed only in YouTube thumbnails — see `THUMBNAIL.md`).
- Don't crowd the hero with stats or secondary content — photo + title + one CTA.
- Don't rebuild the wordmark from a random font in creatives.
- Don't invent thumbnail layouts that skip the vortex, watermark, or timestamp
  safe zone — follow `THUMBNAIL.md`.

## Iteration Guide

1. One component at a time; reference YAML keys.
2. Use `{token.refs}` — do not invent hexes.
3. A new chromatic colour almost always means you wanted blue vs amber, not a third hue.
4. Contrast: white on blue, ink on white, and on-dark on dark must clear WCAG AA.
5. When implementation and this file disagree, this file wins.

## Known Gaps

- **The wordmark and mark are outlined paths** (no live text / webfont dependency).
- **No success/error token usage yet on marketing surfaces.**
- **Raster packs** (PNG/WebP @2x/@3x, `.ico`) are not yet generated — export them from
  `logo/master/` when needed.
- **Poppins 500/600/800** are not shipped on the live site yet; this spec uses 400/700
  and treats 500 (buttons) as an optional load.
- **Instagram brand colour** is the standard `#e1306c`; the live share palette does not
  yet include an Instagram button.
- **White on `{colors.primary}` is 4.26:1** (just under WCAG AA for normal text). It
  passes AA only for large/bold text (≥18.66px bold, e.g. the 20px button). For small
  blue labels (12px eyebrow badges), prefer `{colors.primary-hover}` (#0065aa) or bump
  to bold/larger type. Kept at `#007ed4` because it is the real brand value.
- **Transparent-background components** (nav links, headings, card titles, leads) are
  flagged by the linter against black, but in use they inherit white, where
  `{colors.ink}` reads ~15.9:1 and `{colors.ink-dim}` ~4.68:1 — both AA-compliant.
- **YouTube thumbnail CTR stack** (condensed display, `#ffcc00` gold, vortex FX) is
  specified in `THUMBNAIL.md` and intentionally excluded from site tokens /
  `theme.css`.
