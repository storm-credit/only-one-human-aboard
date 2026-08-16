# WL13 — Destination Resource & Arrival Timeline 4 Designs v0.1

Status: `DESIGN COMPARISON / PROVISIONAL HYBRID RECOMMENDATION / NOT CANON`

Purpose:
WL12에서 남은 P0인 `목적지 초기정착 자원 / 남은 항해기간 / 우주선 해체의 실제 이득 / 보존 시 실제 지연폭`을 정량 수준까지 내려 비교한다.

Important:
- 어떤 안도 CANON 아님.
- 목적지는 최종보스 맵이 아님.
- `우주선 보존 vs 행성 정착`을 버튼 두 개짜리 양자택일로 만들지 않는다.
- 초기정착의 병목은 단순 철/물의 총량보다 `전력 + 방열 + 정밀기계 + 로봇 + 공정설비 + 숙련인력 + 시간`으로 잡는다.
- 현지 ISRU가 장기적으로 대량 원료를 담당하고, 우주선 해체는 **산업 bootstrap 속도**를 좌우해야 한다.

---

# 0. Existing Constraints Restored

현재 선박 규모 후보:
- 인구 약 300,000
- 3개 대형 회전 Habitat + Non-Rotating Spine + Outer Works
- 생활/농업/산업 지속전력 수 GW~10GW대 후보
- 완전 폐쇄계 아님
- 수백 년 항해 후 우주선 자체가 도시/고향/역사공간이 됨

기존 H9 1순위:
- `이중유산 식민계획` + `우주선 자체가 이미 고향`
- 실제 목적지 존재
- 지구 복제품 낙원 금지
- 현재 시민을 퇴역/삭제하는 식민계획 금지

이 문서는 그 기반을 유지하면서 4개의 구조적으로 다른 자원/도착 모델을 다시 비교한다.

---

# 1. Science Guardrails

현재 실제 우주개척 연구에서 유효한 방향성:
- ISRU는 물/산소/연료/건설재를 현지에서 얻어 장거리 보급 의존을 줄이는 핵심 방향이다.
- 그러나 자원이 존재하는 것과 `어디에 얼마나 있고 실제로 채굴 가능한가`는 다른 문제다.
- 초기 정착은 채굴, 정제, 전력, 저장, 건설, 운송이 연결된 산업 사슬이 필요하다.
- 따라서 미래 식민선도 현지에 철과 물이 있다고 즉시 자립할 수는 없다.
- K형 왜성은 G형보다 수명이 길고 M형보다 고에너지 방사선 부담이 낮은 편이라 장기 거주 후보 별로 설계하기 좋다.

Reference baseline:
- NASA Lunar Surface Technology / ISRU
- NASA Overview: In-Situ Resource Utilization
- NASA Science: Comparison of G, K, and M Stars for Habitability

작품은 현재 기술의 정확한 확장이 아니라 미래기술 SF이므로 숫자는 `order-of-magnitude story model`로만 사용한다.

---

# 2. Shared Resource Model — What Actually Matters At Arrival

초기 식민지에 필요한 것은 단순 `건물 재료`가 아니다.

## R1. Power
초기 5천~2만 명 규모의 지상/궤도 정착지라도:
- 대기/수처리
- 채굴
- 정제/제련
- 농업
- 냉난방
- 로봇
- 운송
- 데이터/의료

를 동시에 돌리려면 수백 MW~수 GW급의 안정적 전력원이 필요할 수 있다.

Story target:
- bootstrap colony: `0.5~2 GW-class industrial power` 후보
- 확장 colony: `수 GW~10GW+` 후보

정확 출력은 Tech Freeze에서 다시 검증.

## R2. Heat Rejection
전력을 쓰면 폐열을 버려야 한다.
궤도 산업/밀폐 거주지에서는 대형 방열 시스템이 핵심 자산.

## R3. Precision Capital Stock
현지 암석으로 즉시 만들기 어려운 것:
- 고정밀 공작기계
- 반도체/센서 생산라인
- 로봇
- 펌프/밸브
- 고급 베어링
- 촉매
- 의료/생명공학 장비
- 반응로 핵심부
- 제어계

## R4. Bulk Feedstock
현지에서 얻기 쉬워야 하는 것:
- 물
- 산소/탄소/질소 원료
- 철/알루미늄/마그네슘/실리케이트
- 건축/차폐용 bulk mass

장기적으로는 현지 조달이 압도적으로 유리.

## R5. People / Time
가장 자주 빠지는 자원:
- 숙련 기술자
- 의료진
- 생태/농업 인력
- 정비 인력
- 관리자/교육자
- 가족이 이동을 받아들일 시간

즉 `100만 톤 장비`가 있어도 사회가 하루 만에 이전하지 않는다.

---

# 3. What Dismantling The Ship Actually Gives

우주선을 해체하면 얻는 것은 단순 고철이 아니다.

### High-value transplantable assets
- 소형/중형 발전 모듈
- 열교환기/방열판
- 정밀 제작라인
- 재활용/화학처리 공정
- 의료/배양 설비
- 대형 펌프/압축기
- 압력용기
- 전력변환/배전 장치
- 케이블/초전도체 후보
- 로봇/무인 운송체
- 부품창고

### Medium-value assets
- 외곽 구조재
- 차폐재
- 물/휘발성 비축
- 구형 산업모듈
- 빈 저장탱크

### Bad idea to treat as free resource
- 시민이 사는 Habitat 주거공간
- 핵심 회전구조
- 생태계 전체
- 모든 방사선 차폐층
- 모든 비상중복 설비

이것을 뜯으면 곧바로 `사람을 어디에 살게 할 것인가` 문제가 생긴다.

## Critical Rule
**해체율이 곧 식민속도는 아니다.**

어떤 5%를 떼느냐가 어떤 20%를 떼느냐보다 중요할 수 있다.

따라서 최종 갈등은 `선체 질량 % 투표`가 아니라 **구체적인 시스템별 이식 결정**이어야 한다.

---

# 4. Design A — Quiet K-Dwarf / Surface-First Temperate Basin

## Core Structure
가까운 조용한 K형 왜성의 온대 암석행성.
행성은 지구 복제품이 아니지만:
- 0.85~1.1g 범위 후보
- 안정적인 대기
- 대규모 물 저장고
- 현지 금속/실리케이트
- 장기 표면거주 가능성 높음

대기는 즉시 호흡 가능한 지구형으로 만들지 않는다.
초기에는 밀폐 거주지가 필요.

## Why This Destination
출항 당시:
- 더 가까운 M형 왜성 후보보다 항성활동 위험이 낮음
- 행성 질량/대기 보존 가능성 양호
- 물과 암석자원 징후
- 수백 년 뒤에도 안정된 항성 환경 기대

즉 `가장 가까운 곳`이 아니라 **가장 보수적으로 실패확률이 낮은 곳**을 선택.

## Timeline Candidate
- planned total voyage: 약 420~460년
- elapsed: 약 410~440년
- remaining: `10~14년`
- 현재는 이미 장기 감속 단계 진입

정확 cruise speed/추진계는 아직 Freeze하지 않는다.

## Current Observation Confidence
Mission planning confidence band 후보:
- 행성 존재/궤도/질량: 사실상 확정
- 대기 bulk composition: 매우 높은 확신
- 대규모 물: 높은 확신
- 장기 기후 안정성: 중상
- 실제 농업/토양 독성/지역재해: 중간
- 즉시 대규모 도시건설 가능성: 낮음~중간

## Preparation Start
- T-30y: 장기 관측/forward scout 데이터 반영 시작
- T-18y: 식민 산업설계 갱신
- T-12y: 감속과 동시에 detachable bootstrap kit 우선순위 결정
- T-5y: 착륙/궤도 인프라 최종 조립
- Arrival~+3y: 무인/소수 선발대
- +3~10y: 5천~3만 명 규모
- +10~30y: 대규모 이주 가능

## Resource Architecture
현지:
- 물/대기/암석은 풍부
- bulk construction은 빠르게 현지화 가능

우주선에서 필요한 것:
- 발전
- 방열
- 정밀 산업
- 의료/생명공학
- 로봇

## Preserve vs Dismantle
### Conservative
우주선 핵심 생활권 90%+ 보존.
- 표면정착은 안전하지만 느림
- 10만 명 규모까지 20~30년 이상 후보

### Balanced
산업/외곽 중복설비를 선택적으로 이식.
- 10만 명 규모까지 12~20년 후보
- 우주선은 여전히 독립된 도시로 존속

### Aggressive
생활권 지원계까지 뜯음.
- 5~10년 빠르게 대형 정착 가능
- 우주선 재난중복성/주거여유 급락

## Strength
- 독자 이해가 가장 쉬움
- 기존 H9와 잘 맞음
- 도착 자체가 확실한 보상
- SF 설명이 과도하게 주제를 먹지 않음

## Weakness
표면이 너무 좋으면 결국 `왜 배에 남아?`가 약해진다.

## SF Plausibility
`HIGH` — 미래기술 가정 안에서 가장 보수적.

## Long-form Durability
`HIGH`
- 감속 경제
- 선발대
- 토지/주거/출생
- 이주가족 갈등
- 선체 이식
- 첫 도시

## Social Conflict
`HIGH`
다만 시간이 지나면 표면정착이 정답처럼 보일 위험.

## Character Events
`HIGH`
가족 중 일부만 내려가거나, 복원대기/출생권이 행성 이주와 얽힐 수 있음.

## Ending Connection
`STRONG`
현재 시민의 고향을 지키면서 미래 식민지에 투자하는 문명선택으로 연결.

## Biggest Trap
**행성이 너무 좋으면 정착주의가 사실상 승리한다.**

---

# 5. Design B — K-Dwarf Resource Triangle / Orbit-First System Colonization

## Core Structure
목적지는 `행성 하나`가 아니라 하나의 K형 왜성계.

구성 후보:
- 거주가능 후보 행성 1개
- 물/휘발성 풍부한 소천체 또는 위성
- 금속자원 풍부한 소행성군/내행성 잔해

행성표면은 장기 목표지만 **첫 10~20년의 실질 정착지는 궤도/위성/자원거점과 함께 성장**.

## Why This Destination
출항 당시 최우선 기준이:
`행성의 낙원성`이 아니라 `한 시스템 안에서 문명을 자립시킬 자원 다양성`.

즉 실패해도 한 행성에 모든 것을 걸지 않는 계획.

## Timeline Candidate
- planned voyage: 약 430~480년
- elapsed: 약 410~450년
- remaining: `15~20년`

행성만 보는 A보다 약간 긴 준비기간을 줌.

## Current Observation Confidence
- 항성/행성계: 확정
- 주요 천체 질량/궤도: 확정에 가까움
- 물/금속 자원 존재: 높음
- 실제 채굴농도/접근성: 중간
- 행성표면 장기거주: 중상

## Preparation Start
- T-35y: 자원천체 우선순위 시뮬레이션
- T-20y: 궤도제련/정제 모듈 제작
- T-12y: 전력/방열/로봇 이식 목록 정치화
- Arrival~+2y: 궤도 depot + 무인 채굴
- +2~8y: 위성/궤도 산업거점
- +5~15y: 행성표면 정착 확대
- +10~30y: 현지 bulk 산업이 우주선 의존을 추월

## Resource Architecture
핵심은 `resource triangle`:
1. 행성 — 대기/중력/장기 생활
2. 물/휘발성 천체 — 물/추진제/화학원료
3. 금속 천체 — 구조/산업 bulk

## Preserve vs Dismantle
우주선을 거의 보존해도 **현지자원만으로 결국 성장 가능**.
문제는 bootstrap delay.

### Conservative
- 핵심 ship systems 유지
- 현지 산업 자립까지 15~25년
- 낮은 신규출생/복원 여력 유지기간 길어짐

### Balanced
- 외곽 산업 + 예비 발전/방열 일부 이식
- 현지 자립 8~15년

### Aggressive
- 주거 지원계 일부까지 이식
- 현지 자립 5~8년
- ship redundancy 훼손

## Strength
**가짜 양자택일을 가장 잘 피한다.**
선택지는:
- ship-home 유지
- orbital industry
- surface settlement
- 새 orbital habitat
- 다중거점 혼합

으로 늘어난다.

## Weakness
세계가 갑자기 태양계 개척물처럼 넓어질 수 있음.

## SF Plausibility
`HIGH`
현지 bulk resource 활용이라는 기본 방향이 강함.

## Long-form Durability
`VERY HIGH`
150~250화에 가장 많은 독립 사건을 제공.

## Social Conflict
`VERY HIGH`
- 누가 먼저 자원거점에 갈지
- 어떤 거점이 독립권을 얻는지
- ship 시민권과 surface 시민권
- 새 habitat 건설 우선순위

## Character Events
`VERY HIGH`
주인공 직업이 궤도/행성/ship 간 관할권과 연속성 사건으로 자연스럽게 이동 가능.

## Ending Connection
`VERY STRONG`
끝을 `배를 살릴까 행성을 택할까`가 아니라 **어떤 문명구조를 후손에게 남길까**로 확장 가능.

## Biggest Trap
**Scope Explosion.**
너무 많은 천체/도시/정치체를 만들면 핵심 인물과 Human/Personhood 테마가 묻힌다.

---

# 6. Design C — M-Dwarf Tidally Locked Terminator World

## Core Structure
더 가까운 M형 왜성의 조석고정 암석행성.

거주 적합지역은:
- 낮/밤 경계의 terminator corridor
- 지하/차폐형 도시

중심.

## Why This Destination
출항시대에는:
- 매우 가까움
- 물/대기 신호 강함
- 다른 장거리 후보보다 도달시간 짧음

때문에 선택.

## Timeline Candidate
- planned voyage: 약 250~320년
- elapsed: 대부분 완료
- remaining: `6~9년`

## Current Observation Confidence
- 행성 존재: 확정
- 물/대기: 높음
- 표면 거주가능성: 중간
- 항성 flare 장기위험: 여전히 큰 uncertainty

## Preparation Start
- T-40y: radiation/thermal settlement planning
- T-20y: 대형 차폐/열교환 시스템 배정
- T-8y: 사실상 작품 시작과 동시에 countdown

## Resource Architecture
현지 원료는 충분해도:
- radiation shelter
- thermal transport
- 전력 grid
- 밀폐 농업

비중이 매우 큼.

## Preserve vs Dismantle
우주선의:
- 물 차폐
- 열관리
- 반응로
- 지하/밀폐용 구조

를 이식하면 큰 시간단축.

보존을 강하게 선택하면 대규모 행성정착이 20~40년 늦어질 수 있음.

## Strength
- 공간적/시각적 개성이 강함
- 정착자원 갈등이 매우 선명
- 도착 countdown이 강한 물리압박 엔진

## Weakness
- 작품이 `M-dwarf settlement engineering` 이야기로 변할 위험
- 정착 기술이 Human/AI 사회미스터리보다 앞설 수 있음

## SF Plausibility
`MEDIUM-HIGH`
가능한 SF지만 flare/대기유지/조석고정 변수 부담이 A/B보다 큼.

## Long-form Durability
`HIGH`
그러나 사건의 상당수가 survival engineering으로 수렴할 수 있음.

## Social Conflict
`HIGH`
희소 안전지대/인프라 배분 갈등 강함.

## Character Events
`HIGH`
가족이 안전지대 quota와 얽히면 강함.

## Ending Connection
`GOOD`
하지만 최종 선택이 환경압력 때문에 사실상 강제될 위험.

## Biggest Trap
**핵심 작품이 다른 작품으로 변한다.**

---

# 7. Design D — Habitable World With Biosafety Delay

## Core Structure
조용한 K/G형 항성의 물-rich 행성.
인간 거주 물리조건은 A보다 오히려 좋지만, 장거리 관측에서 `비생명 화학인지 미생물권인지 확정되지 않는 biosignature`가 존재.

외계 지성체 없음.
외계 침략 없음.

## Why This Destination
출항 당시에는 생명신호가 불확실했고:
- 물
- 대기
- 중력
- 기후

이 최우선.

수백 년 뒤 관측기술이 좋아지며 오히려 생태/오염 문제가 새로 커짐.

## Timeline Candidate
- planned voyage: 약 400~460년
- remaining: `12~16년`

## Current Observation Confidence
- 물리적 거주가능성: 높음
- 생물학적 안전성: 낮음~중간
- 행성생태 훼손 없이 대규모 이주 가능성: 미확정

## Preparation Start
- T-30y: quarantine architecture
- T-15y: sealed settlement / orbital ecology plan
- Arrival~+10y 이상: 개방정착 여부 단계 검증

## Resource Architecture
행성 bulk resource는 풍부하지만 바로 쓸 수 없는 지역이 생김.

첫 정착은:
- orbital habitat
- sealed enclave
- sterilized industrial zones

비중이 큼.

## Preserve vs Dismantle
우주선은 `오염되지 않은 완성 생태계`이므로 보존가치가 A/B보다 더 높음.

반대로 대규모 sealed settlement를 빠르게 만들려면 ship 산업설비/방열/생태장비 이식이 필요.

## Strength
- 도착=정답을 막음
- 우주선의 생태적 고향가치 강화
- 악당 없는 선택 가능

## Weakness
- 외계 미생물/행성보호라는 **두 번째 대주제**가 생김

## SF Plausibility
`HIGH`

## Long-form Durability
`HIGH`

## Social Conflict
`HIGH`
정착권 vs 보존윤리 vs 시민의 생존/출생권.

## Character Events
`HIGH`
개인의 이주/출산/감염판정/격리 문제가 가능.

## Ending Connection
`GOOD`

## Biggest Trap
**Human/Personhood 작품이 Planetary Protection 작품으로 변함.**

---

# 8. Side-by-Side Comparison

| Axis | A Surface-First | B Resource Triangle | C Terminator | D Biosafety |
|---|---:|---:|---:|---:|
| SF plausibility | 9 | 9 | 7.5 | 8.5 |
| Core premise fit | 9 | 9.5 | 7 | 7.5 |
| 150~250화 durability | 8.5 | 10 | 8 | 8.5 |
| Social conflict | 8.5 | 10 | 9 | 9 |
| Character 사건 | 9 | 9.5 | 8.5 | 8.5 |
| Ending flexibility | 8.5 | 10 | 7.5 | 8 |
| Fake binary avoidance | 7.5 | 10 | 6.5 | 9 |
| Scope-control safety | 9 | 7.5 | 8 | 6.5 |

Current ranking:
1. **B — Resource Triangle / Orbit-First**
2. **A — Quiet K-Dwarf Surface-First**
3. D — Biosafety Delay
4. C — Terminator World

A alone is cleaner.
B alone is richer.
Recommended direction is **A+B controlled Hybrid**.

---

# 9. Recommended Hybrid H9R — Quiet K-Dwarf + Resource Triangle + Staged Settlement

Status: `PROVISIONAL RECOMMENDATION / NOT CANON`

## Destination
가칭 K2~K4V급의 조용한 K형 왜성계.
실제 명칭/별 이름은 World Bible에서 결정.

거리 후보:
`약 12~14 light-years`

행성:
- 0.85~1.1g급 암석행성 후보
- 안정적 대기
- 대규모 물
- 즉시 맨몸 생활 가능한 지구복제는 아님
- 밀폐 거주/대기처리 필요

동일 계에는:
- water/volatile-rich small body
- metal/silicate-rich asteroid or moon

가 최소 1개씩 있어 `resource triangle` 형성.

## Why Chosen
원래 탐사자들은 가장 가까운 행성보다:
1. 장수하고 비교적 안정된 항성
2. 지상중력/대기 유지 가능성
3. 물
4. 시스템 전체의 자원 다양성
5. 실패했을 때 orbital civilization으로 전환할 여지

를 우선.

즉 **목적지는 행성 하나가 아니라 문명을 다시 시작할 수 있는 별계 전체**였음.

## Voyage Timeline
추천 후보:
- planned total voyage: 약 `440~460년`
- 현재 elapsed: 약 `425~445년`
- remaining to system insertion: 약 `12~15년`

현재 1순위 숫자:
> **약 14년 남음**

이유:
- 250화 동안 목적지를 잊지 않게 할 수 있음
- 조카/가족 성장 체감 가능
- 감속/준비가 이미 현실정치가 됨
- 도착 후 1차 정착까지 본편에서 다룰 수 있음

## Deceleration
현재는 장기 감속이 이미 시작된 상태 후보.

정확 추진가속도는 아직 Freeze하지 않지만:
- 추진전력 증가
- 방열 capacity 압박
- 생활/산업 전력예산 조정

이 발생해 `목적지 준비 deadline`이 실제 생활사건을 만든다.

## Reconnaissance Timeline
- T-80~50y: fast scout/remote observatory package 분리 후보
- T-30y: 고해상도 자료가 식민계획에 본격 반영
- T-20y: surface/orbital candidate sites 공개 논쟁
- T-14y: 현재 본편 시점 후보, 감속 + allocation conflict
- T-8y: detachable bootstrap modules 최종 생산
- T-3y: local resource mapping 신뢰도 급상승
- T0: system insertion
- +0~3y: orbital depot / unmanned ISRU / power foothold
- +3~8y: 5천~2만 명 규모의 surface settlement 후보
- +8~20y: 정책에 따라 5만~12만 명 규모
- +20~50y: 다수 시민이 이동할 수도 있고, ship-city가 계속 존속할 수도 있음

정확 인구이동은 Act Architecture 후 조정.

---

# 10. H9R Resource Budget — Order of Magnitude

## Ship Mass
정확 총질량은 아직 미확정.
현재 3 Habitat + water/shielding + industry 규모를 감안하면:

> `10^12 kg-class` 이상 거대선 후보

즉 억~수십억 톤 스케일이 이상하지 않은 범위.

정확 수치는 별도 structural mass test 필요.

## Important Mass Buckets
### A. Civilizational Core Mass
- inhabited habitat structure
- water/radiation shielding
- agriculture/ecology
- critical thermal systems

쉽게 못 뜯음.

### B. Detachable Industrial Reserve
- 구형/중복 manufacturing modules
- spare radiator banks
- reserve power units
- chemical plants
- cargo tanks
- robots

처음부터 식민 이식 가능성을 염두에 둔 legacy hardware 일부가 남아 있을 수 있음.

### C. Precision Bootstrap Package
Story-order candidate:
`10^8~10^9 kg class` 고가치 설비가 수년간 단계적으로 이동할 수 있음.

중요:
이 질량 대부분은 벽돌이 아니라 **산업을 만드는 기계**.

### D. Local Bulk Materials
10~20년 뒤에는:
- 구조재
- 차폐재
- 물
- 산소/화학원료

대부분을 현지화하는 목표.

---

# 11. Cannibalization Bands — Not A Two-Button Choice

## Green Band — 5~8% Equivalent Mission Assets
대상:
- cargo reserve
- obsolete/duplicate industrial modules
- 일부 spare radiator
- detachable power modules

Effect:
- ship 시민생활 영향 제한적
- 현지 bootstrap 느리지만 안정
- 대규모 이주까지 +20~30년 후보

## Amber Band — 12~18%
대상:
- 주요 spare/industrial redundancy
- Outer Works 일부
- 선체 장기정비 여유 일부

Effect:
- local industry를 8~15년 빨리 self-sustaining 상태로 만들 수 있음
- ship의 사고복구 여유 감소
- maintenance rationing 발생

## Red Band — 25~35%
대상:
- Habitat support redundancy
- 대형 thermal/power assets
- 오래된 거주/산업구획 일부

Effect:
- 빠른 대규모 settlement
- ship-city의 일부 주민 강제이주/재배치 필요
- 한 번 실행하면 사실상 되돌릴 수 없음
- 재난 redundancy 급감

중요:
실제 의사결정은 퍼센트 하나가 아니라:
`어떤 reactor / 어떤 radiator / 어떤 factory / 어떤 archive cooling loop / 어떤 habitat support`를 떼느냐로 사건화.

---

# 12. Why Not Just Preserve The Ship And Mine Locally?

이 질문은 P0.

## Answer
그 선택은 **가능해야 한다.**
금지하면 가짜 갈등.

하지만 비용:
1. 처음 현지 광산을 파는 로봇 자체가 필요
2. 채굴물을 정제하는 공정이 필요
3. 공정을 돌리는 전력과 방열이 필요
4. 정밀부품을 생산하는 기계가 필요
5. 이 모든 생산망이 안정될 때까지 수년~수십 년 걸림

따라서 ship 완전보존 전략은:
- 실패가 아니라
- **느린 식민 + 낮은 인구성장 + 오래 지속되는 ship 자원긴축**

이라는 실제 비용을 가짐.

---

# 13. Why Colonize At All If The Ship Is Already Home?

행성정착이 도덕적 의무가 되면 안 됨.

정착의 실제 장점:
- 사실상 무제한에 가까운 bulk matter 접근
- 장기적으로 넓은 에너지/산업 base
- 인구 30만 capacity ceiling 완화
- 생태/유전 다양성 확장 가능
- 수백 년 노후 선체 하나에 문명 전체를 묶지 않음

ship 유지의 실제 장점:
- 이미 검증된 생태계
- 기존 도시/관계/법/역사
- 완성된 인프라
- 안전성이 알려진 환경

따라서 둘 다 합리적이어야 한다.

---

# 14. Third / Fourth Paths Must Exist

Final choice 후보는 최소 다음처럼 연속적이어야 함.

1. **Ship Home Priority**
   - ship 보존
   - small surface colony
   - 낮은 성장률

2. **Balanced Dual Civilization**
   - ship + orbit + surface 공동 성장
   - 중간 속도

3. **Surface Acceleration**
   - 대규모 산업 이식
   - 빠른 식민
   - ship 기능 축소

4. **New Orbital Habitat Path**
   - asteroid resources로 새 habitat 건설
   - planet 의존 최소화
   - 가장 긴 bootstrap time

즉 final argument는:

> `어디에 살 것인가?`

보다

> **`누구의 현재를 얼마나 깎아 누구의 미래를 얼마나 빨리 만들 것인가?`**

가 된다.

---

# 15. 150~250 Episode Event Generation Check

H9R은 최소 6개의 사건군을 제공.

## Phase 1 — T-14~T-10: Deceleration Society
- 추진/방열 우선순위
- 생활전력 감축
- 산업시설 이식 후보 선정
- 이주 신청/거부

## Phase 2 — T-10~T-6: New Data Changes Old Plans
- 예상 자원광맥 수정
- settlement site 변경
- 이미 투자한 세력의 손실
- 가짜/오래된 식민권 계약

## Phase 3 — T-6~T-2: Irreversible Preparation
- 특정 공장 해체
- worker relocation
- archive cooling budget
- restoration capacity와 식민공장 생산 충돌

## Phase 4 — T-2~Arrival: Mission Law vs Civic Law
- 구식 도착 프로토콜 부활
- 누가 자원결정을 최종 승인하는가
- C8 natural-origin 분류가 상징/법률폭탄이 됨
- C8에게 실제 관리자키는 없음

## Phase 5 — Arrival~+5y: First Infrastructure
- 궤도 사고
- first surface death/birth
- local resource failure
- ship과 colony의 법적 동일성/시민권

## Phase 6 — +5~20y: Two Homes Become Real
- 가족 분리
- 조카 세대의 정체성
- colony-born 시민
- ship-born vs surface-born 문화차
- restoration/continuity precedent가 새 환경에서 달라짐

### Verdict
`PASS candidate`

목적지가 단순 후반 배경이 아니라 초중후반 모두 사건을 공급.

---

# 16. Character / Theme Connections

## Protagonist P
현장 연속성 심사관은:
- ship/colony 관할권
- 이주 중 사망/복원
- family custody across settlements
- old mission law

를 통해 목적지 사건과 자연스럽게 연결.

## S / N Family
가족이:
- 누가 ship에 남을지
- 누가 colony로 갈지
- 친권/보호권이 다른 jurisdiction에서 어떻게 변할지

로 개인갈등을 유지 가능.

## Rival R
자원배분 자체보다:
- 시민권
- 절차
- 이주권
- old mission authority

를 공격하게 하면 정치논문 캐릭터화를 피할 수 있음.

## C8-B
C8은:
- 특별능력 없음
- 목적지 인증키 아님
- 식민선 command authority 없음

하지만 구식 분류가 살아나면:
- `human colonist`
- `civic person`
- `seeded-origin descendant`

의 법적 문구 충돌에서 상징적 폭발점이 될 수 있음.

핵심은 C8 자신도 그 분류를 원치 않거나 가족에게 해가 된다고 느낄 수 있다는 점.

---

# 17. Ending Connection

H9R은 결말을 즉시 확정하지 않지만 다음 4개 ending architecture를 열어 둔다.

- ship을 역사도시로 유지 + surface expansion
- ship 일부를 해체해 새로운 orbital/surface network로 재구성
- 두 정치체가 분리되지만 mutual resource covenant 체결
- 새 habitat를 만들어 `ship vs planet` 구도를 제3의 문명형으로 해체

좋은 결말은 하나의 버튼 선택보다:
- 이미 발생한 이전 결정
- 해체된 설비
- 이동한 가족
- 새로 태어난 세대

때문에 **완전히 되돌릴 수 없는 누적 결과**가 되어야 한다.

---

# 18. Red Team

## RT-D13-01 — Why Didn't They Decide This 100 Years Ago?
Severity: `P0 if unresolved`

Answer candidate:
과거 세대는 doctrine을 정했지만 구체적 자원배분은:
- 현재 ship condition
- 최신 target data
- 현재 population
- current industrial redundancy

가 있어야 결정 가능.

따라서 과거계획은 방향이고 현재세대가 실제 비용을 지불.

## RT-D13-02 — Why Not Preserve Everything And Wait?
Severity: `P0`

Answer:
가능하나:
- population ceiling
- restoration/birth resource competition
- aging ship maintenance
- slow industrial bootstrap

비용이 수십 년 지속.

## RT-D13-03 — Is Ship Aging A Fake Countdown?
Severity: `P1`

Guardrail:
`5년 안에 배가 터진다` 금지.
우주선은 여전히 장기 존속 가능하지만 유지비가 점점 커짐.

## RT-D13-04 — Local Resources Make Ship Dismantling Meaningless
Severity: `P0`

Repair:
갈등을 bulk material이 아니라 `capital equipment / power / thermal / production bootstrap`로 이동.

## RT-D13-05 — B Turns Into The Expanse-Like Multi-Polity Sprawl
Severity: `P1`

Guardrail:
본편 250화 안에서는:
- ship
- primary planet
- 1~2 orbital resource nodes

까지만 핵심 무대로 제한.

## RT-D13-06 — Arrival Protocol Makes C8 A Chosen One
Severity: `P0`

Guardrail:
C8에게:
- command key
- override
- biometric lock
- genetic authorization

을 주지 않는다.

C8의 중요성은 **분류가 사회에 끼치는 의미**뿐.

## RT-D13-07 — 14 Years Is Too Long For Tension
Severity: `P1`

Repair:
도착 자체가 deadline이 아니라:
- T-12 industrial allocations
- T-8 dismantling
- T-5 settlement kit lock
- T-2 mission-law transition

처럼 여러 irreversible deadline을 둔다.

## RT-D13-08 — 14 Years Is Too Short For 250 Episodes
Severity: `P1`

Answer:
본편이 매일 연속이 아니라:
- 사건 사이 수주/수개월
- 일부 phase time skip
- arrival 이후 수년

을 포함하면 가능.

Character ages/relationship arc에서 검증 필요.

---

# 19. Current Verdict

## Recommended Hybrid
**H9R — Quiet K-Dwarf System + Resource Triangle + Staged Settlement**

Why:
1. 기존 H9 B+C의 강점을 유지
2. 행성을 정답으로 만들지 않음
3. local ISRU 때문에 ship 해체가 무의미해지는 구멍을 막음
4. 해체의 실제 가치를 `산업 bootstrap`으로 정의
5. 14년 countdown을 여러 중간 deadline으로 쪼갬
6. ship / orbit / surface의 3단계 사회변화를 만들어 150~250화 사건을 공급
7. C8을 관리자키로 만들지 않고도 구식 도착법과 연결 가능

## Status
`PROVISIONAL RECOMMENDATION / NOT CANON`

P0 remaining before promotion:
1. ship structural mass order-of-magnitude deeper test
2. arrival propulsion/deceleration sanity check
3. H9R을 C-full Act에 넣었을 때 150~250화 rhythm regression
4. C8 reveal과 old mission law가 chosen-one 구조가 되지 않는지 재검증

Do NOT promote to CANON yet.
