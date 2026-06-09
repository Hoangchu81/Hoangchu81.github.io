---
status: final
project: HoangCDAcademicWebsite
owner: TS. Chử Đức Hoàng
date: 2026-06-09
source: BMAD UX workflow
---

# DESIGN.md — HoangCD Academic Website

## Brand & Style

**Brand posture:** Academic executive, evidence-based, international, trustworthy, Vietnamese STI leadership.

**Design principles:**
- Professional over decorative.
- Research-first hierarchy.
- Clear separation of 03 fields.
- Publications must feel current, searchable, and credible.
- News/social activity should support authority, not distract.

**Tone:** Senior expert, institution-ready, policy-and-research oriented.

## Colors

```yaml
colors:
  background: '#f8fafc'
  surface: '#ffffff'
  ink: '#0f172a'
  muted: '#64748b'
  border: '#e2e8f0'
  primary: '#0b1d33'
  primary_alt: '#173b63'
  accent_blue: '#2563eb'
  accent_cyan: '#0891b2'
  accent_gold: '#d97706'
  success: '#059669'
```

## Typography

```yaml
typography:
  heading:
    family: Inter, ui-sans-serif, system-ui
    weight: 900
    tracking: '-0.045em'
  body:
    family: Inter, ui-sans-serif, system-ui
    weight: 400
    line_height: 1.65
  meta:
    family: Inter, ui-sans-serif, system-ui
    weight: 800
```

## Layout & Spacing

```yaml
spacing:
  page_width: min(1180px, 92vw)
  nav_height: 72px
  section_y: 34px
  card_padding: 24px
  grid_gap: 16px
  hero_gap: 26px
```

## Elevation & Depth

```yaml
elevation:
  card: 0 14px 45px rgba(15, 23, 42, .07)
  hero: 0 24px 70px rgba(15, 23, 42, .12)
```

## Shapes

```yaml
rounded:
  small: 14px
  medium: 20px
  large: 28px
  hero: 34px
  pill: 999px
```

## Components

### Navigation
Sticky top nav, white translucent background, blur, section anchors.

### Hero
Dark navy gradient, large positioning statement, 2 CTAs, profile card on right.

### Field Cards
Three equal cards with numeric watermark: 01 / 02 / 03.

### Publications
JSON-fed list with filter tabs. Filters: All, STI/Green, AI/Data, Biomedical.

### News
Card list with compact date/category block.

### Contact
Dark gradient panel with email CTA.

## Do's and Don'ts

**Do:**
- Use sharp academic copy.
- Use strong hierarchy.
- Keep publications machine-readable.
- Optimize for mobile.

**Don't:**
- Use generic SaaS icons.
- Overuse animation.
- Invent unverified metrics.
- Hide contact info.
