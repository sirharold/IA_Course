from __future__ import annotations

import json
import os

import requests


def main() -> None:
    project_id = os.getenv("VERTEX_PROJECT_ID")
    region = os.getenv("VERTEX_REGION", "us-central1")
    access_token = os.getenv("VERTEX_ACCESS_TOKEN")
    model = os.getenv("VERTEX_MODEL", "gemini-1.5-flash")
    if not project_id or not access_token:
        raise ValueError("VERTEX_PROJECT_ID and VERTEX_ACCESS_TOKEN are required")

    url = (
        f"https://{region}-aiplatform.googleapis.com/v1/projects/"
        f"{project_id}/locations/{region}/publishers/google/models/{model}:generateContent"
    )
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json={
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                "Summarize this incident as JSON with keys "
                                "system, severity, symptom, next_step.\n\n"
                                "Billing export produced null values in tax_id column after CSV ingestion."
                            )
                        }
                    ],
                }
            ]
        },
        timeout=30,
    )
    print("status:", response.status_code)
    print(json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    main()
