# Báo cáo kết quả Lab 17: Zep Multi-Memory Agent

## 1. Trả lời các câu hỏi về Memory Layers

* **Layer quan trọng nhất trong bộ test này:** `Long-term memory`. Nó chiếm tỷ trọng lớn nhất với 4 tests (E02, E03, E08, E09) cộng thêm đóng góp vào test mixed (E07). Việc không có long-term memory sẽ khiến agent mất trí nhớ hoàn toàn về dự án, sở thích, và các open-loop.
* **Trade-off giữa Zep Cloud và Redis+Qdrant:** Zep Cloud (Context Block) hoạt động dạng managed service, tự động trích xuất edges, nodes, và facts từ các threads của user giúp tiết kiệm công sức xây dựng pipeline ingestion, chunking, và tóm tắt. Tuy nhiên, nó mất đi tính linh hoạt và tuỳ chỉnh sâu so với việc tự vận hành Redis và Qdrant local, nơi lập trình viên toàn quyền kiểm soát cách lưu trữ và retreive vector data.
* **Guardrail chống memory poisoning:** Zep bảo vệ dữ liệu bằng cơ chế scope theo `user_id`, ngăn user này truy cập dữ liệu user khác (minh chứng qua E09). Hơn nữa, việc cập nhật `durable memory` (như các policy hay KB chung) nên thông qua Heartbeat an toàn (không tự tạo instruction) hoặc kiểm duyệt manual để tránh bị tiêm nhiễm độc hại.

## 2. Phân tích Benchmark

* **Layer có hit rate thấp nhất:** Semantic memory. Nếu lấy scope sai (như `scope="auto"` thay vì `episodes`), các marker quan trọng sẽ dễ dàng bị mất, làm hỏng hit rate.
* **Query lấy nhiều token nhất:** Case E07 (mixed) tiêu thụ nhiều token nhất vì phải kết hợp cả semantic context (quy định API) và long-term context (sở thích cá nhân).
* **Case mixed (E07) cần kết hợp memory nào?** Cần kết hợp `semantic memory` (để lấy evidence `Idempotency-Key` từ Knowledge Base chung) và `long-term memory` (để lấy evidence preference `Python` của user).
* **Token reduction so với full context:** `ContextBudgetManager` giúp reduction hiệu quả mà vẫn đạt hit rate cao nhờ lưu giữ những thông tin cô đọng nhất (Summary, edges). Ngược lại, `no-memory` baseline có độ reduction cực cao vì nó bỏ hết sạch các session cũ, dẫn tới hit rate thê thảm (0%).

## 3. Nhận xét về Recency và Compaction

* **E08 Recency:** Agent lấy thông tin mới nhất (BLUEBIRD-42, TypeScript) thay vì thông tin cũ, cho thấy tính năng thay thế (decay) hoạt động tốt.
* **E10 Compaction:** Dù raw data đã rơi khỏi short-term window, nhưng `durable note` vẫn giữ được deadline `16:00` nhờ việc tóm tắt hiệu quả.
