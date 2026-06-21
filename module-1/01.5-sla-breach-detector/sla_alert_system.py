def monitor_sla_performance(operational_batch):

    for record in operational_batch:
        try:
            duration = record["shipped_hour"] - record["received_hour"]
 
            if duration < 0:
                raise ValueError("Shipped hour cannot be before received hour.")
            
            if duration > 24:
                status = "BREACH"
            else:
                status = "COMPLIANT"

            print(f"ORDER ID: {record['order_id']} | DURATION: {duration}h | STATUS: {status}")

        except TypeError as e:
            print("❌ DATA TYPE ERROR: Incompatible timestamp encountered.")
            continue

        except ValueError as e:
            print(f"❌ VALUE RANGE ERROR: {e}")
            continue

# --- LOGISTICS PERFORMANCE REAL-WORLD STREAM ---
friday_logs = [
    {"order_id": "ORD-501", "received_hour": 8, "shipped_hour": 12},      # Compliant
    {"order_id": "ORD-502", "received_hour": 6, "shipped_hour": 34},      # Breach (>24h)
    {"order_id": "ORD-503", "received_hour": 10, "shipped_hour": "22"},   # TypeError (String)
    {"order_id": "ORD-504", "received_hour": 18, "shipped_hour": 14},      # ValueError (Negative)
    {"order_id": "ORD-505", "received_hour": 9, "shipped_hour": 20}       # Compliant
]

print("--- STARTING CRASH-PROOF LOGISTICS SLA AUDIT ---")
monitor_sla_performance(friday_logs)

