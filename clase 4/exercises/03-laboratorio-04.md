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

Usar como base los archivos de `../technical_automation_lab/`:

- `reconcile_transactions.py`
- `extract_incidents.py`
- `derive_contract_candidates.py`
- `anomaly_report.py`
- instrucciones y prompt files dentro de `.github/`

## Paso 1. Elegir el caso

Seleccionar uno de los cuatro patrones de trabajo.

Antes de tocar codigo, anotar en 3 a 5 lineas:

- que problema tecnico resuelve;
- que artefactos entran;
- que salida esperan;
- por que este caso no es solo una transformacion trivial.

## Paso 2. Abrir artefactos y leer el contexto

Abrir en Visual Studio Code:

- el script base relacionado con el caso;
- los archivos de entrada;
- si aplica, el prompt file asociado en `../technical_automation_lab/.github/prompts/`.

Objetivo de este paso:

- entender rapidamente el flujo actual;
- detectar donde hay reglas implicitas;
- decidir donde conviene intervenir.

## Paso 3. Delimitar que parte es determinista y cual requiere IA

Escribir una nota breve con dos columnas:

- parte determinista;
- parte asistida por IA.

Ejemplos:

- determinista:
  - leer archivos;
  - contar registros;
  - serializar JSON;
  - agrupar por tipo.
- asistida por IA:
  - criticar heuristicas de matching;
  - detectar contradicciones de contrato;
  - proponer validaciones faltantes;
  - mejorar estructura de salida para decision tecnica.

## Paso 4. Pedir a Copilot una lectura tecnica del flujo actual

Usar un prompt como este:

```text
Revisa este flujo tecnico.
Necesito que:
1. Expliques que hace hoy.
2. Detectes supuestos fragiles o zonas ambiguas.
3. Propongas una mejora pequena y verificable.
4. Sugieras validaciones sobre entrada, transformacion y salida.
No inventes reglas de negocio.
Separa hechos observables de inferencias.
```

El objetivo no es aceptar la primera respuesta, sino revisar si:

- entendio bien el flujo;
- detecto riesgos reales;
- propuso algo acotado;
- no sobrecomplico el caso.

## Paso 5. Elegir una sola mejora concreta

Seleccionar una mejora pequena, por ejemplo:

- endurecer una normalizacion;
- enriquecer la salida con mas contexto;
- agregar una validacion nueva;
- separar anomalia confirmada de anomalia sospechosa;
- hacer visible un campo dudoso o faltante.

No elegir dos o tres mejoras a la vez.

## Paso 6. Pedir a Copilot ayuda para implementar esa mejora

Usar un prompt como este:

```text
Ayudame a hacer una mejora pequena sobre este script.
La mejora es:
[describir la mejora].

Necesito:
1. Un cambio acotado y verificable.
2. Que no reescriba todo el archivo.
3. Que deje visible la validacion o heuristica usada.
4. Que no agregue dependencias innecesarias.
```

Revisar el cambio antes de aceptarlo.

## Paso 7. Ejecutar el script

Correr el script relacionado con el caso.

Ejemplos:

```bash
python3 ../technical_automation_lab/reconcile_transactions.py
python3 ../technical_automation_lab/extract_incidents.py
python3 ../technical_automation_lab/derive_contract_candidates.py
python3 ../technical_automation_lab/anomaly_report.py
```

Verificar en terminal:

- que el script corre;
- que no rompe el flujo base;
- que genera la salida esperada.

## Paso 8. Abrir la salida y validarla

Abrir el archivo generado y revisar al menos estas tres cosas:

1. La salida responde al objetivo original del caso.
2. Existe evidencia visible de la mejora realizada.
3. Hay al menos tres validaciones o controles entendibles.

Tipos de validacion aceptables:

- conteo de registros;
- campos obligatorios;
- anomalias por tipo;
- contradicciones detectadas;
- casos dudosos marcados;
- warnings o limites del proceso.

## Paso 9. Pedir a Copilot una critica de la salida

Usar un prompt como este:

```text
Revisa esta salida y este script final.
Necesito que identifiques:
1. Que partes son confiables.
2. Que partes siguen siendo ambiguas o fragiles.
3. Que validacion adicional agregarias si hubiera tiempo.
4. Que riesgo tecnico sigue abierto.
No propongas una reescritura grande.
```

No es obligatorio implementar una segunda mejora, pero si registrar lo que falto.

## Paso 10. Preparar el entregable final

Cada alumno o pareja debe dejar:

- script o ajuste concreto sobre el codigo base;
- salida estructurada;
- mini nota tecnica de maximo media pagina con:
  - problema que resolvio;
  - donde uso Copilot;
  - que mejora introdujo;
  - como valido el resultado;
  - que riesgo o incertidumbre quedo abierta.

## Resultado esperado

Al terminar el laboratorio deberia quedar claro:

- que el caso tenia valor tecnico real;
- que la IA no se uso para una tarea trivial;
- que la mejora fue acotada y defendible;
- que la salida sirve para revisar o decidir algo;
- que los limites del flujo quedaron explicitados.

## Pauta de revision docente

Observar si los alumnos:

- eligieron un problema con valor tecnico real;
- evitaron usar IA para tareas triviales;
- dejaron validaciones conectadas al riesgo del caso;
- produjeron una salida accionable;
- distinguieron entre automatizacion convincente y automatizacion confiable.
