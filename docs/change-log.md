# Design Change Log — Active

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Historical Archives

### CHG-001~026
- archive pointer: `docs/change-log-archive-001-026.md`
- original full-history blob noted in prior archive

### CHG-027~032
The immediately previous active log is preserved in Git history.
- immutable previous blob SHA: `586c6fd1a6d03009a297a13a78df61cfb47efd7b`
- last entry: `CHG-032 — Full-series POV architecture + Protocol v1.1 보정`

This file continues from CHG-033.

---

## Template

### CHG-XXX — 제목
- Date:
- Change Location:
- Previous:
- New:
- Reason:
- Trigger / Evidence:
- Characters Affected:
- Acts Affected:
- Foreshadowing Affected:
- World Rules Affected:
- Documents Repaired:
- Status:

---

### CHG-033 — 사용자 품질기준 상향: Encyclopedic Deep Design Gate 신설 / 원고 재잠금
- Date: 2026-08-17
- Change Location: Project workflow / World & Setting Bible completeness
- Previous:
  - Core Design Freeze v1 = PASSED
  - Core Canon Freeze v1 = PASSED
  - Structural Writing Ready = PASSED
  - EP001~230 Blueprint/POV/QA complete
  - manuscript could begin on explicit request
- New:
  - Existing v1 Canon remains a stable core baseline.
  - New higher quality bar introduced: the design blueprint/worldbuilding/setting bible itself must become reference-grade and encyclopedically complete before prose.
  - `ENCYCLOPEDIC DEEP DESIGN = IN PROGRESS / BLOCKED`
  - `ENCYCLOPEDIC CANON FREEZE v2 = NOT PASSED`
  - `MANUSCRIPT = BLOCKED`
  - Initial required Packages A~H established: Society; Culture/Daily Life; Infrastructure/Operations; 450y History; Destination/Arrival; Character Encyclopedia v2; Reference Atlas; Final Completeness Harness.
  - Final v2 pass requires random-citizen/day, life-cycle, crime/emergency, class/disability, family lifecycle, media/privacy, culture/religion/leisure, AI/automation, arrival property/migration, random-scene no-new-rule tests, and regression against EP001~230.
- Reason:
  - The existing project was structurally writable and logic-consistent, but `WORLD_BIBLE-v1` and `CHARACTER_BIBLE-v1` intentionally left many everyday/cultural/institutional domains partial or elastic.
  - User explicitly prefers finishing the design/world/setting bible to a much higher completeness standard before manuscript drafting.
- Trigger / Evidence:
  - direct user instruction on 2026-08-17
  - `docs/qa/ENCYCLOPEDIC-DEEP-DESIGN-COMPLETENESS-AUDIT-v0.1.md`
  - audit identified major completeness gaps in governance detail, criminal justice, economy deep layer, family/education/general medicine/death, language/religion/calendar/cuisine/clothing/media/leisure, everyday AI, 450-year history, atlas/reference artifacts, and character encyclopedia depth.
- Characters Affected:
  - all recurring cast eventually through Package F; locked core origins/arcs remain unchanged unless separately approved.
- Acts Affected:
  - all Acts only through regression/texture unless a new contradiction appears.
  - Act/Reveal/Ending architecture remains locked baseline.
- Foreshadowing Affected:
  - no immediate factual change; all new v2 rules must be checked against existing Information/Foreshadow ledgers.
- World Rules Affected:
  - broad expansion of previously unspecified everyday social/cultural/institutional rules.
  - core v1 ontology/Seed/Reconstruction/destination/rights rules remain stable baseline.
- Documents Repaired:
  - `CLAUDE.md`
  - `canon/CANON_STATUS.md`
  - `docs/current-work-status.md`
  - `docs/qa/ENCYCLOPEDIC-DEEP-DESIGN-COMPLETENESS-AUDIT-v0.1.md`
  - `docs/manuscript/MANUSCRIPT-STATUS.md` (to reflect prose block)
  - `docs/NEXT-CHAT-HANDOFF.md`
- Status:
  - `CORE v1 STABLE / ENCYCLOPEDIC v2 OPEN / MANUSCRIPT BLOCKED`

---

### CHG-034 — Narrative Engineering + Obsidian Context Atlas를 Encyclopedic Gate에 추가
- Date: 2026-08-17
- Change Location: Narrative architecture navigation / foreshadow-device dependency / future Obsidian retrieval
- Previous:
  - 7 Acts / 23 Sub-Acts / EP001~230 Blueprint already existed.
  - Information Ladder and Foreshadow/Payoff Ledger already contained hard clues, world residue, character tells, MacGuffins and fair red herrings.
  - However there was no unified Act→Sub-Act device map and no Obsidian/context-retrieval graph for selecting only episode-relevant material.
- New:
  - Encyclopedic packages expanded from initial A~H layout to **A~I**.
  - Package F remains `Character Encyclopedia v2`.
  - new **Package G = Narrative Engineering & Obsidian Context Atlas**.
  - old Reference Atlas shifts to Package H.
  - Final Completeness Harness shifts to Package I.
  - four map architectures compared; `NAM-H1 — Hierarchical MOC + Cross-Linked Device Atlas + Episode Context Manifest` selected.
  - major device families assigned stable IDs.
  - all 23 Sub-Acts mapped to Plant / Reinforce / Trigger / Payoff / Aftershock work.
  - 7 Act Obsidian nodes + 23 Sub-Act nodes created.
  - `CP-H1` minimal Episode Context Pack schema defined with AUTHOR / POV / PUBLIC / PROTECTED knowledge separation.
  - interim hostile Red Team passed structural foundation with remaining EP-level blockers.
- Reason:
  - user explicitly requested that MacGuffin and other narrative devices be inspectable by Act/Sub-Act and later linkable through Obsidian so only necessary context is supplied to a writing agent.
  - existing ledgers proved device logic existed, but did not provide a single navigable dependency layer.
- Trigger / Evidence:
  - direct user request on 2026-08-17.
  - `docs/act/FORESHADOW-PAYOFF-LEDGER-4-DESIGNS-v0.1.md`
  - `canon/ACT_BIBLE-v1.md`
  - `docs/narrative-engineering/*`
  - `docs/qa/NARRATIVE-ENGINEERING-MAP-RED-TEAM-v0.1.md`
- Characters Affected:
  - no character Canon changed; Maren/Ella/Noah/Amara/Raul and others gain explicit device/dependency links only.
- Acts Affected:
  - all 7 Acts / all 23 Sub-Acts as navigation/QA metadata.
  - no Act order/reveal/ending change.
- Foreshadowing Affected:
  - existing signals consolidated into stable lifecycle IDs.
  - no new larger ontology twist added.
  - MG-01 Origin Audit / MG-02 Ella Preference Record / MG-03 Arrival Registry Stack explicitly constrained from becoming universal truth keys.
- World Rules Affected:
  - none; map layer cannot override Canon.
- Documents Repaired/Created:
  - `docs/narrative-engineering/00-NARRATIVE-MOC.md`
  - `docs/narrative-engineering/NARRATIVE-MAP-ARCHITECTURE-4-DESIGNS-v0.1.md`
  - `docs/narrative-engineering/NARRATIVE-DEVICE-ATLAS-v0.1.md`
  - `docs/narrative-engineering/ACT-SUBACT-NARRATIVE-DEVICE-MAP-v0.1.md`
  - `docs/narrative-engineering/OBSIDIAN-LINK-CONTEXT-PACK-SPEC-v0.1.md`
  - `docs/narrative-engineering/acts/ACT-01~07.md`
  - `docs/narrative-engineering/subacts/SA-1A~7C.md`
  - `docs/qa/NARRATIVE-ENGINEERING-MAP-RED-TEAM-v0.1.md`
  - `docs/qa/ENCYCLOPEDIC-DEEP-DESIGN-COMPLETENESS-AUDIT-v0.2.md`
  - `docs/current-work-status.md`
- Status:
  - `PACKAGE G STRUCTURAL GRAPH FOUNDATION = PASS`
  - `PACKAGE G FULL PASS = BLOCKED BY EP001~230 CONTEXT MANIFEST + EP-LEVEL QA`

---

### CHG-035 — Material Culture / Equipment / Relics를 독립 완성도 Gate로 승격
- Date: 2026-08-17
- Change Location: Encyclopedic Setting Bible / material culture / equipment / heritage / collection engine
- Previous:
  - weapons, equipment, historical artifacts, heirlooms and collectibles were scattered implicitly across Infrastructure, Culture, History and Act-level strategic assets.
  - no single reference layer prevented scene-by-scene invention or `old object = secret lore key` drift.
- New:
  - mandatory cross-cutting **Package C-M = Material Culture / Equipment / Relics Bible** added without renumbering stabilized A~I packages.
  - four material-culture models compared.
  - `MC-H1 — Layered Material Ecology + Selective Heritage Objects` selected as provisional base.
  - object ecology O1~O5 defined: ordinary cycle goods / durable personal goods / professional-controlled equipment / strategic commons assets / heritage-provenance objects.
  - provenance states defined by evidence and restoration history rather than RPG rarity rank.
  - weapon/public-safety direction set as a closed-habitat safety/legal problem, not a combat progression system.
  - Earth-origin objects, voyage-era artifacts, family heirlooms, museums, collectibles, salvage and strategic heritage become explicit design domains.
  - collection pleasure is defined as recognition → provenance → return → completion, not loot → power progression.
  - Material Culture-specific adversarial tests added to the final completeness gate.
- Reason:
  - user explicitly asked whether weapons/relics/equipment and collection-worthy material objects must be part of the complete setting bible.
  - a 450-year 300k-person civilization would otherwise remain materially underdesigned despite strong macro world logic.
- Trigger / Evidence:
  - direct user instruction on 2026-08-17.
  - `docs/material-culture/MATERIAL-CULTURE-EQUIPMENT-RELICS-4-DESIGNS-v0.1.md`
  - `docs/material-culture/MATERIAL-CULTURE-BIBLE-v0.1.md`
  - `docs/qa/MATERIAL-CULTURE-EQUIPMENT-RELICS-RED-TEAM-v0.1.md`
- Characters Affected:
  - none locked yet; recurring personal objects remain deferred to Character Encyclopedia v2.
  - future candidates may support Ella/Noah/Jun/Amara and ordinary supporting cast without becoming character gimmicks.
- Acts Affected:
  - Act 1~4 primarily through everyday texture / heirloom / work equipment.
  - Act 5~7 through strategic machinery, heritage/function conflicts and arrival transfer.
  - no Act ordering or reveal architecture changed.
- Foreshadowing Affected:
  - only high-salience objects may enter Package G Device Atlas.
  - ordinary objects must greatly outnumber clue-bearing props.
  - no new universal MacGuffin added.
- World Rules Affected:
  - new provisional material-culture domain only.
  - public-safety/weapon, AI/autonomous security, property/inheritance/salvage and exact historical provenance remain dependency-blocked until Packages A/C/D etc. are completed.
- Documents Repaired/Created:
  - `docs/material-culture/MATERIAL-CULTURE-EQUIPMENT-RELICS-4-DESIGNS-v0.1.md`
  - `docs/material-culture/MATERIAL-CULTURE-BIBLE-v0.1.md`
  - `docs/qa/MATERIAL-CULTURE-EQUIPMENT-RELICS-RED-TEAM-v0.1.md`
  - `docs/qa/ENCYCLOPEDIC-DEEP-DESIGN-COMPLETENESS-AUDIT-v0.3.md`
  - `docs/current-work-status.md`
- Status:
  - `MC-H1 STRUCTURAL BASE = PASS`
  - `PACKAGE C-M FULL PASS = BLOCKED BY CROSS-PACKAGE DEPENDENCIES`
  - `CORE v1 UNCHANGED / MANUSCRIPT STILL BLOCKED`

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

Narrative Engineering maps are metadata/index/QA only; Canon/active Blueprint/M1/POV always override map summaries.

Material Culture Bible is provisional until its legal/economic/AI/history/arrival dependencies are reconciled.

Do not draft manuscript until:
`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`.
