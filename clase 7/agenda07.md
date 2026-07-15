# Agenda 07

Hora inicio: 15:00

Hora fin: 18:00

Duracion: 180 minutos

Break: 10 minutos

Tema: skills, customizacion reusable y MCP en Copilot

## Objetivo de la sesion

Entender como pasar de prompts aislados a capacidades mas reutilizables con instructions, prompt files y skills, e introducir MCP como mecanismo para ampliar el alcance de Copilot cuando el workspace local no basta.

## Ajuste de foco para esta clase

- Esta sesion ya no se centra en evaluacion extensa de oportunidades.
- El foco pasa a ser:
  - reducir ambiguedad;
  - reutilizar criterio tecnico;
  - entender cuando encapsular;
  - entender cuando hace falta herramienta o contexto externo.
- La clase no busca convertir a MCP en tema dominante.
- Si busca que los alumnos entiendan:
  - que es;
  - que aporta;
  - que no aporta;
  - y cuando conviene no usarlo.

## Relacion con el temario rediseñado

Esta agenda cubre la nueva orientacion de la clase 7:

- customizacion avanzada de Copilot;
- diferencia entre prompt, instruction, prompt file y skill;
- beneficios y contras de encapsular conocimiento reusable;
- introduccion practica a MCP;
- preparacion para workflows avanzados en la clase 8.

## Sustento oficial recomendado

Usar como base de esta sesion:

- Microsoft Learn:
  - GitHub Copilot Fundamentals Part 1 of 2;
  - Introduction to prompt engineering with GitHub Copilot;
  - Configure GitHub Copilot instructions and create custom agents;
  - Using advanced GitHub Copilot features.
- GitHub Docs:
  - Customization library;
  - Using custom instructions to unlock the power of Copilot code review;
  - Best practices for using GitHub Copilot;
  - Best practices for GitHub Copilot CLI.

Estos materiales deben sostener:

- definiciones;
- comparaciones;
- beneficios y limites;
- y criterio de uso.

## Resumen de la agenda

| Horario | Duracion | Bloque |
| --- | --- | --- |
| 15:00-15:15 | 15 min | Recuperacion de la clase 6 y encuadre de la sesion |
| 15:15-15:35 | 20 min | Del prompt aislado a la capacidad reusable |
| 15:35-15:55 | 20 min | Instructions, prompt files y skills: diferencias practicas |
| 15:55-16:15 | 20 min | Beneficios, contras y errores comunes al encapsular |
| 16:15-16:25 | 10 min | Break |
| 16:25-16:45 | 20 min | MCP: que es, que aporta y que no aporta |
| 16:45-17:05 | 20 min | Panorama rapido: MCPs y skills populares |
| 17:05-17:50 | 45 min | Laboratorio guiado: 2 ejercicios base y una comparacion corta |
| 17:50-18:00 | 10 min | Cierre y siguiente trabajo |

## Supuestos para esta clase

- Los participantes ya usaron Copilot en editor y/o terminal.
- El grupo ya conoce prompting tecnico y validacion minima.
- Se cuenta con acceso operativo a Copilot en el entorno de trabajo.
- Los alumnos pueden reutilizar tareas reales del curso para probar capacidades reutilizables.

## Enfoque metodologico

- partir desde tareas tecnicas reales y no desde taxonomias abstractas;
- mostrar que repetir prompts no escala bien;
- distinguir entre encapsular criterio y ampliar alcance;
- no presentar MCP como solucion universal;
- dejar instalada una base conceptual util para la clase 8.

## Agenda detallada

- 15:00-15:15 Recuperacion de la clase 6 y encuadre de la sesion.
  - Retomar:
    - que se vio sobre Copilot CLI;
    - donde aparecio repeticion de instrucciones;
    - donde hizo falta mas contexto o mas herramientas.
  - Abrir la pregunta de hoy:
    - como reducir repeticion;
    - como hacer tareas mas consistentes;
    - y cuando el repo local deja de ser suficiente.

- 15:15-15:35 Del prompt aislado a la capacidad reusable.
  - Diferenciar:
    - pedir algo una vez;
    - repetir una tarea muchas veces;
    - convertir esa tarea en una capacidad reutilizable.
  - Mostrar por que importa:
    - menos variacion;
    - menos perdida de contexto;
    - mejor consistencia entre personas.

- 15:35-15:55 Instructions, prompt files y skills: diferencias practicas.
  - Custom instructions:
    - reglas persistentes de comportamiento.
  - Prompt files:
    - estructura reusable para tareas frecuentes.
  - Skills:
    - capacidad reusable mas acotada y mas operativa.
  - Cerrar con criterio de uso:
    - cuando basta instruction;
    - cuando conviene prompt file;
    - cuando tiene sentido skill.

- 15:55-16:15 Beneficios, contras y errores comunes al encapsular.
  - Beneficios:
    - consistencia;
    - menos ambiguedad;
    - ahorro de tiempo;
    - mejor delegacion.
  - Contras:
    - rigidez prematura;
    - mantenimiento extra;
    - error repetido con mas consistencia.
  - Error comun:
    - encapsular una tarea que todavia no esta bien definida.

- 16:15-16:25 Break.

- 16:25-16:45 MCP: que es, que aporta y que no aporta.
  - Explicar MCP en una idea:
    - herramienta para ampliar acceso a contexto y acciones mas alla del chat o archivo local.
  - Casos donde si aporta:
    - herramientas externas;
    - fuentes fuera del repo;
    - workflows que cruzan sistemas.
  - Casos donde no aporta tanto:
    - cuando el repo local basta;
    - cuando agrega friccion sin valor;
    - cuando solo hace la demo mas sofisticada.

- 16:45-17:05 Panorama rapido: MCPs y skills populares.
  - Mostrar:
    - que tipos de MCPs aparecen con frecuencia;
    - que tipos de skills son comunes en Copilot;
    - por que conviene verlos como referencia y no como checklist para instalar todo.
  - Cerrar con criterio:
    - que parece reusable;
    - que parece redundante;
    - que vale la pena explorar despues.

- 17:05-17:50 Laboratorio guiado: 2 ejercicios base y una comparacion corta.
  - Trabajo individual o en parejas.
  - En clase no se intentan resolver los 10 ejercicios.
  - Seleccion sugerida para la sesion:
    - 1 ejercicio de skills;
    - 1 ejercicio de MCP;
    - 1 comparacion corta entre prompt libre y skill.
  - Objetivos:
    - probar al menos un skill;
    - observar un caso donde MCP aporte de verdad;
    - distinguir entre necesidad real y complejidad innecesaria.
  - Entregable minimo:
    - ejercicio de skills completado o avanzado;
    - ejercicio de MCP completado o avanzado;
    - nota breve comparando prompt libre, skill y MCP.

- 17:50-18:00 Cierre y siguiente trabajo.
  - Sintetizar:
    - que mejoro;
    - que se volvio mas complejo;
    - que siguio necesitando supervision humana.
  - Preparar la transicion hacia la clase 8, donde skill, agente, CLI y tooling ya aparecen dentro de workflows mas ricos.

## Checklist operativa para la sesion

Usar esta secuencia durante la clase:

1. Identificar una tarea tecnica que se repita.
2. Revisar como se resuelve hoy con prompt libre.
3. Decidir si vale la pena encapsularla.
4. Comparar instruction, prompt file y skill como opciones.
5. Probar al menos un skill.
6. Preguntarse si el caso realmente necesita tooling o contexto externo.
7. Registrar beneficio observado, complejidad agregada y validacion humana necesaria.

## Criterio de carga de trabajo

- Los 10 ejercicios base son un banco de practica, no una lista para completar en una sola sesion.
- Los 3 ejercicios avanzados tampoco estan pensados para resolverse completos dentro de estas 3 horas.
- Para una clase de 180 minutos, la carga razonable es:
  - 1 ejercicio corto de skills;
  - 1 ejercicio corto de MCP;
  - 1 revision corta de ejemplos de MCPs y skills del ecosistema;
  - 1 comparacion corta entre enfoques;
  - y dejar los ejercicios avanzados como extension, tarea o laboratorio largo.

## Tarea para los alumnos

Preparar el insumo para la clase 8:

1. Traer una tarea tecnica pequena donde skill, agente o CLI pudieran compararse.
2. Documentar en media pagina:
   - que tarea eligieron;
   - que parte era repetitiva;
   - que customizacion probaron;
   - si MCP aportaria o no;
   - que beneficio obtuvieron;
   - que riesgo o limite vieron.
3. Traer una pregunta abierta sobre:
   - cuando usar skill;
   - cuando usar prompt libre;
   - cuando pasar a workflow con agente, CLI o tooling externo.
