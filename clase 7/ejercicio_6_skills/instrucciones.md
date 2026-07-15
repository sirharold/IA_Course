# Ejercicio 6 Skills - Analisis de logs con y sin skill

## Objetivo del ejercicio

Comparar el analisis de logs hecho con un prompt libre contra el analisis de la misma tarea usando un skill especifico.

## Lo esperado

Al terminar, deberias notar si el skill reduce ambiguedad, ordena mejor la salida y te ahorra repetir instrucciones. El objetivo no es probar que el skill siempre gana, sino ver cuando si agrega consistencia.

## Antes de empezar: preparar el skill

1. Revisa la guia [PREPARACION_SKILLS.md](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/PREPARACION_SKILLS.md).
2. Crea o instala un skill de revision de logs en tu entorno.
3. Si usas skills del proyecto, deja el skill en una carpeta como:
   - `.github/skills/revision-logs/SKILL.md`
4. Si ya estabas dentro de una sesion de Copilot CLI, recarga los skills.
5. Verifica que el skill quede disponible antes de hacer la comparacion.

## Instrucciones

1. Usa este archivo:
   - [clase 6/Ejercicio avanzado 2/sample_runtime_logs.ndjson](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%202/sample_runtime_logs.ndjson)
2. Sin usar skill, pide a Copilot:
   - identificar errores;
   - resumir hallazgos;
   - separar hechos de posibles inferencias;
   - sugerir una validacion adicional.
3. Guarda el resultado en `logs_sin_skill.md`.
4. Ahora usa el skill de analisis de logs que este disponible en tu entorno de clase.
5. Ejecuta la misma tarea sobre el mismo archivo.
6. Guarda el resultado en `logs_con_skill.md`.
7. Compara ambos resultados y escribe 5 lineas:
   - que gano el skill;
   - que siguio necesitando criterio humano;
   - si valdria la pena reutilizar este skill en el trabajo real.

## Entregable

- `logs_sin_skill.md`
- `logs_con_skill.md`
- comparacion breve
