# Ejercicios - Clase 4

## Objetivo general

Construir automatizaciones tecnicas con valor real para un equipo avanzado, mezclando datos y desarrollo cuando haga falta, y usando IA solo donde agregue capacidad y no solo velocidad.

## Regla comun para todos los ejercicios

Antes de empezar, cada alumno o pareja debe dejar explicito:

- que problema tecnico esta resolviendo;
- que artefactos entran al flujo;
- que salida esperan producir;
- que parte del trabajo es determinista;
- que parte justifica usar Copilot.

## Regla comun para el uso de Copilot

No usar Copilot solo para que escriba codigo mas rapido. Usarlo para:

- detectar reglas fragiles;
- proponer validaciones;
- sintetizar contradicciones entre artefactos;
- hacer visible incertidumbre;
- refinar una salida para que sea mas util para decidir algo.

## Ejercicio 1. Conciliador con reglas no alineadas

### Objetivo

Cruzar dos fuentes que describen el mismo proceso, pero con diferencias de nombres, estados o referencias.

### Archivos sugeridos

- `../technical_automation_lab/reconcile_transactions.py`
- `../technical_automation_lab/data/core_transactions.csv`
- `../technical_automation_lab/data/gateway_transactions.csv`
- `../technical_automation_lab/.github/prompts/reconcile-anomalies.prompt.md`

### Lo que deben hacer

- Revisar primero las dos fuentes y detectar diferencias visibles en nombres, referencias y estados.
- Explicar rapidamente cual creen que es la logica actual de matching.
- Ajustar o extender el flujo de conciliacion para dejar mas clara una anomalia o reducir un falso positivo.
- Agregar al menos una validacion nueva sobre el resultado.
- Dejar una salida que permita responder:
  - que registros calzaron;
  - que registros no calzaron;
  - por que no calzaron o por que el matching es dudoso.

### Que se espera ver en pantalla

- Los dos CSV abiertos y comparados.
- El script de conciliacion abierto en el punto donde se hace matching o se clasifican anomalias.
- Una ejecucion del script con salida en terminal.
- El archivo `../technical_automation_lab/output/reconciliation_report.json` o una version mejorada de esa salida.

### Como conviene usar Copilot

- Pedirle primero una lectura tecnica de la logica actual.
- Luego pedirle que critique la logica:
  - que supuestos tiene;
  - donde podria fallar;
  - que validaciones faltan.
- Solo despues pedir una mejora acotada del codigo.

### Prompt sugerido

```text
Revisa este flujo de conciliacion entre dos fuentes.
Necesito que:
1. Expliques la logica actual de matching.
2. Identifiques supuestos fragiles o posibles falsos positivos.
3. Propongas una mejora pequena y verificable.
4. Sugieras validaciones minimas sobre la salida.
No inventes reglas de negocio que no esten en los datos o en el codigo.
Separa hechos observables de inferencias.
```

### Validaciones minimas esperadas

- Conteo de registros de entrada y salida.
- Deteccion explicita de registros presentes en una fuente y ausentes en la otra.
- Identificacion de al menos una anomalia discutible o ambigua.

### Entregable

- Script o mejora concreta.
- Reporte de anomalias.
- Tres validaciones minimas justificadas.
- Breve nota sobre donde Copilot si aporto valor.

## Ejercicio 2. Extraccion util desde documento imperfecto

### Objetivo

Transformar un documento exportado o texto semiestructurado en una salida util para otro proceso tecnico.

### Archivos sugeridos

- `../technical_automation_lab/extract_incidents.py`
- `../technical_automation_lab/docs/incident_report_export.txt`

### Lo que deben hacer

- Revisar el documento fuente y marcar que informacion es estructurada y cual es ambigua.
- Definir que campos vale la pena rescatar y por que.
- Mejorar la extraccion base o enriquecer la salida para reflejar mejor lo que se pudo capturar y lo que quedo dudoso.
- Agregar una forma de distinguir entre:
  - campo extraido con confianza;
  - campo faltante;
  - informacion que requiere revision manual.

### Que se espera ver en pantalla

- El documento fuente abierto.
- El parser o extractor abierto.
- Una ejecucion del script.
- El archivo `../technical_automation_lab/output/incidents_structured.json` o una version extendida de esa salida.

### Como conviene usar Copilot

- Pedirle primero una critica del parser actual.
- Luego pedirle que proponga una mejora puntual:
  - validacion;
  - clasificacion de confianza;
  - captura de notas no parseadas;
  - manejo de campos faltantes.

### Prompt sugerido

```text
Revisa este extractor de incidentes desde texto semiestructurado.
Necesito que:
1. Expliques que casos cubre bien y cuales no.
2. Identifiques que campos pueden quedar ambiguos o perderse.
3. Propongas una mejora pequena para hacer la salida mas util y mas honesta respecto de sus limites.
4. Sugieras validaciones sobre la calidad de extraccion.
No sobreingenierices la solucion.
```

### Validaciones minimas esperadas

- Confirmar cantidad de bloques procesados.
- Verificar presencia de campos criticos definidos por el alumno.
- Hacer visible al menos un caso dudoso o no resuelto totalmente.

### Entregable

- Salida estructurada.
- Campos con confianza alta y campos dudosos.
- Riesgos de calidad del resultado.
- Breve nota sobre que parte resolverian sin IA y que parte no.

## Ejercicio 3. Contrato implicito de integracion

### Objetivo

Reconstruir expectativas de entrada y detectar incompatibilidades entre codigo y payloads.

### Archivos sugeridos

- `../technical_automation_lab/contracts/legacy_order_service.py`
- `../technical_automation_lab/contracts/partner_payload_samples.json`
- `../technical_automation_lab/derive_contract_candidates.py`
- `../technical_automation_lab/.github/prompts/derive-contract.prompt.md`

### Lo que deben hacer

- Revisar primero el codigo consumidor para entender que espera.
- Revisar luego los payloads de muestra para detectar contradicciones visibles.
- Ejecutar o extender el comparador de contrato.
- Proponer una salida que diferencie:
  - campos esperados por codigo;
  - campos observados en muestras;
  - contradicciones reales;
  - equivalencias semanticas plausibles pero no confirmadas.
- Agregar validaciones previas al procesamiento del payload.

### Que se espera ver en pantalla

- El codigo del consumidor abierto.
- Las muestras JSON abiertas.
- La salida `../technical_automation_lab/output/contract_candidates.json` o una version mejorada.
- Un resumen visual de contradicciones o huecos.

### Como conviene usar Copilot

- Pedirle primero una lectura del contrato implicito.
- Despues pedirle que clasifique incompatibilidades por severidad.
- Luego pedirle una mejora pequena del comparador o de la salida.

### Prompt sugerido

```text
Ayudame a derivar un contrato implicito comparando este codigo consumidor y estas muestras reales.
Necesito:
1. Campos que el codigo parece requerir.
2. Campos que llegan con otro nombre o forma.
3. Riesgos de integracion que deberian bloquear procesamiento.
4. Validaciones minimas antes de aceptar el payload.
No inventes reglas ni resuelvas contradicciones silenciosamente.
```

### Validaciones minimas esperadas

- Detectar al menos una contradiccion de nombre o estructura.
- Distinguir entre incompatibilidad segura y equivalencia probable.
- Proponer al menos dos checks previos al procesamiento.

### Entregable

- Lista de contradicciones o huecos.
- Contrato candidato resumido.
- Validaciones sugeridas.
- Breve nota sobre donde Copilot redujo el costo de analisis.

## Ejercicio 4. Reporte tecnico de anomalias

### Objetivo

Consolidar datos y logs para producir una salida que sirva para revisar un incidente o priorizar una mejora.

### Archivos sugeridos

- `../technical_automation_lab/anomaly_report.py`
- `../technical_automation_lab/data/runtime_logs.ndjson`
- `../technical_automation_lab/output/reconciliation_report.json`

### Lo que deben hacer

- Revisar las anomalias de datos por separado de los logs.
- Explicar por que ambas fuentes, vistas por separado, no alcanzan para decidir bien.
- Ajustar o extender el reporte para que:
  - agrupe anomalias;
  - destaque eventos de log relevantes;
  - sugiera que revisar primero.
- Introducir un criterio simple de priorizacion.

### Que se espera ver en pantalla

- El reporte de conciliacion abierto.
- El archivo de logs abierto.
- El script del reporte abierto.
- El archivo `../technical_automation_lab/output/anomaly_report.md` o una version mejorada.

### Como conviene usar Copilot

- Pedirle primero una propuesta de estructura de reporte.
- Luego pedirle que critique si la priorizacion es suficiente o superficial.
- Finalmente pedirle una mejora acotada para que la salida sea mas accionable.

### Prompt sugerido

```text
Revisa estas anomalias y estos logs.
Necesito un reporte tecnico breve que:
1. Consolide hallazgos relevantes.
2. Distinga entre warning, error y anomalias repetidas.
3. Sugiera que revisar primero y por que.
4. Haga explicitos los limites de la informacion disponible.
No generes texto ornamental. Prioriza una salida accionable.
```

### Validaciones minimas esperadas

- Conteo de anomalias por tipo.
- Identificacion de eventos de log relevantes.
- Priorizacion defendible de al menos dos hallazgos.

### Entregable

- Reporte estructurado.
- Criterio de priorizacion usado.
- Siguiente accion recomendada.
- Breve nota sobre que parte del analisis seguiria siendo humana.
