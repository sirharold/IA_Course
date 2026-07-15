# Ejercicio 4 MCP - Consultar CSVs con DuckDB MCP

## Objetivo del ejercicio

Usar un MCP de consulta de datos para responder preguntas concretas sobre archivos CSV, sin depender solo de inspeccion manual o de prompts sobre texto copiado.

## Lo esperado

Al terminar, deberias ver que MCP puede agregar valor cuando la tarea exige consultar datos de forma precisa y repetible. El beneficio esperado es menos aproximacion manual y mas respuesta verificable.

## Instrucciones

1. Usa estos archivos como fuente:
   - [clase 4/codigo/data/core_transactions.csv](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%204/codigo/data/core_transactions.csv)
   - [clase 4/codigo/data/gateway_transactions.csv](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%204/codigo/data/gateway_transactions.csv)
2. Sin MCP, inspecciona manualmente los archivos y responde en una nota:
   - cuantos registros aproximados tiene cada archivo;
   - que columnas ves;
   - que preguntas te costaria responder manualmente.
3. Guarda esa nota en `inspeccion_manual.md`.
4. Ahora usa el MCP de DuckDB o el servidor de consulta disponible en tu entorno.
5. Carga ambos CSVs.
6. Responde estas preguntas:
   - cuantos registros tiene cada archivo;
   - que estados distintos aparecen;
   - cuantos registros por estado tiene cada archivo.
7. Guarda la salida en `consulta_con_mcp.md`.
8. Escribe una comparacion de 5 lineas:
   - que pudiste verificar mejor con MCP;
   - que costo de setup aparecio;
   - cuando valdria la pena usar este tipo de tooling.

## Entregable

- `inspeccion_manual.md`
- `consulta_con_mcp.md`
- comparacion breve
