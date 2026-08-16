# Design Change Log

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Template

### CHG-XXX — 제목
- Date:
- Change Location:
- Previous:
- New:
- Reason:
- Trigger / Evidence:
- Characters Affected:
- Acts Affected:
- Foreshadowing Affected:
- World Rules Affected:
- Documents To Repair:
- Status:

---

## CHG-001 — 장편 중심 질문 확장
- Date: 2026-08-16
- Change Location: Core Story Engine
- Previous: ‘30만 명 중 누가 진짜 인간인가?’가 중심 질문으로 보였음.
- New: 장편 중심 질문을 ‘사람인지를 누가 판정할 수 있는가?’로 확장. ‘유일한 인간’은 강력한 미스터리/사회적 폭탄으로 유지.
- Reason: 유일한 인간의 정체만으로 200~300화를 유지하면 비밀 미루기 구조가 됨.
- Trigger / Evidence: B Story Engine 40개 사건 테스트에서 메인 미스터리 없이도 가족·복원·죽음·법·사회 사건이 다수 생성됨.
- Characters Affected: 주인공 직업/욕망, 라이벌
- Acts Affected: 전체
- Foreshadowing Affected: 추후 C-full에서 반영
- World Rules Affected: 인간 정의, 법적 동일성
- Documents To Repair: 향후 Act/Information Ladder
- Status: PROVISIONAL

## CHG-002 — Truth Architecture 우선순위 변경
- Date: 2026-08-16
- Change Location: C-lite Truth Architecture
- Previous: ‘인류가 붕괴해 AI 계승자를 만들었다’는 C1 계승자 문명안이 초기 결말 후보의 기반.
- New: C3 ‘자발적 인공기질 전환’을 기반으로 C1의 증인 계통과 C4의 구식 도착 프로토콜 요소를 섞는 Hybrid H1을 1순위로 올림.
- Reason: AI=가짜/NPC 인상을 줄이고, 현재 30만 명을 실제 후손 문명으로 만들며 악당 없이 사회 SF 갈등을 강화하기 위해.
- Trigger / Evidence: C1~C4 비교에서 C3가 사회 SF·장기성·유사성 위험 측면에서 가장 안정적이었음.
- Characters Affected: 전체 시민, 유일한 인간 후보, 주인공
- Acts Affected: 중후반 전체
- Foreshadowing Affected: 초기 역사/언어/의료 단서
- World Rules Affected: 인간 정의, 출생, 역사, 목적지 프로토콜
- Documents To Repair: World Logic, C-full, Canon Bible
- Status: PROVISIONAL

## CHG-003 — 집필 게이트 강화
- Date: 2026-08-16
- Change Location: Project Workflow
- Previous: 현재 단계에서 본문을 쓰지 않는다는 일반 규칙.
- New: `DESIGN FREEZE → CANON FREEZE → WRITING READY` 통과 전 프롤로그·1화·샘플 장면·긴 대사·문체 테스트까지 금지.
- Reason: 설정집/설계도/세계관을 완성한 뒤 집필한다는 프로젝트 운영 원칙 명확화.
- Trigger / Evidence: 사용자 지시.
- Characters Affected: 없음
- Acts Affected: 없음
- Foreshadowing Affected: 없음
- World Rules Affected: 없음
- Documents To Repair: README, CLAUDE.md, Current Status
- Status: CANON WORKFLOW RULE

## CHG-004 — ‘인공기질’에서 ‘합성기원 의식 + 생물학적 몸’으로 세분화
- Date: 2026-08-16
- Change Location: World Logic / Truth Architecture
- Previous: 현재 30만 명이 인공기질/인공 신체를 사용하는 방향이 유력했음.
- New: 현재 1순위 Body Model은 ‘몸과 뇌는 살아 있는 인간형 생물학적 조직이지만 의식의 발생 기원만 합성’인 H2. 배아 초기 합성 인지 시드로 새로운 의식을 시작시키고 실제 영아기/성장을 거치며, 성인 시점에는 일반 의료검사로 자연기원/합성기원을 구별할 수 없다는 방향.
- Reason: 병원 검사로 유일한 인간이 즉시 드러나는 P0, 30만 중앙연산 문제, AI 캐릭터의 감정적 거리감, 가족/임신/육아의 가짜 느낌을 동시에 줄이기 위해.
- Trigger / Evidence: WL01-02 신체/의료 4안 비교에서 기계신체형과 뉴로코어형은 의료적 은폐에 큰 구멍이 있었고, 생물학적 몸+합성기원 의식형이 가장 적은 보조설정으로 문제를 해결함.
- Characters Affected: 모든 시민, 주인공, 보호대상, 유일한 자연기원 인간 후보
- Acts Affected: 초반 의료사건부터 최종부 인간 정의까지 전체
- Foreshadowing Affected: 출산 프로토콜, 초기 생식기록, ‘생물학적 인간’이라는 용어의 재해석
- World Rules Affected: 신체, 의식, 출생, 의료, 백업, 연산, 인간 정의
- Documents To Repair: Truth Architecture 용어, Canon Bible, Birth Architecture, Backup Architecture
- Status: PROVISIONAL — WL-03 출생 논리 통과 전 Canon 금지

## CHG-005 — World Logic H2~H9 수렴
- Date: 2026-08-16
- Change Location: World Logic 전체
- Previous: 신체/출생/죽음/인구/유일한 인간/역사/목적지가 서로 독립된 미해결 질문이었음.
- New: 현재 1순위 통합모델을 H2~H9로 연결.
  - H2: 생물학적 몸 + 합성기원 의식
  - H3: 보조생식 표준 + 합성 인지 시드
  - H4: 희소 연속성 스캔 + 생활로그 + 조건부 복원
  - H6: 시민 공동 수용량 + 출생/복원 자원 경쟁
  - H7: 세습이 아닌 자연인지 보존 규약
  - H8: 수 세대의 의료/가족 선택으로 합성인지 출생이 표준화된 역사
  - H9: 실제 목적지 + 이중유산 식민계획 + 우주선 고향화
- Reason: 각 P0를 따로 패치하지 않고 하나의 원인-결과 체계로 묶기 위해.
- Trigger / Evidence: 신체/의료, 출생, 죽음/백업, 인구, One Human, History, Destination 4안 비교 및 통합 Red Team.
- Characters Affected: 전 시민, 주인공, 보호대상, 라이벌, 모든 주요 세력
- Acts Affected: 전체
- Foreshadowing Affected: 출생기록, 복원제도, 구역별 문화, 오래된 용어, 목적지 정책
- World Rules Affected: 거의 전체
- Documents To Repair: C-lite Truth Architecture의 ‘인공기질’ 용어를 이후 H8 기준으로 정리, Living World/Act/Character Bible 연결 필요
- Status: PROVISIONAL — 2차 Red Team 및 캐릭터/Act 검증 전 Canon 금지

## CHG-006 — 2차 Red Team에서 ‘생물학적 인간’ 정의 P0 재개방
- Date: 2026-08-16
- Change Location: H2 / Premise Semantics
- Previous: H2의 생물학적 몸 + 합성기원 의식이 제목 전제까지 해결한다고 봄.
- New: 일반 독자 관점에서는 30만 시민 모두 생물학적 몸/DNA를 가지므로 ‘생물학적 인간 한 명’이라는 문장이 용어장난으로 보일 수 있음을 P0로 재등록. H2R 4안 비교 결과 H2R-A를 유지하되 옛 `Bio/Natural-Origin` 분류라는 의미를 명확히 하고, 작품 자체가 그 분류의 정당성을 최종적으로 공격하는 방향을 추천.
- Reason: 제목/첫 대형 Reveal이 독자 기만으로 느껴지면 작품 전체 신뢰가 무너짐.
- Trigger / Evidence: World Logic Red Team v0.2.
- Characters Affected: 전체 시민, 주인공, 유일한 인간 후보
- Acts Affected: 첫 대형 Reveal 이후 전체
- Foreshadowing Affected: 옛 기술용어, 분류체계, 현재 의료용어와의 차이
- World Rules Affected: 인간 정의, 신체/의식 분류
- Documents To Repair: Information Ladder, Foreshadow Ledger, 제목 Reveal 표현
- Status: PROVISIONAL REPAIR — Freeze BLOCKED 유지

## CHG-007 — ‘항상 한 명 유지’보다 현재 세대의 희귀 비시드 출생을 우선 검토
- Date: 2026-08-16
- Change Location: H7 One Human
- Previous: 자연기원 인격이 없으면 시스템이 다음 출생 하나에서 시드를 생략해 항상 한 명을 유지하는 증인/기준선 프로토콜이 1순위.
- New: `OH-D Rare Deliberate Unseeded Birth`를 새 1순위 후보로 올림. 역사적으로 비표준 출생이 전혀 없었던 것은 아니며, 현재 살아 있는 확인 가능한 natural-origin이 한 명인 구조.
- Reason: 선택받은 혈통/비밀 관리자/목적론적 시스템 문제를 줄이고, 유일한 인간이 특별해서 중요한 것이 아니라 사회가 그 차이를 중요하게 만드는 구조로 전환하기 위해.
- Trigger / Evidence: World Logic Red Team v0.2 및 One-Human 4안 재비교.
- Characters Affected: 유일한 인간 후보, 부모/의료진 후보, 주인공
- Acts Affected: 중반 Reveal 이후
- Foreshadowing Affected: 자연출생 운동 기록, 출생 provenance, 비표준 생식 사건
- World Rules Affected: 출생, 인간 수, 역사
- Documents To Repair: 기존 H7, Truth Architecture, Ending 후보
- Status: CANDIDATE PRIORITY CHANGE — 아직 확정 아님

## CHG-008 — Backup을 실행가능 인격파일에서 ‘복구지도’로 축소
- Date: 2026-08-16
- Change Location: H4 Death / Restoration
- Previous: 저빈도 Full Continuity Scan + 생활로그로 사후복원 가능하다는 개념이 성인 새 몸/복제 문제를 열어 둠.
- New: `RB-B Recovery Map + Surviving Neural Anchor`를 1순위로 추천. Scan 자체는 독립 실행 가능한 사람 파일이 아니라 손상된 원 신경기질을 복구하기 위한 지도. 원 신경기질 없이 만든 존재는 가능하더라도 별도 `Derived Person`으로 취급하는 방향.
- Reason: 무제한 복제/불멸/즉시 성인몸 문제를 줄이면서 연속성 사건엔진을 유지하기 위해.
- Trigger / Evidence: Red Team v0.2의 live duplicate 및 adult-body 충돌.
- Characters Affected: 복원된 형제/자매, Continuity Case 전반
- Acts Affected: 초반부터 전체
- Foreshadowing Affected: 복원 대기시간, neural anchor, Derived Person
- World Rules Affected: 죽음, 복원, 백업, 신체생산
- Documents To Repair: 기존 H4 문서, Story Engine 사건 정의
- Status: PROVISIONAL REPAIR

## CHG-009 — 주인공 방향을 현장 연속성 심사관 + Living World 이동성 Hybrid로 강화
- Date: 2026-08-16
- Change Location: Character Architecture
- Previous: 인격연속성 심사관 직업만 1순위 후보.
- New: `P-A 판정형 + P-D 구획이동형` Hybrid를 1순위 후보로 설정. 가족구조는 복원된 형제/자매 + 조카(F-A), 메인 라이벌은 시민권 전문 대리인(R-B)이 우세.
- Reason: 사건해결사 판례집화를 피하면서 개인사건, 구획탐험, Living World, 정치적 후폭풍을 한 주인공 동선에 연결하기 위해.
- Trigger / Evidence: 주인공 4안, 직업/가족/라이벌 4안, Chemistry/Relationship 테스트, 보고 싶은 장면 30개 테스트.
- Characters Affected: 주인공, 가족, 라이벌, 핵심 7인
- Acts Affected: 전체
- Foreshadowing Affected: 가족 복원거부 기록, 판례/제도 변화
- World Rules Affected: 연속성 심사제도
- Documents To Repair: Character Bible, Living World 기관 설계, Act Architecture
- Status: PROVISIONAL CANDIDATE — Canon 금지

## CHG-010 — H9 목적지를 ‘행성 vs 우주선’에서 staged system settlement로 정교화
- Date: 2026-08-16
- Change Location: H9 Destination / Arrival Resource Architecture
- Previous: `이중유산 식민계획 + 우주선 고향화`, 남은 항해 약 10~15년이 1순위였으나 초기정착 자원과 선체해체의 실제 이득은 미정량.
- New: `H9R Quiet K-Dwarf System + Resource Triangle + Staged Settlement`를 1순위 Hybrid로 추천. 목적지는 행성 하나가 아니라 거주가능 후보 행성 + 물/휘발성 자원천체 + 금속자원천체를 가진 별계. 남은 시간은 약 14년 후보. 선체 해체의 핵심 이득을 bulk 고철이 아니라 발전/방열/정밀제조/로봇/공정설비의 산업 bootstrap으로 정의. ship/orbit/surface/new-habitat의 연속적 선택을 유지.
- Reason: 현지 ISRU가 가능한데도 선체를 뜯어야 하는 이유가 없으면 최종 갈등이 가짜가 되고, 반대로 행성정착을 강제하면 `우주선=고향`이 무의미해지기 때문.
- Trigger / Evidence: `WL13-destination-resource-arrival-timeline-4-designs-v0.1.md` 4안 비교 및 Red Team. A Surface-First / B Resource Triangle / C Terminator / D Biosafety 비교에서 B가 장기성·사회갈등·비양자택일성 1위, A가 scope control 1위. A+B controlled Hybrid 추천.
- Characters Affected: P, S, N, R, C8, 선박 전 시민, 향후 정착민
- Acts Affected: 중반 감속준비부터 후반 도착/초기정착까지 전체 장기구조
- Foreshadowing Affected: 목적지 관측자료, 식민용 detachable modules, 구식 mission law, 산업설비 해체, C8 분류의 법적 재등장
- World Rules Affected: H9 목적지, ship resource economy, arrival timeline, population capacity, energy/heat, settlement law
- Documents To Repair: `canon/CANON_STATUS.md`, `docs/current-work-status.md`, C-full Act Architecture, Information Ladder, Foreshadow Ledger
- Status: PROVISIONAL PRIORITY / NOT CANON — structural mass, propulsion/deceleration, Act regression 전 Freeze 금지
