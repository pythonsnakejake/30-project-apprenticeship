def run_data_pipeline(feed_file):
    clean_records_count = 0 
    error_records_count = 0
    
    with open(feed_file, "r") as source, \
         open("./data/sanatized_inventory.csv", "w") as clean_log, \
         open("./data/ingestion_errors.txt", "a") as error_log:
            clean_log.write("Item_ID,Item_Name,Quantity,Weight\n")
            next(source)
            
            for line in source:
                try:
                    Item_ID, Item_Name, quantity_raw, weight_raw = line.strip().split(",")
                    quantity = int(quantity_raw)
                    weight = float(weight_raw)
                    clean_log.write(f"{Item_ID},{Item_Name},{quantity},{weight:.2f}\n")
                    
                    clean_records_count += 1
                except ValueError: 
                    error_log.write(line)
                    error_records_count += 1
                    continue
                
    print(f"""========================================
       DATA PIPELINE AUDIT REPORT       
========================================
Successful Rows Exported: {clean_records_count}
Corrupted Rows Logged:   {error_records_count}
========================================""")

run_data_pipeline("./data/raw_warehouse_feed.txt")