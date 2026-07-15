# Ejercicio avanzado 1 - Triage de incidente con datos, skill y GitHub MCP

## Objetivo del ejercicio

Construir un paquete de triage tecnico a partir de datos reales del curso, usando un skill para analizar evidencia operativa y GitHub MCP para transformar el resultado en un issue o borrador de issue accionable.

## Lo esperado

Al terminar, deberias haber pasado por una secuencia completa: leer datos, resumir hallazgos con una capacidad reusable, decidir que vale la pena escalar y dejar un issue tecnico claro. El objetivo no es solo obtener una respuesta de Copilot, sino convertir evidencia dispersa en una salida defendible.

## Antes de empezar: preparar skill y MCP

1. Revisa [PREPARACION_SKILLS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_SKILLS.md).
2. Revisa [PREPARACION_MCPS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_MCPS.md).
3. Crea o instala un skill de revision de logs o incidentes.
4. Instala o activa `GitHub MCP Server`.
5. Verifica que el skill quede disponible y que GitHub MCP aparezca en `MCP: List Servers` antes de empezar.

## Starter disponible

Ya tienes una base minima para comenzar:

- [starter_triaje.py](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/ejercicio_avanzado_1_datos_triaje/starter_triaje.py)

Este starter no resuelve el ejercicio. Solo crea la carpeta `salidas` y genera un resumen inicial para ayudarte a leer mejor los datos.

## Archivos base

Usa estos archivos:

- [clase 6/Ejercicio avanzado 2/sample_runtime_logs.ndjson](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%202/sample_runtime_logs.ndjson)
- [clase 6/Ejercicio avanzado 3/sample_incidents.json](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%203/sample_incidents.json)

## Instrucciones

1. Abre una terminal en esta carpeta del ejercicio.
2. Ejecuta el starter:
   ```bash
   python starter_triaje.py
   ```
3. Verifica que se haya creado la carpeta `salidas` y el archivo `salidas/resumen_datos_inicial.md`.
4. Lee ese resumen completo antes de seguir.
5. Abre `sample_runtime_logs.ndjson` y `sample_incidents.json`.
6. Sin usar skill todavia, escribe una nota manual de maximo 10 lineas con:
   - que problema principal parece aparecer;
   - que datos son ambiguos;
   - que informacion te falta.
7. Guarda esa nota como `salidas/lectura_manual.md`.
8. Ahora usa un skill de analisis de logs o incidentes para revisar `sample_runtime_logs.ndjson`.
9. Pidele que deje una salida con esta estructura:
   - hechos observables;
   - errores repetidos;
   - dudas o ambiguedades;
   - validacion minima sugerida.
10. Guarda ese resultado como `salidas/analisis_logs_con_skill.md`.
11. Luego usa Copilot para cruzar ese analisis con `sample_incidents.json`.
12. Pide una salida adicional con:
   - patron comun observado;
   - posible agrupacion de incidentes;
   - recomendacion de siguiente paso;
   - riesgo si se clasifica mal.
13. Guarda ese resultado como `salidas/triage_cruzado.md`.
14. Ahora usa GitHub MCP.
15. Con base en `triage_cruzado.md`, pide a Copilot que prepare un issue tecnico para investigacion.
16. El issue debe incluir:
   - titulo;
   - contexto;
   - impacto;
   - evidencia usada;
   - siguiente validacion propuesta.
17. Si el entorno lo permite, crea el issue en un repo de practica.
18. Si no puedes crearlo, deja el borrador final en `salidas/issue_borrador.md`.
19. Escribe una comparacion final en `salidas/reflexion.md` respondiendo:
   - que parte resolvio mejor el skill;
   - que valor agrego MCP;
   - que parte siguio necesitando criterio humano;
   - que habrias hecho sin skill o sin MCP.

## Como usar el starter correctamente

- Corre `starter_triaje.py` una sola vez al inicio.
- Usa `salidas/resumen_datos_inicial.md` solo para orientarte.
- No entregues solo el archivo generado por el starter.
- Tu trabajo real comienza cuando escribes `lectura_manual.md` y luego construyes los entregables con skill y MCP.

## Entregable

- `salidas/resumen_datos_inicial.md`
- `salidas/lectura_manual.md`
- `salidas/analisis_logs_con_skill.md`
- `salidas/triage_cruzado.md`
- `salidas/issue_borrador.md` o issue creado
- `salidas/reflexion.md`
