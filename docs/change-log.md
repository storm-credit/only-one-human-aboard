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
- Trigger / Evidence: WL01-02 신체/의료 4안 비교.
- Characters Affected: 모든 시민, 주인공, 보호대상, 유일한 자연기원 인간 후보
- Acts Affected: 전체
- Foreshadowing Affected: 출산 프로토콜, 초기 생식기록, ‘생물학적 인간’ 용어 재해석
- World Rules Affected: 신체, 의식, 출생, 의료, 백업, 연산, 인간 정의
- Documents To Repair: Truth Architecture, Canon Bible, Birth/Backup Architecture
- Status: PROVISIONAL

## CHG-005 — World Logic H2~H9 수렴
- Date: 2026-08-16
- Change Location: World Logic 전체
- Previous: 신체/출생/죽음/인구/유일한 인간/역사/목적지가 서로 독립된 미해결 질문이었음.
- New: H2~H9를 하나의 원인-결과 체계로 연결하는 통합모델을 1순위로 둠.
- Reason: 각 P0를 따로 패치하지 않고 하나의 세계규칙으로 묶기 위해.
- Trigger / Evidence: World Logic 4안 비교 및 통합 Red Team.
- Characters Affected: 전 시민, 주인공, 보호대상, 라이벌, 주요 세력
- Acts Affected: 전체
- Foreshadowing Affected: 출생기록, 복원제도, 역사용어, 목적지 정책
- World Rules Affected: 거의 전체
- Documents To Repair: Canon/World Bible/Act/Character
- Status: PROVISIONAL

## CHG-006 — ‘생물학적 인간’ 정의 P0 재개방
- Date: 2026-08-16
- Change Location: H2 / Premise Semantics
- Previous: H2가 제목 전제를 자동으로 해결한다고 봄.
- New: 30만 시민 모두 생물학적 몸/DNA를 가지므로 ‘생물학적 인간 한 명’ 문장이 용어장난이 될 위험을 P0로 등록. 옛 Bio/Natural-Origin 분류라는 의미를 명확히 하고 작품이 그 분류의 정당성을 공격하는 방향.
- Reason: 첫 대형 Reveal의 독자 신뢰 보호.
- Trigger / Evidence: World Logic Red Team v0.2.
- Characters Affected: 전체 시민, P, C8
- Acts Affected: Reveal 이후 전체
- Foreshadowing Affected: 옛 기술용어/분류체계
- World Rules Affected: 인간 정의
- Documents To Repair: Information Ladder, Reveal QA
- Status: PROVISIONAL REPAIR

## CHG-007 — 자동 ‘항상 한 명’보다 희귀 비시드 출생 우선
- Date: 2026-08-16
- Change Location: H7 One Human
- Previous: 시스템이 자연기원 한 명을 자동 유지하는 Witness Protocol이 1순위.
- New: `OH-D Rare Deliberate Unseeded Birth`를 1순위로 변경.
- Reason: 선택받은 혈통/관리자/목적론 위험 제거.
- Trigger / Evidence: Red Team v0.2 + One-Human 재비교.
- Characters Affected: C8, C8 부모, P
- Acts Affected: 중반 Reveal 이후
- Foreshadowing Affected: 비시드 출생 기록
- World Rules Affected: 출생, 인간 수, 역사
- Documents To Repair: H7/History/Ending
- Status: PROVISIONAL PRIORITY

## CHG-008 — Backup을 Recovery Map으로 축소
- Date: 2026-08-16
- Change Location: H4 Death / Restoration
- Previous: Full Continuity Scan이 실행 가능한 인격파일처럼 읽힐 여지.
- New: `RB-B Recovery Map + Surviving Neural Anchor` 1순위. Scan은 손상된 원 신경기질 복구지도이며 anchor 없는 존재는 별도 Derived Person 후보.
- Reason: 무제한 복제/불멸/성인 새몸 문제 제거.
- Trigger / Evidence: Red Team v0.2.
- Characters Affected: S, Continuity 사건 전반
- Acts Affected: 전체
- Foreshadowing Affected: neural anchor, 복원대기
- World Rules Affected: 죽음, 복원, 백업
- Documents To Repair: H4/Story Engine
- Status: PROVISIONAL REPAIR

## CHG-009 — 주인공을 현장 연속성 심사관 + 이동성 Hybrid로 강화
- Date: 2026-08-16
- Change Location: Character Architecture
- Previous: 인격연속성 심사관 직업만 1순위 후보.
- New: `P-A + P-D` Hybrid, 가족 F-A, 라이벌 R-B를 우선.
- Reason: 사건집화를 피하면서 개인사건/생활권/정치 후폭풍 연결.
- Trigger / Evidence: Character 4안 + Chemistry + 30 wanted scenes.
- Characters Affected: P/S/N/R/M/D/O
- Acts Affected: 전체
- Foreshadowing Affected: 가족복원거부 기록
- World Rules Affected: Continuity institution
- Documents To Repair: Character Bible/Living World/Act
- Status: PROVISIONAL

## CHG-010 — H9를 staged system settlement로 정교화
- Date: 2026-08-16
- Change Location: H9 Destination
- Previous: 이중유산 식민계획 + 우주선 고향화, 자원 정량 미정.
- New: `H9R Quiet K-Dwarf System + Resource Triangle + Staged Settlement`; 약 14년 남음 후보, 산업 bootstrap 자산이 선박해체의 핵심가치.
- Reason: 현지 ISRU와 ship-home 갈등을 동시에 성립시키기 위해.
- Trigger / Evidence: WL13 4안 비교.
- Characters Affected: 전 시민/P/S/N/R/C8
- Acts Affected: 중후반~결말
- Foreshadowing Affected: 관측자료, detachable modules, mission law
- World Rules Affected: 목적지, 자원, 정착
- Documents To Repair: Canon/Act/Info/Foreshadow
- Status: PROVISIONAL

## CHG-011 — C8을 독립 생활가족으로 정교화
- Date: 2026-08-16
- Change Location: C8 Character
- Previous: 평범한 부모라는 골격만 존재.
- New: `C8-BR Work-First Family` — 42~47세 water/reclamation 중견 실무자, 배우자/두 자녀 독립목표, Reveal 전 3회 생활등장.
- Reason: C8 정체를 제거해도 캐릭터가 성립하도록 하기 위해.
- Trigger / Evidence: C8 Family Autonomy 4안.
- Characters Affected: C8 가족/P/R
- Acts Affected: Act 2~7
- Foreshadowing Affected: C8 provenance는 후순위
- World Rules Affected: 없음
- Documents To Repair: Character/Act/Living World
- Status: PROVISIONAL

## CHG-012 — Living World를 Layered Commons + Market City로 정교화
- Date: 2026-08-16
- Change Location: Living World
- Previous: 3 Habitat 구조는 있으나 돈/주거/통근/기관 운영 미정.
- New: `LW-E1 Layered Commons + Market City`; civic floor + ordinary market + hard capacity commons. Habitat는 직업카스트가 아니라 산업비중 차이.
- Reason: 완전배급/완전자유시장 양극단 회피 및 생활감 확보.
- Trigger / Evidence: Living World economy/institution 4안.
- Characters Affected: 전 시민
- Acts Affected: 전체
- Foreshadowing Affected: 생활세계 선행노출
- World Rules Affected: 경제, 주거, 노동, capacity
- Documents To Repair: Canon/World Bible/Act
- Status: PROVISIONAL

## CHG-013 — 캐릭터 목소리를 감정 회피방식에서 분리
- Date: 2026-08-16
- Change Location: Character Voice
- Previous: 역할은 다르나 전원이 같은 작가목소리 위험.
- New: `V-D Coping-Mechanism Register + restrained realism + selective banter`.
- Reason: 철학토론/AI식 완벽대사 방지.
- Trigger / Evidence: Voice 4안 + collision test.
- Characters Affected: P/S/N/R/M/D/O/C8
- Acts Affected: 전체
- Foreshadowing Affected: jargon knowledge
- World Rules Affected: 없음
- Documents To Repair: Character Bible/Act
- Status: PROVISIONAL

## CHG-014 — C-full 7 Act Relationship/Social Escalation 우선화
- Date: 2026-08-16
- Change Location: C-full Act
- Previous: 5~8 Act 구조와 Reveal 시점 미정.
- New: `C-FULL-H1` 7 Act; count 약 55~65, C8 약 65~78 후보, Reveal 이후가 더 긴 구조.
- Reason: 반전 하나를 200화 미루지 않고 후폭풍을 본체로 만들기 위해.
- Trigger / Evidence: Act 4안 + Living World regression.
- Characters Affected: 전체 핵심인물
- Acts Affected: 전체
- Foreshadowing Affected: Seed/old law/C8/H9R
- World Rules Affected: Reveal 적용순서
- Documents To Repair: Sub-Act/Info/Ending
- Status: PROVISIONAL

## CHG-015 — H9R 감속 독립추진계 + Ram Defense
- Date: 2026-08-16
- Change Location: Propulsion / Shield / Act 5 Pressure
- Previous: 감속이 civil grid 수 GW를 직접 뺏는 표현, 성간 먼지방호 미정.
- New: `H9R-P1 Dedicated Fusion Direct-Exhaust Drive`; 약 13 ly / 0.03c / 447y 후보. 추진계는 civil grid와 별도. `RS-H1 Layered Ram Defense` 추가.
- Reason: 추진에너지 규모와 고속 ISM 충돌 물리 보정.
- Trigger / Evidence: H9R propulsion sanity + Ram Shield 4안.
- Characters Affected: 인프라 관련 인물/전 시민
- Acts Affected: Act 5~7
- Foreshadowing Affected: 감속유지/방호/산업예비
- World Rules Affected: 추진, 열, 방호
- Documents To Repair: Canon/World Bible/C-full wording
- Status: PROVISIONAL

## CHG-016 — C-FULL-H1을 23개 Braided Consequence Relay Sub-Act로 정교화
- Date: 2026-08-17
- Change Location: Sub-Act Architecture
- Previous: 7개 Act만 있고 실제 8~12화 단위 연재리듬/비주인공 주도권/Reveal 묶음이 미정.
- New: `C-FULL-H1-SUB-H1 Braided Consequence Relay` 1순위. 7 Act / 23 Sub-Act 후보, Count 53~58 → Meaning 59~66 → C8 67~76으로 촘촘히 보상. 각 Sub-Act는 Primary Track 1 + Secondary Pressure 1, 종료 시 baseline change 필수.
- Reason: 사건집 reset과 10~20화 설명구간을 막고 Reveal 후 장기 후폭풍을 보장하기 위해.
- Trigger / Evidence: `C-FULL-H1-SUB-ACT-ARCHITECTURE-4-DESIGNS-v0.1.md`.
- Characters Affected: P/S/N/R/M/D/O/C8
- Acts Affected: 전체
- Foreshadowing Affected: Reveal timing, C8 pre-reveal, H9R early pressure
- World Rules Affected: 없음
- Documents To Repair: Act/Info/Foreshadow/Ending
- Status: PROVISIONAL SUB-ACT PRIORITY / NOT CANON

## CHG-017 — Information/Foreshadow를 Distributed Staggered + Mixed Signal로 수렴
- Date: 2026-08-17
- Change Location: Information Ladder / Foreshadow Architecture
- Previous: 누가 무엇을 언제 아는지와 hard clue/생활복선/맥거핀 배분이 미정.
- New: `IL-H1 Distributed Staggered Knowledge` + `FP-H1 Mixed Signal Ledger`. Count는 legacy provenance + prenatal archive + current alive registry crosswalk 결과이며, P는 Truth Keeper가 아님. Hard clue는 factual reveal에 제한하고 관계/생활/제도 residue를 더 많이 사용.
- Reason: 400년 은폐음모와 P 천재탐정화를 피하면서 fair-play Reveal을 만들기 위해.
- Trigger / Evidence: Information Ladder 4안, Foreshadow/Payoff 4안.
- Characters Affected: 전체 핵심인물/전문가/시민
- Acts Affected: Act 1~7
- Foreshadowing Affected: Seed, old law, C8, S memo, mission law, H9R
- World Rules Affected: privacy/schema architecture
- Documents To Repair: Canon/World Bible/Act
- Status: PROVISIONAL INFORMATION PRIORITY / NOT CANON

## CHG-018 — 14년 Longitudinal Wave + Costly Polycentric Arrival 결말 우선화
- Date: 2026-08-17
- Change Location: Time / Ending Architecture
- Previous: 230화를 몇 년에 걸칠지, 실제 도착을 본편에서 볼지, 결말 정착경로가 미정.
- New: `T-H1 Longitudinal Wave` — 초반 2년 밀집 후 시간폭 확대, 약 14년 실제 경과하여 system insertion까지 도달. `E-H1 Costly Polycentric Arrival` + `EC-H1 Shared Constraint Portfolio` + `EB-H1 Braided Irreversible Arrival`을 1순위. Ship/Orbit/Surface/New Habitat를 병행하되 redundancy loss, 정착지연, 가족분산, capacity scarcity 등 실제 비용 부과.
- Reason: 미래세대를 실제 성장시키고 도착을 payoff로 쓰면서도 ‘행성=정답’/공짜 제3길을 피하기 위해.
- Trigger / Evidence: Time+Ending 4안, Ending Cost Ledger, Ending Beat Map.
- Characters Affected: P/S/N/R/M/O/C8 가족, 전 시민
- Acts Affected: 전체, 특히 5~7
- Foreshadowing Affected: countdown, career/settlement paths, asset transfer
- World Rules Affected: arrival timing, settlement paths, transition law
- Documents To Repair: Canon/Character/World Bible
- Status: PROVISIONAL TIME/ENDING PRIORITY / NOT CANON

## CHG-019 — Character Age/생활앵커 + P를 평범한 Seeded-Origin으로 우선화
- Date: 2026-08-17
- Change Location: Character Bible
- Previous: 14년 시간축에 맞는 나이, S/R/M/D/O의 비주제 삶, P의 origin이 미정.
- New: `AGE-B Midlife Bridge` 1순위. P/S 약 39~43, N 11~12, C8 42~47 등의 시작범위 후보. S는 food/hospitality operations, N은 creative/media adult path, R은 ordinary household + performance hobby, M은 B 은퇴계획, D는 community rehab, O는 building maintenance, C8 spouse school operations, first child Spine logistics 후보. P는 `P-OA Ordinary Seeded-Origin Citizen` 1순위.
- Reason: 14년 장기성, 주제기능 캐릭터화, P까지 특별해지는 위험을 줄이기 위해.
- Trigger / Evidence: Character Bible Consolidation, Missing-Gaps 4-Design Pack, Protagonist Origin 4안.
- Characters Affected: 핵심 캐스트 전체
- Acts Affected: 전체
- Foreshadowing Affected: P의 mundane Seed field, N/C8 family growth
- World Rules Affected: 없음
- Documents To Repair: Canon Character Bible
- Status: PROVISIONAL CHARACTER PRIORITY / NOT CANON

## CHG-020 — Demography와 Aging을 결합해 ‘현재 한 명’/유한수명 P0 보정
- Date: 2026-08-17
- Change Location: Population / Aging / Restoration
- Previous: ‘현재 정확히 한 명’이 작가 숫자처럼 보이고 Recovery Map이 노화까지 되감아 불멸을 만들 수 있는 구멍.
- New: Demography sanity에서 수십만 출생당 1회 수준의 full Seed refusal이면 현재 active 1명이 통계적으로 자연스러움을 확인. `AG-H1 Injury-Relative Reconstruction + Partial Healthspan Extension`으로 현재 neural anchor 기준 손상복구만 허용하고 chronological rollback 금지. 평균적 건강수명 중심 100~110년 후보, 넓은 범위 90~120년.
- Reason: Witness Protocol 없이 한 명 상태를 만들고 죽음/노화/세대교체를 유지하기 위해.
- Trigger / Evidence: `DEMOGRAPHY-UNIQUENESS-SANITY-v0.1.md`, `AGING-REJUVENATION-4-DESIGNS-v0.1.md`.
- Characters Affected: 전 시민, M/P/S/N/C8
- Acts Affected: 전체 장기시간축
- Foreshadowing Affected: Finality, 과거 natural-origin 기록
- World Rules Affected: 수명, 복원, 인구
- Documents To Repair: Canon/World Bible
- Status: PROVISIONAL P0 REPAIR / NOT CANON

## CHG-021 — Arrival Law를 Final Approach Transition Certification로 정교화
- Date: 2026-08-17
- Change Location: H9R Arrival Law
- Previous: T-30/T-20부터 준비했는데 Act 5에서 old mission law가 갑자기 발견/발효하는 시간충돌.
- New: `ATL-H1 Final Approach Transition Certification`. 기술계획은 수십 년 전부터 일반 civic law 아래 진행. T-10±1y 후보의 navigation/survey/industrial/legal 다기관 인증 이후에만 current civic law와 founding arrival clauses의 binding reconciliation이 시작. C8는 trigger가 아님.
- Reason: 늦은 법률갈등의 개연성과 Anti-Chosen-One 보장.
- Trigger / Evidence: Arrival Transition Legal Trigger 4안 + Red Team v0.3.
- Characters Affected: P/R/M/C8, 전 시민
- Acts Affected: Act 5~7
- Foreshadowing Affected: arrival compliance schedule, mission clauses
- World Rules Affected: transition jurisdiction, settlement law
- Documents To Repair: Canon/Act/Ending
- Status: PROVISIONAL P0 REPAIR / NOT CANON

## CHG-022 — C8 공개를 leak이 아닌 re-identification pressure + 통제 공개로 정교화
- Date: 2026-08-17
- Change Location: C8 Public Identity
- Previous: 강한 privacy 아래 C8 이름이 어떻게 사회적으로 알려지는지 미정; 일시적 업무제한을 disclosure pressure로 쓰는 안은 의료설정과 충돌 위험.
- New: `ID-H1R Controlled Disclosure Under Re-identification Pressure`. Count=1 공개 후 옛 공개기록/지역사/비시드 논쟁 조각을 결합한 사회적 재식별이 진행되고 오인/가족피해가 커지자 C8이 제한된 공식 확인을 선택. 정부/악당 leak은 주원인 아님.
- Reason: 개인정보보호와 C8 agency를 동시에 살리고, 억지 직업위험을 제거하기 위해.
- Trigger / Evidence: C8 Disclosure 4안 + v0.2 refinement.
- Characters Affected: C8/배우자/자녀/R/P
- Acts Affected: Act 3~4
- Foreshadowing Affected: historical natural-development traces
- World Rules Affected: privacy/re-identification
- Documents To Repair: Canon/Info/Act
- Status: PROVISIONAL P0 REPAIR / NOT CANON

## CHG-023 — History를 ‘다세대 Seed 표준화’로 Repair하고 정확히 한 명 유지 규약 폐기
- Date: 2026-08-17
- Change Location: H8 History
- Previous: C-lite의 ‘인공기질 전환’과 WL11 후반의 one-at-a-time 기원연속성 규약이 최신 H2/OH-D와 충돌.
- New: `H8R-2 Multi-Generation Medical Adoption + Rights Normalization`. 원래 인간들은 살고 자녀를 낳았으며, Seed의 의료적/경로의존적 이점 때문에 다음 세대에서 seeded birth가 표준화. 자연기원 세대는 노화로 사라지고 드문 비시드 예외는 계속 가능. 정확히 한 명을 유지하는 시스템/규약 없음.
- Reason: 원래 30만 인간의 운명, 생물학적 몸, OH-D, privacy/history를 한 원인계로 통합하기 위해.
- Trigger / Evidence: WL11 v0.1 conflict check + H8R-2 4안.
- Characters Affected: 전 시민/C8/P
- Acts Affected: Act 2~5 history reveal
- Foreshadowing Affected: Seed adoption, rights reform, natural-development records
- World Rules Affected: 역사, 인간 정의, 출생
- Documents To Repair: Canon/Truth/World Bible
- Status: PROVISIONAL HISTORY REPAIR / NOT CANON

## CHG-024 — Living World Freeze Sanity 수치범위 통과
- Date: 2026-08-17
- Change Location: Living World Demography / School / Medical / Transit
- Previous: LW-E1은 구조만 있고 30만 사회의 실제 가족·학교·병원·통근 처리량이 미검증.
- New: central order 후보로 lifespan 100~110y, births/permanent exits 2.7k~3.1k/y, minors 45k~55k, school age 30k~36k, households 120k~130k, 학교 70~130 unit, 병원 6~12 + clinics, Continuity mapping 수십 병렬 suite, major reconstruction 수백/y, ordinary cross-Habitat 60~120m가 서로 양립 가능함을 확인.
- Reason: Living World가 숫자 없는 테마파크가 아니라 실제 도시문명인지 검증.
- Trigger / Evidence: `LIVING-WORLD-FREEZE-SANITY-PACK-v0.1.md`.
- Characters Affected: 전 시민/N/C8 family
- Acts Affected: 전체
- Foreshadowing Affected: 없음
- World Rules Affected: 인구/교육/의료/교통
- Documents To Repair: Canon/World Bible
- Status: PROVISIONAL SANITY PASS / NOT CANON EXACT NUMBERS

## CHG-025 — Reveal 문구를 Layered Legacy Audit로 확정 후보화
- Date: 2026-08-17
- Change Location: Major Reveal Wording
- Previous: 단독 `생물학적 인간: 1` 또는 `HUMANS:1`은 용어장난/독자기만 위험.
- New: `RW-H1 Layered Legacy Audit`. 같은 정보구조에서 current civic persons ≈300k + natural/bio-origin=1 + seeded-origin remainder를 보여주고 `human`은 founding-era legacy mapping임을 드러냄. 5~8화 내 의미설명.
- Reason: 제목 충격과 factual fairness 동시 확보.
- Trigger / Evidence: Bio-Origin Reveal Wording 4안 + v0.4 Red Team.
- Characters Affected: 전 시민/P/C8
- Acts Affected: Act 2D~3A
- Foreshadowing Affected: Seed field, old law, synthetic-origin term
- World Rules Affected: 분류표현/정보아키텍처
- Documents To Repair: Canon/Info/Act
- Status: PROVISIONAL REVEAL PRIORITY / NOT CANON

## CHG-026 — Deep Design 구조를 Design Freeze 통과 상태로 전환
- Date: 2026-08-17
- Change Location: Project Workflow Gate
- Previous: `DEEP DESIGN / WORLD LOGIC FREEZE BLOCKED`; P0와 필수 설계항목이 남아 있었음.
- New: Full Red Team v0.4에서 current blocking P0 = 0. World Logic, Living World, Character Architecture, 7 Act, 23 Sub-Act, Information Ladder, Foreshadow/Payoff, Time, Ending, 장기 Regression, P0 Stress Test가 모두 통합 우선안을 가짐. 따라서 **`DESIGN FREEZE = PASSED`**로 이동하고 다음 단계는 `CANON FREEZE PREPARATION`으로 전환. 아직 어떤 설정도 자동 CANON 승격하지 않으며 원고는 계속 BLOCKED.
- Reason: 사용자 정의 Freeze 조건 중 구조적 Deep Design과 P0 closure가 충족됨. 이후 남은 것은 exact names/ages/terminology/institution labels 및 provisional→canon 승격 작업.
- Trigger / Evidence: `FULL-PROJECT-RED-TEAM-v0.4.md`, `CANON-CONFLICT-CHECK-v0.1.md`, `DESIGN-FREEZE-CHECKLIST-v0.1.md` 및 최신 repair 문서군.
- Characters Affected: 전체
- Acts Affected: 전체
- Foreshadowing Affected: 전체 Ledger를 현 구조에 고정
- World Rules Affected: workflow state only; structural candidate set frozen pending Canon Freeze
- Documents To Repair: `canon/CANON_STATUS.md`, `docs/current-work-status.md`, `docs/NEXT-CHAT-HANDOFF.md`, consolidated World/Character Bible
- Status: DESIGN FREEZE WORKFLOW STATE — `PASSED`; CANON FREEZE/WRITING READY는 아직 아님