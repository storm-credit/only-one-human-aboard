# V3 Episode Context Pack Architecture — Blind-Spot / Hostile Audit v0.1

Status: `PREWRITING CONTEXT ARCHITECTURE HOSTILE QA / PATCH REQUIRED BEFORE 410 STATIC MATERIALIZATION / NOT CANON / NO PROSE`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

Purpose:
Attack the proposed architecture:

`STATIC projected Context = EP001~410 materialized now`
`DYNAMIC actual Context = frozen sequentially immediately before drafting`

The goal is NOT to decide whether Context Packs are useful. They are required. The question is whether mass materialization creates a second blueprint, future-state contamination, context overload, graph noise, or execution drift.

---

# 0. Verdict upfront

## Direction verdict
# **STATIC 410/410 = YES, BUT ONLY AS PROJECTED EXECUTION CONTRACTS**
# **DYNAMIC ACTUAL STATE = JIT / SEQUENTIAL FREEZE ONLY**

The current EP001~010 runway proved the five-bundle model, but its copied Episode Card prose must NOT be scaled verbatim to 410 files.

New blocking P0 found: **0**.
New P1 found before patch: **12**.
All 12 are architecture/execution risks, not story-redesign requests.

---

# 1. P1 — Shadow Blueprint / duplicated story truth

Attack:
If every Context Pack copies POV, Want, A-Plot, End Turn, relationship movement and world movement from the Episode Blueprint, what happens when one side changes?

Finding:
**P1.** The repository would contain two episode-level truth surfaces.

Patch:
- exact episode plot/action remains authoritative ONLY in `EPISODE-BLUEPRINT-ACTx`;
- STATIC Context stores a link/selector to the exact episode heading, not a rewritten duplicate;
- Context stores only compiler directives, constraints, state selectors, salience budget, forecast delta and runtime placeholders.

Rule:
`Blueprint = what the episode is designed to do.`
`Context = what information may be loaded to execute it now.`

---

# 2. P1 — Forecast state mistaken for actual state

Attack:
Can an EP260 projected relationship/asset condition be mistaken for something that already happened in prose?

Finding:
**P1.** Naming both as `current state` is unsafe.

Patch namespaces:
- `projected_*` = prewriting expectation/eligibility,
- `actual_*` = realized continuity only,
- `target_delta` = desired episode output,
- `realized_delta` = post-QA result.

No STATIC field may be named `current_*` unless it is explicitly `current_at_compile_time` and generated during JIT freeze.

---

# 3. P1 — Impossible future Immediate Continuity

Attack:
How can EP300 have `Immediate Continuity` before EP299 exists as prose?

Finding:
**P1.** It cannot.

Patch:
STATIC stores:
- `forecast_incoming_carry`, sourced from blueprint/Beat,
- `actual_incoming_continuity: PENDING_PREVIOUS_ACTUAL`.

At JIT compile, actual continuity overrides forecast.

---

# 4. P1 — Relationship target confused with relationship state

Attack:
If a planned `Mira boundary softens` is stored as state, can prose accidentally start after the change rather than dramatize it?

Finding:
**P1.** Yes.

Patch:
STATIC records:
- `relationship_entry_requirement`,
- `relationship_target_delta`,
- never a future achieved relationship state.

DYNAMIC records the achieved boundary after QA.

---

# 5. P1 — Knowledge / reveal leakage backward

Attack:
Can a late Context node expose HUMAN/D3/H-A-H-B truth to an early POV merely because the graph connects to global authority?

Finding:
**P1.** Deep graph traversal can leak future knowledge.

Patch:
Each STATIC Context must include:
- `knowledge_fence_ref`,
- `reveal_phase`,
- `forbidden_forward_truth` class,
- rule: route by episode-local reveal state before following ontology links.

Special hard boundaries:
- EP001~091: no objective misbinding/H-B truth,
- EP092~094: event only, no technical explanation,
- Act3: regression hypothesis may exist but not full lineage truth,
- HUMAN definition only where Reveal Ledger permits.

---

# 6. P1 — Graph-active asset = prose-salient asset error

Attack:
If an episode routes to five assets, will prose introduce five named collectibles?

Finding:
**P1**, already observed in EP001.

Patch:
STATIC distinguishes:
- `eligible_assets`,
- `foreground_recognition_budget`,
- `background_only_assets`,
- `hold_assets`.

Default new foreground recognition:
- 0~1 preferred,
- 2 only when the scene naturally binds them as one perceptual/work unit.

`NONE` is a valid collectibility reward state.

---

# 7. P1 — Rich Context file mistaken for direct prompt payload

Attack:
Does a deep Context node violate the Minimum Action max-5 rule?

Finding:
**P1 if unpatched.** A file may contain routing metadata far beyond five items.

Patch:
- Context FILE may be deep;
- Draft PAYLOAD remains exactly the five compiled bundles;
- metadata/source links/validation fields are not extra prompt slots;
- `compile_to_payload: max_5` is mandatory frontmatter.

---

# 8. P1 — Act2 / Act6 chronology and geography drift

Attack:
Can projected packs independently place people/assets without respecting concurrent closure and travel time?

Finding:
**P1**, especially Act2 (~48~52 h) and Act6 (~8~10 weeks).

Patch:
All STATIC Context nodes in these Acts must carry:
- concurrency ledger ref,
- projected time-window ref,
- access/geography preflight requirement.

FROZEN is forbidden until the current concurrency ledger + actual prior continuity agree.

---

# 9. P1 — Boundary transition contamination

Attack:
Can H-A material/relationship state bleed into H-B after EP094? Can B12's Sub-Act split be flattened?

Finding:
**P1.** This project has unusually dangerous state boundaries.

Patch:
Hard context boundaries:
- EP001~094 lineage context = H-A,
- EP095 onward current lived context = H-B unless an explicit memory/provenance reference says otherwise,
- EP088 B12 resolves through SA-2D exactly as graph already records,
- Arun H-A memory and Arun H-B current person are separate state sources.

No Context compiler may inherit entity state across these boundaries by filename/name similarity alone.

---

# 10. P1 — 410 files become stale when authority changes

Attack:
If a blueprint, reveal ledger, asset overlay or naming freeze changes, how do we know which projected Contexts are stale?

Finding:
**P1.** Without provenance, 410 files become maintenance debt.

Patch mandatory metadata:
- `context_schema_version`,
- `blueprint_ref`,
- `beat_ref`,
- `subact_ref`,
- `reveal_ledger_ref`,
- `asset_router_ref`,
- `authority_status_at_compile`,
- `stale_if_authority_changes: true`.

Static nodes are generated artifacts. Do not hand-edit copied plot truth.

---

# 11. P1 — Overconstraint / prose becomes mechanical

Attack:
If Context contains too many `must` statements, does every episode become execution of a checklist?

Finding:
**P1.** This is a serious craft risk.

Patch directive levels:
- `MUST` = Canon/reveal/causal/continuity invariant,
- `TARGET` = designed episode delta,
- `PREFER` = salience/pacing choice,
- `MAY` = optional texture,
- `FORBID` = leakage/genre/canon failure.

Only MUST/FORBID are hard prose constraints.

---

# 12. P1 — Reader knowledge conflated with character knowledge

Attack:
A character may not know something the reader already inferred, and vice versa.

Finding:
**P1.** One generic `knowledge_state` is insufficient.

Patch DYNAMIC namespaces:
- `pov_known_actual`,
- `other_active_character_known_actual`,
- `reader_confirmed_actual`,
- `reader_suspected_optional` only if tracked operationally.

STATIC may specify fences/targets but not actual reader uptake.

---

# 13. P2 — Every episode forced to carry collectibility reward

Risk:
The collection engine could become visible machinery.

Patch:
`collectibility_job: NONE / PERSIST / BACKGROUND` is valid.
No quota at episode level. Reward cadence remains Beat/Volume/Act governed.

---

# 14. P2 — Obsidian graph visual noise

Risk:
410 Context nodes × every possible entity creates unreadable spaghetti.

Patch:
- Context node links only to active/eligible episode slices, not all 64 entities;
- broad pools remain on Beat/Sub-Act routers;
- Context→Entity links should be 0~small set, normally materialized only when actually selected or state-changing;
- MOC/filter/frontmatter supports graph filtering by `type: episode_context`, Act, Beat, status.

---

# 15. P2 — Unresolved C2 silently frozen by mass generation

Risk:
410 files copy a temporary protagonist name, venue/model term or family surface label.

Patch:
- unresolved surface values remain stable IDs/placeholders (`C01`, `[주인공/TBD]`),
- Context stores stable entity IDs first,
- reader-facing labels are resolved at JIT compile from current C2 authority.

---

# 16. P2 — Actual small delta triggers uncontrolled far-future rewrite

Risk:
A minor EP036 prose variation causes manual edits across hundreds of files.

Patch:
- projected files remain design contracts, not predicted exact actuality;
- propagate only if the realized delta changes a locked future dependency;
- otherwise the JIT compiler resolves the latest actual state locally.

Use a `propagation_required` flag only for genuine future causal dependencies.

---

# 17. P2 — Context file becomes prose outline duplication

Risk:
Writers read Context instead of Blueprint and miss nuance.

Patch:
Every Context node visibly states:
`DO NOT DRAFT FROM THIS NODE ALONE.`
Required resolution order:
`Context → exact Episode Blueprint heading → actual prior continuity → selected microbundles`.

---

# 18. Correct architecture after audit

## STATIC / PROJECTED — 410/410 materialize now
Each episode gets one Context node containing:
- stable graph identity,
- exact Blueprint selector/link,
- Act/Volume/Sub-Act/Beat ancestry,
- projected incoming carry selector,
- target delta categories,
- character/relationship selector,
- asset/location/institution eligibility selector,
- collectibility salience budget,
- reveal/knowledge fence selector,
- concurrency/geography preflight where required,
- hard MUST/FORBID constraints,
- expected outgoing carry selector,
- DYNAMIC placeholders,
- source provenance/staleness metadata.

It does NOT copy the entire episode card.

## DYNAMIC / ACTUAL — sequential JIT
At draft time freeze:
- actual incoming continuity,
- current relationship boundaries,
- actual physical/material state,
- actual location/access state,
- actual institution/network state,
- POV knowledge,
- reader-confirmed knowledge,
- active open/closed devices,
- selected foreground assets,
- exact five-bundle payload.

After prose QA:
- freeze `realized_delta`,
- update entity/state snapshots only where meaningful,
- recompile next episode.

---

# 19. 410 mass-build gate

Mass materialization may proceed ONLY if the generator/schema obeys:

1. no duplicated A-Plot prose as authority,
2. explicit PROJECTED vs ACTUAL namespace,
3. exact source/provenance links,
4. no future Immediate Continuity claim,
5. salience budget != eligibility pool,
6. max-5 compiled payload preserved,
7. Act2/6 concurrency preflight,
8. H-A/H-B and B12 boundary guards,
9. stable IDs over unresolved names,
10. no episode-level collectibility quota,
11. no Context-only drafting,
12. runtime recompile from actual continuity.

---

# FINAL VERDICT

# **STATIC 410/410 SHOULD BE BUILT.**
But it must be a **thin-but-deep projected execution graph layer**, not 410 duplicated mini-blueprints.

# **DYNAMIC ACTUAL STATE MUST NOT BE MASS-FROZEN.**
It is generated/frozen sequentially at drafting time.

After the 12 P1 architecture patches above:
- Blocking P0 = **0**
- Context architecture P1 = **0, conditional on schema enforcement**

Next correct task:
1. supersede v0.1 rolling protocol with a v0.2 STATIC/DYNAMIC schema,
2. materialize EP001~410 projected Context nodes,
3. run whole-series graph/integrity QA,
4. only later JIT-freeze EP001 actual Context after project-level prose gates close.
