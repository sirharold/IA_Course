# Ejercicio avanzado - Clase 4

## Ejercicio. Agente IA para construir un paquete unico de hallazgos

### Objetivo

Usar Copilot en agent mode para crear un script nuevo que ejecute o lea las salidas existentes del laboratorio y genere un unico archivo `incident_packet.json` con los hallazgos mas importantes del caso.

### Resultado esperado

El alumno debe terminar con un script nuevo, por ejemplo:

- `build_incident_packet.py`

Y con una salida nueva, por ejemplo:

- `output/incident_packet.json`

Ese archivo debe reunir en una sola estructura:

- resumen de conciliacion;
- incidentes extraidos;
- contradicciones de contrato;
- anomalias priorizadas.

## Archivos que deben usar

- `../technical_automation_lab/reconcile_transactions.py`
- `../technical_automation_lab/extract_incidents.py`
- `../technical_automation_lab/derive_contract_candidates.py`
- `../technical_automation_lab/anomaly_report.py`
- `../technical_automation_lab/output/reconciliation_report.json`
- `../technical_automation_lab/output/incidents_structured.json`
- `../technical_automation_lab/output/contract_candidates.json`
- `../technical_automation_lab/output/anomaly_report.md`

## Paso 1

Ejecutar primero los scripts base para tener las salidas actualizadas:

```bash
python3 ../technical_automation_lab/reconcile_transactions.py
python3 ../technical_automation_lab/extract_incidents.py
python3 ../technical_automation_lab/derive_contract_candidates.py
python3 ../technical_automation_lab/anomaly_report.py
```

## Paso 2

Abrir las cuatro salidas en `output/` y decidir que informacion minima deberia vivir en `incident_packet.json`.

Como minimo:

- `reconciliation_summary`
- `top_incidents`
- `contract_risks`
- `priority_findings`

## Paso 3

Abrir Copilot Chat y cambiar a `agent mode`.

## Paso 4

Pedirle al agente que cree un script nuevo.

Prompt sugerido:

```text
Quiero que crees un script nuevo llamado build_incident_packet.py.

Tarea:
1. Leer las salidas ya generadas en output/.
2. Construir un archivo output/incident_packet.json.
3. Incluir en ese archivo:
   - resumen de conciliacion,
   - incidentes extraidos,
   - riesgos de contrato,
   - hallazgos priorizados.
4. Mantener el cambio pequeno y verificable.

Restricciones:
- No reescribas los scripts existentes.
- No agregues dependencias nuevas.
- Usa solo los archivos ya disponibles en esta clase.
- Si algun dato no esta claro, dejalo fuera en vez de inventarlo.
```

## Paso 5

Revisar el plan del agente antes de aceptar cambios.

Confirmar que:

- crea un archivo nuevo;
- no modifica mas de lo necesario;
- no inventa datos;
- trabaja sobre las salidas reales del laboratorio.

## Paso 6

Aprobar el cambio del agente.

## Paso 7

Ejecutar el script nuevo:

```bash
python3 build_incident_packet.py
```

## Paso 8

Abrir `output/incident_packet.json` y validar:

- que el archivo se creo;
- que contiene informacion tomada de varias salidas;
- que la estructura es legible;
- que no mezcla texto ornamental con datos utiles.

## Paso 9

Pedirle a Copilot una segunda mejora pequena sobre el script.

Ejemplos validos:

- ordenar mejor la prioridad;
- limitar el numero de hallazgos;
- agregar una seccion `recommended_next_step`;
- dejar mas clara la referencia de origen de cada hallazgo.

Prompt sugerido:

```text
Revisa build_incident_packet.py y el JSON generado.
Haz una sola mejora pequena para que la salida sea mas util para revision tecnica.
No reestructures todo el archivo.
```

## Paso 10

Volver a ejecutar el script y comparar el antes y despues.

## Entregable

- `build_incident_packet.py`
- `output/incident_packet.json`
- nota breve de 5 lineas con:
  - que creo el agente;
  - que parte revisaron manualmente;
  - que mejora aceptaron;
  - que dato seguiria faltando.
