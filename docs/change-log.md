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
- New: GOV-H1 / CJ-H1 / ECO-H1 / PROP-H1 / LAB-H1 / FAM-H1 / EDU-H1 / MED-H1 / DEATH-H1 / integrated Society Bible.
- Integrated blocking P0: 0
- Status: `PACKAGE A STRUCTURAL DEEP DESIGN PASS / NOT CANON`

---

## CHG-037 — Package B Culture & Daily Life 전 영역 Deep Design + 통합 Red Team 완료
- Date: 2026-08-17
- New:
  - LNG-H1 language
  - REL-H1 religion/ritual
  - CAL-H1 civil/voyage time
  - FOOD-H1 cuisine/hospitality
  - CLO-H1 clothing/fashion
  - DOM-H1 domestic life
  - MEDIA-H1 media/social networks
  - ENT-H1 entertainment/art/sport
  - INT-H1 intimacy/social norms
  - ID-HOME-H1 Meridian-home identity
  - integrated `CULTURE-DAILY-LIFE-BIBLE-v0.1.md`
- Integrated blocking P0: 0
- Status: `PACKAGE B STRUCTURAL DEEP DESIGN PASS / NOT CANON`

---

## CHG-038 — Package C Infrastructure & Operations 전 영역 Deep Design + 통합 Red Team 완료
- Date: 2026-08-17
- Change Location: Encyclopedic v2 / physical city / infrastructure / automation / information / operations
- Previous:
  - Core Canon had ship-scale engineering, three Habitats, living-world ranges, civil power/heat/ecology, but lacked reference-grade everyday infrastructure architecture.
  - Package B assumed normal homes/showers/media/leisure but exact physical implementation was open.
- New:
  - ten provisional Infrastructure models selected after 4-design comparison + hostile QA:
    1. `URB-H1 — Compartmented Mixed-Use City + Layered Retrofit + Local Public Realms`
    2. `TRANS-H1 — Walkable Polycentric Habitats + Local Trunks + Spine Express + Separated Freight`
    3. `UTIL-H1 — Hierarchical Commons Loops + District Isolation + Domestic Abstraction`
    4. `EMG-H1 — Layered Incident Command + Automatic Physical Safeties + Human Escalation`
    5. `AI-H1 — Federated Domain Intelligence + Bounded Personal Agents + Heavy Tool Automation + Human Accountability`
    6. `NET-H1 — Redundant Civic Backbone + Segmented Critical Domains + Permissioned Gateways + Local Fallback`
    7. `ARC-H1 — Federated Current Registries + Deep Versioned Archives + Curated Knowledge Commons + Protected Provenance Layers`
    8. `OPS-H1 — Commons Asset Ownership + Mixed Skilled Workforce + Predictive Maintenance + Formal Work Control`
    9. `MAP-H1 — Dual Civic / Engineering Overlay + Landmark Graph + Travel-Time Matrix`
    10. `BIO-PET-H1 — Selective Companion Species + Managed Breeding + Veterinary Commons + Genetic Conservation + Strong Biosecurity`
  - integrated `INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md` created.
  - integrated hostile QA completed with blocking P0 = 0.
- Major results:
  - ~120k–130k household city is structurally compatible with current ship scale.
  - Civic Floor housing does not erase market differences in space/location/privacy.
  - 60–120m cross-Habitat travel is preserved as realistic door-to-door multi-leg travel.
  - normal showers/cooking/laundry coexist with highly efficient closed-loop water/thermal systems.
  - most utility/transit incidents remain local through layered isolation; serious cascades remain possible.
  - emergency authority is hazard-scoped and time-limited.
  - no central sovereign ship AI / no universal citizen score / no autonomous civic adjudication or lethal policing.
  - critical networks are segmented and locally survivable.
  - archives preserve old schemas/provenance without a single master truth database.
  - Count aggregate and identity access are architecturally separated, preserving Amara privacy/re-identification logic.
  - permanent maintenance/fabrication/calibration/training institutions explain 450-year survivability.
  - civic map and engineering isolation map coexist as separate overlays.
  - selected companion species are plausible while broader biodiversity is primarily genetically archived.
- Reason:
  - user's encyclopedic standard requires arbitrary infrastructure/daily/emergency scenes to work without inventing major rules during prose.
- Characters Affected:
  - Amara's water/reclamation work gains realistic automation/operator role.
  - Jun's contractor/co-op maintenance role gains asset/inspection/work-control framework.
  - Kai's Spine logistics apprenticeship gains real routing/exception/hazard work.
  - Noah's school/residential/transit/sport environment gains physical implementation.
  - no character arc changed.
- Acts Affected:
  - Act 1 Spine delay/Old Quarter/2환 scenes physically supported.
  - Acts 2–4 archive/privacy/Count/re-identification infrastructure supported.
  - Act 5 strategic spares/thermal/maintenance conflicts strengthened.
  - Acts 6–7 relocation/arrival logistics supported.
  - no Act timing/reveal/ending change.
- Foreshadowing Affected:
  - no new ontology device.
  - infrastructure/object recurrence remains distinct from narrative-device tagging.
- World Rules Affected:
  - provisional expansion only; Core v1 propulsion/Seed/Reconstruction/rights remains unchanged.
- Key documents:
  - `docs/design-v2/INFRA-*-4-DESIGNS-v0.1.md`
  - matching `docs/qa/INFRA-*-RED-TEAM-v0.1.md`
  - `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`
  - `docs/qa/INFRASTRUCTURE-OPERATIONS-BIBLE-INTEGRATED-RED-TEAM-v0.1.md`
  - `docs/current-work-status.md`
- Status:
  - `PACKAGE C STRUCTURAL DEEP DESIGN = PASS`
  - `PACKAGE C CANON v2 PROMOTION = BLOCKED BY D/E/F + QUANTITATIVE QA`
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

Packages A/B/C/C-M and Package G map layer remain provisional until v2 cross-package integration.

Do not draft manuscript until:
`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`.
