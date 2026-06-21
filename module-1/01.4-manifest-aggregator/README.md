# OmniMart Logistics: Multi-Client Manifest Aggregator

## 🏢 Business Context

OmniMart Logistics onboards disparate order manifest files daily from numerous external e-commerce clients. Because these external platforms rely on varying legacy standards, incoming data payloads arrive as raw, unformatted text strings utilizing conflicting case standards and structural delimiters.

This project implements an automated ingestion engine that detects varying streaming formats dynamically, sanitizes extraneous whitespace, normalizes alphanumeric values, and maps strings into uniform, relational-ready database records.

---

## 🚀 System Architecture

The application runs a clean string-cleansing pipeline:

1. **Dynamic Delimiter Analysis:** Runs internal condition checks to parse character markers (`//` vs `,`).
2. **Token Extraction:** Unpacks unformatted strings safely into localized structural tracking variables.
3. **Fault-Tolerant Skipping:** Utilizes custom control loop jumps (`continue`) to drop malformed input tracks safely while preserving execution continuity for valid records.

---

## 💻 Tech Stack & Specifications

- **Language:** Python 3.11+
- **String Utilities:** `.split()`, `.strip()`, `.upper()`
- **Control Infrastructure:** Conditional whitelisting, loop continuity routing
