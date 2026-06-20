inventory_batch = [{"item_id": "SKU-889", "cost": 45.00, "system_stock": 100, "physical_count": 100},
                   {"item_id": "SKU-412", "cost": 120.00, "system_stock": 50, "physical_count": 45},
                   {"item_id": "SKU-8115", "cost": 15.50, "system_stock": 20, "physical_count": 35}]

def reconcile_inventory(batch_list):
    for batch in batch_list:
        current_id = batch["item_id"]
        variance = batch["physical_count"] - batch["system_stock"]
        batch_cost = batch["cost"]
        alert_flag = ""

        if variance == 0:
            status = "BALANCED"
        elif variance < 0:
            status = "SHRINKAGE"
        else:
            status = "OVERAGE"

        financial_impact = abs(variance * batch_cost)

        if status == "SHRINKAGE" and financial_impact > 500.00:
            alert_flag += "🚨 ALERT: High-Value Loss! Investigation Required!"

        parts = [
            f"ITEM ID: {current_id}",
            f"STATUS: {status}",
            f"VARIANCE: {variance}",
            f"FINANCIAL IMPACT: £{financial_impact}",
        ]

        if alert_flag:
            parts.append(f"ALERT: {alert_flag}")

        print("\n" + " | ".join(parts))

reconcile_inventory(inventory_batch)