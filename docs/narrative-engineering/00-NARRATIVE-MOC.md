# 00 — Narrative Engineering MOC

Status: `PACKAGE G DESIGN = PASS / P0=0 / PRE-PROSE / NOT CANON`

Project: 《우주선에는 인간이 한 명뿐이다》

## Act Navigation

- [ACT-01 — 돌아온 사람들의 자리](./acts/ACT-01.md)
- [ACT-02 — 판정의 비용](./acts/ACT-02.md)
- [ACT-03 — 한 명이라는 숫자](./acts/ACT-03.md)
- [ACT-04 — 공개된 다음 날](./acts/ACT-04.md)
- [ACT-05 — 미래를 위해 현재를 뜯는 법](./acts/ACT-05.md)
- [ACT-06 — 두 고향](./acts/ACT-06.md)
- [ACT-07 — 도착은 판정이 아니다](./acts/ACT-07.md)

All **7 Act nodes / 23 Sub-Act nodes** exist.

## Core Narrative Engineering

- [Narrative Map Architecture — 4 Designs](./NARRATIVE-MAP-ARCHITECTURE-4-DESIGNS-v0.1.md)
- [Narrative Device Atlas](./NARRATIVE-DEVICE-ATLAS-v0.1.md)
- [Act / Sub-Act Narrative Device Map](./ACT-SUBACT-NARRATIVE-DEVICE-MAP-v0.1.md)
- [Repair Addendum v0.2](./NARRATIVE-ENGINEERING-REPAIR-ADDENDUM-v0.2.md)
- [Obsidian Link + Context Pack Spec](./OBSIDIAN-LINK-CONTEXT-PACK-SPEC-v0.1.md)
- [EP001~230 Context Manifest Registry](./EP001-230-CONTEXT-MANIFEST-REGISTRY-v0.1.md)

## QA

- [Initial Narrative Engineering Map Red Team](../qa/NARRATIVE-ENGINEERING-MAP-RED-TEAM-v0.1.md)
- [Full EP001~230 Manifest Regression](../qa/NARRATIVE-ENGINEERING-FULL-MANIFEST-REGRESSION-v0.1.md)

Final design-layer blocking P0: **0**.

## Existing Story Authorities

- [Act Bible](../../canon/ACT_BIBLE-v1.md)
- [World Bible](../../canon/WORLD_BIBLE-v1.md)
- [Character Bible](../../canon/CHARACTER_BIBLE-v1.md)
- [Foreshadow / Payoff Ledger](../act/FORESHADOW-PAYOFF-LEDGER-4-DESIGNS-v0.1.md)
- [Information Ladder](../act/INFORMATION-LADDER-4-DESIGNS-v0.1.md)
- [M1 Time/Age Harness](../writing-ready/HARNESS-M1-TIME-AGE-v0.1.md)
- [POV Maps](../writing-ready/ACT1-EXECUTION-POV-MAP-v1.md)

## Authority Rule

Narrative Engineering documents are a **map / retrieval / QA layer**.

Authority order:

`Canon → active Episode Blueprint → locked POV Map → M1 → applicable Deep Card → full-series Manifest Registry → Sub-Act candidate map`.

Narrative Engineering may never silently override an authority above it.

## Current Obsidian Graph State

Completed design layer:
- 1 Series MOC
- 7 Act nodes
- 23 Sub-Act nodes
- Device Atlas
- cross-Sub-Act device lifecycle map
- Context Pack schema
- knowledge-fence model
- full EP001~230 Manifest Registry
- full-series POV/reveal/knowledge regression

Individual authored episode notes:
- `EP001~028` = 28 detailed example manifests.
- `EP029~230` = **not individually split yet**.

This is intentional.
Individual split is mechanical implementation work and is not required to claim design-data completion.

## Critical Device Rule

**Sub-Act candidate ≠ episode exposure.**

A device listed in a Sub-Act's `active_devices` is only eligible in that range.
It enters an episode Context Pack only if the exact Blueprint / Deep Card / locked ledger supports that episode-level work.

Known over-tag repairs remain active:
- MG-01 Seed clue starts SA-1B / EP012~013, not SA-1A.
- EP014 transit fault is not TK-01.
- EP026 routine repair scarcity is not CK-01.
- invalid early IDs are repaired/overridden by the v0.2 addendum.

## Retrieval Target

For any episode:

`EP → Sub-Act → Act → exact Blueprint → exact POV → M1 → relevant Deep Card → relevant Canon/Character/Location/Device → incoming carry → future constraint`

The writing agent should not receive the entire repository by default.

## Implementation Contract — Later

Claude Code / Obsidian tooling may mechanically create:
`episodes/EP-029.md` ... `EP-230.md`

Generated notes must:
- derive from the Registry,
- retrieve the exact Episode Blueprint card,
- retrieve exact locked POV and M1,
- preserve AUTHOR / POV / PUBLIC / PROTECTED knowledge separation,
- calculate device exposure from episode-explicit authority only,
- fail closed on missing/ambiguous authority,
- create no new Canon.

Optional Dataview is allowed later, but plain Markdown/YAML/wikilinks remain sufficient.

## Package G Verdict

`STRUCTURAL GRAPH = PASS`

`EP001~230 DESIGN REGISTRY = 230/230 PASS`

`POV / REVEAL / KNOWLEDGE-FENCE REGRESSION = PASS`

`BLOCKING P0 = 0`

Overall:

**`PACKAGE G NARRATIVE ENGINEERING DESIGN = PASS / NOT CANON`**

Manuscript remains blocked until the full Encyclopedic Canon Freeze v2 gate passes.
