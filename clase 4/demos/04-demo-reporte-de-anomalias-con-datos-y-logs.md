# Demo 04 - Reporte de anomalias combinando datos y logs

## Objetivo

Consolidar anomalias de conciliacion y eventos de log en un reporte accionable que permita priorizar revision manual o siguiente iteracion tecnica.

## Artefactos de apoyo

- `../technical_automation_lab/anomaly_report.py`
- `../technical_automation_lab/data/runtime_logs.ndjson`
- `../technical_automation_lab/output/reconciliation_report.json`

## Resultado esperado

- Ejecutar `python3 anomaly_report.py`.
- Abrir `output/anomaly_report.md`.
- Revisar:
  - hallazgos priorizados;
  - evidencia de logs;
  - sugerencias de siguiente accion;
  - controles recomendados.
