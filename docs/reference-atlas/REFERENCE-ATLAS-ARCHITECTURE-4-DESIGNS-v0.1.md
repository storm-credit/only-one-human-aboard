# Reference Atlas Architecture — 4 Designs v0.1

Status: `PACKAGE H DESIGN COMPARISON / PRE-PROSE / NOT CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. Problem

Packages A~G now contain strong structural candidates, but the repository is large enough that a human/agent can make a new kind of error:

> finding an old Markdown sentence is mistaken for finding current truth.

Package H must make the world **navigable without becoming a fourth Canon Bible**.

It must answer quickly:
- What is Canon v1?
- What is a v2 candidate?
- What is Controlled Elastic?
- What is implementation detail?
- What is superseded/rejected?
- Which file actually owns the fact?
- Which neighboring systems does a fact depend on?
- Which episode/context is allowed to know it?

Hard constraint:
Reference Atlas may summarize and link; it may not silently promote candidates or resurrect superseded concepts.

---

# 1. Design A — Monolithic Encyclopedia

## Structure
One giant `REFERENCE-BIBLE.md` containing:
- glossary,
- institutions,
- timelines,
- maps,
- characters,
- tech,
- objects,
- episode index.

## Strength
- easy Ctrl+F
- one file for a human
- easy export/print.

## Failure Modes
- duplicates thousands of facts,
- becomes stale immediately,
- silently competes with Canon/Blueprints,
- diff/review becomes difficult,
- agents may treat summary prose as highest authority.

## Verdict
`REJECT AS PRIMARY`

May later export a generated read-only compendium, but it must never be hand-maintained authority.

---

# 2. Design B — Pure Obsidian Graph

## Structure
Hundreds of small linked notes:
- one term,
- one place,
- one institution,
- one object,
- one character,
- one rule per note.

## Strength
- excellent graph navigation,
- local context is small,
- good backlink discovery.

## Failure Modes
- too many nodes before stable naming,
- status/authority is visually inconsistent,
- graph can become decorative spaghetti,
- users must click repeatedly to answer simple questions,
- broken links can hide supersession.

## Verdict
`USE AS SECONDARY NAVIGATION, NOT SOLE ARCHITECTURE`

---

# 3. Design C — Human MOC + Source-Linked Reference Tables + Authority Registry

## Structure
A small set of human-readable atlas pages:
- Master MOC
- Glossary
- Institution Authority Matrix
- Civic Map
- Engineering Overlay
- Master Timeline
- Technology Dependency Matrix
- Life-Cycle Flow
- Authority/Elastic Registry
- Destination Atlas
- Character Network
- Material Culture Atlas
- Episode Context Index

Every row/entry carries or links to:
- `status`
- `authority`
- `scope`
- `dependencies`
- `supersedes/superseded_by` when relevant.

## Strength
- human readable,
- machine parsable enough with Markdown/YAML/table conventions,
- source authority remains explicit,
- supports Obsidian without requiring plugins,
- answers common questions in one or two hops,
- low duplication if summaries are short.

## Failure Modes
- tables can still become stale,
- temptation to put too much prose in Atlas.

## Guardrail
Atlas entry must be a **locator/constraint summary**, not a replacement explanation.
If meaning depends on nuance, link to owner document.

## Verdict
`CURRENT BEST BASE`

---

# 4. Design D — Database/YAML-First Canon Registry

## Structure
Everything encoded as structured records:
```yaml
id:
type:
status:
authority:
depends_on:
supersedes:
value:
```
Generated Markdown provides human views.

## Strength
- strongest programmatic validation,
- excellent for future agents/CI,
- easy consistency queries.

## Failure Modes
- implementation-heavy now,
- schema design can consume more effort than story design,
- prose nuance does not fit cleanly,
- user explicitly wants design completed before tooling implementation.

## Verdict
`FUTURE IMPLEMENTATION OPTION`

Use a small stable metadata vocabulary now; do not build a database yet.

---

# 5. Selected Hybrid — REF-H1

## Name
**`REF-H1 — Human-Readable MOC + Source-Linked Atlas Tables + Authority/Elastic Registry + Optional Structured Metadata`**

## Principle
**Atlas tells you where truth lives; it does not become the truth.**

## Required Layers

### H1. Human Navigation
`00-REFERENCE-MOC.md`

### H2. Semantic Lookup
`GLOSSARY.md`

### H3. Power / Institution Lookup
`INSTITUTION-AUTHORITY-MATRIX.md`

### H4. Place Lookup
- `MERIDIAN-CIVIC-MAP.md`
- `MERIDIAN-ENGINEERING-OVERLAY.md`

### H5. Time Lookup
`MASTER-TIMELINE-450Y-14Y-ARRIVAL.md`

### H6. System Dependency Lookup
`TECH-DEPENDENCY-MATRIX.md`

### H7. Ordinary-Life Lookup
`LIFE-CYCLE-FLOW.md`

### H8. Status / Supersession Lookup
`AUTHORITY-ELASTIC-REGISTRY.md`

### H9. Destination Lookup
`DESTINATION-SYSTEM-ATLAS.md`

### H10. People Lookup
`CHARACTER-SOCIAL-NETWORK.md`

### H11. Object Lookup
`MATERIAL-CULTURE-ATLAS.md`

### H12. Story Retrieval Lookup
`EPISODE-CONTEXT-INDEX.md`

---

# 6. Stable Status Vocabulary

Atlas uses only:

- `CANON-V1` — current locked Canon.
- `LOCKED-STORY` — locked Act/Blueprint/POV/M1 execution authority, not world Canon.
- `V2-CANDIDATE` — structurally passed candidate awaiting v2 Freeze.
- `C2-ELASTIC` — bounded range/detail intentionally open.
- `IMPLEMENTATION` — tooling/file-splitting/UI detail, not story truth.
- `SUPERSEDED` — retained for history; must not be used as current truth.
- `REJECTED` — intentionally excluded design.
- `FORBIDDEN` — hard anti-drift rule.

No Atlas page may invent a status synonym.

---

# 7. Authority Link Rule

Every consequential Atlas entry should identify one of:
- Canon owner,
- candidate Bible owner,
- locked Blueprint/POV/M1 owner,
- explicit QA/supersession owner.

If no authority can be named:
**the entry must be omitted or labeled unresolved rather than guessed.**

---

# 8. Supersession Rule

Old files remain searchable for design history.
Therefore the Atlas must explicitly flag high-risk obsolete concepts, including:
- exact-one Natural-Origin preservation protocol,
- adult-machine-substrate interpretation of current citizens,
- Act6 v0.1 as active Blueprint,
- any old Human=objective-real-human wording,
- early device over-tags repaired by Package G.

`Found in repository` ≠ `current truth`.

---

# 9. Map Rule

Civic and engineering maps are deliberately separate.

Civic layer answers:
- where people live/work/meet,
- neighborhoods/landmarks,
- commute graph.

Engineering layer answers:
- pressure/isolation boundaries,
- utility topology,
- emergency containment,
- rotation/Spine interfaces.

A civic neighborhood must never be assumed identical to one pressure sector or social caste.

---

# 10. Timeline Rule

Three scales coexist:
1. ~450-year Voyage History
2. ~14-year main-story chronology
3. insertion → ~+1 year arrival ending.

Do not force every historical era to an exact year.
Use exact episode/time locks only where M1/Blueprint requires them; retain broad era ranges elsewhere.

---

# 11. Agent Retrieval Rule

A drafting/review agent should begin from:
`EPISODE-CONTEXT-INDEX → Package G Registry → exact authorities`

It should not load the full Atlas as story context by default.
The Atlas is for discovery and verification.

---

# 12. Completion Criteria

REF-H1 passes only if:
- all required atlas files exist,
- every page declares non-authority status,
- high-risk superseded concepts are flagged,
- civic/engineering maps are separated,
- v1 Canon vs v2 Candidate vs C2 Elastic is visible,
- timelines preserve M1 authority,
- institution matrix does not grant new powers,
- dependency matrix does not invent exact engineering values,
- Episode index delegates knowledge fences to Package G,
- a hostile Shadow-Canon Red Team finds P0=0.

---

# Verdict

Selected:

**`REF-H1 — Human-Readable MOC + Source-Linked Atlas Tables + Authority/Elastic Registry + Optional Structured Metadata`**

Status:
`SELECTED PACKAGE H ARCHITECTURE / NOT CANON`
