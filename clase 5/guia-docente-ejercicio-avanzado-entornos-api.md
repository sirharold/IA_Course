# Guia docente - Ejercicio avanzado de entornos y `.env`

## Objetivo

Usar una API local realista para que los alumnos practiquen entornos, configuracion por variables de entorno y consumo de una misma API con respuestas distintas segun el ambiente llamador.

## Que aporta este ejercicio

- introduce entornos como concepto concreto;
- refuerza consumo de APIs desde Python;
- obliga a separar configuracion de codigo;
- muestra por que un mismo servicio puede responder distinto en `development`, `staging` y `production`;
- da un caso realista para usar Copilot con foco en desarrollo, no solo en prompting.

## Preparacion previa

Levantar la API:

```bash
python advanced_env_api/service.py
```

Verificar salud:

```bash
curl http://127.0.0.1:8020/health
```

## Que mostrar al presentar el ejercicio

- la carpeta `advanced_env_api/`;
- que hay tres fuentes JSON distintas;
- que la API es la misma, pero responde segun `X-Caller-Environment`;
- que el cliente no deberia cambiar al pasar de development a production;
- que el cambio debe vivir en `.env`.

## Puntos clave para mencionar

- esto no es infraestructura compleja;
- es configuracion aplicada al desarrollo real;
- el aprendizaje importante es separar:
  - codigo;
  - configuracion;
  - datos;
  - comportamiento por ambiente.

## Codigo que deben usar

- API entregada:
  - `advanced_env_api/service.py`
- datos:
  - `advanced_env_api/data/development.json`
  - `advanced_env_api/data/staging.json`
  - `advanced_env_api/data/production.json`
- cliente del alumno:
  - por ejemplo `advanced_env_client.py`

## Que deberian observar los alumnos

Con el mismo `user_id` y la misma `region`:

- en `development` aparecen mas campos y `debug`;
- en `staging` aparece `release_tag` y una respuesta intermedia;
- en `production` la respuesta es mas sobria y con menos exposicion de detalles internos.

## Donde debe ayudar Copilot

- bosquejo del cliente;
- lectura de variables de entorno;
- construccion de la llamada;
- validaciones minimas;
- comparacion de respuestas;
- mejora pequena del output para hacerlo mas util.

## Preguntas utiles para el cierre

- que quedo configurado en `.env` y que quedo en el codigo;
- que diferencia observaron entre development, staging y production;
- por que es util que el mismo cliente funcione en los tres ambientes;
- que riesgo habria si hubieran hardcodeado URL, API key o ambiente.
