# Ejercicio avanzado 2 - Backlog tecnico con datos locales, skill y MCP documental

## Objetivo del ejercicio

Tomar un conjunto de tickets o hallazgos locales, construir un backlog tecnico resumido con ayuda de un skill y luego usar un MCP documental para verificar o enriquecer parte del criterio tecnico con una fuente oficial.

## Lo esperado

Al terminar, deberias tener un backlog preliminar mejor estructurado, con una mezcla de datos locales y una verificacion externa justificada. El objetivo es mostrar que skill y MCP no compiten: uno ayuda a estructurar una tarea repetitiva y el otro ayuda a buscar contexto confiable cuando hace falta.

## Archivos base

Usa estos archivos:

- [clase 6/Ejercicio avanzado 1/sample_tickets.json](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%201/sample_tickets.json)
- [clase 5/Ejercicio avanzado 3/evaluacion_modelos.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%205/Ejercicio%20avanzado%203/evaluacion_modelos.md)

## Instrucciones

1. Crea una carpeta de trabajo llamada `salidas`.
2. Revisa `sample_tickets.json`.
3. Sin usar skill todavia, anota en `salidas/observacion_inicial.md`:
   - que tipos de tickets ves;
   - cuales parecen mas urgentes;
   - que informacion te gustaria agrupar mejor.
4. Usa un skill de reporte operativo o backlog tecnico para procesar `sample_tickets.json`.
5. Pide que la salida incluya:
   - conteo por severidad;
   - tickets abiertos sin owner;
   - agrupacion de hallazgos repetidos;
   - lista corta de focos de atencion.
6. Guarda el resultado en `salidas/backlog_con_skill.md`.
7. Ahora revisa `evaluacion_modelos.md` y el backlog generado.
8. Elige una duda tecnica concreta que necesite verificacion externa. Ejemplos validos:
   - si una recomendacion depende de CLI;
   - si una accion depende de custom instructions;
   - si una integracion requiere documentacion oficial actual.
9. Usa un MCP documental, idealmente Microsoft Learn MCP, para buscar documentacion oficial relacionada con esa duda.
10. Si necesitas instalar Microsoft Learn MCP en Visual Studio Code, usa este orden:
   - primero busca `@mcp Microsoft`;
   - luego ubica `Microsoft Learn` en la lista;
   - si no aparece, usa la configuracion manual del archivo [PREPARACION_MCPS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_MCPS.md).
11. Guarda la respuesta en `salidas/consulta_documental_mcp.md`.
12. Actualiza el backlog inicial con una seccion llamada `validacion documental`.
13. Guarda la version final en `salidas/backlog_validado.md`.
14. Escribe una reflexion final en `salidas/reflexion.md` respondiendo:
   - que parte hizo mejor el skill;
   - en que punto hizo falta MCP;
   - que riesgo habria existido si no validabas con fuente externa;
   - donde aun no confiarias ciegamente.

## Entregable

- `salidas/observacion_inicial.md`
- `salidas/backlog_con_skill.md`
- `salidas/consulta_documental_mcp.md`
- `salidas/backlog_validado.md`
- `salidas/reflexion.md`
