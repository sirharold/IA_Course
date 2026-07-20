# Clase 8: Agentes, subagentes y orquestacion con GitHub Copilot

## Objetivo

Entender como funciona el trabajo con agentes en GitHub Copilot durante 2026, cuando conviene usar agent mode, cuando crear agentes especializados, como delegar trabajo a subagentes y como mantener control, validacion y trazabilidad en flujos agenticos reales, reutilizando CLI, MCP y skills como capacidades ya conocidas y no como contenido nuevo.

## Cambio de nivel respecto de la clase 7

- Clase 7:
  - encapsular conocimiento reusable con instructions, prompt files, skills y criterio sobre MCP.
- Clase 8:
  - pasar de la customizacion reusable a la orquestacion agentica;
  - crear agentes especializados;
  - delegar tareas a subagentes;
  - y operar workflows asincronicos o multi paso sin perder control.

## Resultados de aprendizaje

- Diferenciar asistente, agent mode, custom agent, subagente y cloud agent.
- Explicar cuando un workflow agentico agrega valor real y cuando solo agrega complejidad.
- Crear un agente especializado con alcance, instrucciones y herramientas acotadas.
- Entender el rol de handoffs y subagentes en tareas multi etapa.
- Reconocer donde un agente puede reutilizar CLI, MCP o skills sin volver a disenar esas piezas.
- Definir puntos de validacion humana, evidencia y guardrails para un flujo con agentes.

## Contenidos

- Que es un agente en GitHub Copilot en 2026.
- Agent mode en IDE:
  - iteracion sobre errores;
  - refactorizacion;
  - desarrollo de features;
  - uso de contexto y herramientas.
- Agentes especializados:
  - built-in agents;
  - custom agents;
  - alcance y responsabilidades.
- Subagentes y handoffs:
  - delegacion;
  - contexto aislado;
  - coordinacion entre agentes.
- Copilot cloud agent:
  - investigacion;
  - plan;
  - cambios en rama;
  - apertura de pull request.
- Guardrails, permisos y validacion humana.
- Validacion humana, trazabilidad y limites de la automatizacion agentica.

## Lo que esta clase no vuelve a ensenar

- Copilot CLI como herramienta base:
  - eso ya se vio en la clase 6.
- Skills y customizacion reusable:
  - eso ya se vio en la clase 7.
- MCP como mecanismo para traer herramientas o contexto externo:
  - eso ya se introdujo en la clase 7.

En esta clase esas piezas se reutilizan solo cuando mejoran un workflow agentico o un ejercicio.

## Actividad practica

Tomar una tarea tecnica pequena ya conocida del curso y resolverla con un enfoque agentico concreto:

- crear o configurar un agente especializado;
- decidir si conviene reutilizar un skill, MCP o hook ya conocido;
- definir si una parte debe delegarse a un subagente;
- ejecutar una parte del flujo con evidencia visible;
- y justificar que controles humanos siguen siendo necesarios.

## Entregables

- Definicion breve del agente o agentes usados.
- Secuencia del workflow agentico.
- Evidencia de validacion:
  - diff;
  - test;
  - log;
  - salida estructurada;
  - o revision manual explicita.
- Comparacion corta entre una alternativa agentica y una alternativa mas simple.
- Limite principal o riesgo abierto del enfoque.

## Preparacion

- Tener acceso operativo a GitHub Copilot en el entorno que se use en clase.
- Idealmente contar con:
  - VS Code o Visual Studio con capacidades de agente;
  - Copilot CLI operativo;
  - y un repositorio o caso pequeno para practicar.
- Reutilizar casos de clases 3 a 7 para no gastar tiempo en inventar un problema nuevo.

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

## Ver tambien

- [agenda08.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%208/agenda08.md)
- [presentacion08.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%208/presentacion08.md)
- [REDISENO_CLASES_7_8_9.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/REDISENO_CLASES_7_8_9.md)
