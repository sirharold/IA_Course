import json
from pathlib import Path

from payment_review.normalizers import (
    normalize_channel,
    normalize_currency,
    normalize_customer_name,
)
from payment_review.reporting import build_review_summary
from payment_review.rules import evaluate_review


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATA_FILE = BASE_DIR / "data" / "sample_reviews.json"


def load_reviews(path=DEFAULT_DATA_FILE):
    with open(path, "r", encoding="utf-8") as file:
        payload = json.load(file)

    rows = []
    for item in payload:
        normalized = {
            "payment_id": item.get("payment_id", ""),
            "customer_name": normalize_customer_name(item.get("customer_name")),
            "amount": item.get("amount", 0),
            "currency": normalize_currency(item.get("currency")),
            "channel": normalize_channel(item.get("channel")),
            "tags": item.get("tags", []),
            "notes": item.get("notes", ""),
        }
        rows.append(normalized)
    return rows


def review_payments(path=DEFAULT_DATA_FILE):
    payments = load_reviews(path)
    output = []

    for payment in payments:
        review = evaluate_review(payment)
        packaged = {
            "raw": payment,
            "review": review,
        }
        packaged["summary"] = build_review_summary(packaged)
        output.append(packaged)

    return output


def print_report(path=DEFAULT_DATA_FILE):
    items = review_payments(path)
    print("PAYMENT REVIEW REPORT")
    print("=" * 60)

    for item in items:
        summary = item["summary"]
        print(summary["headline"])
        print(summary["detail"])
        print(f"Priority: {summary['priority']}")
        print("-" * 60)


if __name__ == "__main__":
    print_report()
