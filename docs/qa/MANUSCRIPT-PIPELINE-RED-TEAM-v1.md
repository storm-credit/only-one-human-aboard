# Manuscript Pipeline Red Team v1

Status: `EXECUTION INFRASTRUCTURE QA / NO PROSE`

Target:
`MP-H1 Separate Work / Accepted Trees`

---

# RT-01 — Does `ACCEPTED` imply user personally approved every sentence?

## Risk
The system may internally QA an episode and call it accepted even if user later dislikes style.

## Repair
Define:
`ACCEPTED = current official manuscript version that passed project QA`.

It does NOT mean immutable or permanently user-approved.
User rewrite request reopens episode to `REVISION_REQUIRED`.
Git preserves prior accepted version.

Verdict: `PASS`.

---

# RT-02 — What if work is interrupted after draft but before QA?

`_work` exists; accepted path remains absent/old.
Status ledger must say DRAFT or QA_REVIEW.

Next chat can recover exact working text without treating it as official.

Verdict: `PASS STRONG`.

---

# RT-03 — What if QA finds Canon P0?

Do NOT repair by inventing a prose workaround.

- leave accepted untouched
- mark work `REVISION_REQUIRED / CANON_REVIEW`
- stop drafting later episodes if dependency is blocking
- update change-log if Canon change is proposed

Verdict: `PASS`.

---

# RT-04 — Do we need numbered draft files for each revision?

No.
Git history already versions `_work/EPXXX.md`.
Creating `v0.1/v0.2/v0.3` files would clutter 230 episodes.

Use one current work file + Git commits.

Verdict: `PASS`.

---

# RT-05 — Should accepted file be deleted while rewrite is happening?

No.
Last-known accepted version remains available until replacement passes.

Ledger may say:
`REVISION_REQUIRED (accepted version still current until replacement)`.

This prevents periods with no official text.

Verdict: `PASS STRONG`.

---

# RT-06 — What if user asks for a deliberately rough draft only?

Then stop at `_work` and DRAFT state.
Do not auto-promote if user explicitly requested rough/unreviewed text only.

Default when user asks `1화 써`:
perform draft → QA → repair → accepted within the same response if possible.

Verdict: `PASS`.

---

# RT-07 — Can QA become ceremonial rubber stamp?

Risk is high once many episodes exist.

Repair:
Episode QA must output explicit:
- PASS / REPAIR / BLOCK
- concrete evidence for each failed item
- repair actions performed

Accepted promotion requires all hard checks pass.
P1 warnings can remain only if they are logged for batch QA and do not break episode function.

Verdict: `PASS WITH HARD QA FORMAT`.

---

# RT-08 — Does committing draft prose to main pollute repository?

It adds work files but preserves continuity, which is a higher priority in this project.
Path prefix `_work` makes state explicit.

If repository size later becomes a problem, old work files can be removed after acceptance because Git history retains them. Do not optimize prematurely.

Verdict: `PASS`.

---

# RT-09 — How does completion count work?

Only episodes present in:
`manuscript/accepted/`
and marked ACCEPTED in ledger count as completed.

`_work` never counts.

Verdict: `PASS`.

---

# RT-10 — What if accepted EP010 revision affects EP011~015?

Before replacement:
- identify downstream accepted dependencies
- mark affected episodes `RECHECK_REQUIRED` if needed
- run batch/carry QA

Do not silently repair only EP010 if its Next Carry changed.

Verdict: `PASS WITH DEPENDENCY RULE`.

---

# RT-11 — Should accepted manuscript be called Canon?

Avoid confusion.
World/Character/Act `Canon` and manuscript official version are different layers.

Terminology:
- **Canon** = world/story authority
- **Accepted Manuscript** = current official prose realization

Accepted prose can be revised without reopening Canon if underlying facts/functions stay fixed.

Verdict: `PASS`.

---

# RT-12 — Concurrent chat/write conflict

Every GitHub update must fetch current SHA first.
Do not overwrite a changed work/accepted file from stale SHA.
If conflict occurs, re-read and merge intentionally.

Verdict: `PASS`.

---

# Final Repair Set — MP-H1R

1. separate `_work` and `accepted` paths
2. ledger is official completion index
3. accepted means QA-official, not immutable user approval
4. last accepted remains while rewrite is in progress
5. draft-only request stops before promotion
6. hard QA result must be explicit
7. downstream carry changes trigger recheck
8. Canon vs Accepted Manuscript terminology stays separate
9. Git SHA conflict protection mandatory

Blocking P0:
**0**

Verdict:
# `MP-H1R = PASS`

Recommended next:
- lock `MANUSCRIPT-PIPELINE-v1.md`
- create manuscript status ledger
- create episode/batch/Sub-Act QA templates
