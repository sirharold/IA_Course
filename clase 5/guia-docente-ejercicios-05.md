# Guia docente - Ejercicios Clase 5

## Objetivo

Conducir los ejercicios de clase 5 con foco en integracion, request/response, credenciales, validacion y pipeline tecnico.

## Preparacion previa

### Si van a usar internet

- Confirmar conectividad para:
  - HTTPBin;
  - Open-Meteo.

### Si quieren alternativa local

- Levantar el mock:

```bash
export DEMO_API_KEY=demo-local-key
python mock_api/mock_service.py
```

- Verificar salud:

```bash
curl http://127.0.0.1:8010/health
```

## Ejercicio 1. Radiografia de una llamada HTTP

### Como presentarlo

- Explicar que el objetivo no es hacer algo sofisticado.
- El objetivo es ver con claridad:
  - que se envia;
  - como se envia;
  - que devuelve la API.

### Que mostrar

- Una llamada `GET` con `params`.
- Una llamada `POST` con `json`.
- La diferencia visible en la respuesta.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio1_http.py`
- Libreria:
  - `requests`

### Puntos clave para mencionar

- Diferencia entre query params y body JSON.
- Importancia de mirar `status_code`.
- No imprimir todo el JSON si no hace falta.

## Ejercicio 2. Leer una API publica y producir una salida util

### Como presentarlo

- Enfatizar que una API real suele devolver mucho mas de lo que necesitamos.
- La tarea madura es filtrar y producir una salida util.

### Que mostrar

- Una URL simple de Open-Meteo.
- Un JSON real.
- Una salida resumida ya procesada.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio2_meteo.py`
- Libreria:
  - `requests`

### Puntos clave para mencionar

- Elegir pocas variables.
- Validar claves antes de asumir que existen.
- Separar consumo de postproceso.

## Ejercicio 3. Credenciales y variables de entorno con una API local

### Como presentarlo

- Explicar que este ejercicio simula un caso real de autenticacion, pero sin depender de secretos reales.
- Reforzar que configuracion y codigo no deben mezclarse.

### Que mostrar

- Variable de entorno `DEMO_API_KEY`.
- Header `X-API-Key`.
- Caso exitoso.
- Caso 401.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio3_auth.py`
- Servicio:
  - `mock_api/mock_service.py`

### Puntos clave para mencionar

- No hardcodear llaves.
- Leer con `os.getenv(...)`.
- Responder distinto ante exito y error.

## Ejercicio 4. Gemini como integracion de modelo generativo

### Como presentarlo

- Explicar que aqui aparece explicitamente Gemini como modelo del temario.
- El foco no es memorizar SDKs, sino entender el patron de integracion.

### Que mostrar

- Caso pequeno de texto tecnico.
- Payload de entrada para Gemini.
- Formato esperado de salida.
- Validaciones minimas sobre la respuesta.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio4_gemini.py`
- Si no hay credenciales:
  - dejar el script preparado aunque no se ejecute.

### Puntos clave para mencionar

- Gemini aparece como ejemplo concreto del contenido del curso.
- El uso de Copilot aqui debe ayudar a:
  - bosquejar cliente;
  - estructurar payload;
  - proponer validaciones.
- No gastar demasiado tiempo en prompting manual.

## Ejercicio 5. Vertex AI como variante de integracion

### Como presentarlo

- Explicar que Vertex AI entra para mostrar el mismo problema en contexto de plataforma.
- El alumno debe notar que cambia proveedor, autenticacion y operacion, pero no cambia la logica del pipeline.

### Que mostrar

- El mismo caso usado para Gemini.
- Una comparacion entre:
  - configuracion;
  - autenticacion;
  - llamada;
  - validacion.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio5_vertex.py`
- Si no hay credenciales:
  - trabajar en modo diseno o pseudocodigo ejecutable.

### Puntos clave para mencionar

- Vertex AI queda explicitamente cubierto en ejercicios.
- Pedir a Copilot comparacion tecnica, no marketing del producto.
- Mantener foco en diferencias de integracion, no en detalles de consola cloud.

## Ejercicio 6. El prompt como pieza de un pipeline

### Como presentarlo

- Aclarar que ya no estamos enseñando prompting desde cero.
- El foco es mostrar el prompt embebido dentro de un flujo.

### Que mostrar

- Archivo de entrada:
  - `mock_api/sample_incidents.txt`
- Request al endpoint:
  - `POST /v1/extract-incident`
- Response estructurada.
- Validacion de campos esperados.

### Codigo que debe usarse

- Script nuevo del alumno, por ejemplo:
  - `ejercicio6_pipeline.py`
- Servicio:
  - `mock_api/mock_service.py`

### Puntos clave para mencionar

- Entrada.
- Construccion del payload.
- Llamada.
- Postproceso.
- Validacion.
- Uso de Copilot para revisar y endurecer el script.

## Ejercicio 7. Cambiar entre API publica y API local sin romper el flujo

### Como presentarlo

- Explicar que un flujo bien diseñado no depende completamente de un endpoint especifico.
- La meta es empezar a pensar en desacoplamiento.

### Que mostrar

- Script base de un ejercicio anterior.
- Cambio de endpoint o fuente.
- Misma forma de salida final.

### Codigo que debe usarse

- Reusar uno de los scripts anteriores y refactorizarlo.

### Puntos clave para mencionar

- Separar:
  - obtencion de datos;
  - validacion;
  - salida.
- Cambiar pocas lineas al mover la fuente.

## Si falla internet

- Saltar HTTPBin y Open-Meteo.
- Trabajar con:
  - ejercicio 3;
  - ejercicio 4;
  - ejercicio 5;
  - ejercicio 6;
  - ejercicio 7.

## Archivos de apoyo

- [mock_api/mock_service.py](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%205/mock_api/mock_service.py)
- [mock_api/sample_incidents.txt](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%205/mock_api/sample_incidents.txt)
- [mock_api/README.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%205/mock_api/README.md)
