# V3 C2 READER-FACING ASSET LABEL LEDGER v0.1

Status: `C2 TERMINOLOGY LOAD — ACTIVE UNDER v3 CANON (promoted 2026-08-21) / NO PROSE`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

Purpose:
Select the small reader-facing vocabulary that connects the 64 deep-designed asset families to 410-episode prose without forcing readers to memorize the internal catalog.

Authority:
- `V3-COLLECTIBLE-ASSET-MASTER-ROSTER-v0.1.md`
- `V3-COLLECTIBLE-ASSET-EXPOSURE-AND-NAMING-BUDGET-v0.1.md`
- `V3-ASSET-ACT-LIFECYCLE-MATRIX-v0.1.md`

Hard budget:
- non-character asset families = 51,
- stable recurring reader-facing labels <= 20,
- decorative invented proper/model/manufacturer terms <= 6,
- function/context/artbook-only assets >= 31.

Hostile-QA patch:
Do NOT fill the cap by default. Keep one reserve slot for a genuinely necessary recurring term discovered during prose/visual execution.

---

# 1. Selected stable 19 + reserve 1 — candidate

These are the non-character labels currently authorized for repeated reader-facing familiarity by default.

| # | Asset | Reader-facing label | Why it earns memory |
|---:|---|---|---|
| 1 | M01 Structural crawler | **구조 크롤러** | protagonist work + lineage payoff |
| 2 | M03 Utility tug | **화물 터그** | city logistics + Act6/9 inheritance |
| 3 | M04 Rescue skiff | **구조 스키프** | recurring rescue/care identity |
| 4 | M15 Settlement field rig | **필드리그** | Act9 strongest completion object |
| 5 | P01 Protagonist field case | **필드케이스** | protagonist material identity |
| 6 | P02 Damage marking system | **손상 마킹** | visible professional philosophy |
| 7 | P04 Mira route tags | **루트 태그** | logistics material language |
| 8 | P05 Niko qualification marker | **자격표식** | career-state recognition |
| 9 | L01 Transfer Belt | **벨트** | primary movement geography |
| 10 | L03 Garden Commons | **가든** | ordinary-life/emotional landmark |
| 11 | L05 Old Works | **올드웍스** | layered material-history landmark |
| 12 | L10 First Substrate Yard | **기판 야드** | Act9 signature site after reveal |
| 13 | M02 Damage-mapping drone | **매핑 드론** | recurring field support |
| 14 | M05 Medical transfer cradle | **이송 크래들** | medicine continuity across Acts |
| 15 | M07 Service frame | **서비스 프레임** | shared technical ancestry |
| 16 | L02 Midring | **미드링** | family/home/community geography |
| 17 | L04 Med-University | **메드** | recurring public medicine/care geography |
| 18 | L06 Juno venue | **주노네** | natural lived label; avoids new proper noun |
| 19 | M08 Outer Ark inspection pod | **점검 포드** | late reveal functional craft anchor |
| 20 | — | **RESERVE** | only for proven recurring execution need |

Hard:
This is a preferred recurring set, not a checklist requiring every term every Act.
Reserve cannot be consumed because a name merely sounds cool.

---

# 2. Demoted from stable-label obligation

M06 Public-safety barrier drone remains a fully designed recurring asset family, but its prose label is contextual rather than memorization-stable.

Allowed scene language:
- `차단 드론`,
- `이동식 차단판`,
- `안전 경계 장비`,
- role-specific description.

Reason:
its dramatic value comes from changing boundary/authority use, not from readers remembering one fixed product term.

---

# 3. Proper-name burden count

The following place labels are treated as functionalized proper/shorthand terms for burden accounting:
- 벨트,
- 가든,
- 올드웍스,
- 기판 야드,
- 미드링,
- 메드.

Count:
# **6**

This reaches the current hard cap for invented/proper-style recurring non-character terminology.

Therefore:
- no new recurring branded vehicle family name,
- no recurring manufacturer name,
- no decorative proper name for Spine/Rim/Legacy Layer,
- no named destination mountain/sea/valley in the current design pass.

Any future addition must displace an existing proper-style term or reopen the cap explicitly.

---

# 4. Context-only families — do NOT promote to stable terms

Examples:
- M06 barrier drone → context language from section 2.
- M09 Outer Ark service tug → `외부 서비스 터그`, `대형 서비스 터그` as needed; no permanent special name.
- M10 rescue/access craft → describe by role.
- M11 radiator/shield carriage → `방열판 정비 캐리지` in the technical scene only.
- M12 deployment barge → `정착 화물 바지선/배치 바지선` according to prose flow.
- M13 atmospheric lander → `화물 착륙선`, no signature model name.
- M14 surface vehicle → `지상 작업차`, `화물형 작업차`.
- P03 calibration set → `기디언의 검교정 세트` when ownership matters.
- P06 trauma roll → `구조용 처치 롤/키트` by scene.
- P07 evidence seal/access sleeve → functional description.
- P08 provenance tools → `이력 태그/검증 도구`.
- P09 authority panel/seals → `비상권한 패널/표식`.
- P10 breathing support → `보조호흡 장비` / `산소 보조팩` according to scene.
- P11 Juno containers/surfaces → ordinary nouns only.
- P12 Arun training sample → `파손 부품 샘플`.
- L07 central axis → `중앙 서비스축`.
- L08 expansion edge → `확장구역`, `림 쪽 공사구역` only if needed; no stable `림` requirement.
- L09 legacy service layer → `구형 서비스층` first; exact technical registry label only in evidence context.
- L11 commons → `첫 공용마당/공용구역`, no mythic proper name.
- L12 inland-sea workpoint → `내해 관측점/작업점`.
- W01~W12 culture families → ordinary nouns, never glossary entries.

---

# 5. Juno venue naming decision

Reader-facing label:
# **주노네**

Reason:
- natural spoken-life identity,
- no unnecessary cafe/restaurant brand lore,
- survives role changes from ordinary service to aid/network pressure and reopening,
- lets environment become memorable through people/use rather than invented signage.

An official cooperative/business registry name may exist internally but should not be repeated in prose unless paperwork requires it.

---

# 6. Internal model-code layer

Art/production/internal documentation may use stable design IDs without teaching them to readers.

Suggested internal family-code syntax:
- CR = crawler,
- MD = mapping drone,
- TG = tug,
- RS = rescue skiff,
- SF = service frame,
- OP = inspection pod,
- FR = field rig.

Generation/state syntax example:
`CR-G4`, `CR-G4-A6`, `FR-G1-SETTLEMENT`.

These are production identifiers, NOT automatic story model codes.

Prose may expose a code only if:
1. compatibility distinction matters,
2. two generations must be distinguished operationally,
3. a character would naturally use the code,
4. the episode remains under the model-code budget.

---

# 7. Brand/manufacturer decision

Recurring prose brands/manufacturers now:
# **ZERO**

Internal design may record maker/provenance as unnamed civic fabrication networks/workshops.

If a future compatibility/provenance incident requires a maker name, it must pass targeted C2 QA and the 6-term proper-name cap must be re-evaluated.

---

# 8. Act-introduction discipline

A1:
most stable place/work labels are learned through use, not glossary explanation.

A2:
`구조 스키프 / 이송 크래들` can become salient because emergency function earns them. M06 boundary equipment stays context-described.

A3:
prefer altered familiar labels; introduce almost no new stable terminology.

A4:
new social behavior > new object names.

A5:
legacy/provenance objects stay mostly descriptive; do not create relic names.

A6:
transformation of familiar labels dominates.

A7:
`점검 포드` is the only selected new recurring Outer-Ark craft label by default; the rest are functional descriptions.

A8:
care/legal vocabulary dominates; no new collectible label wave.

A9:
`필드리그` and `기판 야드` carry completion; other destination assets remain functional nouns.

---

# 9. Current verdict

Stable non-character recurring label count:
# **19 / 20 maximum + 1 reserve**

Proper/shorthand invented-place burden:
# **6 / 6 maximum**

Recurring manufacturer/brand count:
# **0**

Function/context/artbook-only families:
# **32+ preserved**

Result:
The internal world remains deep while reader terminology remains bounded and one execution reserve remains available.
