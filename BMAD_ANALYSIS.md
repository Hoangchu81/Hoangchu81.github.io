# BMAD website strategy — TS. Chử Đức Hoàng

## B — Business / Brand
Website cá nhân học thuật chuyên nghiệp cho TS. Chử Đức Hoàng, định vị là chuyên gia liên ngành về khoa học công nghệ, đổi mới sáng tạo, AI/chuyển đổi số và kỹ thuật y sinh.

## M — Market / Audience
- Đối tác dự án, viện/trường, tổ chức quốc tế
- Doanh nghiệp cần tư vấn đổi mới công nghệ
- Nhà nghiên cứu, học viên, cộng đồng KH&CN trẻ
- Báo chí / truyền thông cần hồ sơ nhanh

## A — Architecture / IA
Trang chủ single-page + sẵn sàng mở rộng multi-page:
1. Hero + positioning
2. 03 lĩnh vực chính
3. Research themes
4. Publications — đồng bộ Google Scholar
5. News & activities
6. Social/community roles
7. Contact / CV download

## D — Design / Delivery
Style: academic executive, modern, responsive, trust-focused.
Visual: navy/white/gold/cyan, clean card system, timeline, publication filters.

## 03 lĩnh vực chính đề xuất
1. Science, Technology & Innovation Policy
2. AI, Digital Transformation & Data Analytics
3. Biomedical Engineering & Digital Health

## Google Scholar sync design
Google Scholar không có API chính thức ổn định. Phương án triển khai:
- Preferred: dùng scholarly Python package hoặc SerpAPI/Publish-or-Perish export.
- Script định kỳ tạo `data/publications.json`.
- Website frontend đọc JSON để render bài báo.
- Có fallback manual list khi Scholar chặn scraping.

## Repo structure đề xuất
- `index.html` — landing page
- `data/publications.json` — cache bài báo Scholar
- `scripts/sync_scholar.py` — sync Google Scholar
- `.github/workflows/sync-scholar.yml` — cron GitHub Actions hằng ngày/tuần

## Next data needed
- Google Scholar profile URL/ID của TS. Hoàng
- Ảnh chân dung chính thức
- CV PDF bản public
- Links: ORCID, ResearchGate, Scopus, LinkedIn, Facebook/news
