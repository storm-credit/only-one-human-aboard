# CHG-055 — V3 CANON PROMOTION (Option B) + 주인공 이름 확정 + D2 / I-01 / J-01 실행

Date: 2026-08-21
Status: `EXECUTED / OFFICIAL ACTIVE CANON = v3`
Project: 《우주선에는 인간이 한 명뿐이다》

Authorizing input: **explicit user authorization** — Gate A 승격 승인, Gate B 이름 확정, D2 실행 지시,
그리고 I-01 / J-01 을 Act 락으로 이연하지 말고 지금 해소하라는 지시.

Authorizing audit: `docs/qa/V3-FINAL-PRE-MANUSCRIPT-BLIND-SPOT-AUDIT-v1.md` (verdict PATCH).
Decision package: `docs/change-control/V3-CANON-PROMOTION-DECISION-PACKAGE-v0.2.md` — **OPTION B**.

---

# 1. GATE A — v3 CANON PROMOTION

Executed against the package's §9 ten-step checklist.

| # | Step | State |
|---|---|---|
| 1 | `canon/CANON_STATUS.md` → v3 active / v2 historical | DONE |
| 2 | v2→v3 promotion change record referencing final audit | DONE — this file |
| 3 | historical v2 manuscript 10/230 preserved | DONE |
| 4 | active v3 manuscript initialized 0/410 | DONE |
| 5 | `CLAUDE.md` authority routing updated | DONE — full rewrite to v3 |
| 6 | current-work-status / authority-map / handoff updated | DONE |
| 7 | regression: no file claims v2 active for new work except historical records | DONE |
| 8 | regression: no stale v3 design-history file claims active authority | DONE |
| 9 | protagonist name | **APPROVED — 루카스 켈러** (Gate B, below) |
| 10 | do not start prose | HELD — manuscript remains 0/410, NOT STARTED |

## Minimal-mutation principle honored
Per package §5, **no mass rename** was performed. `CANDIDATE` suffixes remain in filenames;
authority is asserted by `CANON_STATUS.md` §2 and `CLAUDE.md` §0, not by filename.

## v2 treatment
`FROZEN HISTORICAL EDITION / NOT ACTIVE FOR NEW v3 MANUSCRIPT`.
Nothing deleted: v2 bibles, Amendment A, v2 blueprints, v2 Obsidian graph, v2 QA and the
accepted EP001~010 prose all remain. v2 reveal locks (EP056/058/066/068/075) no longer
constrain v3. Hybrid v3-world + v2-230 structure remains rejected.

---

# 2. GATE B — PROTAGONIST FINAL NAME

# **루카스 켈러 / Lukas Keller**

Reader-facing call-name: **`루카스`** only. Do not alternate `루카스 / 켈러` for style.

## Why this and not the prior leading candidate
The prior leading C2 candidate was `루카스 베르너`. The user challenged it on the grounds that
**베르너(Werner) is both a given name and a surname** in German, so the full name reads as two
given names. That objection is correct, and re-checking the repo's own scoring made the case stronger:

- `V3-PROTAGONIST-NAME-DEEP-BRAINSTORM-v0.2.md` ranks `루카스 베르너` **4th at 32/35 with a `HERO` flag**
  ("slightly more lead-coded") — it was never the top-scored option.
- `V3-PROTAGONIST-NAME-HOSTILE-SOUND-QA-v0.1.md` scores `루카스` **4/5** with
  "stronger conventional male-lead coloration".
- The 1st-ranked `다니엘 마레크` (34/35) is on the handoff's `Do NOT revive` list.
- `켈러 / Keller` is a **surname-only** German name, removing the ambiguity entirely.
- `마레크`, `로렌츠`, `베르너` all carry the same given-name/surname ambiguity; `켈러`, `나바로`,
  `노박` do not.

The user selected `루카스 켈러`: retains the preferred call-name `루카스` while replacing the
ambiguous surname with an unambiguous one.

## Collision check
- `켈러 / Keller` was previously **unused** anywhere in canon or design docs — no collision.
- Against core cast surnames (Solano, Adebayo, Chen, Mbeki, Noor, Park, Osman, Reyes, Kouri,
  Serrin, Dae, Kalev): the only near-neighbour is `Kalev`, and both names surface rarely in prose
  (Arun is called by given name; the protagonist is called `루카스`). Risk assessed LOW.
- Given name `루카스` collides with no cast member.

## Household surname recalibration
`베르너 → 켈러` for the protagonist's paternal line:
- 마르틴 켈러 (부, 68)
- 클라라 켈러 (누나, 41)

Unchanged, different households by design: 나디아 소토 (모), 사미르 코스타 (매형), 에바 코스타 (조카).
Family **architecture** is unchanged; only surface labels moved.

## Placeholder substitution
`[주인공/TBD]` → `루카스` across the 410 episode blueprints, 410 CTX routers and 410 Deep sidecars.
Mechanical, verified by count.

---

# 3. D2 — 미스터리 실 전진 배치 (audit C-03, P1)

Opened in CHG-051, never executed. The audit found v3 had moved the ignition point *later* than the
v2 line that already produced the recorded `재미없다` ×2 / `장르가 다르다` ×1 reader failure.

Executed **Design A** — the smallest fix, and the one that matches the original D2 candidate spec
(`primer → 1A EP005~009`, `anomaly → early 1B`). Same D-chain element (D05), same accident cause,
no new episode, no change to Act1 length or Act boundaries.

| Episode | Before | After |
|---|---|---|
| EP007 | `Clue: NONE` | **D05 mundane primer** — old emergency-bracing checklist as ordinary safety knowledge |
| EP012 | `Clue: NONE` | **D05 professional PLANT** — an inherited brace step proves useful under live damage |
| EP014 | ordinary-accident payoff | ordinary-accident payoff **+ D05 local bounded payoff** — the step has no origin |
| EP021 | "review an old safety procedure" | "review **another** old safety procedure" |
| EP022 | D05 **PLANT** (first) | D05 **PLANT (second procedure family)** — no longer the first plant |
| EP028 | D05 local bounded payoff | D05 **second** local bounded payoff |

Result: first primer **EP022 → EP007**, first genuine professional anomaly **EP022 → EP012**,
first bounded payoff **EP028 → EP014**. Now earlier than the v2 EP012 primer / EP017 anomaly.

## Guards preserved
- Act1 reveal fence intact: no objective confirmation of regression / branching / substrate / HUMAN:1 / Outer Ark.
- `ordinary_event_guard: HARD` intact — the EP008~014 accident stays a genuine ordinary accident.
  EP014's anti-mystery payoff is retained, not replaced.
- No mystery music: the anomaly is administrative and is noticed for professional reasons only.
- Reveal windows unviolated: D05 `PLANT — Act1~3`, `TRIGGER — Act5~6`, `FINAL PAYOFF — Act7` unchanged.
  D03 remains `Act1 EP029~042`. D02 C4 trigger remains EP093~094.
- EP001~006 remain deliberately clue-free; EP008~014 carries the early genre load.
- EP022 is labelled a **second PLANT**, not a REINFORCE. The ledger's D05 `REINFORCE` window is
  `Act3/4`, while its `PLANT — Act1~3` entry explicitly allows `one or two procedures`. The first
  draft of this patch labelled EP022 `REINFORCE` and Codex correctly rejected it as a window
  violation; it was corrected before merge.

## Ledger vocabulary clarified
The D05 ledger enumerates `PLANT / REINFORCE / TRIGGER / PARTIAL PAYOFF / FINAL PAYOFF / AFTERSHOCK`.
It has no `local bounded payoff` stage, so EP014/EP028 are now labelled **local bounded reward
(not a ledger payoff)** and state explicitly that D05 `PARTIAL/FINAL PAYOFF` remains untouched in its
Act7 window. EP028 carried this pattern before the change; EP014 now mirrors it. No ledger stage is
consumed inside Act1.

## Pre-existing issue noted, deliberately NOT changed
`EP023` has carried `Clue: D05 REINFORCE` since before this change, which sits outside the ledger's
`REINFORCE — Act3/4` window. It is a **pre-existing** blueprint/ledger mismatch, not introduced here,
and correcting it would require its own downstream regression. Recorded for a future targeted pass.

---

# 4. I-01 — EP280~290 반복 공식 (audit P1)

The audit confirmed EP281/284/286/287/288/289/290 repeat one move — an inherited rule/record whose
origin cannot be traced — varied only by domain, with End Turns repeatedly shaped as
"another domain shows the same pattern".

Smallest fix: **two episodes re-tasked**, Act7 length unchanged, D05 escalation intact
(EP284/286/287/289/294 still carry it).

- **EP288** — from "apply the inherited safeguard" to a **physical resource/relationship payoff**:
  following the rule would keep a theoretical margin but leave a neighborhood service offline;
  he and Niko test a bounded modification and physically restore the route. Niko owns the field check.
  End Turn no longer points at "another domain".
- **EP290** — from another record-origin survey to **asset-linked physical evidence**:
  the preservation record only resolves when paired with a live maintenance asset ID still drawing
  protected power. Hands off cleanly to EP291's protected-load evidence.

Cited compression authority: `V3-410-EPISODE-DENSITY-MAP-v0.2.md` Act7 B39~B40 note.

---

# 5. J-01 — Act9 gestation clock (audit P2)

**This was a synchronization defect, not an open design question.** The numbers were already
resolved and the wording patch already prescribed; the blueprints had simply never been updated.

Pre-existing authorities:
- `docs/prewriting-v3/V3-FULL-SERIES-TIMELINE-v0.1.md` — "Combined Act7~9 working center: **8 + 12 + 18 = 38 weeks**",
  and final-approach window opens at Act7 opening ~38 weeks before the birth milestone.
- `docs/qa/V3-HUMAN1-MEDICAL-DEVELOPMENTAL-PLAUSIBILITY-PASS-v0.1.md` §6 — ~38-week
  post-fertilization-class interval; §7 **"Act8 blueprint wording patch"**; §8 Act9 patch.

Locked: option (a), **actual birth at EP408**, no accelerated biology, no fallback milestone needed.

| File | Change |
|---|---|
| Act9 working time | `weeks to several months / unresolved` → **~18 weeks; clock LOCKED**, with the 8+12+18=38 derivation and the trigger rule |
| EP332 | biostasis phrasing → **cryopreserved early-stage continuity with validated viability**; gestational system is a separate later phase |
| EP359 | "in early developmental arrest" → **gestation already began at the Act7-opening mission-clock threshold**, underway for weeks before anyone knew its meaning |
| EP360 | "control of activation/gestation" → control of **ongoing** gestation, birth timing, guardianship |
| EP361 | generic readiness work → **ex vivo gestation integrity / environment-analog support** |
| EP406 | "gestation timeline-dependent" → **Act9 week ~18**, approaching the ~38-week interval |
| EP407 | milestone "occurs" → **birth begins** off-POV under ordinary medical-team care |
| EP408 | "timeline-dependent milestone" → **~38-week interval complete; birth / first neonatal record** |
| Act9 hostile QA | **Timeline gate CLOSED** with all three items resolved |

## Guards preserved
- `public discovery of HUMAN does not trigger gestation` — mission-clock + medical viability protocol does.
  Characters do not "switch on the baby" after discovering HUMAN.
- EP408 keeps ordinary medical/caregiver external POV, no infant interior POV, no ceremony,
  no miraculous cognition. HUMAN:1 remains de-collectified.
- Exact calendar date and medical week remain C2.
- Far-future ectogenesis remains an explicitly declared speculative assumption, not current science.

---

# 7. VERIFICATION RECORD — READ THIS BEFORE TRUSTING §1~§6

Independent adversarial verification was run with Codex CLI. **The patch was rejected three times
before the substantive content passed.** What Codex caught, in order:

| Round | Verdict | Caught |
|---|---|---|
| 1 | REJECTED | Active authority files still claimed v2 official / v3 not canon; promoted Bibles still said protagonist TBD; authority map still used `베르너` family names; active C2 docs still worded as candidate; **EP022 labelled `REINFORCE`, violating the ledger's `REINFORCE — Act3/4` window**; Act9 QA gate both closed and still listed unresolved. |
| 2 | REJECTED | EP022 fixed but its sidecar still said `first soft anomaly`; EP007/EP012 sidecars gained D05 while keeping stale `no clue/collectible` retrieval lanes and a `mystery hint` FORBID; EP014/EP028 `local bounded payoff` wording readable as a ledger-window violation; several pre-promotion phrases still live in `ACT_BIBLE-v3.2`, `CHARACTER_BIBLE-v3.1`, authority map, asset roster, `ENTITY-C01`, density map. |
| 3 | REJECTED | Remaining stale wording in the C2 closure doc, asset overlay, language addendum, authority map gate line, and **all nine active v3 World addenda still carrying `NOT CANON` status headers**. |
| 4 | **NOT RUN** | Codex hit its account usage limit before the fourth pass could execute. |

## Honest limitation
Round 3's fixes — status-header and wording corrections only, listed above — were verified by the
orchestrator with the same mechanical checks Codex used, **not by an independent adversarial pass.**
The substantive content (the D2 design, the 47-episode POV set, D05 ledger-window compatibility,
Deep sidecar/card consistency, graph integrity, scope containment) *was* Codex-verified in rounds 1~3.

Self-verified results at merge time:
- previously-open items 1~5: all clear;
- no active file claims v2 official / v3 candidate / protagonist TBD;
- `deep_context_integrity.py`: 410 files, 0 errors, 0 warnings;
- CTX 410 / DEEP 410 / episode cards 410;
- broken wikilinks repo-wide: **0** of 594 distinct targets;
- v2 canon, `canon/v2/`, `docs/writing-ready/` and `manuscript/` files modified: **0**;
- Act1 D05 chain coherent; EP023 remains the only pre-existing ledger mismatch, documented above.

**Recommended follow-up:** re-run a Codex adversarial pass over this commit when quota resets, focused
on the round-3 wording changes. Nothing in that round altered story content, so this is a hygiene
check rather than a correctness risk.

---

# 6. SCOPE CONTROL

Changed: authority/status/routing docs, `CLAUDE.md`, four Act blueprints (Act1, Act7, Act8, Act9),
Act9 hostile QA, name placeholders, and this record.

**Not changed:** the 9-Act / 410-episode structure, Act boundaries, episode counts, POV ownership
totals, the reveal ledger, the ontology, the character architecture, the asset roster, the C2
terminology budget, or any v2 file.

**No prose was drafted.** Active v3 manuscript remains **0 / 410**.

Remaining gate: **explicit user Manuscript Start instruction.**
