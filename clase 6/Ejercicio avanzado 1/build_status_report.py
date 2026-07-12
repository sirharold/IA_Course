import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sample_tickets.json")


def load_tickets(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_report(tickets):
    lines = ["# Daily Status Report", ""]

    for ticket in tickets:
        lines.append(
            f"- {ticket['id']} | {ticket['status']} | {ticket['severity']} | {ticket['owner']} | {ticket['summary']}"
        )

    return "\n".join(lines)


def main():
    tickets = load_tickets(DATA_FILE)
    report = build_report(tickets)
    print(report)


if __name__ == "__main__":
    main()
