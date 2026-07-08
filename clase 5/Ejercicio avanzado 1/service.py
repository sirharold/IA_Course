import json
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


HOST = "127.0.0.1"
PORT = 8020
API_KEY = "course-demo-key"
SUPPORTED_ENVS = {"development", "staging", "production"}
DATA_DIR = Path(__file__).resolve().parent / "data"


def load_env_data() -> dict[str, list[dict]]:
    datasets = {}
    for env_name in SUPPORTED_ENVS:
        with (DATA_DIR / f"{env_name}.json").open("r", encoding="utf-8") as handle:
            datasets[env_name] = json.load(handle)
    return datasets


DATASETS = load_env_data()


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=True, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def find_record(records: list[dict], user_id: str, region: str | None) -> dict | None:
    for record in records:
        if record["user_id"] != user_id:
            continue
        if region and record["region"] != region:
            continue
        return record
    return None


def build_customer_payload(caller_env: str, record: dict) -> dict:
    base_customer = {
        "user_id": record["user_id"],
        "full_name": record["full_name"],
        "region": record["region"],
        "plan": record["plan"],
        "account_status": record["account_status"],
        "recommended_product": record["recommended_product"],
        "discount_pct": record["discount_pct"],
        "price_usd": record["price_usd"],
        "features": record["features"],
    }
    if caller_env == "development":
        return {
            "customer": {
                **base_customer,
                "internal_score": record["internal_score"],
                "experiments": record["experiments"],
                "notes": record["notes"],
            },
            "debug": {
                "matched_from": "development.json",
                "campaign_id": record["campaign_id"],
                "request_shape": "verbose",
            },
        }
    if caller_env == "staging":
        return {
            "customer": {
                **base_customer,
                "experiments": record["experiments"],
            },
            "release_tag": record["release_tag"],
        }
    return {"customer": base_customer}


def build_customer_row(caller_env: str, record: dict) -> dict:
    row = {
        "user_id": record["user_id"],
        "full_name": record["full_name"],
        "region": record["region"],
        "plan": record["plan"],
        "account_status": record["account_status"],
        "recommended_product": record["recommended_product"],
        "discount_pct": record["discount_pct"],
        "price_usd": record["price_usd"],
        "feature_count": len(record["features"]),
    }
    if caller_env == "development":
        row["internal_score"] = record["internal_score"]
        row["has_debug"] = True
    elif caller_env == "staging":
        row["release_tag"] = record["release_tag"]
    return row


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            json_response(self, 200, {"status": "ok", "supported_environments": sorted(SUPPORTED_ENVS)})
            return
        if parsed.path not in {"/v1/customer-offer", "/v1/customer-offers"}:
            json_response(self, 404, {"error": "not_found"})
            return

        if self.headers.get("X-API-Key") != API_KEY:
            json_response(self, 401, {"error": "unauthorized", "message": "invalid API key"})
            return

        caller_env = self.headers.get("X-Caller-Environment", "").strip().lower()
        if caller_env not in SUPPORTED_ENVS:
            json_response(self, 400, {"error": "bad_request", "message": "invalid caller environment"})
            return

        query = parse_qs(parsed.query)
        user_id = query.get("user_id", [""])[0].strip()
        region = query.get("region", [""])[0].strip().lower() or None

        if parsed.path == "/v1/customer-offers":
            plan = query.get("plan", [""])[0].strip().lower() or None
            rows = []
            for record in DATASETS[caller_env]:
                if region and record["region"] != region:
                    continue
                if plan and record["plan"] != plan:
                    continue
                rows.append(build_customer_row(caller_env, record))
            json_response(
                self,
                200,
                {
                    "request_id": str(uuid.uuid4()),
                    "caller_environment": caller_env,
                    "data_version": f"{caller_env}-2026-07",
                    "query": {"region": region, "plan": plan},
                    "rows": rows,
                    "row_count": len(rows),
                },
            )
            return

        if not user_id:
            json_response(self, 400, {"error": "bad_request", "message": "user_id is required"})
            return

        record = find_record(DATASETS[caller_env], user_id, region)
        if not record:
            json_response(self, 404, {"error": "not_found", "message": f"user {user_id} not found"})
            return

        payload = build_customer_payload(caller_env, record)
        json_response(
            self,
            200,
            {
                "request_id": str(uuid.uuid4()),
                "caller_environment": caller_env,
                "data_version": f"{caller_env}-2026-07",
                "query": {"user_id": user_id, "region": region},
                **payload,
            },
        )

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Advanced Env API listening on http://{HOST}:{PORT}")
    print("Required API key:", API_KEY)
    server.serve_forever()
