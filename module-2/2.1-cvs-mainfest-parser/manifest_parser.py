total_weight = 0.0

file_name = "./shipping_manifest.csv"

with open(file_name, "r") as file:
    next(file)
    
    for line in file:
        tracking_id, carrier, weight_raw = line.strip().split(",")
        
        print(f"TRACKING ID: {tracking_id} | CARRIER: {carrier} | WEIGHT: {weight_raw}kg")