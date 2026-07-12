import json
from pathlib import Path

LOG_FILE = Path(__file__).with_name("sample_runtime_logs.ndjson")


def load_records(path: Path):
    records = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def main():
    records = load_records(LOG_FILE)
    error_count = 0

    for record in records:
        if record.get("level") == "ERROR":
            error_count += 1

    print(f"ERROR count: {error_count}")


if __name__ == "__main__":
    main()
