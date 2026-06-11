# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal academic website for TS. Chử Đức Hoàng (hoangchu81.github.io), served directly by GitHub Pages from the `main` branch. There is **no build system, no package manager, no tests, and no linter** — every page is a single self-contained HTML file with all CSS and JS inlined. Site content is in Vietnamese.

## Development

Pages fetch JSON at runtime, so opening files via `file://` breaks them. Serve locally instead:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/ and http://localhost:8000/admin/
```

Deployment = push to `main`. GitHub Pages picks it up in 1–2 minutes.

## Architecture

Three moving parts, connected only through the JSON files in `data/`:

1. **`index.html`** — the public single-page site (hero, timeline, fields, publications, news, contact). At load time it fetches `data/publications.json` (rendered sorted by citations desc, filterable by topic tabs) and `data/news.json` (sorted by date desc). All styling uses CSS custom properties defined in `:root` (navy/gold/cream editorial palette); reuse those tokens rather than hardcoding colors.

2. **`admin/index.html`** — a serverless CMS, also a single file. It loads the same JSON files, keeps edits in `localStorage` (keys `news_data` / `pubs_data`), and writes back to the repo **client-side via the GitHub Contents API**, committing directly to `main`. It prompts for a GitHub PAT and caches it in `localStorage` under `gh_token`. The "Đồng bộ Scholar" button triggers the `scholar-sync.yml` workflow via `workflow_dispatch`. Repo/branch constants live at the top of its script (`GH_REPO`, `GH_BRANCH`).

3. **GitHub Actions Scholar sync** — two overlapping workflows both write `data/publications.json` and commit to `main`:
   - `.github/workflows/scholar-sync.yml` — the primary one (daily cron + the admin button's dispatch target). Contains inline Python that scrapes the Google Scholar profile page (user `tcJwNTsAAAAJ`) with regex and auto-assigns the `topic` field by keyword matching on title/venue.
   - `.github/workflows/sync-scholar.yml` — older weekly variant running `scripts/sync_scholar.py` (uses the `scholarly` package, requires `SCHOLAR_ID` secret, exits cleanly keeping existing JSON on failure).

### Data schemas

These shapes are shared by the frontend, the admin, and the sync workflows — keep all three in agreement when changing them. All values are strings (including `year` and `citations`).

- `data/publications.json`: `{id, title, authors, venue, year, citations, topic, url}`. `topic` ∈ `STI` | `AI` | `Biomedical` | `Digital Health`; the homepage filter tabs match on substring of `topic`.
- `data/news.json`: `{id, title, source, url, date (YYYY-MM-DD), category, excerpt (HTML), image}`. `category` ∈ `STI Policy` | `AI & Digital` | `Digital Health` | `Khác`. `excerpt` is WYSIWYG HTML; `image` may be an external URL or a base64 data URL embedded by the admin's upload feature.

### Edits made outside Git

The admin UI and the cron workflows commit straight to `main`. Before editing `data/*.json`, pull first — the working copy may be behind, and a force-push or stale overwrite would destroy content edits made through the admin.

## BMAD artifacts

The repo carries BMAD-method tooling and planning docs that are **not part of the served site**: `_bmad/` (installer-managed config — treat as read-only), `_bmad-output/planning-artifacts/` (PRD, ARCHITECTURE, DESIGN, EXPERIENCE, product brief), `.claude/skills/bmad-*`, and `BMAD_ANALYSIS.md` (the original site strategy: positioning, IA, the three expertise pillars, and the Scholar-sync design rationale). BMAD document output language is configured as Vietnamese.
