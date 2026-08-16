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

### 먼저 읽을 GitHub 파일
1. `CLAUDE.md`
2. `docs/current-work-status.md`
3. `canon/CANON_STATUS.md`
4. `docs/change-log.md`
5. `docs/qa/WORLD-LOGIC-RED-TEAM-v0.2.md`
6. `docs/world-logic/WL-REPAIR-v0.2-4-designs.md`
7. `docs/world-logic/OH-D-UNSEEDED-BIRTH-STRESS-TEST-v0.1.md`
8. `docs/qa/BIO-HUMAN-REVEAL-FAIRNESS-v0.1.md`
9. `docs/qa/RB-B-STORY-ENGINE-REGRESSION-v0.1.md`
10. `docs/research/CONNECTOMIC-SEED-SCIENCE-BOUNDARY-v0.1.md`
11. `docs/characters/PROTAGONIST-4-DESIGNS-v0.1.md`
12. `docs/characters/PROTAGONIST-HYBRID-DEEPENING-v0.1.md`
13. `docs/characters/CORE-CAST-BIBLE-v0.1.md`
14. `docs/characters/CHEMISTRY-RELATIONSHIP-MATRIX-v0.1.md`
15. `docs/characters/C8-ONE-HUMAN-4-DESIGNS-v0.1.md`
16. `docs/design/WANTED-SCENES-30-v0.1.md`
17. `docs/design/REWARD-PHYSICAL-PRESSURE-ENGINES-v0.1.md`
18. `docs/design/03-living-world-v0.2.md`

### 현재 Gate
- `WORLD LOGIC FREEZE = BLOCKED`
- `CHARACTER DESIGN = IN PROGRESS`
- `LIVING WORLD v0.2 = PROVISIONAL`
- `MANUSCRIPT = BLOCKED`

### 현재 핵심 1순위 후보 — 전부 미확정

#### World Logic
- 시민 대부분은 실제 인간형 생물학적 몸/뇌와 실제 가족/성장을 가짐.
- 차이는 `Natural/Bio-Origin Cognition` vs `Seeded/Synthetic-Origin Cognition`이라는 인지 발생 이력.
- Seed는 단순 산전 자극이 아니라 **computationally generated connectomic growth prior**를 초기 뇌 발달에 적용하는 미래기술.
- 기억/성격/충성/명령/원격조종/관리자키 삽입 불가.
- 자연임신/보조생식 모두 가능하고, 임신 초기 Connectomic Seed가 수백 년 동안 평범한 표준 산전의료가 된 U-C 모델 우세.
- Continuity Scan은 실행 가능한 영혼파일이 아니라 `recovery map`.
- 정상 복원에는 원 neural anchor 필요. anchor 없이 만든 존재는 `Derived Person` 별도 범주 후보.
- 현재 natural-origin 한 명은 항상 유지되는 Witness가 아니라 `OH-D Rare Deliberate Unseeded Birth` 후보가 우세.
- 역사상 비시드 출생이 전혀 없었던 것은 아니며 **현재 살아 있는 확인 가능한 사람이 한 명**.
- 본인은 비시드 출생 가족사는 알 수 있지만 그것이 옛 분류의 ‘유일한 인간’이라는 의미는 모르는 K2 후보.
- 역사 지식은 중앙정부 삭제가 아니라 `Semantic Drift + Specialist Obsolescence + 약한 Archive Loss`.
- 목적지는 실제 존재. 우주선은 이미 고향이 됐고 행성정착 속도와 우주선 보존은 연속적 자원 Trade-off.

#### Reveal Fairness
단독 `생물학적 인간: 1` 화면은 REJECT 우선.
추천:
- `CIVIC PERSONS ≈ 300,000`
- `BIO-ORIGIN HUMAN LINEAGE = 1`
처럼 두 분류를 함께 보여주고, 옛 분류의 의미가 문제임을 공정하게 제시.

선행 단서 최소 3종:
1. 출생기록 Seed field
2. seeded-born human recognition 옛 법률 흔적
3. 현대 산전의료와 옛 synthetic cognition 연구용어의 겹침

#### Protagonist
`P-A 판정형 + P-D 구획이동형` Hybrid.
가칭 `현장 연속성 심사관`.
중견 실무자, 임시 권리판정, 제한적 현장파견, 항고/재심 가능.

결핍:
애매함을 견디지 못하고 판정하면 감정도 정리된다고 믿음.

가족 F-A:
- 복원된 형제/자매 S
- 조카 N
- 사고 후 P가 N을 수년간 보호
- S 복원 후 친권 회복 요구

P의 비밀 후보:
S가 생전 남긴 복원거부 취지의 미제출 기록을 발견했으나 공개하지 않음.

라이벌 R-B:
시민권 전문 대리인/변호사. P의 판정을 실제로 뒤집고 연속성 심사제도 권한 축소를 독립적으로 추진.

#### C8 Sole Natural-Origin
현재 1순위 `C8-B`:
- 30대 후반~50대의 평범한 부모
- 부모가 C8 임신 때 seed를 거부
- C8은 오히려 부모 결정을 위험한 고집으로 생각했을 수 있음
- 자기 자녀에게는 모두 표준 seeded prenatal care 선택
- Reveal 뒤 옛 시스템은 C8만 human, 배우자/자녀는 synthetic-origin으로 분류
- 핵심 감정: `나만 인간이고 내 아이들은 아니라는 말을 왜 받아들여야 하지?`
- 특별능력/관리자권한 없음
- 주인공 조카 N과 C8은 분리 추천

#### Living World v0.2
3개의 거대 회전 Habitat + Spine/Outer Works.
- Habitat A: Civic / Old Urban
- Habitat B: Green / Watershed
- Habitat C: Technical / Mixed Worker Residence
- Non-Rotating Spine: 교통/물류/무중력 작업
- Outer Works: 외벽/방열/전력/위험정비
- Founding Core/Legacy Decks: 초기 거주/설비 잔존

v0.1의 독립 `유년원`, `제작환`, `기억원`은 REJECT 추천.
`구환`은 Habitat A의 Old Quarter로 축소.

사회집단은 철학정당이 아니라 이해관계 기반 네트워크로 재구성.

### 이미 통과한 내구성 테스트
- 40개 사건 생성 테스트 PASS
- 30개 보고 싶은 장면 PASS
- 메인 미스터리 직접 연결 약 5~6개뿐이어도 장면 작동
- RB-B 복원규칙 적용 후 40개 사건 중 약 27 유지 / 10 수정 / 3 재설계 → Story Engine PASS
- Chemistry: P×S / S×N / P×R / P×D / P×O 강함
- Non-combat physical pressure 6개 + reward 8개 확보

### 아직 중요한 위험
- ‘Bio-Origin Human’ 표현이 끝까지 용어장난처럼 보이지 않아야 함
- OH-D/U-C의 현재 1명 희귀성은 Act/사회설계에서도 검증 필요
- C8가 작품의 도덕적 정답머신이 되면 안 됨
- 사건해결사 판례집/회의실 정치/철학토론화 계속 감시
- Habitat A/B/C가 도시/농민/노동자 카스트처럼 보이면 안 됨
- 목적지 남은 항해기간/초기정착 자원모델 아직 미확정

### 바로 이어서 할 작업
**1순위부터 순서대로 진행:**
1. `Destination Resource & Arrival Timeline 4안`
   - 어디로 가는가
   - 왜 가는가
   - 얼마나 남았는가
   - 실제 거주가능성
   - 착륙/초기정착 자원
   - 우주선 보존과 식민 가속 Trade-off
2. `C8-B Family Autonomy / Pre-Reveal Appearance Test`
3. Living World v0.2 인구/경제/기관 Deep Pass
4. Character Bible 성격/대사 Preliminary
5. C-full 5~8 Act Architecture
6. Sub-Act / Information Ladder / Foreshadow Ledger

아직 어떤 새 설정도 CANON으로 승격하지 않는다.
GitHub를 현재 프로젝트 정본 저장소로 사용하고 의미 있는 설계는 계속 동기화한다.
