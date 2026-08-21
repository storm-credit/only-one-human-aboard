# MANUSCRIPT STATUS

Project: 《우주선에는 인간이 한 명뿐이다》

Pipeline: `docs/manuscript/MANUSCRIPT-PIPELINE-v1.md`

Official rule:
Only `manuscript/accepted/` + this ledger count as completed manuscript.

---

# 0. TWO LINES — DO NOT MIX

## Active line — v3 (9 Acts / 410 episodes)
# **4 / 410 — IN PROGRESS**

Paths: `manuscript/v3/_work/actXX/` → `manuscript/v3/accepted/actXX/`.
The v2 tree at `manuscript/_work/` + `manuscript/accepted/` is **frozen — never write into it.**
Both editions number from EP001, so the trees are deliberately separate (CHG-055).

Official Canon since **2026-08-21** (`docs/change-control/CHG-055-V3-CANON-PROMOTION.md`).
Protagonist: **루카스 켈러**, reader-facing call-name `루카스`.

## Historical line — v2 (7 Acts / 230 episodes)
# **10 / 230 — FROZEN / PRESERVED / CLOSED**

`manuscript/accepted/` EP001~010 belong to this line. They are **not** failed and **not** deleted.
Do **not** carry them into the v3 line, and do not treat v2 reveal locks
(EP056/058/066/068/075) as v3 constraints.

---

# 1. CURRENT GATE

- `V3 CANON PROMOTION = EXECUTED — 2026-08-21`
- `PROTAGONIST FINAL NAME = APPROVED — 루카스 켈러`
- `EP001~410 BLUEPRINT = 410 / 410`
- `DEEP PROJECTED CONTEXT = 410 / 410 / P0=0 / P1=0`
- `FINAL PRE-MANUSCRIPT BLIND-SPOT AUDIT = PATCH → 해소`
- **`MANUSCRIPT DRAFTING = IN PROGRESS`** — started 2026-08-21 on explicit user instruction

Next eligible episode: **EP002 — 원인은 한 칸 앞에 있다**

A generic `이어서/진행` still does **not** authorize the next episode.

---

# 2. CURRENT SUMMARY — v3 ACTIVE LINE

- Accepted: **4 / 410**
- Work Draft: **0**
- QA Review: **0**
- Revision Required: **0**
- Canon Review: **0**
- Recheck Required: **0**
- Published: **0**

## Accepted episodes
- **EP001 — 오래된 진동** — 루카스 POV — QA `PASS` (`docs/manuscript/qa/V3-EP001-QA.md`) — 2026-08-21
  - r1 `REPAIR` (10 required repairs) → r2 `PASS` → r3 staging/register fixes at promotion.
  - Clue `NONE` honored; 0 new stable terminology labels; all 9 blueprint card fields delivered.
- **EP002 — 원인은 한 칸 앞에 있다** — 루카스 POV — QA `PASS` (`docs/manuscript/qa/V3-EP002-QA.md`) — 2026-08-22
  - Drafted by Codex. r1 over-length (12,008자, orchestrator gave a byte count as a char count)
    → compressed → `REPAIR` (9 items, 3 High) → r2 `PASS` → r3 three optional planes.
  - Clue `NONE`; 0 new stable labels; 9/9 card fields; EP007 credit debt unspent and **enlarged**.

- **EP003 — 퇴근은 이동이다** — 루카스 POV — QA `PASS` (`docs/manuscript/qa/V3-EP003-QA.md`) — 2026-08-22
  - Drafted by Codex. r1 `REPAIR`(9) → r2 `REPAIR`(5+2) → r3 `PASS`. **16 repairs, 3 revisions.**
  - **Both binding structural risks retired**: the 메리디언 enclosed-world debt cleared through use,
    and the personal stake landed in sentence 1 after two episodes of deferring it to the final page.

- **EP004 — 한 노선 덜 쓰기** — **미라 POV (첫 비주인공 시점)** — QA `PASS` (`docs/manuscript/qa/V3-EP004-QA.md`) — 2026-08-22
  - Drafted by Codex. r1 `REPAIR`(P0×4, P1×9) → r2 `REPAIR`(9) → r3 `REPAIR`(1) → r4 `PASS`.
  - **첫 7종 정량 전부 통과.** 루카스 0회. 종결 장치 `대가` 확보로 EP001~003 A-B-A 회전 탈출.
  - **"비주인공이 한 화를 감당하는가" = YES.** 410화 중 91화가 비주인공 POV라 구조적으로 중요.

Next eligible v3 episode:
# **EP005 — 남의 결정도 내 하루가 된다**

**Before drafting EP005 read `docs/manuscript/qa/V3-EP004-QA.md` §8.** 미라는 등장하지 않는다 —
루카스는 그녀가 아니라 **그녀의 결정**을 만난다. EP004가 `미드링 4번 환승 게시 화면`에
`현장 권한 없음` 문장을 심어 뒀다. 비용은 이미 확정돼 있다: **4,200명 × 17분.**
**미결: 댐퍼 담당 칸 공란 — EP006까지 채우거나 재배정.**

---

# 3. ACT PROGRESS — v3

| Act | Episodes | Count | Accepted | State |
|---|---|---:|---:|---|
| Act1 우리가 살던 메리디언 | EP001~042 | 42 | **4** | IN_PROGRESS |
| Act2 닫힌 구획 | EP043~094 | 52 | 0 | LOCKED_FUTURE |
| Act3 같은 아침이 아니다 | EP095~136 | 42 | 0 | LOCKED_FUTURE |
| Act4 미래를 안다고 믿는 사람들 | EP137~181 | 45 | 0 | LOCKED_FUTURE |
| Act5 없었던 역사 | EP182~228 | 47 | 0 | LOCKED_FUTURE |
| Act6 멸망했던 메리디언 | EP229~279 | 51 | 0 | LOCKED_FUTURE |
| Act7 셀 수 없는 삶 | EP280~327 | 48 | 0 | LOCKED_FUTURE |
| Act8 한 명과 수많은 사람 | EP328~370 | 43 | 0 | LOCKED_FUTURE |
| Act9 처음 가는 곳 | EP371~410 | 40 | 0 | LOCKED_FUTURE |
| **Total** | **EP001~410** | **410** | **4** | |

`LOCKED_FUTURE` = designed and Canon-locked, but not the next manuscript episode.

---

# 4. EP001 EXECUTION CONTRACT — v3

When EP001 drafting is explicitly started, retrieve in this order:

1. `CLAUDE.md`
2. `canon/CANON_STATUS.md` — confirm v3 active
3. `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md` — **exact EP001 card only**
4. `docs/obsidian-v3/contexts/CTX-V3-EP001.md` — thin router
5. `docs/obsidian-v3/deep-contexts/DEEP-V3-EP001.md` — deep sidecar + its 5-lane Retrieval Compile Map
6. `docs/prewriting-v3/POV-OWNERSHIP-REALLOCATION-v0.2.md` — POV ownership check
7. `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md` — 루카스 / Gideon / Niko only
8. `canon/WORLD_BIBLE-v3-*` — only EP001-relevant sections (Old Works)
9. `docs/prewriting-v3/V3-FULL-SERIES-TIMELINE-v0.1.md`
10. `docs/prewriting-v3/V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1.md` — EP001~014 execution locks
11. `docs/manuscript/PROSE-STYLE-RUBRIC-v1.md` §20 + `STYLE-METHOD-v1.md`

**Max 5 direct context bundles.** Large matrices are routers only.

Do NOT load:
- `canon/v2/` (retracted),
- v2 bibles / `ACT_BIBLE-v1.md` / Amendment A as active Canon,
- `docs/writing-ready/EPISODE-BLUEPRINT-ACT1-v0.1.md` — **that is the v2 file with the same name**,
- the whole encyclopedia when a narrow Context Pack is enough.

Hard:
- one POV per episode, close third, causal-owner POV, no head hopping
- AUTHOR future knowledge must not leak into POV
- Sub-Act candidate device ≠ episode exposure
- no new major world rule invented during prose
- C2 detail must stay inside frozen v3 constraints
- any recurring/causal new fact must be logged through Change Control before accepted status

---

# 5. ACT1 EARLY-SERIES EXECUTION LOCKS

From `V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1.md` + CHG-055 (D2 실행):

- EP001~006: deliberately clue-free. Reading promise = `이 주인공은 일하는 걸 보는 재미가 있다`.
- **EP007** — D05 mundane primer. Ordinary safety knowledge, no anomaly, **no ominous framing**.
- **EP008~014** — the genuine industrial accident arc carries the early genre load.
- **EP012** — D05 professional PLANT. Noticed for professional reasons only.
- **EP014** — the accident really was an accident **and** one inherited procedure has no origin.
- **EP022 / EP028** — REINFORCE and second bounded payoff.
- `ordinary_event_guard: HARD` — ordinary failures must stay genuinely ordinary.
- EP042 ends on an ordinary next-work state; no manufactured cliffhanger.

---

# 6. ACCEPTANCE RULE

A generated draft does not count as completed. Progress counts only after:

1. work draft
2. prose/voice/continuity QA
3. Canon/reveal/knowledge-fence QA (read-only `episode-qa` agent)
4. required revision
5. accepted copy under `manuscript/accepted/`
6. this ledger updated

Draft가 이 파이프라인을 통과해야만 Accepted로 계상된다.

---

# 7. NEXT ACTION

Eligible next action:
**v3 EP005 manuscript execution** — requires a new explicit user instruction.

# 회차 분량 규정 — 하한만 있고 상한은 없다 (작가 결정, 2026-08-22)

# **하한 5,500자. 상한 없음.**

측정은 Python `len()`, 본문만. **`wc -c` / `wc -m` 금지** — 여기서는 바이트를 보고하므로 약 2.4배로 오도한다.

근거와 경위:
- 유일하게 문서화된 규정은 `docs/writing-ready/PROSE-EXECUTION-PROTOCOL-v1.1.md` §6
  (`soft production band 5,500~8,000 / exact count is not Canon`)이며, 이는 **v2 시대 문서**로
  v3 권위 목록에 없다. 즉 v3에는 분량 규정이 없었다.
- 그 공백에서 오케스트레이터가 승인된 EP001~003으로부터 `5,410~5,539` 밴드를 **역산해 상한처럼 사용**했다.
  이는 규정이 아니었고, 회차를 정당 범위의 바닥에 묶었다. **EP001~003은 전부 하한 5,500에 걸치거나 미달이다**
  (5,512 / 5,410 / 5,539). EP002는 90자 부족.
- 작가 결정으로 정정: **하한만 유지하고 상한은 두지 않는다.**

운용:
- 하한 미달은 결함이다. 초과는 결함이 아니다.
- 길이를 이유로 장면을 자르지 마라. 자를 이유는 언제나 문장 수준의 결함이어야 한다.
- 협상·다자 대화가 있는 화는 독백형 화보다 길어지는 것이 정상이다.

# `IN PROGRESS / 4 of 410`
