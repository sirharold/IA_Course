import json
import sys
from pathlib import Path

REQUIRED_KEYS = {"incident_id", "service", "priority", "status"}


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_sync.py <output-file>")
        raise SystemExit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Missing output file: {path}")
        raise SystemExit(1)

    with path.open("r", encoding="utf-8") as handle:
        items = json.load(handle)

    if not isinstance(items, list):
        print("Output must be a JSON list")
        raise SystemExit(1)

    for index, item in enumerate(items, start=1):
        missing = REQUIRED_KEYS - set(item.keys())
        if missing:
            print(f"Record {index} is missing keys: {sorted(missing)}")
            raise SystemExit(1)

        for key in REQUIRED_KEYS:
            value = item.get(key)
            if not isinstance(value, str) or not value.strip():
                print(f"Record {index} has invalid value for {key}")
                raise SystemExit(1)

    print(f"Validation OK: {len(items)} records")


if __name__ == "__main__":
    main()
