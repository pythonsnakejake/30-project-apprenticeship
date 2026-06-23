def generate_route_master(route_data):
    
    with open("./route_master.csv", "w") as file:
        file.write("Hub,Carrier,Zone\n")

        for route in route_data:        
            row_fields = [route['hub'], route['carrier'], route['zone']]
            
            row_string = ",".join(row_fields) + "\n"
            
            file.write(row_string)
            
# --- PRIMARY HARDWARE CONVEYOR MAP MATRIX ---
conveyor_map = [
    {"hub": "Midlands Hub", "carrier": "DHL Express", "zone": "MID-01"},
    {"hub": "London South", "carrier": "FedEx Freight", "zone": "LON-04"},
    {"hub": "Northwest Gate", "carrier": "Royal Mail", "zone": "NW-09"},
    {"hub": "Scotland Central", "carrier": "APC Overland", "zone": "SCO-02"}
]

print("--- GENERATING HARDWARE ROUTE MASTER CSV ---")
generate_route_master(conveyor_map)
print("[SUCCESS] route_master.csv compiled natively and written to disk!")

