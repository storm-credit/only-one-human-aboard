#!/usr/bin/env python3
"""Compatibility front-end for Deep Context compilation.

V2 keeps the frozen Deep Context schema while accepting the exact field vocabulary
used across the nine existing Episode Blueprint files. It delegates story serialization
to compile_deep_contexts.py; no story fact is invented here.
"""
from __future__ import annotations

import re
import compile_deep_contexts as base

_original_field = base.field
_original_normalize = base.normalize_preserved

ALIASES = {
    "Immediate Want": ("Immediate Want", "Want"),
    "A-Plot": ("A-Plot", "Action"),
    "End Turn": ("End Turn", "End State"),
    "Continuity Output": ("Continuity Output", "Continuity"),
}


def parse_fields_bounded(block: str) -> dict[str, str]:
    """Parse bold Episode Card fields without leaking following Beat/Act QA prose.

    The source blueprints use slightly different field vocabularies, but all actual
    card fields are bold `**Key:** value` lines. Any Markdown heading or horizontal
    rule terminates the currently open field capture.
    """
    out: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal key, buf
        if key is not None:
            out[key] = base.clean(" ".join(buf))
        key, buf = None, []

    for line in block.splitlines():
        s = line.strip()
        m = re.match(r"^\*\*([^*]+?):\*\*\s*(.*)$", s)
        if m:
            flush()
            key = m.group(1).strip()
            buf = [m.group(2).strip()]
            continue
        if s == "---" or s.startswith("#"):
            flush()
            continue
        if key is not None:
            if not s:
                continue
            if s.startswith("- "):
                buf.append(s[2:].strip())
            else:
                buf.append(s)
    flush()
    return out


def field_with_blueprint_aliases(card, *names: str, default: str = "NOT_SPECIFIED") -> str:
    expanded: list[str] = []
    for name in names:
        for candidate in ALIASES.get(name, (name,)):
            if candidate not in expanded:
                expanded.append(candidate)
    return _original_field(card, *expanded, default=default)


def normalize_preserved_v2(ep, card, rm, path) -> None:
    _original_normalize(ep, card, rm, path)
    text = path.read_text(encoding="utf-8")
    keys = (
        "realized_relationship_delta",
        "realized_knowledge_delta",
        "realized_material_delta",
        "realized_world_institution_delta",
        "realized_asset_lifecycle_delta",
        "actual_next_episode_carry",
    )
    key_alt = "|".join(re.escape(k) for k in keys)
    text = re.sub(
        rf"(?m)^-\s+({key_alt}):\s*PENDING\s*$",
        r"\1: PENDING",
        text,
    )
    path.write_text(text, encoding="utf-8")


base.parse_fields = parse_fields_bounded
base.field = field_with_blueprint_aliases
base.normalize_preserved = normalize_preserved_v2

if __name__ == "__main__":
    raise SystemExit(base.main())
