# Living World A/B/C Event Regression v0.1

Status: `STORY-ENGINE QA / NOT CANON`

Purpose:
`C-FULL-H1 7 Act`를 적용했을 때 Habitat A/B/C가 각각:
- A = 법/엘리트
- B = 농업/자연
- C = 노동/공장

으로 굳는 hidden caste 문제를 실제 사건 생성력으로 검증한다.

Rule:
각 Habitat에서 최소:
- family
- youth
- service
- white-collar
- technical
- medical
- housing

사건을 생성한다.

메인 Human mystery 직접 연결은 소수만 허용.

---

# 1. Habitat A — 12 Events

A의 identity는 `가장 오래되고 도시적인 생활권`이지 엘리트 수도가 아니다.

## A01 — 복원된 임차인의 보증금
복원된 시민이 사고 전 살던 민간/협동주거 unit의 보증금·점유권 일부를 요구하지만 현재 세입자가 존재.

Engine: Housing + Continuity
Act fit: 1~2
Class check: ordinary household

## A02 — 학교 교사의 B 전근
A 학교 교사가 B의 더 나은 직책을 받아 이직하려 하지만 자녀는 A에 남고 싶어 함.

Engine: Family + Work + Mobility
Act fit: 1~4
Class check: education worker

## A03 — 병원 전문의가 C로 떠난다
A의 reconstruction 전문의가 C의 산업재활센터로 이직하면서 A 환자 대기시간이 늘어남.

Engine: Medical + Labor Market
Act fit: 2~4
Class check: professional mobility, not A monopoly

## A04 — Old Quarter 식당의 이전
수십 년 된 가족식당이 안전폐쇄 때문에 이전 보상을 받지만 새 상권에서는 단골을 잃음.

Engine: Service + Place + O
Act fit: 1~3
Class check: small business

## A05 — 청소년 무중력 스포츠팀
A 학생들이 Spine 훈련시설을 쓰는데 교통봉쇄로 시즌 참가가 흔들림.

Engine: Youth + Mobility
Act fit: 1~2
Class check: youth life unrelated to mystery

## A06 — 아카이브 계약직의 잘못된 분류
역사기록 디지털화 계약직이 오래된 metadata를 현대 분류로 자동변환했다가 법적 분쟁 발생.

Engine: Work + Archive
Act fit: 2
Mystery relation: indirect only
Class check: ordinary clerical/technical work

## A07 — 민간 소프트웨어사의 Capacity 예측 서비스
공공 Capacity Forecast를 기반으로 통근/주거 추천 서비스를 파는 회사가 특정 구역을 낮게 평가해 집값/이주에 영향.

Engine: Market + Housing + Data
Act fit: 3~4
Class check: private white-collar, but not government

## A08 — 건물 배관노동자의 파업
A 중심가 고층주거의 노후 배관 교체노동자들이 위험수당을 요구.

Engine: Technical + Labor
Act fit: 2~4
Class check: A has manual/technical workers

## A09 — 출생승인 뒤 더 큰 집이 없다
아이를 기다리던 부부가 capacity 승인을 받았지만 적절한 family unit 대기기간이 길어 출산시기와 주거가 충돌.

Engine: Birth + Housing + Family
Act fit: 3~5

## A10 — 지역병원 야간응급 폐쇄 논쟁
예산/인력 부족으로 A 외곽 일반병원의 야간응급을 통합하려 하자 주민 반발.

Engine: Medical + Local Politics
Act fit: 4~5
Class check: A에도 서비스 격차 존재

## A11 — 복원 반대 노년층의 평범한 모임
정치운동보다 취미모임에 가까운 노년층에서 do-not-restore 등록을 함께 준비하면서 가족들이 뒤늦게 반발.

Engine: Family + Finality
Act fit: 1~4

## A12 — Arrival 준비로 공연장 전력시간 축소
감속/산업전력 peak 때문에 대형 공연장 운영시간이 줄어 문화업계/주민이 반발.

Engine: Culture + H9R Cost
Act fit: 5
Class check: H9R가 일상문화에도 비용

### A Distribution
- family: 4+
- youth: 1+
- service/culture: 3+
- white-collar: 3+
- technical/manual: 2+
- medical: 3+
- housing: 4+

A ≠ `법/행정만 하는 수도`.

---

# 2. Habitat B — 12 Events

B의 identity는 `물/식물/생태인프라가 생활풍경에 보이는 대도시권`이지 농촌이 아니다.

## B01 — C8 수처리 교대사고
C8이 관련된 현장사고/책임문제.
C8은 여러 숙련 실무자 중 한 명.

Engine: Technical + C8
Act fit: 2
Mystery relation: NONE

## B02 — 바이오 스타트업의 물사용 계약
의료용 생물소재 회사가 생산확장을 위해 water allocation을 더 요구하고 지역 식품업체/주거망과 충돌.

Engine: Business + Resource
Act fit: 2~5
Class check: B white-collar/private industry

## B03 — 운하 상업지구의 임대료 상승
B의 인기 수변 상권이 고급화되며 오래된 세탁소/식당이 밀려남.

Engine: Market + Service + Housing
Act fit: 1~4
Class check: urban commercial life

## B04 — B 법률사무소의 복원 분쟁
R과 무관한 지역 변호사가 농업협동조합 구성원의 복원 뒤 지분권 문제를 맡음.

Engine: Law + Business + Continuity
Act fit: 2~4
Class check: B에도 legal profession

## B05 — 초등학교의 생태실습이 취소된다
수질오염 경보로 학교 야외/수변 수업이 중단되고 아이들은 단순히 불평하지만 부모들은 더 큰 문제를 감지.

Engine: Youth + Ecology
Act fit: 2~5
Class check: ordinary school life

## B06 — Reconstruction 병원의 재활 대기
B 병원은 생체재활에 강하지만 특정 전문의가 부족해 복원자는 C로 장거리 통원해야 함.

Engine: Medical + Mobility
Act fit: 2~4
Class check: specialists distributed

## B07 — 원격근무 개발자의 A 출근명령
B에서 사는 소프트웨어 개발자가 회사 정책변경으로 주 3회 A 본사 출근을 요구받아 가족이 이주를 고민.

Engine: White-collar + Commute + Family
Act fit: 1~4

## B08 — 도시형 농업구획 위의 주거 증축
농업데크 상부 유휴구조를 주거로 전환하려는 개발안이 식량안전 여유율과 충돌.

Engine: Housing + Planning + Ecology
Act fit: 3~5

## B09 — 결혼식장 예약이 정전계획과 겹친다
감속 전력조정으로 수변 상업지구 순환정전이 예정되어 가족행사가 흔들림.

Engine: Family + Service + H9R
Act fit: 5
Class check: macro cost becomes ordinary inconvenience

## B10 — 예술가 작업실의 곰팡이/습도 문제
생태계 습도관리 변경으로 저렴한 작업실 구역에 곰팡이 피해가 늘고 관리주체와 임차인이 충돌.

Engine: Culture + Housing + Utility
Act fit: 3~5

## B11 — 펌프 부품 제작업체의 C 이전
B의 중형 제조업체가 C/Spine 물류접근 때문에 이전하면서 숙련직 가족들이 통근/이사를 선택해야 함.

Engine: Manufacturing + Labor + Mobility
Act fit: 4~6
Class check: B에도 manufacturing exists

## B12 — C8 배우자의 이주신청
C8 가족이 A/B 통근과 첫째 apprenticeship 때문에 거주지를 실제로 재검토.
Natural-Origin과 무관하게 진행.

Engine: Family + Housing + C8
Act fit: 2~4, Reveal 이후에도 지속

### B Distribution
- family: 4+
- youth: 1+
- service/culture: 3+
- white-collar/legal: 3+
- technical/manufacturing: 4+
- medical: 1+
- housing: 4+

B ≠ `농업/자연 사람들만 사는 곳`.

---

# 3. Habitat C — 12 Events

C의 identity는 `Spine/산업 접근과 교대근무가 생활리듬에 더 큰 영향을 주는 혼합도시`이지 노동자 빈민구역이 아니다.

## C01 — 교대근무 부모의 학교시간
Outer Works 교대근무 부모와 일반 학교시간이 맞지 않아 가족 돌봄/통근이 꼬임.

Engine: Family + Work
Act fit: 1~5

## C02 — 24시간 카페의 폐업
C의 야간문화 상징인 작은 카페가 hub 임대료 상승으로 폐업 위기.

Engine: Service + Market + Place
Act fit: 1~4

## C03 — 재활병원의 고급 전문직 채용
C 산업재활센터가 A 전문의를 높은 조건으로 영입하면서 `C는 저숙련 노동자 구역` 이미지를 깨고 지역의료가 성장.

Engine: Medical + Labor Market
Act fit: 2~4

## C04 — 로봇설계 회사의 안전책임
민간 로봇회사 설계오류가 Outer Works 사고와 연결되지만 현장 노동자만 책임받는다는 논쟁.

Engine: White-collar + Technical + Liability
Act fit: 2~5

## C05 — 조용한 외곽주거 노년층
C에서 평생 일하고 은퇴한 노년층이 24시간 교대도시 이미지와 달리 조용한 주거지 폐쇄/통합에 반발.

Engine: Housing + Elderly + Place
Act fit: 2~5

## C06 — 청년 apprenticeship 경쟁
부모가 A/B에서 일하는 청년들이 C/Spine 기술 apprenticeship를 두고 경쟁.
C 출신자만의 길이 아님.

Engine: Youth + Education + Mobility
Act fit: 2~4

## C07 — 공공변호사의 산업사고 소송
C의 법률지원센터가 worker뿐 아니라 사고를 낸 중소기업 경영자의 continuity/책임 문제까지 다룸.

Engine: Law + Continuity
Act fit: 2~4
Class check: legal/civic services present

## C08 — 공연창고/예술공간
폐공장 일부가 공연·전시 공간으로 쓰이는데 H9R 제조확장 때문에 다시 산업용으로 회수하려 함.

Engine: Culture + H9R + Place
Act fit: 5~6

## C09 — Transit Hub 고급주거
Spine 접근성이 좋은 C 중심부 주거가 A 중심가보다 비싸지며 `C=빈민구역` 고정관념과 충돌.

Engine: Housing + Market
Act fit: 2~5

## C10 — 일반 의원의 야간진료 과부하
교대근무 인구 때문에 야간 일반진료가 과부하. 거대한 reconstruction이 아니라 감기/부상/육아 같은 의료문제.

Engine: Medical + Daily Life
Act fit: 1~5

## C11 — 게임/방송 스튜디오의 야간노동
C의 미디어/게임회사도 교대문화에 맞춰 야간제작을 하며 청년 노동문제가 발생.

Engine: Creative Industry + Labor
Act fit: 3~5

## C12 — Colony Module 생산라인 노동자 아닌 회계팀
H9R bootstrap module 제조기업의 회계/조달팀이 원료전용 정책 때문에 계약을 재작성하고 대규모 해고 여부를 결정해야 함.

Engine: White-collar + H9R + Business
Act fit: 5~6
Class check: H9R industrial story not only manual labor

### C Distribution
- family: 2+
- youth: 1+
- service/culture: 4+
- white-collar/legal: 4+
- technical/manual: 3+
- medical: 2+
- housing: 3+

C ≠ `공장 노동자만 사는 곳`.

---

# 4. Cross-Habitat — 6 Events

## X01 — A+B 부부의 통근 파탄
A 공공서비스 / B 바이오산업 부부가 transit timetable 변경으로 같은 집을 유지하기 어려워짐.

## X02 — B+C 형제의 복원결정
한 형제는 B one-life 문화에 가까우며 다른 형제는 C 위험직이라 restoration access를 당연하게 봄.
같은 가족 내부에서 문화차이가 생김.

## X03 — C 출신 의사의 A 병원 파견
지역정체보다 전문직 네트워크가 더 강한 사례.

## X04 — A 학생의 C apprenticeship
부유한 A 가족이 자녀의 C 기술훈련 선택을 이해하지 못함.
계급상승/하락 프레임으로 단순화 금지.

## X05 — B 상인의 A Old Quarter 2호점
Habitat 문화가 사람/사업 이동으로 섞임.

## X06 — H9R 가족투표
한 가족의 성인 구성원이 각각 ship 잔류 / surface / orbital path를 다르게 선택.
Habitat 소속과 정착정치가 1:1이 아님을 보임.

---

# 5. C-FULL-H1 Act Distribution Check

## Act 1 (1~28)
A 비중이 높지만:
- B: B03/B05/B07 중 1~2
- C: C01/C02/C10 중 1~2
필수.

## Act 2 (29~58)
B/C 확대:
- C8 B01/B12
- C C04/C06/C07
- A Old Quarter/병원/주거

## Act 3 (59~88)
Origin Reveal가 A 기록실/법정만으로 진행되지 않게:
- C8 family/직장 B
- school/workplace reaction C/B
- A archive/legal evidence
분산.

## Act 4 (89~122)
각 Habitat 최소 3개의 생활후폭풍.

## Act 5 (123~156)
H9R:
- A: culture/hospital/housing power costs
- B: water/biotech/family
- C: module production/culture/housing

## Act 6 (157~194)
정착정치는 Habitat별 블록이 아니라 X06 같은 가족/직업 cross-cutting 구조.

## Act 7 (195~230)
새 habitat/surface/ship 선택에서도 출신 Habitat가 자동결정하지 않음.

---

# 6. Mystery Contamination Check

42 events 중 Human mystery 직접 연결 가능성이 높은 것:
- A06 archive metadata
- 일부 C8 사건이 Reveal 후 연결

나머지 대부분은 독립 작동.

`PASS`

이것이 중요하다.
Living World는 메인 비밀을 설명하기 위한 무대가 아니라 자체 사건생성기다.

---

# 7. Hidden Caste Red Team

## RT-ABC-01 — A Still Owns Law / Power
A에는 중앙기관이 많지만:
- B04 local law
- C07 legal aid
- Habitat Councils
- distributed hospitals/schools
를 유지.

Verdict: `PASS CANDIDATE`

## RT-ABC-02 — B Still Feels Like Eco District
B03/B04/B07/B10/B11/B12로 상업/법률/소프트웨어/예술/제조/통근가족 확보.

Verdict: `PASS CANDIDATE`

## RT-ABC-03 — C Still Feels Like Worker District
C02/C03/C07/C08/C09/C11/C12로 서비스/전문의료/법률/문화/고급주거/미디어/회계 확보.

Verdict: `PASS CANDIDATE`

## RT-ABC-04 — Specialization Disappears Completely
모든 Habitat가 너무 똑같아지면 장소재미가 사라짐.

Guardrail:
- A: old urban / institutions / historic density
- B: visible water/ecology / bio-infrastructure
- C: shift rhythm / transit / industrial proximity

차이는 `풍경 + 하루 리듬 + 산업 비중`에 두고 사람종류에 두지 않는다.

Severity: `P1`

## RT-ABC-05 — P Conveniently Visits Every Event
P가 모든 사건에 참여하면 세계가 다시 주인공 중심으로 축소.

Guardrail:
42개 중 상당수는:
- S
- R
- O
- C8
- D
- N
또는 뉴스가 아닌 `독립 생활 후속효과`
로 진행.

P가 직접 관여하지 않는 Living World event 목표:
`최소 30~40%`.

Severity: `P0 CHARACTER AUTONOMY`

---

# 8. Verdict

총 42개 사건:
- A 12
- B 12
- C 12
- Cross-Habitat 6

각 Habitat에서 family/youth/service/white-collar/technical/medical/housing 사건 생성 가능.

결론:
`A/B/C HIDDEN CASTE RISK = CONDITIONAL PASS`

C-FULL-H1과 결합 가능.

하지만 Freeze 전 필요:
1. 실제 Sub-Act에 이 사건군을 분배
2. P 비관여 사건 30~40% 확인
3. 주요 인물의 거주/직업 지도를 만든 뒤 이동편향 검증
4. Transit geometry/time sanity

아직 Living World Freeze 금지.
