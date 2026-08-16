# H9R Structural Mass / Propulsion-Deceleration Sanity v0.1

Status: `ORDER-OF-MAGNITUDE QA / PROVISIONAL REPAIR / NOT CANON`

Purpose:
H9R의:
- 약 12~14 ly 목적지
- 전체 440~460년 항해
- 현재 약 14년 남음
- 3 Large Habitat + Spine/Outer Works

가 물리적으로 서로 같은 범위에 놓일 수 있는지 검증한다.

정확 우주선 공학 설계가 아니라 Story-level P0 sanity test다.

---

# 1. Primary External Baselines

## NASA NTRS — Fusion Propulsion System Requirements for an Interstellar Probe
NASA/JPL 1963 연구는 fusion interstellar propulsion에서 **fusion plasma에서 chamber wall로 들어가는 열을 버리기 위한 radiator weight/size**를 주요 제한으로 지적.

Implication:
`핵융합 추진 = 폐열문제 없음` 금지.

## NASA NTRS — Use of Magnetic Sails for Advanced Exploration Missions
Magnetic sail은 interstellar medium/solar wind와 상호작용해 drag를 만들며, 고속 성간선의 braking concept으로 제안됨.

Implication:
propellantless braking 개념은 SF 근거가 있지만, 본 작품의 trillion-kg급 선박에 그대로 확대해 공짜 브레이크로 쓰면 안 됨.

## Perakis & Hein — Magnetic + Electric Sail Deceleration
수-ton급 probe의 0.05c 감속에도 수십 년 규모가 나오는 연구 사례가 있음.

Implication:
Magsail을 10^12 kg급 세대선의 주 braking system으로 단순 scaling 금지.

## NASA Habitat / Radiation Research
- habitat pressure/gravity/shielding 조건이 구조질량을 크게 바꿈.
- water/polyethylene 등 hydrogen-rich multipurpose shielding이 유리.
- 장기 deep-space GCR은 단순 얇은 금속벽으로 해결되지 않음.

## Relativistic / Fast Interstellar ISM Studies
고속 성간선은 interstellar gas/dust impact를 무시할 수 없음.

Implication:
forward ram shield / sacrificial shielding / charged-particle deflection architecture 필요.

---

# 2. Distance / Time Check

Candidate midpoint:
- distance: `13 ly`
- cruise velocity: `0.03c`
- acceleration duration: `14 years`
- deceleration duration: `14 years`

0.03c를 14년에 걸쳐 바꾸는 평균가속도:

> 약 `0.020 m/s²`
> 약 `0.0021 g`

14년 acceleration 동안 이동거리:

> 약 `0.21 ly`

14년 deceleration도 약 0.21 ly.

13 ly에서 나머지 cruise distance:

> 약 `12.58 ly`

0.03c cruise time:

> 약 `419 years`

총:

> `14 + 419 + 14 ≈ 447 years`

즉 H9R의:
- 12~14 ly
- 440~460년
- 14년 남은 시점에서 장기 감속 시작

은 **서로 놀랍도록 잘 맞는 order-of-magnitude 조합**.

### Verdict
`TIMELINE PHYSICS = PASS CANDIDATE`

정확 항법/추진 profile은 아직 Freeze 금지.

---

# 3. Rotation / Acceleration Interaction

Habitat spin gravity ~1g에 비해 axial deceleration ~0.002g는 매우 작음.

따라서 생활권 주민이:
- 바닥이 크게 기울거나
- 일상중력이 눈에 띄게 변하는

효과는 없어야 함.

감속의 생활압력은 중력변화가 아니라:
- propulsion maintenance
- outer-work exclusion
- thermal architecture
- resource diversion
- vibration/noise windows
- risk reserve

에서 발생하는 편이 자연스러움.

---

# 4. Ship Mass Envelope

기존 후보:
3 cylinders, each roughly:
- radius ~1 km
- length ~6 km

합계 cylindrical inner surface:
> 약 `113 km²`

총 enclosed geometric volume:
> 약 `56.5 km³`

### Atmosphere
Earthlike/sub-Earth pressure atmosphere density order를 쓰면 전체 atmosphere mass는 대략:
> `수 × 10^10 kg`

즉 공기만으로 10^12 kg이 되지는 않음.

### Radiation / Multi-use Shield
전체 외피/끝단에 수백~수천 kg/m² order의:
- water
- polymer
- consumables
- structural mass

를 multipurpose shielding으로 배치하면:
> `10^11 kg order`가 쉽게 나옴.

### Other Major Mass
- primary structure
- floors/buildings
- agriculture
- reservoirs
- machinery
- industrial feedstock
- radiators
- propulsion system
- forward ram shield

을 더하면 inhabited dry complex는:

> **low `10^12 kg-class`**

이 충분히 가능한 story envelope.

정확 후보 범위는 일부러 넓게:
> `~0.5–3 × 10^12 kg dry/civil complex`

정도로만 둔다.

남은 deceleration propellant를 포함한 arrival-phase gross mass는:
> `few × 10^12 kg`

까지 커질 수 있음.

### Verdict
기존 `10^12 kg-class`는 폐기할 필요 없음.
다만 `정확히 10^12 kg`처럼 쓰면 안 됨.

`MASS SCALE = PASS CANDIDATE / WIDE BAND`

---

# 5. Propulsion Energy Scale — Critical Repair

1×10^12 kg ship at 0.03c kinetic energy:

> 약 `4 × 10^25 J`

14년 평균으로 나누면:

> 약 `9 × 10^16 W`

ship mass가 3~5×10^12 kg이면:

> `~3 × 10^17` to `5 × 10^17 W`

order.

즉 propulsion power scale은:
> `10^17~10^18 W class candidate`

civilization 생활전력:
> `10^9~10^10 W class`

보다 약 7~8 orders larger.

## P0 Finding
기존의:
> 감속 추진 때문에 생활전력 몇 GW가 부족해진다

라는 식의 직접 에너지 경쟁은 **물리 규모가 맞지 않는다.**

### Required Repair
추진계와 civil grid를 분리.

propulsion energy 대부분은:
- fusion products
- reaction mass exhaust

로 직접 빠져나가야 함.

civil grid는 propulsion의:
- control
- pumps
- magnetic systems
- support equipment
- maintenance

auxiliary load 일부만 부담.

---

# 6. What Deceleration Actually Costs Society

감속이 생활을 압박하는 진짜 경로를 다음으로 변경 추천.

## C1 — Thermal Geometry
propulsion radiators / civil radiators의:
- orientation
- shadowing
- safe separation
- coolant maintenance

가 충돌.

엔진을 오래 돌릴수록 Outer Works의 접근/정비계획이 달라짐.

## C2 — Propellant / Reaction Mass
남은 추진제는 엄청난 전략자산.

- 도착 braking reserve
- emergency maneuver reserve
- 일부 future orbital industry feedstock

가 경쟁할 수 있음.

## C3 — Manufacturing Capacity
감속계 유지에 필요한:
- superconductors
- nozzle/chamber parts
- pumps
- radiator panels

를 만들면 colony bootstrap module 생산이 늦어짐.

## C4 — Human Labor
Outer Works / propulsion specialists가:
- civil maintenance
- colony preparation

에 동시에 투입될 수 없음.

## C5 — Safety / Exclusion
엔진 가동 시:
- 일부 exterior work 중단
- docking windows 제한
- sensor/communications geometry 변화

가능.

## C6 — Redundancy Burn-Down
감속 과정에서 spare/radiator/reactor redundancy를 소모하면:
`도착 시 ship을 얼마나 오래 고향으로 유지할 수 있나`가 악화.

### Story Improvement
감속과 정착준비가 경쟁하는 자원은 `전기 몇 GW`보다:
> **부품 / 열관리 / 인력 / spare / 반응질량 / 정비시간**

으로 두는 것이 훨씬 자연스러움.

---

# 7. Propulsion Architecture 4 Designs

## P-A — Dedicated Fusion Pulse / Direct-Exhaust Drive

### Concept
성간 추진용 초고출력 fusion drive가 civil reactors와 별도.
Fusion products / heated reaction mass를 직접 exhaust.

### Strength
- 가장 단순
- 0.03c mission과 직결
- 14년 low-g deceleration 설명 쉬움
- 목적지 인프라 없이 독립 도착 가능

### Weakness
- 10^17~10^18 W scale
- chamber/nozzle heat가 극단적
- effective exhaust velocity가 수% c급이어야 propellant ratio가 감당 가능

### Rocket-Equation Story Check
Δv ≈ 0.03c일 때:

if effective exhaust velocity:
- 0.03c → decel start/final mass ratio ~2.7
- 0.05c → ~1.8
- 0.08c → ~1.45
- 0.10c → ~1.35

즉 propulsion tech 자체가 `few-percent-c exhaust` class여야 함.

이것은 큰 SF 가정이지만 **0.03c 세대우주선을 이미 허용한 순간 필요한 가정**.

### Verdict
`CURRENT BEST BASE`

---

## P-B — Fusion + Magnetic Sail Major Braking

### Concept
고속에서 magsail이 ISM drag를 사용해 큰 비율의 deceleration 담당.
Fusion은 저속/최종 insertion.

### Strength
- onboard propellant 절약
- braking이 visually distinctive

### Weakness
현재 연구의 promising cases는 훨씬 작은 probe.
10^12 kg급으로 scaling하면 sail field/coil size/mass 불확실성이 너무 큼.

### Verdict
`DO NOT USE AS PRIMARY BRAKE`

가능한 역할:
- charged-particle shielding
- minor velocity trimming
- stellar-wind maneuver support

정도.

---

## P-C — Origin Beamed Acceleration + Onboard Fusion Deceleration

### Concept
출항시 태양계의 거대 beam infrastructure가 acceleration을 도와 departure propellant를 절약.
도착은 onboard fusion.

### Strength
- 출발 mass ratio 완화 가능
- 원래 문명의 mega-engineering 느낌

### Weakness
- 작품에 필요 없는 origin infrastructure 설정 증가
- 현재 story에 사건을 거의 만들지 않음
- arrival P0는 여전히 fusion으로 해결해야 함

### Verdict
`POSSIBLE BACKGROUND / NOT NEEDED TO FREEZE NOW`

---

## P-D — Precursor-Built Destination Brake

### Concept
수십 년 먼저 도착한 빠른 무인 precursor가 target system에서:
- beam
- mass-driver
- magnetic infrastructure

를 구축해 main ship 감속 보조.

### Strength
- onboard energy/propellant 부담 완화 가능
- scout program과 연결

### Fatal Risks
- 목적지에 이미 거대산업이 있다는 새 전제가 필요
- precursor 실패 시 mission 전체 붕괴
- `왜 그 로봇이 식민지도 다 만들지 않았나?` 문제
- AI/자동화 scale P0 추가

### Verdict
`REJECT AS CURRENT BASE`

작은 navigation beacon / resource survey infrastructure만 허용 가능.

---

# 8. Recommended Propulsion Hybrid H9R-P1

Status: `PROVISIONAL / NOT CANON`

Base:
**P-A Dedicated Fusion Direct-Exhaust Drive**

Allow:
- magnetic fields / sail-like structures as charged-particle shielding or minor trim
- departure acceleration history는 나중에 필요하면 P-C 요소

Do NOT rely on:
- magsail as free primary brake
- destination mega-infrastructure

Minimum story rules:
1. cruise ~0.03c candidate
2. acceleration/deceleration ~14 years each candidate
3. axial accel ~0.002g candidate
4. propulsion plant is physically/energetically separate from civil grid
5. propulsion waste heat is serious and has dedicated thermal architecture
6. civil pressure comes through parts/heat geometry/labor/spares/propellant, not direct energy subtraction

---

# 9. NEW P0 — Interstellar Ram Shield

At ~0.03c:
- gas/dust impacts are hypervelocity
- neutral dust cannot be solved by magnetic fields alone

따라서 forward protection은 선택이 아니라 필수.

## Candidate Architecture
- ship long-axis aligned with travel direction
- forward sacrificial multi-layer shield
- ice/water/graphite/polymer/ceramic mass candidate
- spaced bumpers / replaceable blocks
- magnetic/electric deflection for charged particles
- small forward scouts/sensors for larger rare debris if useful

## Story Consequences
- forward shield erosion survey
- shield replacement mass
- deceleration reduces impact energy over time
- arrival 때 남은 forward shield material을 재활용할지 보존할지
- Outer Works와 별개 전문 위험직

### Status
`P0 OPEN — detailed shield sanity needed before World Logic Freeze`

이것은 이번 test에서 새로 발견된 중요한 맹점.

---

# 10. H9R / C-FULL-H1 Impact

## Repair Act 5 Pressure
OLD candidate:
`감속 때문에 생활전력을 직접 삭감`

NEW candidate:
`감속 유지 + colony preparation이 같은 산업부품/방열정비/Outer Works 인력/spares를 경쟁`

농업/생활전력 제한은:
- propulsion power를 빼앗겨서가 아니라
- civil radiator outage
- maintenance shutdown
- grid auxiliary constraints

등 구체적 상황에서만 발생.

## C8
water/reclamation 설비와 propulsion 자체는 분리.
C8가 propulsion 해결사로 승격되지 않음.

## Living World
Habitat C/Spine/Outer Works가 propulsion maintenance를 독점하는 `worker caste`처럼 보이지 않게:
- 전문 engineers
- procurement
- medicine
- family logistics
- service economy

가 함께 영향을 받게 함.

---

# 11. Red Team

## RT-PROP-01 — Fusion Drive Is Magic
### Risk
few-percent-c exhaust가 설명 없이 만능기술.

### Guardrail
능력을 제한:
- enormous propellant
- chamber wear
- thermal constraints
- fixed long acceleration profile
- cannot casually change destination
- no combat use

Severity: `P0 TECH`

## RT-PROP-02 — Why Not Use Drive Power For Civilization?
### Answer
10^17W-class propulsion energy는 electricity가 아니라 direct high-energy exhaust architecture.
생활 grid에 연결 가능한 발전소가 아님.

엔진을 발전기로 전환해 100PW 도시를 돌리는 설정 금지.

Severity: `PASS CANDIDATE`

## RT-PROP-03 — Why Not Accelerate Faster?
### Answer Candidate
- crew/habitat g는 문제가 아님
- thermal throughput
- engine lifetime
- propellant flow
- shield/dust risk

가 practical limit.

0.002g는 `못 더 세게 해서`라기보다 450년 mission optimization 결과 후보.

Severity: `P1`

## RT-PROP-04 — Ship Mass Too Uncertain
### Required
정확 구조질량은 World Bible Tech Freeze 전 별도 budget.
현재는 low-10^12 kg dry class만 사용.

Severity: `P1`

## RT-PROP-05 — Ram Shield Was Missing
### Verdict
새 P0로 등록.
World Logic Freeze는 계속 BLOCKED.

---

# 12. Verdict

## H9R Distance / Timeline
`PASS CANDIDATE`

13 ly / 0.03c / 14y accel / ~419y cruise / 14y decel ≈ 447y.

## Ship Scale
`PASS CANDIDATE` at low-10^12 kg dry-class order, exact mass NOT FROZEN.

## Propulsion
`REPAIR REQUIRED BUT SOLVABLE`

Recommended:
`H9R-P1 Dedicated Fusion Direct-Exhaust Drive`.

## Deceleration Story Pressure
기존 direct civil-power competition은 우선순위 하락/폐기 추천.
새 압력:
`thermal geometry + spare parts + manufacturing + labor + propellant + redundancy`.

## New Blocker
`Interstellar Ram Shield = P0 OPEN`.

아직 World Logic Freeze 금지.

---

# 13. Next Work

1. `Interstellar Ram Shield 3~4 designs + mass/story sanity`
2. H9R propulsion repair를 `change-log / CANON_STATUS`에 반영
3. C-FULL-H1 Act 5의 감속-pressure 표현 수정
4. 이후 Sub-Act / Information Ladder 진행
