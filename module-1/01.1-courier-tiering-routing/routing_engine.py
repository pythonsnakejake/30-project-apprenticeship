def route_package(package_id, weight, destination_zone, sla):
    formatted_sla = sla.strip().lower()

    recognized_sla = ["overnight", "express", "standard"]

    if weight <= 0:
        print("❌ ERROR: Weight must be greater than 0. Please try again.")
        return

    if formatted_sla not in recognized_sla:
        print("❌ ERROR: SLA not recognised. Please try again.")
        return
    
    if formatted_sla == "overnight":
        courier = "NextDay Air"
    elif formatted_sla == "express":
        if weight > 5.0:
            courier = "Atlas Freight"
        else:
            courier = "RapidPost Express"
    elif formatted_sla == "standard":
        if weight > 5.0:
            courier = "Atlas Ground"
        else:
            courier = "RapidPost Eco"

    print(f"Package {package_id} routed via {courier}")

# --- MANUAL TEST SUITE ---
# Test Case 1: Standard Weight, Overnight SLA
route_package("PKG-001", 2.5, "Zone A", "Overnight")

# Test Case 2: Heavy Weight, Express SLA
route_package("PKG-002", 12.4, "Zone B", "Express")

# Test Case 3: Edge Case, Boundary Weight (Exactly 5.0kg), Standard SLA
route_package("PKG-003", 5.0, "Zone C", "Standard")

# Test Case 4: Invalid Input, Negative Weight
route_package("PKG-004", -1.0, "Zone A", "Express")

