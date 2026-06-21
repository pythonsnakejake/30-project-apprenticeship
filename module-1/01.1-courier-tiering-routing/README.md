# OmniMart Logistics: Courier Tiering & Routing Engine

## 🏢 Business Context

OmniMart Logistics is a rapidly growing third-party logistics (3PL) and e-commerce fulfillment provider handling thousands of daily orders. Historically, warehouse staff manually selected courier carriers and service levels at packing stations. This manual intervention introduced human error, created severe packing lane bottlenecks, and caused significant margin leakage due to accidental selection of premium shipping tiers for low-priority parcels.

This project automates the carrier allocation process by creating a deterministic routing engine that instantly maps package attributes to the most cost-efficient courier tier that meets client service level agreements (SLAs).

---

## 🚀 Features

- **Automated Allocation Logic:** Instantly processes package weight and delivery targets to assign the optimal courier service.
- **Defensive Edge-Case Guarding:** Uses defensive coding patterns (Guard Clauses) to intercept invalid operations data—such as negative weights or unrecognized delivery tiers—before processing.
- **Input Normalization:** Implements structural string scrubbing (`.lower()` and `.strip()`) to handle erratic manual data entry or malformed system inputs smoothly.
- **Scalable Whitelisting:** Leverages explicit list-membership checking for tier validation, allowing frictionless expansion when new shipping partners are onboarded.

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.11+
- **Core Paradigms:** Functional Programming, Defensive Design, String Cleansing
- **Control Structures:** Conditional trees (`if / elif / else`), Logical operators (`and`, `not in`)

---

## 📊 Operational Architecture & Business Rules

The routing engine evaluates package parameters based on the following operational routing hierarchy:

| SLA Tier      | Weight Class        | Assigned Courier      | Business Justification                                |
| :------------ | :------------------ | :-------------------- | :---------------------------------------------------- |
| **Overnight** | Any Weight          | **NextDay Air**       | Absolute speed priority under legal SLA contract.     |
| **Express**   | Heavy (> 5.0 kg)    | **Atlas Freight**     | High weight capacity vehicle routing required.        |
| **Express**   | Standard (≤ 5.0 kg) | **RapidPost Express** | Speed optimization for standard parcel cargo.         |
| **Standard**  | Heavy (> 5.0 kg)    | **Atlas Ground**      | Bulk ground freight tracking for weight efficiencies. |
| **Standard**  | Standard (≤ 5.0 kg) | **RapidPost Eco**     | Maximum margin retention for low-priority cargo.      |

---

## 💻 Code Architecture & Usage

### Sample Implementation

```python
def route_package(package_id, weight, destination_zone, sla):
    # 1. Normalize inputs
    formatted_sla = sla.strip().lower()
    recognized_sla = ["overnight", "express", "standard"]

    # 2. Guard Clauses for defensive data filtering
    if weight <= 0:
        print("❌ ERROR: Weight must be greater than 0. Please try again.")
        return

    if formatted_sla not in recognized_sla:
        print("❌ ERROR: SLA not recognised. Please try again.")
        return

    # 3. Deterministic execution tree
    if formatted_sla == "overnight":
        courier = "NextDay Air"
    elif formatted_sla == "express":
        if weight > 5.0:
            courier = "Atlas Freight"
        else:
            courier = "RapidPost Express"
    elif formatted_sla == "standard":
        if weight > 5.0:
            courier = "Atlas Ground"
        else:
            courier = "RapidPost Eco"

    print(f"Package {package_id} routed via {courier}")

```

### Example Verification Console Outputs

```
>>> route_package("PKG-001", 2.5, "Zone A", "Overnight")
Package PKG-001 routed via NextDay Air

>>> route_package("PKG-002", 12.4, "Zone B", "Express")
Package PKG-002 routed via Atlas Freight

>>> route_package("PKG-004", -1.0, "Zone A", "Express")
❌ ERROR: Weight must be greater than 0. Please try again.
```

## 🧠 Lessons Learned & Interview Talking Points

- **Defensive Architecture Over Troubleshooting**: By placing validation criteria at the absolute entry point of the function, the script prevents silent, downstream data corruption in logistics ledgers. It handles failures cleanly without system crashes.

- **Elimination of Dead Code (Refactoring Debt)**: Initial design iterations contained fallback else logic traps at the root of the conditional tree. Code auditing revealed these structures were mathematically unreachable due to the upstream whitelisting architecture. Removing this dead code optimized code legibility and maintainability.

- **String Optimization**: In production, data formats change or contain white space. Adding .strip().lower() mitigates basic pipeline ingestion errors before processing.

## 🔮 Future Architecture Evolution

- **Database Transition**: Migrate hardcoded whitelists out of script runtime and move configuration states into relational tables (SQLite / PostgreSQL).

- **API Integration**: Refactor print outcomes into structured payload objects (dict) to feed automated label printing APIs over webhooks.
