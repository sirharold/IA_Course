# Ejercicio avanzado 3 - Dashboard web para comparar prompt, skill y MCP

## Objetivo del ejercicio

Construir una pequeña interfaz web o dashboard que muestre, en una sola vista, como cambia una misma tarea cuando se resuelve con prompt libre, con skill y con apoyo de MCP.

## Lo esperado

Al terminar, deberias tener una demo visual y entendible. El objetivo no es hacer una aplicación compleja, sino un dashboard pequeño que permita comparar enfoques y discutir cuándo vale la pena usar cada uno.

## Requisitos sugeridos

Puedes usar una de estas opciones:

- Streamlit
- una pagina HTML simple con datos generados previamente
- cualquier herramienta web ligera que puedas ejecutar localmente

La recomendacion para este ejercicio es `Streamlit`.

## Starter disponible

Ya tienes una base minima para empezar:

- [starter_app.py](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/ejercicio_avanzado_3_web_dashboard/starter_app.py)
- [requirements.txt](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%207/ejercicio_avanzado_3_web_dashboard/requirements.txt)

No lo dejes tal cual. Usalo como punto de partida para mostrar tus propios resultados.

## Archivos base

Usa como fuente al menos uno de estos conjuntos:

- [clase 6/Ejercicio avanzado 2/sample_runtime_logs.ndjson](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%202/sample_runtime_logs.ndjson)
- [clase 6/Ejercicio avanzado 1/sample_tickets.json](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/clase%206/Ejercicio%20avanzado%201/sample_tickets.json)

Y apóyate, si hace falta, en resultados generados en ejercicios anteriores.

## Instrucciones

1. Instala las dependencias del starter:
   ```bash
   pip install -r requirements.txt
   ```
2. Crea una carpeta `salidas` dentro de este ejercicio.
3. Elige una tarea tecnica concreta para comparar. Ejemplos validos:
   - resumen de logs;
   - triage inicial;
   - backlog operativo.
4. Genera tres salidas separadas para esa misma tarea:
   - una con prompt libre;
   - una con skill;
   - una donde decidas si MCP aporta o no.
5. Guarda esos tres resultados como:
   - `salidas/prompt_libre.md`
   - `salidas/con_skill.md`
   - `salidas/con_mcp_o_decision.md`
6. Ejecuta el starter una primera vez:
   ```bash
   streamlit run starter_app.py
   ```
7. Comprueba que la app muestre tus archivos de `salidas/`.
8. Crea una aplicacion web ligera con estos componentes minimos:
   - titulo del caso;
   - descripcion de la tarea elegida;
   - una seccion por enfoque;
   - una tabla o lista comparativa final.
9. Si usas Streamlit, parte desde `starter_app.py`.
10. Si prefieres, renombralo a `app.py` o crea tu propia variante.
11. En la interfaz muestra obligatoriamente:
   - que tarea se esta comparando;
   - que entrada se uso;
   - salida del prompt libre;
   - salida del skill;
   - salida o decision sobre MCP;
   - una conclusion final.
12. Agrega al menos un componente visual. Puede ser:
   - tabla;
   - métrica;
   - gráfico simple;
   - tabs;
   - columnas comparativas.
13. Personaliza el starter. Como minimo debes:
   - cambiar el nombre del caso;
   - reemplazar los textos de ejemplo;
   - completar la comparacion final;
   - ajustar la interfaz para que refleje tu caso.
14. Ejecuta la aplicacion localmente y revisa que no queden placeholders.
15. Toma una captura o deja una nota con:
   - que se entiende mejor al verlo en dashboard;
   - que enfoque fue mas util;
   - donde el dashboard deja visible un tradeoff real.
16. Guarda esa nota en `salidas/reflexion_dashboard.md`.

## Como usar el starter correctamente

- Primero genera los archivos de `salidas/`.
- Despues ejecuta `streamlit run starter_app.py`.
- Usa el starter para cargar y visualizar tus resultados.
- No entregues la app con los textos de ejemplo ni con la tabla vacia.

## Entregable

- `app.py`, `starter_app.py` adaptado o equivalente
- `salidas/prompt_libre.md`
- `salidas/con_skill.md`
- `salidas/con_mcp_o_decision.md`
- `salidas/reflexion_dashboard.md`
