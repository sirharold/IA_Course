from __future__ import annotations

import os

import requests


BASE_URL = "http://127.0.0.1:8010"


def main() -> None:
    api_key = os.getenv("DEMO_API_KEY")
    if not api_key:
        raise ValueError("DEMO_API_KEY is not defined")

    response = requests.post(
        f"{BASE_URL}/v1/classify-ticket",
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
        },
        json={
            "ticket_id": "INC-301",
            "text": "Partner auth credential expired and requests are failing with 401.",
        },
        timeout=20,
    )

    print("status:", response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()
