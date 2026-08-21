# Design Change Log — Active

설정 변경은 삭제가 아니라 이유와 영향까지 기록한다.

## Historical Archives

### CHG-001~026
- archive pointer: `docs/change-log-archive-001-026.md`

### CHG-027~032
- previous history preserved in Git history
- prior immutable blob reference: `586c6fd1a6d03009a297a13a78df61cfb47efd7b`

### CHG-033~042
- archive pointer: `docs/change-log-archive-033-042.md`
- covers Encyclopedic gate opening, Packages A~G/C-M structural passes, Character Encyclopedia and full EP001~230 Context Registry.

---

## CHG-043 — Package H Reference Atlas + Package I Final Completeness Harness 완성
- Date: 2026-08-18
- Change Location:
  - `docs/reference-atlas/`
  - `docs/qa/FINAL-COMPLETENESS-*`
  - `docs/qa/RANDOM-SCENE-FUZZ-20-v0.1.md`
  - `docs/qa/FINAL-CANON-STORY-REGRESSION-v0.1.md`
- Previous:
  - Packages A~G had structural/design passes, but there was no final current/superseded authority atlas and no arbitrary-scene completeness proof.
- New:
  - `REF-H1` Reference Atlas built with 13/13 required views.
  - Atlas separates human-readable navigation from current authority and prevents Shadow Canon.
  - actual stale Package-F support-name defect discovered and repaired.
  - `FC-H1` Final Completeness Harness created.
  - deterministic citizen/lifecycle/crime/emergency/class/family/school/media/culture/AI/arrival/material suites PASS.
  - **20/20 arbitrary random-scene fuzz tests PASS** without a new major civilization rule.
  - full Canon/story/Reveal/POV regression PASS.
- Blocking P0: **0**.
- Status:
  `PACKAGE H = PASS / PACKAGE I = PASS / FINAL P1 LEDGER EXPOSED`.

---

## CHG-044 — Final MUST-CLOSE P1 closure
- Date: 2026-08-18
- Change Location:
  - `docs/design-v2/P1-Q-SHIP-QUANTITATIVE-CLOSURE-v0.2.md`
  - `docs/design-v2/P1-Q-DEST-SCIENCE-LOGISTICS-CLOSURE-v0.2.md`
  - `docs/design-v2/P1-LEGAL-OPERATIONAL-POLICY-GRAMMAR-CLOSURE-v0.1.md`
  - `docs/design-v2/P1-CULTURE-HISTORY-SPORT-SUPPORT-CLOSURE-v0.2.md`
  - corresponding hostile QA files.
- Previous:
  - core architecture existed, but final reference-grade ranges/policy grammars/examples remained open.
- New — Q-SHIP:
  - Habitat radius 0.9–1.1 km, 5–7 km length order, ~0.9–1.0g, ~0.9–1.0 rpm.
  - explicit internally compartmented pressure architecture; no giant undivided air cylinder.
  - pressure/refuge/transfer/water/power/thermal/workforce/spare working bands selected.
- New — Q-DEST:
  - Epsilon Indi A retained as real star anchor; rocky settlement world remains future fictional mission-era discovery.
  - ~0.50–0.54 AU / ~150–165d / ~0.93–1.02g / ~28–31h.
  - near-Earth pressure with oxygen far below safe breathing; outdoor breathing support mandatory but normal pressure EVA unnecessary.
  - high planetocentric Meridian staging orbit, resource transfer/cargo/power/Year-1 population bands selected.
- New — legal/operational:
  - `AGE-H1` 18-year civil majority + staged youth autonomy.
  - `DATA-H1` purpose-class retention + protected provenance + versioned correction.
  - `FORCE-H1` closed-habitat T0~T4 dangerous-tool/force tiers.
  - `STRIKE-H1` strike right + minimum life-safety service + rapid neutral review.
  - `ARRLAW-H1` shared civic baseline + location/service nexus + staged local competence.
  - `BIO-H1` quarantine/contained living systems + outdoor release moratorium during ending window.
- New — culture/history/support:
  - small recurring observance/food/idiom/art set.
  - six representative historical anchors.
  - `REBOUND-H1` repeatable low/zero-g sport model.
  - 14 stable-if-used C1 support anchors; Sorin Das/Yuna Bekele remain C2 reserve.
  - civic-equality holiday/history wording repaired so it does not leak EP059~066 Meaning.
- Blocking P1 remaining: **0**.
- Status:
  `P1 CLOSURE = PASS / READY FOR CANON v2 CONSOLIDATION`.

---

## CHG-045 — Encyclopedic Canon Freeze v2 / World+Character 정본 승격 / 원고 게이트 해제
- Date: 2026-08-18
- Change Location:
  - `canon/WORLD_BIBLE-v2.md`
  - `canon/CHARACTER_BIBLE-v2.md`
  - `docs/qa/ENCYCLOPEDIC-CANON-v2-FINAL-RED-TEAM.md`
  - `canon/CANON_STATUS.md`
  - `docs/current-work-status.md`
  - `docs/manuscript/MANUSCRIPT-STATUS.md`
  - `CLAUDE.md`
  - `docs/NEXT-CHAT-HANDOFF.md`
  - `docs/reference-atlas/*` authority/status navigation.
- Previous:
  - World/Character v1 remained formal Canon while A~I/P1 v2 material was candidate/supporting design.
  - manuscript was blocked by the stronger encyclopedic completeness gate.
- New:
  - final hostile regression checked World/Character v2 against v1 Canon, Act Bible, all active Blueprints, Act6 v0.2, M1, POV maps, Package G Registry and final Harness.
  - blocking P0 = **0**.
  - blocking P1 = **0**.
  - Reveal moved = NO.
  - POV architecture changed = NO.
  - core character arcs changed = NO.
  - ending architecture changed = NO.
  - Shadow Canon unresolved = NO.
  - **`ENCYCLOPEDIC CANON FREEZE v2 = PASSED`**.
  - `canon/WORLD_BIBLE-v2.md` promoted to **CANON**.
  - `canon/CHARACTER_BIBLE-v2.md` promoted to **CANON**.
  - `canon/WORLD_BIBLE-v1.md` / `CHARACTER_BIBLE-v1.md` become historical/superseded reference.
  - `canon/ACT_BIBLE-v1.md` remains ACTIVE because macro narrative did not change.
  - manuscript state changes from `BLOCKED` to **`READY / NOT STARTED`**.
  - Accepted manuscript remains **0 / 230**; first eligible episode = EP001.
- Milestone:
  `docs/status/ENCYCLOPEDIC-CANON-FREEZE-v2-PASS-2026-08-18.md`
- Status:
  **`DESIGN/WORLD/SETTING-BIBLE COMPLETE / CANON v2 FROZEN / MANUSCRIPT READY`**.

---

## CHG-046 — EP001~230 개별 Context Manifest 완성 / 추가 맹점 점검 / Amendment A 승격
- Date: 2026-08-18
- Change Location:
  - `docs/narrative-engineering/episodes/EP-029.md` ... `EP-230.md`
  - `docs/change-control/CANON-v2-AMENDMENT-A-CHANGE-RECORD.md`
  - `docs/change-control/CANON-v2-AMENDMENT-A-CANDIDATE.md`
  - `docs/qa/CANON-v2-AMENDMENT-A-RED-TEAM.md`
  - `canon/CANON-v2-AMENDMENT-A-GOVERNANCE-ETHICS.md`
  - `canon/v2/*` retraction notices
  - global authority/status/handoff files.
- Previous:
  - Package G design Registry covered 230/230, but the old status/handoff still described EP029~230 individual split as a later implementation task.
  - Official monolithic Canon v2 had already passed Freeze, but a further rare-scene fuzz pass found that ordinary election/executive/court mechanics plus salvage/research/MAID should not be invented ad hoc in prose.
- New — Context Manifests:
  - EP029~230 individual Markdown Context Manifest files materialized on main.
  - key regression samples EP029 / EP058 / EP112 / EP145 / EP216 / EP230 read back successfully.
  - Count, PR-H1, Final Approach, insertion and ending knowledge fences preserved.
- New — additional blind-spot audit:
  - Q8 governance design selected `Mixed-Member Civic Assembly + Assembly-Selected Collective Executive + Independent Multi-Level Courts`.
  - Q9 closed found-property/salvage, human-subject research ethics and narrow competent-adult MAID rules.
- Shadow Canon incident:
  - an experimental modular authority set was created under `canon/v2/` during the additional audit.
  - later comparison discovered that official `canon/WORLD_BIBLE-v2.md` / `CHARACTER_BIBLE-v2.md` were already newer and contained later P1 quantitative closures and support-name overrides.
  - experimental modular set contained older candidates/names and was therefore **RETRACTED / NON-CANON**, retained only as design history.
  - this prevents stale transfer/pressure/water/arrival bands and superseded support names from overriding the official Canon.
- Official support names preserved from `CHARACTER_BIBLE-v2.md`, including:
  - Eli Rhee
  - Dalia Diniz
  - Nadia Idris
  - Abeni Okoro
  - Hana Wu.
- Amendment A formal Change Control:
  - baseline remains official World v2 + Character v2 + Act Bible v1.
  - governance additions: franchise 18+, 4-year election, mixed-member two-vote 선내의회, ~120–180 seats bounded, collective 5–7-member Assembly-selected executive, constructive no-confidence, local councils, multi-level judiciary, 시민항소원 role clarification, emergency-election guardrail.
  - salvage: finding ≠ ownership; strategic/common/controlled property remains regulated.
  - research: consent + ethics review + data minimization; **Amara has no research duty**.
  - MAID: contemporaneously competent adult only under independent safeguards; no proxy active authorization for incapable person.
- Amendment A Red Team:
  - blocking P0 = **0**
  - unresolved P1 = **0**
  - Blueprint changes = **0**
  - POV changes = **0**
  - Reveal changes = **0**
  - Character C0 changes = **0**
  - official ship/destination quantitative changes = **0**.
- Status:
  **`OFFICIAL CANON v2 PRESERVED + AMENDMENT A FROZEN / EXPERIMENTAL MODULAR SHADOW CANON RETRACTED / EP001~230 CONTEXT FILES COMPLETE`**.

---

## CHG-047 — 공식 World/Character Bible v2 본문 복원 (스텁 잔존 결함 수리)
- Date: 2026-08-18
- Change Location:
  - `canon/WORLD_BIBLE-v2.md`
  - `canon/CHARACTER_BIBLE-v2.md`
- Previous:
  - CHG-046에서 `canon/v2/` 실험 모듈이 RETRACTED 처리되고 상태/라우팅/handoff 문서는 공식 모놀리식 v2 권위로 복원되었으나,
  - 정작 `canon/WORLD_BIBLE-v2.md` / `canon/CHARACTER_BIBLE-v2.md` 파일 본문은 실험 기간에 만들어진 32줄짜리 `SUPERSEDED POINTER → canon/v2/` 스텁 상태로 main에 잔존.
  - 결과적으로 "선언된 정본 파일이 철회된 폴더를 가리키는" 라우팅 모순(P0) 발생.
- New:
  - 두 파일 본문을 Freeze 당시 보존 blob에서 기계적으로 복원:
    - World: blob `6267807167cf162f920b9073315ebf6a451d0a53` (승격 커밋 `2adf6e0` 시점 파일과 동일함을 검증)
    - Character: blob `dd4a061d31fca03b883fc01ea80d5f9b4fdb782e`
  - 복원본 검증:
    - Status 헤더 = `CANON — ENCYCLOPEDIC CANON FREEZE v2 PASSED — 2026-08-18`
    - 최신 C1 지지 인물명 오버라이드(Eli Rhee / Dalia Diniz / Nadia Idris / Abeni Okoro / Hana Wu) 포함, 구명은 superseded 표기로만 존재
    - Epsilon Indi A / Amara / Meridian 핵심 사실 존재
    - `canon/v2/` 참조 없음.
- 설계 변경: **0** (내용 변경 없는 기계적 복원. Blueprint/POV/Reveal/quant 영향 없음.)
- Status:
  **`OFFICIAL MONOLITHIC CANON v2 FILES PHYSICALLY RESTORED / ROUTING CONTRADICTION CLOSED / P0=0`**.

---

## CHG-048 — PROSE STYLE CALIBRATION C1 + EP001~003 개정
- Date: 2026-08-18
- Change Location:
  - `docs/manuscript/PROSE-STYLE-RUBRIC-v1.md` §20 CALIBRATION C1 신설
  - `docs/manuscript/STYLE-REFERENCES-v1.md` 신설 (참고 작가/작품 10선)
  - `manuscript/accepted/act01/EP001~003.md`
- Previous:
  - 초판 EP001~003이 QA PASS했으나 첫 독자(작가) 피드백 "재미없다".
  - 진단: STYLE-H1R 절제의 과잉 적용 — 사건 온도·훅 강도·대사 열기 부족.
- Process:
  - 동일 장면(EP001 오프닝) 3-모델 A/B 테스트: Fable 리듬 강화 / Opus / Sonnet.
  - 사용자 선택: **Fable 리듬 강화**.
  - C1 규칙 신설(오프닝 인메디아스레스, 대사 온도 상향, 장면당 인물 펀치 1+, 서술자 격언 제한 유지).
- New:
  - EP001 전면 재작성(카운트다운 구조), EP002 국소 개정, EP003 QA 수리 + C1 반영.
  - 3화 통합 QA 통과 후 accepted 교체.
- Canon/Blueprint/POV/Reveal 변경: **0**.
- Status: **`CALIBRATION C1 ACTIVE / EP001~003 ACCEPTED (3/230)`**.

---

## CHG-049 — STYLE-METHOD-v1 제정 + EP001 플래시포워드 프롤로그 도입
- Date: 2026-08-18
- Change Location:
  - `docs/manuscript/STYLE-METHOD-v1.md` 신설 (10개 참고 작품 기법 합성 → M1~M11 실행 코덱스)
  - `manuscript/*/act01/EP001.md` — 프롤로그 추가
- Previous:
  - 사용자 2차 피드백: C1 문체 보정 후에도 "1화가 재미없다".
  - 진단: 문체가 아니라 구조 — 제목의 약속(1명)과 1화 소재(주거 분쟁) 사이 견인력 공백. Deep Card §9가 예고한 Title-Promise Delay 리스크의 현실화.
- New:
  - EP058 공표 순간의 익명 몽타주 프롤로그(~700자)를 EP001 앞에 배치.
  - **Reveal fence 검증**: 노출 정보 = 제목이 이미 공개한 것(집계 1) + 공표가 언젠가 일어난다는 사실뿐.
    - Amara/이름/신원 단서 0. 의미(Meaning) 설명 0 — "폐지된 지 오래된 기술 분류라고만" (§52 pre-explain 금지 준수).
    - 공표 주체 = 정합 보고서 (§50 "schema-integrity report publishes aggregate 1" 정합).
    - "나머지는 무엇인가"는 시민들의 질문으로 프레이밍 — 서술자 ontology 선언 아님 (§50 FORBIDDEN 준수).
    - "열 달 전" = M1 산술 정합 (EP001 T-14.0 → EP058 T-13.15 ≈ 10.2개월).
  - **POV 규칙 예외 기록**: 프롤로그는 에피소드가 아닌 프레이밍 장치. 공적 사실의 익명 몽타주만 허용, 에피소드 본문 POV 규칙은 불변. 이 장치는 EP001 1회 한정 — 남용 금지.
- 스토리 락 이동: **0** (EP056/058 사건 시점 불변 — 표현 장치만 추가).
- Status: **`PROLOGUE FRAME ADOPTED / STYLE-METHOD-v1 ACTIVE`**.

---

## CHG-050 — Minimum Action Agent OS 작업방법론 채택 (도메인 무변경)
- Date: 2026-08-19
- Change Location:
  - `CLAUDE.md` §13 신설 (순수 가산 +41행, 삭제 0행)
  - `.claude/agents/episode-qa.md` 신설
- Previous:
  - 프로젝트에 `.claude/` 없음. 작업체계가 전부 산문 규칙으로만 존재.
  - 원고 QA를 매번 `general-purpose` 서브에이전트(도구 `*` = Write/Edit/Bash/Agent 포함)에 위임 — 심사자가 심사 대상을 수정할 수 있는 구조적 독립성 결함.
- New:
  - `storm-credit/minimum-action-agent-os`를 **작업 방법론으로만** 채택. Local action space 기본 `<= 5`, 전체 Agent 수 무제한, 5 초과 시 시정 사다리 명문화.
  - OS 프리미티브 9종을 **기존 자산에 매핑**(Harness M1~M8 / Red Team 72건 / 4-DESIGNS 93건 / change-log 등) — 중복 기계장치 생성 0.
  - `episode-qa` 에이전트: `tools: Read, Grep, Glob` 화이트리스트로 local action space **∞ → 3**. Write/Edit/Bash/Agent 차단으로 재위임 우회까지 봉쇄.
- Canon / Blueprint / POV / Reveal / 원고 변경: **0**. Agent 삭제: **0**.
- QA: 독립 Critic 검수 `PASS_WITH_RISKS` / blocking **0** / 지적 7건 전량 반영 완료.
- Status: **`OS ADOPTED AS METHOD ONLY / DOMAIN CANON UNTOUCHED`**.

---

## CHG-051 — 원고 진척 수치 동기화 + PROVISIONAL 줄거리 대조 진단
- Date: 2026-08-19
- Change Location:
  - `CLAUDE.md` §1 / §12
  - `docs/current-work-status.md`
  - `canon/CANON_STATUS.md` §1 / §8
  - `docs/NEXT-CHAT-HANDOFF.md` Global State / Manuscript State
  - `docs/change-control/PROVISIONAL-LOGLINE-vs-CANON-v2-COMPARISON.md` 신설
- Previous:
  - EP001~010 승인 후에도 위 4개 파일이 `MANUSCRIPT = READY / NOT STARTED` / `Accepted 0 / 230` / `First eligible EP001` 로 잔존.
  - `NEXT-CHAT-HANDOFF.md` 는 상단 롤링 블록(10/230)과 하단 절(0/230)이 **한 파일 안에서 자기모순**.
  - 사용자 제기: "현재 줄거리가 내가 처음 설계한 것과 다른 것 같다" (장르 불일치 감각).
- New:
  - 4개 파일 수치를 `IN PROGRESS` / `10 / 230 (EP001~010)` / `First eligible EP011` 로 정정.
  - 각 위치에 "원고 진척 수치의 정본은 `docs/manuscript/MANUSCRIPT-STATUS.md`" 명시 — 재발 방지.
  - **PROVISIONAL 줄거리 대조표 신설.** 사용자 기억 설계 ↔ CANON v2 항목별 대조 결과:
    - **14개 항목 중 13개 일치.** 설계 유실 없음.
    - 실질 불일치 = **주인공 성별 1건** (사용자 기억 = 남성 / 정본 = 마렌 베일 여성).
    - 특히 §12 "유일한 인간 = 부모가 Seed를 거부해 태어났으나 본인은 자기 아이들에게 Seed를 시술한 평범한 부모" = 아마라 오코로 C0와 **완전 일치**.
  - "장르가 다르다"의 원인 규명: 설계 문제 아님. **미스터리 실이 EP012(프라이머)/EP017(첫 이상징후)에서 시작하는데 승인 원고가 EP010에서 끝나** 독자가 엔진 점화 직전에 멈춘 구조.
- 설계 변경: **0**. Canon / Blueprint / POV / Reveal / 원고 변경: **0**.
- 열린 결정 2건 (미실행, 각각 별도 CHG 필요):
  - **D1** 마렌 성별 남성화 — Character Bible C0 재개방 + EP001~010 호칭 회귀 필요.
  - **D2** 미스터리 실 전진 배치 — Blueprint 조정 등급, Canon 무변경.
- Status: **`STATUS SYNC COMPLETE / DESIGN MISMATCH SCOPED TO 1 ITEM / D1·D2 PENDING USER DECISION`**.

---

## CHG-054 — V3 최종 집필 전 맹점 감사 + 라우팅/POV 우선순위 패치
- Date: 2026-08-21
- Change Location:
  - `docs/qa/V3-FINAL-PRE-MANUSCRIPT-BLIND-SPOT-AUDIT-v1.md` 신설
  - `CLAUDE.md` §0.5 신설 (순수 가산) + §1 / §12 v2/v3 라인 구분 표기
  - `canon/CANON_STATUS.md` V3 TRACK NOTICE 추가
  - `docs/manuscript/MANUSCRIPT-STATUS.md` V3 TRACK NOTICE 추가
  - `docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md` §3.1 POV OWNERSHIP PRECEDENCE 신설
- Trigger:
  Claude(오케스트레이터) + Codex CLI(독립 적대 검수, 3회 분리 실행) 합동 게이트 감사.
- Previous:
  - **C-01 (P0)** — `CLAUDE.md` / `CANON_STATUS.md` / `MANUSCRIPT-STATUS.md` 에 v3 트랙 언급이 **0건**.
    권위 1순위 문서가 신규 세션을 v2 EP011로 라우팅하고 v3로 가는 경로를 제공하지 않음.
  - **C-02 (P1)** — `POV-OWNERSHIP-REALLOCATION-v0.2` 가 protagonist-owned로 판정하는 **47화**의
    블루프린트 카드·Deep 사이드카가 여전히 조연 POV이며 `Do not reroute … through the protagonist` 를 지시.
    CTX/DEEP 820노드 중 overlay 참조 **0건**.
- New:
  - v3 트랙 포인터 3곳 추가. `10 / 230` · `EP011` 을 v2 라인 한정으로 명시. v3 = `0 / 410` 미착수 명시.
  - 47화 목록 + overlay가 부재로 유지하는 6화 + 재현 가능한 도출 방법을 명문화.
    overlay 자체 선언의 집행이며 새 결정 아님.
  - Codex 재검증 1차에서 초안 42화 목록이 오류로 REJECT됨(`Reason:` 산문의 부정 진술 오염).
    §0 규칙 1 기준 차집합으로 재계산 → **47화**, 검산 272 + 47 = 319 일치. 수정 반영.
- Canon 승격: **0**. Blueprint 카드 수정: **0**. Deep Context 노드 생성/수정: **0**.
  주인공 이름 확정: **0**. 원고: **0**.
- 감사 결과: P0 = 1 (해소) / P1 = 3 (2건 해소, 1건 작가 결정 대기) / P2 = 5 / Taste = 0.
- 미해소 P1 = **D2 미스터리 실 전진 배치** (CHG-051에서 개방, 미실행).
  v3 Act1 최초 clue PLANT = EP022 / 최초 미스터리 실(D05) bounded payoff = EP028 로
  v2(프라이머 EP012 / 첫 이상징후 EP017)보다 늦어졌고,
  `GENRE_ENGINE_RED_TEAM-v1` 의 "P1 NARRATIVE-ENGINE CORRECTION REQUIRED BEFORE PROSE" 판정이 미종결.
  **작가 결정 사항이므로 감사자가 임의 처리하지 않음.**
- Status: **`AUDIT COMPLETE / VERDICT = PATCH / ROUTING+POV PATCHED / D2 PENDING USER DECISION`**.

---

## CHG-055 — V3 Canon 승격 + 주인공 이름 확정 + D2 / I-01 / J-01 실행
- Date: 2026-08-21
- 전체 기록: `docs/change-control/CHG-055-V3-CANON-PROMOTION.md`
- 사용자 명시 승인: Gate A 승격 / Gate B 이름 / D2 실행 / I-01·J-01 즉시 해소.
- **Gate A** — Option B 승격 실행. 공식 정본 = v3(9막/410화). v2 = FROZEN HISTORICAL EDITION.
  10단계 체크리스트 전부 완료. minimal-mutation 원칙 준수(대량 리네임 없음).
- **Gate B** — 주인공 **루카스 켈러 / Lukas Keller** 확정, 호칭 `루카스`.
  `루카스 베르너` 기각 사유: 베르너가 이름/성 겸용 + 자체 채점 4위(32/35) + HERO 플래그.
  `[주인공/TBD]` → `루카스` 치환 **1040건 / 259파일**. 가족 성씨 베르너→켈러.
- **D2 (감사 C-03, P1)** — 미스터리 실 전진 배치 실행(Design A).
  첫 primer EP022→**EP007**, 첫 전문적 PLANT→**EP012**, 첫 bounded payoff EP028→**EP014**.
  reveal window 무위반, `ordinary_event_guard: HARD` 유지, Act 길이·경계 무변경.
- **I-01 (P1)** — EP288/EP290 재배치로 EP280~290 "같은 이상, 다음 도메인" 공식 해체. Act7 길이 무변경.
- **J-01 (P2)** — Act9 임신 시계 LOCK. Act7 개시 촉발 + 8/12/18 = ~38주 → EP408 정상 출산.
  이미 `V3-FULL-SERIES-TIMELINE`·`HUMAN1 의학 QA §7~§8`에 있던 수치를 블루프린트에 동기화한 것.
  Act9 hostile QA Timeline gate **CLOSED**.
- 구조 변경: **0**. 9막/410화·Act 경계·POV 총계·reveal ledger·존재론·자산 로스터 무변경.
- 원고: **0**. 활성 v3 원고 = **0 / 410**.
- Status: **`V3 PROMOTED / NAME FROZEN / AUDIT P0=0 P1=0 / MANUSCRIPT START = 사용자 지시 대기`**.

---

## CHG-056 — v3 EP001 집필 시작 + 승인 (1 / 410)
- Date: 2026-08-21
- Change Location:
  - `manuscript/v3/_work/act01/EP001.md` / `manuscript/v3/accepted/act01/EP001.md` 신설
  - `docs/manuscript/qa/V3-EP001-QA.md` 신설
  - `docs/manuscript/MANUSCRIPT-STATUS.md` 0/410 → **1/410**
  - `docs/manuscript/MANUSCRIPT-PIPELINE-v1.md` §2 경로 분리 명문화
- Trigger: 사용자의 명시적 Manuscript Start 지시.
- **경로 분리(중요):** v2·v3 둘 다 EP001부터 번호를 매기므로 트리를 공유하면
  v3 EP001이 승인된 v2 EP001을 덮어쓴다. v2 파일은 **이동하지 않았다**(기존 QA/변경기록 참조가 깨짐).
  v3는 `manuscript/v3/` 하위 트리를 새로 쓴다. v2 트리는 **쓰기 금지**.
- QA: 읽기 전용 `episode-qa` 에이전트, 백지 상태 2회 독립 심사.
  - r1 **REPAIR** — 필수 수정 10건. 하드 펜스(Clue NONE / ordinary_event_guard / 리빌 금지 /
    POV / 권한 한계 / 용어 예산)는 1차부터 전부 통과, 블루프린트 9개 필드 전부 이행.
    결함은 전부 문장 수준: 기디언 현자화, EP007 관계 비트 조기 소진, 인물 소개 dossier 2건,
    볼트/접합부 기술 오류, 훅이 EP002와 다른 부서 지시, 종결부 서술자 요약, 존댓말 불일치,
    서술자 회피성 은닉, `선체` 누락(우주선임이 드러나지 않음), M10 계량 위반 4종.
  - r2 **PASS** — 10/10 반영 확인, 계량 5종 전부 상한 내 재계수.
  - r3 — 승격 커밋에서 staging 중복 1건 + register drift 1건 수정.
- 핵심 진단(EP002~ 이월): **"서술자가 이 화에서 제일 약한 인물"**. 서술 문장 12개 제거 후 등급 상승.
- 설계/Canon/Blueprint/POV/Reveal 변경: **0**. v2 파일 변경: **0**.
- Status: **`EP001 ACCEPTED / v3 1 of 410 / EP002 대기(사용자 지시 필요)`**.

---

## CHG-057 — Deep Context JIT 실현 상태 도입 (스키마 명확화 + 검증기)
- Date: 2026-08-21
- Change Location:
  - `docs/prewriting-v3/DEEP-CONTEXT-SCHEMA-v1.md` §1 — 2-state 계약 명문화
  - `tools/deep_context_integrity.py` — 상태별 검증 + act 매핑 헬퍼
  - `docs/obsidian-v3/deep-contexts/DEEP-V3-EP001.md` — REALIZED 전환 + 6개 필드 실현
  - `docs/obsidian-v3/deep-contexts/DEEP-V3-EP002.md` — lane 2에 EP001 실제 연속성 주입
- Trigger:
  EP001 원고가 승인되면서 설계상 예정돼 있던 **JIT Dynamic Actual 단계가 처음으로 발동**.
  그런데 `deep_context_integrity.py`가 `realized_*` 6개 필드를 **무조건** `PENDING`으로 강제해서
  실현을 기록하면 검증이 깨졌다. 검증기는 승인 원고가 0편이던 시점에 작성된 것이다.
- 판단:
  스키마 §1은 원래 `PENDING`을 "**until JIT pre-draft freeze**"로 규정했고, §0은 `5. future JIT
  Dynamic Actual state`를 계층으로 열거한다. 즉 실현은 설계된 전이이며, 검증기가 과도했다.
  다만 전 시리즈 Red Team이 닫은 P0 `Forecast silently becomes Actual continuity`를 되열면 안 된다.
- New:
  노드는 **정확히 두 상태 중 하나**이고 frontmatter가 어느 쪽인지 **선언**해야 한다.
  - Forecast: `FORECAST_NOT_ACTUAL` + `PENDING` → 6필드 전부 `PENDING` 강제
  - Realized: `REALIZED_FROM_ACCEPTED_PROSE` + `REALIZED` → 6필드 전부 실값 강제,
    **그리고 `manuscript/v3/accepted/actXX/EPxxx.md`가 실제로 존재해야 한다**
  선언 자체가 P0 가드다. forecast가 조용히 actual이 되는 경로가 없다.
- 음성 테스트 2건 통과:
  ① forecast 노드에 실값 주입 → ERROR. ② 승인 원고 없이 REALIZED 선언 → ERROR.
- 적용: EP001 REALIZED 전환, EP002 lane 2에 실제 연속성 주입(장비 스레드 = EP002, 배차 스레드는 열린 채).
- Canon / Blueprint / POV / Reveal 변경: **0**. 410/410 무결성 유지, errors 0 / warnings 0.
- 함께 처리: **CHG-055 미실행 4차 검증(위생)** — Codex 한도 복구 후 실행, `HYGIENE FAIL`.
  1~3차가 놓친 승격 잔여 4건 발견(해당 파일들을 아무도 열어보지 않았기 때문):
  `V3-CORE-CAST-ACT-ROLE-MATRIX`(Protagonist TBD, authority map에서 라우팅됨),
  `V3-C2-ACT-SURFACE-LANGUAGE-OVERLAY`(루카스 미승인 취급 + `주인공/TBD` 허용),
  `CURRENT-GRAPH-STATUS` / `contexts/V3-410-PROJECTED-CONTEXT-MANIFEST`(공식 Canon = v2 주장).
  전부 수정. 재스윕 결과 잔여는 `SUPERSEDED` 명시 또는 라우팅 0인 역사 기록뿐.
  실질 내용(47화 POV 목록 272+47=319, D2 Act1 일정, Act9 38주, v2 원고 바이트 동일)은 무손상 재확인.
  Codex의 FAIL 1건(`942dfbe`가 `CANON_STATUS.md` 수정)은 **기각** — 원고 진척 반영은 정상 동작이며 질문 표현이 부정확했다.
- Status: **`JIT REALIZATION ACTIVE / P0 FORECAST-VS-ACTUAL GUARD PRESERVED / CHG-055 HYGIENE GAP CLOSED`**.

---

## CHG-058 — v3 EP002 승인 (2 / 410) + Codex 집필 파이프라인 첫 운용
- Date: 2026-08-22
- Change Location:
  - `manuscript/v3/{_work,accepted}/act01/EP002.md` 신설
  - `docs/manuscript/qa/V3-EP002-QA.md` 신설
  - `docs/manuscript/MANUSCRIPT-STATUS.md` 1/410 → **2/410**
  - `DEEP-V3-EP002` → `REALIZED`, `DEEP-V3-EP003` lane 2에 실제 연속성 주입
- 집필: **Codex CLI**. 심사: 읽기 전용 `episode-qa` 2회 독립 심사. 최종 판정: 오케스트레이터.
- **오케스트레이터 오류 기록**: 초고가 12,008자로 정본 길이의 2.2배였다.
  원인은 집필 지시서에 `EP001 = 12,862자`라고 준 것 — 그건 **문자 수가 아니라 바이트 수**였다.
  한국어 UTF-8은 문자당 약 3바이트이므로 실제 정본 길이는 ~5,500자다.
  Codex는 지시를 정확히 따랐다. 목표 정정 후 압축으로 품질 손실 없이 복구.
  **교훈: 한국어 분량은 문자로 재라. `wc -c` / `wc -m` 금지.**
- QA r1 `REPAIR` 9건 (High 3):
  - **R1** 승인된 EP001과 모순 — EP001은 `"고쳤네요."`로 끝나는데 EP002는 볼트가 안 조여진 채 열림.
    → EP001의 `0.11`이 *3구획을 비워둔 값*이었다는 한 문장으로 화해. **승인 원고 수정 없이 해결.**
  - **R2** 서술자 격언 4/1 — EP001 핵심 교훈("서술자가 제일 약한 인물") 부분 퇴행. 3건 행동으로 전환.
  - **R3** 종결 장치가 EP001과 중복(구성요소 동일, 순서만 반전, 화자쌍도 동일).
    → `조용한 비가역 파급 + 물리 상태`로 교체.
  - R4~R8: 기디언 조건 필드 미종결 / EP001이 두 번 심은 배차실 마찰을 한 문장으로 지불 /
    프레팅 몇 달 vs 두 달 계단 논리 공백 / 3장면 행정 전용 / EP001의 수치 축 단절.
  - **R9 (설계급)** `flaw_pressure` 미달 — 루카스가 모든 응수를 이기고 아무도 그에게 착지하지 않음.
    게다가 기디언의 EP001 교정을 완벽히 수행해서, **9막에 걸쳐 그를 부술 결함이 2화에 벌써 나아 보임.**
    → 통제가 대가를 치르는 비트 추가.
- r2 `PASS`. 계량 7종 전부 상한 내(격언 1/1, 부정-반전 2/2, 금지 3종 0). conditional-gnomic 상습화 해소(3→1).
- r3에서 P2 3건 반영. 그중 하나는 **심사자가 자기가 쓴 문장을 스스로 감사해서** 지적한 것.
- 오케스트레이터가 요청 없이 추가한 밀폐세계 질감 1줄은 심사자에게 명시적으로 판단을 맡겼고, **유지 판정**.
- Canon / Blueprint / POV / Reveal 변경: **0**. v2 트리 변경: **0**. 무결성 410/410.
- Status: **`EP002 ACCEPTED / v3 2 of 410 / EP003 대기(사용자 지시 필요)`**.

---

# Current Change-Control Rule

Current official world/character/narrative authority (**v3, promoted 2026-08-21**):
- `canon/WORLD_BIBLE-v3-CANDIDATE.md` + `canon/WORLD_BIBLE-v3-ADDENDUM-*.md`
- `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md`
- `canon/ACT_BIBLE-v3.2-CANDIDATE.md`

Current narrative execution authority:
- `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT{1..9}-v0.1.md`
- `docs/prewriting-v3/POV-OWNERSHIP-REALLOCATION-v0.2.md`
- `docs/prewriting-v3/V3-FULL-SERIES-TIMELINE-v0.1.md`
- `docs/obsidian-v3/contexts/` → `docs/obsidian-v3/deep-contexts/`

**v2 (`WORLD_BIBLE-v2` / `CHARACTER_BIBLE-v2` / `ACT_BIBLE-v1` / Amendment A) = FROZEN HISTORICAL EDITION.**
**`canon/v2/` = NON-CANON experimental design history.**

For contradiction-level change after v3 promotion:
`identify issue → alternatives/impact → CHG entry → hostile Red Team → affected-episode regression → deliberate Canon reopening`.

Never silently overwrite v3 Canon from prose.

C2 refinement inside frozen ranges is allowed, but recurring/clue-bearing/causal C2 must be
promoted/logged before manuscript acceptance.

Current manuscript state:
**`IN PROGRESS`** — active v3 **2 / 410** (EP001~002 accepted); historical v2 **10 / 230** frozen.

원고 진척 수치의 정본은 `docs/manuscript/MANUSCRIPT-STATUS.md`.
