# OmniMart Logistics: CSV Shipping Manifest Ingestion Engine

## 🏢 Business Context

OmniMart Logistics receives volumetric tracking manifests daily from external dispatch networks. Manual extraction of freight data points via spreadsheet platforms can throttle dispatch queues, delay vehicle loading teams, and leave calculations vulnerable to manual input errors.

This system introduces a native, high-performance file-parsing component designed to stream comma-separated tracking files directly from disk storage, bypass text layout headers, and compile live batch metrics.

---

## ⚙️ Execution Pipeline

1. **Context Buffer Streaming:** Employs a file environment manager (`with open()`) to parse data line-by-line, bypassing system memory leaks.
2. **Cursor Displacement Control:** Tracks data positions using iterative functions (`next()`) to jump column descriptive metadata labels seamlessly.
3. **Floating-Point Isolation:** Caps summary calculation data types (`:.2f`) to immunize report displays against floating-point binary precision anomalies.

---

## 💻 Tech Stack & Specifications

- **Language:** Python 3.11+
- **File Operations:** Native context streaming buffers (`mode='r'`)
- **Formatting Controls:** Explicit rounding precision masks, string extraction systems
