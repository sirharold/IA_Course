from __future__ import annotations

import requests


API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_forecast() -> dict:
    response = requests.get(
        API_URL,
        params={
            "latitude": -33.45,
            "longitude": -70.67,
            "hourly": "temperature_2m,precipitation_probability",
            "forecast_days": 1,
            "timezone": "America/Santiago",
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def print_summary(payload: dict) -> None:
    hourly = payload.get("hourly", {})
    times = hourly.get("time", [])
    temperatures = hourly.get("temperature_2m", [])
    precipitation = hourly.get("precipitation_probability", [])

    if not times or not temperatures:
        raise ValueError("Hourly forecast is missing required fields")

    print("Forecast summary")
    for index in range(min(3, len(times), len(temperatures))):
        precip_value = precipitation[index] if index < len(precipitation) else "n/a"
        print(
            {
                "time": times[index],
                "temperature_2m": temperatures[index],
                "precipitation_probability": precip_value,
            }
        )


if __name__ == "__main__":
    print_summary(fetch_forecast())
