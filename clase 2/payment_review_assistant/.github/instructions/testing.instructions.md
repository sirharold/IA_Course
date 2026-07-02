---
applyTo: "payment_review/**/*.py"
---

## Pruebas

- Derivar pruebas desde comportamiento visible y riesgos detectados.
- Cubrir al menos:
  - normalizacion de nombre;
  - normalizacion de canal y moneda;
  - scoring por monto;
  - casos con tags bloqueados;
  - ausencia de nombre o canal.
- Separar casos base, edge cases y casos de error.
