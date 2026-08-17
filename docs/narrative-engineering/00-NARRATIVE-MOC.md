# 00 — Narrative Engineering MOC

Status: `PACKAGE G DESIGN = PASS / P0=0 / MANUSCRIPT-READY SUPPORT LAYER / NOT CANON`

Project: 《우주선에는 인간이 한 명뿐이다》

Current project gate:
- `ENCYCLOPEDIC CANON FREEZE v2 = PASSED — 2026-08-18`
- `MANUSCRIPT = READY / NOT STARTED`
- Accepted = `0/230`.

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

Blocking P0: **0**.

## Current Story Authorities

- [World Bible v2](../../canon/WORLD_BIBLE-v2.md) — CANON
- [Character Bible v2](../../canon/CHARACTER_BIBLE-v2.md) — CANON
- [Act Bible v1](../../canon/ACT_BIBLE-v1.md) — ACTIVE NARRATIVE CANON
- active Episode Blueprints
- [M1 Time/Age Harness](../writing-ready/HARNESS-M1-TIME-AGE-v0.1.md)
- locked POV Maps
- applicable Deep Cards
- [Prose Protocol v1.1](../writing-ready/PROSE-EXECUTION-PROTOCOL-v1.1.md)

Act6 Blueprint v0.2 is active; v0.1 is superseded.

## Authority Rule

Narrative Engineering is a **map / retrieval / QA layer**, not Canon.

Authority order:

`Canon v2 → active Episode Blueprint → locked POV Map → M1 → applicable Deep Card → full-series Manifest Registry → Sub-Act candidate map`.

Narrative Engineering may never silently override an authority above it.

## Current Obsidian Graph State

Completed:
- 1 Series MOC
- 7 Act nodes
- 23 Sub-Act nodes
- Device Atlas
- cross-Sub-Act lifecycle map
- Context Pack schema
- knowledge-fence model
- full EP001~230 Registry
- full-series POV/reveal/knowledge regression.

Individual authored example notes:
- `EP001~028` = 28 detailed examples.
- `EP029~230` = not individually split.

This is intentional.
The remaining split is mechanical implementation work, not incomplete Deep Design.

## Critical Device Rule

**Sub-Act candidate ≠ episode exposure.**

A Sub-Act device is only eligible in the range.
It enters an episode Context Pack only when exact Blueprint / Deep Card / locked ledger supports that episode-level work.

Known repairs:
- MG-01 Seed clue starts SA-1B / EP012~013, not SA-1A.
- EP014 transit fault is not TK-01.
- EP026 routine repair scarcity is not CK-01.
- invalid early IDs are repaired/overridden by v0.2 addendum.

## Retrieval Target

For any episode:

`EP → Sub-Act → Act → exact Blueprint → exact POV → M1 → relevant Deep Card → relevant World-v2 / Character-v2 / Location / Device → incoming carry → future AUTHOR constraint`.

Do not load the entire repository or full global Canon into POV context by default.

## Implementation Contract — Later

Claude Code / Obsidian tooling may mechanically generate:
`episodes/EP-029.md` ... `EP-230.md`.

Generated notes must:
- derive from Registry,
- fetch exact Blueprint card,
- fetch exact POV/M1,
- preserve AUTHOR / POV / PUBLIC / PROTECTED separation,
- calculate device exposure from episode-explicit authority only,
- fail closed on ambiguity,
- create no new Canon.

Optional Dataview is allowed; plain Markdown/YAML/wikilinks remain sufficient.

## Package G Verdict

- `STRUCTURAL GRAPH = PASS`
- `EP001~230 DESIGN REGISTRY = 230/230 PASS`
- `POV / REVEAL / KNOWLEDGE-FENCE REGRESSION = PASS`
- `BLOCKING P0 = 0`

# `PACKAGE G NARRATIVE ENGINEERING = PASS / SUPPORT LAYER READY`

The former v2 completeness manuscript block is closed. Prose still starts only when manuscript execution is explicitly initiated.
