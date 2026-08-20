# V3 Rolling Episode Context Compilation Protocol v0.2

Status: `ACTIVE PREWRITING CONTEXT ARCHITECTURE CANDIDATE / NOT CANON / NO PROSE`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

Supersedes for new work:
- `V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.1.md`

Audit authority:
- `docs/qa/V3-EPISODE-CONTEXT-PACK-ARCHITECTURE-BLIND-SPOT-AUDIT-v0.1.md`

---

# 0. Core architecture

The repository already has complete global planning:
- 9 Acts,
- 18 execution Volumes,
- 28 Macro Sub-Acts,
- 56 Beat hubs,
- 410 Episode Blueprints,
- 410 Episode Router nodes,
- character/asset/reveal/state routing ledgers.

Therefore every episode SHOULD have a Context node, but Context has two strictly separated layers:

# `STATIC / PROJECTED` = EP001~410 materialized now
# `DYNAMIC / ACTUAL` = JIT freeze immediately before drafting

STATIC is not a second Blueprint.
DYNAMIC is not allowed to exist as future fact.

---

# 1. Authority split

## Episode Blueprint owns
- POV design,
- Immediate Want,
- A-Plot action,
- B-Plot/relationship design,
- world/institution movement,
- clue/device design,
- End Turn,
- forecast Continuity Output.

## Context Pack owns
- which authoritative slices to load,
- what state class is needed,
- what may/should be foregrounded,
- what may not leak,
- the actual current-state override at draft time,
- the compiled max-5 payload.

Hard:
# `DO NOT DRAFT FROM CONTEXT NODE ALONE.`

Resolution order:
`Context Node`
→ `exact Episode Blueprint heading`
→ `actual prior Continuity`
→ `selected current state slices`
→ `five-bundle drafting payload`.

---

# 2. STATIC / PROJECTED schema

Each `CTX-V3-EPxxx.md` must include:

```yaml
id: CTX-V3-EPxxx
type: episode_context
context_status: PROJECTED
episode: EP-V3-xxx
act: ACT-V3-xx
volume: VOL-V3-xx
subact: SA-V3-xA
beat: BEAT-V3-Bxx
context_schema_version: 0.2
blueprint_ref: <exact Act blueprint + EP heading selector>
reveal_ledger_ref: <current reveal ledger>
asset_router_ref: <current asset/subact router>
authority_status_at_compile: V3_CANDIDATE_NOT_CANON
compile_to_payload: max_5
stale_if_authority_changes: true
dynamic_actual_state: PENDING
```

Body fields:

### A. Projected incoming selector
Not `Immediate Continuity`.
Records the expected carry/source that will later be overridden by actual prior continuity.

### B. Target delta
What category of change this episode is designed to create:
- practical,
- relationship,
- mystery,
- institution/world,
- material/collectibility,
- knowledge/judgment.

Do not restate the whole A-Plot.

### C. Character / relationship selectors
- projected POV source,
- active relationship slice refs,
- relationship entry requirement,
- relationship target delta.

Never store a future target as if already achieved.

### D. World / material selectors
- location/institution slice refs,
- eligible asset families,
- background-only assets,
- HOLD assets where relevant,
- foreground recognition budget.

### E. Reveal / knowledge fence
- reveal phase,
- allowed clue/device state,
- forbidden forward truth,
- POV knowledge fence selector.

### F. Execution constraints
Directive levels:
- `MUST`
- `TARGET`
- `PREFER`
- `MAY`
- `FORBID`

Only MUST/FORBID are hard prose constraints.

### G. Forecast outgoing selector
Expected continuity category/Beat carry.
Actual realized output is written only after prose QA.

### H. Dynamic placeholders
All actual current-state values remain pending.

---

# 3. DYNAMIC / ACTUAL schema

Generated/refreshed JIT immediately before drafting:

```yaml
actual_incoming_continuity: ...
actual_relationship_state: ...
actual_material_state: ...
actual_location_access_state: ...
actual_institution_network_state: ...
pov_known_actual: ...
reader_confirmed_actual: ...
active_devices_actual: ...
foreground_assets_selected: ...
compiled_at: ...
context_status: FROZEN
```

Optional:
- `reader_suspected_optional` only if operationally useful,
- `propagation_required: true` only if a realized delta invalidates a locked future dependency.

DYNAMIC must never be bulk-generated for future episodes.

---

# 4. Runtime loop

`GLOBAL BLUEPRINT / PROJECTED CONTEXT`
→ `LOAD ACTUAL PRIOR CONTINUITY`
→ `JIT DYNAMIC FREEZE`
→ `COMPILE MAX-5 PAYLOAD`
→ `PROSE`
→ `QA`
→ `REALIZED DELTA FREEZE`
→ `MEANINGFUL STATE SNAPSHOT UPDATE`
→ `NEXT EPISODE RECOMPILE`.

---

# 5. Max-5 drafting payload

Regardless of Context file depth:

1. **Episode Card**
   - resolved from exact Episode Blueprint heading.

2. **Immediate Continuity**
   - actual previous output + local chronology only.

3. **POV / Relationship Microbundle**
   - actual POV state + necessary relationship delta(s).

4. **World / Zone / Material Microbundle**
   - actual location/institution rules + selected material families.

5. **Active Device / Return / Collectibility Microbundle**
   - active reveal/payoff/return chain only.

No extra direct slot per person/item.

---

# 6. Collectibility / salience rule

Context routing depth does not equal prose foreground density.

Separate:
- `eligible_assets`,
- `foreground_assets_selected`,
- `background_only`,
- `hold`.

Default:
- new foreground recognition 0~1 preferred,
- 2 only when naturally perceived as one functional unit,
- `collectibility_job: NONE` is valid,
- no model/manufacturer naming merely because asset has an internal ID.

Beat/Volume/Act cadence governs collection reward; no per-episode quota.

---

# 7. Knowledge fences / story-boundary guards

Hard:
- no Context follows global ontology links before episode-local reveal permission,
- reader knowledge and character knowledge remain separate.

Special continuity boundaries:
- EP001~094 current lived branch = H-A,
- EP095~410 current lived branch = H-B,
- H-A memories/provenance may be referenced only through explicit memory/evidence routes,
- Arun H-A memory state != Arun H-B current-person state,
- B12 explicit split remains:
  - EP084~087 → SA-2C,
  - EP088~091 → SA-2D.

No inheritance by same name/face alone.

---

# 8. Act2 / Act6 concurrency preflight

All Context nodes in Act2 and Act6 carry a concurrency requirement.

Before `FROZEN`:
- resolve current time window,
- resolve travel/access/closure state,
- resolve which concurrent causal events have already happened,
- verify location reachability,
- verify institution/resource state.

Authority:
- Act2 concurrency/geography/causal ledger,
- Act6 concurrency/geography/causal ledger.

No teleportation or stale route state.

---

# 9. Provenance / staleness

Projected Context is a generated execution artifact.

Mandatory refs:
- exact Episode Blueprint,
- Beat,
- Sub-Act,
- current reveal ledger,
- current asset router,
- authority map.

If any upstream structural authority changes:
- mark affected projected Context stale,
- regenerate affected fields,
- do not manually reconcile duplicated plot prose because plot prose should not be duplicated here.

Unresolved C2 names/labels use stable IDs/placeholders until approved.

---

# 10. Whole-series materialization policy

Create now:
# **EP001~410 STATIC / PROJECTED Context nodes = 410/410**

Do NOT create now:
- future actual relationship state,
- future actual physical damage state,
- future actual reader knowledge,
- future actual location availability,
- future actual open/closed device state.

Near-term runway may receive additional human-readable compilation detail, but the global 410 layer stays source-linked and drift-resistant.

---

# 11. Status lifecycle

`PROJECTED`
→ planned execution contract; actual state pending.

`STALE`
→ upstream authority changed; regeneration required.

`READY-AFTER-GATES`
→ local projected/actual opening state can be frozen, but project-level prose gate still closed.

`FROZEN`
→ JIT actual state resolved and pre-draft QA passed.

`DRAFTED`
→ prose exists but QA not fully closed.

`CONTINUITY-FROZEN`
→ prose QA closed; realized delta is authoritative input for next episode.

---

# 12. Hard failures

FAIL if:
1. Context duplicates full Episode Blueprint and becomes shadow truth,
2. projected state is described as actual current state,
3. future Immediate Continuity is invented,
4. future relationship target is treated as achieved,
5. reveal/knowledge leaks backward,
6. graph-active assets are all foregrounded,
7. Context file depth becomes >5 prompt slots,
8. Act2/6 ignores concurrency ledger,
9. H-A/H-B state inherits silently across EP094/095,
10. C2 placeholder is silently frozen,
11. every episode is forced to have a collectible beat,
12. Context alone is used as drafting source.

---

# FINAL

# **STATIC PROJECTED CONTEXT = 410/410 BUILD NOW**
# **DYNAMIC ACTUAL CONTEXT = JIT / SEQUENTIAL FREEZE**

This preserves:
- Deep Design,
- Obsidian graph traceability,
- collectibility routing,
- continuity correctness,
- Minimum Action max-5 drafting context.
