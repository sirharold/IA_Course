---
applyTo: "payment_review/**/*.py"
---

## Requerimientos observables

- El sistema carga pagos desde `data/sample_reviews.json`.
- Cada pago se normaliza antes de evaluarse.
- La salida final resume score, estado, prioridad y razones visibles.
- Los estados observables hoy son `approved`, `monitor` y `needs_manual_review`.
- Si falta contexto de negocio, explicitarlo en vez de inventar reglas nuevas.
