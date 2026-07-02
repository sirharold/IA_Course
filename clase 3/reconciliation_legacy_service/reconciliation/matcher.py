from reconciliation.utils import build_composite_key


def match_transactions(core_rows, gateway_rows):
    gateway_index = {}
    duplicates = []

    for row in gateway_rows:
        key = build_composite_key(row)
        if key in gateway_index:
            duplicates.append(row)
        gateway_index[key] = row

    matched = []
    missing_in_gateway = []
    amount_mismatches = []

    for row in core_rows:
        key = build_composite_key(row)
        gateway_row = gateway_index.get(key)

        if gateway_row:
            matched.append({"core": row, "gateway": gateway_row})
            continue

        partial = find_by_external_id(row, gateway_rows)
        if partial:
            amount_mismatches.append({"core": row, "gateway": partial})
        else:
            missing_in_gateway.append(row)

    return {
        "matched": matched,
        "missing_in_gateway": missing_in_gateway,
        "amount_mismatches": amount_mismatches,
        "duplicate_gateway_rows": duplicates,
    }


def find_by_external_id(core_row, gateway_rows):
    target_id = core_row.get("external_id")
    for row in gateway_rows:
        if row.get("external_id") == target_id:
            return row
    return None
