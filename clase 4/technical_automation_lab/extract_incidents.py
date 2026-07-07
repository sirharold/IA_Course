from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
OUTPUT_DIR = BASE_DIR / "output"

FIELD_PATTERN = re.compile(r"^(Incidente|Servicio|Severidad|Fecha|Sintoma|Causa probable|Accion tomada):\s*(.*)$")
REQUIRED_FIELDS = {"incidente", "servicio", "severidad", "fecha", "sintoma"}
ALLOWED_SEVERITIES = {"alta", "media", "baja"}


def split_blocks(raw_text: str) -> List[str]:
    chunks = [block.strip() for block in raw_text.split("\n---\n")]
    return [block for block in chunks if block]


def parse_block(block: str) -> Dict[str, str]:
    record: Dict[str, str] = {}
    notes: List[str] = []
    current_key = ""

    for line in block.splitlines():
        match = FIELD_PATTERN.match(line.strip())
        if match:
            current_key = match.group(1).lower().replace(" ", "_")
            record[current_key] = match.group(2).strip()
            continue

        if current_key:
            record[current_key] = f"{record[current_key]} {line.strip()}".strip()
        elif line.strip():
            notes.append(line.strip())

    if notes:
        record["unparsed_notes"] = " ".join(notes)
    return record


def assess_record(record: Dict[str, str]) -> Dict[str, Any]:
    missing_required = sorted(field for field in REQUIRED_FIELDS if not record.get(field))
    doubtful_fields: List[Dict[str, str]] = []
    high_confidence_fields: List[str] = []

    for key, value in record.items():
        if key == "unparsed_notes":
            doubtful_fields.append({"field": key, "reason": "contains free-form text outside the expected pattern"})
            continue

        if not value:
            doubtful_fields.append({"field": key, "reason": "field was parsed but is empty"})
            continue

        if key == "severidad" and value.lower() not in ALLOWED_SEVERITIES:
            doubtful_fields.append({"field": key, "reason": "severity is outside the expected catalog"})
            continue

        high_confidence_fields.append(key)

    if missing_required:
        for field in missing_required:
            doubtful_fields.append({"field": field, "reason": "required field was not found in the source block"})

    if missing_required:
        confidence = "low"
    elif doubtful_fields:
        confidence = "medium"
    else:
        confidence = "high"

    return {
        "confidence": confidence,
        "review_required": bool(doubtful_fields),
        "high_confidence_fields": sorted(high_confidence_fields),
        "doubtful_fields": doubtful_fields,
        "missing_required_fields": missing_required,
    }


def extract_incidents(document_path: Path) -> List[Dict[str, Any]]:
    raw_text = document_path.read_text(encoding="utf-8")
    records: List[Dict[str, Any]] = []
    for block in split_blocks(raw_text):
        record = parse_block(block)
        record["quality_assessment"] = assess_record(record)
        records.append(record)
    return records


def main() -> None:
    source_path = DOCS_DIR / "incident_report_export.txt"
    incidents = extract_incidents(source_path)
    output_path = OUTPUT_DIR / "incidents_structured.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(incidents, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"Structured incidents written to {output_path}")
    print(
        json.dumps(
            {
                "records": len(incidents),
                "review_required": sum(1 for item in incidents if item["quality_assessment"]["review_required"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
