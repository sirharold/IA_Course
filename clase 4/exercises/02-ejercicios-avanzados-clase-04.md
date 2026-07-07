# Ejercicios avanzados - Clase 4

## Objetivo general

Llevar las automatizaciones base a un nivel donde aparezcan decisiones de ingenieria mas serias: ambiguedad controlada, validacion cruzada, trazabilidad y reutilizacion del flujo.

## Ejercicio avanzado 1. Motor de matching explicable

### Objetivo

Evolucionar la conciliacion para que no solo haga matching, sino que explique por que considero compatibles o incompatibles dos registros.

### Descripcion breve

Agregar scoring o criterios explicitos de compatibilidad, separar evidencia de heuristica y dejar salida apta para auditoria tecnica.

## Ejercicio avanzado 2. Extraccion con clasificacion de confianza

### Objetivo

Hacer que la salida del extractor distinga entre campos confiables, ambiguos y faltantes.

### Descripcion breve

Introducir una capa de evaluacion de calidad de extraccion para decidir que puede seguir automatico y que debe pasar a revision humana.

## Ejercicio avanzado 3. Contrato candidato con equivalencias semanticas

### Objetivo

Detectar que ciertos campos no coinciden en nombre, pero probablemente si en significado tecnico.

### Descripcion breve

Construir una salida que proponga equivalencias semanticas, contradicciones y riesgos de integracion sin esconder la incertidumbre.

## Ejercicio avanzado 4. Reporte de anomalias con recomendacion operativa

### Objetivo

Pasar de un listado de problemas a una priorizacion breve con siguiente accion sugerida.

### Descripcion breve

Cruzar anomalias, logs y contexto tecnico para decidir que revisar primero, que bloquear y que dejar como deuda visible.
