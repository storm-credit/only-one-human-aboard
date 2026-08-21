# NEXT CHAT HANDOFF — 《우주선에는 인간이 한 명뿐이다》

> Rolling handoff — updated **2026-08-21** (CHG-055).

# 0. TOP LINE

# **OFFICIAL ACTIVE CANON = v3 — 9 Acts / 410 episodes. PROMOTED 2026-08-21.**
# **PROTAGONIST = 루카스 켈러 / Lukas Keller — call-name `루카스`. APPROVED.**
# **ACTIVE v3 MANUSCRIPT = 2 / 410 — EP001~002 ACCEPTED.**
# **HISTORICAL v2 MANUSCRIPT = 10 / 230 — FROZEN, PRESERVED, CLOSED.**

Do not rebuild anything. Do not re-derive design. Do not ask the user to repaste state.

Promotion record: `docs/change-control/CHG-055-V3-CANON-PROMOTION.md`
Authorizing audit: `docs/qa/V3-FINAL-PRE-MANUSCRIPT-BLIND-SPOT-AUDIT-v1.md`

---

# 1. RECOVERY ORDER

1. `CLAUDE.md`
2. `canon/CANON_STATUS.md` — active v3 file list + frozen v2 list
3. `docs/current-work-status.md`
4. `docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md` — routing, incl. **§3.1 POV ownership precedence**
5. `docs/manuscript/MANUSCRIPT-STATUS.md` — 0/410, EP001 execution contract
6. `docs/change-control/CHG-055-V3-CANON-PROMOTION.md`

For an episode: `exact Blueprint → CTX router → Deep sidecar → max-5 payload`.

---

# 2. WHAT CLOSED IN CHG-055

| Item | State |
|---|---|
| Gate A — v3 Canon promotion (Option B) | **EXECUTED** |
| Gate B — protagonist final name | **APPROVED — 루카스 켈러** |
| audit C-01 (P0) v3 routing absent from top docs | CLOSED (CHG-054) |
| audit C-02 (P1) POV overlay not enforced in execution layer | CLOSED (CHG-054) — 47화, authority map §3.1 |
| audit C-03 (P1) / **D2 미스터리 실 전진 배치** | **EXECUTED** |
| audit I-01 (P1) EP280~290 반복 공식 | **해소** — EP288 / EP290 재배치 |
| audit J-01 (P2) Act9 임신 시계 | **해소** — LOCKED, Timeline gate CLOSED |

**Next: EP003 — 퇴근은 이동이다, on explicit user instruction.**

Before EP003 read `docs/manuscript/qa/V3-EP002-QA.md` §7. Four items bind EP003: clear the enclosed-world texture debt; do NOT close on a passing cargo/vehicle (EP001 and EP002 both did); land 루카스's personal stake earlier than ~90% through; negation-reversal narration is at 2/2 with zero headroom.

---

# 3. NAME STATE — CLOSED

Final: **루카스 켈러 / Lukas Keller**. Reader-facing call = **`루카스`** only.
Do not alternate `루카스 / 켈러` for style.

Household: 마르틴 켈러(부, 68) · 나디아 소토(모, 65) · 클라라 켈러(누나, 41) ·
사미르 코스타(매형, 42) · 에바 코스타(조카, 9).

Rejected and **not** to be revived: `루카스 베르너` (베르너 = 이름/성 겸용, 자체 채점 4위 32/35 + HERO 플래그),
`다니엘 마레크`, `Rowan Han`, `카일 한`, 고정 성씨 `한`.

Name does not lock ethnicity or nationality.

---

# 4. ACT1 EARLY-SERIES STATE (post-D2)

- EP001~006 의도적 무단서. Reading promise = `이 주인공은 일하는 걸 보는 재미가 있다`
- **EP007** D05 mundane primer — 평범한 안전지식, 이상함 없음, **미스터리 음악 금지**
- **EP008~014** 진짜 산업재해 아크가 초반 장르 하중을 진다
- **EP012** D05 professional PLANT — 직업적 이유로만 눈에 띈다
- **EP014** 사고는 진짜 사고였다 **+** 상속 절차 하나만 출처가 없다
- **EP022** REINFORCE · **EP028** 두 번째 bounded payoff
- `ordinary_event_guard: HARD` 유지. EP042는 평범한 다음-업무 상태로 끝난다

---

# 5. STANDING LOCKS

- POV: 주인공 소유 319/410 (77.8%), 등장 386/410, 부재 24/410.
  충돌 시 `POV-OWNERSHIP-REALLOCATION-v0.2` 우선 (47화 목록: authority map §3.1)
- Assets: base 64 / variants 28 / 카탈로그 92 / 실링 96. Reader-facing 용어 19+1, 최대 20
- Violence: `consequence-forward / anatomy-light / sensory-moderate`
- Romance: 루카스↔Mira 3~5%. Act9 새 관계는 H-A 운명 복원이 아니다
- Ending: `+1 / earned cautious hope`. EP406~410 새 미스터리 없음
- HUMAN:1 임신 시계 LOCKED — Act7 개시 촉발, 8+12+18=~38주, EP408 정상 출산.
  **HUMAN 공개 발견이 임신을 촉발하지 않는다**
- Visual Production: `DOC-READY / EMPIRICAL QA OPEN` — 최종 아트 동결 전에만 필요, 집필을 막지 않음

---

# 6. GENERIC CONTINUATION RULE

Generic `진행/이어서` must NOT:
- start prose,
- reopen closed design,
- mass-generate images,
- revive v2 (마렌/아마라/7막/230화) content.

Manuscript Start requires an explicit user instruction naming drafting.

---

# 7. CONTEXT PROTECTION

Before context becomes unreliable, update this file, `docs/current-work-status.md`,
`canon/CANON_STATUS.md` and `docs/manuscript/MANUSCRIPT-STATUS.md`.
Never ask the user to repaste state recoverable from GitHub.
