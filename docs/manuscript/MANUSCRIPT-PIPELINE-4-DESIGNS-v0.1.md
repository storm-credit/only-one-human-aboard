# Manuscript Pipeline — 4 Designs v0.1

Status: `EXECUTION INFRASTRUCTURE / NO PROSE`

Purpose:
EP001 집필이 시작된 뒤 초고/수정본/공식원고가 섞이지 않도록 GitHub 상태와 QA 승격규칙을 설계한다.

Hard requirements:
- Draft ≠ accepted manuscript.
- Canon/Blueprint impact failure must stop promotion.
- A later agent/chat must know exactly which episode is official.
- Git history should preserve revisions without forcing user to paste text.
- 230 episodes should remain manageable.

---

# A — Single File + Frontmatter Status

Path:
`manuscript/act01/EP001.md`

Frontmatter changes:
`DRAFT → QA → ACCEPTED`.

## Strengths
- simplest directory
- one obvious file per episode

## Weaknesses
- another agent may read DRAFT as official prose
- half-finished file exists in canonical-looking path
- failed QA and accepted text share same current location

## Verdict
`REJECT AS BASE`

---

# B — Separate Work / Accepted Trees

Working:
`manuscript/_work/act01/EP001.md`

Official:
`manuscript/accepted/act01/EP001.md`

Status ledger:
`docs/manuscript/MANUSCRIPT-STATUS.md`

Promotion:
Draft in `_work` → episode QA → revisions → copy final to `accepted` → ledger marks ACCEPTED.

## Strengths
- impossible to confuse draft and official by path
- next chat can read accepted only by default
- work can be revised freely
- Git history keeps audit trail

## Weaknesses
- duplicate file temporarily
- promotion requires an extra write

## Verdict
`CURRENT BEST`

---

# C — One Git Branch / PR Per Episode

Every episode drafted on separate branch and merged after QA.

## Strengths
- excellent software-style review history
- clean main branch

## Weaknesses
- 230 PRs is operationally heavy
- fiction revision often spans episode boundaries
- branch/merge overhead becomes project management noise

## Verdict
`TOO HEAVY FOR DEFAULT`

May be useful only for major later rewrite waves.

---

# D — Accepted-Only Git / Draft Outside Repository

Only final prose enters GitHub.
Draft exists in chat/local temporary space.

## Strengths
- clean repository

## Weaknesses
- conversation loss can destroy latest draft
- new chat cannot continue revision from source
- violates project's strong persistence/handoff philosophy

## Verdict
`REJECT`

---

# Recommended Hybrid — MP-H1

Base:
**B Separate Work / Accepted Trees**.

Use Git history instead of creating numbered work copies for every micro-revision.

## Active Paths

### Work
`manuscript/_work/actXX/EPXXX.md`

Contains current working draft only.
Can be overwritten after QA repairs; Git history preserves earlier state.

### Accepted
`manuscript/accepted/actXX/EPXXX.md`

Contains only the latest officially accepted episode text.

### Status
`docs/manuscript/MANUSCRIPT-STATUS.md`

### QA records
`docs/manuscript/qa/EPXXX-QA.md`

Batch QA:
`docs/manuscript/qa/BATCH-EP001-005.md`

Sub-Act QA:
`docs/manuscript/qa/SUBACT-1A.md`

---

# 1. Episode States

Allowed state machine:

`NOT_STARTED`
→ `DRAFT`
→ `QA_REVIEW`
→ either `REVISION_REQUIRED` or `QA_PASS`
→ `ACCEPTED`

Optional later:
`PUBLISHED`

No jump:
`DRAFT → ACCEPTED` without QA.

---

# 2. Promotion Rule

An episode can enter `manuscript/accepted/` only if:

1. Blueprint core choice/consequence/carry preserved.
2. Canon check = PASS.
3. POV/knowledge boundary = PASS.
4. character voice = PASS or repaired.
5. exposition/jargon = PASS or repaired.
6. hook/reward = PASS.
7. anti-AI prose QA = PASS.
8. no unresolved episode P0.

If P0:
- do not promote
- stop manuscript continuation if Canon-impacting
- log change if needed

---

# 3. Accepted Is The Only Prose Authority

When a future chat asks:
`20화까지 써져 있어?`

Official answer uses:
`manuscript/accepted/` + `MANUSCRIPT-STATUS.md`.

Never count `_work` as completed manuscript.

---

# 4. Revision After Acceptance

Minor prose polish preserving Blueprint/Canon:
- update accepted file
- record revision date/reason in status or QA note when meaningful

Structural episode change:
- reopen `_work`
- QA again
- replace accepted only after pass

Canon-impact change:
- STOP
- change-log + relevant Freeze review

---

# 5. Cross-Episode Revision

If an episode repair changes next-carry or prior payoff:
identify affected accepted episodes before edit.

Do not silently fix EP010 by contradicting EP009.

For 2+ accepted episodes changed together:
create a batch revision QA note.

---

# 6. User Rejection

If user says accepted prose is wrong/bad and requests a rewrite:
- accepted version remains historical in Git
- set ledger to `REVISION_REQUIRED`
- create/update `_work`
- do not delete accepted path until replacement passes
- once replacement passes, update accepted file

Thus there is always a last-known accepted version.

---

# 7. Prose Generation Workflow

When user explicitly asks for EPXXX:

1. read Canon authority
2. read Episode Blueprint card
3. read relevant Deep Card if any
4. read POV Map
5. read Protocol v1.1
6. draft to `_work`
7. run Episode QA
8. repair draft
9. rerun failed checks
10. write QA record
11. promote to `accepted`
12. update `MANUSCRIPT-STATUS.md`
13. if episode ends a 5-episode batch/Sub-Act, run corresponding QA

Do all work in current response; do not promise background completion.

---

# 8. File Naming

Zero-padded episode names:
- `EP001.md`
- `EP002.md`
...
- `EP230.md`

Act directories:
- `act01`
- `act02`
...
- `act07`

Avoid title in filename; episode title can live inside file metadata/body and may change more easily than episode identity.

---

# 9. Manuscript Frontmatter

Recommended minimal metadata in work/accepted file:

```yaml
---
episode: EP001
act: 1
sub_act: 1A
status: DRAFT | ACCEPTED
pov: Maren Vale
blueprint: docs/writing-ready/EPISODE-BLUEPRINT-ACT1-v0.1.md
protocol: docs/writing-ready/PROSE-EXECUTION-PROTOCOL-v1.1.md
canon_version: v1
---
```

Do not put hidden future spoilers in public-facing episode title metadata if these files may later be exposed externally.

---

# Verdict

`MP-H1 Separate Work / Accepted Trees = CURRENT RECOMMENDED MANUSCRIPT PIPELINE`

No manuscript prose written.
