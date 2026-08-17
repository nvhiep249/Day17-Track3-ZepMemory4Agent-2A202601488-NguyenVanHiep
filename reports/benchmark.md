# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1276.8 ms**
- Average token reduction vs full source context: **1.5%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 1399.6 | 570 | 0.0% |  |
| E09 | long_term | PASS | 1387.2 | 793 | 0.0% |  |
| E10 | short_term | PASS | 0.4 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1384.5 | 1351 | 0.0% |  |
| E03 | long_term | PASS | 1781.7 | 1344 | 0.0% |  |
| E04 | episodic | PASS | 286.3 | 223 | 0.0% |  |
| E05 | episodic | PASS | 305.5 | 185 | 16.3% |  |
| E07 | mixed | PASS | 4813.6 | 581 | 0.0% |  |
| E11 | semantic | PASS | 881.5 | 657 | 0.0% |  |
| E08 | long_term | PASS | 1804.7 | 1326 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempoten`

### E09 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot for backend development.  Lan prefers Java and Spring Boot and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  For BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python should not be used. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 09:35:15     Source: message     Content: [`

### E03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  For BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python should not be used. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 09:35:08     Source: message     Content: [`

### E04 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua minh cho vui thoi. Truoc khi minh chon template va cai dependen EPISODE: Minh dang chuan bi tu on lai phan async cua Python vi tuan sau co bai kiem tra nho, ma minh thi hoc kieu de vao dau lai de troi ra lam neu chi doc chu suong. Neu lat nua ban phai giai thich cho minh n EPISODE: Toi nay min`

### E05 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Sang mai minh phai hop review tien do voi mentor nen toi nay minh muon don dep lai het may thu con dang do. Minh biet minh con vai viec chua chot xong nhung dau oc dang roi qua khong nho het. Ban lam  EPISODE: Toi nay minh muon viet cho tron ven cai retry payment ma vua dung so thich stack ca nhan cua minh, vua theo dung policy thanh toan chinh thuc, vua tranh dam lai dung cai su co async ma lan truoc minh  EPISODE: Voi demo ca`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  For BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python should not be used. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 09:35:34     Source: message   `

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= ENTITY: timeout - When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency b`

### E08 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  For BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python should not be used. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: message     Content: [`
