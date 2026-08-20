---
id: MOC-V3-CONTEXT-PACK
type: moc
---
# Episode Context Pack MOC

## Whole-series architecture

Every episode now has one STATIC / PROJECTED Context node:
`[[contexts/CTX-V3-EP001]]` → … → `[[contexts/CTX-V3-EP410]]`.

Registry / audit:
- [[contexts/V3-410-PROJECTED-CONTEXT-MANIFEST]]
- [[PROJECTED-CONTEXT-NODE-TEMPLATE-v0.1]]
- [[../prewriting-v3/V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.2]]
- [[../qa/V3-410-PROJECTED-CONTEXT-INTEGRITY-QA-v0.1]]

STATIC / PROJECTED is a source-linked execution contract, not a second Episode Blueprint.
DYNAMIC / ACTUAL remains `PENDING` until JIT pre-draft compilation.

## EPxxx resolution

`Context Node`
→ exact Episode Blueprint selector
→ actual previous Continuity
→ Beat / Macro Sub-Act / Volume / Act
→ current POV/relationship state
→ current world/zone/material state
→ active reveal/payoff/collectibility state
→ max-5 drafting payload.

Hard:
- DO NOT draft from Context node alone.
- eligibility does not equal foreground salience.
- future projected state is never Actual.
- Act2 and Act6 require concurrency/geography preflight before FROZEN.
- EP094 H-A current-lived state does not auto-inherit into EP095 H-B.

## Direct prompt cap

1. Episode Card
2. Immediate Continuity
3. POV/Relationship State
4. World/Zone/Material State
5. Active Device/Return/Collectibility State

Graph depth is retrieval topology, not prompt bulk.

## Runtime loop

`Projected Context`
→ actual prior continuity load
→ JIT Dynamic freeze
→ max-5 compile
→ prose
→ QA
→ realized continuity freeze
→ next Context recompile.

EP001 may become `READY-AFTER-GATES`; later Contexts remain PROJECTED until their actual predecessor is frozen.
