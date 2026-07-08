# Ejercicio avanzado 1 - API por ambiente y cliente con `.env`

## Objetivo

Consumir una API local que responde distinto segun el ambiente llamador y ejecutar el mismo cliente con `.env.development`, `.env.staging` y `.env.production`.

## Archivos principales

- `service.py`
- `advanced_env_client.py`
- `.env.development.example`
- `.env.staging.example`
- `.env.production.example`

## Lo que deben hacer

- levantar la API local;
- crear sus archivos `.env` a partir de los `.example`;
- ejecutar el mismo cliente en tres ambientes;
- comparar diferencias de respuesta;
- mejorar el cliente con ayuda de Copilot.

## Prompts sugeridos para Copilot

### Prompt 1

```text
Necesito un cliente Python pequeno que lea API_BASE_URL, API_KEY, CALLER_ENV, USER_ID y REGION desde entorno.
Debe llamar GET /v1/customer-offer con headers X-API-Key y X-Caller-Environment.
Quiero una salida reducida y clara.
```

### Prompt 2

```text
Revisa este cliente Python.
Agrega validaciones minimas para variables de entorno faltantes, errores 401 y 404, y campos minimos de la respuesta.
Haz cambios pequenos.
```

### Prompt 3

```text
Quiero comparar development, staging y production usando el mismo cliente.
Ayudame a imprimir recommended_product, discount_pct, price_usd y campos visibles solo en algunos ambientes.
```

## Ejecucion sugerida

```bash
python service.py
```

Luego, en otra terminal:

```bash
cp .env.development.example .env.development
set -a
source .env.development
set +a
python advanced_env_client.py
```
