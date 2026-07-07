from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, Iterable, List, Optional


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


@dataclass
class Transaction:
    source: str
    record_id: str
    external_ref: str
    customer_ref: str
    amount: Decimal
    currency: str
    status: str
    occurred_at: str


def normalize_text(value: str) -> str:
    return "".join(ch for ch in value.strip().lower() if ch.isalnum())


def parse_amount(raw_value: str) -> Decimal:
    normalized = raw_value.strip().replace("$", "").replace(",", "")
    try:
        return Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid amount: {raw_value}") from exc


def load_transactions(csv_path: Path, source: str) -> List[Transaction]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        items: List[Transaction] = []
        for row in rows:
            items.append(
                Transaction(
                    source=source,
                    record_id=row["record_id"],
                    external_ref=normalize_text(row["external_ref"]),
                    customer_ref=normalize_text(row["customer_ref"]),
                    amount=parse_amount(row["amount"]),
                    currency=row["currency"].strip().upper(),
                    status=row["status"].strip().lower(),
                    occurred_at=row["occurred_at"].strip(),
                )
            )
        return items


def index_by_external_ref(items: Iterable[Transaction]) -> Dict[str, Transaction]:
    return {item.external_ref: item for item in items}


def amounts_close(left: Decimal, right: Decimal, tolerance: Decimal = Decimal("1.00")) -> bool:
    return abs(left - right) <= tolerance


def classify_status_mismatch(core_status: str, gateway_status: str) -> Optional[str]:
    valid_pairs = {
        ("approved", "settled"),
        ("approved", "authorized"),
        ("reversed", "voided"),
    }
    if core_status == gateway_status:
        return None
    if (core_status, gateway_status) in valid_pairs:
        return None
    return f"status mismatch: core={core_status} gateway={gateway_status}"


def reconcile(core_items: List[Transaction], gateway_items: List[Transaction]) -> Dict[str, object]:
    gateway_by_ref = index_by_external_ref(gateway_items)
    matched: List[Dict[str, object]] = []
    anomalies: List[Dict[str, object]] = []

    seen_gateway_refs = set()
    for core_item in core_items:
        gateway_item = gateway_by_ref.get(core_item.external_ref)
        if gateway_item is None:
            anomalies.append(
                {
                    "type": "missing_in_gateway",
                    "external_ref": core_item.external_ref,
                    "core_record_id": core_item.record_id,
                    "detail": "transaction exists in core but not in gateway export",
                }
            )
            continue

        seen_gateway_refs.add(gateway_item.external_ref)
        record = {
            "external_ref": core_item.external_ref,
            "core_record_id": core_item.record_id,
            "gateway_record_id": gateway_item.record_id,
            "customer_match": core_item.customer_ref == gateway_item.customer_ref,
            "amount_match": core_item.amount == gateway_item.amount,
            "status_pair": [core_item.status, gateway_item.status],
        }

        status_issue = classify_status_mismatch(core_item.status, gateway_item.status)
        if status_issue:
            record["status_issue"] = status_issue

        if core_item.customer_ref != gateway_item.customer_ref:
            anomalies.append(
                {
                    "type": "customer_ref_mismatch",
                    "external_ref": core_item.external_ref,
                    "core_customer_ref": core_item.customer_ref,
                    "gateway_customer_ref": gateway_item.customer_ref,
                }
            )

        if not amounts_close(core_item.amount, gateway_item.amount):
            anomalies.append(
                {
                    "type": "amount_mismatch",
                    "external_ref": core_item.external_ref,
                    "core_amount": str(core_item.amount),
                    "gateway_amount": str(gateway_item.amount),
                }
            )

        if status_issue:
            anomalies.append(
                {
                    "type": "status_mismatch",
                    "external_ref": core_item.external_ref,
                    "detail": status_issue,
                }
            )

        matched.append(record)

    for gateway_item in gateway_items:
        if gateway_item.external_ref not in seen_gateway_refs:
            anomalies.append(
                {
                    "type": "missing_in_core",
                    "external_ref": gateway_item.external_ref,
                    "gateway_record_id": gateway_item.record_id,
                    "detail": "transaction exists in gateway export but not in core export",
                }
            )

    return {
        "summary": {
            "core_records": len(core_items),
            "gateway_records": len(gateway_items),
            "matched_records": len(matched),
            "anomaly_count": len(anomalies),
        },
        "matched_records": matched,
        "anomalies": anomalies,
    }


def write_json(output_path: Path, payload: Dict[str, object]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def main() -> None:
    core_items = load_transactions(DATA_DIR / "core_transactions.csv", "core")
    gateway_items = load_transactions(DATA_DIR / "gateway_transactions.csv", "gateway")
    result = reconcile(core_items, gateway_items)
    output_path = OUTPUT_DIR / "reconciliation_report.json"
    write_json(output_path, result)
    print(f"Reconciliation written to {output_path}")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
