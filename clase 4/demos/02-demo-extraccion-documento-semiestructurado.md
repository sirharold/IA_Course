# Demo 02 - Extraccion estructurada desde documento tecnico semiestructurado

## Objetivo

Convertir un documento exportado desde una fuente imperfecta en una salida JSON revisable, util para triage o automatizacion posterior.

## Artefactos de apoyo

- `../technical_automation_lab/extract_incidents.py`
- `../technical_automation_lab/docs/incident_report_export.txt`

## Resultado esperado

- Ejecutar `python3 extract_incidents.py`.
- Abrir `output/incidents_structured.json`.
- Revisar campos estructurados, `quality_assessment`, confianza y necesidad de revision manual.
