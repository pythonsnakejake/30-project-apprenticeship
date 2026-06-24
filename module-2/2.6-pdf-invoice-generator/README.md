# OmniMart Logistics: Automated PDF/Text Invoice Generator

## 🏢 Business Context

OmniMart's corporate finance teams require clean, consistent, and audit-ready billing documents to invoice corporate partners. Manual spreadsheet exports or text summaries look unprofessional and risk introducing structural layout drift, visual clipping, or currency truncation errors.

This script automates invoice creation by dynamically mapping raw operational database streams directly into an immutable, corporate-branded PDF document with perfect structural alignment.

---

## 🛠️ Performance Architecture

1. **Uncoupled Presentation Layers:** Strictly insulates core numerical tracking operations from presentation strings, allowing float values to maintain calculation precision until formatting inside the template.
2. **Cross-Platform Vector Rendering:** Bypasses unpredictable dynamic web frameworks in favor of an explicit CSS table-grid layout configuration, ensuring the document renders identically on all systems.
3. **Idempotent Storage Initialization:** Uses automated directory path tracking configurations (`os.makedirs`) to dynamically establish missing output locations before triggering file stream flushes.

---

## 💻 Tech Stack & Specifications

- **Language:** Python 3.11+
- **Data Synthesis:** Dynamic HTML paged-media template mapping paired with WeasyPrint binary generation
- **Data Format:** Vector PDF Documents (.pdf) and temporary layout assets (.html)
