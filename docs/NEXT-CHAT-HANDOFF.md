# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> 이 문서는 대화가 길어지기 전에 새 채팅으로 안전하게 넘기기 위한 롤링 인수인계 문서다.
> 작업이 크게 진행될 때마다 갱신한다.

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
- 대화가 다시 길어지기 전에 이 `docs/NEXT-CHAT-HANDOFF.md`를 갱신하고 사용자에게 새 채팅용 프롬프트를 먼저 제공한다.

## 먼저 읽을 GitHub 문서
1. `CLAUDE.md`
2. `docs/current-work-status.md`
3. `canon/CANON_STATUS.md`
4. `docs/change-log.md`
5. `docs/world-logic/P0-CLOSURE-minimum-rules-v0.1.md`
6. `docs/qa/WORLD-LOGIC-INTEGRATED-RED-TEAM-v0.1.md`
7. `docs/design/01-story-engine-v0.1.md`
8. `docs/design/02-truth-architecture-c-lite-v0.1.md`
9. `docs/design/03-living-world-v0.1.md`

## 현재 1순위 통합 모델 — 전부 PROVISIONAL
- H2 Body/Mind: 시민 대부분은 실제 인간형 생물학적 몸과 살아 있는 뇌를 가진다. 차이는 몸의 재질보다 의식의 발생 기원.
- H3 Birth: 부모 유전정보로 배아를 만들고, 표준 보조생식 과정에서 발달 유도형 합성 인지 시드가 초기 신경발달을 점화. 실제 임신/출산/육아가 존재.
- H4 Death/Backup: 현재 의식은 각자의 살아 있는 뇌에서 작동. 실시간 완전백업 없음. 저빈도 Full Continuity Scan + 생활로그 + 조건부 복원.
- H6 Population: 약 30만은 안전 수용범위의 현재값. 신규출생과 복원이 같은 주거/식량/의료/신체 자원을 경쟁.
- H7 One Human: 선택받은 혈통이 아님. 자연기원 인격이 없을 때 정상 출생 하나에서 인지 시드를 생략하는 역사적 타협 프로토콜이 1순위 후보.
- H8 History: 원래 인간이 한 번에 전멸한 것이 아니라, 수 세대에 걸쳐 seeded birth가 표준화되며 태어나는 방식이 바뀜. 현재 30만은 복제품/NPC가 아니라 실제 후손사회.
- H9 Destination: 목적지는 실제 존재. 우주선은 원래 도착 후 일부 해체되어 식민자원으로 쓰일 계획이었지만 수백 년 사이 30만 명의 고향이 됨. 최종 갈등은 과거의 계획과 현재 살아 있는 사회의 권리가 충돌하는 구조.

## Story Engine 1차 결과
- 인격연속성 사건
- 가족/관계
- 구획별 문명/탐험
- 자원갈등
- 독립적으로 움직이는 세력
- 역사 재해석

40개 사건 생성 테스트를 통과했고 메인 미스터리가 없어도 상당수 사건이 성립한다.
주인공 직업 1순위 후보는 `인격연속성 심사관`.
초기 욕망 1순위 후보는 `보호대상/가족이 사회적 오류로 처리되지 않고 평범하게 살도록 지킨다`.

## 현재 핵심 P0/P1
World Logic 1차 P0는 대부분 PASS candidate이나 Canon 아님.
집중 검증할 문제:
1. Cognitive Seed가 너무 만능 SF 기술처럼 보이는가?
2. 표준 보조생식/발달 체크포인트가 과도한 디스토피아처럼 보이는가?
3. Full Continuity Scan 제한이 충분히 자연스러운가?
4. 자연기원 인간을 의료적으로 쉽게 찾을 수 없는 규칙이 공정한가?
5. 목적지 초기정착 자원 Trade-off를 더 구체화해야 함.
6. 제목의 ‘생물학적 인간 한 명’과 기술적 ‘자연기원 인격 한 명’의 표현 정합성.
7. 보호대상이 유일한 인간일 경우 독자 조기예측 위험.
8. 사건해결사물/회의실 정치/철학강의로 변질될 위험.

## 바로 이어서 할 작업
순서대로 진행:
1. `World Logic Red Team v0.2`
   - 현재 H2/H3/H4/H6/H7/H8/H9를 서로 충돌시키며 공격
   - 문제/가능성/심각도/수정안
   - P0 재오픈 여부 판정
2. 통과하면 `Character Deep Design — 4안`
   - 주인공을 단순 탐정으로 만들지 말 것
   - 직업 / 가족 / 사회적 위치 / 결핍 / 가장 소중한 관계 / 기존 인간관 / 밝혀지면 위험한 개인 비밀
   - 서로 완전히 다른 주인공 4안을 설계하고 비교
3. 추천 주인공 Hybrid 후보
4. 주요 관계 5~7인 Character Bible 후보
5. Chemistry / Relationship Matrix

아직 어떤 설정도 새로 CANON으로 승격하지 않는다.
GitHub를 현재 상태의 정본 저장소로 사용하며 의미 있는 설계 결과는 문서에 동기화한다.
