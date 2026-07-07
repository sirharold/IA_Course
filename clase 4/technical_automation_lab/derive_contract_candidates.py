from __future__ import annotations

import ast
import json
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set


BASE_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = BASE_DIR / "contracts"
OUTPUT_DIR = BASE_DIR / "output"

SEMANTIC_EQUIVALENTS = {
    ("order_id", "orderId"): "snake_case vs camelCase for order id",
    ("created_at", "requestedAt"): "timestamp field with alternate naming",
    ("totalAmount", "amount"): "prefixed amount field used by partner",
    ("document_id", "documentNumber"): "document identifier with alternate naming",
    ("full_name", "fullName"): "customer full name with alternate naming",
    ("country", "countryCode"): "country value likely encoded with shorter field name",
    ("qty", "quantity"): "quantity abbreviation used inside line items",
}


def gather_key_paths(value: Any, prefix: str = "") -> Set[str]:
    paths: Set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            current = f"{prefix}.{key}" if prefix else key
            paths.add(current)
            paths.update(gather_key_paths(item, current))
    elif isinstance(value, list):
        array_path = f"{prefix}[]" if prefix else "[]"
        paths.add(array_path)
        for item in value:
            paths.update(gather_key_paths(item, array_path))
    return paths


class PayloadVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.paths: Set[str] = set()
        self.scope_stack: List[Dict[str, str]] = [{}]

    def visit_Assign(self, node: ast.Assign) -> None:
        self.visit(node.value)
        resolved = self._resolve_expression_path(node.value)
        if resolved:
            for target in node.targets:
                self._bind_target(target, resolved)

    def visit_For(self, node: ast.For) -> None:
        iterable_path = self._resolve_iterable_path(node.iter)
        self.visit(node.iter)
        self._push_scope()
        try:
            if iterable_path:
                self._bind_target(node.target, iterable_path)
            for statement in node.body:
                self.visit(statement)
            for statement in node.orelse:
                self.visit(statement)
        finally:
            self._pop_scope()

    def visit_ListComp(self, node: ast.ListComp) -> None:
        self._visit_comprehension(node.generators, node.elt)

    def visit_DictComp(self, node: ast.DictComp) -> None:
        self._visit_comprehension(node.generators, node.key, node.value)

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        self._visit_comprehension(node.generators, node.elt)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        path = self._resolve_expression_path(node)
        if path:
            self.paths.add(path)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        path = self._resolve_expression_path(node)
        if path:
            self.paths.add(path)
        self.generic_visit(node)

    def _visit_comprehension(self, generators: Iterable[ast.comprehension], *body_nodes: ast.AST) -> None:
        generators = list(generators)

        def walk(index: int) -> None:
            if index >= len(generators):
                for body_node in body_nodes:
                    self.visit(body_node)
                return

            generator = generators[index]
            iterable_path = self._resolve_iterable_path(generator.iter)
            self.visit(generator.iter)
            self._push_scope()
            try:
                if iterable_path:
                    self._bind_target(generator.target, iterable_path)
                for if_node in generator.ifs:
                    self.visit(if_node)
                walk(index + 1)
            finally:
                self._pop_scope()

        walk(0)

    def _bind_target(self, target: ast.AST, source_path: str) -> None:
        if isinstance(target, ast.Name):
            self.scope_stack[-1][target.id] = source_path

    def _push_scope(self) -> None:
        self.scope_stack.append({})

    def _pop_scope(self) -> None:
        self.scope_stack.pop()

    def _lookup_alias(self, name: str) -> str:
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return ""

    def _resolve_iterable_path(self, node: ast.AST) -> str:
        path = self._resolve_expression_path(node)
        return f"{path}[]" if path else ""

    def _resolve_expression_path(self, node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return self._lookup_alias(node.id) or node.id

        if isinstance(node, ast.Subscript):
            base = self._resolve_expression_path(node.value)
            key = self._extract_slice_key(node.slice)
            if base and key:
                return f"{base}.{key}"
            return ""

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr == "get":
                base = self._resolve_expression_path(node.func.value)
                if base and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                    return f"{base}.{node.args[0].value}"
            return ""

        if isinstance(node, ast.Attribute):
            left = self._resolve_expression_path(node.value)
            return f"{left}.{node.attr}" if left else node.attr

        return ""

    @staticmethod
    def _extract_slice_key(slice_node: ast.AST) -> str:
        if isinstance(slice_node, ast.Constant) and isinstance(slice_node.value, str):
            return slice_node.value
        return ""


def extract_expected_paths(code_path: Path) -> Set[str]:
    tree = ast.parse(code_path.read_text(encoding="utf-8"))
    visitor = PayloadVisitor()
    visitor.visit(tree)
    return {
        path.removeprefix("payload.")
        for path in visitor.paths
        if path == "payload" or path.startswith("payload.")
    }


def load_payloads(samples_path: Path) -> List[Dict[str, Any]]:
    return json.loads(samples_path.read_text(encoding="utf-8"))


def normalize_leaf_name(value: str) -> str:
    return "".join(ch for ch in value.lower() if ch.isalnum())


def leaf_name(path: str) -> str:
    return path.split(".")[-1].replace("[]", "")


def parent_path(path: str) -> str:
    parts = path.split(".")
    return ".".join(parts[:-1])


def semantic_reason(observed_leaf: str, expected_leaf: str) -> str:
    for left, right in SEMANTIC_EQUIVALENTS:
        if {left, right} == {observed_leaf, expected_leaf}:
            return SEMANTIC_EQUIVALENTS[(left, right)]
    return ""


def mapping_score(observed_path: str, expected_path: str) -> tuple[int, str]:
    observed_leaf = leaf_name(observed_path)
    expected_leaf = leaf_name(expected_path)

    explicit_reason = semantic_reason(observed_leaf, expected_leaf)
    if explicit_reason:
        return 100, explicit_reason

    if parent_path(observed_path) == parent_path(expected_path):
        left = normalize_leaf_name(observed_leaf)
        right = normalize_leaf_name(expected_leaf)
        ratio = SequenceMatcher(None, left, right).ratio()
        if ratio >= 0.8:
            return 80, "similar field name under the same parent context"
        if ratio >= 0.55:
            return 55, "possible alternate naming under the same parent context"

    return 0, ""


def infer_candidate_mappings(expected: Set[str], observed: Set[str]) -> List[Dict[str, str]]:
    candidates: List[Dict[str, str]] = []
    missing = sorted(expected - observed)
    unexpected = sorted(observed - expected)

    for expected_path in missing:
        scored: List[tuple[int, str, str]] = []
        for observed_path in unexpected:
            score, reason = mapping_score(observed_path, expected_path)
            if score > 0:
                scored.append((score, observed_path, reason))

        if not scored:
            continue

        best_score, observed_path, reason = max(scored, key=lambda item: item[0])
        confidence = "high" if best_score >= 90 else "medium"
        candidates.append(
            {
                "expected_path": expected_path,
                "observed_path": observed_path,
                "confidence": confidence,
                "reason": reason,
            }
        )

    return candidates


def analyze_samples(expected: Set[str], payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    analyses: List[Dict[str, Any]] = []

    for index, payload in enumerate(payloads, start=1):
        observed = gather_key_paths(payload)
        missing = sorted(expected - observed)
        unexpected = sorted(observed - expected)
        candidate_mappings = infer_candidate_mappings(expected, observed)
        analyses.append(
            {
                "sample_index": index,
                "order_hint": payload.get("orderId") or payload.get("order_id") or f"sample-{index}",
                "missing_expected": missing,
                "unexpected_observed": unexpected,
                "candidate_mappings": candidate_mappings,
            }
        )

    return analyses


def unique_mappings(sample_analyses: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    seen: Set[tuple[str, str]] = set()
    mappings: List[Dict[str, str]] = []

    for analysis in sample_analyses:
        for item in analysis["candidate_mappings"]:
            key = (item["expected_path"], item["observed_path"])
            if key in seen:
                continue
            seen.add(key)
            mappings.append(item)

    return sorted(mappings, key=lambda item: (item["expected_path"], item["observed_path"]))


def build_validations(expected: Set[str], sample_analyses: List[Dict[str, Any]]) -> List[str]:
    validations: List[str] = [
        "Validar presencia de campos requeridos antes de transformar el payload.",
        "Registrar explicitamente equivalencias semanticas aceptadas entre nombres alternativos.",
        "Separar contradicciones confirmadas de mapeos solo sugeridos por heuristica.",
    ]

    if any(analysis["candidate_mappings"] for analysis in sample_analyses):
        validations.append("Agregar tabla de mapeo previo para aliases como `order_id -> orderId` o `qty -> quantity`.")

    if any("items[].quantity" in analysis["missing_expected"] for analysis in sample_analyses):
        validations.append("Verificar estructura de `items` y rechazar payloads que mezclen `quantity` con `qty` sin normalizacion.")

    return validations


def compare_paths(expected: Set[str], payloads: List[Dict[str, Any]]) -> Dict[str, Any]:
    observed_union: Set[str] = set()
    for payload in payloads:
        observed_union.update(gather_key_paths(payload))

    sample_analyses = analyze_samples(expected, payloads)
    return {
        "expected_by_code": sorted(expected),
        "observed_in_samples": sorted(observed_union),
        "missing_in_all_samples": sorted(expected - observed_union),
        "unexpected_in_any_sample": sorted(observed_union - expected),
        "sample_analysis": sample_analyses,
        "candidate_semantic_mappings": unique_mappings(sample_analyses),
        "suggested_validations": build_validations(expected, sample_analyses),
    }


def main() -> None:
    code_path = CONTRACTS_DIR / "legacy_order_service.py"
    samples_path = CONTRACTS_DIR / "partner_payload_samples.json"
    expected = extract_expected_paths(code_path)
    payloads = load_payloads(samples_path)
    comparison = compare_paths(expected, payloads)
    output_path = OUTPUT_DIR / "contract_candidates.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(comparison, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"Contract comparison written to {output_path}")
    print(
        json.dumps(
            {
                "samples": len(comparison["sample_analysis"]),
                "candidate_mappings": len(comparison["candidate_semantic_mappings"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
