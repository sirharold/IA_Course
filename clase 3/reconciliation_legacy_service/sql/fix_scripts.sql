-- Safe preview before fixing whitespace in external_id
SELECT
    row_number,
    external_id,
    TRIM(external_id) AS cleaned_external_id
FROM gateway_transactions
WHERE external_id != TRIM(external_id);

-- Example small cleanup script
UPDATE gateway_transactions
SET external_id = TRIM(external_id)
WHERE external_id != TRIM(external_id);

-- Safe preview before replacing empty amounts
SELECT
    row_number,
    external_id,
    amount_raw
FROM gateway_transactions
WHERE amount_raw IS NULL OR TRIM(amount_raw) = '';

-- Example targeted data fix for training purposes only
UPDATE gateway_transactions
SET amount_raw = '0'
WHERE amount_raw IS NULL OR TRIM(amount_raw) = '';
