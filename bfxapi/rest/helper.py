from ..rest.types import CustomerInfo, InvoiceSubmission, Invoice

def parse_invoice_response(response):
    customer_info: CustomerInfo = CustomerInfo(
        nationality=response["customerInfo"]["nationality"],
        resid_country=response["customerInfo"]["residCountry"],
        resid_city=response["customerInfo"]["residCity"],
        resid_zip_code=response["customerInfo"]["residZipCode"],
        resid_street=response["customerInfo"]["residStreet"],
        full_name=response["customerInfo"]["fullName"],
        email=response["customerInfo"]["email"],
        tos_accepted=response["customerInfo"]["tosAccepted"],
        resid_building_no=response["customerInfo"].get("residBuildingNo")
    )

    invoices: List[Invoice] = []

    for invoice in response["invoices"]:
        invoices.append(Invoice(
            address=invoice["address"],
            amount=invoice["amount"],
            ext=invoice.get("ext"),
            pay_currency=invoice["payCurrency"],
            pool_currency=invoice["poolCurrency"]
        ))

    return InvoiceSubmission(
        id=response["id"],
        type=response["type"],
        t=response["t"],
        duration=response["duration"],
        amount=response["amount"],
        currency=response["currency"],
        order_id=response["orderId"],
        pay_currencies=response["payCurrencies"],
        status=response["status"],
        customer_info=customer_info,
        invoices=invoices
    )