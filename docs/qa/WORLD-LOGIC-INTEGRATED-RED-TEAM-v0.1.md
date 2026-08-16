# World Logic Integrated Red Team v0.1

Status: `ACTIVE / NOT FREEZE READY`

검증 대상:

`H2 Body + H3 Birth + H4 Death/Backup + H6 Population + H7 One Human + H8 History + H9 Destination + Tech/Scale`

---

# Current Integrated Model

1. 시민 대부분은 실제 인간형 생물학적 몸과 살아 있는 뇌를 가진다.
2. 차이는 몸의 물질보다 의식의 발생 기원에 있다.
3. 일반 출생은 부모 유전정보의 실제 배아 + 합성 인지 시드 + 실제 임신/성장.
4. 현재 의식은 각자의 뇌에서 작동하며 중앙서버에 실시간 존재하지 않는다.
5. 백업은 저빈도 연속성 스캔으로 불완전하고 비용이 있다.
6. 출생과 복원은 약 30만 수용능력을 공유한다.
7. 자연기원 인간은 세습 왕족이 아니라 오래된 ‘기원 연속성 규약’에 따라 한 번에 둘 이상 만들지 않는 희귀 출생.
8. 이 사회는 한 번의 AI 반란으로 생긴 것이 아니라 수 세대의 의료/가족 선택으로 합성기원 출생이 표준화된 후손 문명.
9. 목적지는 실제로 존재하지만, 빠른 행성 식민과 우주선 문명의 완전보존을 동시에 하기 어렵다.

---

# P0 Attack 01 — Blood Test

## Attack
유일한 인간에게 혈액/유전자 검사만 하면 다른 시민과 다르지 않나?

## Current Defense
H2에서는 자연기원/합성기원 모두 인간형 생물학적 몸과 부모 유전정보를 가진다. 차이는 현재 DNA가 아니라 배아 초기 인지 발생 과정.

## Verdict
`PASS` under H2.

---

# P0 Attack 02 — Brain Scan

## Attack
MRI/뇌수술로 인지 시드 흔적을 찾을 수 있지 않나?

## Defense
시드는 영구 하드웨어가 아니라 초기 신경발달의 시작상태를 형성하는 과정이며 성장 뒤 독립 장치가 남지 않는다.

## Remaining Risk
‘초기 동역학만 인공적으로 점화한다’는 기술이 마법처럼 느껴질 수 있음.

## Verdict
`CONDITIONAL PASS`

Tech Bible에서 설명 한계를 정해야 함.

---

# P0 Attack 03 — Natural Pregnancy

## Attack
누군가 병원 밖에서 임신하면 자연기원 인간이 계속 생기지 않나?

## Defense
H3에서는 장기간 항해의 생식 안전장치 때문에 의료적 배아 활성화를 거치지 않은 임신은 정상발달이 불가능하거나 극히 초기 단계에서 종료.

## Risk
과도한 통제사회/인공적 안전장치.

## Verdict
`OPEN P0`

역사적 이유와 생물학적 메커니즘을 조금 더 자연스럽게 다듬어야 함.

---

# P0 Attack 04 — Doctors Know The Seed

## Attack
산부인과/생식의학자들은 합성 인지 시드의 기능을 왜 모르는가?

## Defense
현대 사회에서도 절차 자체는 공개된 ‘신경발달 안정화’ 기술. 숨겨진 것은 절차의 존재가 아니라 수백 년 전 그것이 ‘합성기원 인격’이라는 별도 범주를 만들었다는 역사적 의미.

## Verdict
`PASS DIRECTION`

거대 음모 필요 없음.

---

# P0 Attack 05 — Human Backup Failure Reveals Identity

## Attack
자연기원 인간은 seeded cognition보다 백업 호환성이 낮다면 연속성 스캔에서 바로 들키지 않나?

## Defense Candidate
자연기원도 스캔 가능. 차이는 통계적 보정/오차 경향이며 개인차 범위 안에 들어감.

현재 인간은 ‘희귀 신경매핑형’으로 처리될 수 있음.

## Risk
너무 편리한 오진.

## Verdict
`OPEN P1 / POSSIBLE P0`

정체 단서로 사용할지 완전히 차이를 없앨지 결정 필요.

---

# P0 Attack 06 — Exact One Counter

## Attack
현재 자연기원 인간이 몇 명인지 시스템은 어떻게 아는가?

## Defense
몸 검사 결과가 아니라 출생 프로토콜 provenance: 어떤 배아에서 인지 시드를 생략했는지 기록.

## Verdict
`PASS`

---

# P0 Attack 07 — Protocol Failure Creates Two Humans

## Attack
시스템 오류/해킹으로 시드를 두 번 생략하면?

## Answer
가능해야 한다.

‘절대 물리적으로 불가능’이라 하지 않는다.

그런 사건이 발생하면:
- 제목의 현재 상태가 깨질 수 있음
- 정치적/윤리적 대형 사건 발생

하지만 본편 시작 시점에는 한 명.

## Verdict
`PASS, WITH FAILURE MODE`

시스템이 완벽하지 않아야 세계가 살아 있음.

---

# P0 Attack 08 — Why One At All?

## Attack
과학적 목적이면 한 명은 의미 없는 표본인데 왜 유지?

## Defense
주목적을 과학이 아니라 역사적·정서적 정치 타협으로 둔다.

> 합성기원 출생으로 완전히 전환하되 자연발생 인지를 완전히 끊지는 않는다.

과학적 baseline은 부차적 이유.

## Verdict
`PASS`

불합리하지만 인간적인 제도라는 점이 오히려 Anti-AI 설계에 유리.

---

# P0 Attack 09 — Backup Makes Murder Cheap

## Attack
피해자를 복원하면 살인이 덜 심각하지 않나?

## Defense
- 현재 의식의 연속성은 강제로 종료됨
- 최신 Full Scan 이후 기억 손실
- 복원 대기/자원비용
- 복원 불가능 가능성
- 법은 강제 인격중단을 중범죄로 취급

## Verdict
`PASS`

---

# P0 Attack 10 — Rich Immortality

## Attack
부자는 매일 Full Scan하여 사실상 불멸 아닌가?

## Required Defense
가격만으로 막으면 부족.

필요한 물리적 제한:
- 스캔시설 throughput
- 신경계 반복측정 부담
- Full Scan 과정의 시간/회복 필요

## Verdict
`OPEN P0`

Tech rule required.

---

# P0 Attack 11 — 30만 서버 연산

## Attack
AI 30만 명이면 슈퍼컴퓨터 전력이 터지지 않나?

## Defense
현재 인격은 생물학적 뇌에서 로컬 실행. 중앙 연산은 사회 인프라/백업 처리용.

## Verdict
`PASS`

---

# P0 Attack 12 — Food Scale

## Attack
30만 생물학적 몸을 수백 년 먹일 수 있나?

## Defense
현재 NASA CEA 기준선의 1인당 약 40~50 m² crop canopy를 sanity baseline으로 사용하면 약 15 km². 작품에서는 20~30 km²+ 발효/배양식품/비축으로 설계.

3개의 km급 회전생활권 안에 물리적으로 배치 가능한 범위.

## Verdict
`PASS ORDER-OF-MAGNITUDE`

---

# P0 Attack 13 — Energy

## Attack
농업 조명만으로 엄청난 전력이 필요하지 않나?

## Defense
그렇다. 숨기지 않는다.

성간 세대우주선의 기술 전제로 다중 GW급 핵융합 발전을 허용하고, 전력보다 폐열/정비/시설처리량도 제약으로 둔다.

## Verdict
`SPECULATIVE BUT CONSISTENT`

핵융합은 작품의 SF 허용기술 목록에 명시해야 함.

---

# P0 Attack 14 — Radiation

## Attack
수백 년간 생물학적 몸이 GCR에 노출되면?

## Defense
- 생활권을 다층 질량/물/원료 안쪽에 배치
- 장기 유전검사/배아안정화
- 피난구역
- 미래기술 보조 차폐

## Verdict
`CONDITIONAL`

‘얇은 금속벽’ 묘사 금지.

---

# P0 Attack 15 — Why Not Make More Space?

## Attack
핵융합/거대선박 기술이면 그냥 새 생활권 만들어 출생 제한을 풀면 되지 않나?

## Defense
새 생활권은:
- 구조재
- 회전구조
- 차폐질량
- 농업
- 방열
- 수십 년 건설

이 필요한 대형 국가사업.

가능하지만 즉시 해결책은 아님.

## Verdict
`PASS`

오히려 정치 Story Engine.

---

# P1 Attack 16 — Everyone Is Biologically Human Anyway

## Attack
몸/뇌/DNA가 모두 인간이면 ‘생물학적 인간 한 명’이라는 전제가 낚시 아닌가?

## Risk
현재 가장 중요한 의미론 문제.

## Proposed Handling
초기 비밀문서의 실제 분류는:

`Natural-Origin Human Cognition: 1`

또는 이에 준하는 옛 기술용어.

주인공/사회가 이를 ‘진짜 인간 한 명’으로 해석하지만 후반에는 바로 그 분류법이 문제였음이 드러난다.

## Verdict
`OPEN P1 — THEMATICALLY PROMISING`

제목은 유지 가능하지만 작품소개/초기 Reveal의 문장 정밀설계 필요.

---

# P1 Attack 17 — Protecting Child Predictability

## Attack
보호대상에게 출생기록 이상이 있으면 독자가 바로 ‘저 아이가 인간’이라 맞힘.

## Mitigation
출생기록 이상 ≠ 자연기원 직접단서.

필요:
- 다른 인물의 비슷한 출생오류
- 복원/배아기록 문제
- 인간 후보 최소 3~5개
- 보호대상의 실제 이상점은 다른 개인적 문제와 겹치게 함

## Verdict
`OPEN NARRATIVE TASK`

---

# P1 Attack 18 — No Villain

## Attack
명확한 악당이 없으면 웹소설 추진력이 약하지 않나?

## Defense
명확한 **적대자/라이벌**은 존재 가능.

단 최종 세계 문제의 원인을 ‘악한 중앙 AI’ 한 명에게 몰지 않는다.

각 Act에서는:
- 이해관계가 분명한 개인
- 조직 지도자
- 법집행자
- 운동가

등이 실질적 적대 역할을 수행.

## Verdict
`PASS DIRECTION`

---

# P1 Attack 19 — Too Much Philosophy

## Attack
모든 사건이 ‘인간이란 무엇인가’ 질문이면 피곤함.

## Mitigation
사건의 표면목표를 구체적으로 유지:
- 집
- 친권
- 돈
- 기억
- 직장
- 학교
- 이주
- 결혼
- 복원

철학은 선택의 결과로만 드러냄.

## Verdict
`PASS IF ENFORCED`

---

# P1 Attack 20 — Mystery Removed

## Stress Test
40화에 ‘Natural-Origin Human = 1’ 사실을 완전히 공개한다고 가정.

남는 엔진:
- 누가 그 한 명인가
- 왜 한 명인가
- 현재 시민은 무엇인가
- 역사
- 가족 사건
- 복원/출생 정치
- 생활권 갈등
- 목적지

## Verdict
`PASS`

작품은 첫 대형 Reveal 후에도 살아 있음.

---

# P1 Attack 21 — Delete The One Human Entirely

## Stress Test
유일한 인간 설정을 중후반에서 서사적으로 잠시 제거하고 세계 사건만 본다.

H3/H4/H6/H8/H9는 모두 독립적으로 작동.

## Verdict
`PASS`

제목 미스터리가 Story Engine의 유일한 연료가 아님.

---

# P1 Attack 22 — Delete Destination Protocol

H9의 구식 프로토콜을 삭제해도:
- 정착주의 vs 항해주의
- 우주선 해체 문제
- 유전은행
- 현재 시민 vs 미래 출생 자원

갈등 유지.

## Verdict
`PASS`

프로토콜은 갈등 강화장치이지 최종보스가 아니어야 함.

---

# Current P0 Blockers

### P0-1
자연임신/배아 활성 안전장치의 역사·생물학적 설명.

### P0-2
Full Continuity Scan 반복을 제한하는 물리적 이유.

### P0-3
합성 인지 시드의 최소 내부규칙.

### P0-4
자연기원 인간의 스캔/의료 차이가 너무 직접적이지 않도록 조정.

### P0-5
목적지 초기정착의 실제 자원 Trade-off를 한 단계 더 구체화.

---

# Current Verdict

## World Logic
`PROMISING / NOT FREEZE READY`

큰 초기 구멍이었던:
- 의료검사
- 30만 연산
- 출생/가족 진정성
- 죽음 무력화
- 한 명의 혈통특권
- 인구 유지

는 모두 구조적 해결 방향을 확보했다.

남은 P0는 이제 ‘전제 붕괴’보다 기술세부의 과도한 편의성을 줄이는 문제에 가깝다.

다음 권장 작업:
1. P0-1~4 기술 규칙 최소화
2. Character Bible
3. 30~50개의 ‘보고 싶은 장면’ 확장
4. C-full Act / Information Architecture

단, World Logic P0를 먼저 닫은 뒤 Character Deep Design으로 넘어가는 것을 권장.
