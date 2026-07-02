---
applyTo: "payment_review/**/*.py"
---

## Arquitectura

- Mantener el flujo principal en `payment_review/service.py`.
- `normalizers.py` contiene transformaciones pequenas y reutilizables.
- `rules.py` concentra la evaluacion de riesgo y scoring.
- `reporting.py` transforma resultados tecnicos en texto legible.
- Evitar mezclar carga de datos, reglas de negocio y presentacion en una sola funcion.
- Preferir cambios pequenos que respeten la separacion actual antes de proponer una reescritura total.
