import argparse
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "incident_note.txt"
DEFAULT_OUTPUT = ROOT / "incident_summary.md"


def build_prompt(incident_text: str) -> str:
    return f"""
Lee el siguiente incidente tecnico y responde en Markdown.

Necesito exactamente estas secciones:
- Resumen breve
- Severidad sugerida
- Siguiente paso recomendado

No inventes datos que no esten en el texto.
Mantente breve y tecnico.

Incidente:
{incident_text}
""".strip()


def call_copilot(prompt: str) -> str:
    if shutil.which("copilot") is None:
        raise RuntimeError("GitHub Copilot CLI no esta instalado o no esta disponible en PATH.")

    result = subprocess.run(
        ["copilot", "-p", prompt],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        stderr = result.stderr.strip() or "Sin detalle adicional."
        raise RuntimeError(f"La llamada a copilot fallo con codigo {result.returncode}: {stderr}")

    output = result.stdout.strip()
    if not output:
        raise RuntimeError("Copilot no devolvio contenido.")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera un resumen tecnico usando GitHub Copilot CLI.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Ruta al archivo de entrada.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Ruta al archivo Markdown de salida.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"No existe el archivo de entrada: {input_path}")

    incident_text = input_path.read_text(encoding="utf-8").strip()
    if not incident_text:
        raise SystemExit("El archivo de entrada esta vacio.")

    prompt = build_prompt(incident_text)
    summary = call_copilot(prompt)
    output_path.write_text(summary + "\n", encoding="utf-8")

    print(f"Resumen generado en: {output_path}")


if __name__ == "__main__":
    main()
