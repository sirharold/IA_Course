-- Query 1: duplicate external_id values in gateway
SELECT
    TRIM(external_id) AS external_id,
    COUNT(*) AS duplicate_count
FROM gateway_transactions
GROUP BY TRIM(external_id)
HAVING COUNT(*) > 1;

-- Query 2: rows with suspicious amount formats
SELECT
    row_number,
    external_id,
    amount_raw,
    currency
FROM gateway_transactions
WHERE amount_raw IS NULL
   OR TRIM(amount_raw) = ''
   OR amount_raw GLOB '*[A-Za-z]*';

-- Query 3: rows that might fail reconciliation due to spacing
SELECT
    row_number,
    external_id,
    '[' || external_id || ']' AS visible_id
FROM gateway_transactions
WHERE external_id != TRIM(external_id);

-- Query 4: compare core and gateway by cleaned id only
SELECT
    c.external_id AS core_id,
    g.external_id AS gateway_id,
    c.amount_raw AS core_amount,
    g.amount_raw AS gateway_amount
FROM core_transactions c
JOIN gateway_transactions g
  ON TRIM(c.external_id) = TRIM(g.external_id)
ORDER BY c.external_id;
