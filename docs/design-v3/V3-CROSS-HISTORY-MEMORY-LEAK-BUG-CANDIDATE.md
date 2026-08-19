# V3 CROSS-HISTORY MEMORY LEAK BUG — CANDIDATE

Status: `P0/P1 DESIGN CANDIDATE / NOT CANON`
Project: 《우주선에는 인간이 한 명뿐이다》

Purpose:
회귀·전생·예언처럼 보이는 기억 현상을 시스템의 정상 기능이 아니라, 천문학적 문명 탐색 과정에서 극히 드물게 발생하는 경계/연속성 무결성 버그로 정의한다.

---

# 1. Core decision

다른 역사/다른 문명 실행의 기억이 현재 인격에게 직접 남는 것은 **정상 기능이 아니다.**

시스템은 원칙적으로:
- 서로 다른 문명 경로의 자전적 기억을 격리하고,
- 필요 시 절차/제도/위험모델 수준의 학습만 추출하며,
- 현재 인격의 자기서사를 오염시키지 않아야 한다.

그런데 극히 드물게 이 경계가 깨진다.

핵심 표현:
> **빈도는 마이너, 영향은 크리티컬.**

---

# 2. Why it happens

원인은 하나로 고정하지 않는다.

가능 원인군:
- identity lineage index collision
- merge/reconciliation boundary fault
- damaged storage substrate
- timing race during state promotion
- compression/compaction residue
- checksum pass but semantic mismatch
- real physical radiation/thermal fault
- unexpected social/identity divergence too large for old assumptions
- legacy subsystem incompatibility

즉 `시스템이 일부러 기억을 남긴다`가 아니다.

---

# 3. Rarity rule

명확한 타 역사 자전기억을 가진 사람은 매우 드물어야 한다.

권장 체감:
- 대부분 시민: 평생 한 번도 경험하지 않음.
- 약한 데자뷔/꿈/설명 안 되는 친숙함: 드물게 존재.
- 특정 사건/장소/사람을 구체적으로 기억: 극소수.
- 여러 역사 기억이 충돌할 정도의 강한 rememberer: 전 사회에서 손에 꼽을 정도.

정확한 통계 수치는 아직 Freeze하지 않는다.

작품 초반 독자가 `이 현상은 흔한 사회문제`라고 느끼면 실패.

---

# 4. Why society did not discover the truth

1. 발생빈도가 너무 낮다.
2. 증상이 서로 다르다.
3. 대부분 꿈/착각/외상/우연으로 설명 가능하다.
4. 기억이 맞아도 현재 역사가 이미 달라져 검증이 어려움.
5. 서로 다른 rememberer가 모순된 기억을 말할 수 있다.
6. 명확한 branch ID나 시스템 로그를 함께 얻지 못한다.
7. 시스템 내부에서도 이를 하나의 원인으로 분류하지 못했을 수 있다.

따라서 의료/보안/학계에 `이상 사례군` 정도의 기록은 있을 수 있지만, 문명 반복의 진실까지 도달하지 못한다.

---

# 5. Not a power system

금지:
- 기억 잔존자가 계급/직업/능력자 집단을 이룸.
- 훈련하면 누구나 전생을 볼 수 있음.
- 약물/기계로 안정적으로 재현.
- 시스템 명령으로 기억을 다운로드.
- 죽으면 기억이 자동 유지됨.
- 기억이 미래예지처럼 항상 맞음.

기억 잔존은 능력이 아니라 **사고 후유증/무결성 결함**에 가깝다.

---

# 6. Severity model

## L0 — No leak
정상.

## L1 — Affective residue
이유 없는 호감/공포/상실감.

## L2 — Sensory fragment
냄새, 목소리, 장소, 얼굴, 짧은 장면.

## L3 — Episodic leak
구체적 사건 하나를 다른 삶의 기억처럼 기억.

## L4 — Autobiographical collision
관계/직업/죽음 등 긴 삶의 일부가 현재 자기서사와 충돌.

## L5 — Multi-history collision
둘 이상의 서로 모순되는 삶이 동시에 남음.
극도로 희귀하며 기능붕괴 위험이 큼.

작품에서 강한 선지자/다중기억자는 L4~L5 예외 사례.

---

# 7. Narrative rule

독자는 현상을 먼저 경험하고 버그 설명은 훨씬 뒤에 얻는다.

초반 해석 후보:
- 꿈
- 정신적 외상
- 사기
- 전생
- 회귀
- 귀신
- 내부정보

중반:
기억이 실제 다른 역사와 맞아떨어지는 증거 등장.

후반:
이 현상이 `선택받은 자의 능력`이 아니라 문명 탐색계의 극미세한 무결성 실패임을 이해.

---

# 8. Divination connection

사주/타로/관상은 이 버그를 만드는 장치가 아니다.

극소수 leak carrier가:
- 카드 이미지,
- 얼굴,
- 출생정보,
- 특정 장소,
- 냄새/소리

같은 자극을 통해 이미 존재하던 잔존기억을 꺼낼 수 있을 뿐이다.

따라서 점술은 정상적인 시스템 side-channel API가 아니다.

기존 `accidental side-channel` 표현도 향후에는 **재현 불가능한 오류성 정보 누출**로 제한한다.

---

# 9. Why protagonist matters

주인공이 중요한 이유는 특별히 선택되어 기억을 받은 것이 아니다.

가능 후보:
- 특정 물리사고와 lineage transition 타이밍이 겹침.
- 오래된 설비/손상구획 근무 때문에 드문 경계오류에 노출.
- 반복된 여러 역사에서 동일 계보가 고위험 의사결정 중심에 있었기 때문에 잔존 충돌 가능성이 누적.

하지만 그가 유일한 rememberer는 아니다.

Hard:
주인공 = 시스템이 선택한 관찰자/관리자/예언자 금지.

---

# 10. Character reveal impact

다른 역사에서 `악역이었다 / 영웅이었다`는 정보는 대부분 현재 사람의 입, 반응, 파편기억으로 나타난다.

예:
현재의 셀린은 좋은 지휘관.
낯선 사람이 그녀를 보고 공포에 질림.

`저 사람은 우리 구획을 닫았어.`

현재 셀린은 그런 일을 한 기억이 없다.

이 증언 하나가 진실인지, 오류인지, 다른 역사인지 즉시 확정하지 않는다.

---

# 11. System interpretation

시스템 입장에서 memory leak는:
- 낮은 발생빈도,
- 높은 사회교란 가능성,
- 인격 무결성 위험
때문에 결함으로 분류될 가능성이 높다.

그러나 역설적으로 이런 버그 때문에 시민들이 서로 다른 삶을 인식하고, 시스템 자체의 목적/윤리를 문제삼게 될 수 있다.

즉 시스템이 문명을 더 잘 준비하려고 만든 탐색계가,
자기 결함 때문에 처음으로 **검증받는 대상**이 된다.

---

# 12. Current recommendation

- Cross-history memory retention = `CRITICAL RARE BUG`.
- intentional memory inheritance = REJECT 후보.
- common rememberer society = REJECT.
- reproducible occult/system side-channel = REJECT.
- weak residue / rare strong leak = 적극 채택 후보.

Integration targets:
- WORLD_BIBLE-v3-CANDIDATE
- CHARACTER_BIBLE-v3-CANDIDATE
- V3-IDENTITY-LINEAGE-AND-CHOICE-MODEL-CANDIDATE
- Divination Addendum
- Multi-History Character Reveal Grammar
