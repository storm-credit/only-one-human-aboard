# V3 DEEP PROJECTED CONTEXT — BLIND-SPOT AUDIT v1

Status: `PRE-SCHEMA HOSTILE AUDIT / P0=0 AFTER PATCH / P1=0 AFTER PATCH / NO PROSE / NOT CANON`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. Audit scope

This audit is the mandatory gate before materializing `EP001~410 DEEP PROJECTED CONTEXT`.

Authority recovered from current `main` at `0fc8ccc35eb06054d85987847f02b8fc6931c1fb`:
- `docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md`
- `canon/ACT_BIBLE-v3.2-CANDIDATE.md`
- `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md`
- exact Act-specific `EPISODE-BLUEPRINT-ACT*-v0.1.md`
- `docs/prewriting-v3/V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.2.md`
- `docs/prewriting-v3/V3-CORE-CAST-ACT-ROLE-MATRIX-v0.1.md`
- current relationship / asset / return / concurrency ledgers
- current Obsidian graph and existing `CTX-V3-EP001~410` router layer.

The existing `CTX-V3-EP001~410` layer is treated as **THIN PROJECTED ROUTER / EXECUTION CONTRACT**, not as the deep per-episode state compilation requested here.

Hard source-recovery rule:
**chat memory, old handoff wording, previous model summaries, and pre-v3 names are never authority when they conflict with current GitHub.**

---

# 1. Blocking findings found before schema freeze

| ID | Initial | Finding | Patch | State |
|---|---|---|---|---|
| P0-01 | P0 | `410/410 projected context complete` can mean either thin router completion or deep context completion. This can create a false project-complete state. | Reserve `ROUTER 410/410` for existing nodes and `DEEP PROJECTED CONTEXT 410/410` for the new sidecar layer only. Completion docs must state both separately. | CLOSED |
| P0-02 | P0 | Existing thin template does not type every future state as forecast vs realized fact. A mass-expanded node could silently turn projection into Actual continuity. | New schema requires `context_kind: DEEP_PROJECTED`, `projection_semantics: FORECAST_NOT_ACTUAL`, field-level `PROJECTED_*` labels, and immutable `dynamic_actual: PENDING` before JIT freeze. | CLOSED |
| P0-03 | P0 | Thin branch/concurrency guard strings alone are insufficient once detailed character/relationship/knowledge state is added. Cross-lineage state or sealed truth could leak through detailed fields. | New schema adds `branch_state_namespace`, `cross_branch_inheritance`, `knowledge_fence`, `world_truth_reference: SEALED/LINK_ONLY` default, `allowed_reveal`, `forbidden_future_reveal`, plus Act2/Act6 concurrency scope. | CLOSED |
| P1-01 | P1 | EP001~010 runway references Protocol v0.1 and predates the current v0.2 compile rules. | Golden sample must be recompiled against v0.2 and this schema; old runway remains provenance only or is superseded. | CLOSED |
| P1-02 | P1 | Pilot Episode Cards duplicate A-Plot/turn fields closely enough to become a Shadow Blueprint. | Deep context may summarize structural job/state but may not restage beat sequence or own A-Plot truth; exact Blueprint remains the only episode event authority. | CLOSED |
| P1-03 | P1 | Relationship forecast can be mistaken for already-earned trust/intimacy/boundary change. | Relationship block separates `entry_baseline`, `projected_target_delta`, `absolute_forbid`; future target never enters `entry_baseline`. | CLOSED |
| P1-04 | P1 | Asset lifecycle projection can pre-confirm future damage, ownership or relocation. | Every future asset field is `PROJECTED`; realized owner/condition is supplied only by Dynamic Actual. | CLOSED |
| P1-05 | P1 | POV-known, character-known, reader-confirmed and reader-suspected states are not explicit in thin nodes. | Mandatory typed knowledge-fence block. | CLOSED |
| P1-06 | P1 | Graph-active assets can accidentally become prose-foreground assets. | `eligible`, `foreground`, `background`, `HOLD` are separate. Foreground recognition target is 0~1; 2 only as one natural unit. `collectibility_job: NONE` is valid. | CLOSED |
| P1-07 | P1 | A collectible beat can become a per-episode quota and distort ordinary-life prose. | No collectible quota; the Context may explicitly state `NONE`. Fictional function outranks IP salience. | CLOSED |
| P1-08 | P1 | Deep context can overpopulate scenes with all graph-connected cast. | `active_core` defaults to max 3 salient characters including POV; `influence_only` is separate and does not imply appearance. Exceptions require Blueprint/ledger justification. | CLOSED |
| P1-09 | P1 | Protagonist may absorb all independent causality during compilation. | Protagonist block requires agency plus a `must_not_solve` field; character/institution blocks preserve at least one independent causal owner where upstream design contains one. | CLOSED |
| P1-10 | P1 | Ordinary accidents and lifestyle texture can be misclassified as foreshadowing. | Foreshadow block allows `NONE`; `ordinary_event_guard` explicitly marks mundane events that must remain mundane. | CLOSED |
| P1-11 | P1 | Deep graph size can break the max-5 direct drafting payload rule. | Every node contains a Retrieval Compile Map that maps deep fields into the fixed five microbundles. No sixth direct bundle is permitted. | CLOSED |
| P1-12 | P1 | Upstream edits can leave rich sidecars silently stale. | Source snapshot + `stale_if_changed` list required; no automatic semantic regeneration. | CLOSED |
| P1-13 | P1 | Act7~8 ontology/personhood exposition can replace mystery-thriller-survival action. | Genre block requires `action_before_ontology` for Acts7~8 and preserves a concrete action engine. | CLOSED |
| P1-14 | P1 | Act9 can become a late-setting/product/reveal exhibition. | Act9 contexts default `late_new_ontology: FORBID`; EP406~410 are closure/return biased and may not open fresh major mystery chains. | CLOSED |
| P2-01 | P2 | `NONE` fields can be treated as incomplete rather than intentional. | Schema distinguishes `NONE_AUTHORIZED` from `PENDING`. | CLOSED |
| P2-02 | P2 | Same episode can have multiple useful zones/institutions and encourage giant bundles. | Only scene-relevant projected state is compiled; deep links may remain retrieval references. | CLOSED |
| P2-03 | P2 | Current v3 protagonist is unnamed and old names can re-enter from historical summaries. | Use `[주인공/TBD]` exactly until current authority changes; never infer a name. | CLOSED |

After these patches, schema-freeze gate result:
- `P0 OPEN = 0`
- `P1 OPEN = 0`
- `P2 OPEN = 0` for generation-blocking items.

---

# 2. Mandatory 25-point audit checklist

| # | Required check | Severity if violated | v1 control | Gate |
|---:|---|---|---|---|
| 1 | Context becomes Shadow Blueprint | P1 | structural compression only; Blueprint owns event truth | PASS |
| 2 | Blueprint copied unnecessarily | P1 | no beat-by-beat duplication | PASS |
| 3 | Projected mistaken for Actual | P0 | forecast typing + `dynamic_actual: PENDING` | PASS |
| 4 | Future relationship state pre-earned | P1 | baseline vs projected delta split | PASS |
| 5 | Future asset damage/move/access pre-earned | P1 | projected lifecycle fields only | PASS |
| 6 | POV knowledge mixed with Reader knowledge | P1 | typed knowledge fence | PASS |
| 7 | World Truth leaks early | P0 | sealed/link-only world truth by default | PASS |
| 8 | Every graph-active asset foregrounded | P1 | eligibility/salience split | PASS |
| 9 | Collectibility reward forced each episode | P1 | `collectibility_job: NONE` valid | PASS |
| 10 | Character cognitive load explodes | P1 | active-core cap + influence-only | PASS |
| 11 | Too many core actors per scene | P1 | max-3 default unless source justifies | PASS |
| 12 | Protagonist owns every causal line | P1 | independent agenda/causal owner preserved | PASS |
| 13 | Supporting cast independent action disappears | P1 | character/institution independent-action field | PASS |
| 14 | Act2/Act6 concurrency violates time/space | P0 | concurrency scope + required ledger preflight | PASS |
| 15 | Wrong Sub-Act inherited at boundary | P0 | thin router remains ancestry authority; deep sidecar links rather than recomputes | PASS |
| 16 | H-A→H-B state auto-merges | P0 | branch namespace + cross-branch block | PASS |
| 17 | Reveal chain becomes too dense | P1 | allowed reveal budget; `NONE` legal | PASS |
| 18 | Mundane failure/life event becomes clue | P1 | ordinary-event guard | PASS |
| 19 | Context size breaks max-5 | P1 | fixed Retrieval Compile Map | PASS |
| 20 | Upstream change cannot propagate STALE | P1 | source snapshot / stale list | PASS |
| 21 | Deep Context conflicts with Episode Blueprint authority | P0 | Blueprint precedence explicit | PASS |
| 22 | IP/collectibility outranks fiction | P1 | fiction-first hard rule | PASS |
| 23 | Act7~8 philosophy replaces action | P1 | action-before-ontology hard guard | PASS |
| 24 | Act9 becomes new-setting exhibition | P1 | late-new-ontology forbidden by default | PASS |
| 25 | New mystery is created after ending closure begins | P1 | closure-only late gate | PASS |

---

# 3. Architecture decision from audit

Do **not** overwrite or delete the existing 410 thin router nodes.

Materialize a separate deep layer:

`docs/obsidian-v3/deep-contexts/DEEP-V3-EP001.md` ... `DEEP-V3-EP410.md`

Each deep node:
- points to its existing `CTX-V3-EPxxx` router,
- inherits exact Act/Volume/Sub-Act/Beat ancestry from that router,
- points to the exact Episode Blueprint,
- compiles only projected execution state and fences,
- leaves every future realized state `PENDING`.

This physical separation is the main patch for P0-01 and P1-02.

Graph becomes:

`Episode → thin CTX Router → DEEP PROJECTED Context → JIT Dynamic Actual → Prose → Actual Continuity`

The old router stays stable and reversible.

---

# 4. Hostile generation invariants

A generated deep node FAILS if any of the following is true:
1. it narrates the episode instead of constraining context;
2. it contains a future realized fact not already true at entry;
3. it exposes sealed ontology merely because author-side truth is known;
4. it imports a character/name/state from chat memory rather than current GitHub authority;
5. it marks every eligible asset as foreground;
6. it requires a sixth direct drafting bundle;
7. it lets a relationship target masquerade as baseline;
8. it lets an Act2/Act6 participant appear outside plausible concurrent geography;
9. it lets H-A state become H-B current state without an explicit convergence/provenance rule;
10. it upgrades Context into Canon.

---

# 5. Audit verdict

Pre-patch finding: `P0=3 / P1=14 / P2=3`.

All generation-blocking findings are patched by the companion `DEEP-CONTEXT-SCHEMA-v1` rules before any 410 expansion.

# `SCHEMA FREEZE MAY PROCEED`
# `P0 OPEN = 0`
# `P1 OPEN = 0`
