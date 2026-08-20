# V3 VISUAL PRODUCTION INDEX v0.1

Status: `ACTIVE VISUAL-PRODUCTION ROUTER / NOT CANON / NO PROSE / ART NOT FROZEN`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. 현재 상태

# **VISUAL PRODUCTION SYSTEM = DOC-READY**
# **MASS IMAGE GENERATION = NOT REQUIRED / NOT DEFAULT**
# **EMPIRICAL VISUAL QA = TARGETED / OPEN**

현재 목표는 이미지를 많이 만드는 것이 아니라, 다른 이미지 도구를 사용해도 같은 세계/캐릭터/기체를 재현할 수 있는 **Production Specification**을 유지하는 것이다.

---

# 1. 읽는 순서

## 1 — 전체 미술/제작 원칙
`V3-VISUAL-PRODUCTION-BIBLE-v0.1.md`

무엇을 정의하는가:
- 2D semi-real 방향
- A/C 주인공 샘플에서 가져올 것/버릴 것
- 캐릭터/기체/배경/소품 제작 규칙
- Identity Lock vs Shot/State 분리
- 파일/버전 규칙
- mass-generation stop rule

## 2 — 프롬프트 구조
`V3-IMAGE-GENERATION-PROMPT-PACK-v0.1.md`

무엇을 정의하는가:
- 공통 style lock
- negative constraints
- 캐릭터/기체/배경/소품 master template
- same-face test template
- lineage comparison template

## 3 — 64/92 실제 생산 범위
`V3-VISUAL-ASSET-MANIFEST-v0.1.md`

무엇을 정의하는가:
- 64 base assets
- 28 variants
- 92 internal catalog target
- 96 hard ceiling
- 각 ID별 deliverable / status / spoiler class
- VP-M1 / VP-M2 production milestone

## 4 — 첫 실증 테스트의 고정값
`V3-VP-M1-IDENTITY-LOCKS-v0.1.md`

무엇을 정의하는가:
- C01/C13/C07/C11 얼굴·체형·자세 차이
- M01~M04 기능 기반 실루엣
- L01~L05 공간 문법
- 동일 조건 비교 규칙

## 5 — 바로 복붙 가능한 13개 입력
`V3-VP-M1-READY-TO-RUN-PROMPT-CARDS-v0.1.md`

무엇을 정의하는가:
- 캐릭터 4
- 기체 4
- 배경 5
- tool-agnostic ready prompt

## 6 — 생성 결과 판정
`../qa/V3-VISUAL-PRODUCTION-EMPIRICAL-QA-v0.1.md`

무엇을 정의하는가:
- same-face
- same-machine
- same-corridor
- collectibility
- style fit
- 외부 레퍼런스 과의존
- KEEP / REVISE / DISCARD

---

# 2. 현재 주인공 비주얼 상태

최근 이미지 생성은 **방법을 검증하기 위한 샘플**이었다.

결과:
- photoreal older-worker sample = DISCARD
- Proposal A = KEEP AS STYLE CALIBRATION
- Proposal C = KEEP AS STYLE CALIBRATION

현재 synthesis:
# **A의 정돈감 + C의 현장성**

그러나 아직 미확정:
- exact face
- ethnicity
- nationality
- hair
- palette
- protagonist name

사용자는 주인공이 한국인/동양인일 필요가 없다고 명시했다.
시각 제작 시스템은 특정 인종을 기본값으로 고정하지 않는다.

---

# 3. 언제 이미지를 생성하는가

이미지 생성은 다음 질문이 있을 때만 한다.

- 두 캐릭터가 정말 다른 얼굴인가?
- 두 기체가 색 없이도 구분되는가?
- 두 장소가 같은 복도처럼 보이지 않는가?
- SIGNATURE 자산이 실제로 기억되는가?
- 표지/키아트 제작이 실제로 필요한가?

이미지 생성하지 않는 이유:
- 그냥 보고 싶어서
- 더 멋진 랜덤 결과가 나올 것 같아서
- 92 슬롯을 채우기 위해서

---

# 4. 현재 VP-M1 대상

## Character
- C01 Protagonist
- C13 Arun
- C07 Gideon
- C11 Ivo

## Machine
- M01 Structural Crawler
- M02 Mapping Drone
- M03 Utility Tug
- M04 Rescue Skiff

## Environment
- L01 Transfer
- L02 Midring
- L03 Garden
- L04 Med
- L05 Old Works

13개는 **실증대상 숫자**이지 즉시 생성수량이 아니다.

---

# 5. 다음 작업 기본값

현재 Visual Production 문서 시스템은 충분히 구성되었다.

따라서 generic `진행/이어서`에서:

1. 특정 이미지 도구가 정해졌다면 → 이 Master Prompt를 해당 도구 syntax에 맞춘 adapter 작성
2. 실제 visual collision 검증이 필요하다면 → 최소 샘플만 생성
3. 이미지 작업이 당장 필요 없다면 → 더 이상 이미지 쪽을 확장하지 않고 C2/naming/promotion 준비로 복귀

---

# 6. Authority boundary

이 폴더의 문서는 **production authority**이지 official story Canon이 아니다.

- story Canon promotion = 별도 explicit gate
- final visual art Freeze = VP-M1/VP-M2 이후
- prose start = 별도 manuscript gate

---

# FINAL

이제 이 프로젝트의 시각/IP 작업은:

> **레퍼런스를 많이 모으는 단계도 아니고, 이미지를 많이 뽑는 단계도 아니다.**
>
> **잘 정의된 자산을 필요할 때 재현하고 검증할 수 있는 생산 시스템 단계다.**
