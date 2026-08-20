---
id: MOC-V3-CONTEXT-PACK
type: moc
---
# Episode Context Pack MOC

For EPxxx resolve:
1. exact Episode Card,
2. Beat Hub,
3. Macro Sub-Act Hub,
4. Volume/Act intent,
5. POV+relationship state,
6. zone/material state,
7. active reveal/payoff/collectibility state.

Direct prompt payload remains max 5 context bundles. Graph depth is retrieval structure, not prompt bulk.

## Runtime compilation

Do NOT generate 410 blank Context files or freeze future actual-state snapshots.

Use:
- [[EPISODE-GRAPH-CONTEXT-PACK-SPEC-v0.1]] for logical pack shape,
- [[../prewriting-v3/V3-ROLLING-EPISODE-CONTEXT-COMPILATION-PROTOCOL-v0.1]] for just-in-time compilation,
- [[../prewriting-v3/context-packs-v3/EP001-010-CONTEXT-RUNWAY-v0.1]] for the initial runway.

Runtime loop:
`Blueprint forecast → Context compile → prose → QA → actual continuity freeze → next Context recompile`.

EP001 may be `READY-AFTER-GATES`; future runway packs remain `PROVISIONAL` until the previous episode's actual continuity is frozen.
