from __future__ import annotations

import os

import requests


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"{name} is required")
    return value


def fetch_offer() -> dict:
    base_url = required_env("API_BASE_URL")
    api_key = required_env("API_KEY")
    caller_env = required_env("CALLER_ENV")
    user_id = required_env("USER_ID")
    region = required_env("REGION")

    response = requests.get(
        f"{base_url}/v1/customer-offer",
        headers={
            "X-API-Key": api_key,
            "X-Caller-Environment": caller_env,
        },
        params={
            "user_id": user_id,
            "region": region,
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def print_summary(payload: dict) -> None:
    customer = payload["customer"]
    print(
        {
            "caller_environment": payload.get("caller_environment"),
            "user_id": customer.get("user_id"),
            "recommended_product": customer.get("recommended_product"),
            "discount_pct": customer.get("discount_pct"),
            "price_usd": customer.get("price_usd"),
            "has_debug": "debug" in payload,
            "has_release_tag": "release_tag" in payload,
            "feature_count": len(customer.get("features", [])),
        }
    )


if __name__ == "__main__":
    print_summary(fetch_offer())
