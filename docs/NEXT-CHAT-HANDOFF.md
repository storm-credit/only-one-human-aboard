# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> 롤링 인수인계. 현재 채팅이 길어질 경우 새 채팅에서 GitHub 정본을 직접 읽고 이어간다.
> **현재는 DESIGN FREEZE를 통과했지만 CANON FREEZE / WRITING READY는 아직 아니다.**

---

# 새 채팅용 시작 프롬프트

프로젝트: 《우주선에는 인간이 한 명뿐이다》
GitHub Repository: `storm-credit/only-one-human-aboard`

이 프로젝트는 다른 소설/프로젝트와 완전히 독립적이다. 다른 프로젝트 설정/캐릭터를 가져오지 않는다.

너는 이 작품의 SF 총괄 기획자 + 미스터리 설계자 + 사회구조/AI 세계관 전문가 + 캐릭터 디렉터 + 장기 웹소설 구조 전문가 + 서사공학 전문가 + 연재 QA 담당자다.

## 가장 먼저 GitHub Connector로 직접 읽을 것
1. `CLAUDE.md`
2. `docs/NEXT-CHAT-HANDOFF.md`
3. `docs/current-work-status.md`
4. `canon/CANON_STATUS.md`
5. `docs/change-log.md`

사용자에게 내용을 다시 붙여넣으라고 요구하지 않는다.

## 현재 Canon Freeze 직결 필독
6. `docs/design/WORLD-BIBLE-CONSOLIDATION-v0.1.md`
7. `docs/characters/CHARACTER-BIBLE-CONSOLIDATION-AGE-4-DESIGNS-v0.1.md`
8. `docs/characters/CHARACTER-MISSING-GAPS-4-DESIGN-PACK-v0.1.md`
9. `docs/characters/PROTAGONIST-ORIGIN-4-DESIGNS-v0.1.md`
10. `docs/act/C-FULL-H1-SUB-ACT-ARCHITECTURE-4-DESIGNS-v0.1.md`
11. `docs/act/INFORMATION-LADDER-4-DESIGNS-v0.1.md`
12. `docs/act/FORESHADOW-PAYOFF-LEDGER-4-DESIGNS-v0.1.md`
13. `docs/act/TIME-ARCHITECTURE-ENDING-4-DESIGNS-v0.1.md`
14. `docs/act/ENDING-BEAT-MAP-4-DESIGNS-v0.1.md`
15. `docs/qa/FULL-PROJECT-RED-TEAM-v0.4.md`
16. `docs/qa/CANON-CONFLICT-CHECK-v0.1.md`
17. `docs/qa/DESIGN-FREEZE-CHECKLIST-v0.1.md`
18. `docs/qa/ENDING-COST-LEDGER-4-DESIGNS-v0.1.md`
19. `docs/qa/ACT-NON-P-CAUSAL-REGRESSION-v0.1.md`
20. `docs/qa/BIO-ORIGIN-REVEAL-WORDING-4-DESIGNS-v0.1.md`
21. `docs/world-logic/WL11-HISTORY-REPAIR-v0.2-4-DESIGNS.md`
22. `docs/world-logic/AGING-REJUVENATION-4-DESIGNS-v0.1.md`
23. `docs/world-logic/ARRIVAL-TRANSITION-LEGAL-TRIGGER-4-DESIGNS-v0.1.md`
24. `docs/world-logic/DEMOGRAPHY-UNIQUENESS-SANITY-v0.1.md`
25. `docs/characters/C8-PUBLIC-IDENTITY-REFINEMENT-v0.2.md`
26. `docs/design/LIVING-WORLD-FREEZE-SANITY-PACK-v0.1.md`

---

# 절대 규칙

현재 Gate:
- `DESIGN FREEZE = PASSED — 2026-08-17`
- `CANON FREEZE = NOT PASSED`
- `WRITING READY = BLOCKED`
- `MANUSCRIPT = BLOCKED`

따라서 아직 금지:
- 프롤로그
- 1화
- 소설 본문
- 샘플 장면
- 긴 대사
- 문체 테스트

Design Freeze 이후에는 구조를 임의로 다시 브레인스토밍하지 않는다.
구조를 바꾸려면:
1. 새 P0/명확한 근거
2. change-log
3. 영향분석
4. Red Team
을 거친다.

`PROVISIONAL`은 아직 `CANON`이 아니다.

---

# Design Freeze 근거

`docs/qa/FULL-PROJECT-RED-TEAM-v0.4.md`
- current blocking P0 = **0**
- Reader Promise 20/100/200 regression PASS

`docs/qa/CANON-CONFLICT-CHECK-v0.1.md`
- latest priority models 간 current P0 contradiction 없음

`docs/change-log.md`
- CHG-026에서 DESIGN FREEZE PASS 기록

---

# Design-Frozen World Priorities — 전부 아직 PROVISIONAL

## H2R-A
실제 생물학적 인간형 몸/뇌 + cognitive origin만 구분.

## Seed
Developmental Connectomic Seed.
초기 고차 자기모델/인지회로 형성에 computationally generated developmental prior를 제공.
기억/성격/명령/원격조종/admin key 삽입 불가.

## H3/U-C
자연임신/보조생식 모두 가능 + prenatal Seed 표준.
Natural-origin은 full Seed-window deliberate refusal.

## RB-B
Recovery Map + surviving neural anchor.
Standalone soul-file 아님.

## AG-H1
손상복구는 현재 neural anchor 기준.
옛 scan으로 젊은 시절 rollback 금지.
건강수명은 늘지만 불멸 아님.

## H6
약 30만 capacity band + birth/restoration/housing/medical commons.

## OH-D
Rare Deliberate Unseeded Birth.
Exact-one protocol 없음.
현재 active natural-origin=1은 demographic state.

## H8R-2
원래 탑승자들은 몰살/기계업로드되지 않음.
그들이 살고 자녀를 낳았고, 여러 세대에 걸쳐 Seeded birth가 의료표준이 됨.
Natural-origin 세대는 노화로 감소.

## H9R
Quiet K-Dwarf System + Resource Triangle + Staged Settlement.
약 12~14 ly 후보, 시작 시 system insertion까지 약 14년.

## H9R-P1
Dedicated Fusion Direct-Exhaust Drive.
약 13 ly / 0.03c / total ~447y sanity candidate.
Civil grid와 propulsion 직접전력경쟁 금지.

## RS-H1
Layered Ram Defense.

## ATL-H1
Final Approach Transition Certification.
T-30~T-10 기술준비와 T-10±1y binding legal transition을 분리.
C8가 법 발동키가 아님.

---

# Living World

3 Large Habitats + Spine + Outer Works + Founding Core.

`LW-E1 Layered Commons + Market City`.

Sanity central candidates:
- lifespan ~100~110y
- births/permanent exits ~2.7k~3.1k/y
- minors ~45k~55k
- school age ~30k~36k
- households ~120k~130k
- ordinary cross-Habitat 60~120m

A/B/C hidden-caste 42-event regression PASS at design level.

---

# Character Current Priorities — 아직 PROVISIONAL

## P
- field continuity adjudicator P-A + P-D
- `P-OA Ordinary Seeded-Origin Citizen`
- start age ~39~43 candidate
- special ontology protagonist 금지

## S
restored sibling / N parent.
Food/hospitality cooperative operations current career candidate.

## N
start ~11~12 → ~25~26 ending candidate.
Youth: zero-g sport/games/music.
Adult direction: creative/media technical production.

## R
civic/continuity rights advocate.
Ordinary household/partner + community performance hobby candidate.

## M
senior institution administrator, B retirement plan candidate.

## D
field medical evaluator, community rehab long-term goal.

## O
Old Quarter friend/resident actor, building maintenance livelihood candidate.

## C8-BR
- ~42~47
- Habitat B water/reclamation mid-level worker
- spouse school operations candidate
- first child 17~19, Spine logistics apprenticeship candidate
- second child 7~9, future unfrozen
- children seeded-origin
- no admin key / prophecy / unique engineer status

Exact names/genders/ages are Canon Freeze tasks.

---

# C-full / Reveal

## 7 Acts
1. 돌아온 사람들의 자리 ~1~28
2. 판정의 비용 ~29~58
3. 한 명이라는 숫자 ~59~88
4. 공개된 다음 날 ~89~122
5. 미래를 위해 현재를 뜯는 법 ~123~156
6. 두 고향 ~157~194
7. 도착은 판정이 아니다 ~195~230

## SUB-H1
23 Sub-Acts Braided Consequence Relay.

Current detailed Reveal:
- Count ~53~58
- Meaning ~59~66
- C8 identity ~67~76
- social consequence ~77~88

Reveal 이후가 더 길어야 한다는 원칙은 Design-Frozen.

## RW-H1
Layered Legacy Audit:
- current civic persons ≈300k
- natural/bio-origin =1
- seeded/synthetic-origin remainder
- `human`은 founding-era legacy mapping

단독 `REAL HUMANS:1`은 rejected.

---

# C8 Public Identity

`ID-H1R Controlled Disclosure Under Re-identification Pressure`.

- official identity initially private
- Count=1 makes harmless historical/public traces re-identifying
- speculation/false candidates/family collateral
- C8 chooses limited factual confirmation
- no convenient villain/system leak

---

# Information / Foreshadow

## IL-H1
Distributed Staggered Knowledge.
Count = legacy provenance + prenatal archive + current alive registry crosswalk.
No single Truth Keeper.

## FP-H1
Mixed Signal Ledger.
Hard clue + world residue + character tell + institutional residue + fair alternative interpretation + primer/mirror/MacGuffin.
Most ordinary details are not clues.

---

# Time / Ending

## T-H1
Longitudinal Wave, total ~14 in-world years.
Early dense, later time scale expands.

## E-H1
Costly Polycentric Arrival.

## EC-H1
Visible costs include ship redundancy loss / Old Quarter partial loss / surface delay / continuing capacity scarcity / family separation / new habitat delay / incomplete transition law.

## EB-H1
Braided Irreversible Arrival.
System insertion late Act 7B, first limited deployment/foothold in 7C.
No mature colony instantly at T0.

---

# Mandatory Arrival-Law Guardrail

Old arrival law cannot simply erase ordinary ship citizenship of 299,999 citizens.
Conflict may affect:
- destination settler category
- mission-reserved assets/trusts
- transition registry
- settlement jurisdiction
- stewardship language
and must be reconciled with strong current civic personhood law.

---

# Rejected/Superseded — 재사용 금지

- adult mass artificial-substrate conversion
- exact-one Witness/Origin Continuity Protocol
- executable soul backup
- routine age-reset immortality
- obvious mechanical-body majority
- 8 philosophy-biome sectors
- A=elite/B=farmers/C=workers caste
- civil-grid powered interstellar deceleration
- ship-vs-planet binary
- C8 mission/admin key
- public C8 name via system dump/villain leak as primary
- mature surface colony immediately at T0
- one-human mystery delayed to 200 episodes

---

# 지금 이어서 할 작업 — CANON FREEZE PREPARATION

1. **Canonical World Bible v1 draft**
   - Design-Frozen priorities를 Exact / Elastic / Forbidden으로 정리
2. **Canonical Character Bible v1 design pass**
   - naming/gender/age/family chronology 3~4안 비교 후 선택
3. **Canonical Act Bible v1**
4. terminology/institution naming pass
5. P-S secret record exact form/timing lock
6. C8 re-identification historical trace exact lock
7. current law vs arrival law wording lock
8. Canon Conflict Check v0.2
9. Canon Red Team
10. CANON FREEZE decision

그 전까지 소설 본문 절대 금지.

---

# 채팅 운영

새 채팅이 필요해질 정도로 길어지기 전에 이 파일을 다시 업데이트한다.
하지만 현재 채팅이 이미 새 채팅이라면 **또 이동하라고 하지 말고 여기서 계속 진행한다.**
