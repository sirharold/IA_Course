def build_summary(result):
    lines = []
    lines.append("RECONCILIATION SUMMARY")
    lines.append(f"Matched: {len(result['matched'])}")
    lines.append(f"Missing in gateway: {len(result['missing_in_gateway'])}")
    lines.append(f"Amount mismatches: {len(result['amount_mismatches'])}")
    lines.append(f"Duplicate gateway rows: {len(result['duplicate_gateway_rows'])}")
    lines.append("")

    if result["missing_in_gateway"]:
        lines.append("Missing rows:")
        for row in result["missing_in_gateway"]:
            lines.append(
                f"- {row['external_id']} {row['amount']} {row['currency']} (core row {row['row_number']})"
            )

    if result["amount_mismatches"]:
        lines.append("")
        lines.append("Amount mismatches:")
        for item in result["amount_mismatches"]:
            lines.append(
                "- "
                f"{item['core']['external_id']} core={item['core']['amount']} "
                f"gateway={item['gateway']['amount']}"
            )

    return "\n".join(lines)
