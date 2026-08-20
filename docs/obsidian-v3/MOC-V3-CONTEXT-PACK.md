---
id: MOC-V3-CONTEXT-PACK
type: moc
---
# Episode Context Pack MOC

## Whole-series architecture

Every v3 episode has two intentionally separate projected execution layers:

1. thin router: `[[contexts/CTX-V3-EP001]]` → … → `[[contexts/CTX-V3-EP410]]`;
2. deep sidecar: `[[deep-contexts/DEEP-V3-EP001]]` → … → `[[deep-contexts/DEEP-V3-EP410]]`.

Current coverage:
- Thin Router = **410/410**.
- Deep Projected Context = **410/410**.
- Dynamic Actual = **PENDING / JIT**.

Registry / audit:
- [[contexts/V3-410-PROJECTED-CONTEXT-MANIFEST]] — thin-router manifest only.
- [[deep-contexts/V3-410-DEEP-PROJECTED-CONTEXT-MANIFEST-v1]] — Deep manifest.
- [[../prewriting-v3/DEEP-CONTEXT-SCHEMA-v1]]
- [[../prewriting-v3/V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.2]]
- [[../qa/V3-DEEP-CONTEXT-ACT-BY-ACT-QA-v1]]
- [[../qa/V3-DEEP-CONTEXT-WHOLE-SERIES-RED-TEAM-v1]]
- [[../qa/V3-DEEP-CONTEXT-COMPLETION-GATE-v1]]

Neither projected layer is a second Episode Blueprint.
DYNAMIC / ACTUAL remains `PENDING` until JIT pre-draft compilation from realized continuity.

## EPxxx resolution

`Exact Episode Blueprint`
→ `thin CTX Router`
→ `DEEP PROJECTED Context`
→ actual previous Continuity
→ JIT Dynamic freeze
→ max-5 drafting payload.

The Deep node may route to Beat/Macro Sub-Act/Volume/Act and current relationship/world/asset/reveal sources, but it may not pre-freeze future Actual state.

Hard:
- DO NOT draft from a projected Context node alone.
- eligibility does not equal foreground salience.
- future projected state is never Actual.
- Act2 and Act6 require concurrency/geography preflight before FROZEN.
- EP094 H-A current-lived state does not auto-inherit into EP095 H-B.
- Act7~8 action/evidence precedes ontology.
- HUMAN:1 is de-collectified.
- EP406~410 are closure/return and cannot open a new major mystery.

## Direct prompt cap

1. Episode Card
2. Immediate Continuity
3. POV/Relationship State
4. World/Zone/Material State
5. Active Device/Return/Collectibility State

Graph depth is retrieval topology, not prompt bulk.

## Runtime loop

`Blueprint + Router + Deep Projected`
→ actual prior continuity load
→ JIT Dynamic freeze
→ max-5 compile
→ prose
→ QA
→ realized continuity freeze
→ next Context recompile.

EP001 may become `READY-AFTER-GATES`; later Deep Contexts remain PROJECTED until their actual predecessor is frozen.
