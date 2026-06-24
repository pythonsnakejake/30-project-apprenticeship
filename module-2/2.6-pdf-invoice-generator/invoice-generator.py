import os
from weasyprint import HTML

def compile_pdf_invoice(client_data, output_pdf_path):
    
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    os.makedirs("./invoices", exist_ok=True)
    
    client_name = client_data['client_name']
    order_count = int(client_data['order_count'])
    subtotal = float(client_data['subtotal'])
    tax_amount = float(client_data['tax_amount'])
    total_due = float(client_data['total_due'])
    
    hmt_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <lang
        <style>
            @page {{ size: A4; margin: 20mm 15mm; }}
            body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #2d3748; line-height: 1.6; }}
            h1 {{ color: #1a365d; border-bottom: 2px solid #2b6cb0; padding-bottom: 10px; text-transform: uppercase; }}
            .meta-table {{ display: table; width: 100%; margin-top: 20px; border-collapse: collapse; }}
            .meta-row {{ display: table-row; }}
            .meta-cell {{ display: table-cell; width: 50%; padding: 8px 0; vertical-align: top; }}
            .data-table {{ width: 100%; margin-top: 30px; border-collapse: collapse; }}
            .data-table th {{ background-color: #2b6cb0; color: white; padding: 10px; text-align: left; }}
            .data-table td {{ padding: 10px; border-bottom: 1px solid #e2e8f0; }}
            .text-right {{ text-align: right; }}
        </style>
    </head>
    <body>
        <h1>OmniMart Logistics Invoices</h1>
        
        <div class="meta-table">
            <div class="meta-row">
                <div class="meta-cell">
                    <strong>Billed To:</strong><br>
                    {client_name}<br>
                    Fulfillment Partner Account
                </div>
                <div class="meta-cell text-right">
                    <strong>Invoice Status:</strong> UNPAID<br>
                    <strong>Generated Date:</strong> 2026-06-24
                </div>
            </div>
        </div>

        <table class="data-table">
            <thead>
                <tr>
                    <th>Operational Metric Field</th>
                    <th class="text-right">Volume / Absolute Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Base Order Fulfillment Ingestion Tier</td>
                    <td class="text-right">{order_count} Orders</td>
                </tr>
                <tr>
                    <td>Subtotal Line Item Assessment</td>
                    <td class="text-right">£{subtotal:.2f}</td>
                </tr>
                <tr>
                    <td>VAT / Tax Amount Evaluation (20%)</td>
                    <td class="text-right">£{tax_amount:.2f}</td>
                </tr>
                <tr style="font-weight: bold; color: #1a365d; font-size: 12pt;">
                    <td>Total Account Amount Due</td>
                    <td class="text-right" style="border-top: 2px solid #2b6cb0;">£{total_due:.2f}</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    """

    with open("./invoices/invoice_template.html", "w") as f:
        f.write(hmt_content)
        
    HTML("./invoices/invoice_template.html").write_pdf(output_pdf_path)
    print(f"[SUCCESS] Invoice successfully compiled and exported to: {output_pdf_path}")
    
# --- SYSTEM RUNTIME GATEWAY ---
# Test data payload definition
test_payload = {
    "client_name": "Samuels Inc", 
    "order_count": 150, 
    "subtotal": 300.0, 
    "tax_amount": 60.0, 
    "total_due": 360.0
}

# Fire script from the global scope with BOTH required structural parameters
compile_pdf_invoice(test_payload, "./invoices/samuels_invoice.pdf")