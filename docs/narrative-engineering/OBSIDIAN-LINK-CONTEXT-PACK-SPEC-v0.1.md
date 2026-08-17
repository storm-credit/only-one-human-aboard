# Obsidian Link + Episode Context Pack Spec v0.1

Status: `PACKAGE G / IMPLEMENTATION SPEC / NO PROSE`
Date: 2026-08-17

## Goal

When opening one episode, a human or writing agent should not receive the entire repository.
It should receive only the minimum authoritative context needed to write that episode without breaking:
- Canon,
- character state,
- information fairness,
- active narrative devices,
- prior causal carry,
- future payoff constraints.

Obsidian is the human navigation layer. The same metadata can later be parsed by Claude Code/automation to assemble Context Packs.

---

# 1. MOC Hierarchy

Recommended logical graph:

```text
00-NARRATIVE-MOC
  ├─ ACT-01 ... ACT-07
  │    └─ SA-1A ... SA-7C
  │          └─ EP-001 ... EP-230
  ├─ DEVICE-ATLAS
  ├─ CHARACTER-MOC
  ├─ WORLD-RULE-MOC
  ├─ INFORMATION-MOC
  ├─ LOCATION-MOC
  └─ PAYOFF-LEDGER
```

Cross-links are first-class:
- Episode ↔ Device
- Episode ↔ Character
- Episode ↔ World Rule
- Episode ↔ Location
- Episode ↔ Previous Carry
- Episode ↔ Future Constraint

Hierarchy answers **where am I in the story?**
Cross-links answer **what must I know here?**

---

# 2. Stable IDs

Human-readable file names may change; stable IDs should not.

Examples:
- `ACT-04`
- `SA-4C`
- `EP-117`
- `CHAR-ELLA`
- `CHAR-MAREN`
- `RULE-RECONSTRUCTION`
- `RULE-COI-H1`
- `MG-02`
- `CT-01`
- `LOC-OLD-QUARTER`

Later tooling should join by ID, not by display title.

---

# 3. Episode Frontmatter Schema

Recommended Obsidian-compatible YAML:

```yaml
---
id: EP-117
type: episode
act: ACT-04
subact: SA-4C
state: NOT_STARTED
pov: CHAR-ELLA

canon_refs:
  - RULE-RECONSTRUCTION
  - RULE-COI-H1
  - RULE-PR-H1

character_refs:
  - CHAR-ELLA
  - CHAR-MAREN
  - CHAR-NOAH

device_refs:
  - MG-02
  - CT-01
  - RP-01
  - MR-01

location_refs: []

incoming_carries:
  - EP-116

outgoing_carries:
  - EP-118
  - EP-120

information_allowed:
  - PR-H1 draft exists
  - Ella has obtained independent archive/access evidence

information_forbidden:
  - any later private thought Ella cannot know

future_constraints:
  - EP-120 Maren accountability remains meaningful
  - Maren cannot adjudicate her own family case
  - record is nonbinding, not automatic no-Reconstruction

source_authority:
  - canon/CHARACTER_BIBLE-v1.md
  - canon/ACT_BIBLE-v1.md
  - active Act4 Blueprint
  - ACT4 POV Map
---
```

This example is structural, not a replacement for the exact EP117 Blueprint card.

---

# 4. Sub-Act Frontmatter Schema

```yaml
---
id: SA-4C
type: subact
act: ACT-04
episodes: [EP-112, EP-113, EP-114, EP-115, EP-116, EP-117, EP-118, EP-119, EP-120, EP-121, EP-122]
primary_track: family / agency
secondary_pressure: institutional accountability
baseline_change: Maren's private control becomes an exposed family/professional problem
active_devices:
  - MG-02
  - CT-01
  - RP-01
  - MR-01
forbidden_drift:
  - record becomes binding directive
  - Maren judges own family case
  - second ontology twist
---
```

---

# 5. Device Node Schema

```yaml
---
id: MG-02
type: macguffin
name: Ella Unfiled Reconstruction Preference Record
state: OPEN
plant:
  - SA-1C
reinforce:
  - SA-4B
trigger:
  - SA-4C
payoff:
  - EP-117
aftershock:
  - EP-120
characters:
  - CHAR-ELLA
  - CHAR-MAREN
canon_refs:
  - RULE-PR-H1
---
```

Narrative text below the frontmatter explains actual narrative value and guardrails.

---

# 6. Context Pack Assembly — CP-H1

For a requested episode `EP-X`, assemble in this order:

## Tier 0 — Hard Authority
Always include concise extracts/references from:
1. CLAUDE project rules,
2. relevant Canon rules,
3. exact episode Blueprint card,
4. exact POV map assignment,
5. M1 time/age value.

## Tier 1 — Local Story State
Include:
- parent Act summary,
- parent Sub-Act baseline/target change,
- current POV character state,
- directly participating character states,
- current locations/institutions.

## Tier 2 — Active Narrative Engineering
Include only active device nodes linked to the episode:
- planted clues to preserve,
- trigger/payoff obligations,
- open loops,
- forbidden early reveals,
- future constraints.

## Tier 3 — Causal Neighbors
Include:
- previous 1~3 relevant episode carries,
- future dependency notes required to avoid breaking later payoff.

## Tier 4 — Optional Texture
Retrieve only if scene requires it:
- food,
- clothing,
- transit,
- school,
- media,
- job procedure,
- district texture.

Do not include unrelated encyclopedic setting sections by default.

---

# 7. Context Budget Rule

Preferred principle:
**authority first, locality second, narrative dependencies third, texture on demand.**

Never solve prompt limits by removing:
- exact Blueprint choice/consequence,
- POV knowledge boundary,
- active hard-stop Canon,
- future payoff constraint.

Cut first:
- unrelated setting lore,
- already-resolved device history,
- characters not present or causally relevant,
- distant Acts with no active dependency.

---

# 8. Link Direction Rules

Every episode links upward:
- Act
- Sub-Act

Every high-salience device links both ways:
- device → plant/payoff episodes
- episode → device

Every future constraint has a reverse dependency:
Example:
`EP117 → must preserve EP120 accountability`
`EP120 ← depends on EP117 record/confrontation handling`

This enables orphan detection.

---

# 9. Obsidian Graph Filters

Useful graph views:

## Episode View
Show:
Episode + parent Sub-Act + direct characters + active devices + immediate carries.

## Device View
Show:
One MacGuffin/Chekhov/Clue and all plant/reinforce/payoff nodes.

## Character Arc View
Show:
Character + episodes where they initiate baseline changes + character tells/mirrors.

## Reveal View
Show:
Hard clues + institutional residues + false interpretations + reveal/payoff episodes.

## Canon Impact View
Show:
One world rule and every episode/device depending on it.

---

# 10. Retrieval Safety

A future agent may use links to retrieve context, but must not infer:
- that every backlink is equally important,
- that an old provisional design overrides Canon,
- that a device node can redefine Canon,
- that a future payoff fact is knowable by the current POV.

Therefore every Context Pack must distinguish:
- `AUTHOR_KNOWLEDGE`
- `POV_KNOWLEDGE`
- `PUBLIC_KNOWLEDGE`
- `PROTECTED_KNOWLEDGE`

---

# 11. Minimal Episode Context Pack Output

Recommended generated packet:

```text
EP117
TIME: [M1 exact]
POV: Ella
SUBACT GOAL: [SA-4C]

MUST PRESERVE
- exact Blueprint problem/choice/consequence
- relevant Canon hard stops

CHARACTER STATE
- Ella
- Maren
- Noah if causally active

ACTIVE DEVICES
- MG-02 payoff
- CT-01 major exposure
- RP-01 family turn
- MR-01 personal/civic mirror

INCOMING CARRY
- only relevant prior episode carries

FUTURE CONSTRAINTS
- EP120 accountability
- no Maren self-adjudication
- record remains nonbinding

FORBIDDEN EARLY/LATE INFO
- explicit list

OPTIONAL TEXTURE
- retrieve on demand
```

---

# 12. Future Automation Hooks

A later Claude Code/agent implementation can:
1. parse YAML IDs,
2. resolve direct references,
3. traverse one dependency hop by default,
4. fetch authoritative source chunks,
5. deduplicate overlapping context,
6. output an episode Context Pack,
7. run orphan/premature-payoff QA.

No coding is required now; this document defines the data contract first.

---

# Current Verdict

`CP-H1 = SELECTED CONTEXT RETRIEVAL MODEL`

Obsidian-ready link architecture is now specified at design level.
Full EP001~230 manifests are **not yet generated** and remain a Package G completion task.
