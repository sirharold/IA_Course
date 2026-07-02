# Guia de ejercicios - Clase 3

## Objetivo de la clase

Usar GitHub Copilot y Copilot Chat para comprender, diagnosticar y mejorar un sistema existente con criterio tecnico.

El foco no es crear software nuevo. El foco es:

- leer codigo heredado;
- reconstruir el flujo;
- analizar logs y errores;
- detectar riesgos y deuda tecnica;
- producir artefactos visuales utiles;
- proponer mejoras pequenas;
- derivar pruebas desde hallazgos reales.

## Carpeta de trabajo

Trabaja sobre:

- `reconciliation_legacy_service`

## Archivos principales

- `main.py`
- `reconciliation/service.py`
- `reconciliation/loaders.py`
- `reconciliation/matcher.py`
- `reconciliation/reporting.py`
- `reconciliation/utils.py`
- `data/core_transactions.csv`
- `data/gateway_transactions.csv`
- `data/gateway_transactions_dirty.csv`
- `logs/reconciliation_error.log`
- `logs/reconciliation_warning.log`
- `docs/reconciliation_rules.md`
- `tests/test_smoke.py`

## Herramientas gratuitas sugeridas

- Visual Studio Code
- GitHub Copilot y Copilot Chat
- Mermaid en archivos Markdown
- Vista previa Markdown de VS Code
- SQLite local con `sqlite3`

## Regla general

No aceptes respuestas de IA si no puedes respaldarlas con:

- un archivo;
- una funcion;
- un dato;
- un log;
- o un comportamiento observable.

## Preparacion

1. Abre la carpeta `reconciliation_legacy_service` en Visual Studio Code.
2. Revisa rapidamente la estructura de archivos.
3. Si quieres validar el comportamiento base, ejecuta:

```bash
python3 main.py
```

4. Observa el resultado general antes de empezar a preguntar a Copilot.
5. Abre tambien la carpeta `plantillas-mermaid`.
6. Revisa `.github/copilot-instructions.md` dentro del repo de ejercicio.

## Artefactos utiles para el dia a dia

Dentro del repo tambien tienes plantillas reutilizables:

- `.github/copilot-instructions.md`
- `docs/incident-investigation-template.md`
- `docs/change-plan-template.md`

La idea es que los alumnos no solo practiquen, sino que se lleven formatos que despues puedan copiar a sus proyectos reales.

## Prompt base sugerido

```text
Actua como analista tecnico senior.
Analiza el archivo o log seleccionado y responde en este orden:
1. Que hace o que muestra.
2. Flujo, entradas, salidas y dependencias visibles.
3. Riesgos tecnicos o dudas relevantes.
4. Evidencia concreta que respalda cada conclusion.
5. Pruebas iniciales sugeridas.
No inventes reglas de negocio, librerias ni archivos no visibles.
Si falta contexto, indicalo explicitamente.
```

## Prompt visual sugerido

```text
Genera un diagrama Mermaid simple y correcto a partir del codigo o log analizado.
No inventes componentes no visibles.
Si hay incertidumbre, usa etiquetas como "posible" o agregala fuera del diagrama.
Ademas, explica en 3 puntos que parte del diagrama esta respaldada por evidencia directa.
```

## Ejercicio 1. Mapa del flujo principal

### Objetivo

Entender rapidamente como funciona el servicio.

### Paso a paso

1. Abre `main.py`.
2. Abre `reconciliation/service.py`.
3. Pide a Copilot una explicacion del flujo principal.
4. Verifica manualmente:
   - donde entra el proceso;
   - que archivos participan;
   - que datos carga;
   - que salida produce.
5. Resume el flujo en 4 o 5 pasos.

### Entregable

- Un mapa breve del flujo.
- Lista de archivos principales involucrados.

## Ejercicio 2. Flujograma visual en Mermaid

### Objetivo

Convertir la explicacion del flujo en un entregable visual.

### Paso a paso

1. Usa lo aprendido en el ejercicio 1.
2. Abre `plantillas-mermaid/flujo-base.md`.
3. Pide a Copilot un flujograma Mermaid del proceso completo.
4. Pega el resultado en una copia de esa plantilla.
5. Revisa si el diagrama representa:
   - carga de datos;
   - matching;
   - resumen final;
   - posible error en carga.
6. Ajusta manualmente lo que no coincida con el codigo.

### Entregable

- Un diagrama Mermaid del flujo principal.

## Ejercicio 3. Dependencias y arquitectura implicita

### Objetivo

Detectar dependencias importantes que no siempre son obvias a primera vista.

### Paso a paso

1. Revisa `reconciliation/loaders.py`, `reconciliation/matcher.py` y `reconciliation/utils.py`.
2. Pide a Copilot que identifique:
   - dependencias entre modulos;
   - supuestos de formato de datos;
   - puntos de acoplamiento fuerte.
3. Contrasta la respuesta con el codigo real.
4. Marca al menos dos dependencias que podrian provocar errores o resultados incorrectos.

### Entregable

- Dos a cuatro dependencias importantes.
- Dos riesgos asociados a esas dependencias.

## Ejercicio 4. Diagrama de dependencias

### Objetivo

Hacer visible la arquitectura implicita del servicio.

### Paso a paso

1. Abre `plantillas-mermaid/dependencias-base.md`.
2. Pide a Copilot un diagrama Mermaid de dependencias entre:
   - `main.py`
   - `service.py`
   - `loaders.py`
   - `matcher.py`
   - `utils.py`
   - `reporting.py`
   - `data/*.csv`
   - `logs/*.log`
3. Revisa si las flechas tienen sentido.
4. Marca en el diagrama:
   - dependencia de codigo;
   - dependencia de datos;
   - dependencia operativa.

### Entregable

- Un diagrama de dependencias anotado.

## Ejercicio 5. Hechos versus inferencias

### Objetivo

Evitar aceptar explicaciones plausibles que no estan demostradas.

### Paso a paso

1. Abre `reconciliation/matcher.py`.
2. Abre `docs/reconciliation_rules.md`.
3. Pide a Copilot que compare documentacion y codigo.
4. Separa el resultado en:
   - hechos visibles en el codigo;
   - inferencias razonables;
   - contradicciones o dudas abiertas.
5. Marca al menos una regla del documento que no coincida del todo con el comportamiento real.

### Entregable

- Una tabla simple con hechos, inferencias y contradicciones.

## Ejercicio 6. Triage de incidente

### Objetivo

Interpretar un error con evidencia, no con intuicion.

### Paso a paso

1. Abre `logs/reconciliation_error.log`.
2. Pide a Copilot:
   - que error se observa;
   - en que parte del flujo ocurre;
   - hipotesis principal;
   - hipotesis alternativa;
   - que evidencia favorece cada una;
   - que informacion falta para confirmar.
3. Revisa `reconciliation/utils.py` y `reconciliation/loaders.py`.
4. Decide cual hipotesis esta mejor respaldada.

### Entregable

- Resumen del incidente.
- Hipotesis principal.
- Hipotesis alternativa.
- Evidencia concreta usada para sostenerlas.

## Ejercicio 7. Secuencia visual del incidente

### Objetivo

Representar el incidente como una secuencia tecnica simple.

### Paso a paso

1. Abre `plantillas-mermaid/incidente-base.md`.
2. Usa `logs/reconciliation_error.log`, `loaders.py` y `utils.py`.
3. Pide a Copilot un diagrama Mermaid tipo `sequenceDiagram`.
4. Verifica que el diagrama muestre:
   - lectura de archivo;
   - parseo de fila;
   - falla en conversion;
   - propagacion del error.
5. Corrige cualquier paso inventado.

### Entregable

- Un diagrama de secuencia del incidente.

## Ejercicio 8. Incidente silencioso

### Objetivo

Analizar problemas que no rompen la ejecucion, pero si afectan la confiabilidad del resultado.

### Paso a paso

1. Abre `logs/reconciliation_warning.log`.
2. Revisa `data/gateway_transactions.csv`.
3. Pide a Copilot que explique:
   - que warnings aparecen;
   - si el sistema termina igual;
   - por que el resultado sigue siendo riesgoso.
4. Verifica en `matcher.py` y `reporting.py` si el warning realmente tiene impacto tecnico.

### Entregable

- Explicacion del warning.
- Riesgo tecnico asociado.

## Ejercicio 9. Riesgos de datos

### Objetivo

Cruzar codigo y datos reales para detectar problemas de calidad de entrada.

### Paso a paso

1. Abre `data/gateway_transactions_dirty.csv`.
2. Revisa `reconciliation/utils.py`.
3. Pide a Copilot que identifique:
   - filas riesgosas;
   - formatos problematicos;
   - que valores pueden romper el parseo;
   - que valores pueden provocar discrepancias falsas.
4. Conecta cada observacion con una funcion concreta del codigo.

### Entregable

- Tres observaciones sobre calidad de datos.
- Dos riesgos concretos de parseo o matching.

## Ejercicio 10. Mapa de evidencia

### Objetivo

Dejar trazabilidad clara entre hallazgo y evidencia.

### Paso a paso

1. Toma dos hallazgos de los ejercicios anteriores.
2. Crea una tabla con estas columnas:
   - hallazgo;
   - evidencia;
   - riesgo;
   - incertidumbre;
   - prueba sugerida.
3. Pide a Copilot un borrador inicial.
4. Corrigelo para que cada fila cite un archivo o log real.

### Entregable

- Un mapa de evidencia con al menos dos filas completas.

## Ejercicio 11. SQL de investigacion

### Objetivo

Llevar el analisis a una tarea muy parecida al dia a dia: consultar datos operativos para validar una hipotesis.

### Paso a paso

1. Ejecuta:

```bash
python3 scripts/build_reconciliation_db.py
sqlite3 artifacts/reconciliation.db
```

2. Abre `sql/investigation_queries.sql`.
3. Pide a Copilot que explique que valida cada query.
4. Ejecuta al menos dos consultas.
5. Responde:
   - que problema de datos queda demostrado;
   - que problema sigue siendo solo una hipotesis;
   - que query agregarias.

### Entregable

- Dos consultas ejecutadas.
- Hallazgo confirmado por SQL.
- Una query nueva propuesta por el alumno.

## Ejercicio 12. Script de correccion de datos

### Objetivo

Practicar un caso realista de soporte: proponer un cambio pequeño sobre datos con validacion previa.

### Paso a paso

1. Abre `sql/fix_scripts.sql`.
2. Pide a Copilot que:
   - explique el impacto de cada `UPDATE`;
   - proponga primero una consulta de preview;
   - indique riesgos de aplicar el script sin validacion.
3. Ejecuta primero solo los `SELECT`.
4. Decide si aplicarias o no uno de los cambios.
5. Si lo aplicas, vuelve a ejecutar la consulta de validacion.

### Entregable

- Preview query.
- Decision razonada de aplicar o no aplicar el cambio.
- Riesgo principal del script.

## Ejercicio 13. Mini tarea ETL

### Objetivo

Practicar una tarea muy cercana al trabajo real: extraer datos sucios, transformarlos con reglas visibles y cargar una salida limpia o un archivo de rechazos.

### Paso a paso

1. Abre `etl/run_gateway_etl.py`.
2. Pide a Copilot que explique:
   - que parte es extract;
   - que parte es transform;
   - que parte es load;
   - que reglas de limpieza aplica;
   - que limitaciones visibles tiene.
3. Ejecuta:

```bash
python3 etl/run_gateway_etl.py
```

4. Revisa los archivos generados:
   - `artifacts/gateway_transactions_clean.csv`
   - `artifacts/gateway_rejects.csv`
5. Pide a Copilot una mejora pequena sobre el ETL. Ejemplos:
   - nueva regla de validacion;
   - mejor razon de rechazo;
   - separacion mas clara de transformaciones.
6. Decide si la mejora conviene para esta etapa o si ya se pasa de alcance.

### Entregable

- Explicacion corta del ETL.
- Una regla de transformacion identificada.
- Un problema o limitacion del flujo actual.
- Una mejora pequena propuesta.

## Ejercicio 14. Documentacion tecnica controlada

### Objetivo

Generar documentacion util sin alucinar comportamiento.

### Paso a paso

1. Elige uno de estos archivos:
   - `reconciliation/matcher.py`
   - `reconciliation/reporting.py`
   - `reconciliation/service.py`
2. Pide a Copilot una mini documentacion tecnica.
3. Revisa si inventa reglas, tolerancias o validaciones no visibles.
4. Corrige el resultado separando:
   - hechos;
   - inferencias;
   - supuestos pendientes.

### Entregable

- Version inicial generada por IA.
- Version corregida por el alumno.

## Ejercicio 15. Mejora pequena y defendible

### Objetivo

Transformar el analisis en una mejora concreta de bajo riesgo.

### Paso a paso

1. Identifica un problema visible. Ejemplos:
   - conversion fragil de montos;
   - validacion insuficiente;
   - mezcla de responsabilidades;
   - mensajes de error pobres.
2. Pide a Copilot una mejora pequena.
3. Evalua si la propuesta:
   - responde al problema real;
   - no reescribe demasiado;
   - es verificable;
   - no inventa arquitectura nueva.
4. Decide si la aceptarias, la ajustarias o la rechazarias.

### Entregable

- Problema elegido.
- Mejora propuesta.
- Decision: aceptar, ajustar o rechazar.

## Ejercicio 16. Pruebas desde riesgos

### Objetivo

Diseñar pruebas utiles a partir de incidentes y hallazgos, no solo desde la firma de una funcion.

### Paso a paso

1. Revisa `tests/test_smoke.py`.
2. Toma uno de los riesgos detectados en ejercicios anteriores.
3. Pide a Copilot una propuesta de pruebas separada en:
   - casos base;
   - edge cases;
   - casos de error;
   - supuestos pendientes de validar.
4. Verifica si las pruebas realmente cubren el riesgo observado.
5. Marca cual prueba implementarias primero y por que.

### Entregable

- Lista de pruebas sugeridas.
- Riesgo que cubre cada una.
- Prueba prioritaria.

## Ejercicio 17. Workflow por roles

### Objetivo

Entender como dividir una investigacion tecnica en subtareas.

### Paso a paso

1. Toma el incidente de `reconciliation_error.log`.
2. Divide el trabajo en tres roles:
   - lector de logs;
   - lector de codigo;
   - diseniador de pruebas.
3. Define para cada rol:
   - entrada;
   - salida;
   - evidencia obligatoria;
   - decisiones que requieren validacion humana.
4. Redacta un handoff breve entre roles.

### Entregable

- Flujo de 3 roles.
- Entrada y salida de cada uno.
- Al menos una decision que no debe delegarse por completo.

## Cierre sugerido

Al terminar, cada alumno o pareja deberia poder responder:

1. Como funciona el flujo principal.
2. Que dependencia es la mas fragil.
3. Que muestra realmente el incidente.
4. Que parte de la documentacion no coincide con el codigo.
5. Que mejora pequena tendria mejor relacion impacto-riesgo.
6. Que prueba conviene escribir primero.
7. Que diagrama ayudaria mas a otro desarrollador a entender el sistema.

## Recomendacion docente

Si el tiempo es limitado, prioriza estos ejercicios:

1. `Mapa del flujo principal`
2. `Flujograma visual en Mermaid`
3. `Triage de incidente`
4. `Diagrama de dependencias`
5. `SQL de investigacion`
6. `Mini tarea ETL`
7. `Pruebas desde riesgos`

Si el grupo avanza rapido, agrega:

8. `Secuencia visual del incidente`
9. `Mapa de evidencia`
10. `Script de correccion de datos`
11. `Workflow por roles`
