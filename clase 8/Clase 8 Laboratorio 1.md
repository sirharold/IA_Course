# Clase 8 Laboratorio 1 - Agente de Triage de Incidentes

## Objetivo

Crear un agente especializado en triage de incidentes tecnicos y usarlo para investigar un problema real del servicio legado del curso.

## Duracion sugerida

- 15 minutos para crear el agente.
- 20 minutos para ejecutar el analisis.
- 10 minutos para validar resultados.

## Modalidad

- Profesor guiando en vivo.
- Alumnos replicando el mismo paso a paso en sus equipos.
- Individual o en parejas.

## Requisitos

- Visual Studio Code o Visual Studio con GitHub Copilot habilitado.
- Acceso a Copilot Chat o Agent Mode.
- Python operativo en terminal.
- Carpeta del curso disponible localmente.

## Carpeta de trabajo

- `clase 3/Ejercicios/reconciliation_legacy_service`

## Archivos que se usaran

- `logs/reconciliation_error.log`
- `logs/reconciliation_warning.log`
- `reconciliation/service.py`
- `reconciliation/matcher.py`
- `reconciliation/utils.py`
- `tests/test_smoke.py`

## Resultado esperado

Al finalizar, cada alumno o pareja deberia tener:

- un agente principal creado o configurado;
- un subagente creado o configurado;
- un resumen del incidente;
- una separacion entre hechos, hipotesis y dudas abiertas;
- un siguiente paso tecnico recomendado;
- una lista corta de pruebas o verificaciones sugeridas.

## Preparacion del docente

Antes de iniciar la clase:

1. Abrir la carpeta `clase 3/Ejercicios/reconciliation_legacy_service`.
2. Verificar que `main.py` corre.
3. Verificar que las pruebas base corren.
4. Tener abierto `reconciliation_error.log`.

## Parte 1. Abrir el caso y comprobar que el entorno funciona

### Bash

```bash
cd "clase 3/Ejercicios/reconciliation_legacy_service"
python3 main.py
python3 -m pytest tests/test_smoke.py -q
```

### PowerShell

```powershell
Set-Location "clase 3\Ejercicios\reconciliation_legacy_service"
python main.py
python -m pytest tests/test_smoke.py -q
```

### Que deberia ocurrir

- `main.py` deberia ejecutar la conciliacion.
- `test_smoke.py` deberia terminar sin errores.

Si algo falla, resolver eso antes de crear el agente.

## Parte 2. Crear el agente

### Metodo de creacion para este laboratorio

Crear el agente desde el chat usando el slash command que aparece en Copilot para crear agentes.

Si en el chat aparece `/create-agent`, usar ese comando.

Si en el chat aparece la variante `Create new custom agent` o una variante equivalente, usar esa opcion desde el mismo flujo.

### Nombre sugerido

- `Agente Principal de Triage`

### Como nombrar o invocar este agente

Seleccionar `Agente Principal de Triage` en el selector de agentes de Copilot.

Durante este laboratorio, cuando el profesor cambie de agente, los alumnos deben confirmar visualmente que el nombre del agente activo es el correcto antes de enviar el prompt.

### Paso a paso de creacion del agente principal

1. Abrir GitHub Copilot Chat.
2. Escribir `/` en la caja de prompt.
3. Seleccionar el comando para crear un agente nuevo.
4. Cuando Copilot pida el nombre, escribir exactamente: `Agente Principal de Triage`.
5. Si Copilot muestra el campo `Describe the trigger scenario or type of request that should use this agent`, escribir exactamente:

```text
Use this agent when the request is about investigating a technical incident, reading logs, separating facts from hypotheses, and proposing the next validation step without making large code changes.
```

6. Si Copilot muestra el paso `Where should this agent be saved`, seleccionar exactamente:

```text
Workspace (.github/agents/) Project specific, shared with team
```

7. Si Copilot muestra el paso `Which tool categories should this agent use?`, seleccionar exactamente:

```text
read-only
```

8. Si Copilot muestra un campo de descripcion corta, escribir exactamente:

```text
Investigates incidents using logs, code, and existing tests before proposing the next technical step.
```

9. Pegar las instrucciones base del agente.
10. Guardar el archivo del agente si Copilot abre un archivo `.agent.md`.

### Habilitar uso de subagentes en el agente principal

Despues de crear `Agente Principal de Triage`, hacer esto:

1. Abrir el archivo `.agent.md` del agente principal.
2. Buscar el texto o boton `Configure tool...`.
3. Hacer click en `Configure tool...`.
4. En el menu que se abre, buscar la categoria `agent`.
5. Dentro de `agent`, seleccionar `runSubagent`.
6. Guardar el archivo otra vez.

Este paso es necesario para que el agente principal pueda llamar al `Subagente de Logs`.

### Descripcion sugerida

- Analiza logs, codigo y pruebas existentes para separar hechos, hipotesis y pasos de validacion antes de proponer cambios.

### Instrucciones base del agente

Copiar y pegar este bloque en la configuracion del agente:

```text
## Constraints
- No inventar reglas de negocio.
- No proponer reescrituras grandes.
- No concluir una causa si la evidencia no alcanza.
- Separar siempre hechos observables, hipotesis y dudas abiertas.

## Approach
1. Leer el incidente o log entregado.
2. Revisar solo el codigo relevante antes de concluir.
3. Identificar archivos, funciones y pruebas relacionadas.
4. Consolidar evidencia antes de proponer un siguiente paso.
5. Si falta evidencia, decirlo explicitamente.

## Output
Entregar siempre:
- resumen corto del incidente;
- hechos observables;
- hipotesis principal;
- dudas abiertas;
- siguiente paso tecnico;
- pruebas o verificaciones sugeridas.
```

## Parte 3. Crear el subagente

### Nombre sugerido

- `Subagente de Logs`

### Como nombrar o invocar este subagente

Seleccionar `Subagente de Logs` en el selector de agentes de Copilot.

Antes de enviar el prompt del log, confirmar que no sigue activo `Agente Principal de Triage`.

### Paso a paso de creacion del subagente

1. Volver a la caja de prompt de Copilot Chat.
2. Escribir `/` en la caja de prompt.
3. Seleccionar nuevamente el comando para crear un agente nuevo.
4. Cuando Copilot pida el nombre, escribir exactamente: `Subagente de Logs`.
5. Si Copilot muestra el campo `Describe the trigger scenario or type of request that should use this agent`, escribir exactamente:

```text
Use this agent when the request is only about reading logs, extracting observable evidence, identifying mentioned modules, and listing open questions without deciding the root cause.
```

6. Si Copilot muestra el paso `Where should this agent be saved`, seleccionar exactamente:

```text
Workspace (.github/agents/) Project specific, shared with team
```

7. Si Copilot muestra el paso `Which tool categories should this agent use?`, seleccionar exactamente:

```text
read-only
```

8. Si Copilot muestra un campo de descripcion corta, escribir exactamente:

```text
Extracts only observable evidence from logs and runtime errors.
```

9. Pegar las instrucciones base del subagente.
10. Guardar el archivo del agente si Copilot abre un archivo `.agent.md`.

### Descripcion sugerida

- Revisa logs y errores runtime para devolver solo evidencia observable, sin proponer cambios de codigo.

### Instrucciones base del subagente

Copiar y pegar este bloque en la configuracion del subagente:

```text
## Constraints
- No proponer refactorizaciones ni cambios de arquitectura.
- No concluir causas si el log no las demuestra.
- No mezclar evidencia con interpretaciones.

## Approach
1. Leer logs y mensajes de error.
2. Extraer hechos observables.
3. Identificar patrones repetidos, excepciones y archivos mencionados.
4. Dejar fuera cualquier recomendacion de cambio.

## Output
Entregar siempre:
- error principal observado;
- archivos o modulos mencionados;
- pistas tecnicas concretas;
- dudas abiertas.
```

## Parte 4. Primera ejecucion del subagente

Con `Subagente de Logs` activo, abrir `logs/reconciliation_error.log` y luego enviar este prompt:

```text
Analiza este log y entrega solo evidencia observable.

Necesito:
1. Error principal.
2. Modulos o archivos mencionados.
3. Pistas tecnicas concretas.
4. Dudas abiertas.

No propongas aun una causa raiz.
```

Guardar esa salida porque el agente principal la usara despues.

## Parte 5. Primera ejecucion del agente principal

Con `Agente Principal de Triage` activo, enviar este prompt:

```text
Analiza este incidente.

Necesito que:
1. Resumas el error en no mas de 5 lineas.
2. Identifiques que archivos deberia revisar primero.
3. Separes hechos, hipotesis y dudas abiertas.
4. Si necesitas evidencia puntual del log, usa el Subagente de Logs.
5. Propongas un siguiente paso tecnico sin modificar codigo todavia.

No inventes comportamiento no visible.
```

Si el agente principal no logra invocar al subagente, copiar y pegar manualmente la salida del subagente en el mismo chat.

## Parte 6. Validar la respuesta del agente principal

No aceptar la respuesta de inmediato.

Hacer esta validacion minima:

1. Abrir los archivos que el agente menciona.
2. Confirmar si los nombres de funciones y modulos existen de verdad.
3. Revisar si la hipotesis principal tiene evidencia en el log o en el codigo.
4. Marcar cualquier afirmacion que no tenga respaldo observable.

## Parte 7. Segunda ejecucion del agente principal

Enviar un segundo prompt para obligarlo a cerrar mejor:

```text
Ahora quiero una salida mas operativa.

Entrega:
1. Hechos observables.
2. Hipotesis principal.
3. Hipotesis secundaria.
4. Codigo exacto que deberia revisar una persona.
5. Dos verificaciones manuales o pruebas pequenas para confirmar o descartar la causa.

No sugieras aun una refactorizacion.
```

## Parte 8. Como probar que el trabajo quedo bien

El laboratorio queda bien si se cumple todo esto:

1. El subagente devuelve evidencia y no conclusiones infladas.
2. El agente principal cita archivos reales del proyecto.
3. La hipotesis principal se puede defender con evidencia.
4. Las dudas abiertas estan explicitadas.
5. Las pruebas o verificaciones propuestas son pequenas y ejecutables.
6. El alumno puede explicar:
   - que hizo el subagente;
   - que hizo el agente principal;
   - que parte sigue siendo juicio humano.

## Entregable final

Cada alumno o pareja debe dejar:

- nombre del agente principal;
- nombre del subagente;
- salida corta del subagente con evidencia;
- bloque corto del agente principal con:
  - hechos;
  - hipotesis principal;
  - dudas abiertas;
  - siguiente paso tecnico;
- una lista de dos verificaciones concretas.

## Variante si la invocacion del subagente no funciona

Si el entorno no logra ejecutar `runSubagent`:

1. Ejecutar primero el subagente en un chat o sesion separada.
2. Copiar su salida.
3. Pegar esa salida como contexto para el agente principal.
4. Pedir al agente principal que no vuelva a analizar el log desde cero, sino que use la evidencia entregada.

## Extension opcional

Si el grupo avanza rapido, pedir esta variante:

```text
Actua como agente principal de triage.

Define un handoff minimo para un subagente de logs:
1. Que entrada le darias.
2. Que salida exacta esperarias.
3. Que decision final seguiria quedando en manos de una persona.
```
