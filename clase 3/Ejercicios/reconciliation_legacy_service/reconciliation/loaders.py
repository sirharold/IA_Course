import csv
from pathlib import Path

from reconciliation.utils import normalize_amount, normalize_currency, normalize_external_id


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_transactions(path):
    rows = []
    with open(path, "r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader, start=2):
            rows.append(
                {
                    "row_number": index,
                    "external_id": normalize_external_id(row.get("external_id")),
                    "amount": normalize_amount(row.get("amount")),
                    "currency": normalize_currency(row.get("currency")),
                    "source": row.get("source", ""),
                    "status": row.get("status", ""),
                    "captured_at": row.get("captured_at", ""),
                }
            )
    return rows


def load_core_transactions():
    return load_transactions(DATA_DIR / "core_transactions.csv")


def load_gateway_transactions(filename="gateway_transactions.csv"):
    return load_transactions(DATA_DIR / filename)
