# Reconciliation Legacy Service

Mini servicio legado preparado para la clase 3 del curso.

## Objetivo didactico

Este proyecto existe para practicar:

- comprension de codigo existente;
- analisis de dependencias y supuestos de datos;
- lectura de logs e incidentes;
- separacion entre hechos, inferencias e incertidumbres;
- propuestas de mejora pequenas;
- diseno de pruebas desde riesgos observados.

## Estructura

- `main.py`
- `reconciliation/service.py`
- `reconciliation/loaders.py`
- `reconciliation/matcher.py`
- `reconciliation/reporting.py`
- `reconciliation/utils.py`
- `data/core_transactions.csv`
- `data/gateway_transactions.csv`
- `data/gateway_transactions_dirty.csv`
- `logs/reconciliation_error.log`
- `logs/reconciliation_warning.log`
- `docs/reconciliation_rules.md`
- `tests/test_smoke.py`

## Ejecucion

```bash
python3 main.py
```

## Notas

- El proyecto contiene decisiones tecnicas discutibles a proposito.
- La documentacion no coincide siempre con el codigo.
- Los datos de entrada tienen problemas reales de formato.
- Los logs no entregan toda la observabilidad que seria deseable.
