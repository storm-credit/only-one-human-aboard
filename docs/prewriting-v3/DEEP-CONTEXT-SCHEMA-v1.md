# DEEP CONTEXT SCHEMA v1

Status: `FROZEN FOR EP001~410 DEEP PROJECTED COMPILE / NO PROSE / NOT CANON`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

Companion audit:
`docs/qa/V3-DEEP-PROJECTED-CONTEXT-BLIND-SPOT-AUDIT-v1.md`

Protocol authority:
`docs/prewriting-v3/V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.2.md`

---

# 0. Ownership and precedence

This schema materializes **deep projected execution context**, not plot authority and not Canon.

Authority order on conflict:
1. current authority map / locked upstream source,
2. exact Episode Blueprint,
3. thin `CTX-V3-EPxxx` router for ancestry/branch/concurrency routing,
4. this deep projected node,
5. future JIT Dynamic Actual state.

A deep node must never overwrite an exact Episode Blueprint event merely to make its own projection consistent.

Existing `CTX-V3-EP001~410` nodes remain the **THIN ROUTER 410/410** layer.
New `DEEP-V3-EP001~410` nodes are a separate **DEEP PROJECTED** layer.

---

# 1. Required frontmatter

```yaml
---
id: DEEP-V3-EPxxx
type: deep_projected_context
episode: EPxxx
router: CTX-V3-EPxxx
schema: DEEP-CONTEXT-SCHEMA-v1
context_kind: DEEP_PROJECTED
projection_semantics: FORECAST_NOT_ACTUAL
dynamic_actual: PENDING
branch_state_namespace: H-A | H-B
cross_branch_inheritance: BLOCKED_UNLESS_EXPLICIT
microbundle_compile_cap: 5
source_snapshot:
  protocol: V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.2
  blueprint: <exact Act blueprint>
  router: CTX-V3-EPxxx
stale_if_changed:
  - <router>
  - <blueprint>
  - <relevant character/relationship/asset/concurrency authority>
---
```

Hard:
- `PENDING` means unknown future realized state.
- `NONE_AUTHORIZED` means intentionally no active item.
- never use `NONE` when a realized fact is merely unknown.

## Two node states (CHG-057)

A node is in exactly one of two states, and the **frontmatter must declare which**.
This declaration is the guard that prevents a forecast from silently becoming actual continuity.

| State | `projection_semantics` | `dynamic_actual` | six `realized_*` fields |
|---|---|---|---|
| Forecast (default) | `FORECAST_NOT_ACTUAL` | `PENDING` | all six **must** be `PENDING` |
| Realized (post-acceptance) | `REALIZED_FROM_ACCEPTED_PROSE` | `REALIZED` | all six **must** carry actual values |

Transition happens **only after** the episode's prose is accepted. A node may declare
`REALIZED` only if `manuscript/v3/accepted/actXX/EPxxx.md` actually exists — `tools/deep_context_integrity.py`
enforces this, so the claim cannot be made on an undrafted episode.

Realized content is compiled from the accepted prose, not from the forecast. Where the two
disagree, **the prose is what happened** and the forecast was simply a projection.

The next episode's node consumes this through Retrieval lane 2 (`Immediate Continuity`), which is
why lane 2 is specified as `actual/JIT + forecast` rather than forecast alone.

---

# 2. Section contract

Every node contains all section headings below. A section may use `NONE_AUTHORIZED` when genuinely inactive.

## 2.1 Structural Inheritance

Required fields:
- `series_job`
- `act_job`
- `volume_reward`
- `subact_input_state`
- `subact_target_state`
- `beat_execution_job`
- `exact_blueprint_ref`
- `router_ancestry_ref`

Rule:
compress **why this episode exists inside the hierarchy**. Do not copy the A-Plot or scene sequence.

Volume/Sub-Act/Beat IDs are inherited from the thin router. The deep node must not recalculate ancestry.

## 2.2 Projected Incoming

Required:
- `previous_episode_forecast`
- `previous_beat_carry`
- `subact_entry_condition`
- `projected_continuity`

All values are explicitly forecast unless already established by locked upstream state.

## 2.3 Protagonist Context

Required:
- `projected_goal`
- `pov_known`
- `pov_unknown`
- `projected_judgment`
- `direct_action_requirement`
- `agency_requirement`
- `must_not_solve`
- `flaw_pressure`

If POV is not protagonist, protagonist state may be `INFLUENCE_ONLY`, but the series-level agency line must still remain intact.

## 2.4 Character Context

Use:
```text
active_core: 0~3 normally, including POV
influence_only: any source-justified offstage causal pressure
```

For each active character:
- `projected_want`
- `independent_agenda`
- `projected_entry_state`
- `episode_function`
- `scene_salience`
- `causal_edges`
- `appearance_mode: ONSTAGE | OFFSTAGE_INFLUENCE`
- `projected_delta`

Hard:
- graph connection does not mandate appearance;
- no token cameo merely to preserve a character link;
- use the current v3 character authority, never remembered names from earlier iterations.

## 2.5 Relationship Context

For each active relationship:
- `entry_baseline`
- `tension`
- `trust_or_boundary`
- `mutual_known`
- `hidden_or_unshared`
- `projected_target_delta`
- `absolute_forbid`

Hard:
`projected_target_delta` must not be copied into `entry_baseline` for the same episode.

## 2.6 World / Location Context

Required:
- `location_ref`
- `projected_function`
- `spatial_use`
- `movement_constraints`
- `access_constraints`
- `change_since_previous_use`
- `scene_job`
- `sensory_life_texture`
- `projected_zone_condition`

World texture should support lived civilization, not become an exposition dump.

## 2.7 Asset / Collectibility Context

For each relevant asset:
- `asset_ref`
- `projected_lifecycle: INTRODUCE | RECOGNIZE | RECONTEXTUALIZE | TRANSFORM | PERSIST | DAMAGE | RETIRE | HOLD | NO-CHEKHOV`
- `projected_owner_or_user`
- `last_meaningful_appearance`
- `projected_condition`
- `expected_next_return`
- `eligibility: ELIGIBLE | INELIGIBLE`
- `salience: FOREGROUND | BACKGROUND | HOLD`
- `collectibility_job: <job> | NONE`

Hard:
- `eligible != foreground`;
- new foreground recognition 0~1 preferred;
- 2 only when naturally perceived/used as one functional unit;
- no per-episode collection quota;
- fiction function outranks merchandise potential;
- future realized damage/ownership/relocation remains projection only.

## 2.8 Institution / Faction / Network Context

For each active institution/network:
- `projected_authority`
- `projected_resources`
- `influence_edges`
- `conflict_edges`
- `projected_operating_state`
- `episode_change_target`
- `independent_causality`

`NONE_AUTHORIZED` is valid in purely personal/local episodes.

## 2.9 Mystery / Reveal / Knowledge Fence

Required typed lanes:
- `world_truth_reference`
- `pov_known`
- `character_known`
- `reader_confirmed`
- `reader_suspected`
- `allowed_reveal`
- `forbidden_future_reveal`

Default:
`world_truth_reference: SEALED_LINK_ONLY`.

Do not write author-side ontology prose into a node merely because the system knows it.

H-A/H-B:
- current-lived state is namespaced by branch;
- same name/face/function never grants automatic current-state inheritance;
- H-A memories inside H-B are provenance objects, not H-B current facts.

## 2.10 Foreshadow / MacGuffin / Payoff

Fields:
- `active_chain`
- `previous_touch`
- `current_touch_purpose`
- `current_phase`
- `next_planned_touch`
- `payoff_target`
- `ordinary_event_guard`

All may be `NONE_AUTHORIZED` where appropriate.

Hard:
ordinary accidents, life texture and maintenance events stay ordinary unless an upstream source explicitly assigns a chain.

## 2.11 Genre Engine

Required:
- `primary_engine`
- `secondary_engine`
- `action_obligation`
- `exposition_ceiling`

Allowed engines include:
`mystery / thriller / survival / investigation / civic-social / relationship / exploration / ordinary-life / procedural`.

Act-specific hard gates:
- Act1: ordinary life/procedural remains primary until upstream escalation;
- Act2: survival/concurrency/geography must remain executable;
- Acts7~8: `action_before_ontology: REQUIRED`;
- Act9: `late_new_ontology: FORBID` by default;
- EP406~410: closure/return dominates; no new major mystery chain.

## 2.12 Execution Constraints

Exactly five lanes:
- `MUST`
- `TARGET`
- `PREFER`
- `MAY`
- `FORBID`

Only `MUST` and `FORBID` are hard prose constraints.

A deep node should keep hard constraints few enough to be executable.

## 2.13 Forecast Outgoing

Required:
- `projected_relationship_delta`
- `projected_knowledge_delta`
- `projected_material_delta`
- `projected_world_institution_delta`
- `projected_asset_lifecycle_delta`
- `next_episode_carry`

These fields are never Actual continuity.

## 2.14 Dynamic Actual Placeholder

Always:
```text
realized_relationship_delta: PENDING
realized_knowledge_delta: PENDING
realized_material_delta: PENDING
realized_world_institution_delta: PENDING
realized_asset_lifecycle_delta: PENDING
actual_next_episode_carry: PENDING
```

No future node may prefill these values.

## 2.15 Retrieval Compile Map

Direct drafting payload stays max 5:

1. `Episode Card`
   - exact Blueprint selector only.
2. `Immediate Continuity`
   - Projected Incoming + later JIT Actual carry.
3. `POV / Relationship Microbundle`
   - protagonist + active character + relationship blocks.
4. `World / Zone / Material Microbundle`
   - location + institution + material/asset condition required for scenes.
5. `Active Device / Return / Collectibility Microbundle`
   - knowledge fence + active foreshadow/payoff + only selected salient assets.

Deep graph is retrieval infrastructure. It is never injected wholesale as one giant prompt.

---

# 3. Concurrency contract

## Act2
If the router or episode blueprint touches concurrent disaster lanes:
- load `V3-ACT2-CONCURRENCY-GEOGRAPHY-CAUSAL-LEDGER-v0.1.md`;
- declare active zone/thread scope;
- preserve elapsed-time plausibility;
- no character teleportation;
- protagonist may provide technical evidence but may not absorb security/medical/logistics command.

## Act6
If concurrent resource/network lanes are active:
- load the current Act6 concurrency/resource/network ledger;
- declare causal owners per thread;
- preserve scarcity and travel/communication constraints;
- ensemble causality must not erase protagonist agency.

---

# 4. STALE propagation

A deep node becomes `STALE` when any source in `stale_if_changed` materially changes.

Safe automatic actions:
- detect upstream SHA/path change,
- mark node `STALE`,
- rebuild ancestry pointers,
- run link/count/schema checks.

Never automate without semantic review:
- reveal permissions,
- relationship baseline/delta,
- current-lived branch state,
- character independent agenda,
- asset foreground choice,
- Actual continuity.

---

# 5. Golden-sample gate

Before EP011~410 expansion:
1. compile EP001~010 with this schema;
2. run hostile QA for all mandatory audit dimensions;
3. require `P0=0`, `P1=0`;
4. confirm direct compile stays within five microbundles;
5. confirm `dynamic_actual=PENDING` in all ten;
6. confirm no Shadow Blueprint.

Only then may batch expansion proceed Act1→Act9.

---

# 6. Freeze verdict

This file is the schema authority for the current Deep Projected Context build.

# `DEEP-CONTEXT-SCHEMA-v1 = FROZEN`
# `THIN ROUTER AUTHORITY PRESERVED`
# `FUTURE DYNAMIC ACTUAL = JIT ONLY`
