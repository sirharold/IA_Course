# Advanced Env API - Clase 5

## Objetivo

API local para practicar:

- consumo de APIs desde Python;
- parametros de request;
- variables de entorno;
- diferencias de comportamiento segun ambiente llamador;
- validacion y postproceso con ayuda de Copilot.

## Como levantarla

```bash
python advanced_env_api/service.py
```

La API quedara disponible en:

```text
http://127.0.0.1:8020
```

## Endpoints

### Salud

```bash
curl http://127.0.0.1:8020/health
```

### Customer Offer

```bash
curl "http://127.0.0.1:8020/v1/customer-offer?user_id=usr-1004&region=cl" \
  -H "X-API-Key: course-demo-key" \
  -H "X-Caller-Environment: development"
```

## Reglas de la API

- Requiere header `X-API-Key`.
- Requiere header `X-Caller-Environment` con uno de estos valores:
  - `development`
  - `staging`
  - `production`
- Requiere query param `user_id`.
- `region` es opcional, pero ayuda a validar mejor el match.

## Diferencias entre ambientes

- `development`:
  - respuesta mas verbosa;
  - incluye `debug`;
  - deja visibles campos internos y experimentales.
- `staging`:
  - respuesta intermedia;
  - incluye `release_tag`;
  - oculta algunos detalles internos.
- `production`:
  - respuesta mas sobria;
  - no entrega `debug`;
  - reduce campos no esenciales y no expone notas internas.
