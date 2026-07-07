from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Dict, List


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def load_reconciliation_anomalies(report_path: Path) -> List[Dict[str, str]]:
    if not report_path.exists():
        return []
    payload = json.loads(report_path.read_text(encoding="utf-8"))
    return payload.get("anomalies", [])


def load_runtime_logs(log_path: Path) -> List[Dict[str, str]]:
    records: List[Dict[str, str]] = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))
    return records


def build_markdown_report(anomalies: List[Dict[str, str]], logs: List[Dict[str, str]]) -> str:
    anomaly_counter = Counter(item["type"] for item in anomalies)
    log_counter = Counter(item["level"] for item in logs)

    lines = [
        "# Reporte de anomalias",
        "",
        "## Resumen",
        "",
        f"- Anomalias de conciliacion: {len(anomalies)}",
        f"- Eventos de log: {len(logs)}",
        f"- Niveles de log: {dict(log_counter)}",
        "",
        "## Tipos de anomalia",
        "",
    ]

    for anomaly_type, count in sorted(anomaly_counter.items()):
        lines.append(f"- {anomaly_type}: {count}")

    lines.extend(
        [
            "",
            "## Eventos relevantes",
            "",
        ]
    )

    for record in logs:
        if record["level"] in {"warning", "error"}:
            lines.append(f"- [{record['level']}] {record['event']} :: {record['message']}")

    lines.extend(
        [
            "",
            "## Controles sugeridos",
            "",
            "- Revisar anomalias repetidas por `external_ref`.",
            "- Confirmar si discrepancias de estado corresponden a fases validas del negocio.",
            "- Verificar si los warnings de parsing aparecen sobre las mismas referencias que las anomalias de conciliacion.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    anomalies = load_reconciliation_anomalies(OUTPUT_DIR / "reconciliation_report.json")
    logs = load_runtime_logs(DATA_DIR / "runtime_logs.ndjson")
    report = build_markdown_report(anomalies, logs)
    output_path = OUTPUT_DIR / "anomaly_report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Anomaly report written to {output_path}")


if __name__ == "__main__":
    main()
