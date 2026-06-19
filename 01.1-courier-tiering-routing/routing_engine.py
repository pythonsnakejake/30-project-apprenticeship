def route_package(package_id, weight, destination_zone, sla):
    formatted_sla = sla.lower()
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
    else:
        print("SLA or weight is incorrect. Please try again.")