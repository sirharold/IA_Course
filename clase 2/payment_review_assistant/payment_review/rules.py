HIGH_AMOUNT_BY_CURRENCY = {
    "CLP": 800000,
    "USD": 1200,
    "EUR": 1100,
}

BLOCKED_TAGS = {
    "fraud_watch",
    "chargeback",
}


def evaluate_review(record):
    amount = float(record.get("amount", 0))
    currency = record.get("currency", "CLP")
    tags = record.get("tags", [])
    channel = record.get("channel", "unknown")

    reasons = []
    score = 0

    threshold = HIGH_AMOUNT_BY_CURRENCY.get(currency, 900000)
    if amount >= threshold:
        score += 35
        reasons.append(f"high_amount:{currency}")

    if channel == "unknown":
        score += 15
        reasons.append("missing_channel")

    if channel == "mobile" and amount > threshold * 0.8:
        score += 15
        reasons.append("high_mobile_amount")

    if any(tag in BLOCKED_TAGS for tag in tags):
        score += 40
        reasons.append("blocked_tag")

    if record.get("customer_name", "").strip() == "":
        score += 10
        reasons.append("missing_customer_name")

    if score >= 60:
        status = "needs_manual_review"
    elif score >= 35:
        status = "monitor"
    else:
        status = "approved"

    return {
        "score": score,
        "status": status,
        "reasons": reasons,
    }
