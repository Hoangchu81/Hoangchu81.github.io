---
status: final
project: HoangCDAcademicWebsite
date: 2026-06-09
source: BMAD UX workflow
visual_reference: DESIGN.md
---

# EXPERIENCE.md — HoangCD Academic Website

## Foundation

Single-page GitHub Pages website, optimized for academic authority and fast scanning. Visual rules are governed by `DESIGN.md`.

## Information Architecture

1. **Hero** — Who Dr. Hoàng is and why he matters.
2. **Stats** — Fast credibility anchors.
3. **BMAD Analysis** — Shows design method and site rationale.
4. **03 Fields** — Core positioning.
5. **Research** — Themes and academic background.
6. **Publications** — Google Scholar synced publication list.
7. **News & Activities** — Social roles, events, updates.
8. **Contact** — Collaboration CTA.

## Voice and Tone

- Vietnamese primary.
- Formal but accessible.
- Avoid inflated claims.
- Use institutional vocabulary: KH&CN, đổi mới sáng tạo, chuyển đổi số, y tế số, chính sách.

## Component Patterns

### Hero CTAs
- Primary: explore 03 fields.
- Secondary: view publications.

### Publication Filtering
- Tabs filter client-side by topic/title.
- Empty state: “Chưa có dữ liệu phù hợp.”
- Data source: `data/publications.json`.

### News Cards
- Left category/date block.
- Right title + short summary.

### Field Cards
- Each card has one clear domain, not mixed content.
- Numeric watermark creates scanning rhythm.

## State Patterns

- Publication loading: “Đang tải publications...”
- Publication load fail: “Không tải được data/publications.json.”
- Empty filter result: “Chưa có dữ liệu phù hợp.”

## Interaction Primitives

- Sticky nav anchor jumps.
- Smooth scroll.
- Filter tabs toggle active state.
- CTAs use semantic anchors.

## Accessibility Floor

- High contrast navy/white sections.
- Body text >= 16px.
- Mobile hit targets >= 44px.
- Semantic HTML sections.
- No content hidden behind hover.

## Responsive & Platform

Breakpoints:
- Desktop > 920px: two-column hero, three-field grid.
- Tablet/mobile <= 920px: single-column layout.
- Small mobile <= 560px: reduced padding and h1 scale.

## Key Flows

### Flow 1: International partner validates profile
Partner lands → reads hero → scans 03 fields → reviews publications → contacts.

### Flow 2: Researcher checks publication authority
Researcher lands → jumps to publications → filters by field → follows Scholar-linked source.

### Flow 3: Journalist scans background
Journalist lands → reads stats → social/news section → contact.

## Future Extensions

- Add English toggle.
- Add `/publications.html` for full Scholar profile.
- Add `/news.html` for posts.
- Add CV PDF download.
- Add structured data JSON-LD Person/ScholarlyArticle.
