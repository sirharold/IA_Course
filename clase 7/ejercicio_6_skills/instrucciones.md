# Ejercicio 6 Skills - Analisis de logs con y sin skill

## Objetivo del ejercicio

Comparar el analisis de logs hecho con un prompt libre contra el analisis de la misma tarea usando un skill especifico.

## Lo esperado

Al terminar, deberias notar si el skill reduce ambiguedad, ordena mejor la salida y te ahorra repetir instrucciones. El objetivo no es probar que el skill siempre gana, sino ver cuando si agrega consistencia.

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
