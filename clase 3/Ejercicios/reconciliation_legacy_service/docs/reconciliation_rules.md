# Reconciliation Rules

Version preliminar de reglas operativas.

## Reglas declaradas

1. El matching se hace por `external_id` y monto.
2. Si existe diferencia menor o igual a 100 CLP, se acepta como conciliado.
3. Los duplicados del gateway deben conservarse para revision manual.
4. Los montos vacios deben rechazarse y no convertirse a cero.
5. Las monedas equivalentes como `$` y `CLP` deben tratarse igual.

## Observacion

Este documento puede estar desactualizado respecto del codigo real.
