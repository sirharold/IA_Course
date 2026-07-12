from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

import requests


BASE_DIR = Path(__file__).resolve().parent
PROMPT_FILE = BASE_DIR / "prompt_fijo.txt"
MODELS_FILE = BASE_DIR / "selected_models.txt"
OUTPUT_DIR = BASE_DIR / "outputs"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")


def load_prompt() -> str:
    return PROMPT_FILE.read_text(encoding="utf-8").strip()


def load_models() -> list[str]:
    if not MODELS_FILE.exists():
        raise FileNotFoundError(
            "selected_models.txt does not exist. Create it from selected_models.txt.example first."
        )

    models = []
    for line in MODELS_FILE.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        models.append(value)

    if not models:
        raise ValueError("selected_models.txt is empty")

    return models


def slugify_model(model_slug: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", model_slug)


def call_model(model_slug: str, prompt: str) -> dict:
    if not API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not defined")

    started_at = time.perf_counter()
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model_slug,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": 0.3,
        },
        timeout=60,
    )
    elapsed_ms = round((time.perf_counter() - started_at) * 1000, 2)

    response.raise_for_status()
    payload = response.json()
    content = payload["choices"][0]["message"]["content"]

    return {
        "model": model_slug,
        "elapsed_ms": elapsed_ms,
        "content": content,
        "usage": payload.get("usage", {}),
    }


def save_response(result: dict) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    safe_name = slugify_model(result["model"])
    output_file = OUTPUT_DIR / f"{safe_name}.md"
    output_file.write_text(
        "\n".join(
            [
                f"# Modelo: {result['model']}",
                f"- Latencia aproximada: {result['elapsed_ms']} ms",
                f"- Uso reportado: {json.dumps(result['usage'], ensure_ascii=False)}",
                "",
                "## Respuesta",
                "",
                result["content"],
                "",
            ]
        ),
        encoding="utf-8",
    )


def save_summary(results: list[dict], errors: list[dict]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    summary_file = OUTPUT_DIR / "summary.json"
    summary_file.write_text(
        json.dumps(
            {
                "results": results,
                "errors": errors,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def main() -> None:
    prompt = load_prompt()
    models = load_models()

    print(f"Prompt cargado desde: {PROMPT_FILE.name}")
    print(f"Modelos a comparar: {len(models)}")

    results: list[dict] = []
    errors: list[dict] = []

    for model_slug in models:
        print(f"\nConsultando modelo: {model_slug}")
        try:
            result = call_model(model_slug, prompt)
            save_response(result)
            results.append(result)
            print(f"OK - archivo guardado para {model_slug}")
        except Exception as exc:
            errors.append({"model": model_slug, "error": str(exc)})
            print(f"ERROR - {model_slug}: {exc}")

    save_summary(results, errors)
    print(f"\nRespuestas guardadas en: {OUTPUT_DIR}")
    print("Resumen guardado en: outputs/summary.json")


if __name__ == "__main__":
    main()
