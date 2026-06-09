#!/usr/bin/env python3
"""Sync Google Scholar publications to data/publications.json.
Set SCHOLAR_ID to the Google Scholar user id, e.g. abc1234AAAAJ.
Fallback keeps existing JSON if Scholar blocks requests.
"""
import json, os, pathlib, sys
OUT = pathlib.Path(__file__).resolve().parents[1] / 'data' / 'publications.json'
SCHOLAR_ID = os.getenv('SCHOLAR_ID', '').strip()
if not SCHOLAR_ID:
    print('SCHOLAR_ID not set; keeping existing publications.json')
    sys.exit(0)
try:
    from scholarly import scholarly
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=['publications'])
    pubs=[]
    for p in author.get('publications', [])[:80]:
        bib=p.get('bib', {})
        pubs.append({
            'year': str(bib.get('pub_year','')),
            'title': bib.get('title',''),
            'venue': bib.get('venue','Google Scholar'),
            'topic': 'Google Scholar',
            'link': p.get('pub_url') or p.get('eprint_url') or '#'
        })
    pubs=[p for p in pubs if p['title']]
    OUT.write_text(json.dumps(pubs, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Wrote {len(pubs)} publications -> {OUT}')
except Exception as e:
    print('Scholar sync failed; keeping existing JSON:', e)
    sys.exit(0)
