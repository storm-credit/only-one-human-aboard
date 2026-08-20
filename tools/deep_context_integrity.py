#!/usr/bin/env python3
"""Integrity gate for V3 Deep Projected Context sidecars.

Semantic content is intentionally NOT generated here.  This tool checks the
machine-verifiable contract around source-aware human/agent compilation:
coverage, frontmatter serialization, router ancestry, branch namespaces,
Projected-vs-Actual separation, required sections, and max-5 retrieval compile.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEEP_DIR = ROOT / "docs/obsidian-v3/deep-contexts"
ROUTER_DIR = ROOT / "docs/obsidian-v3/contexts"

REQUIRED_KEYS = {
    "id", "type", "episode", "router", "schema", "context_kind",
    "projection_semantics", "dynamic_actual", "branch_state_namespace",
    "cross_branch_inheritance", "microbundle_compile_cap", "source_snapshot",
    "stale_if_changed",
}
REQUIRED_HEADINGS = [
    "## Structural Inheritance",
    "## Projected Incoming",
    "## Protagonist Context",
    "## Character Context",
    "## Relationship Context",
    "## World / Location Context",
    "## Asset / Collectibility Context",
    "## Institution / Faction / Network Context",
    "## Mystery / Reveal / Knowledge Fence",
    "## Foreshadow / MacGuffin / Payoff",
    "## Genre Engine",
    "## Execution Constraints",
    "## Forecast Outgoing",
    "## Dynamic Actual Placeholder",
    "## Retrieval Compile Map",
]
REALIZED_KEYS = [
    "realized_relationship_delta",
    "realized_knowledge_delta",
    "realized_material_delta",
    "realized_world_institution_delta",
    "realized_asset_lifecycle_delta",
    "actual_next_episode_carry",
]


def frontmatter(text: str, path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing opening frontmatter fence"]
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, [f"{path}: missing closing frontmatter fence"]

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        # Top-level frontmatter is deliberately flat. Inline mappings/lists are
        # values; a space after ':' is required to avoid accidental YAML tokens.
        if line[:1].isspace():
            errors.append(f"{path}: nested/indented frontmatter not allowed: {line!r}")
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):(?:\s+)(.*)$", line)
        if not m:
            errors.append(f"{path}: invalid frontmatter serialization: {line!r}")
            continue
        key, value = m.group(1), m.group(2).strip()
        if key in data:
            errors.append(f"{path}: duplicate frontmatter key: {key}")
        data[key] = value
    return data, errors


def router_meta(ep: int) -> dict[str, str]:
    path = ROUTER_DIR / f"CTX-V3-EP{ep:03d}.md"
    text = path.read_text(encoding="utf-8")
    data, errors = frontmatter(text, path)
    if errors:
        raise RuntimeError("; ".join(errors))
    return data


def validate_one(ep: int, path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm, fm_errors = frontmatter(text, path)
    errors.extend(fm_errors)
    missing = sorted(REQUIRED_KEYS - set(fm))
    if missing:
        errors.append(f"{path}: missing frontmatter keys: {', '.join(missing)}")

    expected = f"{ep:03d}"
    checks = {
        "id": f"DEEP-V3-EP{expected}",
        "episode": f"EP{expected}",
        "router": f"CTX-V3-EP{expected}",
        "type": "deep_projected_context",
        "schema": "DEEP-CONTEXT-SCHEMA-v1",
        "context_kind": "DEEP_PROJECTED",
        "projection_semantics": "FORECAST_NOT_ACTUAL",
        "dynamic_actual": "PENDING",
        "cross_branch_inheritance": "BLOCKED_UNLESS_EXPLICIT",
        "microbundle_compile_cap": "5",
    }
    for key, value in checks.items():
        if fm.get(key) != value:
            errors.append(f"{path}: {key}={fm.get(key)!r}, expected {value!r}")

    try:
        rm = router_meta(ep)
    except Exception as exc:
        errors.append(f"{path}: router read failed: {exc}")
        rm = {}
    branch_guard = rm.get("branch_guard")
    if branch_guard and fm.get("branch_state_namespace") != branch_guard:
        errors.append(
            f"{path}: branch namespace {fm.get('branch_state_namespace')!r} != router {branch_guard!r}"
        )
    for key in ("volume", "subact", "beat"):
        token = rm.get(key)
        if token and token not in text:
            errors.append(f"{path}: missing router ancestry token {key}={token}")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{path}: missing section {heading}")

    for key in REALIZED_KEYS:
        matches = re.findall(rf"(?m)^{re.escape(key)}:\s*(.+)$", text)
        if len(matches) != 1:
            errors.append(f"{path}: {key} must appear exactly once; found {len(matches)}")
        elif matches[0].strip() != "PENDING":
            errors.append(f"{path}: {key} must remain PENDING, got {matches[0]!r}")

    # The retrieval map is a fixed five-bundle execution surface.  It may be
    # compact prose, but all five numbered lanes must remain represented.
    retrieval = text.split("## Retrieval Compile Map", 1)[-1] if "## Retrieval Compile Map" in text else ""
    for n in range(1, 6):
        if not re.search(rf"(?<!\d){n}(?!\d)", retrieval):
            errors.append(f"{path}: Retrieval Compile Map missing lane {n}")

    # Knowledge fence must keep author-side truth sealed or explicitly fenced.
    fence = text.split("## Mystery / Reveal / Knowledge Fence", 1)[-1].split("## Foreshadow / MacGuffin / Payoff", 1)[0]
    if not re.search(r"SEALED", fence, re.I):
        errors.append(f"{path}: knowledge fence lacks SEALED world-truth control")

    # Router concurrency is source authority. Deep Act2/Act6 nodes must declare
    # an explicit scope, but the validator does not invent the semantic scope.
    concurrency = rm.get("concurrency", "NONE")
    if concurrency not in {"", "NONE", None} and concurrency not in text:
        errors.append(f"{path}: router concurrency {concurrency} not carried into deep context")

    fg = len(re.findall(r"\bFOREGROUND\b", text))
    if fg > 5:
        # Text can mention FOREGROUND in guards, so this is a warning rather than
        # an automatic semantic failure. Hostile QA owns the final salience call.
        warnings.append(f"{path}: high FOREGROUND token count={fg}; manual collectibility QA required")

    return errors, warnings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--allow-partial", action="store_true", help="validate existing nodes without requiring 410/410")
    args = ap.parse_args()

    existing = sorted(DEEP_DIR.glob("DEEP-V3-EP[0-9][0-9][0-9].md")) if DEEP_DIR.exists() else []
    found_eps: list[int] = []
    errors: list[str] = []
    warnings: list[str] = []
    for path in existing:
        m = re.fullmatch(r"DEEP-V3-EP(\d{3})\.md", path.name)
        if not m:
            continue
        ep = int(m.group(1))
        found_eps.append(ep)
        e, w = validate_one(ep, path)
        errors.extend(e)
        warnings.extend(w)

    if len(found_eps) != len(set(found_eps)):
        errors.append("duplicate deep episode IDs detected")
    if not args.allow_partial:
        expected = list(range(1, 411))
        if found_eps != expected:
            missing = sorted(set(expected) - set(found_eps))
            extra = sorted(set(found_eps) - set(expected))
            errors.append(f"coverage failure: found={len(found_eps)} missing={missing[:30]} extra={extra[:30]}")

    print(f"deep-context files: {len(found_eps)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    for w in warnings:
        print(f"WARN {w}")
    for e in errors:
        print(f"ERROR {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
