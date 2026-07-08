from __future__ import annotations

from pathlib import Path

import requests


BASE_URL = "http://127.0.0.1:8010"
API_KEY = "demo-local-key"
INCIDENTS_FILE = Path(__file__).resolve().parents[1] / "mock_api" / "sample_incidents.txt"


def first_incident() -> str:
    return INCIDENTS_FILE.read_text(encoding="utf-8").splitlines()[0]


def main() -> None:
    response = requests.post(
        f"{BASE_URL}/v1/extract-incident",
        headers={
            "Content-Type": "application/json",
            "X-API-Key": API_KEY,
        },
        json={
            "instruction": "Return structured fields only",
            "text": first_incident(),
        },
        timeout=20,
    )
    response.raise_for_status()
    result = response.json()["result"]
    print(
        {
            "system": result.get("system"),
            "severity": result.get("severity"),
            "symptom": result.get("symptom"),
            "next_step": result.get("next_step"),
        }
    )


if __name__ == "__main__":
    main()
