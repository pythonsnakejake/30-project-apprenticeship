# OmniMart Logistics: Comprehensive Warehouse Data Ingestion & Audit Pipeline

## 🏢 Business Context

Legacy terminal systems across OmniMart distribution centers frequently dump unstable, unformatted text streams containing missing fields or data typos. Ingesting these raw data files directly into primary transactional databases introduces corruption, risking database crashes and facility processing downtime.

This script automates data sanitation and routing by streaming unverified legacy files, intercepting runtime validation errors defensively, and isolating clean records from corrupted rows using a multi-destination execution track.

---

## 🛠️ Performance Architecture

1. **Multi-Stream Context Isolation:** Spawns stacked file context managers (`with open()`) to handle reading, writing, and appending streams simultaneously, eliminating redundant system I/O opening overhead.
2. **Defensive Exception Insulation:** Enforces type safety via explicit `try/except ValueError` boundaries to catch and process runtime conversion anomalies natively without halting execution.
3. **Fault-Tolerant Uptime Control:** Deploys the loop-skipping `continue` keyword to bypass structural record failures instantly, ensuring an isolated bad row cannot truncate subsequent batch entries.
4. **Atomic Operational Telemetry:** Accumulates stream counters dynamically in memory, triggering a console-printed audit summary tracking data health across the entire operational batch.

---

## 💻 Tech Stack & Specifications

- **Language:** Python 3.11+
- **Data Synthesis:** Stream-isolated, multi-target ETL routing (O(1) space complexity)
- **Data Format:** Comma-Separated Values (CSV) and plain text logging
