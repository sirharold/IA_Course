# Demo 01 - Conciliacion inteligente entre dos fuentes operativas

## Objetivo

Mostrar como automatizar el cruce entre dos exportaciones que deberian representar el mismo proceso, pero no usan exactamente las mismas convenciones de nombres, estados o referencias.

## Artefactos de apoyo

- `../technical_automation_lab/reconcile_transactions.py`
- `../technical_automation_lab/data/core_transactions.csv`
- `../technical_automation_lab/data/gateway_transactions.csv`
- `../technical_automation_lab/.github/prompts/reconcile-anomalies.prompt.md`

## Resultado esperado

- Ejecutar `python3 reconcile_transactions.py`.
- Abrir `output/reconciliation_report.json`.
- Discutir matching, anomalias reales, falsos positivos y validaciones faltantes.
