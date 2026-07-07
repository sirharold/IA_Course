from __future__ import annotations


def build_partner_order(payload: dict) -> dict:
    customer = payload["customer"]
    address = customer["address"]

    return {
        "order_id": payload["orderId"],
        "created_at": payload.get("requestedAt"),
        "currency": payload["currency"],
        "amount": payload["amount"],
        "customer_document": customer["documentNumber"],
        "customer_name": customer["fullName"],
        "city": address["city"],
        "country": address["countryCode"],
        "line_items": [
            {
                "sku": item["sku"],
                "quantity": item["quantity"],
            }
            for item in payload["items"]
        ],
    }
