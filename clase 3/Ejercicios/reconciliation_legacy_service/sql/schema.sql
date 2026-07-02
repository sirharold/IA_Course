DROP TABLE IF EXISTS core_transactions;
DROP TABLE IF EXISTS gateway_transactions;

CREATE TABLE core_transactions (
    row_number INTEGER,
    external_id TEXT,
    amount_raw TEXT,
    currency TEXT,
    source TEXT,
    status TEXT,
    captured_at TEXT
);

CREATE TABLE gateway_transactions (
    row_number INTEGER,
    external_id TEXT,
    amount_raw TEXT,
    currency TEXT,
    source TEXT,
    status TEXT,
    captured_at TEXT
);
