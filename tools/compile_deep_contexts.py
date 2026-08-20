#!/usr/bin/env python3
"""Compile V3 Deep Projected Context sidecars from exact Episode Blueprints + thin routers.

This compiler does not invent story events. It serializes already-authored Episode Blueprint
fields into the frozen Deep Context schema, carries router ancestry/branch/concurrency guards,
and preserves EP001-028 hand-compiled bodies while normalizing their frontmatter.

PROJECTED is forecast, never realized continuity. Dynamic Actual remains PENDING until prose/JIT.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BP_DIR = ROOT / "docs/prewriting-v3"
ROUTER_DIR = ROOT / "docs/obsidian-v3/contexts"
DEEP_DIR = ROOT / "docs/obsidian-v3/deep-contexts"

ACT_RANGES = {
    1: (1, 42), 2: (43, 94), 3: (95, 136), 4: (137, 181), 5: (182, 228),
    6: (229, 279), 7: (280, 327), 8: (328, 370), 9: (371, 410),
}

ACT_GUARDS = {
    1: "Ordinary-world first. Do not objectively confirm regression, branching, substrate, or HUMAN:1; ordinary failures remain genuinely possible.",
    2: "Disaster/concurrency first. Resolve ACT2_LEDGER geography/time before scene execution; do not explain the branch mechanism. EP094 ends H-A current-lived state.",
    3: "H-B is current-lived. H-A knowledge/state enters only through explicit memory/provenance; secondary characters retain independent causality.",
    4: "Prediction and social consequence before ontology. Evidence must change choices/relationships before any explanatory model hardens.",
    5: "Keep Arun current-life separation explicit and hold HUMAN meaning behind the reveal fence; do not collapse identity into explanation.",
    6: "Resolve ACT6_LEDGER concurrency/resource/network state before execution; causality must remain distributed across people and institutions.",
    7: "Action/evidence before ontology. Every explanatory beat must be earned by a concrete decision, cost, failed model, or operational consequence.",
    8: "HUMAN provenance is not personhood. HUMAN:1 must remain de-collectified and must not become a collectible-character family or sacred merchandise target.",
    9: "Descendant completion and return/payoff outrank novelty. No rerun/new ontology by default; EP406-410 add no major mystery and close through consequence/return.",
}

KNOWN_LABELS = [
    "[주인공/TBD]", "Mira", "Selene", "Rafi", "Arun", "Sora", "Gideon", "Niko", "Juno",
    "Transit Dispatcher", "caregiver", "Caregiver", "family", "parents", "sibling",
]

@dataclass
class EpisodeCard:
    ep: int
    act: int
    title: str
    fields: dict[str, str]
    raw: str
    source: str


def clean(value: str | None, default: str = "NOT_SPECIFIED") -> str:
    if value is None:
        return default
    value = re.sub(r"\s+", " ", value).strip()
    return value or default


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("unterminated frontmatter")
    out: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def router(ep: int) -> dict[str, str]:
    path = ROUTER_DIR / f"CTX-V3-EP{ep:03d}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return parse_frontmatter(path.read_text(encoding="utf-8"))


def parse_fields(block: str) -> dict[str, str]:
    out: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal key, buf
        if key is not None:
            out[key] = clean(" ".join(buf))
        key, buf = None, []

    for line in block.splitlines():
        m = re.match(r"^\*\*([^*]+?):\*\*\s*(.*)$", line.strip())
        if m:
            flush()
            key = m.group(1).strip()
            buf = [m.group(2).strip()]
            continue
        if key is not None:
            s = line.strip()
            if not s or s == "---" or s.startswith("# ") or s.startswith("## "):
                continue
            if s.startswith("- "):
                buf.append(s[2:].strip())
            elif not s.startswith("#"):
                buf.append(s)
    flush()
    return out


def load_blueprints() -> dict[int, EpisodeCard]:
    cards: dict[int, EpisodeCard] = {}
    heading = re.compile(r"(?m)^##\s+EP(\d{3})\s*[—–-]\s*(.+?)\s*$")
    for act in range(1, 10):
        path = BP_DIR / f"EPISODE-BLUEPRINT-ACT{act}-v0.1.md"
        if not path.exists():
            raise FileNotFoundError(path)
        text = path.read_text(encoding="utf-8")
        matches = list(heading.finditer(text))
        if not matches:
            raise RuntimeError(f"no episode headings parsed from {path}")
        for i, m in enumerate(matches):
            ep = int(m.group(1))
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[m.end():end]
            if ep in cards:
                raise RuntimeError(f"duplicate EP{ep:03d}")
            cards[ep] = EpisodeCard(
                ep=ep, act=act, title=clean(m.group(2)), fields=parse_fields(block), raw=block,
                source=str(path.relative_to(ROOT)).replace("\\", "/"),
            )
    expected = set(range(1, 411))
    missing = sorted(expected - set(cards))
    extra = sorted(set(cards) - expected)
    if missing or extra:
        raise RuntimeError(f"blueprint coverage error missing={missing} extra={extra}")
    for act, (lo, hi) in ACT_RANGES.items():
        bad = [ep for ep in range(lo, hi + 1) if cards[ep].act != act]
        if bad:
            raise RuntimeError(f"Act{act} range mismatch: {bad}")
    return cards


def fm_for(ep: int, rm: dict[str, str], source: str, preserved: bool) -> str:
    branch = rm.get("branch_guard", "H-A" if ep <= 94 else "H-B")
    concurrency = rm.get("concurrency", "NONE") or "NONE"
    mode = "manual-body-preserved" if preserved else "blueprint-compiled"
    lines = [
        "---", f"id: DEEP-V3-EP{ep:03d}", "type: deep_projected_context", f"episode: EP{ep:03d}",
        f"router: CTX-V3-EP{ep:03d}", "schema: DEEP-CONTEXT-SCHEMA-v1", "context_kind: DEEP_PROJECTED",
        "projection_semantics: FORECAST_NOT_ACTUAL", "dynamic_actual: PENDING",
        f"branch_state_namespace: {branch}", "cross_branch_inheritance: BLOCKED_UNLESS_EXPLICIT",
        "microbundle_compile_cap: 5", f"act: {rm.get('act', 'UNKNOWN')}", f"volume: {rm.get('volume', 'UNKNOWN')}",
        f"subact: {rm.get('subact', 'UNKNOWN')}", f"beat: {rm.get('beat', 'UNKNOWN')}", f"concurrency: {concurrency}",
        f"source_snapshot: router=CTX-V3-EP{ep:03d}; blueprint={source}; mode={mode}",
        "stale_if_changed: router|exact_episode_blueprint|DEEP-CONTEXT-SCHEMA-v1|character-role-matrix|relationship-network|asset-roster|reveal-router",
        "---",
    ]
    return "\n".join(lines)


def body_after_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return text
    return "\n".join(lines[end + 1:]).lstrip("\n")


def field(card: EpisodeCard, *names: str, default: str = "NOT_SPECIFIED") -> str:
    for name in names:
        if name in card.fields:
            return clean(card.fields[name], default)
    return default


def clue_class(clue: str) -> str:
    c = clue.upper()
    tags = [tag for tag in ("PLANT", "REINFORCE", "PAYOFF", "OPEN", "SEED", "NONE") if tag in c]
    if "NONE" in tags and len(tags) > 1:
        tags.remove("NONE")
    return "+".join(tags) if tags else ("NONE" if clue == "NOT_SPECIFIED" else "SOURCE_DEFINED")


def mentioned_labels(card: EpisodeCard) -> list[str]:
    hay = " ".join([field(card, "POV", default=""), field(card, "Relationship", default=""), field(card, "A-Plot", default=""), field(card, "Immediate Want", default="")])
    found: list[str] = []
    for label in KNOWN_LABELS:
        if label.lower() in hay.lower() and label not in found:
            found.append(label)
    pov = field(card, "POV", default="")
    if pov and pov != "NOT_SPECIFIED" and pov not in found:
        found.insert(0, pov)
    return found[:3]


def boundary_note(ep: int, branch: str) -> str:
    if ep == 94:
        return "BOUNDARY: this is the final H-A current-lived episode. Forecast to EP095 must not auto-inherit same-name/same-face current-person state."
    if ep == 95:
        return "BOUNDARY: first H-B current-lived episode. H-A state may enter only as explicit memory/provenance, never as automatic current-person continuity."
    if ep == 1:
        return "SERIES ENTRY: no prior prose Actual exists; incoming is authored baseline only."
    if ep == 410:
        return "SERIES EXIT: closure/return only; no next-episode forecast and no new major mystery."
    return f"Current-lived namespace remains {branch}; cross-branch inheritance stays blocked unless explicitly sourced."


def compile_body(card: EpisodeCard, cards: dict[int, EpisodeCard], rm: dict[str, str]) -> str:
    ep = card.ep
    branch = rm.get("branch_guard", "H-A" if ep <= 94 else "H-B")
    concurrency = rm.get("concurrency", "NONE") or "NONE"
    pov = field(card, "POV")
    zone = field(card, "Zone")
    want = field(card, "Immediate Want")
    aplot = field(card, "A-Plot")
    relationship = field(card, "Relationship")
    world = field(card, "World")
    clue = field(card, "Clue")
    kf = field(card, "Knowledge Fence", default="Blueprint supplies no narrower local fence; author-side world truth remains SEALED and only observed evidence is available to POV/reader.")
    end_turn = field(card, "End Turn")
    continuity = field(card, "Continuity Output", default="No extra Blueprint continuity field; use End Turn as forecast selector only.")
    act_guard = ACT_GUARDS[card.act]
    labels = mentioned_labels(card)
    active = ", ".join(labels) if labels else f"POV={pov}; relationship actors from exact Blueprint only"

    if ep > 1:
        prev = cards[ep - 1]
        incoming = f"FORECAST from EP{ep-1:03d}: End Turn={field(prev, 'End Turn')} | Continuity Output={field(prev, 'Continuity Output', default='No explicit Continuity Output.')}. This is not realized Actual; replace with JIT CONTINUITY-FROZEN before drafting."
    else:
        incoming = "Authored series baseline only. There is no prior prose Actual; do not fabricate one."

    if "주인공" in pov or "[주인공/TBD]" in pov:
        protag = f"POV_OWNER. Immediate Want={want} Decision surface is bounded by A-Plot and authority in World/Relationship; competence creates options, not universal command."
    else:
        protag = f"OFF-POV / INFLUENCE_ONLY_UNLESS_BLUEPRINT_EXPLICIT. {pov} owns the episode's lived decision line. Do not reroute success, discovery, or emotional resolution through the protagonist merely for centrality."

    if clue == "NOT_SPECIFIED":
        clue = "NONE unless the exact Blueprint card says otherwise; compiler may not invent a clue."
    cc = clue_class(clue)
    asset = "collectibility_job: NONE_BY_DEFAULT_AT_STATIC_COMPILE. eligible != foreground. Use current sub-act collectibility overlay + master roster at JIT; 0-1 new foreground recognition preferred, 2 only as one natural functional unit. Never promote HUMAN:1 into a collectible-character family."
    institution = f"Source-owned institutional/world pressure: {world} Relationship/institution interface: {relationship}"
    foreshadow = f"classification={cc}. Source clue={clue} Outgoing selector={end_turn} No authorial ominous narration beyond Blueprint evidence."
    genre = f"Execution engine: {aplot} Immediate Want: {want} Act guard: {act_guard}"
    concurrency_line = f"Concurrency preflight REQUIRED: router token {concurrency}; resolve time/geography/resource order before FROZEN." if concurrency != "NONE" else "Concurrency preflight: NONE beyond ordinary local continuity unless exact Blueprint/ledger says otherwise."

    return f"""# DEEP V3 EP{ep:03d} — {card.title}

> Deep Projected Context sidecar. It compiles existing authority for execution; it is **not Canon**, does **not override the exact Episode Blueprint**, and does **not contain future Actual continuity**.

## Structural Inheritance
- episode: EP{ep:03d}
- router: CTX-V3-EP{ep:03d}
- act: {rm.get('act', 'UNKNOWN')}
- volume: {rm.get('volume', 'UNKNOWN')}
- subact: {rm.get('subact', 'UNKNOWN')}
- beat: {rm.get('beat', 'UNKNOWN')}
- blueprint: {card.source} selector `EP{ep:03d}`
- branch: {branch}
- concurrency: {concurrency}
- {boundary_note(ep, branch)}

## Projected Incoming
{incoming}

## Protagonist Context
- POV: {pov}
- {protag}

## Character Context
- active_core_cap: max 3 salient characters including POV.
- projected_active_core: {active}
- influence_only: everyone else referenced by Blueprint/relationship graph; do not pull them into scene causality without need.
- character agenda authority: exact Episode Blueprint + current `V3-CORE-CAST-ACT-ROLE-MATRIX-v0.1.md`; this sidecar does not invent a new agenda.

## Relationship Context
- projected relationship line: {relationship}
- state semantics: FORECAST_NOT_ACTUAL. Before drafting, replace assumptions with realized prior-episode continuity.
- independence guard: every named character keeps an off-protagonist objective and may refuse/help/act for reasons not routed through protagonist convenience.

## World / Location Context
- zone: {zone}
- projected world pressure: {world}
- location truth: current observable/operational layer only; inaccessible author-side world model remains sealed.

## Asset / Collectibility Context
- {asset}

## Institution / Faction / Network Context
- {institution}
- authority guard: technical knowledge, social standing, or narrative centrality never grants cross-domain command unless the Blueprint explicitly does.

## Mystery / Reveal / Knowledge Fence
- source clue: {clue}
- local knowledge fence: {kf}
- world_truth: SEALED_LINK_ONLY.
- reader/POV may use only evidence already exposed by prior realized prose plus this episode's Blueprint-observable actions.
- {boundary_note(ep, branch)}

## Foreshadow / MacGuffin / Payoff
- {foreshadow}
- ordinary-cause guard: mundane incidents remain allowed to be mundane; not every repeat, object, route, failure, or record gap becomes a clue.

## Genre Engine
- {genre}
- causal diversity guard: rotate practical, social, institutional, survival, mystery, relationship, and cost/reward engines as Blueprint assigns; no protagonist causal monopoly.

## Execution Constraints
- exact Blueprint A-Plot: {aplot}
- exact Immediate Want: {want}
- exact End Turn: {end_turn}
- {concurrency_line}
- act hard guard: {act_guard}
- no Shadow Blueprint; no prose drafting from this node alone; max 5 direct retrieval bundles.
- active-core target <=3; collectible foreground is not a quota.

## Forecast Outgoing
- projected End Turn: {end_turn}
- projected Continuity Output: {continuity}
- semantics: FORECAST_NOT_ACTUAL. The next episode must consume realized prose delta when available, not blindly inherit this forecast.

## Dynamic Actual Placeholder
realized_relationship_delta: PENDING
realized_knowledge_delta: PENDING
realized_material_delta: PENDING
realized_world_institution_delta: PENDING
realized_asset_lifecycle_delta: PENDING
actual_next_episode_carry: PENDING

## Retrieval Compile Map
1. Episode Card — exact EP{ep:03d} Blueprint selector; A-Plot/Want/End Turn authority.
2. Immediate Continuity — prior realized CONTINUITY-FROZEN + this forecast selector; never future guessed Actual.
3. POV/Relationship — POV={pov}; relationship line + current role/relationship graph, active core <=3.
4. World/Zone/Material — Zone={zone}; current world/material/location router, branch={branch}.
5. Active Device/Return/Collectibility — clue/payoff selector + eligible asset overlay; foreground chosen JIT, not by quota.
"""


def normalize_preserved(ep: int, card: EpisodeCard, rm: dict[str, str], path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    body = body_after_frontmatter(text)
    path.write_text(fm_for(ep, rm, card.source, preserved=True) + "\n" + body.rstrip() + "\n", encoding="utf-8")


def write_all(preserve_through: int) -> tuple[int, int]:
    cards = load_blueprints()
    DEEP_DIR.mkdir(parents=True, exist_ok=True)
    preserved = 0
    compiled = 0
    for ep in range(1, 411):
        card = cards[ep]
        rm = router(ep)
        path = DEEP_DIR / f"DEEP-V3-EP{ep:03d}.md"
        if ep <= preserve_through and path.exists():
            normalize_preserved(ep, card, rm, path)
            preserved += 1
            continue
        path.write_text(fm_for(ep, rm, card.source, preserved=False) + "\n" + compile_body(card, cards, rm).rstrip() + "\n", encoding="utf-8")
        compiled += 1
    return preserved, compiled


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preserve-through", type=int, default=28, help="preserve existing hand-compiled body through this episode while normalizing frontmatter")
    args = ap.parse_args()
    if not 0 <= args.preserve_through <= 410:
        raise SystemExit("--preserve-through must be 0..410")
    preserved, compiled = write_all(args.preserve_through)
    print(f"Deep Context write complete: preserved={preserved} compiled={compiled} total={preserved+compiled}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
