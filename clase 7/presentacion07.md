# Presentacion 07 - Skills, customizacion reusable y MCP en Copilot

## Slide 1. Titulo

- Clase 7 de 9
- Skills, customizacion reusable y MCP en Copilot
- Mensaje clave:
  - ya no estamos aprendiendo solo a operar mejor el flujo;
  - estamos aprendiendo a customizarlo y ampliarlo con criterio.

## Slide 2. Agenda

- Del prompt aislado a la capacidad reusable.
- Instructions, prompt files y skills.
- MCP:
  - que es;
  - que aporta;
  - que no aporta.
- Comparar skill, MCP y prompt libre.
- Laboratorio:
  - probar skills;
  - observar donde MCP cambia el alcance.

## Slide 3. Contenidos del curso

- Clase 1:
  - estrategia de uso de IA, riesgos y validacion.
- Clase 2:
  - VS Code, Copilot, contexto e instrucciones.
- Clase 3:
  - comprension de sistemas existentes, riesgos y pruebas iniciales.
- Clase 4:
  - automatizacion con Python y procesamiento de datos.
- Clase 5:
  - APIs, modelos generativos y configuracion operativa.
- Clase 6:
  - Copilot CLI, terminal y repetibilidad del flujo.
- Clase 7:
  - identificacion de procesos automatizables con IA.
- Clase 8:
  - analisis de oportunidades y priorizacion de iniciativas.
- Clase 9:
  - cierre del proyecto aplicado y consolidacion del trabajo del curso.

## Slide 4. Cambio de nivel respecto de la clase 6

- Clase 6:
  - operar mejor con Copilot CLI.
- Clase 7:
  - dejar de repetir instrucciones sueltas;
  - formalizar tareas recurrentes;
  - entender cuando hace falta traer herramientas o contexto externo.

## Slide 5. Elegir la capa correcta

- Prompt libre:
  - flexible y rapido;
  - depende mucho de quien lo escriba.
- Skill:
  - reusable y mas consistente;
  - sirve cuando la tarea ya esta razonablemente clara.
- MCP:
  - agrega alcance y herramientas;
  - sirve cuando hace falta salir del repo o del chat.

Idea central:

- no compiten siempre;
- a veces se complementan;
- y a veces ninguno hace falta.

## Slide 6. Que es un skill

- un skill es un paquete de instrucciones especializado para resolver una tarea concreta;
- no es una herramienta externa;
- no es una fuente nueva de datos;
- organiza una forma de trabajar para repetirla mejor.

Analogia:

- custom instruction:
  - como decirle a un colaborador "asi me gusta que trabajemos siempre".
- prompt file:
  - como pasarle una plantilla de solicitud ya armada.
- skill:
  - como entregarle una guia de trabajo especializada para una tarea recurrente.

## Slide 7. Ejemplos de skills

- revisar logs o incidentes siempre con la misma estructura;
- generar documentacion tecnica con un formato fijo;
- hacer triage de bugs recurrentes;
- revisar codigo con un criterio de equipo ya definido;
- preparar reportes operativos repetitivos;
- crear planes tecnicos o especificaciones con una plantilla estable.

Idea central:

- skill sirve mejor cuando la tarea se repite y ya sabes como quieres que se haga.

## Slide 8. Beneficios y limites de usar skills

- Beneficios:
  - misma tarea, misma forma de trabajar;
  - menos explicacion repetida;
  - mas facil delegar una tarea recurrente.
- Limites:
  - si el skill esta mal definido, repite errores con consistencia;
  - no sirve si la tarea aun esta mal entendida;
  - no reemplaza revision humana ni evidencia.

## Slide 9. Que es un MCP

- MCP es una forma estandar de conectar Copilot con herramientas o fuentes externas;
- no cambia solo la forma de responder;
- cambia a que contexto o herramientas puede acceder el agente.

Analogia:

- si el skill es una forma de trabajar mejor;
- el MCP es darle nuevas manos y nuevos ojos para interactuar con otros sistemas.

## Slide 10. Ejemplos de MCP

- GitHub MCP:
  - leer issues y PRs reales.
- Microsoft Learn MCP:
  - consultar documentacion oficial actual.
- MarkItDown MCP:
  - convertir PDF a Markdown reutilizable.
- DuckDB MCP:
  - consultar CSVs o datos tabulares con precision.
- Filesystem MCP:
  - leer archivos o carpetas fuera del contexto inmediato.
- Playwright MCP:
  - observar o automatizar una interfaz web.

## Slide 11. Beneficios y limites de usar MCP

- Si aporta:
  - cuando falta contexto fuera del repo;
  - cuando hace falta consultar una fuente oficial o un sistema real;
  - cuando el flujo necesita herramientas, no solo texto.
- No aporta tanto:
  - si el caso se resuelve con archivos locales;
  - si solo agrega setup y complejidad;
  - si se usa solo para que la demo se vea mas sofisticada.

Analogia:

- skill ensena una rutina;
- MCP abre una puerta hacia otra herramienta o fuente;
- si no hace falta salir de la pieza, abrir esa puerta agrega poco valor.

## Slide 12. Errores comunes

- encapsular demasiado pronto una tarea mal definida;
- usar skill como si fuera garantia de calidad;
- meter MCP cuando el repo local bastaba;
- confundir mas herramientas con mejor solucion;
- olvidar que el punto sigue siendo validar.

## Slide 13. 10 MCPs populares y su beneficio

- Referencia orientativa:
  - MCPs muy visibles en listas curadas, demos y flujos reales del ecosistema 2026.
- Lista:
  - GitHub MCP Server:
    - acceso a issues y PRs reales.
  - Context7 MCP:
    - documentacion tecnica actual y util para desarrollo.
  - Playwright MCP:
    - automatizacion y observacion web.
  - Figma MCP:
    - acceso a diseno y handoff de interfaces.
  - PostgreSQL MCP:
    - consultas sobre bases relacionales.
  - Supabase MCP:
    - acceso a base, auth y storage en un mismo stack.
  - Slack MCP:
    - acceso a conversaciones o contexto de equipo.
  - Notion MCP:
    - acceso a documentacion viva del equipo.
  - Linear MCP:
    - acceso a backlog e issues operativos.
  - Sentry MCP:
    - acceso a errores y contexto de incidentes.
  - MarkItDown MCP:
    - conversion de PDF a Markdown.

## Slide 14. 10 skills populares y su beneficio

- Referencia orientativa:
  - skills visibles en `awesome-copilot` y en flujos actuales de Copilot durante 2026.
- Lista:
  - Acquire Codebase Knowledge:
    - mapear y documentar una base de codigo existente.
  - Ai Ready:
    - preparar un repo para trabajar mejor con IA.
  - Agent Owasp Compliance:
    - revisar riesgos agenticos con foco de seguridad 2026.
  - Architecture Blueprint Generator:
    - generar arquitectura tecnica mas consistente.
  - Automate This:
    - convertir procesos manuales en automatizacion asistida.
  - Autoresearch:
    - ejecutar ciclos iterativos de mejora o experimentacion.
  - Aws Resource Query:
    - consultar recursos AWS en lenguaje natural.
  - Azure Architecture Autopilot:
    - diseñar o analizar arquitecturas Azure.
  - Boost Prompt:
    - refinar prompts de forma guiada.
  - Brag Sheet:
    - reconstruir y documentar impacto o trabajo realizado.
  - Aspire:
    - trabajar mejor con aplicaciones distribuidas en .NET Aspire.

## Slide 15. Bloque practico de hoy

- comparar prompt libre versus skill;
- instalar y probar algunos skills;
- revisar donde una herramienta externa o MCP si cambia el alcance;
- registrar:
  - que mejoro;
  - que se volvio mas complejo;
  - que siguio necesitando supervision humana.

## Slide 16. Cierre

- prompt, skill y MCP son capas distintas de trabajo.
- El valor no esta en usar mas piezas.
- El valor esta en elegir la capa correcta para la tarea correcta.
- Esto prepara la clase 8:
  - workflows avanzados con agente, CLI y herramientas.
