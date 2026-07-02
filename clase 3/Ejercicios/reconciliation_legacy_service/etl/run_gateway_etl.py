import csv
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from reconciliation.utils import normalize_currency, normalize_external_id

INPUT_FILE = BASE_DIR / "data" / "gateway_transactions_dirty.csv"
ARTIFACTS_DIR = BASE_DIR / "artifacts"
CLEAN_FILE = ARTIFACTS_DIR / "gateway_transactions_clean.csv"
REJECT_FILE = ARTIFACTS_DIR / "gateway_rejects.csv"


def clean_amount(raw_value):
    if raw_value is None:
        return "", "missing_amount"

    text = str(raw_value).strip()
    if not text:
        return "", "missing_amount"

    sanitized = text.replace("$", "").replace(" ", "")
    if sanitized.upper().startswith("USD"):
        sanitized = sanitized[3:]

    if sanitized.count(".") == 1 and sanitized.replace(".", "").isdigit():
        left, right = sanitized.split(".")
        if len(right) == 3:
            sanitized = left + right

    if sanitized.isdigit():
        return sanitized, ""

    return text, "invalid_amount_format"


def run_etl():
    ARTIFACTS_DIR.mkdir(exist_ok=True)

    clean_rows = []
    rejected_rows = []

    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader, start=2):
            external_id = normalize_external_id(row.get("external_id"))
            amount_clean, error_code = clean_amount(row.get("amount"))
            currency = normalize_currency(row.get("currency"))

            transformed = {
                "row_number": index,
                "external_id": external_id,
                "amount_raw": row.get("amount", ""),
                "amount_clean": amount_clean,
                "currency": currency,
                "status": row.get("status", ""),
                "captured_at": row.get("captured_at", ""),
            }

            if error_code:
                transformed["reject_reason"] = error_code
                rejected_rows.append(transformed)
            else:
                clean_rows.append(transformed)

    write_csv(
        CLEAN_FILE,
        clean_rows,
        [
            "row_number",
            "external_id",
            "amount_raw",
            "amount_clean",
            "currency",
            "status",
            "captured_at",
        ],
    )
    write_csv(
        REJECT_FILE,
        rejected_rows,
        [
            "row_number",
            "external_id",
            "amount_raw",
            "amount_clean",
            "currency",
            "status",
            "captured_at",
            "reject_reason",
        ],
    )

    print(f"clean_rows={len(clean_rows)}")
    print(f"rejected_rows={len(rejected_rows)}")
    print(CLEAN_FILE)
    print(REJECT_FILE)


def write_csv(path, rows, fieldnames):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run_etl()
