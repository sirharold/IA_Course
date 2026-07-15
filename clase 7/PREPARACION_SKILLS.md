# Preparacion y demos de skills - Clase 7

Fecha de revision: 2026-07-15

## Objetivo de este documento

Este documento sirve para preparar la parte de skills de la clase 7 y tambien para ejecutar demos simples durante la sesion.

La idea es:

1. entender que es un skill;
2. dejar uno o mas skills listos para usar;
3. comparar una tarea sin skill y con skill;
4. discutir si el skill realmente agrego consistencia o solo agrego trabajo extra.

## Que es un skill

Un skill es un paquete de instrucciones especializado para resolver una tarea concreta de forma mas repetible.

No agrega una fuente nueva de datos por si mismo.

No conecta automaticamente herramientas externas.

Lo que hace es organizar una forma de trabajar para que Copilot la reutilice cuando la tarea corresponde.

## Analogia

- custom instruction:
  - decirle a un colaborador como te gusta trabajar siempre.
- prompt file:
  - pasarle una plantilla ya armada.
- skill:
  - entregarle una guia de trabajo especializada para una tarea recurrente.

En simple:

- skill:
  - ensena una rutina.
- MCP:
  - abre una puerta hacia otra herramienta o fuente.

## Donde viven los skills

Segun GitHub Docs, Copilot soporta skills en estas ubicaciones:

- skills del proyecto:
  - `.github/skills`
  - `.claude/skills`
  - `.agents/skills`
- skills personales:
  - `~/.copilot/skills`
  - `~/.agents/skills`

Para esta clase, la recomendacion es usar `skills del proyecto`, porque:

- quedan ligados al repo del curso;
- son mas faciles de mostrar;
- no dependen del home de cada alumno.

## Estructura minima de un skill

Cada skill debe vivir en su propia carpeta.

Ejemplo:

```text
.github/skills/revision-logs/
└── SKILL.md
```

El archivo obligatorio es `SKILL.md`.

## Contenido minimo de SKILL.md

Un skill simple usa un archivo Markdown con frontmatter YAML.

Ejemplo minimo:

```md
---
name: revision-logs
description: Guia para revisar logs tecnicos. Usar cuando se pida analizar logs o incidentes.
---

Cuando te pidan analizar logs:

1. Resume hechos observables.
2. Separa errores, advertencias y dudas.
3. No inventes causas si no hay evidencia.
4. Cierra con una validacion minima sugerida.
```

## Preparacion recomendada para la clase

## Opcion A: crear un skill simple del curso

1. En el repo, crea esta carpeta:

```text
.github/skills/revision-logs
```

2. Dentro, crea el archivo `SKILL.md`.
3. Pega una version simple como la del ejemplo anterior.
4. Guarda los cambios.

## Opcion B: instalar un skill existente

Segun GitHub Docs, tambien puedes:

- descargar un skill ya hecho y mover su carpeta a `.github/skills`;
- o usar `gh skill` en GitHub CLI para buscar e instalar skills.

Para esta clase, la opcion mas estable es:

- copiar o crear un skill pequeno dentro del repo;
- evitar depender de instalacion externa si no es necesaria.

## Como verificar que Copilot ve el skill

### En Copilot CLI

1. Inicia una sesion de Copilot CLI.
2. Si ya estabas dentro de una sesion, ejecuta:

```text
/skills reload
```

3. Luego ejecuta:

```text
/skills info revision-logs
```

4. Si el skill aparece, ya fue detectado.

### En otros clientes

La verificacion practica es mas simple:

1. Pide una tarea que encaje exactamente con la descripcion del skill.
2. Revisa si la salida sigue la estructura definida en `SKILL.md`.

## Skill recomendado 1: revision de logs

### Que hace este skill

Ordena el analisis de logs o incidentes para que Copilot no responda de forma caotica cada vez.

### Que beneficio aporta

- misma estructura de salida;
- menos ambiguedad;
- menos necesidad de volver a explicar el formato esperado.

### Demo sugerida

#### Sin skill

Usa un archivo de logs del curso, por ejemplo:

- [sample_runtime_logs.ndjson](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%202/sample_runtime_logs.ndjson)

Prompt:

```text
Analiza estos logs y dime que esta pasando.
```

#### Con skill

Prompt:

```text
Analiza estos logs y entrega:
1. hechos observables
2. errores repetidos
3. dudas o ambiguedades
4. validacion minima sugerida
```

O pide la misma tarea y observa si Copilot activa el skill automaticamente.

#### Que observar

- con skill, la respuesta deberia salir mas ordenada;
- el beneficio no es "mas inteligencia";
- el beneficio es "mas consistencia".

## Skill recomendado 2: documentacion tecnica breve

### Que hace este skill

Estandariza como Copilot resume o documenta un modulo, endpoint o script.

### Que beneficio aporta

- documentacion mas pareja;
- menos diferencias entre quien pide la tarea;
- mejor reutilizacion del formato.

### Demo sugerida

#### Sin skill

Prompt:

```text
Documenta este script de forma breve.
```

#### Con skill

Prompt:

```text
Documenta este script usando esta estructura:
1. objetivo
2. entradas
3. salidas
4. riesgos
5. como validarlo
```

#### Que observar

- con skill, la estructura deberia ser mas estable;
- sin skill, la salida puede variar bastante entre ejecuciones.

## Skill recomendado 3: code review guiado

### Que hace este skill

Hace que Copilot revise cambios con un criterio tecnico repetible en vez de comentarios dispersos.

### Que beneficio aporta

- revisiones mas comparables;
- mas foco en riesgos reales;
- menos comentarios superficiales.

### Demo sugerida

#### Sin skill

Prompt:

```text
Revisa este cambio de codigo.
```

#### Con skill

Prompt:

```text
Revisa este cambio de codigo y reporta:
1. riesgos funcionales
2. riesgos de mantenimiento
3. validaciones faltantes
4. pruebas recomendadas
```

#### Que observar

- con skill, la revision deberia ser mas util para trabajo de equipo;
- sin skill, puede quedarse en observaciones mas generales.

## Criterio para decidir si un skill vale la pena

Un skill vale la pena cuando:

- la tarea se repite;
- ya sabes como quieres que se haga;
- quieres menos variacion entre personas o entre ejecuciones.

Un skill no vale tanto la pena cuando:

- la tarea todavia no esta clara;
- aun estas explorando el problema;
- el costo de mantener el skill es mayor que repetir el prompt.

## Checklist minimo antes de la clase

1. Tienes al menos un skill listo en el repo o en tu carpeta personal.
2. El skill tiene `SKILL.md` con nombre y descripcion claros.
3. Probaste una tarea sin skill y la misma tarea con skill.
4. Ya sabes que diferencia quieres mostrar.
5. Tienes un plan B si el cliente no activa el skill automaticamente.

## Plan B rapido

- Si Copilot no activa el skill solo:
  - formula el prompt de forma mas cercana a la descripcion del skill.
- Si aun asi no se nota:
  - muestra el `SKILL.md` y explica que el valor esperado era consistencia de salida.
- Si el entorno del alumno no detecta el skill:
  - usa un skill ya preparado por el docente y muestra la demo desde tu entorno.

## Recomendacion final para clase 7

Si quieres una sesion estable:

1. usa un skill pequeno y muy claro;
2. evita skills demasiado largos o ambiguos;
3. compara siempre una tarea sin skill y con skill;
4. evalua el resultado por consistencia, no por espectacularidad.
