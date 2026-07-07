# Demo 03 - Reconstruccion de contrato implicito desde codigo y payloads

## Objetivo

Derivar un contrato tecnico probable comparando lo que espera el codigo con lo que traen payloads de ejemplo, para detectar incompatibilidades de integracion sin depender de documentacion completa.

## Artefactos de apoyo

- `../technical_automation_lab/derive_contract_candidates.py`
- `../technical_automation_lab/contracts/legacy_order_service.py`
- `../technical_automation_lab/contracts/partner_payload_samples.json`
- `../technical_automation_lab/.github/prompts/derive-contract.prompt.md`

## Resultado esperado

- Ejecutar `python3 derive_contract_candidates.py`.
- Abrir `output/contract_candidates.json`.
- Mostrar:
  - campos esperados por codigo;
  - diferencias por muestra;
  - mapeos semanticos candidatos;
  - validaciones sugeridas.
