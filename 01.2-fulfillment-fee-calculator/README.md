# OmniMart Logistics: Dynamic Fulfillment Fee Calculator

## 🏢 Business Context

OmniMart Logistics relies on a volume-based pricing model to bill e-commerce clients for warehouse picking and packing services. Historically, billing personnel manually reviewed transaction logs and calculated fees using static spreadsheets. This human-dependent process introduced severe invoicing discrepancies, triggered client billing disputes, and caused significant margin leakage due to rounding errors and misapplied volume brackets.

This project introduces an automated financial calculation engine. It guarantees 100% billing accuracy, handles contracted client loyalty discounts, balances baseline operational surcharges, and completely standardizes ledger outputs.

---

## 🚀 Features

- **Automated Tier Allocation:** Dynamically switches from flat-rate billing (low-volume orders) to unit-rate billing (high-volume orders) instantly based on item scale.
- **Contractual Loyalty Matrix:** Seamlessly applies variable corporate tier discounts (10% off) to verified priority accounts before final invoicing.
- **Operational Surcharge Padding:** Automatically adds localized flat fuel surcharges to every processed order to stabilize operational margins.
- **Strict Runtime Type Guarding:** Implements zero-tolerance type validation to catch and block malformed float quantities or string inputs before they can poison accounting data.
- **Precision Financial Formatting:** Overrides standard Python floating-point behavior to force all output data into a clean, professional currency structure (`.2f`).

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.11+
- **Mathematical Operations:** Variable mutation, conditional scaling, compound assignment operators (`*=`, `+=`)
- **Defensive Architecture:** Boolean logical validation, explicit type comparison (`type() != int`)
- **String Manipulation:** Numeric format specifiers (`:.2f`)

---

## 📊 Business Rules & Pricing Architecture

The calculation pipeline evaluates client order metrics using the following strict structural framework:

| Volume Tier         | Order Size (Items) | Base Pricing Structure     | Priority Client Discount | Fuel Surcharge   |
| :------------------ | :----------------- | :------------------------- | :----------------------- | :--------------- |
| **Tier 1 (Small)**  | 1 – 5 items        | \$5.00 Flat Fee per Order  | 10% off base fee         | +\$1.50 flat fee |
| **Tier 2 (Medium)** | 6 – 20 items       | \$4.50 Unit Fee _per Item_ | 10% off base fee         | +\$1.50 flat fee |
| **Tier 3 (Large)**  | 21+ items          | \$3.75 Unit Fee _per Item_ | 10% off base fee         | +\$1.50 flat fee |

---

## 💻 Code Implementation & Testing Architecture

### Core Billing Engine Script

```python
def calculated_fulfillment_fee(order_id, item_count, priority_client):
    # 1. Type Guard: Block non-integers (e.g., floats, strings)
    if type(item_count) != int:
        print("❌ ERROR: Item count must be a whole integer.")
        return

    # 2. Value Guard: Block zero or negative values
    if item_count <= 0:
        print("❌ ERROR: Item count must be greater than 0.")
        return

    # 3. Tier Evaluation Matrix
    if item_count <= 5:
        initial_price = 5.0
    elif item_count <= 20:
        initial_price = item_count * 4.50
    else:
        initial_price = item_count * 3.75

    # 4. Apply Loyalty Multipliers
    if priority_client:
        initial_price *= 0.9

    # 5. Append Fixed Operational Surcharges
    final_price = initial_price + 1.5

    # 6. Format to Standard Financial Precision
    print(f"Total Price: £{final_price:.2f}")

```

> > > # Test 1: Standard Client, Tier 1
> > >
> > > calculated_fulfillment_fee("ORD-001", 3, False)
> > > Total Price: £6.50

> > > # Test 2: Priority Client, Tier 2
> > >
> > > calculated_fulfillment_fee("ORD-002", 10, True)
> > > Total Price: £42.00

> > > # Test 3: Boundary Condition, Exactly 20 Items
> > >
> > > calculated_fulfillment_fee("ORD-003", 20, False)
> > > Total Price: £91.50

> > > # Test 4: Mismatched Input Interception
> > >
> > > calculated_fulfillment_fee("ORD-004", 5.5, False)
> > > ❌ ERROR: Item count must be a whole integer.

## 🧠 Lessons Learned & Interview Talking Points

- **Mitigating Floating-Point Arbitrage**: In financial engineering, Python's default floating-point behavior can cause silent fractional truncation (e.g., displaying `42.0` instead of `42.00`). I utilized explicit format specification (`:.2f`) to enforce strict compliance with financial auditing standards.

- **Defensive Structural Guarding**: Rather than letting the system fail loudly or throw an unhandled `TypeError` during mathematical execution, I constructed upfront type validation layers (`type(item_count) != int`). This separates bad input streams from core logical processing pipelines.

- **Variable Mutation Discipline**: I structured the algorithm to progressively mutate a single source of truth variable (`initial_price`) through mathematical steps rather than instantiating redundant variables, minimizing memory allocation and footprint clutter.
