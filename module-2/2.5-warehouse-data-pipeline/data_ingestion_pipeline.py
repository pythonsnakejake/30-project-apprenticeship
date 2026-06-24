def run_data_pipeline(feed_file):
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
                    
                except ValueError: 
                    error_log.write(line)
                    continue

run_data_pipeline("./data/raw_warehouse_feed.txt")