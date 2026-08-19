# V3 CANON PROMOTION DECISION PACKAGE v0.1

Status: `PROMOTION DECISION READY / NO PROMOTION PERFORMED`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》
Repository: `storm-credit/only-one-human-aboard`

Purpose:
Present the safe options for moving from official frozen v2 to the completed v3 candidate after Deep Design + EP001~410 blueprint materialization + full hostile regression.

Important:
This document does **not** change `canon/CANON_STATUS.md`.
Official Canon remains v2 until an explicit promotion decision is made.

---

# 0. Current evidence before decision

v3 status:
- Deep Completion G01~G20 = PASS
- Candidate Freeze = PASS
- EP001~410 episode blueprint materialization = COMPLETE
- all 9 Act blueprint hostile QAs = PASS WITH EXECUTION DISCIPLINE
- full-series blueprint regression = STRUCTURAL PASS
- Blocking P0 = 0
- structural P1 = 0
- hard-science boundary pass = COMPLETE
- HUMAN medical/developmental pass = COMPLETE
- Minimum Action context-pack architecture = PASS
- final prewriting structural lock = PASS

Therefore the decision is no longer `is v3 sufficiently designed?`
It is:
**which authority/manuscript branch should become official?**

---

# 1. Option A — Keep v2 official, v3 remains parallel candidate

## Action
- do not change Canon authority,
- preserve v2 manuscript EP001~010 as active official manuscript,
- keep all v3 work as candidate/prewriting branch.

## Advantages
- zero official migration risk,
- preserves all prior v2 freeze/work exactly,
- useful if user still wants to compare v2 vs v3 before committing.

## Costs
- future work has two competing story architectures,
- generic `진행` requires constant routing discipline,
- v3 410-episode blueprint cannot become manuscript authority,
- risk of Shadow Canon remains organizationally higher despite routing files.

## Judgment
**보류용 선택 / safe but inefficient if v3 is now the intended novel.**

---

# 2. Option B — Promote v3 as new official Canon; archive v2 as historical branch

## Action
- promote v3 world/character/act/narrative authorities,
- update `canon/CANON_STATUS.md`,
- explicitly mark v2 frozen Canon as historical previous edition, not deleted,
- preserve accepted v2 EP001~010 as historical manuscript branch,
- create a **new v3 manuscript line starting from EP001** using v3 episode blueprint,
- never silently call old prose failed/rejected; it belongs to a different frozen design.

## Advantages
- one clear active authority,
- completed 410-episode blueprint becomes executable,
- no need to force old 230-episode prose into a materially different structure,
- preserves provenance/change history,
- minimizes future context confusion.

## Costs
- old accepted EP001~010 no longer belong to current active manuscript line,
- v3 prose must begin again at EP001 when user explicitly starts manuscript execution,
- requires careful promotion/change-control update.

## Judgment
# **RECOMMENDED / 채택 1순위**

Reason:
v3 is no longer a minor amendment. It changes ontology, 9-Act macro, 410-episode pacing, protagonist occupation/biography, reveal order, H-A/H-B mechanism, HUMAN meaning and final settlement architecture. A clean edition/branch transition is safer than pretending continuity with v2 prose.

---

# 3. Option C — Promote v3 world/characters but retain old v2 230-episode Act/manuscript structure

## Action
Attempt to replace only world/character Canon while preserving v2 Act1~7/230 and EP001~010.

## Advantages
- appears to save old prose and old episode architecture.

## Failures
- v3 mysteries require first major transition near EP094 rather than old reveal cadence,
- v3 H-A/H-B structure depends on 9 Acts and ~410 pacing,
- HUMAN meaning and reveal timing changed materially,
- protagonist profession/personal history changed,
- Act6/7/8/9 rights/lineage/settlement architecture has no equivalent in old 230 structure,
- old blueprints/context manifests would carry incompatible knowledge/reveal assumptions.

## Judgment
# **REJECT / 폐기**

This creates the highest Shadow Canon risk.

---

# 4. Option D — Promote v3 but retrofit old accepted EP001~010 into the new 410-episode manuscript

## Action
Keep old prose as EP001~010 and force subsequent v3 blueprint to continue from EP011.

## Apparent advantage
- avoids rewriting ten already accepted episodes.

## Failures
- old episodes were written for a different protagonist/world/act/reveal architecture,
- even if line-level prose can be reused, scene purposes and planted continuity may be wrong,
- v3 Act1 explicitly needs new ordinary-life, profession, family, relationship and Act2 fair-plant structure,
- retrofitting would require hidden rewrites anyway and make provenance hard to audit.

Potential salvage:
Specific **lines/scenes/images** from old prose may later be reused only after v3 episode-card compliance review, but not by assuming entire episodes are compatible.

## Judgment
# **REJECT AS DEFAULT / 폐기**

Do not save sunk work at the cost of story coherence.

---

# 5. Recommended promotion architecture

If user chooses Option B:

## 5.1 Authority
Create/update official authority so active order becomes approximately:
1. `CLAUDE.md`
2. new v3 Canon status/router
3. v3 World/ontology consolidated authorities
4. `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md` promoted version
5. `canon/ACT_BIBLE-v3.2-CANDIDATE.md` promoted version
6. v3 setting addenda
7. v3 reveal/writer grammar
8. v3 EP001~410 blueprint registry
9. context-pack execution spec

Before promotion, decide whether to rename `*-CANDIDATE` files to frozen Canon files or freeze by authoritative routing without mass renames. Preferred approach:
**minimal mutation: promote through an explicit v3 Canon Constitution/Status that names exact files and hashes/versions; only rename the three top-level Bible files if reader/developer ergonomics materially improve.**

Why:
Avoid unnecessary large repository churn and broken references.

## 5.2 Historical v2
Preserve:
- v2 Canon files,
- v2 Amendment A,
- all v2 QA,
- old EP001~010 prose,
- old context/blueprints.

Mark as:
`FROZEN HISTORICAL EDITION / NOT ACTIVE FOR NEW V3 MANUSCRIPT`.

Do not delete.

## 5.3 Manuscript routing
Create separate status:
- Historical v2 manuscript: EP001~010/230 preserved
- Active v3 manuscript: 0/410 until first v3 episode is explicitly drafted and accepted

No prose begins during promotion itself.

## 5.4 Change control
Promotion record must include:
- old → new authority map,
- v2 preservation path/status,
- protagonist placeholder/name state,
- episode count change 230 → 410 candidate/frozen center,
- all major ontology/reveal differences,
- treatment of old manuscript,
- QA evidence.

Use:
`docs/change-control/V2-TO-V3-CANDIDATE-FREEZE-CHANGE-RECORD-v0.1.md` as input.

---

# 6. Remaining surface C2 before or after promotion

Promotion does NOT technically require these to decide architecture:
- protagonist final name,
- family names,
- exact district proper names,
- currency/payment term,
- venue/shop/room names,
- exact final Mira scene wording.

However, **protagonist final name should close before v3 prose EP001 is drafted.**

Recommended ordering:
Promotion decision may happen first.
Final naming pass happens before Manuscript Start Gate.

---

# 7. Promotion hostile test

## Attack: `Why not preserve both as equally active?`
Because all future generic references become ambiguous and context cost doubles.
Historical preservation is enough; active authority should be singular.

## Attack: `Why throw away accepted ten episodes?`
They are not thrown away. They remain the finished beginning of v2 edition. Reusing entire episodes in v3 would import invisible assumptions and is higher risk than a fresh v3 execution.

## Attack: `Is v3 actually sufficiently designed to justify promotion?`
Yes at structural/prewriting level: 410/410 cards, P0=0, full regression PASS, science/medical boundary passes, context architecture complete.

## Attack: `Could v3 still change during prose?`
C2 and scene-level refinements can. C0/C1 contradictions require change control. That is normal after Freeze and does not justify keeping v3 unofficial forever.

---

# 8. Decision table

| Option | Coherence | Provenance | Old prose preservation | Future routing | Verdict |
|---|---|---|---|---|---|
| A v2 official / v3 parallel | High separately | High | Full | Medium-low | HOLD |
| B v3 promote / v2 historical | **Highest** | **Highest** | Full historical | **Highest** | **RECOMMENDED** |
| C hybrid v3 world + v2 acts | Low | Low | Apparent | Low | REJECT |
| D force old EP001~010 into v3 | Medium-low | Medium | Full active | Medium-low | REJECT |

---

# 9. Current decision status

# **PROMOTION PACKAGE READY**

# **RECOMMENDATION: OPTION B**

No promotion action has been performed by this document.
`canon/CANON_STATUS.md` remains v2 until explicit promotion execution.