# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1208.0 ms**
- Average token reduction vs full source context: **12.2%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.5 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1344.0 | 708 | 0.0% |  |
| G09 | semantic | PASS | 508.0 | 223 | 51.4% |  |
| G10 | semantic | PASS | 525.3 | 214 | 53.4% |  |
| G14 | mixed | PASS | 1732.7 | 534 | 0.0% |  |
| G03 | long_term | PASS | 1574.4 | 1314 | 0.0% |  |
| G04 | long_term | PASS | 1416.5 | 1316 | 0.0% |  |
| G07 | episodic | PASS | 286.9 | 143 | 35.3% |  |
| G08 | episodic | PASS | 262.3 | 154 | 30.3% |  |
| G11 | mixed | PASS | 1932.9 | 581 | 0.0% |  |
| G13 | mixed | PASS | 786.3 | 410 | 27.4% |  |
| G15 | mixed | PASS | 2107.1 | 732 | 0.0% |  |
| G16 | mixed | PASS | 1779.9 | 559 | 1.1% |  |
| G17 | mixed | PASS | 1872.7 | 559 | 1.1% |  |
| G18 | mixed | PASS | 763.2 | 420 | 25.7% |  |
| G19 | mixed | PASS | 1646.6 | 536 | 5.1% |  |
| G05 | long_term | PASS | 1429.9 | 1450 | 0.0% |  |
| G12 | mixed | PASS | 2283.9 | 554 | 12.3% |  |
| G20 | mixed | PASS | 1906.6 | 684 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot for backend development.  Lan prefers Java and Spring Boot and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, J`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. ENTITY: Agent Memory Privacy Rule - Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store, marked as DELETE-VERIFY-ALL. ENTITY: transient 5xx errors -  ENTITY: Async HTTP Incident Playbook - When async HTTP calls time out, inspect connec`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot for backend development.  Lan prefers Java and Spring Boot and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu:`

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency.  The user prefers Python over Java and requests that code explanations include concise examples. For explanations involving async/await and coroutines versus Tasks, the user wants the information presented in a timeline format.  The user wants explanations of coroutines and Tasks to be presented as a timeline. </USER_SUMMARY>  <EPISODES> Episodes ar`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency.  The user prefers Python over Java and requests that code explanations include concise examples. For explanations involving async/await and coroutines versus Tasks, the user wants the information presented in a timeline format.  The user wants explanations of coroutines and Tasks to be presented as a timeline. </USER_SUMMARY>  <EPISODES> Episodes ar`

### G07 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.`

### G08 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency. They found that reusing the aiohttp ClientSession and setting concurrency to 20 resolved the issue, identifying the main problem as connection churn rather than the timeout threshold. This is related to the ASYNC-FIX-20 incident.  The user prefers Python over Java and requests that code explanations include concise examples. For explanat`

### G13 - mixed

`<EPISODIC> EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. </EPISODIC>  <SEMANTIC> EPISODE: When async HTTP calls time out, inspect c`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency. They found that reusing the aiohttp ClientSession and setting concurrency to 20 resolved the issue, identifying the main problem as connection churn rather than the timeout threshold. This is related to the ASYNC-FIX-20 incident.  The user prefers Python over Java and requests that code explanations include concise examples. For explanat`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency. They found that reusing the aiohttp ClientSession and setting concurrency to 20 resolved the issue, identifying the main problem as connection churn rather than the timeout threshold. This is related to the ASYNC-FIX-20 incident.  The user prefers Python over Java and requests that code explanations include concise examples. For explanat`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency. They found that reusing the aiohttp ClientSession and setting concurrency to 20 resolved the issue, identifying the main problem as connection churn rather than the timeout threshold. This is related to the ASYNC-FIX-20 incident.  The user prefers Python over Java and requests that code explanations include concise examples. For explanat`

### G18 - mixed

`<EPISODIC> EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. </EPISODIC>  <SEMANTIC> EPISODE: W`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They need to complete a benchmark report, LAB-REPORT-1600, before Friday at 16:00. Currently, the user is debugging async HTTP and has attempted to increase the timeout to 60 seconds without success. The user is also investigating connection pool and client lifecycle with concurrency. They found that reusing the aiohttp ClientSession and setting concurrency to 20 resolved the issue, identifying the main problem as connection churn rather than the timeout threshold. This is related to the ASYNC-FIX-20 incident.  The user prefers Python over Java and requests that code explanations include concise examples. For explanat`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is also working on debugging async HTTP issues related to the ASYNC-FIX-20 incident, specifically concerning connection churn and client session reuse with aiohttp, which resolved issues previously attributed to timeout thresholds.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  When explaining async/awa`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is also working on debugging async HTTP issues related to the ASYNC-FIX-20 incident, specifically concerning connection churn and client session reuse with aiohttp, which resolved issues previously attributed to timeout thresholds.  The user prefers Python over Java. For async/await and coroutines versus Tasks, the user wants explanations presented in a timeline format and requests that code explanations include concise examples.  When explaini`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
