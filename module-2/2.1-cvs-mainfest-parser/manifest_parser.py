total_weight = 0.0
record_count = 0

file_name = "./shipping_manifest.csv"

with open(file_name, "r") as file:
    next(file) # Skips first line of the .csv file
    
    for line in file:
        tracking_id, carrier, weight_raw = line.strip().split(",")
        
        total_weight += float(weight_raw)
        
        record_count += 1
        
        print(f"TRACKING ID: {tracking_id} | CARRIER: {carrier} | WEIGHT: {weight_raw}kg")
        
print(f"""
========================================
Total Rows Processed: {record_count}
Total Manifest Weight: {total_weight}kg
========================================
""")