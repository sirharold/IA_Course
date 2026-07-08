from __future__ import annotations

from pathlib import Path

import pandas as pd
import requests
import streamlit as st
from dotenv import dotenv_values


APP_DIR = Path(__file__).resolve().parent
ENV_FILES = {
    "development": APP_DIR / ".env.development",
    "staging": APP_DIR / ".env.staging",
    "production": APP_DIR / ".env.production",
}


def load_config(selected_env: str) -> dict[str, str]:
    env_file = ENV_FILES[selected_env]
    if not env_file.exists():
        raise FileNotFoundError(
            f"Missing {env_file.name}. Create it from {env_file.name}.example first."
        )
    config = dotenv_values(env_file)
    required_keys = [
        "API_BASE_URL",
        "API_KEY",
        "CALLER_ENV",
        "DEFAULT_USER_ID",
        "DEFAULT_REGION",
    ]
    missing = [key for key in required_keys if not config.get(key)]
    if missing:
        raise ValueError(f"Missing required keys in {env_file.name}: {', '.join(missing)}")
    return {key: str(value) for key, value in config.items() if value is not None}


def fetch_offers(config: dict[str, str], region: str | None = None) -> dict:
    response = requests.get(
        f"{config['API_BASE_URL']}/v1/customer-offers",
        headers={
            "X-API-Key": config["API_KEY"],
            "X-Caller-Environment": config["CALLER_ENV"],
        },
        params={
            "region": region or config["DEFAULT_REGION"],
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def fetch_single_customer(config: dict[str, str], user_id: str, region: str | None = None) -> dict:
    response = requests.get(
        f"{config['API_BASE_URL']}/v1/customer-offer",
        headers={
            "X-API-Key": config["API_KEY"],
            "X-Caller-Environment": config["CALLER_ENV"],
        },
        params={
            "user_id": user_id,
            "region": region or config["DEFAULT_REGION"],
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    st.set_page_config(page_title="Customer Offers Viewer", layout="wide")
    st.title("Customer Offers Viewer")
    st.caption("Streamlit app for environment-aware API exploration")

    selected_env = st.selectbox("Environment", ["development", "staging", "production"])
    object_to_show = st.selectbox(
        "Object to show",
        ["offers_grid", "single_customer", "raw_response"],
    )

    try:
        config = load_config(selected_env)
        offers_payload = fetch_offers(config)
        rows = offers_payload.get("rows", [])
        df = pd.DataFrame(rows)
    except Exception as exc:
        st.error(f"Configuration or API error: {exc}")
        return

    if df.empty:
        st.warning("No rows returned from the API.")
        return

    user_options = df["user_id"].tolist()
    default_user = config["DEFAULT_USER_ID"]
    default_index = user_options.index(default_user) if default_user in user_options else 0
    selected_user = st.selectbox("Customer", user_options, index=default_index)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Grid")
        st.dataframe(df, use_container_width=True, hide_index=True)

    with col2:
        st.subheader("Selection summary")
        if selected_user:
            selected_row = df[df["user_id"] == selected_user].iloc[0].to_dict()
            st.json(selected_row)

    if object_to_show in {"single_customer", "raw_response"}:
        try:
            customer_payload = fetch_single_customer(config, selected_user)
        except Exception as exc:
            st.error(f"Could not fetch single customer: {exc}")
            return

        if object_to_show == "single_customer":
            st.subheader("Single customer detail")
            st.json(customer_payload.get("customer", {}))

        if object_to_show == "raw_response":
            with st.expander("Raw API response", expanded=True):
                st.json(customer_payload)


if __name__ == "__main__":
    main()
