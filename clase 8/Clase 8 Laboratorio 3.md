# Clase 8 Laboratorio 3 - Agente de Documentacion Tecnica

## Objetivo

Crear un agente especializado en documentar comportamiento tecnico observable sin inventar reglas ni suposiciones.

## Duracion sugerida

- 15 minutos para crear el agente.
- 20 minutos para generar documentacion.
- 10 minutos para revisar y corregir.

## Modalidad

- Profesor guiando en vivo.
- Alumnos replicando el mismo caso.
- Individual o en parejas.

## Requisitos

- Visual Studio Code o Visual Studio con GitHub Copilot habilitado.
- Acceso a Copilot Chat o Agent Mode.
- Python operativo en terminal.

## Carpeta de trabajo

- `clase 4/codigo`

## Archivo principal

- `reconcile_transactions.py`

## Resultado esperado

Al finalizar, cada alumno o pareja deberia tener:

- un agente creado o configurado;
- una explicacion tecnica breve del modulo;
- una seccion de entradas, salidas y supuestos;
- una seccion de limites o ambiguedades;
- una validacion manual de que la documentacion coincide con el codigo.

## Preparacion del docente

Antes de iniciar la clase:

1. Abrir `clase 4/codigo/reconcile_transactions.py`.
2. Ejecutar el script una vez para recordar su salida.
3. Tener abierto `output/reconciliation_report.json` si ya existe.

## Parte 1. Validar el contexto tecnico

### Bash

```bash
cd "clase 4/codigo"
python3 reconcile_transactions.py
```

### PowerShell

```powershell
Set-Location "clase 4\codigo"
python reconcile_transactions.py
```

### Que deberia ocurrir

- El script deberia generar un reporte en JSON.
- La salida en terminal deberia mostrar un resumen de conciliacion.

## Parte 2. Crear el agente

### Metodo de creacion para este laboratorio

Crear el agente manualmente como archivo `.agent.md` dentro del proyecto.

### Nombre sugerido

- `Agente de Documentacion Tecnica`

### Como nombrar o invocar este agente

Seleccionar `Agente de Documentacion Tecnica` en el selector de agentes de Copilot.

Antes de enviar cada prompt, confirmar que ese agente sigue siendo el agente activo.

### Paso a paso de creacion

1. Crear la carpeta `.github/agents` si todavia no existe.
2. Crear un archivo nuevo llamado `agente-documentacion-tecnica.agent.md`.
3. Abrir ese archivo en el editor.
4. Pegar este contenido base exacto en el archivo:

```md
# Agente de Documentacion Tecnica

Use this agent when the request is about documenting code, explaining observable behavior, listing inputs and outputs, and making technical documentation precise without inventing business rules.

## Constraints
- No inventar reglas de negocio.
- No atribuir comportamiento que no este visible en el codigo.
- Si algo no esta claro, debes decirlo explicitamente.
- Redactar para un equipo tecnico, no para marketing.

## Approach
1. Leer el codigo completo antes de documentar.
2. Explicar solo comportamiento observable.
3. Separar proposito, entradas, salidas, supuestos y limites.
4. Revisar que la documentacion pueda verificarse contra el codigo.

## Output
Entregar siempre:
- proposito del modulo;
- flujo principal;
- funciones clave;
- entradas y salidas observables;
- supuestos;
- limites o ambiguedades.
```

5. Guardar el archivo.
6. Volver a GitHub Copilot Chat y comprobar si el agente aparece en el selector.
7. Si no aparece de inmediato, cerrar y volver a abrir el chat de Copilot.

En este laboratorio no hace falta usar `Configure tool...` para habilitar `runSubagent`.

### Descripcion sugerida

- Lee codigo y produce documentacion tecnica precisa, breve y trazable, distinguiendo hechos observables de supuestos o limites.

### Instrucciones base del agente

Copiar y pegar este bloque en la configuracion del agente:

```text
## Constraints
- No inventar reglas de negocio.
- No atribuir comportamiento que no este visible en el codigo.
- Si algo no esta claro, debes decirlo explicitamente.
- Redactar para un equipo tecnico, no para marketing.

## Approach
1. Leer el codigo completo antes de documentar.
2. Explicar solo comportamiento observable.
3. Separar proposito, entradas, salidas, supuestos y limites.
4. Revisar que la documentacion pueda verificarse contra el codigo.

## Output
Entregar siempre:
- proposito del modulo;
- flujo principal;
- funciones clave;
- entradas y salidas observables;
- supuestos;
- limites o ambiguedades.
```

## Parte 3. Primera ejecucion del agente

Abrir `reconcile_transactions.py` y enviar este prompt con `Agente de Documentacion Tecnica` activo:

```text
Documenta este modulo para un equipo tecnico.

Necesito:
1. Proposito del modulo.
2. Flujo principal.
3. Funciones mas importantes y que hace cada una.
4. Entradas y salidas observables.
5. Supuestos y limites visibles.

No inventes reglas que no se vean en el codigo.
```

## Parte 4. Pedir una version mas util para equipo tecnico

Si la respuesta queda muy general, pedir una segunda version, manteniendo activo `Agente de Documentacion Tecnica`:

```text
Hazlo mas util para un desarrollador que recibe este archivo por primera vez.

Quiero:
1. Resumen tecnico en maximo 8 lineas.
2. Tabla o lista de funciones clave.
3. Riesgos o ambiguedades visibles.
4. Que deberia revisar primero una persona antes de modificar este modulo.
```

## Parte 5. Validar la documentacion contra el codigo

Revisar manualmente estos puntos:

1. Que las funciones mencionadas existan de verdad.
2. Que la descripcion de entradas y salidas coincida con el codigo.
3. Que no se atribuyan reglas de negocio no visibles.
4. Que las ambiguedades esten explicitadas cuando corresponde.

Si el agente invento algo, pedir correccion inmediata, manteniendo activo `Agente de Documentacion Tecnica`:

```text
Corrige la documentacion.

Estas partes no tienen respaldo claro en el codigo:
[copiar aqui la frase o punto dudoso]

Reescribe solo lo necesario y marca la ambiguedad si sigue existiendo.
```

## Parte 6. Generar una version final corta

Pedir al agente una salida final de cierre con `Agente de Documentacion Tecnica` activo:

```text
Entrega una version final corta con esta estructura:
1. Proposito.
2. Flujo principal.
3. Funciones clave.
4. Supuestos.
5. Limites o dudas abiertas.
```

## Parte 7. Como probar que el trabajo quedo bien

El laboratorio queda bien si se cumple todo esto:

1. La documentacion coincide con el codigo real.
2. No aparecen reglas inventadas.
3. El modulo queda entendible para otro desarrollador.
4. Los limites y ambiguedades quedan visibles.
5. El alumno puede defender que partes acepto y que partes corrigio.

## Entregable final

Cada alumno o pareja debe dejar:

- nombre del agente creado;
- version final de la documentacion;
- una lista corta de correcciones hechas a la primera respuesta;
- una nota breve con:
  - que parte del modulo quedo mas clara;
  - que duda tecnica sigue abierta.

## Extension opcional

Si el grupo avanza rapido, pedir una salida adicional:

```text
Genera una mini guia de mantenimiento para este modulo.

Debe incluir:
1. Que funcion revisar primero si falla la conciliacion.
2. Que datos o archivos afectan mas el resultado.
3. Que cambio pequeno seria riesgoso tocar sin pruebas.
```
