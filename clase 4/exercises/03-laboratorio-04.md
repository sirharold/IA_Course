# Laboratorio 04 - Automatizacion tecnica avanzada

## Objetivo

Construir una automatizacion pequena pero tecnicamente defendible que procese artefactos heterogeneos, deje una salida estructurada y explicite validaciones, riesgos y limites del enfoque.

## Duracion sugerida

- 25 minutos para definir el caso y el flujo.
- 20 minutos para implementar o ajustar el script base.
- 15 minutos para validaciones y salida.
- 10 minutos para revision tecnica y cierre.

## Modalidad sugerida

- Individual o en parejas.
- Priorizar profundidad tecnica sobre cantidad de codigo.

## Regla base del laboratorio

No gana quien use mas IA ni quien escriba mas lineas. Gana quien resuelva mejor un problema donde la IA si aporta algo no trivial y quien deje mas claro como valida el resultado.

## Casos sugeridos

Elegir uno de estos patrones:

- conciliacion entre fuentes con nomenclaturas no alineadas;
- extraccion estructurada desde documento semiformateado;
- reconstruccion de contrato implicito desde codigo y payloads;
- reporte de anomalias combinando datos y logs.

## Artefactos sugeridos

Usar como base los archivos de `codigo/`:

- `reconcile_transactions.py`
- `extract_incidents.py`
- `derive_contract_candidates.py`
- `anomaly_report.py`
- instrucciones y prompt files dentro de `codigo/.github/`

## Parte 1 - Delimitacion del problema

### Tarea

Definir que se quiere automatizar y por que no basta una solucion mecanica trivial.

### El alumno debe dejar claro

- que entra;
- que sale;
- que parte es determinista;
- que parte requiere interpretacion o contexto;
- que riesgo tecnico quiere controlar.

## Parte 2 - Implementacion o mejora acotada

### Tarea

Tomar uno de los scripts base y hacer una mejora concreta o construir una variante sobre el mismo patron.

### Tipos de mejora validos

- endurecer matching o normalizacion;
- mejorar estructura de salida;
- incorporar una validacion nueva;
- hacer visible una incertidumbre que antes quedaba escondida;
- separar mejor evidencia y heuristica.

## Parte 3 - Validacion y salida

### Tarea

Producir una salida que sirva para revisar o decidir algo.

### La salida debe incluir

- resultado principal;
- al menos tres validaciones;
- supuestos relevantes;
- principal limitacion o riesgo abierto.

## Entregable esperado

- script o ajuste concreto sobre el codigo base;
- salida estructurada;
- mini nota tecnica con:
  - que problema resuelve;
  - donde aporta IA;
  - como se valido;
  - que sigue siendo incierto.

## Pauta de revision docente

Observar si los alumnos:

- eligieron un problema con valor tecnico real;
- evitaron usar IA para tareas triviales;
- dejaron validaciones conectadas al riesgo del caso;
- produjeron una salida accionable;
- distinguieron entre automatizacion convincente y automatizacion confiable.
