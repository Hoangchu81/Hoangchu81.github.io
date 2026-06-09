# Product Brief: Website cá nhân học thuật TS. Chử Đức Hoàng

## Vision
Website cá nhân học thuật chuyên nghiệp, chuyên sâu cho TS. Chử Đức Hoàng — thể hiện hồ sơ nghiên cứu, 03 lĩnh vực hoạt động chính, công bố khoa học (đồng bộ Google Scholar), hoạt động xã hội và tin tức.

## Target Users
1. Đối tác dự án quốc tế (UN, APEC, World Bank)
2. Viện/trường, doanh nghiệp cần tư vấn đổi mới công nghệ
3. Nhà nghiên cứu, học viên, cộng đồng KH&CN trẻ
4. Báo chí / truyền thông

## Core Features
1. Hero + Positioning — TS. Chử Đức Hoàng, 03 lĩnh vực chính
2. 03 Lĩnh vực nghiên cứu:
   - Quản lý KH&CN và Đổi mới Sáng tạo (STI Policy)
   - AI, Chuyển đổi số và Phân tích dữ liệu
   - Kỹ thuật Y sinh và Y tế số
3. Publications — tự động đồng bộ Google Scholar (JSON + GitHub Actions)
4. Tin tức và hoạt động — sự kiện, truyền thông, vai trò cộng đồng
5. Hoạt động xã hội — VAYSE, LifVietnam, CVFA, BME community
6. About / CV — tiểu sử, học vấn, kinh nghiệm
7. Contact — email, mobile, social links

## Constraints
- Single-page responsive HTML (GitHub Pages)
- No build tools / framework dependency
- Self-contained CSS/JS
- Google Scholar sync via external JSON
- Bilingual-ready (VI primary, EN expandable)
- Professional academic tone, not flashy SaaS

## Success Metrics
- Load time < 2s
- Mobile-first responsive
- Google Scholar publications auto-update weekly
- Professional enough for UN/APEC project submissions

## Tech Stack
- Pure HTML/CSS/JS
- GitHub Pages hosting
- GitHub Actions for Scholar sync
- data/publications.json as data source
