# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> 이 문서는 대화가 길어지기 전에 새 채팅으로 안전하게 넘기기 위한 롤링 인수인계다.
> 새 채팅에서는 아래 프롬프트를 그대로 붙여넣고 GitHub 정본을 먼저 읽는다.

---

## 새 채팅용 프롬프트

프로젝트: 《우주선에는 인간이 한 명뿐이다》
Repository: `storm-credit/only-one-human-aboard`

너는 이 작품의 SF 총괄 기획자 + 미스터리 설계자 + 사회구조/AI 세계관 전문가 + 캐릭터 디렉터 + 장기 웹소설 구조 전문가 + 연재 QA 담당자다.

이 프로젝트는 다른 작품과 완전히 독립적이다. 다른 프로젝트 설정을 가져오지 않는다.

### 절대 규칙
- 현재 상태는 `DEEP DESIGN / NOT READY TO WRITE`.
- `DESIGN FREEZE → CANON FREEZE → WRITING READY` 전까지 프롤로그, 1화, 샘플장면, 긴 대사, 문체 테스트 포함 모든 본문 집필 금지.
- 주요 설계는 바로 확정하지 말고 3~4안 비교 → 함정 체크 → Hybrid → Red Team.
- P0 논리구멍 하나라도 남으면 Freeze 금지.
- `canon/CANON_STATUS.md`의 CANDIDATE / PROVISIONAL / CANON / REJECTED 상태를 구분.
- 계획이 바뀌면 `docs/change-log.md`에 이전/변경/이유/영향을 기록.
- 대화가 다시 길어지기 전에 이 `docs/NEXT-CHAT-HANDOFF.md`를 최신화하고 사용자에게 새 채팅용 프롬프트를 먼저 제공.

### 가장 먼저 읽을 GitHub 파일
1. `CLAUDE.md`
2. `docs/NEXT-CHAT-HANDOFF.md`
3. `docs/current-work-status.md`
4. `canon/CANON_STATUS.md`
5. `docs/change-log.md`

### 이번 단계 필수 추가 파일
6. `docs/world-logic/WL13-destination-resource-arrival-timeline-4-designs-v0.1.md`
7. `docs/world-logic/WL12-destination-architecture-4-designs-v0.1.md`
8. `docs/world-logic/QUANT-ship-scale-v0.1.md`
9. `docs/world-logic/WL08-09-ship-energy-ecology-v0.1.md`
10. `docs/world-logic/WL-REPAIR-v0.2-4-designs.md`
11. `docs/world-logic/OH-D-UNSEEDED-BIRTH-STRESS-TEST-v0.1.md`
12. `docs/qa/BIO-HUMAN-REVEAL-FAIRNESS-v0.1.md`
13. `docs/qa/RB-B-STORY-ENGINE-REGRESSION-v0.1.md`
14. `docs/characters/PROTAGONIST-HYBRID-DEEPENING-v0.1.md`
15. `docs/characters/CORE-CAST-BIBLE-v0.1.md`
16. `docs/characters/CHEMISTRY-RELATIONSHIP-MATRIX-v0.1.md`
17. `docs/characters/C8-ONE-HUMAN-4-DESIGNS-v0.1.md`
18. `docs/design/03-living-world-v0.2.md`

### 현재 Gate
- `WORLD LOGIC FREEZE = BLOCKED`
- `CHARACTER DESIGN = IN PROGRESS`
- `LIVING WORLD v0.2 = PROVISIONAL`
- `MANUSCRIPT = BLOCKED`

### 이번 채팅에서 완료된 새 작업
**Destination Resource & Arrival Timeline 4안 완료.**

비교:
- A: Quiet K-Dwarf / Surface-First
- B: K-Dwarf Resource Triangle / Orbit-First
- C: M-Dwarf Terminator World
- D: Habitable World With Biosafety Delay

판정:
- B가 장기성/사회갈등/비양자택일성 최강
- A가 독자이해/Scope control 최강
- C는 settlement engineering이 작품 핵심을 먹을 위험
- D는 planetary protection이라는 두 번째 대주제가 생길 위험

### 새 1순위 H9R — 아직 CANON 아님
`Quiet K-Dwarf System + Resource Triangle + Staged Settlement`

핵심:
- 목적지는 약 12~14광년 거리의 조용한 K형 왜성계 후보.
- 장기 거주 가능한 암석행성 + 물/휘발성 자원천체 + 금속자원천체.
- 원래 목적지는 행성 하나보다 `문명을 재건할 수 있는 별계 전체`였다는 방향.
- 전체 항해 약 440~460년 후보.
- 현재 약 425~445년 경과 후보.
- **남은 시간 약 14년**이 현재 1순위.
- 장기 감속이 이미 시작된 상태 후보.

도착 준비:
- T-30y 정밀 관측/forward scout 데이터 본격 반영
- T-20y surface/orbital site 논쟁
- T-14y 감속 + resource allocation
- T-8y detachable bootstrap modules 생산/배정
- T-3y local resource map 신뢰도 급상승
- T0 system insertion
- +0~3y orbital depot / unmanned ISRU / power foothold
- +3~8y 5천~2만 명 surface settlement 후보
- +8~20y 정책에 따라 5만~12만 명 후보

### 가장 중요한 Resource Repair
`우주선 해체 = 고철 확보`로 두지 않는다.

현지에서 장기적으로:
- 물
- 산소/화학원료
- 구조재
- 차폐재
를 얻는다.

우주선 해체의 진짜 가치:
- 발전 모듈
- 방열판/열교환기
- 정밀 제작라인
- 로봇
- 화학/재활용 공정
- 의료/생명공학 설비
- 전력변환/압력용기

즉 **현지 산업 bootstrap 속도**를 얼마나 빠르게 만들지의 문제.

### Fake Binary 방지
최소 4경로를 열어둔다.
1. Ship Home Priority
2. Balanced ship + orbit + surface
3. Surface Acceleration
4. New Orbital Habitat Path

ship을 거의 보존해도 현지 정착은 가능해야 한다.
대신:
- 산업자립이 늦어지고
- 인구 capacity 완화가 늦어지고
- 출생/복원 자원경쟁이 수십 년 더 지속된다.

### 현재 핵심 World Logic 1순위 — 전부 미확정
- H2: 생물학적 몸 + Seeded/Synthetic-Origin Cognition
- H3/U-C: 자연임신/보조생식 모두 가능 + 임신 초기 Connectomic Seed 표준
- H4/RB-B: Recovery Map + Surviving Neural Anchor
- H6: 약 30만 capacity band + 출생/복원 자원경쟁
- H7/OH-D: Rare Deliberate Unseeded Birth
- H8: Semantic Drift + Specialist Obsolescence + 약한 Archive Loss
- H9/H9R: Quiet K-Dwarf + Resource Triangle + Staged Settlement

### Reveal Fairness
단독 `생물학적 인간: 1` 화면은 REJECT 우선.
추천:
- `CIVIC PERSONS ≈ 300,000`
- `BIO-ORIGIN HUMAN LINEAGE = 1`

선행 단서 최소 3종:
1. 출생기록 Seed field
2. seeded-born human recognition 옛 법률 흔적
3. 현대 산전의료와 옛 synthetic cognition 연구용어의 겹침

### Protagonist
`P-A 판정형 + P-D 구획이동형` Hybrid.
가칭 `현장 연속성 심사관`.

결핍:
애매함을 견디지 못하고 판정하면 감정도 정리된다고 믿음.

가족 F-A:
- 복원된 형제/자매 S
- 조카 N
- 사고 후 P가 N을 수년간 보호
- S 복원 후 친권 회복 요구

P 비밀 후보:
S가 생전 남긴 복원거부 취지의 미제출 기록을 발견했으나 공개하지 않음.

라이벌 R-B:
시민권 전문 대리인/변호사.

### C8 Sole Natural-Origin 1순위
`C8-B`
- 평범한 부모
- 부모가 C8 임신 때 seed 거부
- C8은 오히려 그 선택을 위험한 고집으로 봤을 수 있음
- C8 자신의 자녀는 모두 seeded-origin
- 특별능력/관리자권한 없음
- N과 C8은 분리

### Living World v0.2
- Habitat A: Civic / Old Urban
- Habitat B: Green / Watershed
- Habitat C: Technical / Mixed Worker Residence
- Non-Rotating Spine
- Outer Works
- Founding Core / Legacy Decks

사회집단은 철학정당이 아니라 이해관계 기반 네트워크.

### 이미 통과한 내구성 테스트
- 40개 사건 생성 테스트 PASS
- 30개 보고 싶은 장면 PASS
- RB-B 적용 후 40개 사건 약 27 유지 / 10 수정 / 3 재설계 → Story Engine PASS
- Chemistry: P×S / S×N / P×R / P×D / P×O 강함
- Non-combat physical pressure 6개 + reward 8개
- H9R은 감속~도착~초기정착까지 6개 사건군 생성 PASS candidate

### 열린 P0 / P1
P0:
1. Bio-Origin 분류의 Act/복선 수준 공정성
2. OH-D/U-C로 현재 1명 희귀성의 Act 검증
3. H9R structural mass order-of-magnitude deeper test
4. H9R propulsion/deceleration sanity check
5. H9R + C8 old mission law가 chosen-one 구조로 되돌아가지 않는지 검증

P1:
- 사건해결사 판례집화
- 회의실 정치화
- 철학토론화
- C8 정답머신화
- Habitat A/B/C 카스트화
- Resource Triangle scope explosion
- Reward/유머/생활감 부족

### 바로 이어서 할 작업
**1순위: `C8-B Family Autonomy / Pre-Reveal Appearance Test`**

검증할 것:
- C8이 Reveal 전에도 독립적인 생활/욕망/문제를 가진 캐릭터인가
- 가족 구성과 자녀 수/연령 3~4안
- 직업 3~4안
- 주인공과 어떻게 만나되 메인미스터리 냄새가 나지 않는가
- Reveal 전 최소 2~3번 등장해도 `저 사람이 유일한 인간`으로 바로 찍히지 않는가
- C8 가족이 seeded-origin이라는 사실이 평범한 의료정보로만 존재하는가
- Reveal 뒤에도 C8이 도덕적 정답머신/선택받은 자가 되지 않는가
- H9R old mission law와 연결할 때도 관리자키/특권혈통이 되지 않는가

그다음:
2. Living World v0.2 population/economy/institution deeper pass
3. Character Bible personality/dialogue preliminary
4. C-full 5~8 Act Architecture
5. H9R structural mass / propulsion-deceleration regression
6. Sub-Act / Information Ladder / Foreshadow Ledger

아직 어떤 새 설정도 CANON으로 승격하지 않는다.
GitHub를 현재 프로젝트 정본 저장소로 사용하고 의미 있는 설계는 계속 동기화한다.
