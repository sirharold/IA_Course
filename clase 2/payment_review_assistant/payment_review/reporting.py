from payment_review.normalizers import normalize_channel


def build_review_summary(review):
    x = review["review"]
    raw = review["raw"]

    score = x["score"]
    status = x["status"]
    reasons = x["reasons"]
    customer_name = raw.get("customer_name", "")
    amount = raw.get("amount", 0)
    currency = raw.get("currency", "CLP")
    channel = normalize_channel(raw.get("channel"))

    if status == "needs_manual_review":
        priority = "high"
    elif status == "monitor":
        priority = "medium"
    else:
        priority = "low"

    if reasons:
        rs = ", ".join(reasons)
    else:
        rs = "no visible reasons"

    headline = f"{customer_name or 'Unknown customer'} - {status}"
    detail = (
        f"Score {score}. "
        f"Amount {amount} {currency}. "
        f"Channel {channel}. "
        f"Reasons: {rs}."
    )

    return {
        "headline": headline,
        "detail": detail,
        "priority": priority,
        "status": status,
        "score": score,
    }
