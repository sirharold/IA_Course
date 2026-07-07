from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

TX_REF_PATTERN = re.compile(r"(TX-\d+)", re.IGNORECASE)
ORDER_REF_PATTERN = re.compile(r"(PO-\d+)", re.IGNORECASE)


def load_reconciliation_anomalies(report_path: Path) -> List[Dict[str, Any]]:
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


def extract_reference(message: str, pattern: re.Pattern[str]) -> str:
    match = pattern.search(message)
    return normalize_reference(match.group(1)) if match else ""


def normalize_reference(value: str) -> str:
    return "".join(ch for ch in value.upper() if ch.isalnum())


def priority_for_anomaly(anomaly: Dict[str, Any], related_logs: List[Dict[str, str]]) -> str:
    anomaly_type = anomaly["type"]
    if anomaly_type in {"missing_in_gateway", "missing_in_core"}:
        return "high"
    if any(item["level"] == "error" for item in related_logs):
        return "high"
    if anomaly_type in {"status_mismatch", "amount_mismatch"}:
        return "medium"
    return "medium" if related_logs else "low"


def next_action_for_anomaly(anomaly: Dict[str, Any]) -> str:
    actions = {
        "missing_in_gateway": "revisar si la exportacion del gateway quedo incompleta o si hubo desfase de corte",
        "missing_in_core": "confirmar si el core omitio el registro o si la referencia pertenece a otro proceso",
        "status_mismatch": "validar si la pareja de estados corresponde a una fase permitida del flujo",
        "amount_mismatch": "comparar reglas de redondeo, moneda y fuente del monto",
        "customer_ref_mismatch": "revisar normalizacion y origen de `customer_ref` antes de reconciliar",
    }
    return actions.get(anomaly["type"], "revisar evidencia adicional antes de cerrar una conclusion")


def build_prioritized_findings(anomalies: List[Dict[str, Any]], logs: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []

    for anomaly in anomalies:
        external_ref = normalize_reference(str(anomaly.get("external_ref", "")))
        related_logs = [
            record
            for record in logs
            if external_ref and external_ref == extract_reference(record["message"], TX_REF_PATTERN)
        ]
        findings.append(
            {
                "kind": "reconciliation_anomaly",
                "reference": external_ref or anomaly.get("gateway_record_id") or anomaly.get("core_record_id", "n/a"),
                "type": anomaly["type"],
                "priority": priority_for_anomaly(anomaly, related_logs),
                "detail": anomaly.get("detail")
                or f"core={anomaly.get('core_amount', anomaly.get('core_customer_ref', 'n/a'))} gateway={anomaly.get('gateway_amount', anomaly.get('gateway_customer_ref', 'n/a'))}",
                "supporting_logs": related_logs,
                "next_action": next_action_for_anomaly(anomaly),
            }
        )

    for record in logs:
        order_ref = extract_reference(record["message"], ORDER_REF_PATTERN)
        if not order_ref:
            continue
        findings.append(
            {
                "kind": "integration_signal",
                "reference": order_ref,
                "type": record["event"],
                "priority": "high" if record["level"] == "error" else "medium",
                "detail": record["message"],
                "supporting_logs": [record],
                "next_action": "comparar este payload con el contrato esperado antes de reintentar la integracion",
            }
        )

    priority_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(findings, key=lambda item: (priority_order[item["priority"]], item["reference"], item["type"]))


def build_markdown_report(anomalies: List[Dict[str, Any]], logs: List[Dict[str, str]]) -> str:
    anomaly_counter = Counter(item["type"] for item in anomalies)
    log_counter = Counter(item["level"] for item in logs)
    prioritized = build_prioritized_findings(anomalies, logs)

    lines = [
        "# Reporte de anomalias",
        "",
        "## Resumen",
        "",
        f"- Anomalias de conciliacion: {len(anomalies)}",
        f"- Eventos de log: {len(logs)}",
        f"- Niveles de log: {dict(log_counter)}",
        f"- Hallazgos priorizados: {len(prioritized)}",
        "",
        "## Tipos de anomalia",
        "",
    ]

    for anomaly_type, count in sorted(anomaly_counter.items()):
        lines.append(f"- {anomaly_type}: {count}")

    lines.extend(
        [
            "",
            "## Hallazgos priorizados",
            "",
        ]
    )

    for item in prioritized:
        lines.append(
            f"- [{item['priority']}] {item['type']} | ref={item['reference']} | accion={item['next_action']}"
        )
        lines.append(f"  - detalle: {item['detail']}")
        if item["supporting_logs"]:
            evidence = ", ".join(
                f"{record['level']}:{record['event']}" for record in item["supporting_logs"]
            )
            lines.append(f"  - evidencia: {evidence}")

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
            "- Revisar anomalias repetidas por `external_ref` y no solo por tipo.",
            "- Confirmar si discrepancias de estado corresponden a fases validas del negocio o a un bug real.",
            "- Registrar referencias explicitas en logs de integracion para poder correlacionar payloads y anomalias sin lectura manual.",
            "- Mantener separadas las evidencias observables de las recomendaciones operativas.",
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
