# Mock API - Clase 5

## Objetivo

Dar una alternativa local para los ejercicios de integracion cuando:

- no conviene depender de internet;
- no hay credenciales reales disponibles;
- se quiere practicar request, response, headers, variables de entorno y salida estructurada.

## Como levantarlo

```bash
export DEMO_API_KEY=demo-local-key
python mock_api/mock_service.py
```

## Endpoint de salud

```bash
curl http://127.0.0.1:8010/health
```

## Endpoint 1. Clasificar ticket

```bash
curl -X POST http://127.0.0.1:8010/v1/classify-ticket \
  -H "Content-Type: application/json" \
  -H "X-API-Key: demo-local-key" \
  -d '{"ticket_id":"INC-101","text":"Partner auth credential expired and requests are failing with 401"}'
```

## Endpoint 2. Extraer incidente

```bash
curl -X POST http://127.0.0.1:8010/v1/extract-incident \
  -H "Content-Type: application/json" \
  -H "X-API-Key: demo-local-key" \
  -d '{"instruction":"Return structured fields","text":"Payments API timeout after partner response exceeded 30 seconds."}'
```
