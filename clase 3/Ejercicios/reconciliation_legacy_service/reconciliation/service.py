from pathlib import Path

from reconciliation.loaders import load_core_transactions, load_gateway_transactions
from reconciliation.matcher import match_transactions
from reconciliation.reporting import build_summary


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"


def reconcile(gateway_filename="gateway_transactions.csv"):
    core_rows = load_core_transactions()
    gateway_rows = load_gateway_transactions(gateway_filename)
    result = match_transactions(core_rows, gateway_rows)
    return result


def print_reconciliation_report(gateway_filename="gateway_transactions.csv"):
    result = reconcile(gateway_filename)
    print(build_summary(result))


def run_with_basic_logging(gateway_filename="gateway_transactions_dirty.csv"):
    try:
        return reconcile(gateway_filename)
    except Exception as error:
        log_path = LOG_DIR / "runtime.log"
        with open(log_path, "a", encoding="utf-8") as handle:
            handle.write(f"reconciliation failed: {error}\n")
        raise
