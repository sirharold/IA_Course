# Presentacion 08 - Agentes, subagentes y orquestacion con GitHub Copilot

## Slide 1. Titulo

- Clase 8 de 9
- Agentes, subagentes y orquestacion con GitHub Copilot
- Mensaje clave:
  - ya no estamos aprendiendo solo a customizar capacidades;
  - estamos aprendiendo a delegar, coordinar y controlar trabajo agentico.

## Slide 2. Agenda

- Que es un agente en Copilot hoy.
- Cuando agent mode aporta y cuando no.
- Custom agents, subagentes y handoffs.
- Crear agentes y elegir bien la superficie.
- Riesgos, guardrails y preparacion operativa para la clase 9.

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
  - customizacion reusable con instructions, prompt files, skills y MCP.
- Clase 8:
  - agentes, subagentes y orquestacion con Copilot.
- Clase 9:
  - proyecto integrador con Copilot avanzado.

## Slide 4. Que es un agente en Copilot en 2026

- no solo responde preguntas;
- puede planificar;
- puede usar herramientas;
- puede iterar sobre errores;
- puede editar artefactos;
- puede delegar partes del trabajo;
- puede operar de forma sincronica o asincronica segun la superficie.

Idea central:

- un agente no reemplaza al desarrollador;
- le cambia la forma de coordinar el trabajo.

## Slide 5. Las superficies agenticas que importan

- Agent mode en IDE:
  - iteracion directa sobre el proyecto.
- Copilot cloud agent:
  - investigacion y cambios en GitHub sobre ramas y pull requests.
- Custom agents:
  - especializacion por tarea, equipo o workflow.
- Built-in agents:
  - agentes ya afinados para ciertos trabajos en algunos entornos.

Idea central:

- no todas las superficies sirven para lo mismo;
- elegir mal la superficie produce mas friccion que valor.

## Slide 6. Agent mode: donde aporta de verdad

- sirve cuando hay una tarea tecnica multi paso dentro del proyecto;
- sirve cuando el trabajo requiere leer, editar, probar y volver a iterar;
- sirve cuando un chat comun obliga a repetir demasiado contexto;
- sirve cuando el costo de coordinar pasos manualmente ya es alto.

Limite:

- no conviene para tareas triviales;
- no reemplaza criterio tecnico;
- sin contexto, restricciones y validacion, un agente mas potente tambien se equivoca mas lejos.

## Slide 7. Custom agents: por que importan

- importan cuando una tarea ya se repite con suficiente claridad;
- permiten especializar comportamiento sin contaminar al agente principal;
- permiten acotar herramientas, foco y expectativas;
- permiten reutilizar una forma de trabajar del equipo con menos ambiguedad.

Ejemplos utiles para el curso:

- agente de triage de incidentes;
- agente de documentacion tecnica;
- agente de pruebas desde riesgos;
- agente de refactorizacion segura.

## Slide 8. Subagentes y handoffs

- subagente:
  - agente temporal o especializado que toma una subtarea.
- handoff:
  - transferencia explicita de una etapa del trabajo a otro agente o contexto.

Por que importa:

- aislar contexto;
- evitar saturar al agente principal;
- separar investigacion, ejecucion y validacion;
- mantener mejor trazabilidad del flujo.

Patron util:

- agente principal:
  - entiende el problema y define el plan.
- subagente:
  - resuelve una parte acotada.
- humano:
  - valida, corrige y decide si se continua.

## Slide 9. Crear agentes y elegir la superficie correcta

- crear un agente obliga a definir:
  - objetivo;
  - alcance;
  - herramientas;
  - restricciones;
  - y criterio de exito.
- Cloud agent:
  - mejor para trabajo asincronico sobre ramas, investigacion y cambios que terminan en PR.

Pregunta clave:

- necesito agent mode en el entorno local;
- o necesito delegar trabajo en GitHub y revisarlo despues.

Criterio practico:

- si necesito iteracion rapida sobre codigo local:
  - agent mode.
- si necesito trabajo asincronico revisable:
  - cloud agent.
- si no hay una tarea realmente agentica:
  - no fuerces un agente.

## Slide 10. Reutilizar lo ya visto sin repetirlo

- CLI:
  - sirve si el agente necesita operacion visible o apoyo de terminal.
- Skills:
  - sirven si una parte del trabajo ya tiene una rutina reusable.
- MCP:
  - sirve si el agente necesita contexto o herramientas fuera del repo local.

Regla simple:

- no meter estas piezas por moda;
- meterlas solo si reducen ambiguedad o mejoran validacion.

## Slide 11. Riesgos y guardrails

- delegar demasiado pronto;
- mezclar muchas piezas sin entender el flujo;
- dar herramientas amplias sin restricciones;
- aceptar resultados convincentes sin evidencia;
- usar agentes para tareas que aun no estan bien definidas.

Guardrails minimos:

- objetivo claro;
- alcance acotado;
- evidencia visible;
- revision humana;
- limite explicitado.

## Slide 12. Ultimos 30 minutos de hoy

- reabrir documentos creados o ajustados en la clase 7;
- modificar instructions, prompt files o skills para el caso final;
- dejar lista la pieza reusable que se usara en la clase 9;
- definir:
  - problema tecnico;
  - agente o combinacion de agentes;
  - validacion que se mostrara.

Idea central:

- la clase 9 no deberia partir desde cero;
- deberia partir desde una base reusable ya afinada.

## Slide 13. Cierre y puente a la clase 9

- en 2026 saber prompting ya no basta.
- hay que saber cuando delegar y cuando no.
- hay que saber crear especializacion sin perder control.
- la clase 9 pedira una demo pequena, clara y defendible:
  - problema real;
  - agente o combinacion elegida;
  - validacion;
  - y criterio tecnico.
