# Presentacion 05 - APIs y modelos generativos en flujos tecnicos

Nota: la agenda vive como lamina separada. Esta presentacion queda pensada para 18 laminas desde `cambio de nivel`, para un total de 19 incluyendo agenda.

## Slide 2. Cambio de nivel respecto de la clase 4

- Clase 4:
  - automatizar lectura, transformacion y salida sobre archivos, datos y documentos.
- Clase 5:
  - conectar ese flujo con APIs o modelos generativos;
  - decidir cuando la integracion agrega valor real;
  - dejar una salida estructurada y validable.

## Slide 3. Criterio central de esta sesion

- No se trata de `hacer una llamada`.
- Se trata de responder:
  - que problema mejora la integracion;
  - que entrada consume;
  - que salida produce;
  - como validamos que sirvio;
  - donde podria fallar.

## Slide 4. Cuando vale la pena integrar una API o un modelo

- Si vale la pena:
  - enriquecer datos con informacion externa;
  - clasificar o resumir texto tecnico;
  - extraer estructura desde texto libre;
  - conectar pasos de un flujo con salida util.
- No vale la pena:
  - reemplazar una regla simple;
  - hacer una demo vistosa sin impacto tecnico;
  - introducir dependencia externa para una tarea totalmente mecanica.

## Slide 5. Mapa mental de una integracion sana

- Entrada:
  - texto, archivo, registro, payload o dato previo.
- Llamada:
  - endpoint, autenticacion, parametros, prompt o payload.
- Respuesta:
  - JSON, texto, tabla o mezcla.
- Validacion:
  - formato, campos, consistencia, error.
- Salida:
  - artefacto reutilizable para el flujo tecnico.

## Slide 6. APIs tradicionales versus modelos generativos

- API tradicional:
  - contrato mas estable;
  - campos esperados;
  - validacion mas directa.
- Modelo generativo:
  - mas flexible;
  - mejor para ambiguedad o texto libre;
  - exige mas control sobre prompt, salida y validacion.
- Decision practica:
  - elegir segun el tipo de problema, no por novedad.

## Slide 7. Estructura minima de una llamada desde Python

- Configuracion:
  - variables de entorno;
  - endpoint;
  - parametros.
- Ejecucion:
  - request;
  - timeout;
  - control de error.
- Postproceso:
  - parseo;
  - validacion;
  - salida limpia.

## Slide 8. Credenciales y seguridad operativa

- No hardcodear secretos.
- No dejar llaves en notebooks, prompts o capturas.
- No mezclar datos sensibles con experimentacion descuidada.
- Separar:
  - codigo;
  - configuracion;
  - evidencia de salida.
- Mensaje clave:
  - una integracion fragil o insegura no cuenta como buen avance tecnico.

## Slide 9. Recordatorio breve: prompts pragmaticos

- Como ya vimos en clases anteriores:
  - objetivo claro;
  - contexto suficiente;
  - restricciones explicitas;
  - formato de salida definido.
- En esta clase no volvemos a ensenar prompting desde cero.
- El cambio real es otro:
  - el prompt pasa a ser una pieza del pipeline tecnico.

## Slide 10. Introduccion practica a Gemini

- Rol en esta clase:
  - ejemplo concreto de modelo generativo consumido desde flujo programatico.
- Casos utiles:
  - clasificacion;
  - extraccion;
  - resumen tecnico;
  - transformacion de texto a JSON.
- Que interesa mostrar:
  - entrada;
  - prompt;
  - salida;
  - validacion posterior.
- Mensaje clave:
  - no importa memorizar el producto;
  - importa entender el patron de integracion.

## Slide 11. Introduccion practica a Vertex AI

- Rol en esta clase:
  - ubicar el mismo tipo de integracion en un contexto de plataforma.
- Valor didactico:
  - ayuda a explicar que no todo uso de modelos queda en chat o script aislado.
- Puntos a tocar:
  - uso en entornos Google Cloud;
  - relacion entre modelo, API, credenciales y operacion;
  - cuando conviene mencionarlo aunque el laboratorio sea pequeno.
- Mensaje clave:
  - Gemini y Vertex AI no compiten en la presentacion;
  - muestran dos niveles de aterrizaje del mismo tema.

## Slide 12. El pipeline completo de integracion

- Entrada:
  - archivo, texto, log, payload o resultado previo.
- Preparacion:
  - limpieza minima;
  - seleccion de contexto;
  - construccion del prompt o request.
- Llamada:
  - API o modelo.
- Postproceso:
  - parseo;
  - validacion;
  - transformacion de salida.
- Resultado:
  - JSON, reporte, clasificacion o artefacto reutilizable.

## Slide 13. Que puede salir mal

- Timeout o credencial incorrecta.
- Respuesta vacia o truncada.
- JSON invalido.
- Clasificacion ambigua.
- Texto aparentemente util pero dificil de automatizar.
- Error comun:
  - confiar en la primera salida porque `suena razonable`.

## Slide 14. Validacion: donde se gana o se pierde calidad

- Verificar:
  - campos obligatorios;
  - tipos esperados;
  - consistencia con reglas simples;
  - evidencia de error si algo falla.
- Combinar:
  - IA generativa para interpretar;
  - reglas deterministas para controlar.

## Slide 15. Demo 1: texto libre a JSON usable

- Caso:
  - recibir descripcion tecnica desordenada.
- Meta:
  - convertirla en estructura util para otro paso.
- Valor real:
  - menos trabajo manual;
  - mas reutilizacion;
  - mejor trazabilidad.

## Slide 16. Demo 2: integracion sobre el flujo de la clase 4

- Caso:
  - tomar un output previo de automatizacion.
- Agregar:
  - enriquecimiento por API o clasificacion por modelo.
- Meta:
  - mostrar continuidad real del proyecto aplicado.

## Slide 17. Criterio de calidad para lo que generemos hoy

- Tiene una entrada clara.
- Tiene una salida util y entendible.
- Explica donde usa IA y donde no.
- Valida lo suficiente para no confiar a ciegas.
- Se puede defender tecnicamente frente a otro desarrollador.

## Slide 18. Actividad de hoy

- Retomar el caso trabajado en clase 4.
- Elegir una integracion externa con sentido.
- Implementar llamada, manejo basico de error y validacion.
- Dejar evidencia del resultado o del principal bloqueo tecnico.

## Slide 19. Cierre y siguiente paso

- Hoy el proyecto aplicado debe quedar con:
  - automatizacion base;
  - una integracion externa significativa;
  - salida estructurada o validacion clara.
- La clase 6 no cambia el caso:
  - mejora su operacion, repetibilidad y control desde terminal.
