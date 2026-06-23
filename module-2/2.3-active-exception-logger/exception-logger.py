def log_transit_exceptions(shipment_batch):
    
    with open("./freight_exceptions.txt", "a") as file:
        for shipment in shipment_batch:
            if shipment["status"] != "In Transit":
                file.write(f"ID: {shipment['tracking_id']} | Carrier: {shipment['carrier']} | Status: {shipment['status']}\n") 