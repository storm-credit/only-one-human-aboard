# V3 VISUAL ASSET MANIFEST v0.1

Status: `PRODUCTION MANIFEST / NOT CANON / NO PROSE / ART NOT FROZEN`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. 목적

이 문서는 `V3-COLLECTIBLE-ASSET-MASTER-ROSTER-v0.1.md`의 **64 base assets + 28 sanctioned variants**를 실제 제작 순서와 산출물로 변환한다.

숫자:
- Base asset families: **64**
- Variant slots: **28**
- Initial internal catalog target: **92**
- Hard ceiling: **96**

이 Manifest는 92장의 이미지를 즉시 만들라는 의미가 아니다.

기본 순서:
1. Visual QA 대표 샘플
2. SIGNATURE 16
3. RECURRING 24
4. 필요한 WORLD-DEPTH 24
5. 승인된 variants 28

---

# 1. STATUS ENUM

- `SPEC-READY` — 문서 설계만 완료
- `CALIBRATION-SAMPLED` — 스타일 확인용 샘플 존재
- `TEST-REQUIRED` — 중립 QA 이미지 필요
- `TEST-GENERATED` — QA용 이미지 존재
- `QA-FAIL`
- `QA-REVISE`
- `QA-PASS-CANDIDATE`
- `VISUAL-FROZEN`

현재 전체 기본값:
# `SPEC-READY`

C01 주인공만:
# `CALIBRATION-SAMPLED / FINAL IDENTITY OPEN`

최근 Proposal A/C는 스타일 캘리브레이션이지 정본 얼굴이 아니다.

---

# 2. PRODUCTION DELIVERABLE TYPES

## D-CHAR-BASE
- full body
- face close-up
- 3/4/profile
- ordinary-work pose
- key material/prop detail

## D-CHAR-CONFUSION
- identical light/background
- neutral gray clothing
- front / 3/4 / side
- hair styling minimized
- small silhouette

## D-MACHINE-BASE
- 3/4
- side
- scale cue
- functional detail

## D-MACHINE-LINEAGE
- 2~4 authorized generations/states
- shared interface ancestry visible

## D-ENV-BASE
- wide establishing
- human eye-level
- material/detail vignette

## D-PROP-BASE
- idle/closed
- in-use
- detail/material breakdown

## D-CULTURE-SPOT
- one ordinary in-world use context
- optional collection/display context

---

# 3. PHASE V-A — CHARACTER CONFUSION FIRST

| Order | ID | Asset | Tier | Required output | Current status | Why first |
|---:|---|---|---|---|---|---|
| 1 | C01 | Protagonist | SIGNATURE | D-CHAR-CONFUSION + later D-CHAR-BASE | CALIBRATION-SAMPLED | final identity still open |
| 2 | C13 | Arun Kalev | SIGNATURE | D-CHAR-CONFUSION | TEST-REQUIRED | same-age technical collision |
| 3 | C07 | Gideon Park | RECURRING | D-CHAR-CONFUSION | TEST-REQUIRED | older technical collision |
| 4 | C11 | Ivo Serrin | RECURRING | D-CHAR-CONFUSION | TEST-REQUIRED | tired-middle-aged male collision |

V-A passes only if these four remain distinguishable under identical neutral conditions.

---

# 4. CHARACTER BASE ASSETS — 13

| ID | Asset | Tier | Base deliverable | Variant allocation | Status |
|---|---|---|---|---|---|
| C01 | Protagonist | SIGNATURE | D-CHAR-BASE | +1 Act6/Act9 selected state | CALIBRATION-SAMPLED |
| C02 | Mira Solano | SIGNATURE | D-CHAR-BASE | +1 Act6 logistics state | SPEC-READY |
| C03 | Selene Adebayo | RECURRING | D-CHAR-BASE | +1 Act6 peak-authority state | SPEC-READY |
| C04 | Rafi Chen | RECURRING | D-CHAR-BASE | +1 Act6 scarcity rescue state | SPEC-READY |
| C05 | Leila Noor | RECURRING | D-CHAR-BASE | +1 late rights/care state | SPEC-READY |
| C06 | Sora Mbeki | RECURRING | D-CHAR-BASE | none | SPEC-READY |
| C07 | Gideon Park | RECURRING | D-CHAR-BASE | none | TEST-REQUIRED |
| C08 | Niko Osman | SIGNATURE | D-CHAR-BASE | +1 Act9 field state | SPEC-READY |
| C09 | Juno Reyes | RECURRING | D-CHAR-BASE | +1 Act6 environment-integrated state | SPEC-READY |
| C10 | Hana Kouri | RECURRING | D-CHAR-BASE | none | SPEC-READY |
| C11 | Ivo Serrin | RECURRING | D-CHAR-BASE | none | TEST-REQUIRED |
| C12 | Cassian Dae | RECURRING | D-CHAR-BASE | none | SPEC-READY |
| C13 | Arun Kalev | SIGNATURE | D-CHAR-BASE | +1 current-workplace/late-current-life state | TEST-REQUIRED |

Character variants = **8**.

---

# 5. PHASE V-B — MACHINE CONFUSION FIRST

| Order | ID | Asset | Tier | Required output | Status |
|---:|---|---|---|---|---|
| 1 | M01 | Structural Crawler | SIGNATURE | D-MACHINE-BASE | TEST-REQUIRED |
| 2 | M02 | Damage-Mapping Drone | RECURRING | D-MACHINE-BASE | TEST-REQUIRED |
| 3 | M03 | Utility Tug | SIGNATURE | D-MACHINE-BASE | TEST-REQUIRED |
| 4 | M04 | Rescue Skiff | SIGNATURE | D-MACHINE-BASE | TEST-REQUIRED |

V-B passes only if color/logo/model text를 제거해도 역할이 서로 다르게 읽힌다.

---

# 6. MACHINE / CRAFT BASE ASSETS — 15

| ID | Asset | Tier | Base output | Variant slots | Spoiler | Status |
|---|---|---|---|---:|---|---|
| M01 | Structural Inspection Crawler | SIGNATURE | D-MACHINE-BASE | +3 | PUBLIC-SAFE | TEST-REQUIRED |
| M02 | Damage-Mapping Drone | RECURRING | D-MACHINE-BASE | 0 | PUBLIC-SAFE | TEST-REQUIRED |
| M03 | Utility Tug / Freight Tractor | SIGNATURE | D-MACHINE-BASE | +2 | PUBLIC-SAFE | TEST-REQUIRED |
| M04 | Rescue Skiff | SIGNATURE | D-MACHINE-BASE | +2 | PUBLIC-SAFE | TEST-REQUIRED |
| M05 | Medical Transfer Cradle | RECURRING | D-MACHINE-BASE | 0 | PUBLIC-SAFE | SPEC-READY |
| M06 | Public-Safety Barrier Drone | RECURRING | D-MACHINE-BASE | 0 | PUBLIC-SAFE | SPEC-READY |
| M07 | Non-Combat Service Frame | RECURRING | D-MACHINE-BASE | +1 | PUBLIC-SAFE | SPEC-READY |
| M08 | Outer Ark Inspection Pod | RECURRING | D-MACHINE-BASE | +1 | OUTER-ARK-SPOILER | SPEC-READY |
| M09 | Outer Ark Service Tug | RECURRING | D-MACHINE-BASE | +1 | OUTER-ARK-SPOILER | SPEC-READY |
| M10 | Outer Ark Rescue / Access Craft | WORLD-DEPTH | D-MACHINE-BASE | 0 | OUTER-ARK-SPOILER | SPEC-READY |
| M11 | Radiator / Shield Maintenance Carriage | WORLD-DEPTH | D-MACHINE-BASE | 0 | OUTER-ARK-SPOILER | SPEC-READY |
| M12 | Settlement Deployment Barge | WORLD-DEPTH | D-MACHINE-BASE | 0 | ENDGAME-SPOILER | SPEC-READY |
| M13 | Atmospheric Utility Lander | WORLD-DEPTH | D-MACHINE-BASE | 0 | ENDGAME-SPOILER | SPEC-READY |
| M14 | Surface Utility Vehicle | RECURRING | D-MACHINE-BASE | 0 | ENDGAME-SPOILER | SPEC-READY |
| M15 | Settlement Commissioning Field Rig | SIGNATURE | D-MACHINE-BASE | +2 | ENDGAME-SPOILER | SPEC-READY |

Machine variants = **12**.

---

# 7. PHASE V-C — ENVIRONMENT RECOGNITION FIRST

| Order | ID | Asset | Tier | Output | Status |
|---:|---|---|---|---|---|
| 1 | L01 | Transfer Belt Interchange | SIGNATURE | D-ENV-BASE | TEST-REQUIRED |
| 2 | L02 | Midring Courtyard | RECURRING | D-ENV-BASE | TEST-REQUIRED |
| 3 | L03 | Garden Lightwell Terrace | SIGNATURE | D-ENV-BASE | TEST-REQUIRED |
| 4 | L04 | Med/University Promenade | RECURRING | D-ENV-BASE | TEST-REQUIRED |
| 5 | L05 | Old Works Junction | SIGNATURE | D-ENV-BASE | TEST-REQUIRED |

V-C passes only if 장소명을 지워도 서로 구분되며 동시에 하나의 Meridian 도시로 읽힌다.

---

# 8. PLACE BASE ASSETS — 12

| ID | Asset | Tier | Base output | Variant | Spoiler | Status |
|---|---|---|---|---|---|---|
| L01 | Transfer Belt Layered Bridge Interchange | SIGNATURE | D-ENV-BASE | +1 Act6 transformed | PUBLIC-SAFE | TEST-REQUIRED |
| L02 | Midring Community Courtyard | RECURRING | D-ENV-BASE | 0 | PUBLIC-SAFE | TEST-REQUIRED |
| L03 | Garden Lightwell Terrace | SIGNATURE | D-ENV-BASE | +1 late persistence | PUBLIC-SAFE | TEST-REQUIRED |
| L04 | Med/University Rehab-Education Promenade | RECURRING | D-ENV-BASE | 0 | PUBLIC-SAFE | TEST-REQUIRED |
| L05 | Old Works Multi-Generation Junction | SIGNATURE | D-ENV-BASE | +1 permanent-retirement/damage | PUBLIC-SAFE | TEST-REQUIRED |
| L06 | Juno Community Venue | RECURRING | D-ENV-BASE | 0 | PUBLIC-SAFE | SPEC-READY |
| L07 | Spine Civic/Service Axis | WORLD-DEPTH | D-ENV-BASE | 0 | PUBLIC-SAFE | SPEC-READY |
| L08 | Rim/Expansion Build Edge | WORLD-DEPTH | D-ENV-BASE | 0 | PUBLIC-SAFE | SPEC-READY |
| L09 | Legacy Service Layer Access Node | WORLD-DEPTH | D-ENV-BASE | 0 | ACT3+/REVEAL-SENSITIVE | SPEC-READY |
| L10 | First Substrate Yard | SIGNATURE | D-ENV-BASE | +1 post-crisis lived state | ENDGAME-SPOILER | SPEC-READY |
| L11 | First Human-Scale Commons | WORLD-DEPTH | D-ENV-BASE | 0 | ENDGAME-SPOILER | SPEC-READY |
| L12 | Inland-Sea Survey/Observation Workpoint | WORLD-DEPTH | D-ENV-BASE | 0 | ENDGAME-SPOILER | SPEC-READY |

Place variants = **4**.

---

# 9. PROP BASE ASSETS — 12

| ID | Asset | Tier | Base output | Variant | Status |
|---|---|---|---|---|---|
| P01 | Protagonist Field Case / Damage Kit | SIGNATURE | D-PROP-BASE | +1 early/late | SPEC-READY |
| P02 | Damage-Marking Language / Set | SIGNATURE | D-PROP-BASE | 0 | SPEC-READY |
| P03 | Gideon Calibration Set | RECURRING | D-PROP-BASE | 0 | SPEC-READY |
| P04 | Mira Route Tags | SIGNATURE | D-PROP-BASE | +1 Act6 distributed coordination | SPEC-READY |
| P05 | Niko Qualification Marker | SIGNATURE | D-PROP-BASE | +1 state change | SPEC-READY |
| P06 | Rafi Trauma Roll | RECURRING | D-PROP-BASE | 0 | SPEC-READY |
| P07 | Sora Evidence Seal/Access Sleeves | WORLD-DEPTH | D-PROP-BASE | 0 | SPEC-READY |
| P08 | Hana Provenance/Archive Kit | RECURRING | D-PROP-BASE | 0 | SPEC-READY |
| P09 | Selene Authority Panel / Manual Seal Tags | RECURRING | D-PROP-BASE | 0 | SPEC-READY |
| P10 | Destination Breathing-Support Kit | WORLD-DEPTH | D-PROP-BASE | 0 | SPEC-READY |
| P11 | Juno Service Container / Notice Surface | WORLD-DEPTH | D-PROP-BASE | 0 | SPEC-READY |
| P12 | Arun Failed-Component Training Sample | RECURRING | D-PROP-BASE | 0 | SPEC-READY |

Prop variants allocated explicitly = **3**, plus W-family comparison 1 = total prop/culture variant budget **4**.

---

# 10. IN-WORLD CULTURE BASE ASSETS — 12

| ID | Asset | Tier | Output | Status |
|---|---|---|---|---|
| W01 | Utility Craft Miniature Generations | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W02 | Transit Route Maps / Pins | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W03 | Retired Route/Station Memorabilia | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W04 | District Festival/Civic Badges | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W05 | Sports/Team Objects | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W06 | School/Community Pins | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W07 | Heritage Reproduction Prints/Books/Art | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W08 | Old Game/Board-Game Sets | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W09 | Historical Signage Reproductions | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W10 | Retired Certified Tool Housings/Manuals | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W11 | Household Reissue/Restoration Objects | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |
| W12 | First-Year Settlement Maps/Service Patches | WORLD-DEPTH | D-CULTURE-SPOT | SPEC-READY |

One W-family receives one generation/reissue comparison variant **only after Visual QA**.

---

# 11. VARIANT COUNT CHECK

Character variants: **8**
Machine variants: **12**
Place variants: **4**
Prop/culture variants: **4**

Total = **28**.

Base 64 + variants 28 = **92**.

Reserve +4 is locked and may be opened only by explicit Visual QA need.

---

# 12. FIRST PRODUCTION MILESTONE

Do NOT produce all 92.

Milestone `VP-M1`:

### Character
- C01 / C13 / C07 / C11 confusion test

### Machine
- M01 / M02 / M03 / M04 neutral family test

### Environment
- L01 / L02 / L03 / L04 / L05 recognition test

Total empirical test subjects:
# **13**

Only if VP-M1 passes:
- freeze production templates,
- proceed to SIGNATURE 16 base assets.

---

# 13. SECOND PRODUCTION MILESTONE

Milestone `VP-M2`:
SIGNATURE 16 base assets.

SIGNATURE:
- C01, C02, C08, C13
- M01, M03, M04, M15
- P01, P02, P04, P05
- L01, L03, L05, L10

Not all require final cinematic art.
They require a stable **design identity plate** first.

---

# 14. HARD STOP

Do not create:
- 64 unique logos
- 64 invented brands
- arbitrary color variants
- swimsuit/armor/faction skins
- combat upgrades
- collector rarity tiers
- merch-only assets

The Asset Manifest exists to prevent image generation from becoming uncontrolled content expansion.
