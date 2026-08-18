# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> Rolling handoff — 2026-08-19 MANUSCRIPT IN PROGRESS.
> **Accepted 10/230 (EP001~010). 사용자 지시 배치(EP010까지) 완료 + 배치 QA 완료. Next eligible: EP011 (신규 지시 대기).**
> EP011 집필 전 필독: `docs/manuscript/qa/BATCH-EP001-010.md` 의 P1 하드 제약 6건 (종결 다변화 / 공적 파장 훅 EP013까지 금지 / 관료 조연 원형 금지 / 마렌 POV 복원 / 노아 청취 온스테이지 / 용어 상한) + C2 원장.

## 집필 세션 상태 (2026-08-18 갱신)
- CHG-047: WORLD/CHARACTER Bible v2 본문이 스텁이었던 P0를 blob에서 복원 완료 (main 정상).
- CHG-048: **CALIBRATION C1** — 독자 피드백 "재미없다" → 3-모델 A/B 후 "Fable 리듬 강화" 채택. `PROSE-STYLE-RUBRIC-v1.md` §20.
- **STYLE-METHOD-v1** (`docs/manuscript/STYLE-METHOD-v1.md`) — 10개 참고작 기법 합성 문체법 M1~M11. 집필·QA의 문장 단위 기준. 참고 목록: `STYLE-REFERENCES-v1.md`.
- CHG-049: **EP001 플래시포워드 프롤로그** (EP058 공표 순간 익명 몽타주) — fence 검증 완료, 1회 한정 장치.
- 파이프라인: 화당 draft(_work) → 독립 적대적 QA 서브에이전트 → 수리 → accepted 승격 → MANUSCRIPT-STATUS 갱신 → **매 화 main push** (사용자 지시).
- QA 이월 감시: 일반화 지름길("~들은 ~한다"), 조연 반어 동질화(비반어 조연 화당 1+ 의무), 3항 나열, 훅 유형 로테이션 장부(EP005-QA.md 참조). EP006 훅은 '선택' 계열 회피.
- EP011 제약: EP004 항고 인용 3건이 심사국 workload로 가시화되어야 함. "임시 지위 항고 닷새 심리 / 3인 재판부" C2 고정.
- 신설 C2 인물: 에런 소사(복원 복귀자, 아내는 앵커 소실로 복원 불가), 미오 탄(현 점유 가구), 다닐로 레예스(EP005 환자). 재사용 시 이 설정 유지.

---

# Repository / Recovery Order

Repository:
`storm-credit/only-one-human-aboard`

Read first:
1. `CLAUDE.md`
2. `docs/NEXT-CHAT-HANDOFF.md`
3. `docs/current-work-status.md`
4. `canon/CANON_STATUS.md`
5. **`canon/WORLD_BIBLE-v2.md`**
6. **`canon/CHARACTER_BIBLE-v2.md`**
7. **`canon/ACT_BIBLE-v1.md`**
8. **`canon/CANON-v2-AMENDMENT-A-GOVERNANCE-ETHICS.md`**
9. `docs/manuscript/MANUSCRIPT-STATUS.md`
10. `docs/change-log.md`
11. `docs/reference-atlas/00-REFERENCE-MOC.md`
12. `docs/narrative-engineering/00-NARRATIVE-MOC.md`
13. `docs/narrative-engineering/EP001-230-CONTEXT-MANIFEST-REGISTRY-v0.1.md`
14. `docs/qa/ENCYCLOPEDIC-CANON-v2-FINAL-RED-TEAM.md`
15. `docs/qa/CANON-v2-AMENDMENT-A-RED-TEAM.md`.

## Critical retraction
**`canon/v2/` is RETRACTED / NON-CANON / design history only.**

It was an experimental modularization attempt made after official monolithic v2 was already frozen. Comparison found some older quantitative candidates and superseded support names inside it.
Never use that folder as normative Canon, even if search returns it first.

Historical/regression-only:
- `canon/WORLD_BIBLE-v1.md`
- `canon/CHARACTER_BIBLE-v1.md`.

Act Bible v1 remains current because macro narrative did not change.

---

# Global State

- `CORE DESIGN FREEZE v1 = PASSED — 2026-08-17`
- `CORE CANON FREEZE v1 = PASSED — 2026-08-17`
- `STRUCTURAL WRITING READY = PASSED`
- `EP001~230 BLUEPRINT = COMPLETE`
- `EP001~230 POV = COMPLETE / PASS`
- `ENCYCLOPEDIC DEEP DESIGN = PASSED — 2026-08-18`
- `PACKAGE A~I = PASS / P0=0`
- `ENCYCLOPEDIC CANON FREEZE v2 = PASSED — 2026-08-18`
- **`CANON v2 AMENDMENT A = FROZEN / PASSED — 2026-08-18`**
- **`MANUSCRIPT = READY / NOT STARTED`**
- Accepted manuscript = **0/230**.

Generic `진행/이어서` does not automatically mean manuscript prose. Continue the active admin/design/QA task unless the user explicitly asks to draft.

---

# Current Official Canon Authority

## World
**`canon/WORLD_BIBLE-v2.md` — CANON.**

Use its official final P1 closures/quantitative bands.
Do not substitute experimental Q1~Q7 ranges from `canon/v2/`.

Includes:
- premise / Seed / Reconstruction
- 450y history + selected anchors
- governance / justice / economy / property / labor / family / education / medicine / death
- data/privacy / AI
- Meridian geography / infrastructure / official Q-SHIP bands
- culture / media / material culture / weapon grammar
- destination / official Q-DEST bands / biosecurity / arrival law / Year-1 scale
- controlled elasticity / forbidden drifts / Reveal guardrails.

## Characters
**`canon/CHARACTER_BIBLE-v2.md` — CANON.**

Includes:
- v1 C0 goals/flaws/voices/arcs/PR-H1
- physical/home/finance/health/hobby/AI/object C1 anchors
- 14-year household/life trajectories
- Amara anti-clue rules
- latest C1 support-name overrides
- C2 reserve/support rules.

## Narrative
**`canon/ACT_BIBLE-v1.md` — ACTIVE.**

Act6 active Blueprint = **v0.2**.
M1 = exact writing-ready time/age authority.
POV maps remain locked.

## Amendment A
**`canon/CANON-v2-AMENDMENT-A-GOVERNANCE-ETHICS.md` — FROZEN CANON ADDENDUM.**

Adds only:
- election / executive / judiciary execution rules
- found-property / salvage
- human-subject research ethics
- narrow competent-adult medical aid-in-dying.

It changes no existing World/Character quantitative, Reveal, POV or ending fact.

---

# Amendment A — Key Locks

## Governance
- franchise 18+
- shipwide general election every 4 civil years
- mixed-member two-vote 선내의회
- Assembly ~120–180 seats bounded, preferred ~150
- residential district + compensatory proportional list seats
- no Habitat/origin/profession/property weighted voting
- Assembly-selected collective civic executive ~5–7 members
- constructive no-confidence
- directly elected local councils; no Habitat sovereignty
- multi-level judiciary
- 시민항소원 = specialized high civic/admin-rights appeal, not whole judiciary
- ordinary emergency cannot indefinitely postpone general elections.

## Salvage / Research / MAID
- finding ≠ ownership
- strategic/common/controlled property does not become private because old/disconnected/decommissioned
- first resource discovery ≠ celestial sovereignty
- human-subject research = consent + ethics review + minimum data access
- **Amara has no research duty**
- MAID-H1 = contemporaneously competent adult + serious irreversible condition + independent review
- disability/poverty/housing scarcity alone never qualifies
- no proxy/guardian/AI/old directive active authorization for currently incapable person.

Change record:
`docs/change-control/CANON-v2-AMENDMENT-A-CHANGE-RECORD.md`.

QA:
`docs/qa/CANON-v2-AMENDMENT-A-RED-TEAM.md`.

---

# Locked Reveal / Story Anchors

- EP056 — internal Count
- EP058 — public Count
- EP066 — Meaning complete
- EP068 — protected Amara confirmation
- EP075 — controlled public confirmation
- EP112 — PR-H1 exact discovery begins
- EP142~151 — Human Settler operational cluster
- EP216 — insertion
- EP230 — no thesis speech.

No bigger ontology twist later.

POV core totals:
- Maren 45
- Ella 27
- Amara 25
- Noah 17
- Raul 17
- Jun 15
- Tomas 13
- Kai 13
- Leo 12
- Ines 10
- Mina 5.

---

# Package G — Narrative Engineering / Obsidian

Status:
`PASS / 230/230 REGISTRY / P0=0`.

Authority:
`official Canon → active Blueprint → locked POV → M1 → applicable Deep Card → exact EP Context Manifest`.

Hard:
**Sub-Act candidate device ≠ episode exposure.**

Important update:
**individual Context Manifest files EP001~230 now physically exist on main.**
The earlier handoff statement that only EP001~028 were split is obsolete.

Context Pack must preserve:
AUTHOR / POV / PUBLIC / PROTECTED knowledge separation.

---

# Package H / I

Package H Reference Atlas:
- PASS
- navigation only
- never overrides Canon/Blueprint/POV/M1.

Package I:
- PASS / P0=0
- deterministic suites PASS
- 20/20 arbitrary-scene battery PASS
- full story/knowledge regression PASS.

The later additional blind-spot pass found governance/salvage/research/MAID specificity gaps and closed them through formal Amendment A rather than silently rewriting official v2.

---

# Official Character Support Names

Use latest `CHARACTER_BIBLE-v2.md` names.

C1 stable-if-used:
- Eli Rhee
- Jae Kadir
- Sami Dae
- Rina Vos
- Rosa Imani
- Arun Salcedo
- Dalia Diniz
- Dev Afolayan
- Nadia Idris
- Tavi Morgan
- Abeni Okoro
- Mateo Varga
- Lina Marquez
- Hana Wu.

C2 reserve:
- Sorin Das
- Yuna Bekele.

Do not resurrect experimental Toma Rhee / Mara Diniz / Sana Idris / Imani Okoro / Leonie Wu.

---

# Hard Stops

Do NOT introduce without deliberate Canon reopening:
- adult origin scanner
- Seed memory/personality/command programming
- anchorless adult restoration
- exact-one/Witness protocol
- Amara sovereignty/admin/land/genetic/settler/reproduction/research key
- mass citizenship erasure
- central AI dictatorship
- Habitat sovereignty/caste
- weighted voting by origin/profession/property
- singular captain-president sovereignty
- bigger ontology twist
- Maren family adjudication
- civil-grid propulsion theft
- instant mature colony
- free perfect third way
- alien/combat takeover
- founder superweapon/relic key
- proxy-authorized active death of an incapable person.

---

# Manuscript State

`docs/manuscript/MANUSCRIPT-STATUS.md`

- READY / NOT STARTED
- Accepted 0/230
- Active episode NONE
- First eligible EP001.

When EP001 is explicitly started, load:
1. official World v2 relevant sections
2. official Character v2 relevant sections
3. Act Bible v1
4. Amendment A only if relevant
5. Act1 Blueprint exact EP001 card
6. Act1 POV Map
7. M1
8. Package G EP001 Context Manifest / applicable Deep Card
9. Prose Protocol v1.1
10. style/QA.

Never load experimental `canon/v2/` as Canon.

Draft does not count until accepted pipeline completes.

---

# Chat Operation

- Never ask the user to repeat project state already stored here.
- Sync meaningful Canon/manuscript changes to GitHub.
- Refresh this handoff before context becomes unsafe.
- Reference Atlas is navigation, not authority.
- C2 details may be chosen inside locked grammar; recurring/causal C2 must be promoted/logged.
- Do not silently reopen Canon.
- Do not start prose during mere administrative continuation.
