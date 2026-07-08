# Clase 5: Integracion con APIs y modelos generativos

## Objetivo

Conectar la automatizacion construida en la clase 4 con servicios externos y modelos generativos para resolver una tarea tecnica concreta, produciendo una salida estructurada, validable y util para el proyecto aplicado del curso.

## Cambio de nivel respecto de las clases anteriores

- Clase 1:
  - marco de uso responsable, riesgos y limites.
- Clase 2:
  - prompting tecnico, contexto persistente e instrucciones reutilizables.
- Clase 3:
  - lectura rigurosa de codigo, datos, logs y evidencia tecnica.
- Clase 4:
  - automatizacion local con Python sobre archivos, documentos y datos.
- Clase 5:
  - integracion externa con APIs o modelos cuando esa integracion agrega valor real y no solo complejidad.

## Resultados de aprendizaje

- Consumir una API desde Python con una estructura entendible y mantenible.
- Diferenciar entre una llamada tecnica comun y una llamada a un modelo generativo.
- Manejar solicitudes, respuestas, errores y salidas incompletas de forma controlada.
- Usar variables de entorno para separar credenciales, configuracion y codigo.
- Disenar prompts programaticos con mejor estructura y menor ambiguedad.
- Procesar respuestas generadas para convertirlas en JSON, tabla o resumen tecnico reutilizable.
- Justificar cuando conviene usar IA generativa y cuando basta una solucion determinista.

## Contenidos que debe cubrir la clase

### 1. Puente conceptual: de automatizacion local a integracion externa

- Que cambia cuando el flujo ya no vive solo en archivos locales.
- Tipos de integracion utiles:
  - APIs tradicionales;
  - modelos generativos;
  - servicios de enriquecimiento o clasificacion.
- Criterio central:
  - integrar porque resuelve mejor el problema, no porque se vea mas sofisticado.

### 2. Consumo de APIs desde Python

- Estructura minima de una integracion:
  - endpoint;
  - autenticacion;
  - payload;
  - respuesta;
  - validacion posterior.
- Librerias y patrones simples para partir.
- Separacion entre codigo de llamada, configuracion y postproceso.

### 3. Solicitudes, respuestas y manejo de errores

- Diferencia entre respuesta exitosa, respuesta util pero incompleta y error operativo.
- Casos frecuentes:
  - timeout;
  - autenticacion fallida;
  - formato inesperado;
  - campos faltantes;
  - salida dificil de parsear.
- Estrategias minimas:
  - validar antes de confiar;
  - registrar errores utiles;
  - dejar evidencia para depurar.

### 4. Credenciales, variables de entorno y seguridad operativa

- No hardcodear secretos.
- Uso basico de variables de entorno.
- Separar codigo, configuracion y datos sensibles.
- Cuidado con:
  - secretos en prompts;
  - secretos en logs;
  - ejemplos con datos reales;
  - respuestas generadas que exponen informacion innecesaria.

### 5. Modelos generativos en flujos tecnicos

- Casos donde si aportan:
  - clasificacion;
  - extraccion desde texto libre;
  - resumen tecnico;
  - transformacion a estructura usable.
- Casos donde no aportan tanto:
  - reglas fijas;
  - formateos triviales;
  - validaciones totalmente deterministas.
- Introduccion practica a Gemini y Vertex AI como referencias del ecosistema, sin transformar la sesion en una clase de plataforma.

### 6. Prompts programaticos

- Diferencia entre prompt manual y prompt embebido en script.
- Estructura recomendada:
  - objetivo;
  - contexto;
  - restricciones;
  - formato de salida;
  - criterio de validacion.
- Como reducir ambiguedad y pedir salida mas procesable.

### 7. Postproceso y validacion de respuestas

- Convertir texto generado en salida estructurada util.
- Validar campos obligatorios y consistencia minima.
- Combinar IA generativa con reglas deterministas.
- Dejar trazabilidad:
  - que entro;
  - que salio;
  - que se acepto;
  - que se rechazo o quedo incierto.

## Actividad practica sugerida

Retomar el flujo iniciado en la clase 4 y agregar una integracion externa que mejore el caso de cada alumno o pareja. La actividad debe dejar una salida estructurada o una mejora verificable, no solo una llamada exitosa.

## Ejemplos de casos validos para laboratorio

- Enviar texto tecnico a un modelo para clasificar incidentes o priorizar hallazgos.
- Transformar descripcion libre en JSON usable por otro script.
- Enriquecer una salida previa con datos obtenidos desde una API.
- Leer un archivo local, llamar a un servicio externo y devolver un reporte tecnico resumido.

## Entregables

- Script o modulo de integracion con API o modelo.
- Prompt programatico o plantilla equivalente.
- Salida estructurada validada o resultado verificable.
- Lista corta de validaciones y limites del enfoque.

## Preparacion

- Variables de entorno disponibles.
- Credenciales de prueba, mocks o alternativa local si falla el servicio externo.
- Python y conectividad operativa.
- Caso base iniciado en la clase 4 o una variante pequeña equivalente.

## Criterio docente

La meta de esta clase no es mostrar muchas plataformas. La meta es que cada participante entienda como integrar un servicio externo con criterio tecnico, controlando seguridad, validacion, mantenibilidad y utilidad real para su caso aplicado.
