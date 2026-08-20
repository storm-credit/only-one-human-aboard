# V3 Rolling Episode Context Compilation Protocol v0.1

Status: `PREWRITING EXECUTION PROTOCOL / NOT CANON / NO PROSE`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## Purpose

Define how the already-complete 410-episode blueprint/graph is converted into episode-local drafting context without pre-freezing future continuity.

The repository already contains 410/410 episode blueprints and router nodes, 56 Beat hubs, 28 Macro Sub-Act hubs, 18 Volume hubs, 9 Act hubs, plus entity/asset routing ledgers.

Therefore:
# **DO NOT generate 410 blank context files.**
# **DO NOT pre-materialize future actual-state snapshots.**

## Runtime loop

`BLUEPRINT FORECAST`
→ `CONTEXT COMPILE`
→ `PROSE`
→ `QA`
→ `ACTUAL CONTINUITY FREEZE`
→ `NEXT CONTEXT RECOMPILE`

For EPxxx:
1. resolve exact Episode Blueprint,
2. resolve `Beat → Sub-Act → Volume → Act`,
3. load only current-authorized entity/asset/location/institution slices,
4. compile the max-5 direct Context Pack,
5. draft/QA only after Manuscript Start gates close,
6. freeze actual `Continuity Output`,
7. recompile EPxxx+1 from actual continuity.

## Context statuses

### `READY-AFTER-GATES`
Episode-local context is coherent, but prose is still blocked by project-level gates: official v3 promotion, protagonist final-name approval, explicit Manuscript Start.

### `PROVISIONAL`
Near-term runway context. MUST be recompiled after the immediately preceding episode's actual Continuity Output is frozen.

### `FROZEN`
Regenerated from actual prior continuity and passed pre-draft checks.

## Max-5 direct bundles
1. Episode Card
2. Immediate Continuity
3. POV / Relationship Microbundle
4. World / Zone / Material Microbundle
5. Active Narrative Device / Return / Collectibility Microbundle

Large bibles, 64-asset matrices and whole Act ledgers remain routers only.

## Dynamic state rule

Create a dedicated state snapshot only when physical condition, authority, relationship boundary, custody, knowledge, resource access, collectibility state, or location/network usability materially changes.

A state snapshot may cover an episode range.
Never create `410 episodes × all entities` state duplicates.

## Forecast vs actual

Blueprint Continuity Output is a forecasted target until prose/QA confirms the realized state.

If prose produces a legitimate small delta without violating authority:
- record the delta,
- freeze it as actual continuity,
- update the next Context Pack,
- do not silently rewrite far-future state nodes unless propagation requires it.

## EP001~010 runway policy

- EP001: deepest compile; `READY-AFTER-GATES`.
- EP002~010: `PROVISIONAL`.
- each future pack is recompiled after the previous episode freezes.

## Hard failures

FAIL if:
1. future Context is treated as actual continuity,
2. future knowledge leaks backward,
3. all 64 assets are loaded,
4. quiet Act1 gains a mystery clue merely to make Context useful,
5. protagonist name is silently frozen,
6. v3 prose starts before explicit gates close.

## Final

The graph is deep; drafting payload stays small.
The plan is global; current state is compiled just-in-time.
