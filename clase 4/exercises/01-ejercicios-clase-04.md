# Ejercicios - Clase 4

## Objetivo general

Construir automatizaciones tecnicas con valor real para un equipo avanzado, mezclando datos y desarrollo cuando haga falta, y usando IA solo donde agregue capacidad y no solo velocidad.

## Reglas para los alumnos

- No elegir ejercicios que se resuelvan solo con transformacion mecanica trivial.
- Declarar explicitamente que parte del flujo es determinista y cual requiere interpretacion.
- No aceptar sugerencias de Copilot sin revisar validaciones, supuestos y riesgos.
- Priorizar salidas accionables y trazables sobre soluciones vistosas.

## Ejercicio 1. Conciliador con reglas no alineadas

### Objetivo

Cruzar dos fuentes que describen el mismo proceso, pero con diferencias de nombres, estados o referencias.

### Tarea

- Ajustar o extender el flujo de conciliacion.
- Identificar anomalias reales y posibles falsos positivos.
- Producir una salida explicativa y validable.

### Entregable

- Script o mejora concreta.
- Reporte de anomalias.
- Tres validaciones minimas justificadas.

## Ejercicio 2. Extraccion util desde documento imperfecto

### Objetivo

Transformar un documento exportado o texto semiestructurado en una salida util para otro proceso tecnico.

### Tarea

- Definir que campos rescatar.
- Mejorar la extraccion base.
- Marcar que parte queda incierta o requiere revision manual.

### Entregable

- Salida estructurada.
- Campos con confianza alta y campos dudosos.
- Riesgos de calidad del resultado.

## Ejercicio 3. Contrato implicito de integracion

### Objetivo

Reconstruir expectativas de entrada y detectar incompatibilidades entre codigo y payloads.

### Tarea

- Comparar lo que pide el codigo con lo que traen las muestras.
- Identificar campos obligatorios ausentes, nombres alternativos o tipos ambiguos.
- Proponer validaciones de contrato previas al procesamiento.

### Entregable

- Lista de contradicciones o huecos.
- Contrato candidato resumido.
- Validaciones sugeridas.

## Ejercicio 4. Reporte tecnico de anomalias

### Objetivo

Consolidar datos y logs para producir una salida que sirva para revisar un incidente o priorizar una mejora.

### Tarea

- Integrar hallazgos desde mas de una fuente.
- Clasificar anomalias por severidad o urgencia.
- Redactar una salida breve que habilite accion.

### Entregable

- Reporte estructurado.
- Criterio de priorizacion usado.
- Siguiente accion recomendada.
