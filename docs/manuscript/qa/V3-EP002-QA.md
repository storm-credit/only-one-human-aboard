# V3 EP002 — EPISODE QA RECORD

Episode: **EP002 — 원인은 한 칸 앞에 있다**
Manuscript: `manuscript/v3/accepted/act01/EP002.md`
Date: 2026-08-22
Canon: v3 · POV 루카스 · Zone 올드웍스 서비스 통로 · Clue `NONE`
Drafted by: Codex CLI. Reviewed by: read-only `episode-qa`, blank slate, two independent passes.

# VERDICT

# **PASS — ACCEPTED**

`r1 draft` → over-length → `r1-compressed` → **REPAIR (9 items)** → `r2` → **PASS** → `r3` (three optional planes applied at promotion).

Length: 5,410 chars / 3,429 Hangul (EP001: 5,512 / 3,438). 6 scenes.

---

# 1. PROCESS NOTE — AN ORCHESTRATOR ERROR WORTH RECORDING

The first Codex draft came in at **12,008 chars, 2.2× house length.** The cause was mine: the drafting
brief specified "약 11,000~13,000자, EP001은 12,862자였다" — but **12,862 was a *byte* count, not a
character count.** Korean UTF-8 runs ~3 bytes/char, so the real house length is ~5,500 characters.

Codex followed the instruction correctly. A compression pass with the corrected target recovered it
without quality loss. **Measure Korean length in characters, never `wc -c`/`wc -m` bytes.**

---

# 2. HARD FENCES — ALL PASS

| Fence | Result |
|---|---|
| `Clue: NONE` | PASS. EP001's open two-month step is closed by **approved paperwork** (`벨트 자체 운행은 승인된 변경. 손상 보고 없음.`) — the correct anti-mystery move. R6 strengthens it further: the cause becomes a *daily* routine, the least mysterious possible shape. |
| `ordinary_event_guard: HARD` | PASS |
| Forbidden reveals (regression / branching / substrate / HUMAN:1 / Outer Ark / lineage) | PASS — 0 occurrences |
| Authority limit; no commanding, no policing access | PASS — three separable layers: institutional, credential, physical. The 반장 opens the inspection window on his own initiative. |
| Single POV, close third, no head-hop | PASS |
| `absolute_forbid` — Niko's proposal not mere foolishness | PASS, defended twice on-page: `기술적으로는 좋은 길이었다` / `네 길은 맞아. 접근 근거가 아직 빈칸이야.` |
| Gideon not sage-coded (`influence_only`) | PASS — five lines, all procedural gating, zero maxims. After R4 he is characterized by *response latency* rather than dialogue. |
| **EP007 credit debt unspent** | PASS — **debt increased.** Niko asserts standing, Lukas says nothing. Now visible to the reader, which is the setup EP007 needs. |
| `손도면` not reintroduced | PASS — normalized to `도면`, 0 occurrences |
| M01 구조 크롤러 at BACKGROUND | PASS — absent; 매핑 드론 carries the function |
| New stable terminology labels | **0** |

Blueprint EP002 card: **9/9 fields delivered.**

---

# 3. REPAIRS REQUIRED AT r1 AND APPLIED

| ID | Sev | Defect | Resolution |
|---|---|---|---|
| **R1** | High | **Contradiction with accepted EP001.** EP001 closes on Niko saying `"고쳤네요."`; EP002 opens with the bolts still loose and the crew waiting. Neither reading was supported by either text. | Added `어제 저녁 숫자가 0.11까지 떨어진 건 3구획을 비워둔 값이었다.` — retroactively makes EP001's exchange re-read as Niko misreading a favorable number and Lukas already hedging it. **No amendment to the accepted episode was needed.** |
| **R2** | High | **Narrator aphorism 4 / cap 1.** Partial regression on EP001's core lesson (*the narrator was the weakest character*). | Three converted to behavior; kept only `길게 이으면 보기에는 좋았다. 끊어 그으면 순서가 남았다.` |
| **R3** | High | **Ending device duplicated EP001's** (`dialogue punch + live upstream state`) — same components, order reversed, same Niko→Lukas speaker pair. Carry-constraint (b) breach. | Replaced with **quiet irreversible propagation + physical state**. `괜찮은지는 집에 가면서 보자` cut. |
| R4 | Med | Gideon set an explicit field condition (`내 확인 칸은 사진 뒤에 열어`) that never closed, in an episode whose aesthetic is *fields closing in order*. | Added his confirmation with a timestamp, four minutes after the footage went up. |
| R5 | Med | EP001 planted 배차실 friction **twice** on purpose; EP002 paid it with one offstage summary sentence. | Added the 커피 두 번 빚졌어요 exchange. |
| R6 | Med | EP001 established fretting = months and hypothesized a **single hard event**; EP002 delivers a **permanent schedule change** and nobody notices yesterday's hypothesis was wrong. | Added `"가루는 더 오래됐어. 계단은 두 달 전이고." … "매일이었네."` |
| R7 | Med | Scene 3 ran on schedule pressure alone (C1 §6 marginal-FAIL). | Cured indirectly by R2 + R4. Now marginal-PASS with three pressures. |
| R8 | Low | No amplitude number linking to EP001's 0.42 → 0.11 axis. | `0.38로 튀었다` |
| **R9** | Design | **`flaw_pressure` under-delivered.** Lukas wins every exchange; nobody lands on him. Worse — he executes Gideon's EP001 correction *perfectly*, so at EP002 the flaw meant to break him across nine Acts is **resolving instead of pressuring**. | Extended the documentation-micromanagement beat so control carries a visible cost. |

## Applied at promotion (r3, all optional P2)
- `한 번이 아니라 매일이었네.` → `매일이었네.` — the reviewer's own R6 text had added one more instance of the house cadence.
- `그가 쓴 두 줄이 **그의 이름을 떠나** 다른 사람들의…` → phrase dropped. **The reviewer self-audited a line it had authored** as the most narrator-interpretive phrase in the episode.
- Paragraph break before `어제 저녁 숫자가` for C1 §5 breath.

---

# 4. QUANTITATIVE — RECOUNTED INDEPENDENTLY AT r2

| Pattern | Count / Cap |
|---|---|
| Narrator aphorism | **1 / 1** |
| Negation-reversal 종지 (narration) | **2 / 2** — at cap, zero headroom into EP003 |
| `문제는 ~였다` | 0 / 0 |
| `그건 X가 아니었다 Y였다` | 0 / 0 |
| `그 순간 알았다` | 0 / 0 |
| 3항 rhetorical | 0 / 1 (all enumerations verified diegetic) |
| 일반화 | 1 / 1 |

**Conditional-gnomic tic resolved.** Narration instances 3 → 1. The remaining two are in the protagonist's
own dialogue, i.e. characterization. One narration instance is a signature; three was a crutch.

M1~M10: all PASS. M5 절차 긴장법 is again the strongest law in the episode.

---

# 5. THE UNREQUESTED ADDITION — KEPT

The orchestrator added one enclosed-world texture line unprompted and flagged it for rejection:

> `통로 공기에서는 방청유와 식은 금속 냄새가 났다. 환기가 한 번 돌고 온 냄새였다.`

Reviewer verdict: **keep.** Not narrator intrusion (perceptual, attached to Lukas bracing on the wall),
not ominous (signals *closed volume*, not hidden system), not a fourth aphorism (specific identification,
not generalization), and M2 affirmatively requires it. It reuses two of EP001's three exact nouns —
same nose, same place. The enclosed-world debt now **holds level** instead of increasing.

---

# 6. CRAFT ASSESSMENT

Two repairs did more than repair:
- **R6** converted a logical gap into the episode's best characterization beat.
- **R9** converted a missing flaw into an unpaid debt the reader can watch accruing.
- **R1** retroactively *improved* an accepted episode rather than patching around it.

The `칸` motif is the episode's controlling image and carries zero narrator commentary —
한 칸 줄었다 / 한 칸 앞 / 제 칸 / 빈칸 / 한 칸 후순위 — inverting EP001's
`넌 항상 한 칸 앞을 보고 싶어 하지` into `제 칸은 원인 칸 뒤에 있습니다`. **Do not let a future repair flatten it.**

> Stronger than EP001 on procedure and authority. Weaker on world texture and on the protagonist's
> early personal stake. Both are EP003's job and both are logged.

---

# 7. P2 — CARRY TO BATCH QA (EP001~005)

1. `진단 베이스` (3 uses in its debut) — log as house vocabulary before EP003.
2. `트랜스퍼 댐퍼` — ledger-log or normalize if it recurs past EP002.
3. **`메리디언` / commute-scale world texture debt → EP003 must clear it or it becomes structural.**
4. **M4: Lukas's personal stake arrives ~90% through in both EP001 and EP002. If EP003 also defers it to the final page, it is structural — raise at batch QA.**
5. **Ending-image rotation: EP001 and EP002 both close on cargo passing.** The *device* is correctly rotated and the meaning inverted, so this is craft, not repetition — but **EP003 must not close on a passing cargo or vehicle.**
6. Negation-reversal narration sits at **2/2 with zero headroom** into EP003.
7. Not-X-but-Y has migrated into being the protagonist's default rhetorical mode (~7 dialogue instances). Track, do not repair yet.
8. 반장's register swings from epigram to flat — batch-level voice item; the epigram may belong in 무뇨스's mouth.
9. `기디언 박` full-name reintroduced though already introduced in EP001. Minor tic.
10. Niko's concession is still told rather than shown (`납득보다 계산이 먼저 남은 얼굴이었다`); mitigated by R9 dramatizing the same delta later.
11. **Guard:** the final image is safe from an "ominous silence" reading *only because* `경량 화물이 처음` explains why the deck is quiet. **Never cut that clause.**
