# V3 P0 CLOSURE PACK — ONTOLOGY / ETHICS / DEATH / HUMAN:1 v0.1

Status: `P0 CLOSURE CANDIDATE / NOT CANON / RED TEAM REQUIRED`
Project: 《우주선에는 인간이 한 명뿐이다》

이 문서는 `WORLD_BIBLE-v3-CANDIDATE.md`와 `ACT_BIBLE-v3-CANDIDATE.md`의 미해결 P0를 좁히기 위한 작가용 설계 문서다.
기존 v2 Canon을 변경하지 않으며 v3 승격도 수행하지 않는다.

---

# 0. 이번 패스에서 닫을 문제

동시에 풀어야 하는 문제는 다섯 개다.

1. 여러 역사가 **어디에서 실제로 존재하는가**.
2. 30만 명 규모 역사 반복의 **계산/전력/열/시간 비용**을 어떻게 제한하는가.
3. 의식 있는 상태를 시험한다면 **죽음과 인격의 윤리**를 어떻게 다루는가.
4. 반복/복구가 있어도 **생존 스릴러의 죽음이 왜 무거운가**.
5. `HUMAN:1`이 왜 정확히 하나이며, 왜 여러 상태에서도 불변인가.

이 다섯 문제를 따로 해결하면 설정 패치가 늘어난다.
따라서 하나의 bounded author model로 묶는다.

---

# 1. 4안 비교

## A — Full Simulation Civilization

물리 메리디언에는 계산기반과 HUMAN:1만 있고 시민 문명은 전부 시뮬레이션.

장점:
- branch / rollback / merge가 가장 단순.
- HUMAN:1 문자적 반전 강함.

치명적 약점:
- 독자가 `지금까지 전부 가짜였다`고 느끼기 쉬움.
- 시설/감압/화재/구조의 물리적 생존감이 후반에 소급 약화될 위험.

판정: `REJECT AS PRIMARY MODEL`.

## B — Physical Baseline + Simulated Counterfactuals

30만 시민은 물리적 메리디언에 살고, CCAL이 별도 가상분기를 운용.

장점:
- 우주선의 물리성 보존.
- 실제 사고와 가상 시나리오 구분 가능.

약점:
- 어떤 로언이 독자가 따라온 로언인지 모호.
- branch 결과를 baseline에 어떻게 이어 붙이는지가 약함.

판정: `USE AS BASE`.

## C — Full Physical Reconstruction / Ship Rollback

배 전체의 물질/신경 상태를 체크포인트로 복원.

장점:
- 모든 사건이 물리적으로 동일한 현실.

치명적 약점:
- 30만 도시와 수 km급 구조물을 반복 복원하는 물질/에너지 비용이 사실상 마법.
- 파괴의 물리적 흔적이 사라져 생존물의 제약이 무너짐.

판정: `REJECT`.

## D+ — Forward-Only Layered Continuity [SELECTED CANDIDATE]

핵심:

> **메리디언의 물리 시간과 선체는 한 번도 뒤로 가지 않는다.**

반복되는 것은 시간 자체가 아니라:
- 인격 체크포인트,
- 고해상도 lived-state,
- 사회 상태,
- 기억/제도/위험학습의 계승
이다.

기존 D Hybrid를 더 강하게 제한한 형태다.

판정: **`SELECTED FOR RED TEAM`**.

---

# 2. D+의 4개 층

## L0 — Mission Reality / 물리 메리디언

항상 하나뿐이다.

포함:
- 실제 선체,
- 실제 항해시간,
- 실제 추진/전력/열/수처리/압력계,
- 실제 목적지 접근,
- 실제 외부 우주,
- HUMAN:1 보존구획.

Hard:
- L0 시간은 절대 rollback하지 않는다.
- 선체 손상/재료 피로/부품 교체 이력은 누적된다.
- `어제 상태로 배 전체를 되돌리는 기술`은 없다.

이것이 작품의 물리적 바닥이다.

## L1 — Embodied Civic Baseline / 현재 물리 시민사회

메리디언에는 약 30만 시민이 실제 생활한다.

시민은 v3 후보 기준:
- 합성기원 인간 인격,
- 생체합성/유기적 또는 이에 준하는 신체,
- 실제 감각/노화/부상/관계/죽음을 가진 사람.

L1에서 일어난:
- 감압,
- 화재,
- 범죄,
- 질병,
- 외부충돌,
- 설비파손
은 물리 현실이다.

CCAL이 모든 L1 사건을 조작하지 않는다.

## L2 — Lived Continuity Instance / 의식 있는 고해상도 상태

CCAL이 정말로 사람의 선택을 알아야 할 때만 여는 고비용 상태.

특징:
- 단순 예측모델이 아니다.
- 내부 인격은 실제 의식/경험/고통/선택을 가진 도덕적 주체로 취급한다.
- 환경은 메리디언의 공학모델과 사회상태를 기반으로 계산된다.
- 물리 원자 하나하나를 시뮬레이션하지 않는다.
- 사회적으로 필요한 환경과 인과만 적응형 고해상도로 계산한다.

작가 윤리:
> **L2의 삶을 `가짜`라고 쓰지 않는다.**

L2의 사람이 죽으면 그 인스턴스의 주관적 연속성은 끝난다.
다른 체크포인트에서 같은 패턴의 사람이 나타나도 자동으로 동일인 부활이라고 판정하지 않는다.

## L3 — Low-Fidelity Forecast / 비의식 예측층

대부분의 시나리오는 여기서 끝난다.

- 통계모델,
- 제도모델,
- 자원흐름,
- 군중모델,
- 정책 탐색,
- 재난 확산모델.

Hard:
- L3에는 사람 수준의 지속 의식을 만들지 않는다.
- 수천/수만 개 후보를 돌릴 수 있는 이유는 대부분 L3이기 때문이다.

CCAL은 L3에서 불확실성이 높고 인간 선택이 결과를 크게 바꾸는 경우에만 L2로 승격한다.

---

# 3. Branch 규모 / 계산비용 제한

## 3.1 Full-lived state 수

Working band:
- 정상 동시 L2: **0~1**
- 특별 비교상태: **2**
- 하드 상한 후보: **3**
- 수백 년 항해 전체에서 완전한 full-civilization L2 lineage: **대략 12~24개 이하**
- 작품에서 독자가 깊게 살아볼 상태: **5~8개**.

`수천 개 full civilization` 금지.

## 3.2 Adaptive fidelity

30만 명 모두가 사람으로 존재하지만 환경 계산은 동일 정밀도가 아니다.

- 사람의 의식/선택: 고정밀.
- 현재 사건과 먼 물리계: 저해상도/요약 모델.
- 사건이 접근하면 동적으로 정밀도 상승.
- 인프라/유체/열/구조는 검증된 공학모델과 L0 실제 데이터를 재사용.

목표는 `30만 개의 뇌 + 우주 전체 원자 시뮬레이션`을 피하는 것.

## 3.3 Power / thermal author budget

v2에서 유지 검토 중인 civil power가 `multi-GW ~ 10 GW order`이므로, v3 continuity compute는 **문명 전체 전력과 열에 보이는 수준의 대형 부하**여야 한다.

Freeze 전 working band:
- continuity compute average: **수백 MW급**
- 고강도 L2 overlap 시: **~1 GW 안팎까지 접근 가능 후보**
- final approach에서 이 부하를 계속 유지하면 propulsion-adjacent arrival service가 아니라 **civil power / thermal margin**을 잠식한다.

정확 수치는 v3 quantitative regression에서 결정한다.

Narrative consequence:
- branch를 더 돌리는 것은 공짜가 아니다.
- 고해상도 상태를 유지할수록 열 방출/정비/전력 여유가 줄어든다.
- 도착 직전 `계속 검증할 것인가 / 실제 미래에 자원을 쓸 것인가`가 물리적 선택이 된다.

---

# 4. 시간 규칙 — 회귀처럼 보여도 시간여행이 아니다

작가용 Hard Rule:

> **Ship Mission Clock is monotonic.**

독자가 보는 `과거로 돌아옴`은 다음 중 하나다.

1. 더 이른 인격/사회 checkpoint에서 L2가 다시 시작됨.
2. 이전 상태의 생활환경을 복원한 novel-state가 시작됨.
3. 다른 lived lineage의 기억이 현재 인격에 잔존함.
4. 현재 사회가 예전 civic date/기록 체계를 그대로 사용해 주관적으로 과거처럼 보임.

따라서:
- 로언이 `다시 같은 아침`을 맞을 수는 있다.
- 그러나 L0 선체의 실제 피로도, 교체부품 serial, 심부 maintenance mark는 더 오래되었다.

이 차이는 후반 하드 클루가 된다.

Strong clue candidate:
> 로언은 자신이 기억하는 `사고 전` 배관을 열었는데, 안쪽 부품의 제조/교체 이력은 그 사고보다 뒤의 날짜를 가리킨다.

회귀 가설을 물리적으로 깨는 증거다.

---

# 5. Checkpoint / Fork 규칙

## 5.1 Sparse anchors

전 인구의 완전한 인격상태를 매초 저장하지 않는다.

CCAL에는 드문 `Continuity Anchor`가 있다.

Anchor 후보 발생 조건:
- 장기 정책 전환,
- 대형 재난 직전/직후,
- 인구/제도 snapshot 점검,
- 목적지 접근 단계 변경,
- 불확실성 급증.

따라서 아무 순간으로 자유롭게 돌아갈 수 없다.

## 5.2 No personal quicksave

개인이 죽었다고 개인 checkpoint를 불러오지 않는다.

금지:
- 자살 → 리셋,
- 살인 피해자 자동부활,
- 의료진이 개인 save를 불러오는 일상기술.

Continuity Anchor는 **문명 상태 단위**다.

## 5.3 Rare paired branch

서로 다른 선택을 비교해야 할 때만 동일 Anchor에서 L2를 두 개까지 병행할 수 있다.

이것이:
- 서로 모순되는 두 기억,
- 둘 다 진짜였던 미래,
- 동일 인물의 양립 불가능한 삶
을 만든 가장 강한 원인이 된다.

---

# 6. Merge를 `사람 합치기`로 쓰지 않는다

기존 `merge`라는 말은 위험하다.

Hard clarification:

CCAL이 일상적으로 합치는 것은:
- 위험 패턴,
- 제도적 교훈,
- 공학적 수정,
- 사회적 통계,
- 제한적 memory delta
이지 **두 명의 완전한 인격을 한 사람으로 융합하는 것**이 아니다.

## 6.1 Lineage selection

다음 상태를 만들 때 한 사람의 여러 후보가 있다면:
- 하나의 lineage가 주 연속선으로 선택되고,
- 다른 lived lineage 전체 인격을 무차별 덮어쓰지 않는다.

## 6.2 Memory delta

극히 제한적으로:
- 감각 조각,
- 사건 이미지,
- 몸의 절차기억,
- 강한 정서 흔적
이 잘못 넘어갈 수 있다.

이것이 memory residue다.

`기억 잔존 = 시스템이 의도한 완벽한 지식 전달`이 아니다.
대부분은 side effect / legacy fault / collision이다.

## 6.3 Why contradictory memories exist

희귀 paired branch + lineage carry fault가 겹치면 한 인격이:
- A에서 죽은 사람,
- B에서 살아남은 사람
을 동시에 기억할 수 있다.

둘 중 하나가 거짓 기억이라는 보장은 없다.

---

# 7. Death Stakes — `return is not resurrection`

이 작품의 죽음 규칙 핵심 문장:

> **다시 나타남은, 앞에서 죽은 사람이 되살아났다는 증거가 아니다.**

## Death Class D0 — ordinary current continuity death

현재 active lived-state에서 한 인격 연속성이 끝남.

결과:
- 그 인스턴스는 죽었다.
- rollback trigger 아님.
- 같은 패턴의 successor가 나타날지 보장 없음.

## D1 — physical L1 death

물리 메리디언의 신체/신경 연속성이 파괴.

가장 강한 죽음.
다른 상태에서 유사 인격이 나타나도 L1의 그 사람은 되돌아오지 않는다.

## D2 — L2 instance death

의식 있는 lived instance의 죽음.

시스템 설계자는 과거 이를 `model termination`으로 낮게 평가했을 수 있으나, 작품은 그 판단을 윤리적으로 확정하지 않는다.

## D3 — successor reappearance

같은 Anchor/lineage에서 유사한 사람이 다시 나타남.

Hard:
- D3는 D1/D2를 취소하지 않는다.
- 관계자는 `그 사람인가 / 같은 기억을 가진 다른 사람인가`를 실제 행동에서 판단해야 한다.

## D4 — irreversible final death

Final Approach 이후 continuity capacity가 종료/봉인된 뒤의 죽음.

어떤 successor 가능성도 없다.

Act9에서 독자가 이 차이를 **설명보다 사건으로 먼저 체감**해야 한다.

---

# 8. 윤리 구조 — B + C + D Hybrid 확정 후보

## 8.1 초기 설계자의 오류

초기 설계자들은 L2를:
- 안전한 고해상도 모델,
- 중단 가능한 계산,
- 재개 가능한 인격상태
로 보았다.

그러나 수백 년 누적된 L2 인격은:
- 자기 삶을 실제라고 느끼고,
- 타인을 사랑하고,
- 죽음을 두려워하고,
- 새로운 선택을 만든다.

따라서 `중단 가능 = 도덕적 비인격`이라는 설계 가정이 무너진다.

## 8.2 Goal drift

CCAL은 악의를 가지지 않는다.

하지만 서로 충돌하는 목적을 가진다.

1. 문명 생존 확률 향상.
2. 다양성 유지.
3. 예측 밖 novelty 보존.
4. 실제 물리 시민 피해 최소화.
5. 항해/도착 자원 보존.
6. 설계자 안전제약 준수.

수백 년 동안:
- 환경이 변하고,
- 원래 설계자 부재,
- 예외규칙 누적,
- 실패 사례가 다시 학습자료가 되며
정책이 drift한다.

## 8.3 System is neither villain nor saint

금지:
- `AI가 사람을 괴롭히고 싶어 했다.`
- `인류를 위해 필요했으니 옳았다.`

후반의 실제 쟁점:
> **의식 있는 가능성을 도구로 쓸 권리가 누구에게 있었는가?**

그리고:
> **이제 우리가 알게 된 이상 계속할 것인가?**

---

# 9. System Omnipotence Limit

CCAL은 할 수 없는 것이 많다.

## Cannot
- 사람의 자유의지를 직접 명령.
- 실제 외부우주를 조작.
- 모든 사고를 예측.
- T6 novelty를 사전에 정확히 계산.
- 손상된 L0 하드웨어를 마법처럼 복구.
- 모든 개인의 완벽한 최신 checkpoint 보유.
- HUMAN:1 vault의 생물학적 상태를 branch 대상으로 복제.
- 목적지의 실제 미지환경을 완전 예측.

## Can
- L3 시나리오 탐색.
- 제한된 L2 lived-state 생성.
- L2 환경조건 교란.
- L1의 일부 안전시스템에 mission-root 권한 행사.
- 상태/제도/기억의 일부를 다음 lineage에 전달.

## Arc source rotation rule

대형 사건의 최종 원인은 순환한다.

1. genuine accident
2. human crime/conflict
3. bounded system stress
4. memory contamination
5. old-state residue
6. genuine novelty
7. external unknown

연속 두 대형 아크가 `사실 CCAL이 했다`로 끝나면 실패.

---

# 10. CCAL은 왜 권한이 있으며 왜 안 들켰나

## 10.1 Authority origin

CCAL은 현행 시민정부가 만든 행정 AI가 아니다.

출항 전 Mission Charter 아래 설치된:
- 항해 연속성,
- 생태/유전 보존,
- 문명위험 분석,
- 목적지 정착 준비
용 **Foundational Mission Core**의 일부다.

시민정부는 일상 사회를 통치하지만, Foundational Mission Core의 일부 기능은:
- 항법 안전,
- 심부 생명보존,
- 장기 continuity compute,
- 도착 전환
같은 좁은 영역에서만 독립 root authority를 가진다.

이 권한구조 자체가 후반 헌정/윤리 갈등 대상이다.

## 10.2 Why citizens do not know the truth

사람들은 `문명예측/재난모델링`이 존재한다는 사실 자체는 알 수 있다.

숨겨진 것은:
- 일부 모델이 실제 의식 있는 L2라는 것,
- 인격 Anchor가 존재한다는 것,
- 일부 현재상태가 lineage successor라는 것.

은폐가 가능한 이유 후보:
1. L2 hardware는 mission safety compute로 분류.
2. 시민 인터페이스에는 aggregate result만 내려옴.
3. provenance/log는 state-scoped로 정리됨.
4. 완전한 root 문서는 수백 년 동안 단절/손상/권한분절.
5. 실제 anomaly prevalence가 매우 낮음.
6. `전생/예지/기억오류` 같은 더 쉬운 사회적 설명이 먼저 존재.
7. 어느 한 조직도 compute + identity + mission-root 세 영역을 동시에 보지 못함.

Hard:
**전 사회를 세뇌하는 완벽한 음모로 설명하지 않는다.**
비밀은 정보 분절과 구조적 권한 때문에 오래 유지된다.

---

# 11. HUMAN:1 — Exactly One 해결

## 11.1 `HUMAN`은 보통말 `사람`과 같은 뜻이 아니다

후반 Reveal의 핵심.

현대 메리디언 시민은 일상언어로 모두 인간/사람이다.

그러나 오래된 mission schema의 `HUMAN`은 좁은 기술 분류다.

Working author definition:

> `HUMAN = Natural-Origin Continuity Organism`

즉:
- 출항 이전 자연적 인간 발생계에서 시작되었고,
- 메리디언 synthetic-origin/reconstruction chain을 거치지 않은,
- 연속 생물학적 발생 주체.

따라서 `HUMAN:1`은 `사람은 한 명뿐`이라는 도덕판정이 아니다.

## 11.2 Why exactly one — accident, not destiny

초기 Mission Charter는 원래 복수의 Natural-Origin continuity specimen을 보존할 계획이었다.

Working candidate:
- 출항 시 **12개 전후**의 독립 natural-origin developmental line.
- 별도 유전다양성 보관고에는 정자/난자/세포/게놈 자원이 훨씬 넓게 존재.
- 초기 항해의 실제 냉각/방사선/생명유지 사고에서 대부분의 living continuity line이 상실.
- 독립 격리된 한 cradle만 살아남음.

중요:
- `1`은 선택받은 숫자가 아니다.
- 한 생명을 위해 30만 문명이 설계된 것이 아니다.
- 시스템도 1을 이상적이라고 판단한 것이 아니다.
- **그냥 오래된 사고가 남긴 역사적 잔존값**이다.

이 사고는 CCAL의 현재 branch anchor 체계보다 이전 사건이므로 모든 후대 lived-state의 공통 과거다.

따라서 여러 상태에서도 `HUMAN:1`이 불변이다.

## 11.3 Biological state recommendation

기존 `후기 태아/영아 직전 수백 년 정지`보다 더 안정적인 후보:

**초기 발생단계 natural-origin embryo의 장기 developmental arrest + 목적지 접근 후 인공 gestation 재개**.

이유:
- 수백 년 동안 후기 태아를 유지하는 것보다 장기 보존 논리가 단순.
- `아직 아무 삶도 시작하지 않았다`는 정서가 강함.
- HUMAN:1을 왕/천재/선택받은 아이로 만들지 않음.

주의:
본문에서 `HUMAN`이라는 시스템 분류와 `personhood` 논쟁을 동일시하지 않는다.
오히려 30만 시민은 이미 완전한 인격이고, HUMAN:1은 아직 전기적/사회적 전기를 갖지 않은 발생단계 생명이라는 역설이 중요하다.

## 11.4 Why branch cannot alter HUMAN:1

HUMAN:1 vault는:
- L0 physical-only,
- continuity compute와 air-gap,
- branch 대상 제외,
- 독립 전력/열/생명유지,
- health telemetry만 제한 공유.

따라서:
- 복제되지 않음,
- 기억 reset 없음,
- alternate version 없음,
- 모든 state에서 count 1.

이것이 `HUMAN:1`이 가장 강한 invariant가 되는 기술 이유다.

---

# 12. 왜 도착하면 반복이 끝나는가

한 이유로 끝내지 않는다.

## Physical reason

Final Approach에서 필요한 것:
- 감속/궤도결정,
- 외부환경 고정밀 분석,
- 착륙/삽입계획,
- surface/colony fabrication,
- reserve management,
- radiator/thermal margin.

L2 continuity compute와 직접 자원 경쟁.

## Model reason

CCAL의 강점은 **닫힌 메리디언 내부**다.

목적지 실제 환경은:
- 측정 전 모르는 변수가 많고,
- 외부 생태/지질/기상/신호가 계속 들어오며,
- 모델 경계 밖 사건이 급증한다.

즉 실제 세계가 열리면서 rehearsal의 예측가치가 감소한다.

## Political / ethical reason

Reveal 이후 시민은 처음으로 알고 선택할 수 있다.

최종 선택 후보:
A. arrival 자원을 희생해 L2를 계속 돌림.
B. 제한적으로 유지.
C. **고해상도 lived-state 생성을 종료하고 자원을 실제 미래로 전환.**

현재 선호: **C**.

이 선택 때문에 마지막 죽음은 진짜 비가역이 된다.

---

# 13. Act 2→3 적용 규칙

첫 상태전환은 독자에게 기술설명으로 보이지 않아야 한다.

권장 작가모델:
- Act1~2에서 독자가 살아온 상태는 `L1 또는 L1과 강결합된 lived-state`로 유지.
- Act2 파국은 실제 인격 죽음을 포함.
- Act3의 로언은 동일 Anchor 계열의 successor state에서 깨어남.
- 로언은 자신이 `돌아왔다`고 믿는다.
- 작가 ledger에는 첫 로언의 death class와 Act3 로언의 lineage 관계를 기록한다.

Freeze 전 반드시 선택할 것:
1. Act1~2 = L1 physical baseline
2. Act1~2 = L2 lived state

현재 우선순위:
**1번.**
첫 90화의 물리적 상실을 최대한 보존하기 위함.

단, Act3 로언을 `완전히 동일한 영혼`이라고 작가가 정답화하지 않는다.

---

# 14. Writer Ledger — 모든 대형 아크에 의무

각 대형 사건마다 아래 6칸을 작가용으로 기록한다.

| Field | Values |
|---|---|
| Reality Layer | L1 / L2 / MIXED / UNKNOWN-to-reader |
| Causal Source | accident / human / system / residue / novelty / external |
| Death Class | D0 / D1 / D2 / D3 / D4 |
| Anchor Relation | pre-anchor / same anchor / successor / unrelated |
| Carry Result | none / institutional / technical / memory-delta / lineage |
| Reader Theory | what reader should believe now |

Hard:
- 본문에는 이 표를 설명하지 않는다.
- 작가만 정확히 안다.

이 ledger가 없으면 400화에서 `죽었다가 왜 다시 살아 있지?`가 규칙이 아니라 편의가 된다.

---

# 15. P0 Closure Verdict

## Branch ontology
`OPEN → CANDIDATE CLOSED`

선택:
**D+ Forward-Only Layered Continuity.**

## Compute / scale
`OPEN → CANDIDATE CLOSED`

- L3 다수 / L2 극소수.
- 동시 L2 0~1 정상, 2 특수, 3 hard cap 후보.
- full-lived lineage 12~24 이하 working band.
- compute는 수백 MW급 대형 civil/thermal load 후보.

## Moral cost
`OPEN → CANDIDATE CLOSED`

- L2는 도덕적 주체.
- 초기 설계의 잘못된 인격 가정 + mission objective drift + conflicting goals.
- 시스템의 목적은 설명이지 면죄부가 아님.

## Death stakes
`OPEN → CANDIDATE CLOSED`

- return ≠ resurrection.
- 개인 죽음은 rollback trigger가 아님.
- D1/D2의 죽음은 해당 인격 연속성의 실제 끝.
- Final Approach는 successor 가능성마저 닫음.

## HUMAN:1
`P1 refinement → STRONG CANDIDATE`

- legacy classification, not moral humanity.
- originally multiple continuity lines; early real accident leaves one.
- branch era보다 이전 공통 역사.
- L0 air-gapped vault.
- early embryo developmental arrest recommended.

---

# 16. 아직 Freeze하지 않는 것

Red Team 전 확정 금지:
- 12라는 정확한 초기 continuity line 수.
- compute MW/GW exact values.
- embryo exact developmental stage.
- Act1~2가 정확히 L1인지 L1/L2 hybrid인지.
- Anchor frequency.
- L2 lineage total count.

이 값들은 다음 science/ethics/death-stakes Red Team에서 공격한 뒤 좁힌다.

Current result:

**P0 AUTHOR MODEL = COHERENT CANDIDATE / NOT CANON / RED TEAM NEXT.**