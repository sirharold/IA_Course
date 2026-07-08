from __future__ import annotations

import os

import requests


def fetch_payload() -> dict:
    base_url = os.getenv("API_BASE_URL", "http://127.0.0.1:8010")
    api_key = os.getenv("DEMO_API_KEY", "demo-local-key")
    response = requests.post(
        f"{base_url}/v1/classify-ticket",
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
        },
        json={
            "ticket_id": "INC-701",
            "text": "Billing export failed with null values and retry noise in logs.",
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    payload = fetch_payload()
    print(payload)


if __name__ == "__main__":
    main()
