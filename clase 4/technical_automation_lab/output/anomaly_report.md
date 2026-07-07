# Reporte de anomalias

## Resumen

- Anomalias de conciliacion: 4
- Eventos de log: 4
- Niveles de log: {'warning': 2, 'error': 1, 'info': 1}
- Hallazgos priorizados: 6

## Tipos de anomalia

- customer_ref_mismatch: 1
- missing_in_core: 1
- missing_in_gateway: 1
- status_mismatch: 1

## Hallazgos priorizados

- [high] partner_payload_rejected | ref=PO9001 | accion=comparar este payload con el contrato esperado antes de reintentar la integracion
  - detalle: Missing required field documentNumber in partner payload for order PO-9001
  - evidencia: error:partner_payload_rejected
- [high] missing_in_gateway | ref=TX9004 | accion=revisar si la exportacion del gateway quedo incompleta o si hubo desfase de corte
  - detalle: transaction exists in core but not in gateway export
- [high] missing_in_core | ref=TX9999 | accion=confirmar si el core omitio el registro o si la referencia pertenece a otro proceso
  - detalle: transaction exists in gateway export but not in core export
- [medium] line_item_shape | ref=PO9001 | accion=comparar este payload con el contrato esperado antes de reintentar la integracion
  - detalle: Observed qty instead of quantity in partner payload for order PO-9001
  - evidencia: warning:line_item_shape
- [medium] customer_ref_mismatch | ref=TX9002 | accion=revisar normalizacion y origen de `customer_ref` antes de reconciliar
  - detalle: core=cust002 gateway=cust020
  - evidencia: warning:customer_ref_normalization
- [medium] status_mismatch | ref=TX9003 | accion=validar si la pareja de estados corresponde a una fase permitida del flujo
  - detalle: status mismatch: core=reversed gateway=authorized

## Eventos relevantes

- [warning] customer_ref_normalization :: Gateway customer_ref contained unexpected formatting for external_ref=TX-9002
- [error] partner_payload_rejected :: Missing required field documentNumber in partner payload for order PO-9001
- [warning] line_item_shape :: Observed qty instead of quantity in partner payload for order PO-9001

## Controles sugeridos

- Revisar anomalias repetidas por `external_ref` y no solo por tipo.
- Confirmar si discrepancias de estado corresponden a fases validas del negocio o a un bug real.
- Registrar referencias explicitas en logs de integracion para poder correlacionar payloads y anomalias sin lectura manual.
- Mantener separadas las evidencias observables de las recomendaciones operativas.
