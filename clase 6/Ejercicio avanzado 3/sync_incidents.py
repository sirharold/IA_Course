import json
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("sample_incidents.json")
OUTPUT_FILE = Path(__file__).with_name("incident_sync_output.json")


def load_items(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize(item):
    return {
        "incident_id": item["ticket_id"],
        "service": item["service"],
        "priority": item["severity"],
        "status": item["state"],
    }


def main():
    items = load_items(INPUT_FILE)
    normalized = []

    for item in items:
        normalized.append(normalize(item))

    with OUTPUT_FILE.open("w", encoding="utf-8") as handle:
        json.dump(normalized, handle, indent=2)

    print(f"Synced {len(normalized)} incidents into {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
