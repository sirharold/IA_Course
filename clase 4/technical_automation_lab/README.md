# Codigo base - Clase 4

Este directorio contiene artefactos para demos y ejercicios de la clase 4.

## Objetivo

Trabajar automatizaciones donde Copilot aporte algo mas que autocompletado:

- conciliacion entre fuentes con nomenclaturas distintas;
- extraccion estructurada desde texto exportado de documentos;
- reconstruccion de contratos implicitos desde codigo y payloads;
- generacion de reportes de anomalias combinando datos y logs.

## Estructura

- `reconcile_transactions.py`
  - conciliacion entre dos fuentes operativas.
- `extract_incidents.py`
  - extraccion de incidentes desde texto semiestructurado.
- `derive_contract_candidates.py`
  - comparacion entre lo que espera el codigo y lo que entregan payloads de ejemplo.
- `anomaly_report.py`
  - consolidacion de anomalias y logs en un reporte.
- `data/`
  - fuentes tabulares y logs.
- `contracts/`
  - codigo y payloads para la demo de desarrollo.
- `docs/`
  - documento exportado para extraccion.
- `.github/`
  - ejemplos de `copilot-instructions`, `instructions` y `prompt files`.

## Ejecucion sugerida

```bash
python3 reconcile_transactions.py
python3 extract_incidents.py
python3 derive_contract_candidates.py
python3 anomaly_report.py
```

## Criterio didactico

El codigo busca ser:

- suficientemente realista para discutir decisiones tecnicas;
- lo bastante pequeno para manipularlo en clase;
- intencionalmente mejorable con ayuda de Copilot.
