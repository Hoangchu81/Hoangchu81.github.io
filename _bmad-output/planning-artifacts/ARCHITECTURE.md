# BMAD Architecture — Static Luxury Academic Website

## Stack
- Static GitHub Pages
- HTML/CSS/Vanilla JS
- JSON data sources
- GitHub Contents API for admin publish

## Data
- `data/news.json`: structured media/news items
- `data/publications.json`: structured publications

## Public site
- `index.html`
- Dynamic sections:
  - Publications: fetch `data/publications.json`
  - News: fetch `data/news.json`
- Progressive enhancement: site remains readable if JS partially fails.

## Admin
- `admin/index.html`
- Loads `../data/news.json`
- Edits in browser state + `localStorage`
- Publish flow:
  1. Request PAT from admin user
  2. Fetch current file SHA via GitHub Contents API
  3. PUT updated Base64 JSON to `data/news.json`
  4. GitHub Pages rebuilds automatically

## Security
- PAT only stored in browser `localStorage`; never committed.
- Recommended PAT scope: repo contents read/write, narrow to site repo if fine-grained token.

## Accessibility/performance
- No heavy framework.
- Native semantic HTML.
- `prefers-reduced-motion` supported.
- Fonts loaded via Google Fonts; fallback system fonts present.
