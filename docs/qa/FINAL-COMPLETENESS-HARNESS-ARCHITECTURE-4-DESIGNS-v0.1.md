# Final Completeness Harness Architecture — 4 Designs v0.1

Status: `PACKAGE I DESIGN COMPARISON / PRE-PROSE / NOT CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

## Goal

Determine whether the setting is actually reference-grade complete enough that arbitrary scenes can be written **without inventing new major world rules**.

This is not a test that every restaurant name, salary, room number or statute subsection is frozen.

### P0 failure
A scene requires a new major rule about:
- personhood/origin,
- law/governance,
- economy/property,
- family/education/medicine/death,
- infrastructure/emergency/AI,
- history,
- destination/arrival,
- character core,
- narrative Reveal/POV order.

### P1 gap
The major rule exists, but a recurring or high-salience implementation value still needs a bounded choice/quantification.

### C2 acceptable elastic
Exact scene-level details can be invented within a locked range/grammar without creating a new world rule.

---

# Design A — Static Checklist Audit

## Method
Review all domains and mark present/missing.

## Strength
Fast and easy to document.

## Failure
A document can exist while failing in an actual scene.
Does not expose interaction gaps.

Verdict: `INSUFFICIENT ALONE`

---

# Design B — Full Citizen Life Simulation

## Method
Create several representative citizens and simulate decades of life.

## Strength
Excellent for family/economy/education/medicine/death.

## Failure
Weak against rare emergencies, media events, arrival transitions and narrative knowledge leaks.

Verdict: `STRONG COMPONENT`

---

# Design C — Random Scene Fuzzing

## Method
Generate arbitrary scene prompts across places/classes/ages/incidents and test whether major new rules are required.

## Strength
Finds unexpected cross-domain holes.
Excellent adversarial pressure.

## Failure
Pure random tests can miss mandatory known edge cases.

Verdict: `STRONG COMPONENT`

---

# Design D — Layered Deterministic + Adversarial + Fuzz + Story Regression

## Method
Four layers:

1. **Deterministic mandatory suites**
   - ordinary day,
   - whole life cycle,
   - family,
   - work/class,
   - crime/emergency,
   - media/privacy,
   - AI,
   - arrival,
   - material culture.

2. **Cross-domain adversarial edge cases**
   - reconstructed parent + property + child,
   - rich defendant + public safety,
   - disabled worker + emergency evacuation,
   - legacy record + privacy + media,
   - off-ship family + citizenship + inheritance.

3. **20+ random-scene fuzz tests**
   must resolve using existing rules without major invention.

4. **Full story regression**
   - 230 episode architecture,
   - Reveal timing,
   - POV fences,
   - PR-H1,
   - Human Settler,
   - insertion/ending,
   - material/narrative device boundaries.

## Strength
Tests both completeness and compatibility with the already locked novel.

## Failure Risk
Can become fake pass if every unresolved detail is casually called `elastic`.

## Guardrail
For each open item ask:
> Could two opposite answers materially change institutions, character decisions, or multiple future scenes?

If yes, it is P0/P1, not harmless C2.

## Verdict
`SELECTED`

---

# Selected Harness — FC-H1

**`FC-H1 — Deterministic Life-Cycle Suites + Cross-Domain Adversarial Scenarios + Random Scene Fuzzing + Full Episode Regression`**

## Mandatory Test Suites

### I-01 Random Citizen Day
At least:
- child,
- working adult,
- shift worker,
- elder,
- lower-resource household,
- disabled citizen.

### I-02 Whole Life Cycle
birth → school → training/work → housing → partnership/family → illness/disability → retirement → death/estate.

### I-03 Crime / Public Safety
- theft/fraud,
- assault/domestic violence,
- dangerous tool misuse,
- cyber/privacy crime,
- critical-system sabotage attempt,
- protest/civil disobedience distinction.

### I-04 Accident / Emergency
- apartment fire,
- local decompression,
- contamination,
- power/water outage,
- transit failure,
- Outer Works incident.

### I-05 Class / Economy / Disability
- job loss,
- debt/business failure,
- housing loss/relocation,
- wealthy influence attempt,
- accessibility need,
- retirement on tighter income.

### I-06 Family Lifecycle
- sole parent,
- donor conception,
- partnership/divorce,
- adoption/guardianship,
- reconstructed parent return,
- adolescent residence voice.

### I-07 School / Work / Retirement
- child assessment,
- apprenticeship,
- retraining,
- strike/critical staffing,
- automation displacement,
- actual retirement.

### I-08 Media / Rumor / Privacy
- ordinary rumor,
- protected record,
- public-interest publication,
- re-identification,
- false candidate,
- correction without omniscient truth feed.

### I-09 Religion / Culture / Leisure
- worship/nonreligion,
- holiday,
- restaurant meal,
- clothing/fashion,
- sport/game/music,
- funeral/mourning.

### I-10 AI / Automation Ontology
- personal agent mistake,
- domain AI recommendation conflict,
- control-network outage,
- robot work accident,
- human accountability.

### I-11 Arrival Migration / Property
- volunteer selection,
- family split,
- off-ship residence,
- local representation,
- land/use rights,
- inheritance across nodes,
- no Amara privilege.

### I-12 Material Culture
- ordinary object,
- restricted tool,
- weapon/public-safety edge,
- heirloom,
- disputed provenance,
- salvage/found strategic object,
- heritage vs operational asset.

### I-13 20 Random Scene Fuzz
At least 20 unrelated scenes with no major new rule.

### I-14 Narrative Engineering Regression
- orphan/premature/noise/device overuse,
- AUTHOR/POV/PUBLIC/PROTECTED,
- 230 POV/reveal timing.

### I-15 Canon Conflict Regression
Every selected v2 candidate checked against:
- WORLD_BIBLE-v1,
- CHARACTER_BIBLE-v1,
- ACT_BIBLE-v1,
- active Blueprints,
- M1,
- Prose Protocol.

---

# Pass Rule

Package I may pass only if:
- blocking P0 = 0,
- every remaining P1 has an explicit owner and closure path,
- no P1 secretly changes core Reveal/ending/personhood architecture,
- 20 random scenes all resolve without a new major rule,
- final 230-episode regression passes,
- unresolved exact values are genuinely bounded C2/quant items.

Package I PASS still does not itself make v2 candidates Canon.
After I:
`close P1 → consolidate v2 Bibles → final conflict regression → Encyclopedic Canon Freeze v2`.
