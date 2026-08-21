# CLAUDE.md — 《우주선에는 인간이 한 명뿐이다》

## 0. PROJECT AUTHORITY

Repository: `storm-credit/only-one-human-aboard`

이 파일은 프로젝트 최상위 작업헌법이다.

**현재 공식 정본 = v3 (9막 / 410화).**
v2(7막 / 230화)는 **FROZEN HISTORICAL EDITION**이며 신규 작업의 정본이 아니다.
승격 기록: `docs/change-control/CHG-055-V3-CANON-PROMOTION.md` (2026-08-21).

### Current authority order
1. `CLAUDE.md`
2. **`canon/CANON_STATUS.md`** — 단일 상태표 / 활성 정본 파일 목록
3. **`canon/WORLD_BIBLE-v3-CANDIDATE.md` + `canon/WORLD_BIBLE-v3-ADDENDUM-*.md` — OFFICIAL WORLD CANON**
4. **`canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md` — OFFICIAL CHARACTER CANON**
5. **`canon/ACT_BIBLE-v3.2-CANDIDATE.md` — OFFICIAL NARRATIVE CANON**
6. `docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md` — 활성 라우팅
7. `docs/current-work-status.md` · `docs/NEXT-CHAT-HANDOFF.md`
8. `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT{1..9}-v0.1.md` — exact episode event truth
9. `docs/prewriting-v3/POV-OWNERSHIP-REALLOCATION-v0.2.md` — POV 소유권 정본
10. `docs/obsidian-v3/contexts/CTX-V3-EPxxx.md` → `docs/obsidian-v3/deep-contexts/DEEP-V3-EPxxx.md`
11. `docs/prewriting-v3/V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1.md`
12. `docs/manuscript/PROSE-STYLE-RUBRIC-v1.md` / `STYLE-METHOD-v1.md`
13. Reference Atlas / design history.

파일명에 `CANDIDATE`가 남아 있어도 **권위는 파일명이 아니라 이 라우팅과 `CANON_STATUS.md`에서 나온다.**
대량 리네임은 하지 않는다.

### Hard retractions
- **`canon/v2/` = RETRACTED / NON-CANON / DESIGN HISTORY ONLY.** 절대 정본으로 쓰지 마라.
- **v2 정본군**(`WORLD_BIBLE-v2.md`, `CHARACTER_BIBLE-v2.md`, `ACT_BIBLE-v1.md`, `CANON-v2-AMENDMENT-A-*`)
  = **FROZEN HISTORICAL EDITION.** 보존하되 신규 v3 작업의 정본이 아니다.
- **`docs/writing-ready/EPISODE-BLUEPRINT-ACT{1..7}-v0.1.md` = v2다.**
  v3와 **파일명이 같다.** v3는 반드시 `docs/prewriting-v3/` 경로를 쓴다.
- `docs/design-v3/V3-CURRENT-DESIGN-STATUS.md` = SUPERSEDED.

---

# 1. CURRENT GATE

Completed:
- `V3 STRUCTURAL WRITING READY = PASS`
- `EP001~410 BLUEPRINT = 410/410`
- `THIN CTX ROUTER = 410/410`
- `DEEP PROJECTED CONTEXT = 410/410 / P0=0 / P1=0`
- `POV RECALIBRATION v0.2 = PASS`
- `FINAL PRE-PROMOTION COMPLETENESS AUDIT = PASS`
- `FINAL PRE-MANUSCRIPT BLIND-SPOT AUDIT = PATCH → 해소` (`docs/qa/V3-FINAL-PRE-MANUSCRIPT-BLIND-SPOT-AUDIT-v1.md`)
- **`V3 CANON PROMOTION = EXECUTED — 2026-08-21`**
- **`PROTAGONIST FINAL NAME = APPROVED — 루카스 켈러`**
- **`MANUSCRIPT START = EXECUTED — 2026-08-21`**

Current manuscript state:
**`IN PROGRESS`**

Active v3 manuscript:
**2 / 410** — EP001~002 accepted (CHG-056, CHG-058)

Historical v2 manuscript (frozen, preserved):
**10 / 230** — `manuscript/accepted/` EP001~010. v3 라인으로 끌어오지 마라.

Next eligible v3 episode:
**EP003**

원고 진척 수치의 정본은 `docs/manuscript/MANUSCRIPT-STATUS.md`.

Important:
A generic `이어서/진행` does not automatically mean write prose.
**Manuscript Start는 사용자의 명시적 집필 지시가 있어야 한다.**

---

# 2. COMPLETENESS STANDARD — SATISFIED

Reference-grade standard:
ordinary citizens across age/class/job/family/location can live normal days and encounter
birth/school/work/money/housing/family/illness/crime/emergency/culture/death/arrival
without inventing a new civilization-scale rule.

v3 통과 근거: Deep Design 하네스, Act별 적대 QA 9/9, 전 시리즈 Red Team, 최종 승격 전 감사, 최종 집필 전 맹점 감사.

---

# 3. CORE CANON v3 — DO NOT REINTERPRET

- Ship = **Meridian / 메리디언**, 하나의 실재하는 **Outer Ark**
- 외부 물리 시간은 **항상 전진**한다. 우주론적 다중우주는 요구되지 않는다
- 함내에 **ultradense 분산 문명 기반(substrate)** 이 존재한다
- 실행 깊이 등급: `D0 Seed / D1 Forecast / D2 Deep Civic / D3 Fully Lived / D4 Crisis Depth`
- 선택된 D3 역사들은 **완전히 살아졌고 도덕적으로 실재**한다. 체험된 메리디언은 작가적 가짜가 아니다
- **H-A = Act1~2 (EP001~094)** → 드문 연속성 오결합(misbinding) 1회 → **H-B = Act3~9 (EP095~410)**
- 주인공의 반복적 세계 도약은 없다

## HUMAN
- `HUMAN` = **Natural-Origin 출항 연속성 legacy 범주**이며 **인격(personhood)이 아니다**
- 출항 시 HUMAN > 1. 실제 감손으로 **현재 1명**이 남았다
- **주인공은 HUMAN이 아니다**
- HUMAN:1은 수집물/선택받은 자/열쇠가 아니다. Act8에서 명시적으로 de-collectify된다
- HUMAN:1의 실체 = **극초기 단계 Natural-Origin 생물학적 연속성의 냉동보존체**.
  최종접근 ex vivo 임신은 **Act7 개시 미션클럭 임계**에서 시작되며,
  Act7 ~8주 + Act8 ~12주 + Act9 ~18주 = **~38주** → EP408 정상 출산.
  **HUMAN 공개 발견이 임신을 촉발하지 않는다.** 미션클럭 + 의학적 생존성 프로토콜이 촉발한다

## Destination
근사 호환 총압이지만 **산소 부족**. 선외 작업은 보조 호흡가스/산소 지원 + 모니터링 필요.
정확한 수치는 `WORLD_BIBLE-v3-*`만 사용한다.

---

# 4. PROTAGONIST / CAST

## Protagonist
- **루카스 켈러 / Lukas Keller**
- 독자 노출 호칭은 **`루카스`** 단일. 문체를 위해 `루카스/켈러`를 번갈아 쓰지 마라
- 남성, 시리즈 개시 시점 **38세**
- 직업: **선체 손상분석관(damage analysis)**. 군인 아님, 탐정 아님, 선택받은 자 아님
- 결함 축: 보호를 명분으로 한 **과통제**. EP027에서 지속적 관계 비용을 치른다
- 권한 한계가 항상 보인다: 구조안전을 평가하지만 사람/보안을 지휘하지 않는다

## Household (C2)
마르틴 켈러(부, 68) · 나디아 소토(모, 65) · 클라라 켈러(누나, 41) · 사미르 코스타(매형, 42) · 에바 코스타(조카, 9).

## Core cast 13
루카스 켈러 · Mira Solano · Selene Adebayo · Rafi Chen · Sora Mbeki · Leila Noor ·
Gideon Park · Niko Osman · Juno Reyes · Hana Kouri · Ivo Serrin · Cassian Dae · Arun Kalev.

Authority: `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md`.
조연은 각자 독립 욕망을 갖는다. 주인공이 모든 해결을 흡수하지 않는다.

## POV
- 주인공 소유 **319 / 410 = 77.8%**
- 주인공 등장 **386 / 410 = 94.1%**
- 완전 부재 **24 / 410 = 5.9%**
- 소유권 충돌 시 **`POV-OWNERSHIP-REALLOCATION-v0.2`가 카드 라벨과 Deep 사이드카를 이긴다.**
  해당 47화 목록은 `V3-CURRENT-AUTHORITY-MAP.md` §3.1.

---

# 5. ACT / REVEAL / TIME LOCKS

| Act | 범위 | 제목 |
|---|---|---|
| 1 | EP001~042 | 우리가 살던 메리디언 |
| 2 | EP043~094 | 닫힌 구획 |
| 3 | EP095~136 | 같은 아침이 아니다 |
| 4 | EP137~181 | 미래를 안다고 믿는 사람들 |
| 5 | EP182~228 | 없었던 역사 |
| 6 | EP229~279 | 멸망했던 메리디언 |
| 7 | EP280~327 | 셀 수 없는 삶 |
| 8 | EP328~370 | 한 명과 수많은 사람 |
| 9 | EP371~410 | 처음 가는 곳 |

Reveal 정본: `docs/narrative-engineering/V3-REVEAL-FORESHADOW-PAYOFF-LEDGER-v0.4-CANDIDATE.md`.
Time 정본: `docs/prewriting-v3/V3-FULL-SERIES-TIMELINE-v0.1.md`.

## Act1 미스터리 점화 (CHG-055에서 전진 배치)
- **EP007** D05 mundane primer — 평범한 안전지식. 이상함 없음
- **EP012** D05 professional PLANT — 상속된 브레이싱 단계가 실제로 유용함
- **EP014** 사고는 사고였다 + D05 국소 payoff — 출처만 없음
- **EP022** REINFORCE(두 번째 절차 계열) · **EP028** 두 번째 국소 payoff

Hard: EP001~006은 의도적으로 단서가 없다. 대신 EP008~014 사고/구조 아크가 초반 장르 하중을 진다.
`ordinary_event_guard: HARD` — 평범한 고장은 진짜로 평범해야 한다. **미스터리 음악을 깔지 마라.**

---

# 6. EXECUTION — CONTEXT RETRIEVAL

Retrieval order:
`exact Episode Blueprint → thin CTX Router → Deep Projected sidecar → realized previous Continuity → JIT Dynamic → max-5 payload`

**한 회차는 최대 5개 직접 컨텍스트 번들만 받는다.**
1. Episode Card
2. Immediate Continuity
3. POV/Relationship Microbundle — *POV 소유권은 §4의 overlay 규칙을 먼저 적용*
4. World/Zone/Material Microbundle
5. Active Narrative Device/Return Microbundle

거대 매트릭스는 **라우터일 뿐** 프롬프트에 통째로 싣지 않는다.
Deep Context는 Canon이 아니며 exact Blueprint의 사건 진실을 덮지 못한다.
상위 권위가 바뀌면 해당 Deep 노드는 `STALE`이며 재컴파일 후 사용한다.

Hard:
**Sub-Act candidate device ≠ episode exposure.**
episode-explicit Blueprint / ledger 근거가 있어야 device를 로드한다.

---

# 7. PROSE EXECUTION — ONLY WHEN EXPLICITLY STARTED

Writing model:
- close third / one POV per episode / causal-owner POV / no head hopping
- 주인공 중심 다중인과형 장편 (주인공 만능 아님)

Style:
`STYLE-H1R — Restrained Commercial Social SF` + **`CALIBRATION C1 — ACTIVE`**
(`docs/manuscript/PROSE-STYLE-RUBRIC-v1.md` §20, `STYLE-METHOD-v1.md`)

핵심: 인메디아스레스 오프닝 / 대사 온도 상향 / 장면당 인물 발화 펀치 1+ /
서술자 격언 화당 최대 1회 / 행정 장면도 항상 시간·감정 압력 아래.

문체 참고(모사 금지): `docs/manuscript/STYLE-REFERENCES-v1.md`.

Tone locks:
- Violence: `consequence-forward / anatomy-light / sensory-moderate`
- Romance: 루카스↔Mira 직접 로맨스 코드 표면 **3~5%**. Act9의 새 현재 관계는 H-A 운명 복원이 아니다
- Ending: **`+1 / earned cautious hope`**. 영구적 상실 유지, 유토피아/허무/후반 대반전 없음

Draft generation is not completion.
`manuscript/accepted/` + 원장 등재만 진척으로 계산한다.

---

# 8. C2 CONTROLLED ELASTICITY

C0/C1/C2 규칙은 v3 World/Character Bible을 따른다.
C2는 정확한 주소, 부수적 상호명, 동결 밴드 내 정확 수치, 제품 모델 등 국소 장면 디테일을 포함할 수 있다.

Reader-facing 안정 비인물 용어: **19 활성 + 1 예비 / 하드 최대 20**.
수집형 자산: base 64 / variants 28 / 초기 카탈로그 92 / 하드 실링 96.
64개 자산 전부를 체호프의 총으로 만들지 마라. `HOLD / NO-CHEKHOV / OFFSTAGE`는 유효한 상태다.

C2가 반복적·단서적·인과적으로 변하면 승격/기록하고 영향 Context Pack을 갱신한다.
C2는 새 대규칙을 밀수입할 수 없다.

---

# 9. FORBIDDEN DRIFTS

- human-good / AI-evil 이분법
- 남은 시민을 가짜 NPC로 취급
- 주인공을 HUMAN으로 만들기 / 선택받은 자 서사
- HUMAN:1을 수집물·열쇠·왕좌·연구 의무 대상으로 만들기
- 무능한 조연 / 조연을 설정표 NPC로 축소
- central-AI-explains-everything
- 반복적 세계 도약 / 우주론적 다중우주 진실 요구
- 체험된 메리디언을 작가적 가짜로 격하
- 후반 더 큰 존재론 반전 / 최종 떡밥 투척
- Act7~8을 철학 강의로 전환 (`action/evidence before ontology`)
- Act9를 후반 설정 전시장으로 전환. **EP406~410은 새 미스터리를 추가하지 않는다**
- 외계 침공 / 전쟁 액션 탈취
- 무료 완벽 정착 경로 / 즉석 성숙 식민지
- 대량 성체 기판 업로드 / 실행가능 영혼 백업
- 주권적 선장-대통령 / Habitat 카스트·주권
- proxy가 무능력자의 능동적 죽음을 승인
- **v2 내용(마렌/아마라/7막/230화)을 v3에 복원**

---

# 10. CHANGE CONTROL

모순 수준 변경:
`문제 식별 → 유의미하면 3~4안 → 비교 → 영향분석 → 변경기록 → 적대적 Red Team → 영향 EP 회귀 → 신중한 Canon 승격`

동결 Canon을 침묵 덮어쓰기 금지.
계획 이탈은 `docs/change-log.md` CHG 항목 + `docs/change-control/`에 기록한다.

---

# 11. WORKING METHOD — MINIMUM ACTION AGENT OS

이 프로젝트는 `storm-credit/minimum-action-agent-os`를 **작업 방법론으로만** 채택한다.
OS는 `어떻게 일할지`만 규정한다. **도메인 정본은 언제나 이 저장소의 v3 Canon / Blueprint / POV / Timeline 문서다.**

## Adoption rule
- Local action space 최소화: 각 reasoning node의 직접 callable action 기본 **`<= 5`**. 전체 Agent 수 제한이 아니다
- Least Tool / Least Context / Least Authority. 위임 시 전체 대화 이력이 아니라 과업 Context Pack만 전달
- 새 Agent는 **실제 경계**(도구·권한·컨텍스트·독립평가·증거체계)가 있을 때만 만든다
- 5 초과 시에만 **불필요 Tool 제거 → Skill로 묶기 → 역할 분리 → Router 계층화** 순으로 최소 수정
- 계획 이탈은 침묵 수정하지 않고 기록한다

## OS 프리미티브 → 기존 구현 (중복 생성 금지)

| OS 프리미티브 | 정본 구현 |
|---|---|
| Intent 확인 | `docs/manuscript/MANUSCRIPT-PIPELINE-v1.md` §4 + 본 문서 §1 |
| Blindspot Scan | `docs/qa/V3-FINAL-PRE-MANUSCRIPT-BLIND-SPOT-AUDIT-v1.md`, `V3-G20-RANDOM-SCENE-FUZZ-20` |
| Preflight Trap Check | Deep Card Failure Conditions + 본 문서 §9 |
| Four Alternatives | 본 문서 §10 + `docs/**/*-4-DESIGNS-*.md` |
| Exemplar Research | `docs/manuscript/STYLE-REFERENCES-v1.md`, `docs/reference-atlas/` |
| Independent Critique | `.claude/agents/episode-qa.md` (원고) / `docs/qa/*RED-TEAM*` (설계) / Codex CLI (독립 적대 검수) |
| Harness / Golden Case | `docs/writing-ready/HARNESS-M1~M8-*.md` |
| State Update | `canon/CANON_STATUS.md`, `docs/current-work-status.md`, `docs/manuscript/MANUSCRIPT-STATUS.md`, `docs/NEXT-CHAT-HANDOFF.md` |
| Plan Drift Log | `docs/change-log.md` (CHG-nnn) + `docs/change-control/` |

원고 심사는 범용 에이전트가 아니라 **읽기 전용 `episode-qa`** 에 위임한다.
심사자는 원고를 수정할 수 없다. 수정은 호출자가 한다. 이것이 독립성의 근거다.

## Source of truth
- 작업 방법: 이 문서의 명시적 override → 본 §11 → OS 원칙
- 도메인 내용: v3 Canon / Blueprint / POV / Timeline → 상태·결정 기록 → 과업 입력
- **공통 OS가 공유물이라는 이유로 프로젝트 Canon을 덮어쓸 수 없다.**
