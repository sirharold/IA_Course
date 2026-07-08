# Ejercicios - Clase 5

## Objetivo general

Practicar integracion con APIs y modelos generativos dentro de flujos tecnicos pequenos, validables y nuevos.

## Antes de comenzar

En cada ejercicio, antes de escribir codigo, dejen claro:

- que entrada consume su script;
- que API o endpoint van a usar;
- que salida quieren producir;
- que validacion minima van a aplicar;
- que podria fallar.

En todos los ejercicios deben usar GitHub Copilot al menos para una de estas tareas:

- bosquejar el script inicial;
- explicar la estructura esperada de request y response;
- proponer validaciones minimas;
- sugerir manejo de errores;
- ayudar a refactorizar la salida para que quede mas clara.

## Ejercicio 1. Radiografia de una llamada HTTP

### Objetivo

Entender bien que se envia y que se recibe al consumir una API desde Python.

### API sugerida

- HTTPBin:
  - `GET /get`
  - `POST /post`

### Instrucciones

- Crear un script pequeno en Python.
- Hacer una llamada `GET` con al menos dos query params.
- Hacer una llamada `POST` enviando JSON.
- Imprimir solo estos elementos de la respuesta:
  - URL final;
  - query params recibidos;
  - JSON enviado;
  - status code.

### Uso de Copilot

- Pedir a Copilot un esqueleto minimo del script con una llamada `GET` y una `POST`.
- Pedirle que explique la diferencia entre usar `params=` y `json=`.
- Pedirle una forma breve de imprimir solo la parte importante de la respuesta.

### Entregable esperado

- Un script que haga ambas llamadas.
- Salida clara en consola.

### Validacion minima

- Confirmar que la API devuelve los mismos parametros enviados.
- Confirmar diferencia entre `params=` y `json=`.

<details>
<summary>Paso a paso sugerido</summary>

1. Crear un archivo como `ejercicio1_http.py`.
2. Importar `requests`.
3. Preparar una llamada `GET` a `https://httpbin.org/get` con `params`.
4. Preparar una llamada `POST` a `https://httpbin.org/post` con `json`.
5. Imprimir solo los campos pedidos.
6. Comparar que parte de la respuesta corresponde al `GET` y cual al `POST`.

</details>

## Ejercicio 2. Leer una API publica y producir una salida util

### Objetivo

Consumir una API publica real y transformar la respuesta en una salida tecnica breve y usable.

### API sugerida

- Open-Meteo.

### Instrucciones

- Consultar el pronostico de una ciudad o coordenada definida por el docente.
- Pedir pocas variables para no ensuciar la respuesta.
- Generar una salida resumida con este formato:
  - hora;
  - temperatura;
  - probabilidad de precipitacion o variable equivalente si se consulta;
  - una conclusion breve escrita por ustedes.

### Restriccion

- No imprimir todo el JSON crudo.
- Deben extraer solo 3 a 5 datos relevantes.

### Uso de Copilot

- Pedir a Copilot que proponga la URL o los parametros de consulta.
- Pedirle que identifique las claves del JSON que realmente importan.
- Pedirle una mejora para convertir la respuesta cruda en una salida mas util.

### Entregable esperado

- Script Python de consulta.
- Resumen corto en consola o JSON reducido.

### Validacion minima

- Verificar `status_code`.
- Verificar que las claves esperadas existen antes de leerlas.
- Mostrar que pasa si la clave no existe y como lo manejaron.

<details>
<summary>Paso a paso sugerido</summary>

1. Crear un archivo como `ejercicio2_meteo.py`.
2. Revisar la documentacion o un ejemplo de URL de Open-Meteo.
3. Elegir una coordenada y pocas variables.
4. Hacer la llamada con `requests.get(...)`.
5. Revisar las claves principales del JSON.
6. Extraer solo los campos necesarios.
7. Imprimir una salida reducida y entendible.

</details>

## Ejercicio 3. Credenciales y variables de entorno con una API local

### Objetivo

Practicar autenticacion simple, variables de entorno y manejo de errores sin depender de credenciales reales de nube.

### API sugerida

- `mock_api/mock_service.py`

### Instrucciones

- Definir una variable de entorno `DEMO_API_KEY`.
- Hacer una llamada a `POST /v1/classify-ticket` con header `X-API-Key`.
- Enviar un JSON con:
  - `ticket_id`
  - `text`
- Mostrar dos escenarios:
  - llamada exitosa;
  - llamada con credencial incorrecta.

### Uso de Copilot

- Pedir a Copilot un ejemplo de lectura de `os.getenv(...)`.
- Pedirle que sugiera un manejo simple de error para 401.
- Pedirle que revise si el script esta dejando acoplada la configuracion con el codigo.

### Entregable esperado

- Script con lectura de variable de entorno.
- Manejo simple de error 401.

### Validacion minima

- No hardcodear la API key dentro del script.
- Imprimir mensaje distinto para exito y error.

<details>
<summary>Paso a paso sugerido</summary>

1. Levantar el servicio local o usar el ya levantado por el docente.
2. Exportar `DEMO_API_KEY` en la terminal.
3. Crear un archivo como `ejercicio3_auth.py`.
4. Leer la API key con `os.getenv(...)`.
5. Hacer una llamada correcta al endpoint.
6. Repetir la llamada con una credencial incorrecta.
7. Mostrar en consola la diferencia entre ambos resultados.

</details>

## Ejercicio 4. Gemini como integracion de modelo generativo

### Objetivo

Diseñar una llamada programatica a Gemini para transformar texto tecnico en salida estructurada.

### API o referencia sugerida

- Gemini API o la documentacion que indique el docente.
- Si no hay credenciales disponibles, se puede trabajar el ejercicio en modo diseno sin ejecutar la llamada real.

### Instrucciones

- Definir un caso simple:
  - clasificar un incidente;
  - resumir un texto tecnico;
  - extraer campos desde texto libre.
- Preparar el payload de una llamada a Gemini con:
  - entrada;
  - instruccion;
  - formato esperado de salida.
- Definir que validaciones aplicarian sobre la respuesta.
- Si tienen credenciales, ejecutar la llamada.
- Si no tienen credenciales, dejar el script preparado y documentar que faltaria para ejecutarlo.

### Uso de Copilot

- Pedir a Copilot que bosqueje el cliente Python para Gemini.
- Pedirle que ayude a estructurar el payload de entrada.
- Pedirle que proponga validaciones para la respuesta generada.

### Entregable esperado

- Script o borrador ejecutable de integracion con Gemini.
- Payload de entrada claro.
- Lista minima de validaciones.

### Validacion minima

- Explicar que parte del flujo depende del modelo.
- Explicar que parte validarian con reglas deterministas.

<details>
<summary>Paso a paso sugerido</summary>

1. Crear un archivo como `ejercicio4_gemini.py`.
2. Elegir un texto tecnico corto de entrada.
3. Pedir a Copilot un esqueleto de llamada a Gemini.
4. Definir una instruccion corta y clara.
5. Definir el formato esperado de salida.
6. Agregar validaciones para los campos esperados.
7. Ejecutar si hay credenciales o dejarlo preparado si no las hay.

</details>

## Ejercicio 5. Vertex AI como variante de integracion

### Objetivo

Entender como cambiaria la integracion si el mismo caso se llevara a Vertex AI en un contexto de plataforma.

### API o referencia sugerida

- Vertex AI o la documentacion que indique el docente.
- Si no hay credenciales disponibles, se puede trabajar el ejercicio en modo diseno sin ejecutar la llamada real.

### Instrucciones

- Tomar el mismo caso del ejercicio anterior o uno equivalente.
- Escribir como cambiaria la integracion en Vertex AI respecto de Gemini:
  - autenticacion;
  - configuracion;
  - llamada;
  - validacion.
- Preparar un script base o pseudocodigo ejecutable.
- Identificar que elementos seguirian iguales y cuales no.

### Uso de Copilot

- Pedir a Copilot que compare una integracion simple de Gemini con una de Vertex AI.
- Pedirle que enumere dependencias o configuraciones que habria que revisar.
- Pedirle que proponga una estructura de script que deje separadas configuracion, llamada y validacion.

### Entregable esperado

- Script base, pseudocodigo o comparacion tecnica entre ambas integraciones.
- Lista de diferencias practicas.

### Validacion minima

- Distinguir que parte es propia del proveedor o plataforma.
- Distinguir que parte pertenece al pipeline y seguiria igual.

<details>
<summary>Paso a paso sugerido</summary>

1. Crear un archivo como `ejercicio5_vertex.py`.
2. Reusar el caso elegido para Gemini.
3. Pedir a Copilot una comparacion tecnica entre ambas integraciones.
4. Separar configuracion, llamada y validacion.
5. Dejar claro que partes cambian por plataforma y que partes no cambian.

</details>

## Ejercicio 6. El prompt como pieza de un pipeline

### Objetivo

Conectar entrada, request, response y validacion en un flujo pequeno donde el prompt es solo una pieza del proceso.

### API sugerida

- `mock_api/mock_service.py`

### Instrucciones

- Leer un texto tecnico corto desde `mock_api/sample_incidents.txt`.
- Enviar uno de los incidentes a `POST /v1/extract-incident`.
- El endpoint devuelve una salida estructurada.
- Guardar o imprimir solo estos campos:
  - `system`
  - `severity`
  - `symptom`
  - `next_step`

### Uso de Copilot

- Pedir a Copilot una primera version del script.
- Pedirle que revise si la salida esta demasiado acoplada al JSON crudo.
- Pedirle una mejora pequena para validar campos faltantes.

### Entregable esperado

- Script que toma texto, llama el endpoint y muestra salida estructurada.

### Validacion minima

- Verificar que todos los campos esperados existen.
- Si falta uno, mostrar advertencia.

<details>
<summary>Paso a paso sugerido</summary>

1. Crear un archivo como `ejercicio6_pipeline.py`.
2. Leer una linea de `mock_api/sample_incidents.txt`.
3. Construir un payload con:
   - `instruction`
   - `text`
4. Enviar el payload al endpoint local.
5. Leer `result` de la respuesta.
6. Validar que existan los campos esperados.
7. Imprimir solo la salida reducida.

</details>

## Ejercicio 7. Cambiar entre API publica y API local sin romper el flujo

### Objetivo

Mostrar que un flujo sano desacopla origen de datos, llamada externa, validacion y salida final.

### Instrucciones

- Tomar el script de un ejercicio anterior.
- Cambiar la fuente o endpoint sin reescribir todo:
  - de Open-Meteo a mock local;
  - o de mock local a otra ruta del mismo servicio.
- Mantener el mismo formato de salida final.

### Uso de Copilot

- Pedir a Copilot una propuesta de refactor pequena.
- Pedirle que identifique donde esta el acoplamiento al endpoint actual.
- Pedirle una forma de separar obtencion de datos, validacion y salida.

### Entregable esperado

- Script con funciones separadas al menos en:
  - obtener datos;
  - validar respuesta;
  - producir salida final.

### Validacion minima

- Cambiar endpoint con el menor numero posible de lineas.

<details>
<summary>Paso a paso sugerido</summary>

1. Tomar un script anterior como base.
2. Separar la llamada externa en una funcion.
3. Separar la validacion en otra funcion.
4. Separar la impresion o salida final en otra funcion.
5. Cambiar la fuente de datos o endpoint.
6. Verificar que la salida final siga teniendo la misma forma.

</details>
