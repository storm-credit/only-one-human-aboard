# QUANT — Ship Scale Stress Test v0.1

Status: `ORDER-OF-MAGNITUDE TEST / NOT CANON`

목적은 정확한 우주공학 설계가 아니라 **30만 명 + 농업 + 생활권이라는 설정이 대략적인 물리 규모에서 성립 가능한지** 확인하는 것이다.

---

# 1. Agriculture Baseline

NASA controlled-environment / bioregenerative life-support 연구의 현재 기준선 중 하나:
- 약 20~25 m² crop area / person: 산소 요구량 규모
- 약 40~50 m² crop area / person: 식이 칼로리 규모

이것은 미래 세대우주선의 확정값이 아니라 현재 연구를 이용한 sanity check.

## 300,000 population
50 m² × 300,000 = 15,000,000 m²

= **15 km² active crop canopy**

실제 작품에서는:
- 식이 다양성
- 경작 실패 여유
- 종자 보존
- 작업 통로
- 설비

를 고려해 **20~30 km²급 active agricultural area**를 설계 목표 범위로 두는 것이 안전하다.

정밀발효/배양육/조류 단백질을 함께 쓰므로 모든 식품을 작물면적으로 해결할 필요는 없다.

---

# 2. Metabolic Food Energy

1인 약 2,000~2,300 kcal/day를 단순 기준으로 두면 30만 명의 음식에 저장되는 평균 화학에너지는 수십 MW 규모.

하지만 작물 조명/냉각/물순환은 광합성 효율 때문에 훨씬 더 큰 전력을 요구한다.

Story-level assumption:

> 농업은 수백 MW ~ 수 GW급 전력 소비자.

따라서 세대우주선 전체는 **다중 GW급 지속전력**이 필요하다는 방향이 자연스럽다.

정확 출력은 핵융합 Tech Freeze 때 결정.

---

# 3. Rotation Check

회전 인공중력:

a = ω²r

반경 약 1 km에서 1g를 만들 경우 회전속도는 대략 **0.95 rpm**.

NASA의 인공중력 연구에서도 회전속도가 높아질수록 Coriolis/전정계 적응 문제가 중요해진다.

따라서 1 km급 대형 반경은 독자에게 과도한 설명 없이도 장기 거주용으로 합리적인 방향.

---

# 4. Habitat Layout 4 Designs

## Q1 — 3 × Large Cylinder

각 회전 원통:
- radius: ~1.0 km
- length: ~6 km
- inner surface: 약 37.7 km²

3개 합계:
- 약 **113 km²** 주요 내벽 표면

### Population Density
300,000 / 113 km² ≈ 2,650 persons/km²

이는 순수 도시밀도가 아니라:
- 주거
- 공원
- 학교
- 상업
- 일부 농업

을 포함한 gross scale.

농업 20~30 km²를 별도/다층 설비에 배치해도 충분한 규모.

### Strength
- 약 10만 명씩 서로 다른 큰 생활권 문화 가능
- 하나의 원통 고장 시 나머지 생활권 존재
- 8개 사회구역을 3개 원통 + 중앙척추에 분산 가능
- ‘우주선=대륙’ 체감에 충분

### Risk
구조물 자체가 매우 거대. 이 세계가 이미 성간 세대우주선을 건조할 문명임을 전제로 해야 함.

### Verdict
`CURRENT BEST SCALE CANDIDATE`

---

## Q2 — 2 × Extra-Large Cylinder

각:
- radius ~1.5 km
- length ~8 km
- surface ~75 km²

합계 ~150 km².

### Strength
- 0.8 rpm 이하 가능
- 넓고 지구 같은 경관

### Risk
- 두 생활권만 있으면 세계 정치/지역 다양성이 구조적으로 단순해질 수 있음
- 한 원통 고장 영향이 큼
- 거대구조 건설 부담 증가

### Verdict
`GOOD PHYSICS / WEAKER STORY MODULARITY`

---

## Q3 — 4 × Medium Cylinder

각:
- radius ~0.8 km
- length ~5 km
- surface ~25 km²

합계 ~100 km².

회전 ~1.05 rpm 수준.

### Strength
- 지역 다양성/모듈성 강함
- 정치적으로 4개 큰 생활권 구분 가능
- 사고 격리 쉬움

### Risk
- 연결축/베어링/구조 복잡성 증가
- 각 생활권이 충분히 거대한 세계처럼 느껴지는지 연출 필요

### Verdict
`STRONG ALTERNATIVE`

---

## Q4 — Giant Torus / Ring

하나 또는 두 개의 대형 토러스 생활권.

### Strength
- 이미지가 직관적
- 교통망 간단

### Risk
- 사회구획의 물리적 다양성이 약해질 수 있음
- 단일 대형 구조 고장 위험

### Verdict
`NOT CURRENT FAVORITE`

---

# 5. Recommended Scale v0.1

현재 추천:

> **3개의 약 1 km 반경 / 5~7 km 길이 회전생활원통 + 비회전 중앙척추 + 외곽 산업/방열구조**

정확 치수는 Freeze하지 않는다.

### Suggested Population Split Example
- Cylinder A: 110k
- Cylinder B: 105k
- Cylinder C: 70k
- Central spine / industry / specialist habitats: 15k

= 300k

이 분포 역시 가설.

---

# 6. Sector Mapping Candidate

기존 8구역은 반드시 8개의 물리 원통이 아니다.

예:

### Cylinder A — Civic Core
- 대원환 계열
- 행정/상업/대학
- 구환 일부

### Cylinder B — Bio / Family
- 녹환
- 유년원
- 식품/생태 연구

### Cylinder C — Production / Old City
- 제작환
- 구환의 오래된 공업도시
- 노동문화

### Central Spine / Outer Works
- 외주대
- 기억원의 핵심 서버/아카이브
- 선구역
- 반응로/항법/도킹

이렇게 하면 8개 문화권을 실제 우주공학 구조와 분리해 더 자연스럽게 만들 수 있다.

---

# 7. Travel Time

원통 길이 5~7 km + 중앙 연결축이라면 같은 생활권 내부 이동은 현대 도시 규모.

다른 회전원통 이동은:
- 지역교통
- 허브
- 회전/비회전 전환
- 보안/물류

때문에 의미 있는 시간이 걸릴 수 있다.

Story target:
- 같은 원통: 수십 분
- 다른 원통: 1~3시간급
- 외벽/산업부: 허가/환승 포함 더 오래

정확 교통시스템은 World Bible에서 설계.

이 정도면 지역문화가 분화될 사회적 거리도 만들 수 있다.

---

# 8. Power Order-of-Magnitude

## Biological metabolism
인구 자체의 대사 에너지는 수십 MW.

## Agriculture
인공조명/냉각/펌프를 고려하면 수백 MW~수 GW.

## Other major loads
- 제조
- 신체배양
- 데이터/스캔
- 생활 HVAC
- 물/공기처리
- 교통
- 추진/항법

따라서 설계 목표 가설:

> **평상시 수 GW ~ 10 GW대, 설치용량은 그보다 충분히 큰 다중반응로 체계**

정확 수치는 쓰지 않아도 이야기에는 충분하다.

---

# 9. Waste Heat Stress Test

수 GW급 전력을 사용하는 우주선은 결국 비슷한 규모의 열을 방출해야 한다.

따라서 대형 방열판은 배경 장식이 아니라 핵심 인프라.

Story consequences:
- 방열판 한 구역 손상 → 발전소는 멀쩡하지만 출력 제한
- 농업조명 감축 vs 제조라인 감축 선택
- 외주대 노동자의 중요성 증가
- 고온 산업열 루프와 저온 생활열 루프의 우선순위 충돌

방열판은 이 작품의 visually distinctive space infrastructure가 될 수 있다.

---

# 10. Agriculture Layout

20~30 km² active crop canopy는:
- 회전원통 표면 일부
- 다층 농업데크
- 전용 생태구역

으로 분산.

농업을 완전히 창고형 vertical farm으로 숨기지 않는다.

이유:
- 생활권의 풍경
- 휴식/문화
- 생물다양성
- 종자보존
- 목적지 생태 준비

를 위해 일부는 시민이 실제로 보는 녹지/농경지로 유지.

---

# 11. Failure Architecture From Quant Test

1. 농업구획의 조명전력 20% 삭감
2. 방열판 파손으로 산업/생활 전력 할당 갈등
3. 한 원통의 회전축 정비로 타 원통 대규모 임시이주
4. 수자원을 차폐층에서 농업으로 이동할지 논쟁
5. 중앙척추 교통사고로 두 생활권이 며칠간 고립
6. 반응로 정비 때문에 Full Continuity Scan 시설이 제한운영
7. 목적지 감속 단계에서 생활용 전력예산 축소

기술 설정이 실제 에피소드를 만든다.

---

# Red Team

## RT-Q-01
15 km² crop area는 현재 연구의 실험적 단순 기준인데 너무 낙관적이지 않나?

### Mitigation
작품 설계 목표를 20~30 km² 이상으로 잡고, 발효/배양식품과 비축을 함께 사용. 정확한 식단 계산은 Freeze 전 필요 시 별도 모델.

## RT-Q-02
113 km²에 30만 명이면 너무 넓지 않나?

### Answer
대륙처럼 느껴지게 할 목표에는 오히려 유리. 원통 내부에 농업/공원/산업완충/수자원시설이 포함되므로 도시만 계산하지 않는다.

## RT-Q-03
3개 원통이 너무 오닐 실린더 클리셰 아닌가?

### Required
최종 시각설계에서 전형적인 독립 오닐 실린더 3개가 아니라 하나의 세대우주선 프레임 안에 결합된 고유 구조로 재설계.

## RT-Q-04
세 원통이면 ‘8개 생활권’이 약해지나?

### Answer
생활권은 물리 모듈과 1:1 대응시키지 않는다. 서울의 여러 구가 한 지형 안에서 문화적으로 다른 것과 같은 구조.

---

# Verdict

30만 명 + 실제 생물학적 식사 + 대형 농업 + 회전중력은 **수 km급 거대 생활구조를 허용하는 성간 세대우주선 기술수준이라면 설정적으로 충분히 같은 범위에 놓을 수 있다.**

현재 Q1 ‘3 large cylinders’가 Story/Scale 균형에서 1순위지만 Canon 아님.
