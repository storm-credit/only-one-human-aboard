# MANUSCRIPT PIPELINE v1

Status: `LOCKED EXECUTION INFRASTRUCTURE — 2026-08-17`

Selected:
# `MP-H1R — Separate Work / Accepted Trees + QA Ledger`

Evidence:
- `MANUSCRIPT-PIPELINE-4-DESIGNS-v0.1.md`
- `docs/qa/MANUSCRIPT-PIPELINE-RED-TEAM-v1.md`
- blocking P0 = 0

---

# 1. Terminology

## Canon
World / Character / Act truth authority.

## Work Draft
Current prose being drafted/repaired.
Not official manuscript.

## Accepted Manuscript
Current official prose realization that passed project QA.
May later be revised without reopening Canon if facts/functions stay unchanged.

---

# 2. Paths

**Two editions live side by side. The v2 tree is frozen; never write into it.**

## Active — v3 (9 Acts / 410 episodes)
- Work: `manuscript/v3/_work/actXX/EPXXX.md`
- Accepted: `manuscript/v3/accepted/actXX/EPXXX.md`
- Episode QA: `docs/manuscript/qa/V3-EPXXX-QA.md`

## Frozen — v2 (7 Acts / 230 episodes)
- Work: `manuscript/_work/actXX/EPXXX.md`
- Accepted: `manuscript/accepted/actXX/EPXXX.md`
- Episode QA: `docs/manuscript/qa/EPXXX-QA.md`

Reason for the split: both editions number episodes from EP001, so a shared tree would have
v3 EP001 overwrite the accepted v2 EP001. v2 files were **not moved** — moving them would break
existing QA and change-record references. The v3 line simply gets its own subtree (CHG-055).

## Status Ledger (shared, both lines)
`docs/manuscript/MANUSCRIPT-STATUS.md`

# 2.1 회차 분량 — 하한만 (2026-08-22 작가 결정)

# **하한 5,500자 · 상한 없음.**

Python `len()`, 본문만. **`wc -c` / `wc -m`은 바이트를 보고하므로 쓰지 마라.**
하한 미달은 결함, 초과는 결함이 아니다. **길이를 이유로 장면을 자르지 마라.**
정본 규정은 `docs/manuscript/MANUSCRIPT-STATUS.md` 상단 참조.

## Batch QA
`docs/manuscript/qa/BATCH-EPXXX-XXX.md`

## Sub-Act QA
`docs/manuscript/qa/SUBACT-*.md`

Draft path never counts as completed manuscript.

---

# 3. State Machine

`NOT_STARTED`
→ `DRAFT`
→ `QA_REVIEW`
→ `REVISION_REQUIRED` or `QA_PASS`
→ `ACCEPTED`

Optional later:
`PUBLISHED`.

Special:
`CANON_REVIEW` if draft reveals a possible Canon-level blocker.
`RECHECK_REQUIRED` if an upstream accepted revision may affect this episode.

---

# 4. Default User Request Workflow

If user explicitly says `EP001 써 / 1화 써 / 본문 시작`:

1. read current Canon authority
2. read Episode Blueprint
3. read Deep Card if relevant
4. read execution POV map
5. read `PROSE-EXECUTION-PROTOCOL-v1.1.md`
6. write current draft to `_work`
7. set ledger `DRAFT`
8. run Episode QA
9. repair all hard failures
10. rerun relevant QA
11. write QA record
12. if hard checks all pass, write final to `accepted`
13. set ledger `ACCEPTED`
14. run batch/Sub-Act QA if boundary reached

Perform in current response; no background promise.

If user explicitly requests rough draft only:
stop at DRAFT and do not promote automatically.

---

# 5. Accepted Promotion Requirements

All must pass:

## Blueprint
- immediate episode function preserved
- primary choice preserved
- irreversible consequence preserved
- Next Carry preserved

## Canon
- no silent new world/story rule
- no forbidden technology/authority

## POV
- correct mapped POV unless approved local change
- one POV only
- knowledge boundary intact

## Character
- voice/action consistent
- no core-flaw shortcut

## Prose
- no explanation-only block that should be dramatized
- jargon load manageable
- dialogue not perfect symmetric debate
- opening/hook functions work

## Series
- no accidental payoff/reveal timing shift
- no contradiction with accepted prior episodes

No unresolved hard failure / P0.

---

# 6. QA Outcome Labels

Every Episode QA ends with exactly one:

### `PASS`
Eligible for Accepted promotion.

### `REPAIR`
Local prose/scene repair required; Canon intact.

### `BLOCK`
Canon/Blueprint/major dependency issue; do not continue downstream prose until resolved.

P1 warnings may remain after PASS only if explicitly logged for batch QA.

---

# 7. Revision After Acceptance

When user or QA requests rewrite:

1. keep existing accepted file as current official version
2. set ledger `REVISION_REQUIRED`
3. create/update `_work`
4. QA revised draft
5. if pass, replace accepted file using current SHA
6. ledger returns `ACCEPTED`

Git history preserves previous accepted text.

Never delete the last accepted version merely because a rewrite has started.

---

# 8. Cross-Episode Dependency

If an accepted revision changes:
- end hook
- Next Carry
- fact timing
- relationship baseline
- location/time bridge
- foreshadow/payoff transaction

then identify downstream accepted episodes.

Mark affected files/ledger:
`RECHECK_REQUIRED`.

Run batch/carry QA before replacing downstream prose.

---

# 9. Canon Impact

If prose appears to require changing:
- Seed/Reconstruction/physics/law
- core family/origin
- Reveal truth/timing
- Act order
- ending architecture
- Amara authority

STOP.
Do not solve with a sentence-level patch.

Use project change-control process and reopen Freeze only if required.

---

# 10. Frontmatter

Recommended:

```yaml
---
episode: EP001
act: 1
sub_act: 1A
status: DRAFT
pov: Maren Vale
blueprint: docs/writing-ready/EPISODE-BLUEPRINT-ACT1-v0.1.md
protocol: docs/writing-ready/PROSE-EXECUTION-PROTOCOL-v1.1.md
canon_version: v1
---
```

Accepted copy uses:
`status: ACCEPTED`.

Do not place unrevealed spoiler labels in episode title metadata.

---

# 11. File Naming

Episode:
`EP001.md` ... `EP230.md`.

Act folders:
`act01` ... `act07`.

File identity follows episode number, not episode title.
Episode title may change without path migration.

---

# 12. Git Safety

Before updating any existing work/accepted/status file:
- fetch latest file/SHA
- do not overwrite stale SHA
- if conflict, re-read and merge intentionally

Do not assume the current chat has the latest prose if Git says otherwise.

---

# 13. Completion Counting

Official completion count = episodes that:
1. exist under `manuscript/accepted/`
2. are `ACCEPTED` in `MANUSCRIPT-STATUS.md`

`_work` does not count.

When asked `20화까지 있나?`, check accepted files/ledger, not chat memory.

---

# 14. Current State

No manuscript has been explicitly requested or created yet.

Accepted:
**0 / 230**

Work Draft:
**0**

Next eligible episode:
**EP001**

EP001 may begin only on explicit user request.
