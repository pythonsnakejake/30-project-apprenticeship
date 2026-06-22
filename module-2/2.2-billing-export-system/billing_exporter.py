def export_billing_report(client_name, order_count, subtotal, tax_amount):
    total_due = float(subtotal) + float(tax_amount)
    
    with open("daily_billing_report.txt", "w") as file:
        file.write("========================================\n")
        file.write(f"Client Name: {client_name}\n")
        file.write(f"Total Orders: {order_count}\n")
        file.write("----------------------------------------\n")
        file.write(f"Subtotal: £{subtotal:.2f}\n")
        file.write(f"Tax Amount: £{tax_amount:.2f}\n")
        file.write(f"Total Amount Due: £{total_due:.2f}\n")
        file.write("========================================\n")
        