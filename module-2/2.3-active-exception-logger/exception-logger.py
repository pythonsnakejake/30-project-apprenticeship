def log_transit_exceptions(shipment_batch):
    
    staged_lines = []
    for shipment in shipment_batch:
        if shipment["status"] != "In Transit":
            line = f"ID: {shipment['tracking_id']} | Carrier: {shipment['carrier']} | Status: {shipment['status']}\n"
            staged_lines.append(line)
            
    if staged_lines:
        with open("./freight_exceptions.txt", "a") as file:
            file.writelines(staged_lines)
                
# --- ACTIVE TRANSIT STREAMS (RUN 1: MORNING BATCH) ---
morning_stream = [
    {"tracking_id": "TRK-A1", "carrier": "DHL", "status": "In Transit"},
    {"tracking_id": "TRK-A2", "carrier": "FedEx", "status": "Customs Hold"},
    {"tracking_id": "TRK-A3", "carrier": "DHL", "status": "Damaged In Transit"}
]

# --- ACTIVE TRANSIT STREAMS (RUN 2: AFTERNOON BATCH) ---
afternoon_stream = [
    {"tracking_id": "TRK-B1", "carrier": "Royal Mail", "status": "In Transit"},
    {"tracking_id": "TRK-B2", "carrier": "FedEx", "status": "Address Discrepancy"}
]

print("--- RUNNING MORNING AUTOMATED LOGGING GATES ---")
log_transit_exceptions(morning_stream)

print("--- RUNNING AFTERNOON AUTOMATED LOGGING GATES ---")
log_transit_exceptions(afternoon_stream)

print("[SUCCESS] Bidirectional Exception Logger Active!")

