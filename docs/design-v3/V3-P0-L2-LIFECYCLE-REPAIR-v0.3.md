# V3 P0 REPAIR v0.3 — L2 LIVED-LINEAGE LIFECYCLE

Status: `P0 REPAIR CANDIDATE / NOT CANON / FINAL P0 CRITIC NEXT`
Project: 《우주선에는 인간이 한 명뿐이다》

Repairs the remaining blocker from:
`docs/qa/V3-P0-ONTOLOGY-RE-RED-TEAM-v0.2.md`.

---

# 0. Core correction

기존 `full-lived lineage 12~24개` working band를 **폐기 후보**로 돌린다.

그 수는:
- 계산비용,
- branch survivor 윤리,
- 인격 duplicate 누적,
- 독자 이해도
모두에 불리하다.

새 원칙:

> **고해상도 lived civilization은 여러 개를 만들고 버리는 것이 아니라, 1개의 Primary Lived Lineage를 오래 살아가게 하고 상태를 바꾼다.**

대부분의 `다른 역사`는 새 30만 인격을 만드는 것이 아니라 **같은 lineage가 다른 조건을 실제로 겪은 epoch**다.

---

# 1. Lived Epoch ≠ New Population

작가용 용어를 분리한다.

## Lived Lineage
지속되는 의식 인격군의 연속선.

## Lived Epoch
같은 lineage가 다른 조건/제도/재난 아래 살아간 한 시기.

예:

`Lineage A`
- Epoch A0 안정기
- Epoch A1 자원위기
- Epoch A2 테러 이후
- Epoch A3 비상권력 고착

이 네 개는 네 개의 30만 문명을 새로 만든 것이 아니다.

같은 사람들이 계속 살아가며 조건이 변한 것.

이 규칙이 `같은 사람 / 다른 조건` 테마의 기본이다.

---

# 2. Primary Lived Lineage / PLL

정상 상태에서 full-conscious L2는 **하나**다.

PLL은:
- 실험이 끝나면 삭제되는 disposable world가 아님.
- 한 epoch의 검증 목적이 끝나도 주민은 계속 삶.
- CCAL은 perturbation을 멈추거나 다음 조건으로 전환할 뿐.
- 사회는 이전 선택/상실/관계를 그대로 들고 다음 epoch로 감.

즉:
> **테스트 종료 ≠ 세계 종료.**

이 한 문장으로 surviving 300k deletion 문제를 기본적으로 제거한다.

---

# 3. How rollback-like states happen

같은 PLL이 항상 선형으로만 가면 회귀/상충역사 미스터리가 약해진다.

따라서 rollback-like 현상은 세 가지 희귀 경로만 사용한다.

## R1 — L1 Person-State Succession

v0.2의 PSS.
물리 시민사회의 기억/인격상태가 rare recovery로 Anchor에 가까워짐.

## R2 — Secondary Lived Lineage

동일 Anchor에서 딱 하나의 alternate lived lineage를 추가 생성.

## R3 — Memory Residue Across Lineages

PLL/L1/SLL 사이의 autobiographical fragment leakage.

Hard:
`매번 full world를 새로 만들고 지우는 loop`는 없다.

---

# 4. Secondary Lived Lineage / SLL

## 4.1 Purpose

L3로는 답할 수 없고 `동일한 사람들이 다른 선택을 했을 때`의 결과를 정말 비교해야 할 때만 생성.

## 4.2 Hard cap

- Primary: 1
- Secondary: **0~1**
- unresolved full-conscious lineage total: **최대 2**

새 SLL이 이미 존재하면 제3 full lineage 생성 금지.

이 제한은:
- compute,
- storage,
- ethics,
- narrative complexity
모두의 하드 브레이크다.

## 4.3 Active scheduling

기본:
- PLL active.
- SLL이 필요하면 동일 Anchor에서 생성.
- 두 full civilization을 장기간 동시에 최고속도로 돌리지 않는다.

가능 방식:
- time-sliced execution,
- 한 lineage active / 다른 lineage quiescent,
- 짧은 paired overlap.

정확 실행률은 quantitative pass에서 조정.

---

# 5. Quiescence — pause, not delete

SLL 또는 PLL을 계산자원 때문에 잠시 멈춰야 할 수 있다.

Author definition:
**Quiescence = 동기화된 상태에서 의식 진행을 멈추고 재개 가능한 상태를 보존하는 것.**

Hard:
- 살아 있는 lineage를 단순 storage cleanup으로 삭제하지 않는다.
- quiescence 중에는 주관적 시간도 흐르지 않는다.
- 재개하면 바로 다음 순간으로 체감.

중요:
이것이 윤리적 면죄부는 아니다.

시민은 후반에:
- 동의 없는 suspension,
- 자신의 삶을 mission scheduling 대상으로 취급한 것,
- 누가 어느 lineage를 active로 둘 권리가 있었는가
를 문제 삼을 수 있다.

그러나 `시험 끝나면 30만 명 delete`보다는 시스템의 비인격적 악당화를 피한다.

---

# 6. What happens to the alternate lineage?

## Rule

한 번 full-conscious SLL을 만들면 그 lineage는 다음 중 하나만 가능하다.

1. **Resume** — 다시 active.
2. **Remain Quiescent** — 보존.
3. **Become Primary** — 향후 주 active lineage가 됨.
4. **Die through events/substrate loss** — 실제 사망/붕괴.

금지:
- 목적 달성 후 자동 delete.
- 두 lineage를 완전한 한 사람으로 mind-merge.

## No lineage pile-up

SLL이 unresolved 상태면 새 제3 lineage를 만들 수 없다.

따라서 항해 수백 년 동안:
- lived epoch는 많을 수 있지만,
- 독립 full-conscious 인격군은 1~2개만 존재.

이것이 v0.1의 `12~24 full lineage`보다 훨씬 강한 bounded model이다.

---

# 7. Why conflicting histories can still be rich

full lineage가 2개뿐이어도 충분하다.

각 lineage는 여러 epoch를 산다.

예:

```text
PLL-A:
A0 → A1 → A2 → A3 → A4

SLL-B:
       ↘ B1 → B2 → B3
```

Memory residue가 생기면 한 사람은:
- A2의 죽음,
- B2의 생존,
- A3의 결혼,
- B3의 결별
같은 상충 과거를 가질 수 있다.

독자에게는 충분히 `여러 역사`처럼 보인다.
작가에게는 그래프가 관리 가능하다.

---

# 8. Ethical accounting now becomes bounded

CCAL의 윤리문제는 다음으로 좁혀진다.

1. 의식 있는 PLL에 위험조건을 가한 책임.
2. SLL을 동의 없이 생성한 책임.
3. lineage를 동의 없이 quiesce한 책임.
4. L1 PSS로 현재 인격상태를 덮어쓴 책임.
5. branch death가 실제 고통/사망이라는 문제.

하지만:
- 매 시험마다 30만 명을 만들고 죽이는 구조는 아님.
- 수백만 dormant civilization이 숨어 있는 구조도 아님.

이 범위는 Act8에서 다룰 수 있는 크기로 제한된다.

---

# 9. PSS terminal gate repair

PSS는 단순히 `AI가 이 사회 마음에 안 듦`으로 실행할 수 없다.

Terminal Civilization Recovery Gate 후보:

다음 세 축을 본다.

### G1 — Physical viability
- life-support / critical infrastructure가 복구경로 없이 하락.

### G2 — Cognitive/population viability
- 대규모 신경독성/인지손상/continuity corruption 등으로 현재 인구가 기능 회복 불가능.

### G3 — Civic coordination viability
- 폭력/권력붕괴/통신분열이 생존 인프라 복구를 지속적으로 막음.

Hard:
- 선거결과,
- 특정 이념,
- 평화적 정권교체,
- 인기 없는 정책
만으로 G3 충족 불가.

PSS activation candidate:
- 최소 2개 축의 terminal threshold,
- 독립 mission monitor quorum,
- 자동 audit trail,
- 막대한 resource threshold.

정확 수치/알고리즘은 Freeze하지 않는다.

---

# 10. PSS frequency tightened

v0.2의 `0~3회`보다 더 강하게 제한한다.

Working candidate:

- **역사상 prior PSS: 1회**
- **본편 current-story PSS: 0~1회**

즉 총 1~2회급.

효과:
- 물리세계의 신뢰성 보존.
- historical anomaly source 제공.
- 본편에서 사용한다면 진짜 대형 사건으로 취급.

---

# 11. Act mapping implication

현재 9 Act에서 `새 세계`처럼 보이는 변화가 모두 새 lineage일 필요가 없다.

추천:

- Act1~2: L1 physical 또는 PLL epoch — Freeze 전 비교.
- Act3: PSS aftermath 또는 다른 lineage epoch.
- Act4: residue carriers reveal conflicting A/B history.
- Act5: L0/L1 physical evidence begins breaking simple loop theory.
- Act6: one lineage의 civilization-collapse epoch.
- Act7: PLL/SLL + PSS + novel-state 개념이 행동으로 드러남.
- Act8: lineage rights / HUMAN:1 / mission ethics.
- Act9: high-fidelity experimentation 종료 + irreversible L1 future.

중요:
Act 수 = lineage 수가 아니다.

---

# 12. Final Approach disposition

Final Approach에서 남아 있는 SLL이 있다면 새로운 거대 반전으로 만들지 않는다.

Author preference:
- 본편 시작 전에 SLL이 resolved되었거나,
- 본편 중 A/B conflict의 핵심으로 이미 충분히 드러난 뒤,
- Act8에서 시민권/continuity status가 결정됨.

Act9에 `사실 30만 명이 더 숨어 있었다`를 새로 던지지 않는다.

Hard:
마지막 15%는 new ontology보다 payoff/choice 우선.

---

# 13. v0.3 P0 verdict

Remaining P0 `L2 lifecycle`:
**CANDIDATE CLOSED**.

New bounded model:
- L0 physical ship: 1.
- L1 embodied civic baseline: 1.
- PLL full-conscious lineage: 1.
- SLL: 0~1.
- lived epochs: many.
- full-conscious unresolved lineages: max 2.
- normal test end does not delete population.
- quiescence is pause, not deletion.
- new third lineage forbidden while SLL unresolved.
- PSS 1 prior + 0~1 story candidate.

This preserves:
- multiple lived histories,
- same-person pressure,
- conflicting memories,
- finite compute,
- finite ethical blast radius,
- death stakes,
- final irreversible choice.

Current result:

**D+ ONTOLOGY P0 = READY FOR FINAL CRITIC / NOT CANON.**