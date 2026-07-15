# Resumen inicial del caso

Este archivo fue generado por `starter_triaje.py`.
Sirve para entender rapidamente los datos base, no para resolver el ejercicio completo.

## Archivos analizados

- Logs: `/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My Drive/Material propio/Curso IA Github Copilot/CursoIA/clase 6/Ejercicio avanzado 2/sample_runtime_logs.ndjson`
- Incidentes: `/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My Drive/Material propio/Curso IA Github Copilot/CursoIA/clase 6/Ejercicio avanzado 3/sample_incidents.json`

## Totales

- Registros de log: 7
- Incidentes: 5
- Logs sin correlation_id: 2
- Incidentes sin ticket_id: 1

## Logs por nivel

- ERROR: 4
- INFO: 1
- WARN: 2

## Logs por servicio

- billing: 4
- customer-sync: 2
- reporting: 1

## Incidentes por servicio

- [vacio]: 1
- billing: 1
- customer-sync: 1
- orders: 1
- reporting: 1

## Incidentes por severidad

- critical: 1
- high: 2
- low: 1
- medium: 1

## Incidentes por estado

- in_progress: 1
- open: 3
- resolved: 1

## Pistas para comenzar

- Revisa si los servicios con mas errores aparecen tambien en incidentes abiertos.
- Observa que campos faltan y como eso afecta el triage.
- Usa este resumen solo como punto de partida para tus archivos en `salidas/`.

## Siguiente paso sugerido

1. Lee este resumen.
2. Crea `lectura_manual.md` con tu primera interpretacion.
3. Luego usa skill y MCP para construir el resto de los entregables.
