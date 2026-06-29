def normalize_customer_name(raw_name):
    if raw_name is None:
        return ""

    text = str(raw_name).strip()
    if not text:
        return ""

    parts = text.replace("_", " ").replace("-", " ").split()
    clean_parts = []
    for part in parts:
        if len(part) <= 2:
            clean_parts.append(part.upper())
        else:
            clean_parts.append(part[0].upper() + part[1:].lower())
    return " ".join(clean_parts)


def normalize_channel(channel):
    if channel is None:
        return "unknown"

    value = str(channel).strip().lower()
    aliases = {
        "webapp": "web",
        "browser": "web",
        "app": "mobile",
        "ios": "mobile",
        "android": "mobile",
    }
    return aliases.get(value, value or "unknown")


def normalize_currency(currency):
    if not currency:
        return "CLP"

    value = str(currency).strip().upper()
    if value == "$":
        return "CLP"
    if value == "USD$":
        return "USD"
    return value
