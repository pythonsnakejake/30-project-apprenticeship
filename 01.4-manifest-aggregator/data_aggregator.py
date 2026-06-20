def parse_manifest(raw_manifests):
    cleaned_batch = []

    for raw_line in raw_manifests:
        if "//" in raw_line:
            raw_id, raw_weight, raw_zone = raw_line.split("//")
        elif "," in raw_line:
            raw_id, raw_weight, raw_zone = raw_line.split(",")
        else:
            print("Unrecognized manifest format.")

        normalized_id = raw_id.strip().upper()
        normalized_weight = float(raw_weight)
        normalized_zone = raw_zone.strip().upper()
        

        