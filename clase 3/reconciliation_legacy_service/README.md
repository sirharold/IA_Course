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
- `.github/copilot-instructions.md`
- `docs/incident-investigation-template.md`
- `docs/change-plan-template.md`
- `sql/schema.sql`
- `sql/investigation_queries.sql`
- `sql/fix_scripts.sql`
- `scripts/build_reconciliation_db.py`
- `etl/run_gateway_etl.py`
- `tests/test_smoke.py`

## Ejecucion

```bash
python3 main.py
```

## SQLite local para ejercicios de datos

Puedes crear una base SQLite local sin costo usando:

```bash
python3 scripts/build_reconciliation_db.py
sqlite3 artifacts/reconciliation.db
```

Luego puedes correr consultas desde:

- `sql/investigation_queries.sql`
- `sql/fix_scripts.sql`

## ETL local para clase

Puedes ejecutar una mini tarea ETL sin costo usando:

```bash
python3 etl/run_gateway_etl.py
```

Eso genera:

- `artifacts/gateway_transactions_clean.csv`
- `artifacts/gateway_rejects.csv`

## Notas

- El proyecto contiene decisiones tecnicas discutibles a proposito.
- La documentacion no coincide siempre con el codigo.
- Los datos de entrada tienen problemas reales de formato.
- Los logs no entregan toda la observabilidad que seria deseable.
- Tambien incluye un mini flujo SQL para consultas y scripts de correccion pequeños.
- Tambien incluye una mini tarea ETL para limpiar y clasificar datos de entrada.
