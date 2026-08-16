# Current Work Status

## Project
《우주선에는 인간이 한 명뿐이다》

## Status
`DEEP DESIGN / NOT READY TO WRITE`

## Completed
- 기본 콘셉트/금지 방향
- Reader Promise 후보
- A/B/C/D 4안 비교
- Hybrid 작업 순서 선정
- B Story Engine 1차 테스트
- 40개 사건 생성 테스트 통과
- C-lite 세계 진실 4안 비교
- D Living World 1차 테스트
- 생활권 8개/사회철학 7개 후보
- World Logic P0 Harness
- WL01-02 신체/의료 4안 → H2
- WL03 출생 4안 → H3
- WL05-06 죽음/백업 4안 → H4
- WL07 인구 구조 → H6
- WL10 유일한 인간 4안 → H7
- WL11 역사 4안 → H8
- WL12 목적지 4안 → H9
- WL08-09 우주선/에너지/연산/생태 1차 기술모델
- 30만 인구 우주선 규모 Quant Stress Test
- World Logic Integrated Red Team v0.1
- P0 Closure Minimum Rules v0.1
- Red Team / Reference Matrix / Canon Registry / Change Log 구축

## Current Integrated Model — PROVISIONAL

### H2 Body / Mind
시민 대부분은 실제 인간형 생물학적 몸과 살아 있는 뇌를 가진다. 차이는 몸의 재질이 아니라 **의식의 발생 기원**.

### H3 Birth
부모의 실제 유전정보로 배아를 만들고, 표준 보조생식 과정에서 합성 인지 시드가 초기 신경발달을 점화. 실제 임신/출산/영아기/아동기/육아가 존재.

### H4 Death / Backup
현재 의식은 각자의 살아 있는 뇌에서 작동. 실시간 완전백업은 없음. 저빈도 Full Continuity Scan + 생활로그 + 조건부 사후복원.

### H6 Population
약 30만은 안전 수용범위의 현재값. 신규출생과 복원은 같은 주거/식량/의료/신체 자원을 두고 경쟁.

### H7 One Human
세습 혈통이 아니라, 합성인지 출생 전환 당시 만들어진 역사적 타협. 자연기원 인격이 없을 때 다음 정상 출생 중 하나에서 인지 시드를 생략하는 방식이 현재 1순위.

### H8 History
인간은 어느 날 전멸한 것이 아니다. 부모들이 의료/복원상의 이점 때문에 seeded birth를 선택하고, 그 아이들이 다시 부모가 되는 수 세대 동안 ‘태어나는 방식’이 바뀜. 합성기원 시민은 침입자/복제품이 아니라 현재 인류의 후손사회.

### H9 Destination
목적지는 실제 존재하고 거주 가능성이 있으나 낙원은 아님. 원래 식민계획과 달리 우주선은 이미 고향/문명이 됨. 빠른 행성식민과 우주선의 완전보존을 동시에 최대화할 수 없어 최종 자원·가치 충돌 발생.

## Tech / Scale Candidate
- 3개의 약 1 km 반경, 5~7 km 길이 회전생활원통 후보
- 비회전 중앙척추 + 외곽 산업/방열 구조
- 30만 농업 active crop canopy sanity range 약 15 km² 기준선, 작품에서는 20~30 km²+로 보수 설계
- 수 GW~10 GW대 지속전력 Order-of-Magnitude 후보
- 핵융합 주전원 미래기술 가정
- 중앙 서버가 30만 의식을 실시간 실행하지 않음
- 재생형 생명유지 + 비축 + 실제 손실
- 물/원료/구조질량을 방사선 차폐에도 활용

정확 수치는 아직 Canon 아님.

## P0 Minimum Rules — 1st Pass

### Cognitive Seed
- 완성 AI/기억/성격 주입 아님
- 배아/태아 신경망의 초기 자기조직화를 점화하는 발달 유도 패턴
- 영구칩/원격조종/숨은 명령 금지

### Assisted Reproduction
- 생식세포/배아 유전복구와 발달체크가 수백 년 동안 표준 인프라가 됨
- 현재 사회에서 보조생식은 특별 허가가 아니라 평범한 임신 시작 단계
- 우회가 물리적으로 절대 불가능하지는 않지만 매우 어렵고 위험

### Full Continuity Scan Limit
- 고해상도 스캔은 장시간 전용시설/추적물질/신경활성 측정 필요
- 반복시 신경계·혈관·교세포 부담과 회복기간
- 시설 throughput도 제한
- 돈만으로 매일 스캔하는 불멸 불가

### Natural-Origin Detection
- 현대 Full Scan은 자연/합성기원 모두 처리 가능
- 성인 뇌에서는 초기 시드의 직접 흔적이 사라지고 개인차와 겹침
- 기원을 확정하려면 의료검사가 아니라 출생 provenance가 필요

## Major Problems Strongly Mitigated
- 병원 검사 한 번으로 유일한 인간 식별
- AI 30만 명 중앙연산 비용
- AI 캐릭터의 감정적 거리감
- 가족/임신/육아의 가짜 느낌
- 백업 때문에 죽음 무효화
- 부자의 실시간 불멸
- 30만 인구 유지 이유
- 유일한 인간의 선택받은 혈통화
- ‘원래 인간 전멸’ 단일반전 의존
- 목적지 프로토콜=최종악역 문제

## Still Open Before World Logic Freeze
1. P0 Minimum Rules 2차 Red Team
2. 합성 인지 시드가 너무 만능기술처럼 보이지 않는지 검증
3. 생식 발달체크포인트가 과도한 디스토피아로 느껴지지 않는지 검증
4. 목적지 초기정착 자원 Trade-off 1단계 구체화
5. 우주선 구조/인구분포/구획 명칭의 Living World 재통합
6. ‘생물학적 인간 한 명’이라는 제목용 표현과 기술적 ‘자연기원 인격 1명’의 서사적 정합성

## Next Phase Candidate
World Logic Red Team v0.2 통과 후:

1. Character Bible
2. Chemistry / Relationship Matrix
3. 라이벌/주요 세력 인물화
4. 보고 싶은 장면 30~50개 보강
5. C-full Act / Sub-Act / Information Ladder

## Stop Condition
P0가 다시 열리면 World Logic Freeze 금지.

## Writing Gate
`DESIGN FREEZE → CANON FREEZE → WRITING READY` 전 원고 집필 금지.
