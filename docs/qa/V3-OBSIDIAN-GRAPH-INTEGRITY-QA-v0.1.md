# V3 Obsidian Graph Integrity QA v0.1

Status: `GRAPH STRUCTURE QA / PASS CANDIDATE / NOT CANON`
Date: 2026-08-20

## Expected physical/logical graph
- Grand Series MOC: 1
- Act hubs: 9
- Execution Volume hubs: 18
- Macro Sub-Act hubs: 28
- Beat/Execution hubs: 56
- Episode router nodes: 410
- Collectible/IP entity nodes: 64 = C13 + M15 + P12 + L12 + W12
- Institution/network/governance nodes: 9 = INST6 + NET2 + GOV1

## Hierarchy coverage
EP001~410 is covered continuously by Acts, Volumes, Macro Sub-Acts and Beats.
No Volume cuts through a Macro Sub-Act.
Known exception B12 crosses SA-2C/SA-2D and is explicitly split at EP088 in Episode frontmatter.

## Authority safety
- old v2 `docs/narrative-engineering/` graph remains historical and is not overwritten,
- new v3 graph lives under `docs/obsidian-v3/`,
- graph nodes route to exact v3 Blueprint/ledgers and do not create Canon,
- Official Canon remains v2 until explicit promotion.

## Context safety
Deep graph != giant prompt.
A real episode still loads max five direct bundles:
1 Episode Card
2 Immediate Continuity
3 POV/Relationship State
4 World/Zone/Material State
5 Active Device/Return/Collectibility State

## Collectibility safety
64 asset nodes can all exist in graph while prose reader-facing terminology remains capped.
HOLD / NO-CHEKHOV / OFFSTAGE are valid states.
HUMAN:1 is not converted into collectible-character logic.

## Reader-fun cross-check
Companion QA `V3-CROSS-SYSTEM-READER-FUN-COLLECTIBILITY-RED-TEAM-v0.1` found and patched:
1. missing Act→Volume→Sub-Act→Beat→Episode middle layer,
2. V13/V15/V16 spectator-protagonist risk,
3. ensemble cognitive overload risk.

Final graph verdict:
# `STRUCTURAL GRAPH = PASS CANDIDATE`
# `EP ROUTERS = 410/410 MATERIALIZED`
# `BLOCKING GRAPH P0 = 0`
# `GRAPH/ROUTING P1 = 0 after targeted patches`

Empirical Obsidian UI visualization is optional implementation validation; it does not reopen story design.