# Ejercicio avanzado - API con entornos y consumo configurado por `.env`

## Objetivo

Consumir una API local que responde distinto segun el ambiente llamador y construir un cliente en Python que use archivos `.env` para cambiar entre `development`, `staging` y `production` sin modificar el codigo fuente.

## Archivos de apoyo

- `advanced_env_api/service.py`
- `advanced_env_api/data/development.json`
- `advanced_env_api/data/staging.json`
- `advanced_env_api/data/production.json`
- `advanced_env_api/README.md`

## Lo que deben construir

- un script cliente en Python;
- tres archivos de entorno:
  - `.env.development`
  - `.env.staging`
  - `.env.production`
- una salida clara en consola que permita comparar la misma consulta entre ambientes.

## Reglas del ejercicio

- No hardcodear:
  - URL base;
  - API key;
  - ambiente llamador;
  - usuario;
  - region.
- El mismo script debe funcionar para los tres ambientes.
- Deben usar GitHub Copilot como apoyo para:
  - bosquejar el cliente;
  - leer variables de entorno;
  - construir la llamada HTTP;
  - validar la respuesta;
  - comparar resultados entre ambientes.

## Caso sugerido

Usar el mismo `user_id` y la misma `region` en tres llamadas separadas para observar:

- cambios de precio;
- cambios de descuento;
- diferencias de campos visibles;
- presencia o ausencia de `debug`, `release_tag` u otros campos.

Un buen usuario para partir es:

- `user_id=usr-1004`
- `region=cl`

## Prompts sugeridos para usar con Copilot

### Prompt 1. Bosquejo del cliente

```text
Necesito un script Python pequeno para consumir una API REST local.
Debe:
1. Leer API_BASE_URL, API_KEY, CALLER_ENV, USER_ID y REGION desde variables de entorno.
2. Hacer una llamada GET a /v1/customer-offer.
3. Enviar X-API-Key y X-Caller-Environment en headers.
4. Validar status_code.
5. Imprimir una salida reducida y clara.
No hardcodees valores. Usa requests y os.getenv.
```

### Prompt 2. Validacion de respuesta

```text
Revisa este cliente Python que consume una API local.
Quiero que agregues validaciones minimas para:
1. detectar variables de entorno faltantes;
2. manejar 401, 404 y 400 con mensajes distintos;
3. verificar que la respuesta tenga al menos customer, recommended_product, discount_pct y price_usd.
Haz cambios pequenos y claros.
```

### Prompt 3. Comparacion entre ambientes

```text
Quiero comparar la respuesta de una misma API entre development, staging y production.
Ayudame a ajustar el script para imprimir:
1. caller_environment;
2. recommended_product;
3. discount_pct;
4. price_usd;
5. campos adicionales visibles solo en algunos ambientes.
La salida debe servir para comparar facilmente sin imprimir todo el JSON.
```

## Archivos `.env` que deben crear

Pueden usar este esquema.

### `.env.development`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=development
USER_ID=usr-1004
REGION=cl
```

### `.env.staging`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=staging
USER_ID=usr-1004
REGION=cl
```

### `.env.production`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=production
USER_ID=usr-1004
REGION=cl
```

## Entregable esperado

- script cliente funcional;
- tres archivos `.env`;
- evidencia de tres ejecuciones con respuestas distintas;
- breve explicacion de que cambia entre ambientes y por que ese diseno es util.

## Validacion minima

- El script funciona sin editar el codigo entre una corrida y otra.
- Cambiar de ambiente solo cambia el `.env` cargado.
- La salida deja ver diferencias reales entre ambientes.
- El cliente distingue correctamente:
  - exito;
  - error de autenticacion;
  - usuario no encontrado;
  - variables faltantes.

<details>
<summary>Paso a paso sugerido</summary>

1. Levantar la API local con:

```bash
python advanced_env_api/service.py
```

2. Confirmar salud:

```bash
curl http://127.0.0.1:8020/health
```

3. Crear el script cliente, por ejemplo:

```text
advanced_env_client.py
```

4. Pedir a Copilot el esqueleto inicial usando el Prompt 1.

5. Crear los tres archivos `.env`.

6. Cargar un ambiente y ejecutar el cliente. En `zsh` o `bash` pueden hacerlo asi:

```bash
set -a
source .env.development
set +a
python advanced_env_client.py
```

7. Repetir con `staging`:

```bash
set -a
source .env.staging
set +a
python advanced_env_client.py
```

8. Repetir con `production`:

```bash
set -a
source .env.production
set +a
python advanced_env_client.py
```

9. Pedir a Copilot mejoras usando los Prompts 2 y 3.

10. Comparar:
  - precio;
  - descuento;
  - campos visibles;
  - diferencias entre `debug`, `release_tag` y respuesta reducida.

</details>
