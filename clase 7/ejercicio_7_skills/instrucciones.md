# Ejercicio 7 Skills - Documentar un modulo tecnico con y sin skill

## Objetivo del ejercicio

Comparar la generacion de documentacion tecnica con prompt libre contra el uso de un skill orientado a documentacion o explicacion estructurada de codigo.

## Lo esperado

Al terminar, deberias evaluar si el skill deja una salida mas estable, mas reusable y menos dependiente de como formulas el prompt en ese momento.

## Antes de empezar: preparar el skill

1. Revisa la guia [PREPARACION_SKILLS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_SKILLS.md).
2. Crea o instala un skill de documentacion tecnica o lectura estructurada.
3. Si usas skills del proyecto, deja el skill en una carpeta como:
   - `.github/skills/documentacion-tecnica/SKILL.md`
4. Si ya estabas dentro de una sesion de Copilot CLI, recarga los skills.
5. Verifica que el skill quede disponible antes de hacer la comparacion.

## Instrucciones

1. Usa este archivo:
   - [clase 4/codigo/contracts/legacy_order_service.py](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%204/codigo/contracts/legacy_order_service.py)
2. Sin usar skill, pide a Copilot:
   - explicar que hace el modulo;
   - listar dependencias o supuestos visibles;
   - marcar un riesgo tecnico.
3. Guarda el resultado en `doc_sin_skill.md`.
4. Ahora usa un skill de documentacion tecnica o lectura estructurada.
5. Ejecuta la misma tarea sobre el mismo archivo.
6. Guarda el resultado en `doc_con_skill.md`.
7. Compara ambos resultados y registra:
   - cual fue mas claro;
   - cual fue mas reusable;
   - si el skill realmente redujo ambiguedad.

## Entregable

- `doc_sin_skill.md`
- `doc_con_skill.md`
- comparacion breve
