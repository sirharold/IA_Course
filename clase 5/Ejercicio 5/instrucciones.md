# Ejercicio 5 - Vertex AI

## Objetivo

Preparar una variante de integracion pensada para Vertex AI y comparar que cambia respecto de Gemini.

## Archivo principal

- `ejercicio5_vertex.py`

## Lo que deben hacer

- obtener los parametros necesarios de Vertex AI;
- exportarlos como variables de entorno;
- revisar la estructura del script;
- identificar que depende de plataforma;
- completar configuracion si cuentan con credenciales;
- dejarlo listo para ejecucion o para comparacion tecnica.

## Variables esperadas

- `VERTEX_PROJECT_ID`
- `VERTEX_REGION`
- `VERTEX_ACCESS_TOKEN`
- `VERTEX_MODEL`

## Paso a paso para obtener y grabar los parametros

### 1. Obtener el Project ID

- Abrir la consola de Google Cloud.
- Ir al selector de proyecto.
- Copiar el `Project ID`.

Luego exportarlo:

```bash
export VERTEX_PROJECT_ID='tu-project-id'
```

### 2. Definir la region

Para este ejercicio pueden usar una region comun de Vertex AI como:

```bash
export VERTEX_REGION='us-central1'
```

### 3. Obtener un access token

Si tienen `gcloud` instalado y autenticado, pueden obtener un token temporal con:

```bash
gcloud auth print-access-token
```

Luego exportarlo:

```bash
export VERTEX_ACCESS_TOKEN='pega_aqui_el_token'
```

### 4. Elegir un modelo

Definir el modelo que quieren probar:

```bash
export VERTEX_MODEL='gemini-2.5-flash'
```

### 5. Verificar variables

```bash
echo $VERTEX_PROJECT_ID
echo $VERTEX_REGION
echo $VERTEX_MODEL
```

## Flujo recomendado con Copilot

### Paso 1. Entrar en modo ASK

Antes de tocar el codigo, pedir a Copilot que les ayude a revisar:

- que parametros son propios de Vertex AI;
- cuales son equivalentes a la integracion con Gemini;
- que modelo probar primero;
- que diferencias esperan en autenticacion y endpoint.

### Prompt sugerido para Copilot en modo ASK

```text
Estoy trabajando en un cliente Python para Vertex AI.
Ayudame a entender:
1. que parametros debo configurar;
2. cuales son propios de Vertex AI y cuales son equivalentes a Gemini;
3. que modelo conviene probar primero para extraer JSON desde texto tecnico;
4. que cambios debo esperar en autenticacion y URL.

No escribas aun toda la solucion final.
```

### Paso 2. Volver a modo Agent

Cuando ya tengan claros los parametros, pasar a Agent para ajustar el script.

## Prompt sugerido para Copilot en modo Agent

```text
Compara este cliente orientado a Vertex AI con uno simple de Gemini.
Quiero separar configuracion, llamada y validacion.
No escribas una solucion grande; solo una version clara y mantenible.
```

## Paso adicional del ejercicio

- Ejecutar el script con un modelo en Vertex AI.
- Cambiar `VERTEX_MODEL`.
- Ejecutar de nuevo.
- Comparar:
  - formato de salida;
  - consistencia;
  - utilidad para un pipeline tecnico.
