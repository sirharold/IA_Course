from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
COURSE_ROOT = BASE_DIR.parents[1]
LOGS_PATH = COURSE_ROOT / "clase 6" / "Ejercicio avanzado 2" / "sample_runtime_logs.ndjson"
INCIDENTS_PATH = COURSE_ROOT / "clase 6" / "Ejercicio avanzado 3" / "sample_incidents.json"
OUTPUT_DIR = BASE_DIR / "salidas"
OUTPUT_FILE = OUTPUT_DIR / "resumen_datos_inicial.md"


def load_logs() -> list[dict]:
    rows = []
    for line in LOGS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def load_incidents() -> list[dict]:
    return json.loads(INCIDENTS_PATH.read_text(encoding="utf-8"))


def counter_lines(title: str, counts: Counter) -> list[str]:
    lines = [f"## {title}", ""]
    for key, value in sorted(counts.items()):
        label = key if key else "[vacio]"
        lines.append(f"- {label}: {value}")
    lines.append("")
    return lines


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    logs = load_logs()
    incidents = load_incidents()

    log_levels = Counter(row.get("level", "") for row in logs)
    log_services = Counter(row.get("service", "") for row in logs)
    missing_correlation = sum(1 for row in logs if not row.get("correlation_id"))
    incidents_by_service = Counter(row.get("service", "") for row in incidents)
    incidents_by_severity = Counter(row.get("severity", "") for row in incidents)
    incidents_by_state = Counter(row.get("state", "") for row in incidents)
    missing_ticket_id = sum(1 for row in incidents if not row.get("ticket_id"))

    lines = [
        "# Resumen inicial del caso",
        "",
        "Este archivo fue generado por `starter_triaje.py`.",
        "Sirve para entender rapidamente los datos base, no para resolver el ejercicio completo.",
        "",
        "## Archivos analizados",
        "",
        f"- Logs: `{LOGS_PATH}`",
        f"- Incidentes: `{INCIDENTS_PATH}`",
        "",
        "## Totales",
        "",
        f"- Registros de log: {len(logs)}",
        f"- Incidentes: {len(incidents)}",
        f"- Logs sin correlation_id: {missing_correlation}",
        f"- Incidentes sin ticket_id: {missing_ticket_id}",
        "",
    ]

    lines.extend(counter_lines("Logs por nivel", log_levels))
    lines.extend(counter_lines("Logs por servicio", log_services))
    lines.extend(counter_lines("Incidentes por servicio", incidents_by_service))
    lines.extend(counter_lines("Incidentes por severidad", incidents_by_severity))
    lines.extend(counter_lines("Incidentes por estado", incidents_by_state))

    lines.extend(
        [
            "## Pistas para comenzar",
            "",
            "- Revisa si los servicios con mas errores aparecen tambien en incidentes abiertos.",
            "- Observa que campos faltan y como eso afecta el triage.",
            "- Usa este resumen solo como punto de partida para tus archivos en `salidas/`.",
            "",
            "## Siguiente paso sugerido",
            "",
            "1. Lee este resumen.",
            "2. Crea `lectura_manual.md` con tu primera interpretacion.",
            "3. Luego usa skill y MCP para construir el resto de los entregables.",
            "",
        ]
    )

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Resumen generado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
