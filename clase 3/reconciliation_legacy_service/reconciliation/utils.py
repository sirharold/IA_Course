from decimal import Decimal, InvalidOperation


def normalize_external_id(raw_value):
    if raw_value is None:
        return ""
    return str(raw_value).strip()


def normalize_currency(raw_value):
    if raw_value is None:
        return "CLP"

    value = str(raw_value).strip().upper()
    aliases = {
        "$": "CLP",
        "PESO": "CLP",
        "PESOS": "CLP",
        "USD$": "USD",
    }
    return aliases.get(value, value or "CLP")


def normalize_amount(raw_value):
    if raw_value is None:
        return Decimal("0")

    text = str(raw_value).strip()
    if not text:
        return Decimal("0")

    sanitized = text.replace("$", "").replace(",", "")
    try:
        return Decimal(sanitized)
    except InvalidOperation as error:
        raise ValueError(f"Invalid amount: {raw_value}") from error


def build_composite_key(row):
    return (
        normalize_external_id(row.get("external_id")),
        normalize_currency(row.get("currency")),
        normalize_amount(row.get("amount")),
    )
