# Design Change Log — Active

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Historical Archives

### CHG-001~026
- archive pointer: `docs/change-log-archive-001-026.md`

### CHG-027~032
- previous history preserved in Git history
- prior immutable blob reference: `586c6fd1a6d03009a297a13a78df61cfb47efd7b`

### CHG-033~042
- archive pointer: `docs/change-log-archive-033-042.md`
- covers Encyclopedic gate opening, Packages A~G/C-M structural passes, Character Encyclopedia and full EP001~230 Context Registry.

---

## CHG-043 — Package H Reference Atlas + Package I Final Completeness Harness 완성
- Date: 2026-08-18
- Change Location:
  - `docs/reference-atlas/`
  - `docs/qa/FINAL-COMPLETENESS-*`
  - `docs/qa/RANDOM-SCENE-FUZZ-20-v0.1.md`
  - `docs/qa/FINAL-CANON-STORY-REGRESSION-v0.1.md`
- Previous:
  - Packages A~G had structural/design passes, but there was no final current/superseded authority atlas and no arbitrary-scene completeness proof.
- New:
  - `REF-H1` Reference Atlas built with 13/13 required views.
  - Atlas separates human-readable navigation from current authority and prevents Shadow Canon.
  - actual stale Package-F support-name defect discovered and repaired.
  - `FC-H1` Final Completeness Harness created.
  - deterministic citizen/lifecycle/crime/emergency/class/family/school/media/culture/AI/arrival/material suites PASS.
  - **20/20 arbitrary random-scene fuzz tests PASS** without a new major civilization rule.
  - full Canon/story/Reveal/POV regression PASS.
- Blocking P0: **0**.
- Status:
  `PACKAGE H = PASS / PACKAGE I = PASS / FINAL P1 LEDGER EXPOSED`.

---

## CHG-044 — Final MUST-CLOSE P1 closure
- Date: 2026-08-18
- Change Location:
  - `docs/design-v2/P1-Q-SHIP-QUANTITATIVE-CLOSURE-v0.2.md`
  - `docs/design-v2/P1-Q-DEST-SCIENCE-LOGISTICS-CLOSURE-v0.2.md`
  - `docs/design-v2/P1-LEGAL-OPERATIONAL-POLICY-GRAMMAR-CLOSURE-v0.1.md`
  - `docs/design-v2/P1-CULTURE-HISTORY-SPORT-SUPPORT-CLOSURE-v0.2.md`
  - corresponding hostile QA files.
- Previous:
  - core architecture existed, but final reference-grade ranges/policy grammars/examples remained open.
- New — Q-SHIP:
  - Habitat radius 0.9–1.1 km, 5–7 km length order, ~0.9–1.0g, ~0.9–1.0 rpm.
  - explicit internally compartmented pressure architecture; no giant undivided air cylinder.
  - pressure/refuge/transfer/water/power/thermal/workforce/spare working bands selected.
- New — Q-DEST:
  - Epsilon Indi A retained as real star anchor; rocky settlement world remains future fictional mission-era discovery.
  - ~0.50–0.54 AU / ~150–165d / ~0.93–1.02g / ~28–31h.
  - near-Earth pressure with oxygen far below safe breathing; outdoor breathing support mandatory but normal pressure EVA unnecessary.
  - high planetocentric Meridian staging orbit, resource transfer/cargo/power/Year-1 population bands selected.
- New — legal/operational:
  - `AGE-H1` 18-year civil majority + staged youth autonomy.
  - `DATA-H1` purpose-class retention + protected provenance + versioned correction.
  - `FORCE-H1` closed-habitat T0~T4 dangerous-tool/force tiers.
  - `STRIKE-H1` strike right + minimum life-safety service + rapid neutral review.
  - `ARRLAW-H1` shared civic baseline + location/service nexus + staged local competence.
  - `BIO-H1` quarantine/contained living systems + outdoor release moratorium during ending window.
- New — culture/history/support:
  - small recurring observance/food/idiom/art set.
  - six representative historical anchors.
  - `REBOUND-H1` repeatable low/zero-g sport model.
  - 14 stable-if-used C1 support anchors; Sorin Das/Yuna Bekele remain C2 reserve.
  - civic-equality holiday/history wording repaired so it does not leak EP059~066 Meaning.
- Blocking P1 remaining: **0**.
- Status:
  `P1 CLOSURE = PASS / READY FOR CANON v2 CONSOLIDATION`.

---

## CHG-045 — Encyclopedic Canon Freeze v2 / World+Character 정본 승격 / 원고 게이트 해제
- Date: 2026-08-18
- Change Location:
  - `canon/WORLD_BIBLE-v2.md`
  - `canon/CHARACTER_BIBLE-v2.md`
  - `docs/qa/ENCYCLOPEDIC-CANON-v2-FINAL-RED-TEAM.md`
  - `canon/CANON_STATUS.md`
  - `docs/current-work-status.md`
  - `docs/manuscript/MANUSCRIPT-STATUS.md`
  - `CLAUDE.md`
  - `docs/NEXT-CHAT-HANDOFF.md`
  - `docs/reference-atlas/*` authority/status navigation.
- Previous:
  - World/Character v1 remained formal Canon while A~I/P1 v2 material was candidate/supporting design.
  - manuscript was blocked by the stronger encyclopedic completeness gate.
- New:
  - final hostile regression checked World/Character v2 against v1 Canon, Act Bible, all active Blueprints, Act6 v0.2, M1, POV maps, Package G Registry and final Harness.
  - blocking P0 = **0**.
  - blocking P1 = **0**.
  - Reveal moved = NO.
  - POV architecture changed = NO.
  - core character arcs changed = NO.
  - ending architecture changed = NO.
  - Shadow Canon unresolved = NO.
  - **`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`**.
  - `canon/WORLD_BIBLE-v2.md` promoted to **CANON**.
  - `canon/CHARACTER_BIBLE-v2.md` promoted to **CANON**.
  - `canon/WORLD_BIBLE-v1.md` / `CHARACTER_BIBLE-v1.md` become historical/superseded reference.
  - `canon/ACT_BIBLE-v1.md` remains ACTIVE because macro narrative did not change.
  - manuscript state changes from `BLOCKED` to **`READY / NOT STARTED`**.
  - Accepted manuscript remains **0 / 230**; first eligible episode = EP001.
- Milestone:
  `docs/status/ENCYCLOPEDIC-CANON-FREEZE-v2-PASS-2026-08-18.md`
- Status:
  **`DESIGN/WORLD/SETTING-BIBLE COMPLETE / CANON v2 FROZEN / MANUSCRIPT READY`**.

---

# Current Change-Control Rule

Current world/character authority:
- `canon/WORLD_BIBLE-v2.md`
- `canon/CHARACTER_BIBLE-v2.md`

Current narrative authority:
- `canon/ACT_BIBLE-v1.md`
- active Blueprint
- locked POV Map
- M1
- applicable Deep Card / Context Registry.

For contradiction-level change after Freeze v2:
`identify issue → alternatives/impact → CHG entry → hostile Red Team → affected-episode regression → deliberate Canon reopening/promotion`.

Never silently overwrite v2 Canon from prose.

C2 refinement inside frozen ranges is allowed, but recurring/clue-bearing/causal C2 must be promoted/logged before manuscript acceptance.

Current manuscript state:
**`READY / NOT STARTED`**.
