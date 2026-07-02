import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "artifacts"
SQL_DIR = BASE_DIR / "sql"
DB_PATH = DB_DIR / "reconciliation.db"


def create_schema(connection):
    schema = (SQL_DIR / "schema.sql").read_text(encoding="utf-8")
    connection.executescript(schema)


def load_csv(connection, table_name, filename):
    path = DATA_DIR / filename
    with open(path, "r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for index, row in enumerate(reader, start=2):
            rows.append(
                (
                    index,
                    row.get("external_id", ""),
                    row.get("amount", ""),
                    row.get("currency", ""),
                    row.get("source", ""),
                    row.get("status", ""),
                    row.get("captured_at", ""),
                )
            )

    connection.executemany(
        f"""
        INSERT INTO {table_name} (
            row_number,
            external_id,
            amount_raw,
            currency,
            source,
            status,
            captured_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def main():
    DB_DIR.mkdir(exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    try:
        create_schema(connection)
        load_csv(connection, "core_transactions", "core_transactions.csv")
        load_csv(connection, "gateway_transactions", "gateway_transactions_dirty.csv")
        connection.commit()
    finally:
        connection.close()

    print(DB_PATH)


if __name__ == "__main__":
    main()
