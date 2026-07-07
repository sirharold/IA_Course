from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any, Dict, List, Set


BASE_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = BASE_DIR / "contracts"
OUTPUT_DIR = BASE_DIR / "output"


def gather_key_paths(value: Any, prefix: str = "") -> Set[str]:
    paths: Set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            current = f"{prefix}.{key}" if prefix else key
            paths.add(current)
            paths.update(gather_key_paths(item, current))
    elif isinstance(value, list):
        for item in value:
            current = f"{prefix}[]"
            paths.add(current)
            paths.update(gather_key_paths(item, current))
    return paths


class PayloadVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.paths: Set[str] = set()

    def visit_Subscript(self, node: ast.Subscript) -> None:
        path = self._extract_path(node)
        if path:
            self.paths.add(path)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and node.func.attr == "get":
            path = self._extract_attribute_path(node.func.value)
            if path and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                self.paths.add(f"{path}.{node.args[0].value}")
        self.generic_visit(node)

    def _extract_path(self, node: ast.Subscript) -> str:
        keys: List[str] = []
        current: Any = node
        while isinstance(current, ast.Subscript):
            slice_value = current.slice
            if isinstance(slice_value, ast.Constant) and isinstance(slice_value.value, str):
                keys.append(slice_value.value)
            current = current.value
        base = self._extract_attribute_path(current)
        if base:
            keys.reverse()
            return ".".join([base] + keys)
        return ""

    def _extract_attribute_path(self, node: Any) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            left = self._extract_attribute_path(node.value)
            return f"{left}.{node.attr}" if left else node.attr
        return ""


def extract_expected_paths(code_path: Path) -> Set[str]:
    tree = ast.parse(code_path.read_text(encoding="utf-8"))
    visitor = PayloadVisitor()
    visitor.visit(tree)
    return {path.removeprefix("payload.") for path in visitor.paths if path.startswith("payload")}


def extract_sample_paths(samples_path: Path) -> Set[str]:
    payloads = json.loads(samples_path.read_text(encoding="utf-8"))
    paths: Set[str] = set()
    for payload in payloads:
        paths.update(gather_key_paths(payload))
    return paths


def compare_paths(expected: Set[str], observed: Set[str]) -> Dict[str, List[str]]:
    return {
        "expected_by_code": sorted(expected),
        "observed_in_samples": sorted(observed),
        "missing_in_samples": sorted(expected - observed),
        "unexpected_in_samples": sorted(observed - expected),
    }


def main() -> None:
    code_path = CONTRACTS_DIR / "legacy_order_service.py"
    samples_path = CONTRACTS_DIR / "partner_payload_samples.json"
    expected = extract_expected_paths(code_path)
    observed = extract_sample_paths(samples_path)
    comparison = compare_paths(expected, observed)
    output_path = OUTPUT_DIR / "contract_candidates.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(comparison, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"Contract comparison written to {output_path}")
    print(json.dumps({"missing_in_samples": len(comparison["missing_in_samples"])}, indent=2))


if __name__ == "__main__":
    main()
