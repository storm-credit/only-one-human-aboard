# Narrative Engineering Map Red Team v0.1

Status: `PACKAGE G INTERIM QA / NOT FINAL PASS`
Date: 2026-08-17

Scope:
- Narrative Map Architecture
- Device Atlas
- 23 Sub-Act Device Map
- Obsidian/Context Pack spec

---

## RT-NE-01 — Are devices being forced into every Sub-Act?
Risk:
A checklist can make the novel feel engineered rather than lived.

Finding:
The current map assigns high-salience tracked devices to all blocks, but several are continuations/echoes rather than new tricks.

Rule:
No quota for MacGuffin/Chekhov/Red Herring. A Sub-Act may contain only ordinary consequence work if that is what the story requires.

Verdict: `PASS WITH ANTI-QUOTA GUARDRAIL`

---

## RT-NE-02 — Is every recurring detail becoming foreshadowing?
Risk:
Readers start treating food, commute, objects and jokes as coded clues.

Rule:
Tracked narrative devices must be a minority of recurring detail. Ordinary texture must greatly outnumber clue-bearing detail.

Verdict: `PASS IF NOISE BUDGET ENFORCED`

---

## RT-NE-03 — Are the three MacGuffins actually three universal lore keys?
Finding:
MG-01 resolves Count, MG-02 resolves a family ethics rupture, MG-03 generates arrival-law conflict. Their functions are separate.

Hard guardrail:
No one document may explain history + Amara + destination + ending.

Verdict: `PASS`

---

## RT-NE-04 — Is MG-02 too obviously “the hidden document” for 100+ episodes?
Risk: `HIGH P1`

Mitigation:
- plant behavior and selective precision, not a mysterious object,
- Ella discovers it through ordinary access/archive routes,
- document is nonbinding,
- payoff is Maren's choice to withhold, not secret lore content.

Still required:
Exact EP-level seed frequency audit after Context Manifests are generated.

Verdict: `OPEN P1 / EP-LEVEL AUDIT REQUIRED`

---

## RT-NE-05 — Could MG-03 make late story feel like an arbitrary ancient-law twist?
Risk: `HIGH P1`

Mitigation:
- arrival compliance is present from Act 1,
- legacy metadata appears earlier,
- transition review becomes current administration before Act 5C,
- Amara does not activate it,
- old law creates a problem, not an answer.

Still required:
Exact early/mid arrival-law breadcrumb audit.

Verdict: `CONDITIONAL PASS`

---

## RT-NE-06 — Are Red Herrings manipulative?
Rule:
Red Herrings are character/public hypotheses built from true evidence. Narrator/system cannot state false facts.

Current RHs:
- synthetic-origin = robot interpretation,
- Count=1 = archive error,
- Amara = special authority.

All can be resolved when evidence becomes available.

Verdict: `PASS`

---

## RT-NE-07 — Does the map accidentally leak author knowledge to POV characters?
Risk: `P0 if implementation ignores knowledge layers`

Mitigation:
Context Pack schema explicitly separates AUTHOR / POV / PUBLIC / PROTECTED knowledge.

Required future QA:
Every EP manifest must declare information allowed/forbidden.

Verdict: `DESIGN PASS / IMPLEMENTATION BLOCKER UNTIL MANIFESTS`

---

## RT-NE-08 — Will Obsidian links duplicate Canon and drift?
Risk:
Graph nodes can become shadow Canon.

Rule:
Map/device notes reference Canon; they may summarize but never silently alter source rules. Canon/Blueprint/M1/POV authority always wins.

Verdict: `PASS WITH AUTHORITY HEADER`

---

## RT-NE-09 — Can an agent really receive only needed context?
Current answer:
Design-level yes.
The Context Pack schema defines Tier 0~4 retrieval and direct dependency traversal.

Blocker:
EP001~230 manifests are not yet generated, so context assembly is not yet executable as a complete dataset.

Verdict: `PARTIAL`

---

## RT-NE-10 — Is there enough variety in device families?
Current 23-block mix includes:
- hard clue,
- institutional residue,
- fair red herring,
- primer,
- character tell,
- MacGuffin,
- Chekhov/setup-payoff,
- ticking clock,
- mirror,
- recontextualization,
- reversal,
- relationship payoff,
- material/world payoff.

Finding:
Variety is adequate at macro level.

Risk:
Execution may overuse documents/reports because several devices are institutional.

Guardrail:
Payoffs should occur through behavior, access, physical movement, lost time, changed work, altered relationships or resource transfer whenever possible—not repeated screen reading.

Verdict: `PASS WITH SCENE-FORM GUARDRAIL`

---

## RT-NE-11 — Does the device map replace the 230-episode Blueprint?
No.
The map answers dependency/navigation questions; Blueprint answers episode problem/choice/consequence/carry.

Verdict: `PASS`

---

## RT-NE-12 — Is Package G complete now?
No.

Remaining blockers:
1. exact 7 Act MOC nodes,
2. exact 23 Sub-Act Obsidian nodes,
3. EP001~230 Context Manifest dataset,
4. exact episode lifecycle binding for tracked devices,
5. orphan-device audit,
6. premature-payoff audit,
7. clue-density/noise audit,
8. final cross-check against M1/POV/Blueprint,
9. final Package G hostile QA.

Verdict:
`PACKAGE G = IN PROGRESS / STRUCTURAL MAP FOUNDATION PASS`
