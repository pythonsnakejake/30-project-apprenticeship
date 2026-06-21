# OmniMart Logistics: Core Operations & Scripting Core (Module 1)

## 🏢 Portfolio Overview

This repository contains the foundational core of the automated logistics data pipeline built for **OmniMart Logistics**, a high-volume third-party fulfillment (3PL) operator.

Throughout Module 1, the primary focus was transitioning manual, error-prone supply chain monitoring tools (Excel spreadsheets, text logs, manual billing calculations) into **fault-tolerant, robust Python scripts**. These prototypes address specific business vulnerabilities—ranging from financial margin leakage and inventory shrinkage to data onboarding bottlenecks and contractual SLA penalties.

---

## 🛠️ Global Core Competencies Mastered

- **Defensive Input Validation:** Engineering strict type-checking parameters (`type() is not int`) and constraint barriers to prevent malformed runtime inputs.
- **Complex Data Structures:** Parsing and managing structured, nested tracking data using Python collection primitives (`list[dict]`).
- **Fault-Tolerant System Architecture:** Isolating processing routines inside target exceptions grids (`try / except / raise`) to sustain continuous script uptime.
- **Token Serialization & Normalization:** Tokenizing unstructured, multi-client raw text strings and cleaning string formatting data layout drifts.

---

## 📂 Core Project Registry

### 🏎️ 1.1: Dispatch Courier Routing Optimization Matrix

- **Operational Intent:** Automatically routes order packages to the correct delivery provider based on weight bounds and critical destination markers.
- **Core Mechanics:** Nested logical branching operators (`if / elif / else`), boolean logic variables, and inline variable modifications.
- **Business KPI Impact:** Reduced logistics handling delays by eliminating manual sorting rules and human parsing misclassifications.

### 🏢 1.2: Dynamic Fulfillment Fee Calculation Engine

- **Operational Intent:** Calculates precision client picking-and-packing invoicing costs across multi-tier volume discount brackets.
- **Core Mechanics:** Sequential scaling boundaries, variable mutation, contractual loyalty parameter multipliers, and float precision formatting specifiers (`:.2f`).
- **Business KPI Impact:** Protected corporate revenue margins by eliminating floating-point rounding arithmetic errors and unapplied tiered fees.

### 🗃️ 1.3: Warehouse Inventory Audit Reconciliation Pipeline

- **Operational Intent:** Reconciles manual physical warehouse inventory counts against live central tracking system database balances.
- **Core Mechanics:** Dictionary traversal pipelines, incremental asset loss variance multipliers, absolute value magnitude processing (`abs()`), and stream text array formatting (`" | ".join()`).
- **Business KPI Impact:** Isolated high-priority stock shrinkage discrepancies exceeding £500.00 instantly, reducing asset protection delay queues.

### 📲 1.4: Multi-Client Manifest Text Stream Aggregator

- **Operational Intent:** Ingests unformatted daily shipping manifest lines from varying incoming client formats, standardizing data profiles on the fly.
- **Core Mechanics:** Multi-delimiter inspection parsing (`in`), string splitting (`.split()`), element unpacking, whitespace stripping (`.strip()`), casing normalization (`.upper()`), and loop skip execution controls (`continue`).
- **Business KPI Impact:** Reduced data-onboarding configuration delays from hours to seconds for legacy e-commerce partners.

### 🛡️ 1.5: Resilient SLA Breach Tracking & Alert System

- **Operational Intent:** Scans warehouse handling durations to track contractual fulfillment deadlines while intercepting highly corrupt logging entries.
- **Core Mechanics:** Error-trapping blocks (`try / except`), explicit context exception triggers (`raise ValueError`), and independent loop error isolation boundaries.
- **Business KPI Impact:** Eliminated data-driven script crashes while highlighting operational contract breaches to avoid severe SLA regulatory penalties.

---

## 🖥️ System Performance & Verification Grid

Below is the verified production output stream capturing the fault-tolerant, unified pipelines processing live operational data:

```text
--- RUNNING COURIER ROUTER MATRIX (PROJ 1.1) ---
[SUCCESS] Route Confirmed: DHL Express | Cost: £10.50

--- RUNNING FINANCE ENGINE VERIFICATION (PROJ 1.2) ---
Total Price: £6.50
Total Price: £42.00
Total Price: £91.50

--- RUNNING WAREHOUSE AUDIT REGISTRY (PROJ 1.3) ---
ITEM ID: SKU-889 | STATUS: BALANCED | VARIANCE: 0 | FINANCIAL IMPACT: £45.0
ITEM ID: SKU-412 | STATUS: SHRINKAGE | VARIANCE: -5 | FINANCIAL IMPACT: £600.0 | ALERT: 🚨 ALERT: High-Value Loss! Investigation Required!

--- RUNNING MANIFEST INGESTION BATCH (PROJ 1.4) ---
[
  {'manifest_id': 'AA-9910', 'weight': 4.55, 'zone': 'ZONE_EAST'},
  {'manifest_id': 'BB-2214', 'weight': 12.8, 'zone': 'ZONE_WEST'}
]

--- STARTING CRASH-PROOF LOGISTICS SLA AUDIT (PROJ 1.5) ---
ORDER ID: ORD-501 | DURATION: 4h | STATUS: COMPLIANT
ORDER ID: ORD-502 | DURATION: 28h | STATUS: BREACH
❌ DATA TYPE ERROR: Incompatible timestamp encountered.
❌ VALUE RANGE ERROR: Shipped hour cannot be before received hour.
```

## 🧠 Core Software Engineering Principles Applied

1. **The Principle of Least Surprise**: Standardizing string cases (`.upper()`) and forced float rounding constraints (`:.2f`) ensures downstream database tools consume predictable variables.

2. **Defensive Filtering Over Loud Failures**: Using targeted type guarding blocks instead of blanket python catches preserves corporate runtime integrity while flagging bad data footprints cleanly.

3. **Control Loop Isolation**: Implementing `continue` statements alongside scoped `try/except` statements inside collection sweeps blocks localized corrupt input rows from freezing core warehouse processors.
