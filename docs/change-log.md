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

# Current Change-Control Rule

이제 Story/Canon은 Frozen이다.
본문 실행 중 아래를 바꾸려면 새 CHG 항목 + Canon-impact review가 필요하다.

- world physics / Seed / Reconstruction / reproduction
- core character origin/family/core flaw
- Reveal facts/order/major timing
- Act order / Ending architecture
- arrival-law authority range
- Amara authority or identity meaning

새 blocking P0가 발견되면 관련 Freeze를 재개방한다.
