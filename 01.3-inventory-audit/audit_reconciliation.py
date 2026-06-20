inventory_batch = [{"item_id": "SKU-889", "cost": 45.00, "system_stock": 100, "physical_count": 100},
                   {"item_id": "SKU-412", "cost": 120.00, "system_stock": 50, "physical_count": 45},
                   {"item_id": "SKU-8115", "cost": 15.50, "system_stock": 20, "physical_count": 35}]

def reconcile_inventory(batch_list):
    for batch in batch_list:
        current_id = batch["item_id"]
        variance = batch["physical_count"] - batch["system_stock"]

        print(f"Item ID: {current_id} Variance: {variance}")
