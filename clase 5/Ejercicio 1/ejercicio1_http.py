from __future__ import annotations

import requests


def call_get() -> None:
    response = requests.get(
        "https://httpbin.org/get",
        params={
            "course": "clase5",
            "exercise": "1",
            "topic": "http",
        },
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    print("GET")
    print("status:", response.status_code)
    print("url:", payload.get("url"))
    print("args:", payload.get("args"))
    print()


def call_post() -> None:
    response = requests.post(
        "https://httpbin.org/post",
        json={
            "user_id": "usr-demo-100",
            "action": "compare-request-shapes",
            "source": "class-05",
        },
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    print("POST")
    print("status:", response.status_code)
    print("url:", payload.get("url"))
    print("json:", payload.get("json"))


if __name__ == "__main__":
    call_get()
    call_post()
