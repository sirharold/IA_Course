from reconciliation.service import reconcile
from reconciliation.utils import normalize_amount


def test_reconcile_returns_summary_buckets():
    result = reconcile()
    assert set(result.keys()) == {
        "matched",
        "missing_in_gateway",
        "amount_mismatches",
        "duplicate_gateway_rows",
    }


def test_default_data_has_one_amount_mismatch():
    result = reconcile()
    assert len(result["amount_mismatches"]) == 1


def test_normalize_amount_empty_string_becomes_zero():
    assert normalize_amount("") == 0
