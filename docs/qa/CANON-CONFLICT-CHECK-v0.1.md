# Canon Conflict Check v0.1

Status: `CONSOLIDATION QA / NO CANON FREEZE YET`

Purpose:
현재 repository에 남아 있는 초기 비교문서와 최신 Repair/Act/Character 설계가 충돌하는 지점을 분류한다.

Rules:
- old design docs are not deleted.
- historical comparison value is preserved.
- latest repair/change-log/canon-status take priority.
- `UNRESOLVED`와 `SUPERSEDED`를 구분한다.

---

# 1. Conflict Status Categories

## RESOLVED / SUPERSEDED
옛 문서에 남아 있지만 현재 1순위로 재사용하면 안 되는 표현.

## OPEN DESIGN
서로 충돌이 아니라 아직 선택하지 않은 항목.

## STALE STATUS DOC
설계는 해결됐지만 status/handoff 문서가 최신화되지 않은 경우.

## BLOCKING CONFLICT
두 최신 1순위가 동시에 참일 수 없는 경우.

---

# 2. Truth / History Conflicts

## CC-01 — Adult Artificial Substrate Transition
Old:
`docs/design/02-truth-architecture-c-lite-v0.1.md`
- 자발적 인공기질 전환
- 현재 사회가 machine/artificial substrate 후손처럼 읽힐 수 있음

Latest:
- H2R-A biological body + synthetic-origin cognition
- H8R-2 multi-generation prenatal Seed adoption

Resolution:
**SUPERSEDED wording.**

Current history:
- original natural-origin humans live and reproduce
- successive children increasingly receive generated developmental Seed
- no mass adult mind upload/machine-body conversion required

Status:
`RESOLVED / SUPERSEDED`

---

## CC-02 — Witness / One-at-a-Time Natural Human Protocol
Old:
- C-lite witness lineage
- WL11 late `기원 연속성 규약` one-at-a-time preservation
- earlier Witness Protocol variants

Latest:
- OH-D rare deliberate unseeded birth
- Demography uniqueness sanity
- H8R-2

Resolution:
There is no system/policy guaranteeing one active natural-origin human.
Historical exceptions occur rarely; current active=1 is contingent demographic state.

Status:
`RESOLVED / REJECTED AS CURRENT PRIORITY`

---

## CC-03 — What Happened To Original Passengers
Old possible readings:
- catastrophe replacement
- adult substrate conversion
- disappearance

Latest:
H8R-2:
original passengers and early generations lived ordinary lives, had children, and aged/died while seeded-born descendants became dominant.

Status:
`RESOLVED PROVISIONAL`

---

# 3. Birth / Medical Conflicts

## CC-04 — Universal Assisted Reproduction / Hard Clinic Dependency
Old:
WL03/P0 older candidate can read as all reproduction requires clinic/checkpoint.

Latest:
H3/U-C:
- natural conception possible
- assisted conception possible
- prenatal Seed window is standard care
- true natural-origin requires full Seed-window refusal

Status:
`RESOLVED / OLDER MODEL SUPERSEDED`

---

## CC-05 — Seed Is Necessary For Modern Reconstruction
Old H8 wording:
seeded cognition may sound permanently much more reconstructable.

Latest:
- early primitive continuity medicine had stronger compatibility benefit
- modern mapping can reconstruct both origins
- provenance, not current scan phenotype, proves origin

Status:
`RESOLVED PROVISIONAL`

---

# 4. Death / Aging Conflicts

## CC-06 — Full Scan As Executable Person File
Old:
WL05-06 initial backup alternatives / older H4 interpretations.

Latest:
RB-B Recovery Map + Surviving Neural Anchor.

Status:
`RESOLVED / SUPERSEDED`

---

## CC-07 — Reconstruction Implies Immortality
Old gap:
no clear anti-age-reset rule.

Latest:
AG-H1:
- injury-relative repair
- current anchor dominates
- partial healthspan extension
- no routine chronological rollback
- candidate effective lifespan ~90~120y, exceptional 120~130+

Status:
`RESOLVED PROVISIONAL`

---

# 5. Ship / Destination Conflicts

## CC-08 — 8 Theme Sectors vs 3 Habitats
Old:
Living World v0.1 eight strongly themed sectors.

Latest:
3 large Habitats + Spine/Outer Works + districts.

Resolution:
old names/functions can survive only as districts/institutions/cultural history, not eight separate civilization biomes.

Status:
`RESOLVED / v0.1 STRUCTURE SUPERSEDED`

---

## CC-09 — Planet vs Ship Binary
Old:
WL12 primary framing could be read as surface settlement vs ship preservation.

Latest:
H9R Resource Triangle / staged settlement:
- ship
- orbit
- surface
- future new habitat
continuous paths.

Status:
`RESOLVED / WL13+E-H1 TAKE PRIORITY`

---

## CC-10 — Deceleration Steals Civil Power
Old:
C-FULL parent Act B5 wording includes `감속 전력/방열 압박` and older ship docs can imply direct GW competition.

Latest:
H9R-P1:
propulsion direct-exhaust power scale is 7~8 orders above civil grid.

Current story pressure:
- thermal geometry
- spares
- manufacturing
- specialist labor
- reaction mass
- maintenance windows
- redundancy

Resolution:
**Any phrase meaning direct civil-grid competition is stale.**
`감속 전력 압박` should be read/repaired as `감속계 유지·열관리·산업/정비 자원 압박`.

Status:
`RESOLVED LOGIC / PARENT ACT TEXT NEEDS CLEANUP`

---

## CC-11 — Mature ISRU At T0
Risk:
Some early ending language could imply functioning mature orbital/surface industry immediately at arrival.

Latest:
E-H1 / EC-H1:
At T0 only:
- insertion
- scout confirmation
- deployment/start of depot/power/ISRU

Mature cities/industry occur later.

Status:
`RESOLVED PROVISIONAL`

---

# 6. Arrival Law Conflicts

## CC-12 — Old Mission Law Is Newly Discovered At Act 5
Old risk:
Act wording may read as if nobody knew 400-year-old law until P found it.

Latest:
ATL-H1:
- law/charter known to specialists
- T-30~T-10 technical prep already uses planning frameworks
- around T-10 Final Approach Transition Certification makes reconciliation binding
- C8 does not activate law

Status:
`RESOLVED PROVISIONAL`

---

## CC-13 — C8 As Mission Key
Old C-lite/C4-style risk:
bio-origin human unlocks settlement protocol.

Latest:
Explicitly forbidden.
C8 is legally/symbolically explosive but has no command/admin authority.

Status:
`RESOLVED / REJECTED`

---

# 7. Information / Reveal Conflicts

## CC-14 — Count Is A Public Census Field
Old intuitive reading:
if system knows count, anyone could query it.

Latest:
IL-H1:
count requires legacy provenance + prenatal archive + current alive/civic registry crosswalk.
Aggregate and personal identity access differ under general privacy architecture.

Status:
`RESOLVED PROVISIONAL`

---

## CC-15 — Count Immediately Shows C8 Name
Latest:
aggregate 53~58 → meaning 59~66 → private identity mapping 67~76.
ID-H1 then gives controlled public disclosure.

Status:
`RESOLVED PROVISIONAL`

---

## CC-16 — C8 Public Identity By Leak
Old/open risk:
privacy + public fame gap.

Latest:
ID-H1 Controlled Necessary Disclosure:
- private notice
- temporary work/family privacy friction
- narrow challenge
- rumor/speculation pressure
- C8 chooses limited public identification to control family boundary

Unauthorized leak is rejected as primary.

Status:
`RESOLVED PROVISIONAL`

---

# 8. Character Conflicts / Open Designs

## CC-17 — P Origin
Current status docs still list:
- P synthetic-origin = CANDIDATE
- P derived/no-original = CANDIDATE

Under latest H2/U-C/RB-B:
P being a routine seeded-origin citizen is structurally simplest, but this has **not yet been formally compared/frozen**.

This is not a logical contradiction, but Character Freeze cannot leave both incompatible options open.

Status:
`OPEN DESIGN — MANDATORY BEFORE CHARACTER FREEZE`

---

## CC-18 — P/S/N Exact Ages
AGE-B is current first candidate.
Exact ages not frozen.

Status:
`OPEN DESIGN / NOT P0`

---

## CC-19 — Names / Genders
Not structurally decided.

Status:
`OPEN CHARACTER FREEZE ITEM`

---

## CC-20 — S/R/M/D/O/C8-family Anchors
Missing-gap pack supplies provisional current-first candidates.
They do not currently conflict with core plot.

Status:
`PROVISIONAL / NEED CONSOLIDATION, NOT P0`

---

# 9. Act / Time Conflicts

## CC-21 — Reveal Timing
Parent Act says broad:
- count 55~65
- C8 65~78

Sub-Act refines:
- count 53~58
- meaning 59~66
- C8 67~76

Resolution:
This is not contradiction; parent is range, Sub-Act is current finer candidate.

Status:
`SUB-H1 TAKES PRIORITY / NOT CANON`

---

## CC-22 — Story Span
Old parent Act left exact year span open.
Latest T-H1 spans ~14y.

Status:
`PROVISIONAL NEW PRIORITY`

Character ages must follow T-H1 if adopted.

---

## CC-23 — C8 Pre-Reveal Appearances
C8 old doc says Act1 late/Act2 early; SUB-H1 places:
- 29~36 worker
- 37~44 family
- 45~52 bootstrap issue

No logical conflict.

Status:
`SUB-H1 CURRENT DETAIL`

---

# 10. Ending Conflicts

## CC-24 — One Correct Settlement Path
Rejected by E-H1.

Current:
Costly Polycentric Arrival.

Status:
`RESOLVED PROVISIONAL`

---

## CC-25 — Free Third Way
EC-H1 requires visible costs.
At least 5/7 cost classes recommended, 3+ named-character effects.

Status:
`CONDITIONAL PASS — ENDING BEAT MAP STILL REQUIRED`

---

# 11. Status-Document Staleness

## CANON_STATUS.md
Currently missing newest candidates:
- SUB-H1
- IL-H1
- FP-H1
- T-H1
- E-H1 / EC-H1
- AGE-B / character anchors
- demographic sanity
- AG-H1
- ATL-H1
- ID-H1
- H8R-2

Current Freeze Blockers section is stale.

Status:
`STALE — MUST UPDATE`

---

## docs/current-work-status.md
Does not yet contain current consolidation/red-team/repair progress.

Status:
`STALE — MUST UPDATE`

---

## docs/NEXT-CHAT-HANDOFF.md
Still reflects the checkpoint before Sub-Act/Info/Ending/Aging/Legal/C8 disclosure repairs.

Status:
`STALE — MUST UPDATE BEFORE CHAT RISK`

---

## docs/change-log.md
Last confirmed entry CHG-015.
New meaningful priority shifts need entries.

Status:
`STALE — MUST UPDATE`

---

# 12. Blocking Conflict Result

After H8R-2 / AG-H1 / ATL-H1 / ID-H1:

**No known current-vs-current P0 contradiction remains in the consolidated model.**

However this is NOT equivalent to Design Freeze.

Freeze still requires:
1. mandatory open character choices resolved enough for Character Bible
2. Living World remaining throughput/geometry sanity
3. Ending Beat / cost placement
4. exact reveal wording QA
5. final P0 Red Team rerun against consolidated status
6. Freeze checklist all required design artifacts present

---

# 13. Source Priority Rule Going Forward

When an old file conflicts:

1. `CANON_STATUS.md` after current update
2. `docs/change-log.md` latest CHG
3. latest repair/consolidation doc
4. original 4-design document as historical rationale only

Old docs are not silently deleted.

---

# Verdict

`CANON CONFLICT CHECK = CONDITIONAL PASS`

- current P0 contradictions: none found after repair
- stale historical wording: identified
- status docs: must update
- open non-P0 design choices: still block Design Freeze by completeness, not by logical contradiction

Next:
**Freeze Checklist v0.1 + remaining mandatory design pack**
