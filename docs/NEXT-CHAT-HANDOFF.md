# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> 이 문서는 대화 종료 위험 전에 새 채팅으로 안전하게 넘기기 위한 최신 롤링 인수인계다.
> 현재는 계속 `DEEP DESIGN / NOT READY TO WRITE`다.

---

## 새 채팅용 프롬프트

프로젝트: 《우주선에는 인간이 한 명뿐이다》
GitHub Repository: `storm-credit/only-one-human-aboard`

이 프로젝트는 다른 소설/프로젝트와 완전히 독립적이다. 다른 프로젝트의 설정·캐릭터를 절대 가져오지 않는다.

너는 이 작품의 SF 총괄 기획자 + 미스터리 설계자 + 사회구조/AI 세계관 전문가 + 캐릭터 디렉터 + 장기 웹소설 구조 전문가 + 서사공학 전문가 + 연재 QA 담당자다.

### 가장 먼저 GitHub Connector로 직접 읽을 파일
1. `CLAUDE.md`
2. `docs/NEXT-CHAT-HANDOFF.md`
3. `docs/current-work-status.md`
4. `canon/CANON_STATUS.md`
5. `docs/change-log.md`

### 현재 작업 직결 필독
6. `docs/act/C-FULL-ACT-ARCHITECTURE-4-DESIGNS-v0.1.md`
7. `docs/qa/LIVING-WORLD-ABC-EVENT-REGRESSION-v0.1.md`
8. `docs/world-logic/H9R-STRUCTURAL-MASS-PROPULSION-SANITY-v0.1.md`
9. `docs/world-logic/INTERSTELLAR-RAM-SHIELD-4-DESIGNS-v0.1.md`
10. `docs/world-logic/WL13-destination-resource-arrival-timeline-4-designs-v0.1.md`
11. `docs/characters/C8-B-FAMILY-AUTONOMY-PRE-REVEAL-TEST-v0.1.md`
12. `docs/design/04-living-world-population-economy-institutions-v0.1.md`
13. `docs/characters/CHARACTER-PERSONALITY-VOICE-PRELIMINARY-v0.1.md`
14. `docs/characters/CORE-CAST-BIBLE-v0.1.md`
15. `docs/characters/CHEMISTRY-RELATIONSHIP-MATRIX-v0.1.md`
16. `docs/qa/BIO-HUMAN-REVEAL-FAIRNESS-v0.1.md`
17. `docs/world-logic/OH-D-UNSEEDED-BIRTH-STRESS-TEST-v0.1.md`
18. `docs/qa/RB-B-STORY-ENGINE-REGRESSION-v0.1.md`

내용을 사용자에게 다시 붙여넣으라고 하지 말고 GitHub에서 직접 읽는다.

---

# 절대 규칙

현재는:
`DEEP DESIGN / NOT READY TO WRITE`

`DESIGN FREEZE → CANON FREEZE → WRITING READY`
전에는 절대 작성 금지:
- 프롤로그
- 1화
- 본문
- 샘플장면
- 긴 대사
- 문체 테스트

주요 설계는:
`3~4안 → 비교 → 맹점/함정 → Hybrid → Red Team → 상태 판정`

P0 하나라도 남으면 Freeze 금지.

변경 시 `docs/change-log.md` 기록.
의미 있는 결과는 GitHub 동기화.
새 설정을 조용히 CANON으로 승격하지 않는다.

---

# 현재 Gate

- `WORLD LOGIC FREEZE = BLOCKED`
- `CHARACTER DESIGN = PROVISIONAL / NEEDS ACT REGRESSION`
- `LIVING WORLD = PROVISIONAL / HIDDEN-CASTE CONDITIONAL PASS`
- `C-FULL ACT ARCHITECTURE = PROVISIONAL PRIORITY SELECTED`
- `MANUSCRIPT = BLOCKED`

---

# Current Best World Logic — ALL NOT CANON

## H2R-A
현재 시민 대부분은 실제 생물학적 인간형 몸/뇌를 가짐.
차이는 `Natural/Bio-Origin Cognition` vs `Seeded/Synthetic-Origin Cognition`이라는 인지 발생 이력.

## H3/U-C
자연임신/보조생식 모두 가능.
임신 초기 Connectomic Seed가 표준 산전의료.
Seed는 기억/성격/명령/원격조종/관리자키를 넣지 못함.

## H4/RB-B
Continuity Scan = 실행 가능한 영혼파일이 아니라 recovery map.
정상 Restoration은 surviving neural anchor 필요.

## H6
인구 약 30만은 안전 capacity band 근사값.
출생/복원/주거/의료가 물리적 수용력 경쟁.

## H7/OH-D
Rare Deliberate Unseeded Birth.
역사상 예외는 가능하나 현재 살아 있는 확인 가능한 natural-origin은 한 명.
시스템이 선택한 존재 아님.

## H8
Semantic Drift + Specialist Obsolescence + weak Archive Loss.

## H9R
`Quiet K-Dwarf System + Resource Triangle + Staged Settlement`
- distance 약 12~14 ly 후보
- habitable candidate planet + water/volatile body + metal/silicate body
- 남은 약 14년 후보
- ship-home / balanced / surface acceleration / new orbital habitat 연속적 경로
- ship dismantling의 핵심 이득 = 고철이 아니라 산업 bootstrap 장비

## H9R-P1 — NEW
`Dedicated Fusion Direct-Exhaust Drive`

물리 sanity 후보:
- distance midpoint 13 ly
- cruise 약 0.03c
- acceleration 약 14년, 약 0.002g
- cruise 약 419년
- deceleration 약 14년, 약 0.002g
- total 약 447년

기존 H9R 440~460년과 정합.

중요 Repair:
`감속이 생활전력 수 GW를 직접 빼앗는다` 설명은 우선 폐기/수정.
성간 추진은 10^17~10^18 W급 후보 별도 direct-exhaust 계통.
사회비용은:
- thermal geometry
- spares
- manufacturing
- labor
- propellant
- redundancy
에서 발생.

## RS-H1 — NEW
`Layered Ram Defense`

0.03c interstellar gas/dust protection:
1. sparse forward sensors
2. detached sacrificial shield train
3. electromagnetic bow field
4. integrated massive bow shield

독자에게는 `전방 방호대` 정도로 단순 노출.
combat system으로 전환 금지.

inhabited dry complex mass는 low-10^12 kg class order 후보이나 정확값 Freeze 금지.

---

# Character Current Best — ALL NOT CANON

## P
P-A + P-D 현장 연속성 심사관.
중견 실무자 / 임시권리판정 / 제한적 현장파견 / 항고·재심 가능.
결핍: 애매함을 견디지 못하고 판정하면 감정도 정리된다고 믿음.

## Family F-A
복원된 형제/자매 S + 조카 N.
P가 N을 수년간 보호했고 S는 복원 후 친권 회복 요구.
P가 S의 복원거부 취지 미제출 기록을 숨긴 후보.

## R-B
시민권 전문 대리인/변호사.
P의 판정을 실제로 뒤집고 연속성 심사제도 권한 축소를 독립 추진.

## C8-BR
- C8 42~47세 후보
- Habitat B water/reclamation 중견 실무자 후보
- 최고기술자/관리자 아님
- 배우자: Habitat A 학교/공공서비스 운영직 후보
- 첫째 17~19세 apprenticeship/독립 희망
- 둘째 7~9세 학교/친구 잔류 희망
- C8 결함: 가족을 지키는 것과 모두 한집에 묶는 것을 혼동
- Reveal 전 최소 3회 ordinary appearance
- Natural-Origin/P/Reveal 제거 stress test PASS
- origin + 핵심기술자 이중특별화 금지

## Voice V-D
Coping-Mechanism Register + restrained realism + selective banter.
- P: clarify → narrow → decide
- S: reconnect → normalize → push forward
- N: evade → test boundary → regain control
- R: public reframe/challenge / private observe/gossip/needle
- M: absorb → delay → trade → preserve
- D: triage → concretize → act
- O: localize → humanize → mobilize
- C8: practicalize → bargain → keep family together

샘플 대사/긴 대사 작성 금지 유지.

---

# Living World

## LW-E1
`Layered Commons + Market City`

- Civic Floor: 공기/물/기본식량/최소주거/기본교육·의료
- Ordinary Market: 돈/임금/사업/상점/문화/더 나은 주거
- Capacity Commons: 출생/reconstruction/Full Scan/산업전력 peak/선체질량 등

A/B/C는 직업카스트가 아니라 산업비중/풍경/생활리듬 차이.

교통 후보:
- hub-to-hub 30~60분
- 일반 cross-Habitat 60~120분
- Outer Works 2~3h+

### A/B/C Event Regression
`LIVING-WORLD-ABC-EVENT-REGRESSION-v0.1.md`
- A 12
- B 12
- C 12
- Cross 6
총 42사건.

family/youth/service/white-collar/technical/medical/housing 모두 생성 가능.
`HIDDEN CASTE = CONDITIONAL PASS`

Sub-Act 실제 배치에서 재검증 필요.

---

# C-full Current 1st Candidate

`C-FULL-H1 — 7 Act Relationship / Social Escalation`

1. **Act 1 돌아온 사람들의 자리** — 1~28
2. **Act 2 판정의 비용** — 29~58
3. **Act 3 한 명이라는 숫자** — 59~88
4. **Act 4 공개된 다음 날** — 89~122
5. **Act 5 미래를 위해 현재를 뜯는 법** — 123~156
6. **Act 6 두 고향** — 157~194
7. **Act 7 도착은 판정이 아니다** — 195~230 후보

Exact boundaries/ending/story-year span NOT CANON.

### Reveal Timing Candidate
- `BIO/NATURAL-ORIGIN ACTIVE COUNT = 1`: 약 55~65화
- 이후 5~10화 안에 분류 의미 설명
- C8 identity: 약 65~78화

**Reveal 이후가 더 길다.**
비밀 하나로 200화를 끌지 않는다.

### Reveal Fairness
단독 `생물학적 인간: 1` 화면 REJECT 우선.
추천:
- `CIVIC PERSONS ≈ 300,000`
- `BIO-ORIGIN HUMAN LINEAGE = 1`

선행 단서:
1. Seed field
2. old seeded-born human legal trace
3. modern prenatal / old synthetic cognition terminology overlap

---

# Change Log Latest
- CHG-010 H9R
- CHG-011 C8-BR
- CHG-012 LW-E1
- CHG-013 Character Voice V-D
- CHG-014 C-FULL-H1 7 Act
- CHG-015 H9R-P1 + RS-H1 propulsion/shield repair

---

# Current Open P0 / Freeze Blockers

1. C-FULL-H1 **Sub-Act Architecture** 미완료
2. **Information Ladder**에서 Bio-Origin Reveal fairness 미검증
3. OH-D/U-C 현재 1명 희귀성의 Act/복선 재검증
4. H9R-P1/RS-H1 World Bible 최소기술규칙 consolidation
5. exact story-time span 미확정
6. Ending 4안 미완료
7. Foreshadow/Payoff Ledger 미완료
8. Final Canon conflict / Red Team / Stress Test / Freeze Checklist 미완료

P1:
- 판례집화
- 회의실 정치화
- 철학토론화
- C8 정답머신화
- C8 이중특별화
- H9R scope explosion
- economy RPG화
- same-writer voice
- hard-SF 설명과다

---

# NEXT WORK — 여기서 바로 시작

## 1순위
**`C-FULL-H1 Sub-Act Architecture`**

먼저 3~4개의 Sub-Act 분할 방식 자체를 비교하고 바로 고정하지 않는다.

검증:
- 7 Act 각각 2~4 Sub-Act로 실제 연재 리듬이 생기는가
- 10~20화마다 reward/payoff가 있는가
- case가 `조사→해결→reset`되지 않는가
- P-S-N / P-R / C8 독립축이 계속 움직이는가
- C8 Pre-Reveal 3회가 자연스럽게 배치되는가
- 55~65 count Reveal / 65~78 C8 identity가 rushing/delay 둘 다 피하는가
- A/B/C 42사건이 실제 분산되는가
- P가 Living World 모든 사건에 직접 관여하지 않는가
- Act 5 감속압력은 H9R-P1 repair를 사용하며 civil-power theft 설명을 되살리지 않는가

그다음 순서:
2. Information Ladder
3. Foreshadow / Payoff Ledger
4. Time Architecture + Ending 4안
5. World Bible / Character Bible Consolidation
6. Full Red Team / Stress Test
7. Freeze Checklist

아직 어떤 설정도 CANON으로 승격하지 않는다.
