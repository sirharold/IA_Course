from __future__ import annotations

import json
import os

import requests


def build_prompt(text: str) -> str:
    return (
        "Extract a compact JSON object with keys: "
        "system, severity, symptom, next_step. "
        "Do not add markdown.\n\n"
        f"Incident text:\n{text}"
    )


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not defined")

    incident_text = (
        "Payments API timeout after partner response exceeded 30 seconds. "
        "Checkout retries are failing and users see duplicate attempts."
    )
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        params={"key": api_key},
        headers={"Content-Type": "application/json"},
        json={
            "contents": [
                {
                    "parts": [
                        {
                            "text": build_prompt(incident_text),
                        }
                    ]
                }
            ]
        },
        timeout=30,
    )
    print("status:", response.status_code)
    payload = response.json()
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
