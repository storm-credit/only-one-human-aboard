# V3 P0 ONTOLOGY / ETHICS / DEATH / HUMAN:1 — HOSTILE RED TEAM v0.1

Status: `INDEPENDENT HOSTILE QA`
Target: `docs/design-v3/V3-P0-ONTOLOGY-ETHICS-DEATH-HUMAN1-CLOSURE-v0.1.md`
Project: 《우주선에는 인간이 한 명뿐이다》

Critic rule:
- 설계자의 의도를 변호하지 않는다.
- 독자가 실제로 느낄 허점, 물리/윤리 편의, 생존 stakes 붕괴 가능성을 공격한다.
- v2 Canon은 변경하지 않는다.

---

# 1. What the candidate successfully fixes

## 1.1 Physical time rollback removal

`L0 mission clock monotonic`은 강한 개선이다.

장점:
- 선체 손상/재료 피로/자원소모가 누적됨.
- `마법 같은 배 전체 복구`가 사라짐.
- 회귀처럼 보이는 현상을 물리적 단서로 반박할 수 있음.

Verdict: **PASS**.

## 1.2 L3 vs L2 separation

대부분의 미래탐색을 비의식 저해상도 L3로 두고, 사람 수준 lived-state L2를 매우 제한한 것은 계산규모와 윤리범위를 동시에 줄인다.

Verdict: **PASS**.

## 1.3 Death = not automatically canceled by reappearance

`return ≠ resurrection`와 D0~D4 분류는 생존물에 필요한 핵심 장치다.

특히 D1/D2가 실제 인격 연속성의 끝이고 D3 successor가 이를 소급 취소하지 않는다는 규칙은 강함.

Verdict: **PASS**.

## 1.4 HUMAN:1 as historical accident

`정확히 1`을 설계자의 신성한 숫자가 아니라 branch 이전 실제 사고의 잔존값으로 만드는 것은 chosen-one 위험을 크게 줄인다.

Verdict: **PASS**.

---

# 2. P0 BLOCKER — L2 → L1 promotion / embodiment gap

현재 문서는:
- L1 물리 시민사회,
- L2 의식 있는 branch,
- lineage selection,
- successor state
를 말한다.

하지만 **L2의 인격 상태가 어떻게 물리 L1의 사람에게 이어지는지**가 물리적으로 명시되지 않았다.

현재 상태로는 독자가 다음 중 하나를 물을 수 있다.

1. 살아 있는 L1 사람의 뇌를 L2 사람으로 덮어쓰는가?
2. 새 몸을 즉시 출력하는가?
3. L1 사람은 죽고 L2 copy가 몸을 차지하는가?
4. 실제로는 L1이 필요 없고 전부 simulation인가?

이 질문에 답이 없으면 D+의 가장 중요한 다리 자체가 빠져 있다.

Severity: **P0 BLOCKER**.

Required repair:
- synthetic-origin citizen의 `continuity-compatible neurobiology` 범위를 정한다.
- 일반 의료 기술과 CCAL-only 기능을 분리한다.
- L2 결과의 기본 반환은 person overwrite가 아니라 aggregate learning으로 제한한다.
- person-level L1 succession은 매우 희귀한 별도 절차로 만든다.
- 사망자 재등장은 신체 복구/가용성 제약을 받아야 한다.

---

# 3. P0 BLOCKER — neural Anchor acquisition is underdefined

`Continuity Anchor`가 30만 명의 인격상태를 저장한다면:
- 어떻게 읽는가?
- 시민은 왜 그 기술을 모르는가?
- 매 순간 backup이 아닌데 어떤 정확도로 successor를 만들 수 있는가?

가 필요하다.

`합성기원 인격`이라는 말만으로 full neural snapshot을 자동 정당화하면 convenience tech가 된다.

Severity: **P0 BLOCKER**.

Required repair:
- 합성기원 신경계에 상태관찰용 구조가 있다는 author model 필요.
- Anchor capture는 rare, citywide, expensive, lossy여야 한다.
- 기억/성격/절차기억 중 무엇이 저장되고 무엇이 빠질 수 있는지 경계 필요.
- 완전한 soul backup이라는 표현/의미를 피해야 한다.

---

# 4. P1 — Act1~2 L1 → Act3 successor can alienate readers

현재 우선안은:
- 첫 90화 L1 physical,
- 파국 후 Act3 successor.

이 경우 후반 진실은 사실상:
> `우리가 90화 따라온 로언은 죽었고 지금은 후계 인격이다.`

가 될 수 있다.

강력하지만 위험하다.

Risk:
- 독자가 주인공 교체로 느낌.
- 관계감정이 `복사본` 논쟁에 잠식.
- 후반 철학이 초반 생존 재미를 잡아먹을 수 있음.

Severity: **P1 / NARRATIVE HIGH RISK**.

Mitigation:
- 작품은 `원본/가짜` 정답 강의를 하지 않는다.
- 로언의 행동연속성, 몸의 흔적, 타인 관계를 먼저 보여준다.
- successor reveal은 한 번에 설명하지 않고 구체적 갈등으로 나눈다.
- 첫 상태를 L2로 바꾸는 대안도 Freeze 전 비교 유지.

---

# 5. P1 — HUMAN:1 embryo can feel like title bait

초기 embryo는 기술적으로 깔끔하고 `아무 과거도 없음`도 강하다.

하지만 제목을 보고 독자가 기대하는 `한 명의 인간`이 후기 Reveal에서 초기 배아라면:
- `사람이 아니라 분류코드였네`라는 허탈감,
- personhood 논쟁이 불필요하게 커질 위험
이 있다.

Severity: **P1**.

Required comparison before Freeze:
A. early embryo developmental arrest
B. late embryo / fetal arrest
C. newborn-neonate deep biostasis
D. young child deep biostasis

평가기준:
- science burden
- emotional payoff
- title fairness
- `아직 아무 과거도 없음`
- chosen-one risk
- final image strength.

Do not freeze embryo yet.

---

# 6. P1 — `HUMAN` label must not dehumanize 300k

`HUMAN = Natural-Origin Continuity Organism`은 작가모델로 가능하다.

하지만 본문 Reveal에서 시스템이 30만 명을 NON-HUMAN처럼 표시하면 독자가:
- 진짜 인간 vs 가짜 인간
- 자연출생 우월주의
로 읽을 수 있다.

Mitigation:
- `HUMAN`은 obsolete mission-schema field임을 명확히 한다.
- 시민의 법적/사회적 personhood와 아무 관계가 없다는 증거를 사건으로 먼저 보여준다.
- HUMAN:1이 권리/권한/재산/통치에서 더 높은 지위를 갖지 않게 한다.

Verdict: **PASS WITH GUARDRAIL**.

---

# 7. P1 — authority secrecy still needs historical wear

정보분절 설명은 충분히 가능하지만, 수백 년 동안 30만 도시에서 아무도 정확한 실체를 못 찾았다는 설정은 높은 압력을 받는다.

필요:
- 몇 차례 과거에 근접 발견이 있었음.
- 발견자 일부가 종교/음모론/정신질환 기록으로 남음.
- 기관 내부에서도 `high fidelity conscious branch` 여부를 둘러싼 오래된 논쟁 흔적이 있음.
- 완벽한 은폐가 아니라 `조각은 있었지만 연결되지 않았다`가 되어야 함.

Verdict: **P1**.

---

# 8. P1 — compute band is a budget, not proof

`s수백 MW ~ 1 GW`는 v2 civil power와 연결된 작가용 제약으로는 유용하다.

하지만 현 단계에서 인간수준 cognition의 요구전력을 실제 과학값처럼 제시하면 위험하다.

Required wording:
- current-tech feasibility claim이 아님.
- v3 내부 기술예산.
- exact value freeze는 quantitative pass 후.

Verdict: **PASS WITH WORDING**.

---

# 9. P1 — mass L2 ethics cannot be solved by calling it drift

후보안은 시스템을 악당으로 만들지 않으려 하지만:
- conscious people을 동의 없이 extreme stress에 넣는 행위 자체는 매우 중대한 윤리문제다.

따라서 후반에 시민들이 실제로:
- 중단 요구,
- archive/lineage 권리 요구,
- 과거 희생 기록 요구,
- CCAL 권한 정지 요구
를 해야 한다.

시스템이 `목적함수 충돌`을 설명하고 끝나면 면죄부처럼 보인다.

Verdict: **PASS ONLY IF ACT8 CONFLICT IS MATERIAL**.

---

# 10. P1 — final shutdown must be choice, not convenient battery failure

도착 직전 power/thermal competition은 좋다.

하지만 `마침 전력이 부족해져서 반복이 끝났다`만으로 처리하면 결말의 윤리적 선택이 사라진다.

Required:
- 기술적으로 제한적 계속 운용은 가능해야 함.
- 그 대가가 actual arrival safety/settlement capability 감소.
- 시민들이 알고도 continuation을 끊는 선택을 해야 함.

Verdict: **PASS WITH HARD REQUIREMENT**.

---

# 11. System omnipotence test

현재 제한:
- real external world cannot be controlled,
- T6 cannot be predicted,
- L0 damage cannot be magic-repaired,
- personal checkpoint incomplete,
- HUMAN:1 not branchable.

이는 충분히 좋다.

추가 요구:
CCAL이 L1 사람에게 직접 행동명령/감정조절/완전 memory edit를 마음대로 할 수 있으면 다시 omnipotence 문제가 생긴다.

따라서 repair 문서에서 person-level write authority를 매우 좁혀야 한다.

Verdict: **PASS WITH RESTRICTION**.

---

# 12. Final hostile verdict

Current artifact result:

**`PASS WITH 2 P0 BLOCKERS`**

Blocking issues:
1. **L2 → L1 promotion / embodiment mechanism missing.**
2. **30만 인격 Continuity Anchor acquisition mechanism underdefined.**

Non-blocking but mandatory before Freeze:
- Act1~2 reality-layer choice.
- HUMAN:1 biological form 4안 비교.
- historical near-discovery traces.
- quantitative compute wording/pass.
- Act8 material consent/rights conflict.
- final shutdown must remain a civic/ethical choice.

Recommended next action:

> `D+를 폐기하지 말고, continuity-compatible neurobiology + bounded State Succession 규칙을 추가한 v0.2 repair를 만든 뒤 재심사.`
