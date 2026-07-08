# Ejercicio avanzado 2 - App Streamlit sobre la API por ambientes

## Objetivo

Crear una app en Streamlit que consuma la misma API del `Ejercicio avanzado 1` y permita visualizar los datos en una grilla, cambiando el ambiente desde la interfaz.

## Que debe tener la app

- seleccion de ambiente:
  - `development`
  - `staging`
  - `production`
- seleccion del objeto a mostrar:
  - `offers_grid`
  - `single_customer`
  - `raw_response`
- una grilla con los datos;
- una zona de detalle para ver la respuesta de un cliente o la respuesta cruda;
- lectura de configuracion desde archivos `.env`.

## API que deben usar

Levanten primero la API del `Ejercicio avanzado 1`:

```bash
python ../Ejercicio\ avanzado\ 1/service.py
```

La app consumira:

- `GET /v1/customer-offers`
- `GET /v1/customer-offer`

## Archivo principal

- `streamlit_app.py`

## Dependencias

- `streamlit`
- `requests`
- `python-dotenv`
- `pandas`

## Flujo recomendado con Copilot

Si su entorno de GitHub Copilot tiene `Plan mode` y `Agent mode`, usen este flujo.
Si no lo tiene, repliquen la misma idea manualmente:

- primero plan;
- luego tareas;
- luego ejecucion.

## Paso 1. Entrar en modo Plan

Antes de escribir codigo, entren en modo Plan. Si su interfaz permite seleccionar modelo, elijan uno orientado a codigo y razonamiento.

### Prompt para modo Plan

```text
Quiero crear una app Streamlit pequena que consuma una API local.
La app debe:
1. leer configuracion desde archivos .env por ambiente;
2. permitir seleccionar development, staging o production;
3. permitir elegir que objeto mostrar: offers_grid, single_customer o raw_response;
4. mostrar una grilla con datos desde /v1/customer-offers;
5. mostrar detalle individual desde /v1/customer-offer;
6. manejar errores de configuracion y de request.

Genera primero un plan corto y concreto.
No escribas aun toda la solucion final.
Divide el trabajo en tareas pequenas y ejecutables.
```

## Paso 2. Revisar y ajustar el plan

Antes de cambiar de modo, revisen si el plan incluye al menos:

- lectura de `.env`;
- cliente HTTP separado;
- interfaz Streamlit;
- grilla;
- detalle;
- manejo de errores.

## Paso 3. Entrar en modo Agent

Cuando el plan ya este claro, entren en modo Agent para ejecutar las tareas.

### Prompt para modo Agent

```text
Ejecuta el plan para construir la app Streamlit.
Trabaja por tareas pequenas:
1. carga de .env por ambiente;
2. cliente para /v1/customer-offers y /v1/customer-offer;
3. interfaz con selectbox para ambiente;
4. selectbox para objeto a mostrar;
5. grilla con pandas o st.dataframe;
6. detalle de un cliente;
7. manejo de errores claro.

Mantiene el codigo pequeno, legible y facil de explicar.
```

## Prompts adicionales para Copilot

### Prompt 1. Carga de `.env`

```text
Ayudame a cargar archivos .env distintos segun el ambiente seleccionado en Streamlit.
Quiero una funcion pequena que lea .env.development, .env.staging o .env.production y devuelva la configuracion necesaria.
```

### Prompt 2. Cliente HTTP

```text
Necesito dos funciones Python:
1. una para llamar /v1/customer-offers;
2. otra para llamar /v1/customer-offer.
Ambas deben usar requests, headers X-API-Key y X-Caller-Environment, timeout y manejo simple de errores.
```

### Prompt 3. UI en Streamlit

```text
Quiero una app Streamlit con:
- titulo;
- selectbox de ambiente;
- selectbox de objeto;
- selectbox de user_id;
- grilla para rows;
- expander o bloque para raw JSON.
Manten la interfaz minima y clara.
```

## Archivos `.env` de ejemplo

### `.env.development.example`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=development
DEFAULT_USER_ID=usr-1004
DEFAULT_REGION=cl
```

### `.env.staging.example`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=staging
DEFAULT_USER_ID=usr-1004
DEFAULT_REGION=cl
```

### `.env.production.example`

```text
API_BASE_URL=http://127.0.0.1:8020
API_KEY=course-demo-key
CALLER_ENV=production
DEFAULT_USER_ID=usr-1004
DEFAULT_REGION=cl
```

## Ejecucion sugerida

1. Crear los archivos reales a partir de los `.example`.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Levantar la API del ejercicio avanzado 1.
4. Levantar la app:

```bash
streamlit run streamlit_app.py
```

## Entregable esperado

- app Streamlit funcional;
- seleccion de ambiente;
- seleccion de objeto;
- grilla de datos;
- detalle individual;
- manejo minimo de errores;
- uso visible de Copilot en planificacion y ejecucion.
