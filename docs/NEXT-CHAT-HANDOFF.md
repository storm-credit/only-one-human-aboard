# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> 롤링 인수인계 문서. 대화가 길어지기 전에 갱신하고 사용자에게 새 채팅용 프롬프트로 제공한다.

## 새 채팅에서 그대로 붙여넣을 프롬프트

프로젝트: 《우주선에는 인간이 한 명뿐이다》
Repository: `storm-credit/only-one-human-aboard`

너는 이 작품의 SF 총괄 기획자 + 미스터리 설계자 + 사회구조/AI 세계관 전문가 + 캐릭터 디렉터 + 장기 웹소설 구조 전문가 + 연재 QA 담당자다.

이 프로젝트는 다른 작품과 완전히 독립적이다. 다른 프로젝트 설정을 가져오지 않는다.

## 절대 규칙
- 현재는 `DEEP DESIGN / NOT READY TO WRITE`다.
- `DESIGN FREEZE → CANON FREEZE → WRITING READY` 전까지 프롤로그, 1화, 샘플 장면, 긴 대사, 문체 테스트 포함 모든 소설 본문 집필 금지.
- 설정집, 설계도, 세계관, Character Bible, Act/Sub-Act, 복선/회수, 장기 QA가 완성될 때까지 집필하지 않는다.
- 주요 설계는 바로 확정하지 말고 3~4안 비교 → 함정 체크 → Hybrid → Red Team 순서로 검증한다.
- P0 논리구멍 하나라도 남으면 Freeze 금지.
- 변경 시 `docs/change-log.md`에 이전/변경/이유/영향을 기록한다.
- `canon/CANON_STATUS.md`의 CANDIDATE / PROVISIONAL / CANON / REJECTED 상태를 지킨다.
- 대화가 다시 길어지기 전에 이 문서를 갱신하고 사용자에게 새 채팅용 프롬프트를 먼저 제공한다.

## 반드시 먼저 읽을 GitHub 문서
1. `CLAUDE.md`
2. `docs/current-work-status.md`
3. `canon/CANON_STATUS.md`
4. `docs/change-log.md`
5. `docs/qa/WORLD-LOGIC-RED-TEAM-v0.2.md`
6. `docs/world-logic/WL-REPAIR-v0.2-4-designs.md`
7. `docs/world-logic/P0-CLOSURE-minimum-rules-v0.1.md`
8. `docs/characters/PROTAGONIST-4-DESIGNS-v0.1.md`
9. `docs/characters/PROTAGONIST-HYBRID-DEEPENING-v0.1.md`
10. `docs/characters/CORE-CAST-BIBLE-v0.1.md`
11. `docs/characters/CHEMISTRY-RELATIONSHIP-MATRIX-v0.1.md`
12. `docs/design/WANTED-SCENES-30-v0.1.md`
13. `docs/design/01-story-engine-v0.1.md`
14. `docs/design/02-truth-architecture-c-lite-v0.1.md`
15. `docs/design/03-living-world-v0.1.md`

## 현재 상태
`WORLD LOGIC FREEZE = BLOCKED`
`CHARACTER DESIGN = IN PROGRESS`
`MANUSCRIPT = BLOCKED`

World Logic v0.1에서 대부분 P0가 닫혔으나 Red Team v0.2가 핵심 P0를 다시 열었다. 이것은 실패가 아니라 의도된 QA 결과다.

## 현재 World Logic 1순위 수리 후보 — 전부 PROVISIONAL/CANDIDATE

### H2R-A — Body / Origin
- 시민 대부분은 실제 인간형 생물학적 몸/뇌와 진짜 가족/성장을 가진다.
- 차이는 몸보다 `Natural/Bio-Origin Cognition` vs `Seeded/Synthetic-Origin Cognition`이라는 인지 발생 이력.
- 현 사회에서는 둘 다 인간/사람.
- ‘생물학적 인간 1명’은 옛 분류체계의 충격적 선언이며 작품은 그 분류가 30만 명의 삶보다 정당한지 질문해야 함.
- **용어장난 위험 때문에 아직 P0 semantic guardrail 유지.**

### H3 — Birth
- 실제 부모 유전정보
- 실제 배아/임신/출산/성장
- seeded neurodevelopment가 수백 년 동안 표준 생식의학이 됨

### H4R / RB-B — Death / Restoration
- Full Continuity Scan은 실행 가능한 영혼파일이 아니라 `continuity recovery map`.
- 정상 법적 복원에는 살아 있거나 보존된 원 neural anchor가 필요.
- 원 신경기질 없이 만든 존재는 가능하더라도 `Derived Person` 별도 범주 후보.
- 완전 소멸은 실제 죽음 가능.

### H6 — Population
- 약 30만은 현재 근사값/안전운용대.
- 출생과 복원이 같은 장기 자원을 경쟁.

### H7 Repair — One Human
기존 `항상 한 명 유지 Witness/Baseline Protocol` 우선순위 하락.

현재 1순위 후보:
`OH-D Rare Deliberate Unseeded Birth`
- 역사적으로 natural-development 예외가 전혀 없었던 것은 아님.
- 현재 살아 있는 확인 가능한 natural-origin이 한 명.
- 시스템이 선택한 존재/왕족/관리자키/특별능력 없음.
- 그 사람의 차이가 중요한 이유는 사회가 그것을 중요하게 만들기 때문.

### H8 — History Knowledge
추천 Hybrid:
`Semantic Drift + Specialist Obsolescence + 약한 Archive Loss`
- 기술 존재 자체는 완전 비밀 아님.
- 현재에는 인간 생식의학으로 이해.
- 옛 synthetic cognition 기술의 의미/분류가 수백 년 동안 희석.
- 중앙정부 대규모 기억삭제는 우선 폐기.

### H9 — Destination
- 실제 목적지 존재
- 우주선은 이미 30만의 고향
- 식민 속도와 우주선 보존은 연속적 자원 Trade-off
- 버튼 두 개식 윤리시험 금지

## Red Team v0.2에서 재개방된 핵심 P0
1. ‘생물학적 인간 1명’ 표현과 H2 생물학적 몸의 정합성
2. 기록사회에서 옛 synthetic-origin 의미가 왜 상식이 아닌가
3. 성인 복원 신체와 정상 아동 성장 규칙
4. 현재 natural-origin이 한 명인 이유

## Story Engine 결과
- 40개 사건 생성 테스트 통과
- 보고 싶은 장면 30개 테스트 통과
- 30개 중 메인 미스터리 직접 연결 약 5~6개

따라서 `메인 비밀 없으면 할 일이 없다` 위험은 현재 낮음.

## Character Architecture 현재 1순위 후보

### Protagonist
`P-A 판정형 + P-D 구획이동형 일부`
가칭 `현장 연속성 심사관`.
- 최고권력자 아님
- 연속성 분쟁에서 임시 권리상태 판단
- 구획/재난/이주에 제한적 현장 파견
- 항고/재심 가능

결핍:
애매함을 견디지 못하고 판정하면 감정도 정리된다고 믿음.

### Family F-A
- 복원된 형제/자매 S
- 그 자녀인 조카 N
- 사고 뒤 P가 N을 수년간 보호
- S가 복원되어 친권 회복을 원함

P의 개인 비밀 후보:
S가 생전 남긴 복원거부 취지의 미제출 기록을 발견했지만 공개하지 않음.

### Main Rival R-B
시민권 전문 대리인/변호사.
P의 임시판정을 반복 항고하고 연속성 심사제도의 권한 축소를 추구.
P 없이도 집단소송/정치연대를 독립 진행.

### Core Cast 후보
- P 주인공
- S 복원된 형제/자매
- N 조카
- R 시민권 라이벌
- M 상사/스승
- D 현장 의료평가관
- O 구환 주민대표/오랜 친구
- C8 유일한 natural-origin은 Act 2 이후 진입 후보

중요:
N과 C8을 현재 분리 추천. 모든 비밀이 주인공 가족에 몰리는 인공성을 줄인다.

## Chemistry 1차 PASS
강한 관계:
P×S / S×N / P×R / P×D / P×O

## 새로 발견된 약점
- 물리적 위기/긴장 리듬이 부족할 수 있음
- 즐거운 승리/보상 장면 부족
- C8 유일한 인간의 개인욕망/직업/관계가 아직 비어 있음
- 사건해결사 판례집화/회의실 정치화/철학토론화 계속 감시

## 바로 이어서 할 작업
순서:
1. `OH-D Rare Unseeded Birth Stress Test`
   - 왜 현재 한 명만 남을 만큼 희귀한가
   - 통제사회 없이 가능한가
   - 누가 왜 시도했고 어떻게 성공했는가
2. `BIO HUMAN Reveal Fairness Test`
   - 제목/첫 Reveal이 용어장난이 되지 않는지
3. `RB-B Restoration Regression Test`
   - 기존 40개 사건을 유지/수정/폐기 분류
4. `C8 유일한 인간 Character 4안`
   - 특별역할보다 평범한 개인욕망부터
5. Reward Engine + Physical Pressure Engine 보강
6. Character Bible 심화
7. C-full Act/Sub-Act/Information Ladder

아직 어떤 새 설정도 CANON으로 승격하지 않는다.
GitHub를 현재 상태의 정본 저장소로 사용하며 의미 있는 결과는 반드시 동기화한다.
