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
- Change Location: Project workflow / World & Setting Bible completeness
- New: Core v1 remains stable; encyclopedic v2 completion required before prose; manuscript blocked.
- Status: `CORE v1 STABLE / ENCYCLOPEDIC v2 OPEN / MANUSCRIPT BLOCKED`

---

## CHG-034 — Narrative Engineering + Obsidian Context Atlas를 Encyclopedic Gate에 추가
- Date: 2026-08-17
- Change Location: Narrative navigation / device dependencies / context retrieval
- New: Package G established; NAM-H1 + Device Atlas + Act/Sub-Act Obsidian graph + Context Pack architecture.
- Status: `PACKAGE G STRUCTURAL GRAPH PASS / FULL PASS PENDING EP DATASET`

---

## CHG-035 — Material Culture / Equipment / Relics를 독립 완성도 Gate로 승격
- Date: 2026-08-17
- Change Location: Material culture / equipment / heritage / collection engine
- New: Package C-M established; MC-H1 + CE-H1 selected provisionally; Old ≠ powerful / Rare ≠ useful guardrails.
- Status: `PACKAGE C-M STRUCTURAL BASE PASS / CROSS-PACKAGE DEPENDENCIES OPEN`

---

## CHG-036 — Package A Society Bible 전 영역 Deep Design + 통합 Red Team 완료
- Date: 2026-08-17
- Change Location: Encyclopedic v2 / Society architecture
- Previous:
  - Society Bible had strong core rights/economy premise but lacked full reference-grade treatment of governance, criminal justice, finance/property, labor/class, family, education, general medicine and death/finality.
- New:
  - nine provisional Society models selected after separate 4-design comparisons and hostile tests:
    1. `GOV-H1 — Layered Civic Republic + Commons Constraints + Narrow Safety Command`
    2. `CJ-H1 — Layered Public Safety + Restorative Default + Narrow Coercive Escalation`
    3. `ECO-H1 — Civic Floor + Monetary Market + Capacity Commons + Mixed Enterprise`
    4. `PROP-H1 — Layered Residential Tenure + Common Structure + Transferable Household Interests`
    5. `LAB-H1 — Open Occupational Mobility + Plural Worker Power + Safety-Credential Boundaries`
    6. `FAM-H1 — Civil Partnership + Independent Parenthood + Protected Dependency + Flexible Household`
    7. `EDU-H1 — Common Civic Foundation + Choice-Rich Adolescence + Apprenticeship / Higher Training + Lifelong Modular Retraining`
    8. `MED-H1 — Universal Clinical Floor + Advanced Biological Repair + Privacy-Bounded Prevention + Supported Autonomy`
    9. `DEATH-H1 — Clinical Death + Continuity Review + Bounded Legal Finality + Material Return + Plural Mourning`
  - integrated `SOCIETY-BIBLE-v0.1.md` created.
  - integrated Society hostile Red Team completed with blocking P0 = 0.
  - Package A judged `STRUCTURAL DEEP DESIGN = PASS` but NOT Canon-frozen because B/C/D/E/F dependencies remain.
- Reason:
  - user requires a standalone reference-grade world/setting bible before manuscript.
  - a random citizen's whole life must be possible without improvising major social rules.
- Trigger / Evidence:
  - direct continued user instruction on 2026-08-17.
  - all `docs/design-v2/SOCIETY-*-4-DESIGNS-v0.1.md`
  - all matching `docs/qa/SOCIETY-*-RED-TEAM-v0.1.md`
  - `docs/design-v2/SOCIETY-BIBLE-v0.1.md`
  - `docs/qa/SOCIETY-BIBLE-INTEGRATED-RED-TEAM-v0.1.md`
- Characters Affected:
  - Maren/Ella/Noah family legal architecture clarified without changing existing Canon chronology.
  - Amara/Leo/Kai/Mina ordinary family/work/school rights clarified without origin privilege.
  - Tomas retirement, Ines healthcare role, Jun property/labor context gain reference support.
- Acts Affected:
  - all Acts gain ordinary society detail and consequence logic.
  - no Act order, Count/Meaning/Amara reveal timing or ending architecture changed.
- Foreshadowing Affected:
  - no new ontology clue or universal MacGuffin.
  - social rules may become local episode context only when relevant.
- World Rules Affected:
  - broad provisional expansion only; v1 core personhood/Seed/Reconstruction/destination rules unchanged.
- Key Cross-Package Guardrails:
  - democratic governance cannot become expert/AI sovereignty.
  - engineering telemetry cannot become universal citizen surveillance.
  - money cannot legally purchase birth/Reconstruction/critical survival priority.
  - citizens may hold valuable housing interests without owning hull/life-support sovereignty.
  - person continuity does not automatically roll back lawful third-party property change.
  - careers are chosen; civilization steers needed skills rather than assigning lives.
  - partnership/parenthood/guardianship/property are distinct.
  - future medicine does not abolish disability, aging or death.
  - clinical death / Reconstruction review / legal finality / mourning / inheritance are distinct.
- Documents Created/Repaired:
  - all Package A Society design and QA files listed in `docs/current-work-status.md`
  - `docs/design-v2/SOCIETY-BIBLE-v0.1.md`
  - `docs/qa/SOCIETY-BIBLE-INTEGRATED-RED-TEAM-v0.1.md`
  - `docs/current-work-status.md`
- Status:
  - `PACKAGE A STRUCTURAL DEEP DESIGN = PASS`
  - `PACKAGE A CANON v2 PROMOTION = BLOCKED BY CROSS-PACKAGE DEPENDENCIES`
  - `MANUSCRIPT = BLOCKED`

---

# Current Change-Control Rule

Core v1 is a stable baseline, but v2 completeness expansion is active.

For every meaningful new design:
`3~4 designs → compare → blind-spot/trap check → Hybrid → Red Team → status judgment`.

If new material contradicts v1:
- do not silently overwrite
- add a new CHG entry
- identify affected Character / Act / Foreshadow / World rules
- regression-test affected Episode Cards

Narrative Engineering maps remain metadata/index/QA; Canon/active Blueprint/M1/POV override them.
Material Culture and Society v0.1 remain provisional until cross-package integration.

Do not draft manuscript until:
`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`.
