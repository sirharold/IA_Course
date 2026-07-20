# Agenda 08

Hora inicio: 15:00

Hora fin: 18:00

Duracion: 180 minutos

Break: 10 minutos

Tema: agentes, subagentes y orquestacion con GitHub Copilot

## Objetivo de la sesion

Dar a los alumnos una base practica y actualizada para trabajar con agentes en GitHub Copilot durante 2026, incluyendo agent mode, agentes especializados, subagentes, handoffs, cloud agent y criterios de validacion, reutilizando CLI, MCP y skills solo como piezas ya conocidas, y cerrar la clase dejando preparados los documentos de la clase 7 para el proyecto final de la clase 9.

## Ajuste de foco para esta clase

- La clase 7 se concentro en customizacion reusable.
- La clase 8 deja de poner el foco principal en la pieza reusable aislada.
- El foco pasa a ser:
  - que es un agente de verdad;
  - como se crea o configura;
  - cuando conviene delegar;
  - como se coordinan agente principal y subagentes;
  - y como evitar que el workflow se vuelva opaco.

## Lo que no repetiremos en esta clase

- No volveremos a ensenar Copilot CLI desde cero:
  - eso ya fue contenido de la clase 6.
- No volveremos a ensenar skills ni MCP como tema base:
  - eso ya fue contenido de la clase 7.
- Si apareceran en ejercicios o demos:
  - pero solo como partes de un workflow agentico mas grande.

## Relacion con el temario rediseñado

Esta agenda actualiza la nueva orientacion de la clase 8:

- agent mode como forma de trabajo;
- custom agents como especializacion;
- subagentes y handoffs como mecanismo de delegacion;
- cloud agent como superficie asincronica relevante;
- validacion humana y guardrails como parte obligatoria del flujo.

## Sustento oficial recomendado

Usar como base de esta sesion:

- Microsoft Learn:
  - Configure GitHub Copilot Instructions and Create Custom Agents;
  - Building applications with GitHub Copilot Agent Mode.
- GitHub Docs:
  - Creating and using custom agents for GitHub Copilot CLI;
  - Creating custom agents for Copilot cloud agent;
  - Using hooks with GitHub Copilot CLI;
  - Best practices for GitHub Copilot CLI.
- Microsoft Learn para Visual Studio 2026:
  - Use built-in and custom agents with GitHub Copilot;
  - Use Agent Skills with GitHub Copilot.

Estos materiales deben sostener:

- definiciones;
- casos de uso;
- delegacion y handoffs;
- creacion de agentes;
- criterios de control;
- y transicion operativa hacia el proyecto final.

## Resumen de la agenda

| Horario | Duracion | Bloque |
| --- | --- | --- |
| 15:00-15:15 | 15 min | Repaso de la clase 7 y encuadre de agentes |
| 15:15-15:35 | 20 min | Que es un agente en Copilot en 2026 |
| 15:35-15:55 | 20 min | Agent mode, custom agents y built-in agents |
| 15:55-16:15 | 20 min | Subagentes, handoffs y patron multiagente |
| 16:15-16:25 | 10 min | Break |
| 16:25-16:45 | 20 min | Crear agentes y elegir superficie agentica |
| 16:45-17:30 | 45 min | Laboratorio guiado: crear o configurar un agente pequeno |
| 17:30-18:00 | 30 min | Ajuste de documentos de clase 7 para el proyecto final |

## Supuestos para esta clase

- Los participantes ya conocen prompting, validacion minima y customizacion reusable.
- El grupo ya probo Copilot en editor y/o terminal.
- El grupo ya vio CLI en la clase 6.
- El grupo ya vio skills y MCP en la clase 7.
- No todos tendran exactamente la misma superficie disponible:
  - algunos usaran VS Code;
  - otros Visual Studio;
  - otros CLI o GitHub.
- La clase debe servir aunque no todos puedan ejecutar cloud agent en vivo.

## Enfoque metodologico

- partir desde casos tecnicos reales ya usados en el curso;
- explicar agentes como mecanismo operativo, no como marketing;
- distinguir entre agente generalista y agente especializado;
- no reciclar una clase entera para reensenar herramientas ya vistas;
- mostrar que delegar no elimina responsabilidad;
- cerrar con evidencia visible y documentos listos para el integrador.

## Agenda detallada

- 15:00-15:15 Repaso de la clase 7 y encuadre de agentes.
  - Recuperar:
    - que ya sabemos sobre instructions, skills y MCP;
    - y que ya sabemos sobre CLI como superficie operativa.
  - Abrir la pregunta de hoy:
    - que cambia cuando pasamos desde una capacidad reusable a una estructura de delegacion agentica.

- 15:15-15:35 Que es un agente en Copilot en 2026.
  - Diferenciar:
    - asistente conversacional;
    - agent mode;
    - custom agent;
    - subagente;
    - cloud agent.
  - Idea central:
    - un agente no solo responde;
    - investiga, decide pasos, usa herramientas y ejecuta tareas con mayor autonomia.

- 15:35-15:55 Agent mode, custom agents y built-in agents.
  - Agent mode:
    - itera sobre errores;
    - propone cambios;
    - usa contexto del proyecto.
  - Built-in agents:
    - especializados en tareas como debugging, testing o profiling en ciertos entornos.
  - Custom agents:
    - permiten definir especializacion, herramientas y alcance para tareas de equipo.

- 15:55-16:15 Subagentes, handoffs y patron multiagente.
  - Subagente:
    - agente temporal o especializado al que se delega una parte del trabajo.
  - Handoff:
    - paso controlado de una etapa del workflow a otra.
  - Pregunta clave:
    - que parte conviene delegar y que parte debe quedar en el agente principal o en la persona.

- 16:15-16:25 Break.

- 16:25-16:45 Crear agentes y elegir superficie agentica.
  - Crear agentes:
    - definir objetivo;
    - delimitar alcance;
    - declarar herramientas;
    - fijar restricciones.
  - Cloud agent:
    - trabajo asincronico en GitHub sobre ramas y pull requests.
  - Criterio:
    - reutilizar CLI, MCP o skills solo cuando ya mejoran de verdad la tarea del agente.

- 16:45-17:30 Laboratorio guiado: crear o configurar un agente pequeno.
  - Trabajo individual o en parejas.
  - Opciones sugeridas:
    - agente de triage de incidentes;
    - agente de documentacion tecnica;
    - agente de refactorizacion acotada;
    - agente de validacion de scripts de datos;
    - agente para preparar pruebas iniciales desde riesgos.
  - Objetivos:
    - definir el problema;
    - declarar especializacion del agente;
    - decidir si conviene reutilizar skill, hook o MCP;
    - decidir si alguna parte debe ir a subagente;
    - dejar evidencia visible de validacion;
    - comparar contra una alternativa menos agentica.

- 17:30-18:00 Ajuste de documentos de clase 7 para el proyecto final.
  - Reabrir los documentos creados o ajustados en la clase 7:
    - instructions;
    - prompt files;
    - skills;
    - notas de MCP si existen.
  - Modificarlos para el caso que se llevara a la clase 9.
  - Cada equipo debe dejar:
    - un problema tecnico pequeno elegido;
    - el agente o combinacion de agentes que usara;
    - el documento reusable ajustado para ese caso;
    - la validacion que mostrara en la demo final.

## Checklist operativa para la sesion

Usar esta secuencia durante la clase:

1. Elegir una tarea tecnica pequena del curso.
2. Definir si realmente requiere agente o basta una alternativa mas simple.
3. Si requiere agente, delimitar especializacion y herramientas.
4. Decidir si alguna parte debe delegarse a un subagente.
5. Ejecutar el flujo en pasos visibles.
6. Validar con evidencia concreta.
7. Registrar donde el enfoque agentico aporto y donde agrego costo.
8. Ajustar los documentos reutilizables de la clase 7 para el caso final.

## Criterio de carga de trabajo

- Esta clase no busca construir una plataforma completa de agentes.
- La carga razonable para 180 minutos es:
  - entender las superficies principales;
  - crear o adaptar un agente pequeno;
  - discutir un caso de subagente o handoff;
  - ejecutar una prueba corta;
  - y dejar ajustados los documentos que se usaran en la demo final.

## Tarea para los alumnos

Preparar el caso de la clase 9:

1. Elegir un problema tecnico demostrable.
2. Definir que parte resolvera el agente.
3. Definir que no delegaran.
4. Ajustar el documento reusable que usaran en la demo.
5. Preparar evidencia de entrada, salida y validacion.
6. Explicar por que no eligieron una alternativa mas simple.
