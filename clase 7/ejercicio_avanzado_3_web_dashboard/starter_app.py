from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "salidas"


def read_text(filename: str) -> str:
    path = OUTPUT_DIR / filename
    if not path.exists():
        return f"[Falta el archivo: {filename}]"
    return path.read_text(encoding="utf-8")


st.set_page_config(page_title="Comparador Prompt vs Skill vs MCP", layout="wide")

st.title("Comparador de enfoques: prompt libre, skill y MCP")
st.caption("Starter para el ejercicio avanzado 3 de la clase 7")

st.markdown(
    """
Este dashboard esta pensado para comparar una misma tarea tecnica resuelta de tres formas:

- prompt libre
- skill
- MCP o decision justificada sobre no usar MCP

Completa los archivos en la carpeta `salidas/` y usa esta app como base.
"""
)

case_name = st.text_input(
    "Nombre del caso",
    value="Completa aqui el nombre del caso comparado",
)

task_description = st.text_area(
    "Descripcion breve de la tarea",
    value="Describe en 3 a 5 lineas que tarea tecnica estas comparando.",
    height=120,
)

st.subheader("Resumen del caso")

metric_col_1, metric_col_2, metric_col_3 = st.columns(3)
metric_col_1.metric("Caso", case_name if case_name.strip() else "Sin nombre")
metric_col_2.metric("Tiene skill", "Si")
metric_col_3.metric("MCP evaluado", "Si / No")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Prompt libre",
        "Skill",
        "MCP o decision",
        "Comparacion final",
    ]
)

with tab1:
    st.markdown("### Salida con prompt libre")
    st.code(read_text("prompt_libre.md"), language="markdown")

with tab2:
    st.markdown("### Salida con skill")
    st.code(read_text("con_skill.md"), language="markdown")

with tab3:
    st.markdown("### Salida con MCP o decision sobre MCP")
    st.code(read_text("con_mcp_o_decision.md"), language="markdown")

with tab4:
    st.markdown("### Comparacion estructurada")

    comparison_rows = [
        {
            "Enfoque": "Prompt libre",
            "Ventaja principal": "",
            "Costo o limite": "",
            "Nivel de control": "",
        },
        {
            "Enfoque": "Skill",
            "Ventaja principal": "",
            "Costo o limite": "",
            "Nivel de control": "",
        },
        {
            "Enfoque": "MCP o no usar MCP",
            "Ventaja principal": "",
            "Costo o limite": "",
            "Nivel de control": "",
        },
    ]

    st.dataframe(comparison_rows, use_container_width=True)

    st.markdown("### Reflexion final")
    st.code(read_text("reflexion_dashboard.md"), language="markdown")

st.markdown("---")

st.subheader("Indicaciones para completar el ejercicio")

st.markdown(
    """
1. Crea la carpeta `salidas/` si aun no existe.
2. Guarda estos archivos:
   - `prompt_libre.md`
   - `con_skill.md`
   - `con_mcp_o_decision.md`
   - `reflexion_dashboard.md`
3. Ejecuta la app con:

```bash
streamlit run starter_app.py
```

4. Personaliza este starter:
   - cambia el titulo del caso;
   - mejora la tabla comparativa;
   - agrega visuales si hace sentido;
   - explica tu conclusion final.
"""
)
