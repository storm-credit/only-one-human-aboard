# Design Change Log — Active

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Historical Archives

### CHG-001~026
- archive pointer: `docs/change-log-archive-001-026.md`

### CHG-027~032
The immediately previous active log is preserved in Git history.
- immutable previous blob SHA: `586c6fd1a6d03009a297a13a78df61cfb47efd7b`
- last entry: `CHG-032 — Full-series POV architecture + Protocol v1.1 보정`

This file continues from CHG-033.

---

## CHG-033 — 사용자 품질기준 상향: Encyclopedic Deep Design Gate 신설 / 원고 재잠금
- Date: 2026-08-17
- New: Core v1 remains stable; encyclopedic v2 completion required before prose.
- Status: `CORE v1 STABLE / ENCYCLOPEDIC v2 OPEN / MANUSCRIPT BLOCKED`

---

## CHG-034 — Narrative Engineering + Obsidian Context Atlas 추가
- Date: 2026-08-17
- New: Package G / NAM-H1 / Device Atlas / Act-SubAct graph / Context Pack architecture.
- Status: `STRUCTURAL GRAPH PASS / FULL DATASET PENDING`

---

## CHG-035 — Material Culture / Equipment / Relics 독립 Gate 승격
- Date: 2026-08-17
- New: Package C-M / MC-H1 / CE-H1; Old ≠ powerful; Rare ≠ useful.
- Status: `STRUCTURAL BASE PASS / CROSS-PACKAGE DEPENDENCIES OPEN`

---

## CHG-036 — Package A Society Bible 전 영역 Deep Design + 통합 Red Team 완료
- Date: 2026-08-17
- New:
  - GOV-H1
  - CJ-H1
  - ECO-H1
  - PROP-H1
  - LAB-H1
  - FAM-H1
  - EDU-H1
  - MED-H1
  - DEATH-H1
  - `SOCIETY-BIBLE-v0.1.md`
- Integrated blocking P0: 0
- Status: `PACKAGE A STRUCTURAL DEEP DESIGN PASS / NOT CANON`

---

## CHG-037 — Package B Culture & Daily Life 전 영역 Deep Design + 통합 Red Team 완료
- Date: 2026-08-17
- Change Location: Encyclopedic v2 / lived culture / ordinary daily life
- Previous:
  - core setting had strong technical/social premise but many ordinary cultural domains were incomplete: language drift, belief, calendar, actual cuisine, clothing, hygiene, media, leisure, intimacy and ship-born identity.
- New:
  - ten provisional cultural models selected after design comparison + hostile QA:
    1. `LNG-H1 — Evolved Ship Common + Heritage Language Ecology + Translation Assist`
    2. `REL-H1 — Plural Inherited Traditions + Secular Life + Ship-Born Civic Rituals + Small New Movements`
    3. `CAL-H1 — Synchronized Earth-Descended Civil Time + Voyage-Epoch Archival Time + Ship-Born Observance Calendar`
    4. `FOOD-H1 — Closed-Loop Staples + Heritage Recipe Lineages + Ship-Born Adaptation + Real Hospitality Market`
    5. `CLO-H1 — Recognizable Civilian Fashion + Closed-Loop Textiles + Specialized Workwear + Selective Wearables`
    6. `DOM-H1 — Urban Comfort + High-Efficiency Closed Loops + Repairable Domestic Systems + Selective Automation`
    7. `MEDIA-H1 — Public-Service Information + Plural Journalism/Creators + Interoperable Social Layer + Bounded Recommenders`
    8. `ENT-H1 — Layered Heritage + Ship-Born Creative Canon + Live/Physical Culture + Bounded Immersion`
    9. `INT-H1 — Plural Adult Intimacy + Strong Consent/Privacy + Reproduction Decoupled From Partnership`
    10. `ID-HOME-H1 — Meridian-Home Majority + Layered Heritage + Contested Mission Memory + Plural Arrival Futures`
  - integrated `CULTURE-DAILY-LIFE-BIBLE-v0.1.md` created.
  - integrated Package B hostile QA completed with blocking P0 = 0.
  - ordinary rest-day / child / elder daily-life prototypes pass structurally without new Package-B-scale invention.
- Reason:
  - user's quality bar requires the setting bible itself to function as a complete world reference before prose.
  - the society must feel like a 450-year civilian civilization, not only a story-critical legal/engineering framework.
- Trigger / Evidence:
  - direct continued user instruction.
  - `docs/design-v2/CULTURE-*-4-DESIGNS-v0.1.md`
  - matching `docs/qa/CULTURE-*-RED-TEAM-v0.1.md`
  - `docs/design-v2/CULTURE-DAILY-LIFE-BIBLE-v0.1.md`
  - `docs/qa/CULTURE-DAILY-LIFE-BIBLE-INTEGRATED-RED-TEAM-v0.1.md`
- Characters Affected:
  - no locked arc changed.
  - Noah's zero-g sport/media/music/game life receives a plausible cultural base.
  - Ella's hospitality/food co-op receives actual cuisine/hospitality ecology.
  - Amara's shift work gains shift-time/food/media/home context.
  - all cast can later receive individualized language/belief/taste/clothing/hobby/media/home routines in Package F.
- Acts Affected:
  - all Acts gain daily-life and cultural texture only.
  - Count media diffusion/re-identification path strengthened without altering reveal timing.
  - arrival/ship-home choices gain cultural weight without changing ending.
- Foreshadowing Affected:
  - no new ontology clue.
  - recurring cultural/place/object details are not automatically Chekhov devices.
- World Rules Affected:
  - provisional expansion of everyday culture only; core v1 remains unchanged.
- Key Guardrails:
  - Korean prose is natural translation convention; no faux translated-English cadence.
  - translation tools cannot solve institutional semantic drift.
  - no single religion owns Seed/Natural truth.
  - 24h/7d/Earth-derived civil calendar retained as infrastructure; ship-born observances evolve.
  - citizens eat real cuisine, not default nutrient paste.
  - civilians wear fashion, not universal jumpsuits.
  - closed-loop sustainability is built into domestic infrastructure, not daily misery.
  - no single media feed or perfect truth AI.
  - Earth archive does not erase 450 years of Meridian-created culture.
  - population capacity does not justify regulation of private adult intimacy.
  - Meridian is actual home; surface is not automatically more authentic.
- Documents Created/Repaired:
  - all Package B design/QA files listed in `docs/current-work-status.md`
  - `docs/design-v2/CULTURE-DAILY-LIFE-BIBLE-v0.1.md`
  - `docs/qa/CULTURE-DAILY-LIFE-BIBLE-INTEGRATED-RED-TEAM-v0.1.md`
  - `docs/current-work-status.md`
- Status:
  - `PACKAGE B STRUCTURAL DEEP DESIGN = PASS`
  - `PACKAGE B CANON v2 PROMOTION = BLOCKED BY C/D/E/F DEPENDENCIES`
  - `MANUSCRIPT = BLOCKED`

---

# Current Change-Control Rule

Core v1 remains stable baseline.

For meaningful new design:
`3~4 designs → compare → blind-spot/trap check → Hybrid → hostile Red Team → status judgment`.

If new material contradicts v1:
- do not silently overwrite
- add CHG entry
- identify affected Character / Act / Foreshadow / World rules
- regression-test affected Episode Cards.

Package A/B/C-M and Package G map layer remain provisional until v2 cross-package integration.

Do not draft manuscript until:
`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`.
