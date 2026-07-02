# ETL mini task

## Objetivo

Simular una tarea cotidiana de datos:

- extraer transacciones desde CSV;
- transformarlas con reglas pequenas y visibles;
- cargar una salida limpia para analisis o conciliacion.

## Flujo

1. Extract:
   - `data/gateway_transactions_dirty.csv`
2. Transform:
   - trim de `external_id`
   - normalizacion de `currency`
   - limpieza basica de `amount`
   - clasificacion de filas invalidas
3. Load:
   - `artifacts/gateway_transactions_clean.csv`
   - `artifacts/gateway_rejects.csv`

## Ejecucion

```bash
python3 etl/run_gateway_etl.py
```
