# Design Change Log — Active

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Historical Archive

CHG-001~026 전체 원문은 Git의 immutable blob에 보존되어 있다.

- archive pointer: `docs/change-log-archive-001-026.md`
- verbatim blob SHA: `c4b95d9d1896431d7b165f53bfadc7a26aa59e71`
- last archived entry: `CHG-026 — DESIGN FREEZE PASSED`

이 파일은 CHG-027부터 현행 기록을 계속한다.

---

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
- Documents Repaired:
- Status:

---

### CHG-027 — Canon precision bundle + CANON FREEZE 통과
- Date: 2026-08-17
- Change Location: World / Character / Act Canon precision
- Previous: Design Freeze는 통과했지만 이름·가족법·공개경로·용어·도착법·복원 경계 등 다수가 PROVISIONAL 상태였고 `CANON FREEZE = NOT PASSED`.
- New: 최종 `WORLD_BIBLE-v1 / CHARACTER_BIBLE-v1 / ACT_BIBLE-v1`을 CANON으로 승격. 핵심 정밀선택은 다음과 같다.
  - Ship = `Meridian / 메리디언`
  - Habitats = `1환 / 2환 / 3환`
  - Destination = `Epsilon Indi A / 인디계`
  - P = `Maren Vale / 마렌 베일`, 41F, ordinary Seeded-Origin
  - S = `Ella Vale / 엘라 베일`, 39F, planned sole legal parent of Noah
  - N = `Noah Vale / 노아 베일`, 12M
  - C8 = `Amara Okoro / 아마라 오코로`, 45F
  - family chronology = Ella sole legal parent + Maren emergency guardian + roughly 3y staged Reconstruction/rehab
  - PR-H1 = nonbinding but serious reconstruction-preference draft that Maren knew and withheld from ethics review
  - GA-H1 = gamete/germline/stem-cell genetic-diversity archive, not sleeping `real humans`
  - ALX-H1 = legacy Human Settler field affects destination-jurisdiction translation, not current ship citizenship
  - DP-H1 = anchorless adult-person reconstruction practically impossible
  - COI-H1 = Maren mandatory recusal from formal family adjudication
  - CP-H1 = Count=1 publication passes independent privacy/public-interest review
  - SV-H1 = Seed success verified during prenatal critical window via closed-loop telemetry; adult direct origin scanner does not exist
- Reason: Design-Frozen 구조를 실제 집필 가능한 단일 정본으로 만들고, 최종 Canon Red Team에서 발견된 법적/개인정보/검증 P0를 닫기 위해.
- Trigger / Evidence: `CANON-CONFLICT-CHECK-v0.2.md`, `CANON-FREEZE-RED-TEAM-v1.md`, precision 4-design documents.
- Characters Affected: Maren/Ella/Noah/Raul/Tomas/Ines/Jun/Amara/Leo/Kai/Mina 및 전 시민.
- Acts Affected: 전체, 특히 Act 2~5 Reveal/PR-H1/arrival law.
- Foreshadowing Affected: Seed completion records, C8 re-identification, PR-H1, legal stack, genetic archive.
- World Rules Affected: origin, reproduction, Reconstruction, privacy, family jurisdiction, arrival law, naming.
- Documents Repaired: `canon/WORLD_BIBLE-v1.md`, `canon/CHARACTER_BIBLE-v1.md`, `canon/ACT_BIBLE-v1.md`, `canon/CANON_STATUS.md`.
- Status: `CANON FREEZE = PASSED — 2026-08-17`

---

### CHG-028 — Writing Ready Gate를 WR-H1 Two-Pass Full Blueprint로 확정
- Date: 2026-08-17
- Change Location: Prewriting / episode architecture workflow
- Previous: Canon Freeze 이후 어느 깊이까지 화별 설계를 마쳐야 원고를 허용할지 미정.
- New: `WR-H1 Two-Pass Full Blueprint + Risk-Weighted Deepening + Harness` 채택.
  - Pass 1: EP001~230 전 화 causal Episode Card
  - Pass 2: opening/23 Sub-Act turns/Count/Meaning/Amara/PR-H1/Final Approach/Human Settler/time bridges/ending Deep Card
  - Harness M1~M8: Time/Age, Cast Causality, Location, Information, Foreshadow, Reward/Hook, Canon Dependency, Anti-Drift
  - Hostile QA + Final Writing Ready Red Team 필수
- Reason: 230화 장편에서 쓰면서 뒤 구조를 발명하는 방식 대신, 복선·시간·인과·캐릭터 자율성·결말을 원고 전에 회귀검증하기 위해.
- Trigger / Evidence: `WRITING-READY-GATE-4-DESIGNS-v0.1.md`.
- Characters Affected: 전체.
- Acts Affected: 전체.
- Foreshadowing Affected: 전체 ledger.
- World Rules Affected: 없음; workflow only.
- Documents Repaired: `docs/writing-ready/WRITING-READY-CHECKLIST-v1.md` 및 Blueprint/Harness 문서군.
- Status: `WR-H1 = ACTIVE WRITING READY GATE`

---

### CHG-029 — Full Episode Matrix / Pass-2 time precision repair
- Date: 2026-08-17
- Change Location: Full Episode Blueprint / T-H1 exact execution clock
- Previous: Canon의 Act별 시간범위는 elastic이었고, Act6 v0.1 작성 중 `T-8 → T-1` 표기가 발생하여 전체 약 14년 시간축과 충돌. 일부 EP155/159 Noah age shorthand도 M1과 어긋남.
- New:
  - EP001~230 Full Episode Matrix 완료.
  - Act6 active version을 `EPISODE-BLUEPRINT-ACT6-v0.2.md`로 교체.
  - Act6 = roughly `T-8 → T-3 (~5y)`.
  - Act7 = `T-3 → insertion → roughly +1y epilogue-phase`.
  - M1 Time/Age Matrix를 exact execution clock authority로 지정.
  - Noah EP155/159 나이표현은 M1 기준으로 수정 해석.
  - 구조적 episode 변경은 없음.
- Reason: 14년 종단시간과 Character Bible의 +14년 나이표를 정확히 일치시키기 위해.
- Trigger / Evidence: `HARNESS-M1-TIME-AGE-v0.1.md`, `DEEP-CARD-TIME-BRIDGES-v0.1.md`, `EPISODE-BLUEPRINT-PASS2-NORMALIZATION-v0.1.md`.
- Characters Affected: Noah 포함 전체 장기 캐스트의 age tracking.
- Acts Affected: Act 5~7 중심, 전체 clock.
- Foreshadowing Affected: arrival countdown / career and family maturity timing.
- World Rules Affected: 없음; Canon의 elastic calendar를 precision lock.
- Documents Repaired: Act6 v0.2, M1, Pass2 Normalization.
- Status: `PRECISION REPAIR PASS / NO CANON REOPEN`

---

### CHG-030 — WRITING READY 통과
- Date: 2026-08-17
- Change Location: Project Workflow Gate
- Previous: `WRITING READY = BLOCKED`; manuscript forbidden.
- New:
  - EP001~230 Full Episode Matrix = COMPLETE
  - all named high-risk Deep Cards = COMPLETE
  - all 23 Sub-Act turn Deep Cards = COMPLETE
  - Harness M1~M8 = PASS
  - Hostile QA = PASS WITH P1 EXECUTION GUARDRAILS
  - Final Writing Ready Red Team blocking P0 = 0
  - silent Canon dependency blocker = 0
  - structural missing-design blocker = 0
  - therefore `WRITING READY = PASSED`
  - `MANUSCRIPT = ALLOWED UNDER PROSE EXECUTION PROTOCOL`
- Reason: 사용자 정의 Gate 조건을 전부 만족했고, 집필 중 주요 세계/캐릭터/Act/복선 구조를 새로 발명할 필요가 없음을 확인했기 때문.
- Trigger / Evidence: `docs/qa/FINAL-WRITING-READY-RED-TEAM-v1.md`.
- Characters Affected: 전체.
- Acts Affected: 전체.
- Foreshadowing Affected: 전체 closure verified.
- World Rules Affected: workflow only.
- Documents Repaired: `CLAUDE.md`, `canon/CANON_STATUS.md`, `docs/current-work-status.md`, `docs/writing-ready/WRITING-READY-CHECKLIST-v1.md`, `docs/NEXT-CHAT-HANDOFF.md`.
- Status: `WRITING READY = PASSED — 2026-08-17`

---

### CHG-031 — Prose Execution Protocol + Act 1 POV Map 잠금
- Date: 2026-08-17
- Change Location: Manuscript execution architecture / POV
- Previous: Writing Ready는 통과했지만 실제 본문에서 사용할 POV/person, narrative distance, exposition/jargon, hook, dialogue, anti-AI QA와 Act 1 화별 POV가 미확정.
- New:
  - 4개 실행안 비교 후 `PEP-H1R — Causal-Owner Single-POV Close Third + Maren Series Anchor + Act-Ahead POV Mapping`을 잠금.
  - 기본은 한 화 한 POV의 근접 3인칭 제한시점, mid-episode head hopping 금지.
  - Primary Actor가 자동 POV는 아니며 irreversible choice / immediate cost / information fairness를 우선한다.
  - 마렌은 시리즈 최대 단일 POV 소유자이나 고정 쿼터는 두지 않는다.
  - Act 1 EP001~028 POV Map 확정: Maren 13 / Ella 5 / Noah 4 / Jun 3 / Raul 2 / Ines 1.
  - 초기안은 EP001~009에 6개 POV가 등장하는 P1이 있어 EP005를 Ines→Maren, EP013을 Maren→Ines로 교환. 총분포는 유지하면서 첫 9화 POV owner를 5명으로 줄이고, Seed completion record를 의료전문가의 평범한 시선으로 처리하도록 개선.
  - Act 1 POV mini QA 결과 blocking P0 = 0.
- Reason: 마렌의 주인공 중력과 비마렌 캐릭터의 독립 인과성을 동시에 살리고, Reveal 정보공정성 및 same-writer/AI-like dialogue 위험을 줄이기 위해.
- Trigger / Evidence: `PROSE-EXECUTION-PROTOCOL-4-DESIGNS-v0.1.md`, `PROSE-EXECUTION-PROTOCOL-RED-TEAM-v1.md`, `ACT1-EXECUTION-POV-MAP-v1.md`, `ACT1-POV-MAP-MINI-QA-v1.md`.
- Characters Affected: Maren/Ella/Noah/Raul/Ines/Jun/Amara 및 이후 모든 POV 후보.
- Acts Affected: 전체 execution protocol; Act 1 exact POV map.
- Foreshadowing Affected: 정보공개/관찰자 선택, 특히 Seed/old-origin/C8 pre-Reveal fairness.
- World Rules Affected: 없음; execution-only. Canon truth unchanged.
- Documents Repaired: `CLAUDE.md`, `canon/CANON_STATUS.md`, `docs/current-work-status.md`, `docs/writing-ready/WRITING-READY-CHECKLIST-v1.md`, Prose Protocol/Act1 POV/QA 문서, `docs/NEXT-CHAT-HANDOFF.md`.
- Status: `PROSE EXECUTION PROTOCOL = LOCKED / ACT 1 POV MAP = PASS / EP001 READY ON EXPLICIT REQUEST`

---

### CHG-032 — Full-series POV architecture + Protocol v1.1 보정
- Date: 2026-08-17
- Change Location: Manuscript execution architecture / all Acts POV
- Previous: Protocol v1은 `Maren ~45~60%`를 soft diagnostic으로 두었고 Act1만 exact POV Map이 잠겨 있었음.
- New:
  - Act2~Act7까지 EP029~230 exact Execution POV Map 작성 + 각 Act mini QA 통과.
  - EP001~230 전체가 한 화 한 POV로 배정됨.
  - 전체 POV 합계는 Maren 45 / Ella 27 / Amara 25 / Noah 17 / Raul 17 / 기타 분산.
  - Maren은 Acts 1/2/5/6/7의 plurality POV owner. Act3는 Amara, Act4는 Ella가 구조적 이유로 Act-level owner.
  - full-series regression 4안 비교 결과, 45%를 맞추려면 최소 59화 이상을 Maren POV로 재배정해야 하며 이는 non-Maren causality / Information Ladder / C8 및 PR-H1 agency를 크게 훼손한다고 판정.
  - `POV-H1R Maren-Led Plurality Anchor` 채택: Maren은 majority POV가 아니라 **primary series anchor inside a true ensemble**.
  - Protocol v1의 45~60% diagnostic을 폐기하고 `PROSE-EXECUTION-PROTOCOL-v1.1.md`로 보정.
  - v1.1 hard anchor: Maren = full-series largest single POV owner, majority of Acts plurality, EP001/EP229/EP230 및 핵심 checkpoint ownership, percentage-driven POV theft 금지.
  - `ALL-ACTS-POV-LOCK-QA-v1.md` 결과 blocking P0 = 0.
- Reason: 화별 인과 주체를 끝까지 실제 배정한 뒤 드러난 실행구조가 초기 추정치와 충돌했기 때문. 수치를 맞추기 위해 인물자율성을 훼손하는 것보다 full-series data에 맞춰 execution diagnostic을 수정하는 편이 작품 구조와 주제/정보공정성을 모두 보존함.
- Trigger / Evidence: `ACT2~ACT7-EXECUTION-POV-MAP-v1.md`, 각 Act mini QA, `FULL-SERIES-POV-REGRESSION-4-DESIGNS-v1.md`, `ALL-ACTS-POV-LOCK-QA-v1.md`.
- Characters Affected: 모든 recurring POV character 및 functional specialist POV.
- Acts Affected: 전체 EP001~230.
- Foreshadowing Affected: Count/Meaning/Amara/PR-H1/arrival-law information observer selection; facts/timing 자체는 변경 없음.
- World Rules Affected: 없음. Canon truth unchanged.
- Documents Repaired: `PROSE-EXECUTION-PROTOCOL-v1.1.md`, `CLAUDE.md`, `canon/CANON_STATUS.md`, `docs/current-work-status.md`, `docs/NEXT-CHAT-HANDOFF.md`, POV Map/QA 문서군.
- Status: `ALL-ACTS POV ARCHITECTURE = LOCKED / PROTOCOL v1.1 ACTIVE / NO CANON REOPEN`

---

# Current Change-Control Rule

Story/Canon은 Frozen이다.
본문 실행 중 아래를 바꾸려면 새 CHG 항목 + Canon-impact review가 필요하다.

- world physics / Seed / Reconstruction / reproduction
- core character origin/family/core flaw
- Reveal facts/order/major timing
- Act order / Ending architecture
- arrival-law authority range
- Amara authority or identity meaning

Execution POV/wording/minor names can change within Protocol v1.1 only if local causality + information-fairness QA passes.
Changing full-series Maren anchor architecture requires full POV regression.

새 blocking P0가 발견되면 관련 Freeze를 재개방한다.
