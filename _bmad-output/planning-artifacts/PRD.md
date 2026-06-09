# BMAD PRD — Luxury Academic Editorial Redesign

## Mục tiêu
Thiết kế lại toàn bộ public website và admin cho TS. Chử Đức Hoàng theo phong cách luxury academic editorial: Nature/Harvard/MIT-inspired, tối giản, sang trọng, có motion nhẹ, dễ quản trị.

## Users
- Nhà hoạch định chính sách, cơ quan quản lý KH&CN
- Doanh nghiệp, đối tác đổi mới sáng tạo
- Học giả, nhà nghiên cứu, sinh viên
- Truyền thông, ban tổ chức hội thảo
- Admin nội dung

## Functional requirements
1. Public homepage thể hiện rõ positioning chuyên gia STI Policy / AI & Digital / Digital Health.
2. News section đọc dữ liệu từ `data/news.json`, tự sort theo ngày.
3. Publications đọc từ `data/publications.json`, có filter chủ đề.
4. Admin quản lý tin tức: thêm/sửa/xóa/sắp xếp/tìm kiếm/filter.
5. Admin hỗ trợ WYSIWYG.
6. Admin publish qua GitHub Contents API.
7. Responsive desktop/tablet/mobile.
8. Accessibility: focus states, contrast, reduced motion.

## Design requirements
- Visual style: luxury academic editorial.
- Inspiration: Nature editorial, Harvard institutional restraint, MIT systems clarity.
- Palette: ivory paper, deep ink, navy blue, restrained gold.
- Typography: Crimson Pro headlines, Atkinson Hyperlegible body.
- Motion: reveal-on-scroll, subtle hover only, disabled via prefers-reduced-motion.

## Non-goals
- Không dùng CMS server-side.
- Không build framework phức tạp.
- Không lưu PAT vào repo.
