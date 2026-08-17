# Encyclopedic Canon v2 Architecture — 4 Designs

Status: `CANON CONSOLIDATION DESIGN / NO PROSE`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

Goal:
Promote the completed A~I Deep Design into a clean authoritative Canon v2 without destroying the frozen v1 baseline or creating a second contradictory shadow encyclopedia.

---

# Design A — One Giant WORLD_BIBLE-v2.md

Structure:
Everything—society, culture, infrastructure, history, destination, characters, story, numbers—goes into one enormous file.

Strengths:
- one file to search,
- simple authority label.

Weaknesses:
- merge conflict risk,
- hard to know who owns a rule,
- encourages whole-file context loading,
- character/story facts mix with physical-world facts,
- difficult to mark elastic detail precisely.

Verdict:
`REJECT`.

---

# Design B — Overwrite v1 Files In Place

Structure:
Replace:
- WORLD_BIBLE-v1.md,
- CHARACTER_BIBLE-v1.md,
- ACT_BIBLE-v1.md
with expanded content or rename them.

Strengths:
- fewer files,
- old workflow paths continue.

Weaknesses:
- destroys clean regression baseline,
- makes it hard to audit what changed,
- old Blueprint references become ambiguous,
- rollback is unnecessarily difficult.

Verdict:
`REJECT`.

---

# Design C — Modular Canon v2 Authority Set

Structure:

```text
canon/v2/
├─ 00-CANON-v2-INDEX.md
├─ CANON-v2-PROMOTION-LEDGER.md
├─ CANON-v2-ELASTIC-REGISTRY.md
├─ WORLD-CORE-v2.md
├─ SOCIETY-v2.md
├─ CULTURE-DAILY-LIFE-v2.md
├─ INFRASTRUCTURE-OPERATIONS-v2.md
├─ HISTORY-v2.md
├─ DESTINATION-ARRIVAL-v2.md
├─ CHARACTERS-v2.md
├─ STORY-ARCHITECTURE-v2.md
└─ QUANTITATIVE-BANDS-v2.md
```

Authority:
- the Index defines order/conflict rules,
- each domain has one Canon owner,
- Promotion Ledger shows where each v2 rule came from,
- Elastic Registry states what remains intentionally open,
- v1 stays immutable historical baseline.

Strengths:
- reference-grade,
- Obsidian/agent friendly,
- small-context retrieval,
- explicit ownership,
- easy regression/change control,
- no need to load all Canon for one scene.

Weaknesses:
- more files,
- requires strict index discipline.

Verdict:
**`SELECTED — CANON-H1`**.

---

# Design D — Make The Reference Atlas Itself Canon

Structure:
Promote `docs/reference-atlas/*` to canonical authority.

Strengths:
- already compact and linked.

Weaknesses:
- Atlas intentionally contains navigation summaries and C2 candidates,
- it was specifically designed not to become Shadow Canon,
- would blur source versus summary,
- author-facing routing pages are not equivalent to normative rules.

Verdict:
`REJECT`.

---

# Selected Architecture — CANON-H1

## Authority order after Freeze

1. `canon/v2/00-CANON-v2-INDEX.md`
2. the relevant `canon/v2/*-v2.md` domain owner
3. locked active story execution authorities where explicitly delegated:
   - active Episode Blueprint,
   - locked POV Map,
   - M1 Time/Age,
   - applicable locked Deep Card
4. v2 Elastic Registry for intentionally open values
5. Reference Atlas for navigation only
6. design-v2 source documents for rationale/examples only
7. v1 Canon as historical baseline/superseded authority where v2 explicitly replaces it

Before final Freeze, v1 remains superior to v2 drafts where a contradiction is unresolved.

---

# Core Promotion Rule

A design fact enters Canon v2 only if it is one of:
- a v1 lock preserved unchanged,
- a Package A~I preferred model that passed Red Team,
- a Q1~Q7 provisional band required for repeat consistency,
- an explicit story/character lock already enforced by 230-episode architecture.

Do NOT Canonize merely because a detail exists in:
- an illustrative example,
- a 4-design rejected option,
- an Atlas summary,
- a sample YAML device note,
- an old superseded Blueprint,
- a one-off random-scene test.

---

# Canon Fact Status

Every v2 fact should behave as one of:

## LOCKED
Changing it requires formal change control + impact regression.

## BOUNDED
A range/model is Canon; exact value inside the range can remain elastic.

## DELEGATED
The Canon deliberately delegates exact truth to another locked authority, e.g. episode POV/time.

## ELASTIC
Safe scene-level choice inside stated constraints.

## FORBIDDEN
Explicitly rejected direction that cannot re-enter silently.

---

# Duplication Rule

Facts may be summarized in more than one file for navigation, but only one domain file owns them.

Example:
- exact destination atmosphere owner = `DESTINATION-ARRIVAL-v2.md` / quantitative band reference,
- `WORLD-CORE-v2.md` may only summarize `low-O2 near-Earth-pressure settlement world`.

If summaries disagree, owner wins.

---

# v1 Preservation Rule

Existing:
- `canon/WORLD_BIBLE-v1.md`
- `canon/CHARACTER_BIBLE-v1.md`
- `canon/ACT_BIBLE-v1.md`

remain unchanged as the audited v1 baseline.

They are not deleted or rewritten during v2 consolidation.

Final v2 Index will state which v1 authorities are superseded for new work after Freeze.

---

# Promotion Sequence

1. create v2 Index / Promotion Ledger / Elastic Registry,
2. promote World Core hard locks,
3. promote Society/Culture/Infrastructure/History/Destination,
4. promote Character Encyclopedia locks,
5. promote Story Architecture delegation and reveal fences,
6. promote Q1~Q7 quantitative bands,
7. run v1→v2 contradiction regression,
8. run EP001~230 regression,
9. run random-scene regression against Canon v2 only,
10. update status files,
11. only then mark `ENCYCLOPEDIC CANON FREEZE v2 = PASSED`.

---

# Decision

Use **CANON-H1 — Modular Canon v2 Authority Set**.

This preserves the user's intended workflow:
**deep design first → reference-grade setting bible → Canon Freeze → only then prose.**
