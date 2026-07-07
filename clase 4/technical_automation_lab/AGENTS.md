# AGENTS.md

## Objetivo del repo

Este proyecto existe para practicar automatizacion tecnica sobre artefactos heterogeneos: datos tabulares, logs, texto exportado y codigo con contratos implicitos.

## Como usar este repo con agentes

- Revisa primero `.github/copilot-instructions.md`.
- Revisa luego `.github/instructions/` y `.github/prompts/`.
- Si hay tension entre instrucciones, prioriza:
  1. trazabilidad y validacion;
  2. reglas visibles en codigo, datos o documentos;
  3. seguridad y manejo de datos;
  4. claridad de salida y documentacion.

## Ambitos separados en este ejemplo

- automatizacion Python
- conciliacion de datos
- extraccion estructurada
- contratos implicitos
- reportes de anomalias

## Regla clave

No inventes reglas de negocio ni contratos que no esten sustentados por `data/`, `docs/`, `contracts/` o el codigo visible.
