# Ejercicio 9 Skills - Triage inicial de incidente con y sin skill

## Objetivo del ejercicio

Comparar un triage inicial hecho con prompt libre contra un skill orientado a incidentes o clasificacion inicial.

## Lo esperado

Al terminar, deberias evaluar si el skill mejora la uniformidad de la salida y reduce instrucciones repetidas, sin olvidar que la priorizacion final sigue siendo humana.

## Antes de empezar: preparar el skill

1. Revisa la guia [PREPARACION_SKILLS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_SKILLS.md).
2. Crea o instala un skill de triage de incidentes o clasificacion inicial.
3. Si usas skills del proyecto, deja el skill en una carpeta como:
   - `.github/skills/triage-incidentes/SKILL.md`
4. Si ya estabas dentro de una sesion de Copilot CLI, recarga los skills.
5. Verifica que el skill quede disponible antes de hacer la comparacion.

## Instrucciones

1. Abre el archivo [incidente_ejemplo.txt](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/ejercicio_9_skills/incidente_ejemplo.txt).
2. Sin usar skill, pide a Copilot:
   - resumir el incidente;
   - extraer servicio, error e impacto;
   - listar 2 dudas que requieren validacion.
3. Guarda el resultado en `incidente_sin_skill.md`.
4. Ahora usa un skill de triage o clasificacion inicial.
5. Ejecuta la misma tarea con el mismo archivo.
6. Guarda el resultado en `incidente_con_skill.md`.
7. Compara ambos resultados y registra:
   - si el skill dejo la salida mas util;
   - si hubo menos ambiguedad;
   - que parte igual no deberia automatizarse del todo.

## Entregable

- `incidente_sin_skill.md`
- `incidente_con_skill.md`
- comparacion breve
