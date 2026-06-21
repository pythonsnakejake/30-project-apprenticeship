def calculated_fulfillment_fee(order_id, item_count, priority_client):
    if type(item_count) != int:
        print("❌ ERROR: Item count must be a whole integer.")
        return 
    
    if item_count <= 0:
        print("❌ ERROR: Item count must be greater than 0.")
        return

    if item_count <= 5:
        initial_price = 5.0
    elif item_count <= 20:
        initial_price = item_count * 4.50
    else:
        initial_price = item_count * 3.75

    if priority_client:
        initial_price *= 0.9

    final_price = initial_price + 1.5

    print(f"Total Price: £{final_price:.2f}")

# --- MANUAL TEST SUITE ---
print("--- RUNNING FINANCE ENGINE VERIFICATION ---")

# Test 1: Standard Client, Tier 1 (Flat rate)
print("Test 1 (Expected: £6.50):")
calculated_fulfillment_fee("ORD-001", 3, False)

# Test 2: Priority Client, Tier 2 (Unit rate + 10% off + surcharge)
print("\nTest 2 (Expected: £42.00):")
calculated_fulfillment_fee("ORD-002", 10, True)

# Test 3: Boundary Limit, Exactly 20 items, Standard Client
print("\nTest 3 (Expected: £91.50):")
calculated_fulfillment_fee("ORD-003", 20, False)

# Test 4: Defensive Guard, Type Mismatch Float
print("\nTest 4 (Expected: Type Error):")
calculated_fulfillment_fee("ORD-004", 5.5, False)

