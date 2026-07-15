# Ejercicio 8 Skills - Revisar un script como si fuera code review recurrente

## Objetivo del ejercicio

Usar un skill de revision tecnica para comparar una revision hecha con prompt libre contra una revision con criterio reusable.

## Lo esperado

Al terminar, deberias evaluar si el skill ayuda a repetir un mismo criterio de revision con menos variacion y menos esfuerzo de redaccion.

## Antes de empezar: preparar el skill

1. Revisa la guia [PREPARACION_SKILLS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_SKILLS.md).
2. Crea o instala un skill de code review o revision tecnica.
3. Si usas skills del proyecto, deja el skill en una carpeta como:
   - `.github/skills/code-review/SKILL.md`
4. Si ya estabas dentro de una sesion de Copilot CLI, recarga los skills.
5. Verifica que el skill quede disponible antes de hacer la comparacion.

## Instrucciones

1. Usa este archivo:
   - [clase 5/mock_api/mock_service.py](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%205/mock_api/mock_service.py)
2. Sin usar skill, pide a Copilot:
   - revisar validacion;
   - manejo de errores;
   - claridad del codigo;
   - riesgo tecnico visible.
3. Guarda el resultado en `review_sin_skill.md`.
4. Ahora usa un skill de code review o revision tecnica recurrente.
5. Ejecuta la misma revision sobre el mismo archivo.
6. Guarda el resultado en `review_con_skill.md`.
7. Compara los dos resultados y responde:
   - el skill fue mas consistente?;
   - el skill fue mas estricto o mas util?;
   - que parte aun requeriria revision humana.

## Entregable

- `review_sin_skill.md`
- `review_con_skill.md`
- comparacion breve
