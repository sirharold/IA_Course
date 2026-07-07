# Reporte de anomalias

## Resumen

- Anomalias de conciliacion: 0
- Eventos de log: 4
- Niveles de log: {'warning': 2, 'error': 1, 'info': 1}

## Tipos de anomalia


## Eventos relevantes

- [warning] customer_ref_normalization :: Gateway customer_ref contained unexpected formatting for external_ref=TX-9002
- [error] partner_payload_rejected :: Missing required field documentNumber in partner payload for order PO-9001
- [warning] line_item_shape :: Observed qty instead of quantity in partner payload for order PO-9001

## Controles sugeridos

- Revisar anomalias repetidas por `external_ref`.
- Confirmar si discrepancias de estado corresponden a fases validas del negocio.
- Verificar si los warnings de parsing aparecen sobre las mismas referencias que las anomalias de conciliacion.
