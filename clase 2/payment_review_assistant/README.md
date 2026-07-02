# Payment Review Assistant

Mini proyecto preparado para la clase 2 del curso de IA aplicada al desarrollo de software.

## Objetivo didactico / Learning Goal

ES: Este proyecto no esta pensado para construir una aplicacion completa. Esta pensado para que los alumnos practiquen dentro de Visual Studio Code con GitHub Copilot sobre un codigo pequeno pero suficientemente realista.

EN: This project is not intended to be a full application. It is designed so students can practice in Visual Studio Code with GitHub Copilot on a small but realistic codebase.

## Que deberian hacer los alumnos / Suggested Student Tasks

1. Abrir esta carpeta en Visual Studio Code.
2. Leer rapidamente la estructura del proyecto.
3. Usar Copilot Chat para explicar archivos y funciones.
4. Comparar prompts vagos versus prompts con contexto.
5. Redactar o ajustar `.github/copilot-instructions.md`.
6. Documentar una funcion o modulo.
7. Proponer una mejora pequena y verificable.

## Archivos sugeridos para la clase / Recommended Files

- `main.py`
- `payment_review/service.py`
- `payment_review/normalizers.py`
- `payment_review/rules.py`
- `payment_review/reporting.py`
- `data/sample_reviews.json`

## Archivos de contexto para IA / AI Context Files

Este repo tambien incluye una demostracion de instrucciones separadas por ambito:

- `.github/copilot-instructions.md`
- `.github/instructions/architecture.instructions.md`
- `.github/instructions/requirements.instructions.md`
- `.github/instructions/security.instructions.md`
- `.github/instructions/testing.instructions.md`
- `.github/instructions/data.instructions.md`
- `.github/instructions/refactoring.instructions.md`
- `.github/instructions/documentation.instructions.md`
- `.github/instructions/operations.instructions.md`
- `AGENTS.md`

La idea no es que exista un numero magico de archivos, sino mostrar como separar contexto por responsabilidad cuando el proyecto crece.

## Ejecucion / Run

ES: Si quieres correr el ejemplo localmente:

EN: If you want to run the example locally:

```bash
python3 main.py
```

## Exportacion de reportes / Report Export

ES: Ahora puedes exportar el reporte en `csv`, `excel` o `pdf`.

EN: You can now export the report as `csv`, `excel`, or `pdf`.

### Dependencias / Dependencies

```bash
python3 -m pip install openpyxl reportlab pytest
```

### Uso rapido / Quick Usage

```bash
# Salida de texto en consola (default)
python3 main.py

# CSV
python3 main.py --format csv --output out/reporte.csv

# Excel (.xlsx)
python3 main.py --format excel --output out/reporte.xlsx

# Alias de Excel
python3 main.py --format xlsx --output out/reporte.xlsx

# PDF
python3 main.py --format pdf --output out/reporte.pdf

# Archivo de entrada custom
python3 main.py --format csv --input data/sample_reviews.json --output out/reporte.csv
```

### Rutas por defecto / Default Output Paths

ES: Si no envias `--output` para `csv`, `excel`, `xlsx` o `pdf`, el sistema crea un archivo en `out/`.

EN: If `--output` is omitted for `csv`, `excel`, `xlsx`, or `pdf`, the system writes into `out/`.

- `csv` -> `out/report.csv`
- `excel` / `xlsx` -> `out/report.xlsx`
- `pdf` -> `out/report.pdf`

### Troubleshooting

1. ES: `Unsupported format ...`: usa solo `text`, `csv`, `excel`, `xlsx` o `pdf`.
	EN: Use only `text`, `csv`, `excel`, `xlsx`, or `pdf`.
2. ES: Error de dependencia para Excel/PDF: instala `openpyxl` y `reportlab`.
	EN: Install `openpyxl` and `reportlab`.
3. ES: Error de escritura en salida: verifica permisos y que la carpeta exista o pueda crearse.
	EN: Check write permissions and destination path.

### Pruebas / Tests

```bash
pytest
```

## Observaciones / Notes

- El codigo contiene decisiones discutibles a proposito.
- Hay oportunidades de documentacion, aclaracion de supuestos y refactorizacion pequena.
- No hace falta implementar todo ni dejarlo perfecto.
