# OmniMart Logistics: SLA Breach Alert System

## 🏢 Business Context

OmniMart Logistics operates under tight contractual Service Level Agreements (SLAs), penalizing performance lag times extending beyond 24 hours from receipt to shipment. However, raw historical operations logs are manually input by facility users—leading to malformed entries, empty text fields, and impossible reverse-timed numbers.

This tracking application deploys an enterprise exception-handling grid that calculates operational performance windows, identifies SLA breaches, enforces logical range validation bounds, and isolates individual corrupted payloads to protect core processor uptime.

---

## 🛠️ Fault-Tolerant Architecture

The script processes active batches inside an isolated monitoring layer:

1. **Targeted Exception Blocks:** Avoids generic handler risks by utilizing discrete data type traps (`except TypeError`) and mathematical range filters (`except ValueError`).
2. **Volumetric Data Safeguards:** Intercepts logical anomalies (negative durations) upstream by dynamically triggering manual string alerts (`raise`).
3. **Loop Boundary Insulation:** Integrates directional execution skips (`continue`) directly within exception capture frames to process continuous logging streams seamlessly.

---

## 💻 Tech Stack & Specifications

- **Language:** Python 3.11+
- **Defensive Commands:** `try`, `except`, `raise`, `continue`
- **Error Classes:** `TypeError`, `ValueError`
