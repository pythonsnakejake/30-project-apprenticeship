def calculated_fulfillment_fee(order_id, item_count, priority_client):
    if type(item_count) != int:
        print("❌ ERROR: Item count must be a whole integer.")
        return 
    
    if item_count <= 0:
        print("❌ ERROR: Item count must be greater than 0.")
        return

    if item_count <= 5:
        intial_price = 5.0
    elif item_count <= 20:
        intial_price = item_count * 4.50
    else:
        intial_price = item_count * 3.75

    if priority_client:
        intial_price *= 0.9

    final_price = intial_price + 1.5

    print(f"Total Price: £{final_price:.2f}")
