def parse_manifest(raw_manifests):
    cleaned_batch = []

    for raw_line in raw_manifests:
        if "//" in raw_line:
            raw_id, raw_weight, raw_zone = raw_line.split("//")
        elif "," in raw_line:
            raw_id, raw_weight, raw_zone = raw_line.split(",")
        else:
            print("Unrecognized manifest format.")

        cleaned_batch.append({
            "manifest_id": raw_id.strip().upper(),
            "weight": float(raw_weight),
            "zone": raw_zone.strip().upper()
        })
        
    return cleaned_batch

# --- SYSTEM VERIFICATION STREAM ---
raw_incoming_stream = [
    "AA-9910//4.55//zone_east",
    "  bb-2214 , 12.80 , zone_west  ",
    "AA-5512//1.20//zone_north",
    "bb-8841 ,   0.95 , zone_south  "
]

print("--- RUNNING MANIFEST INGESTION BATCH ---")
processed_data = parse_manifest(raw_incoming_stream)
print(processed_data)
        