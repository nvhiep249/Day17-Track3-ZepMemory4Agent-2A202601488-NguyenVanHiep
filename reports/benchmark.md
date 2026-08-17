# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **2**
- Passed: **2/2**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **619.5 ms**
- Average token reduction vs full source context: **52.9%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E06 | semantic | PASS | 762.1 | 252 | 45.1% |  |
| E11 | semantic | PASS | 476.9 | 222 | 60.7% |  |

## Evidence excerpts

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. ENTITY: POST /payments - POST /payments requires requests to send the same Idempotency-Key for every retryable request. Retries should only occur for HTTP 429 or transient 5xx errors, using exponential backoff, and stopping after a maximum of three retries. This is designated by Marker PAYMENT-RULE-3. ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors using exponential-backoff`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. ENTITY: timeout - When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. ENTITY: Async HTTP Incident Playbook - When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. ENTITY: transient 5xx errors - "Fo`
