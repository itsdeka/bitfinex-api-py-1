from .types import InvoiceSubmission, CustomerInfo, Invoice

def parse_invoice_response(response):
    response["customer_info"] = CustomerInfo(
        nationality=response["customerInfo"]["nationality"],
        resid_country=response["customerInfo"]["residCountry"],
        resid_city=response["customerInfo"]["residCity"],
        resid_zip_code=response["customerInfo"]["residZipCode"],
        resid_street=response["customerInfo"]["residStreet"],
        full_name=response["customerInfo"]["fullName"],
        email=response["customerInfo"]["email"]
    )
    del response["customerInfo"]

    if "invoices" in response and response["invoices"] != None:
        for index, invoice in enumerate(response["invoices"]):
            response["invoices"][index] = Invoice(
                amount=response["invoices"][index]["amount"],
                address=response["invoices"][index]["address"],
                currency=response["invoices"][index]["currency"],
                pay_currency=response["invoices"][index]["payCurrency"],
                pool_currency=response["invoices"][index]["poolCurrency"],
            )

    response["order_id"] = response["orderId"]
    del response["orderId"]

    response["merchant_name"] = response["merchantName"]
    del response["merchantName"]

    response["pay_currencies"] = response["payCurrencies"]
    del response["payCurrencies"]

    return InvoiceSubmission(**response)