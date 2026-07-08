import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "127.0.0.1"
PORT = 8010
API_KEY = os.getenv("DEMO_API_KEY", "demo-local-key")


SAMPLE_CLASSIFICATIONS = {
    "timeout": ("integration", "high"),
    "auth": ("security", "high"),
    "credential": ("security", "high"),
    "latency": ("performance", "medium"),
    "null": ("data-quality", "medium"),
    "csv": ("data-ingestion", "medium"),
}


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _read_json(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length", "0"))
    raw = handler.rfile.read(length) if length else b"{}"
    return json.loads(raw.decode("utf-8"))


def _classify_text(text: str) -> tuple[str, str]:
    lowered = text.lower()
    for needle, result in SAMPLE_CLASSIFICATIONS.items():
        if needle in lowered:
            return result
    return ("general", "low")


def _extract_incident(text: str) -> dict:
    lowered = text.lower()
    category, severity = _classify_text(text)
    system = "unknown"
    if "billing" in lowered:
        system = "billing"
    elif "payments" in lowered or "payment" in lowered:
        system = "payments"
    elif "orders" in lowered or "order" in lowered:
        system = "orders"

    symptom = text.split(".")[0].strip() if "." in text else text.strip()
    next_step = "review logs and validate input data"
    if severity == "high":
        next_step = "check credentials, logs and retry strategy"

    return {
        "system": system,
        "severity": severity,
        "category": category,
        "symptom": symptom,
        "next_step": next_step,
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            _json_response(self, 200, {"status": "ok", "service": "mock-api"})
            return

        _json_response(self, 404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.headers.get("X-API-Key") != API_KEY:
            _json_response(self, 401, {"error": "unauthorized", "message": "invalid API key"})
            return

        try:
            payload = _read_json(self)
        except json.JSONDecodeError:
            _json_response(self, 400, {"error": "bad_request", "message": "invalid JSON"})
            return

        if self.path == "/v1/classify-ticket":
            text = payload.get("text", "").strip()
            ticket_id = payload.get("ticket_id", "").strip()
            if not text or not ticket_id:
                _json_response(self, 400, {"error": "bad_request", "message": "ticket_id and text are required"})
                return
            category, severity = _classify_text(text)
            _json_response(
                self,
                200,
                {
                    "ticket_id": ticket_id,
                    "category": category,
                    "severity": severity,
                    "received_chars": len(text),
                },
            )
            return

        if self.path == "/v1/extract-incident":
            text = payload.get("text", "").strip()
            instruction = payload.get("instruction", "").strip()
            if not text:
                _json_response(self, 400, {"error": "bad_request", "message": "text is required"})
                return
            _json_response(
                self,
                200,
                {
                    "instruction_used": bool(instruction),
                    "result": _extract_incident(text),
                },
            )
            return

        _json_response(self, 404, {"error": "not_found"})

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Mock API listening on http://{HOST}:{PORT}")
    print("Expected X-API-Key:", API_KEY)
    server.serve_forever()
