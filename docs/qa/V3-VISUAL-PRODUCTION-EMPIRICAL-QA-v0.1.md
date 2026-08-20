# V3 VISUAL PRODUCTION EMPIRICAL QA v0.1

Status: `VISUAL EXECUTION QA / NOT CANON / NO PROSE / ART NOT FROZEN`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. 목적

문서상 차별화가 실제 이미지에서도 살아남는지 검증한다.

이 QA의 핵심 질문:

> 예쁜가? 보다 먼저, **같은 세계 안에서 서로 다른 사람/기체/장소로 실제로 보이는가?**

관련 입력:
- `docs/visual-production-v3/V3-VISUAL-PRODUCTION-BIBLE-v0.1.md`
- `docs/visual-production-v3/V3-IMAGE-GENERATION-PROMPT-PACK-v0.1.md`
- `docs/visual-production-v3/V3-VISUAL-ASSET-MANIFEST-v0.1.md`
- `docs/reference-v3/V3-VISUAL-DIFFERENTIATION-MATRIX-v0.1.md`

---

# 1. QA STATE

현재:
- 문서 차별화: PASS
- 레퍼런스 수집: PASS/CLOSED
- 수집욕 자산 범위: PASS
- 실제 visual differentiation: **OPEN**

최근 주인공 샘플 결과:
- 초기 실사형 중년 샘플: **FAIL**
- 이유: 체감 연령 과다 / photoreal 과다 / 주인공 에너지 부족
- 2D 세미리얼 A/C: **CALIBRATION PASS**
- 의미: 스타일 방향은 유효
- 단, 주인공 최종 얼굴 정본은 아직 미확정

---

# 2. HARD FAIL RULES — ALL ASSETS

다음 중 하나면 아름다워도 FAIL.

1. 기존 세계관/직업 기능을 무시함
2. 다른 핵심 자산과 구분이 안 됨
3. 외부 프랜차이즈/실존인물 복제 느낌이 핵심 정체성이 됨
4. 색/로고/텍스트를 제거하면 정체성이 사라짐
5. 설정과 다른 연령/체형/크기/기능으로 보임
6. 멋을 위해 무기/전술/전투메카 요소를 추가함
7. 세계 전체가 같은 AI 미형/기계/복도로 수렴함
8. spoiler class를 위반함

---

# 3. CHARACTER QA — V-A

First batch:
- C01 Protagonist
- C13 Arun
- C07 Gideon
- C11 Ivo

## 3.1 Same-condition test

네 인물은 동일 조건으로 비교한다.

- 같은 배경
- 같은 카메라 거리
- 같은 조명
- 중립 회색 계열 기본복
- 헤어스타일의 극단적 개성 최소화
- 소품 제거
- 정면 / 3/4 / 측면
- 작은 전신 실루엣

## 3.2 PASS criteria

각 인물은 다음 7축 중 최소 **4축 이상**에서 다른 세 명과 명확히 달라야 한다.

- 얼굴 길이/폭
- 턱/광대 질량
- 코 구조
- 눈/눈썹 구조
- 목/어깨/체형
- 자세/중심
- 머리 덩어리 형태

## 3.3 Pairwise gate

### C01 vs C13 Arun
Hard question:
`둘 다 비슷한 나이의 기술직 남성인데 머리/옷 없이도 다른 사람인가?`

### C01 vs C07 Gideon
Hard question:
`기디언이 단순히 늙은 주인공처럼 보이지 않는가?`

### C07 vs C11 Ivo
Hard question:
`둘이 단순히 지친 중년 남성 한 얼굴의 변형이 아닌가?`

## 3.4 Protagonist specific gate

C01 PASS requirements:
- 체감 37~39
- 45+처럼 보이면 FAIL
- photoreal actor portrait처럼 보이면 FAIL
- 지나친 아이돌/소년형도 FAIL
- 장편 주인공으로서 정돈감 + 현장 실무자 에너지 동시 존재
- 특정 인종으로 고정할 필요 없음
- A의 정돈감과 C의 실무감은 참고하되 얼굴 복제 금지

---

# 4. MACHINE QA — V-B

First batch:
- M01 crawler
- M02 mapping drone
- M03 utility tug
- M04 rescue skiff

## 4.1 Neutral test

모든 기체에서:
- color 제거
- logo 제거
- model name 제거
- 동일 배경/스케일 룰

## 4.2 PASS questions

### M01
`붙어서 구조물을 검사하는 기계로 읽히는가?`

### M02
`센서 시야/맵핑이 중심인 가벼운 기계로 읽히는가?`

### M03
`화물 하중/결합이 중심인 일꾼으로 읽히는가?`

### M04
`환자/구조 접근을 중심으로 설계된 기계로 읽히는가?`

Hard fail:
- 네 개가 모두 `박스+다리/바퀴`처럼 보임
- 색 없이는 구분 불가
- 전투기/장갑차/전투드론으로 보임

---

# 5. ENVIRONMENT QA — V-C

First batch:
- L01 Transfer
- L02 Midring
- L03 Garden
- L04 Med
- L05 Old Works

## 5.1 Recognition test

장소명, 텍스트 설명, 구역별 대표색을 제거한 상태에서 확인한다.

PASS:
- 5곳이 서로 구분됨
- 동시에 모두 Meridian의 건축/인터페이스 조상을 공유함

## 5.2 Hard questions

### Transfer
`사람/화물의 방향성과 교차가 공간 자체에서 보이는가?`

### Midring
`사람이 실제로 살고 아이가 다니고 소규모 서비스가 존재하는가?`

### Garden
`가짜 지구숲이 아니라 engineered openness로 보이는가?`

### Med
`비밀 연구소가 아니라 치료/재활/교육/가족이 섞인 공공공간인가?`

### Old Works
`폐허가 아니라 여러 세대의 수리와 유지가 겹친 일하는 공간인가?`

Hard fail:
- 모두 금속 복도
- 모두 컨셉아트 쇼룸처럼 사람이 없음
- 각 장소가 서로 다른 게임 faction map처럼 보임

---

# 6. COLLECTIBILITY QA — V-D

수집욕은 `예쁘다`와 다르다.

각 SIGNATURE 자산은 다음 중 최소 **3개**를 만족해야 한다.

1. label 없이 다시 알아볼 수 있다.
2. 다른 세대/상태를 나란히 보면 같은 family임을 알 수 있다.
3. 사용 흔적이 이야기를 암시한다.
4. 실물/모형/지도/설정집으로 더 보고 싶다.
5. 소유자/장소/직업과 연결된다.
6. 후속 state가 단순 cosmetic recolor가 아니다.

FAIL:
- 희귀도 색상 때문에 갖고 싶음
- 무기/전투력 때문에 갖고 싶음
- 캐릭터가 예쁘기만 하고 고유 silhouette가 없음
- 기체가 멋지지만 Meridian 세계와 관계없음

---

# 7. STYLE QA — V-E

현재 스타일 목표:
# **2D semi-real**

PASS:
- 얼굴/재질 정보는 충분함
- 선/형태 구분이 실사보다 명확함
- setting guide/artbook으로 확장 가능

FAIL LOW:
- 지나치게 photoreal
- 피부 질감이 캐릭터 디자인보다 앞섬
- 30대 후반이 과도하게 늙음

FAIL HIGH:
- 너무 소년/소녀 애니화
- 모든 성인의 체형/얼굴 나이가 20대처럼 수렴
- 직업적 물성이 사라짐

---

# 8. EXTERNAL REFERENCE QA

외부 작품/배우/게임/영화는 참고자료일 뿐이다.

최종 자산 설명이:
`A 배우 같은 얼굴`, `B 게임 같은 기체`, `C 영화 같은 도시`
없이는 성립하지 않으면 FAIL.

PASS 조건:
외부 이름을 지워도 다음으로 설명 가능:
- Meridian function
- morphology
- interface lineage
- use history
- material state
- story placement

---

# 9. QA RECORD TEMPLATE

```md
## [ASSET ID / VERSION]

Status: TEST-GENERATED

### Intended identity
- ...

### What worked
- ...

### Failure / collision
- ...

### Hard gate
- PASS / FAIL

### Collectibility read
- PASS / WATCH / FAIL

### Decision
- KEEP
- REVISE
- DISCARD

### Next prompt changes
- ...
```

---

# 10. CURRENT PROTAGONIST SAMPLE RECORD

## C01 — style calibration round

### Photoreal worker sample
Decision: **DISCARD**

Reason:
- older than intended
- too photoreal
- too weary
- weak IP/silhouette energy

### Proposal A
Decision: **KEEP AS STYLE CALIBRATION**

Strength:
- clean protagonist readability
- good concept-sheet organization
- attractive without being fully photoreal

Risk:
- too polished / generic handsome lead if copied literally

### Proposal C
Decision: **KEEP AS STYLE CALIBRATION**

Strength:
- stronger field-professional adult read
- more grounded than A

Risk:
- can become too hard/older if pushed further

### Current synthesis target
# `A의 정돈감 + C의 현장성`

Not frozen:
- exact face
- ethnicity
- nationality
- final hair
- final color palette
- protagonist name

---

# 11. PHASE GATES

## Gate VP-M1
13 empirical test subjects:
- 4 characters
- 4 machines
- 5 environments

Pass condition:
- no blocking collision
- style consistency holds
- each category can be reproduced from prompt/spec

## Gate VP-M2
SIGNATURE 16 identity plates.

Pass condition:
- recognizability
- lineage/state logic
- story fidelity
- no merch-first drift

Only after VP-M2:
`cinematic key art / cover / final palette family` work may begin.

---

# FINAL VERDICT

현재 Visual Production 시스템 문서화는 가능하다.
실제 비주얼 정본화는 아직 아니다.

이미지 대량 생성은 금지.
대표 샘플을 만들고 이 QA로 실패를 잡는 방식이 기본이다.
