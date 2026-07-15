# Ejercicio 10 Skills - Generar un reporte operativo repetitivo con y sin skill

## Objetivo del ejercicio

Comparar una tarea repetitiva de resumen operativo hecha con prompt libre contra una version apoyada por un skill reusable.

## Lo esperado

Al terminar, deberias evaluar si el skill ayuda cuando necesitas repetir muchas veces una misma estructura de salida y quieres reducir variacion entre ejecuciones.

## Antes de empezar: preparar el skill

1. Crea un skill de reporte operativo o status report.
2. Si usas skills del proyecto, deja el skill en una carpeta como:
   - `.github/skills/reporte-operativo/SKILL.md`
3. Usa un contenido base como este:

```md
---
name: reporte-operativo
description: Genera reportes operativos breves y repetibles. Usar cuando se pida un status report o resumen operativo.
---

Cuando prepares un reporte:

1. Resume pendientes relevantes.
2. Marca items sin owner o sin resolver.
3. Usa una estructura breve y operativa.
4. Cierra con focos de atencion o siguiente paso.
```

4. Si usas Copilot CLI y ya estabas dentro de una sesion, ejecuta:
   ```text
   /skills reload
   ```
5. Si usas VS Code o chat integrado, cierra y vuelve a abrir el chat. Si no basta, recarga la ventana de VS Code.
6. Verifica que el skill quede disponible antes de hacer la comparacion.

## Instrucciones

1. Usa este archivo:
   - [clase 6/Ejercicio avanzado 1/sample_tickets.json](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%201/sample_tickets.json)
2. Sin usar skill, pide a Copilot:
   - contar tickets no resueltos;
   - identificar tickets sin owner;
   - resumir en formato operativo breve.
3. Guarda el resultado en `reporte_sin_skill.md`.
4. Ahora usa un skill de status report, resumen operativo o tarea equivalente.
5. Ejecuta la misma tarea con el mismo archivo.
6. Guarda el resultado en `reporte_con_skill.md`.
7. Compara ambos resultados y responde:
   - cual fue mas facil de repetir;
   - cual dejo una salida mas util para otro miembro del equipo;
   - si el skill realmente ahorra trabajo en una tarea recurrente.

## Entregable

- `reporte_sin_skill.md`
- `reporte_con_skill.md`
- comparacion breve
