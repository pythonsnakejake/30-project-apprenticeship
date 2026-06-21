def monitor_sla_performance(operational_batch):

    for record in operational_batch:
        try:
            duration = record["shipped_hour"] - record["received_hour"]

            if duration < 0:
                raise ValueError("Shipped hour cannot be before recieved hour.")
            
            if duration > 24:
                status = "BREACH"
            else:
                status = "COMPLIANT"

        except TypeError as e:
            print("❌ DATA TYPE ERROR: Incompatible timestamp encountered.")
            continue

        except ValueError as e:
            print(f"❌ VALUE RANGE ERROR: {e}")
            continue