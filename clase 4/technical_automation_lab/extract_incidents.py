from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
OUTPUT_DIR = BASE_DIR / "output"


FIELD_PATTERN = re.compile(r"^(Incidente|Servicio|Severidad|Fecha|Sintoma|Causa probable|Accion tomada):\s*(.*)$")


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


def extract_incidents(document_path: Path) -> List[Dict[str, str]]:
    raw_text = document_path.read_text(encoding="utf-8")
    return [parse_block(block) for block in split_blocks(raw_text)]


def main() -> None:
    source_path = DOCS_DIR / "incident_report_export.txt"
    incidents = extract_incidents(source_path)
    output_path = OUTPUT_DIR / "incidents_structured.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(incidents, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"Structured incidents written to {output_path}")
    print(json.dumps({"records": len(incidents)}, indent=2))


if __name__ == "__main__":
    main()
