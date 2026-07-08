# Agenda 05

Hora inicio: 15:00

Hora fin: 18:15

Duracion: 195 minutos

Tema: integracion de APIs y modelos generativos en flujos tecnicos con avance del proyecto aplicado

## Objetivo de la sesion

Conectar la automatizacion iniciada en la clase 4 con APIs y modelos generativos para resolver una tarea tecnica concreta, produciendo una salida estructurada, validada y reutilizable como avance del proyecto aplicado del curso.

## Ajuste de plan del curso

- El curso ahora se desarrolla en 9 clases de 3 horas y 15 minutos.
- Desde la clase 4 se distribuye parte del antiguo cierre de la clase 10.
- Esta clase debe dejar un avance funcional del caso elegido: ya no solo un flujo automatizable, sino una integracion externa que aporte valor real al problema definido por cada alumno o pareja.

## Resumen de la agenda

| Horario | Duracion | Bloque |
| --- | --- | --- |
| 15:00-15:15 | 15 min | Repaso de clases 1 a 4 y encuadre de la sesion |
| 15:15-15:40 | 25 min | Consumo de APIs desde Python y estructura de integracion |
| 15:40-16:05 | 25 min | Solicitudes, respuestas, errores y salidas estructuradas |
| 16:05-16:25 | 20 min | Credenciales, variables de entorno y seguridad operativa |
| 16:25-16:35 | 10 min | Break |
| 16:35-16:50 | 15 min | Introduccion practica a Gemini y Vertex AI |
| 16:50-17:00 | 10 min | El prompt como parte del pipeline, no como tema nuevo |
| 17:00-17:50 | 50 min | Laboratorio guiado: integrar API o modelo en el flujo iniciado en la clase 4 |
| 17:50-18:05 | 15 min | Ejercicio adicional para alumnos rapidos |
| 18:05-18:10 | 5 min | Revision de resultados y criterios de validacion |
| 18:10-18:15 | 5 min | Cierre, tarea y continuidad del proyecto aplicado |

## Supuestos para esta clase

- Los participantes ya trabajaron prompting tecnico, comprension de codigo y automatizacion con Python sobre archivos o datos.
- Cada alumno o pareja trae un caso pequeno de automatizacion, o al menos una idea concreta iniciada en la clase 4.
- El grupo entiende que una integracion con API o modelo no reemplaza la validacion tecnica de entrada, salida y errores.
- Se dispone de credenciales de prueba, mocks, ejemplos preconfigurados o una alternativa didactica si algun servicio externo falla.

## Enfoque metodologico

- Demostracion breve seguida de aplicacion directa sobre un caso tecnico realista.
- Uso de IA no solo como chat, sino como componente embebido en un flujo programatico.
- Comparacion entre integrar "porque se puede" e integrar "porque agrega valor real".
- Validacion de respuestas, manejo de errores y trazabilidad de supuestos.
- Continuidad del proyecto aplicado: cada bloque debe empujar el caso de cada alumno hacia una solucion mas completa y defendible.
- Criterio transversal:
  - distinguir claramente entre una API tradicional, un servicio externo y un modelo generativo para no mezclar expectativas tecnicas.

## Agenda detallada

- 15:00-15:15 Repaso de clases 1 a 4 y encuadre de la sesion.
  - Recordar la progresion ya trabajada:
    - riesgos y limites de la IA generativa;
    - uso de Copilot con contexto;
    - comprension de sistemas existentes;
    - automatizacion con Python sobre datos y archivos.
  - Conectar con la clase actual:
    - pasar de automatizacion local a integracion con servicios externos;
    - decidir cuando un modelo generativo aporta valor y cuando solo agrega complejidad.
  - Alinear el objetivo del dia:
    - tomar el flujo iniciado en la clase 4 y enriquecerlo con una API o modelo generativo de forma controlada.

- 15:15-15:40 Consumo de APIs desde Python y estructura de integracion.
  - Revisar piezas minimas de una integracion:
    - endpoint o servicio;
    - payload de entrada;
    - autenticacion;
    - respuesta esperada;
    - validacion posterior.
  - Mostrar como pedir a la IA apoyo para:
    - bosquejar el cliente basico;
    - explicar parametros;
    - documentar precondiciones;
    - proponer manejo inicial de errores.
  - Introducir una distincion util para el resto de la clase:
    - API con contrato fijo;
    - modelo con salida mas flexible;
    - implicancias distintas para validacion y postproceso.
  - Reforzar que el script debe seguir siendo entendible y mantenible sin depender de magia oculta.

- 15:40-16:05 Solicitudes, respuestas, errores y salidas estructuradas.
  - Trabajar con respuestas JSON, texto libre o salidas mixtas.
  - Identificar problemas frecuentes:
    - timeouts;
    - errores de autenticacion;
    - formatos inesperados;
    - respuestas incompletas;
    - salidas utiles pero no directamente procesables.
  - Pedir a la IA alternativas para:
    - parsear salida;
    - imponer una estructura esperada;
    - validar campos obligatorios;
    - dejar evidencia de error util para depurar.
  - Conectar con lo aprendido en clases anteriores:
    - una respuesta de IA no reemplaza evidencia tecnica;
    - una salida util debe poder explicarse y verificarse.

- 16:05-16:25 Credenciales, variables de entorno y seguridad operativa.
  - Explicar practicas minimas:
    - no hardcodear llaves;
    - usar variables de entorno;
    - evitar exponer datos sensibles en prompts o logs;
    - separar configuracion de codigo.
  - Revisar errores comunes de seguridad en laboratorios con IA:
    - copiar secretos en el editor;
    - probar con datos reales sin filtrar;
    - confiar en ejemplos generados sin revisarlos.
  - Conectar esta disciplina con el proyecto aplicado:
    - una demo util debe poder explicarse, reproducirse y auditarse.

- 16:25-16:35 Break.

- 16:35-16:50 Introduccion practica a Gemini y Vertex AI.
  - Explicar por que aparecen en esta clase:
    - son referencias concretas para integrar modelos generativos desde flujos programaticos;
    - permiten aterrizar el paso desde prompt manual a consumo desde script.
  - Gemini:
    - como opcion practica para clasificacion, extraccion, resumen y transformacion de texto;
    - foco en entrada, prompt, salida y validacion, no en profundidad de plataforma.
  - Vertex AI:
    - como capa de uso mas empresarial o de plataforma para trabajar con modelos en entornos de Google Cloud;
    - valor de contexto para alumnos que luego deban operar soluciones en stack corporativo.
  - Aclarar el alcance docente:
    - esta no es una clase de certificacion de producto;
    - Gemini y Vertex AI se presentan como ejemplos aplicados dentro del contenido oficial del curso.

- 16:50-17:00 El prompt como parte del pipeline, no como tema nuevo.
  - Recordar brevemente algo ya trabajado en clases anteriores:
    - objetivo claro;
    - contexto suficiente;
    - restricciones explicitas;
    - formato de salida definido.
  - Reubicar el concepto:
    - el prompt ya no es el centro de la sesion;
    - ahora es una pieza dentro de un flujo con entrada, llamada, validacion y postproceso.
  - Reforzar criterio tecnico:
    - usar modelo cuando exista ambiguedad, texto no estructurado o necesidad de interpretacion;
    - preferir logica determinista cuando la tarea sea simple y verificable sin IA.

- 17:00-17:50 Laboratorio guiado: integrar API o modelo en el flujo iniciado en la clase 4.
  - Trabajo individual o en parejas.
  - Objetivos del laboratorio:
    - retomar el caso elegido en la clase 4;
    - agregar una integracion externa que mejore el flujo;
    - producir una salida estructurada o un resultado verificable;
    - definir validaciones minimas sobre la respuesta;
    - documentar supuestos, limites y posible falla del enfoque.
  - Ejemplos de integracion validos:
    - llamar una API para enriquecer datos;
    - probar una integracion corta con Gemini para clasificar o estructurar texto tecnico;
    - revisar como ese mismo tipo de caso podria vivir en Vertex AI cuando el contexto sea mas de plataforma;
    - enviar texto a un modelo y recibir clasificacion o resumen;
    - transformar informacion libre en JSON o tabla usable;
    - encadenar lectura de archivo con una llamada generativa y una salida limpia.
  - Criterio de exito del laboratorio:
    - la integracion debe dejar valor tecnico observable, no solo una llamada que responde.
  - Distribucion sugerida del tiempo:
    - 35 minutos para el caso base;
    - 15 minutos extra ya incorporados en la nueva duracion para robustecer validaciones, manejo de errores o documentacion del flujo.

- 17:50-18:05 Ejercicio adicional para alumnos rapidos.
  - Esta actividad se activa si una parte del grupo termina antes o si el avance general es mas rapido de lo previsto.
  - Objetivo:
    - agregar al menos 30 minutos adicionales de trabajo desafiante respecto del laboratorio base, ademas de los 15 minutos extra ya incorporados en la nueva duracion de la clase.
  - Opciones de profundizacion:
    - comparar dos formas de integrar y validar una misma salida estructurada;
    - agregar reintento simple o manejo de error mas informativo;
    - incorporar una validacion cruzada entre salida del modelo y una regla determinista;
    - convertir el flujo en una funcion o modulo reutilizable para el proyecto aplicado.
  - Entregable rapido:
    - mejora funcional o de diseno tecnico;
    - evidencia de validacion;
    - breve explicacion de por que esa mejora aporta mas confiabilidad o reutilizacion.

- 18:05-18:10 Revision de resultados y criterios de validacion.
  - Revisar si cada avance deja claro:
    - que problema resuelve la integracion;
    - que entrada consume;
    - que salida produce;
    - que validaciones se aplicaron;
    - donde podria fallar.
  - Comparar soluciones con valor tecnico real versus integraciones solo demostrativas.

- 18:10-18:15 Cierre, tarea y continuidad del proyecto aplicado.
  - Resumir aprendizajes de la sesion.
  - Confirmar que el caso ya tiene:
    - automatizacion base;
    - una integracion externa significativa;
    - validaciones minimas.
  - Anticipar que la clase 6 reforzara operacion, productividad y control del flujo desde terminal con Copilot CLI.

## Tarea para los alumnos

Preparar el siguiente avance del proyecto aplicado:

1. Consolidar el flujo trabajado en clase en una version ejecutable o semiejecutable.
2. Documentar en maximo una pagina:
   - problema que resuelve;
   - entrada;
   - salida;
   - integracion externa usada;
   - validaciones aplicadas;
   - principal riesgo tecnico pendiente.
3. Traer un ejemplo de ejecucion, aunque sea parcial, con evidencia de resultado o error observado.
4. Proponer una mejora concreta para la siguiente iteracion:
   - mas robustez;
   - mejor salida;
   - menor ambiguedad;
   - mejor operacion del flujo.

## Proyeccion del antiguo contenido de clase 10

En esta clase el proyecto aplicado debe avanzar asi:

- Clase 4: se definio el caso y se construyo el primer flujo automatizable.
- Clase 5: se agrega una integracion con API o modelo que justifique mejor el valor del caso.
- Clase 6: se mejorara la operacion y repetibilidad del flujo.
- Clase 7: se analizara mejor la oportunidad y el contexto de uso.
- Clase 8: se priorizara el alcance realista del prototipo.
- Clase 9: se definira la forma final de resolucion: script, workflow o agente tecnico.

## Productos esperados al final de la clase

- Script o flujo base con integracion a API o modelo generativo.
- Salida estructurada o resultado verificable.
- Validaciones minimas sobre respuesta, error o consistencia.
- Avance documentado del proyecto aplicado.
- Tarea definida para continuar la siguiente iteracion fuera de clase.

## Recomendaciones para el docente

- Llevar una alternativa de bajo riesgo si falla la conectividad o una credencial externa.
- Preparar uno o dos casos donde el uso de modelo si tenga sentido y otro donde no aporte tanto.
- Insistir en que seguridad, validacion y mantenibilidad pesan tanto como "hacer la llamada".
- Favorecer avances pequenos, defendibles y reutilizables en vez de demos fragiles.
- Si el grupo avanza rapido, activar la profundizacion de al menos 30 minutos adicionales con una mejora de robustez o reutilizacion.
