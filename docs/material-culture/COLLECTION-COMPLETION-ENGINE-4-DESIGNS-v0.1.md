# Collection / Completion Engine — 4 Designs v0.1

Status: `ENCYCLOPEDIC DEEP DESIGN / PACKAGE C-M + G BRIDGE / NO PROSE`
Date: 2026-08-17
Project: 《우주선에는 인간이 한 명뿐이다》

## Purpose

Design a reader-facing sense of collection/completion suitable for this social SF without importing fantasy loot progression.

The question is not:
`What rare item does the protagonist obtain next?`

The question is:
`What part of Meridian's civilization does the reader learn, recognize, revisit and finally understand as a connected whole?`

The engine must survive after Count/Amara Reveal, so mystery-fragment collection cannot be the primary model.

---

# Design CE-A — Mystery Fragment Collection

Reader collects:
- Seed clues,
- old terminology,
- provenance records,
- legal residues,
- identity evidence.

Strengths:
- strong early momentum,
- compatible with current reveal architecture,
- easy setup/payoff tracking.

Weaknesses:
- dies after Meaning/Amara reveal,
- trains reader to treat every detail as clue,
- overweights documents and information,
- encourages later bigger-secret escalation.

Verdict:
`USE AS EARLY SECONDARY LAYER ONLY`

---

# Design CE-B — Meridian Living-World Codex

Reader collects:
- habitats,
- districts,
- jobs,
- schools,
- transit modes,
- clinics,
- festivals,
- food/work/leisure routines,
- public institutions.

Strengths:
- excellent fit for a 300k ship-city,
- supports ordinary-life promise,
- survives the main Reveal,
- makes return visits rewarding.

Weaknesses:
- can become travelogue/worldbuilding showcase,
- novelty falls if locations do not change,
- “new place every arc” can feel episodic.

Verdict:
`STRONG BASE / NEEDS RETURN AND CONSEQUENCE`

---

# Design CE-C — Object / Relic Recognition Loop

Reader collects recognition of:
- recurring tools,
- heirlooms,
- heritage objects,
- industrial assets,
- ordinary material motifs.

Strengths:
- tactile,
- visual,
- good for illustrations/IP,
- lets early mundane objects acquire later significance.

Weaknesses:
- easily becomes gadget catalogue,
- relic overuse can turn into hidden-lore hunting,
- too object-centric for a character/social novel.

Verdict:
`GOOD MATERIAL SUB-LAYER / NOT PRIMARY`

---

# Design CE-D — Civilization Completion Loop

Reader gradually completes a mental model of Meridian through four linked collection modes:

1. **Encounter** — see a place/job/object/rule in ordinary life.
2. **Recognition** — see it again in another person's context.
3. **Recontextualization** — understand its historical/social/resource meaning.
4. **Transformation** — see it change or become part of arrival civilization.

Example:
reserve pump
→ ordinary water redundancy
→ labor/budget constraint
→ designated settlement capital
→ ship redundancy loss
→ early orbital/surface infrastructure ancestry.

Strengths:
- lasts all 230 episodes,
- integrates setting and plot,
- creates reread reward,
- avoids explicit inventory UI,
- works with places, institutions, relationships and objects,
- makes the ending feel like completion rather than only resolution.

Weaknesses:
- requires careful tracking,
- can over-engineer every recurring detail,
- needs a strong ordinary-noise budget.

Verdict:
`SELECTED PRIMARY BASE`

---

# Selected Hybrid — CE-H1

Name:
**CE-H1 — Civilization Completion + Living-World Recognition + Selective Material Return**

Base:
CE-D Civilization Completion.

Add:
- CE-B as the largest visible layer,
- CE-C selectively for memorable objects/assets,
- CE-A only for early/mid factual mystery where already designed.

Hard principle:
**The reader collects understanding, familiarity and changed meaning—not power.**

---

# 1. Five Collection Families

## CF-1 — Place Recognition
Examples:
- 1환 ordinary residential/service districts,
- 구시가지,
- 2환 mixed city/watershed spaces,
- 3환 clinics/industry/living districts,
- Spine transit,
- Outer Works access,
- later orbit/surface/new-habitat spaces.

Completion pattern:
first visit → ordinary return → changed policy/resource state → late transformed version.

## CF-2 — Profession / Institution Recognition
Examples:
- Continuity adjudication,
- rehabilitation,
- appeal/court work,
- water/reclamation,
- maintenance,
- school/youth systems,
- archives,
- manufacturing/logistics,
- transition registry.

Completion pattern:
meet one worker/process → see consequences → revisit under different pressure → understand authority boundary.

## CF-3 — Relationship / Social Network Recognition
Readers accumulate familiarity with recurring non-core people and communities.

Goal:
A school, utility team, Old Quarter block, legal office or clinic should eventually feel populated by recurring social memory rather than exposition NPCs.

## CF-4 — Material Recognition
Selective recurring objects/equipment:
- work tools,
- household/heirloom objects,
- public-space markers,
- strategic equipment,
- heritage objects.

Rule:
Only a small subset earns tracked recurrence.

## CF-5 — Future Path Completion
Readers gradually learn that Meridian's future is not one destination but several real paths:
- ship-city continuation,
- orbit/asteroid industry,
- surface foothold,
- later new habitat.

Completion pattern:
career/background hint → household decision → resource commitment → physical route → lived aftermath.

---

# 2. Act-Level Collection Progression

## Act 1 — Learn The City Through People
Primary collection:
- family/work routines,
- 1환/Spine/2환/3환/Old Quarter glimpses,
- Continuity/appeal/rehab/school processes,
- first recurring places and professional objects.

Reader feeling:
`This is not a ship set; it is a city.`

Avoid:
turning every early location into an information clue.

## Act 2 — Recognize Cross-Habitat Systems
Primary collection:
- utility/work/commute/family networks,
- old/current record systems,
- Amara as one ordinary actor among them,
- redundancy/capacity logic.

Reader feeling:
`The places and systems connect.`

## Act 3 — Recontextualize The Civilization
Primary collection:
- origin terminology gets a new meaning,
- previously ordinary Seed practices become historically legible,
- Amara's household becomes a familiar family under new interpretation.

Reader feeling:
`I had already seen the pieces; now they mean something different.`

## Act 4 — Collect Consequences, Not More Secrets
Primary collection:
- media/admin/work/school/privacy consequences,
- recurring institutions behave differently after Reveal,
- Ella/Maren family history recontextualizes prior behavior.

Reader feeling:
`The same world is now functioning under changed knowledge.`

## Act 5 — Objects And Places Become Resources
Primary collection:
- reserve systems,
- manufacturing tools,
- Old Quarter space,
- careers,
- strategic legal categories.

Reader feeling:
`Things I already knew now carry a price.`

This is the strongest Material Culture collection phase.

## Act 6 — People Complete Different Future Paths
Primary collection:
- careers mature,
- homes split,
- recurring places lose old functions or gain new ones,
- ship/orbit/surface/new-habitat become lived choices.

Reader feeling:
`The future map is being filled by people I know.`

## Act 7 — Return / Transformation Payoff
Primary collection:
- old systems return in changed form,
- strategic assets physically reappear as new infrastructure,
- familiar people/places persist, move or disappear,
- new spaces remain incomplete but real.

Reader feeling:
`I understand where this civilization came from and what became of its pieces.`

Avoid:
ending with a checklist of every collected element.

---

# 3. Internal Completion Ledger

Author-facing only. Never shown as game UI.

For each tracked collection element:

```yaml
id: CF-MAT-XXX
family: material | place | profession | network | future-path
first_encounter: EP-xxx
recognition_returns:
  - EP-xxx
recontextualization:
  - EP-xxx
transformation_payoff:
  - EP-xxx
status: OPEN | RECOGNIZED | RECONTEXTUALIZED | TRANSFORMED | CLOSED
reader_required_memory: LOW | MED | HIGH
ordinary_noise_neighbors:
  - examples of similar details that are not tracked
```

This ledger is lighter than Narrative Device Atlas.
Not every collection element is a foreshadowing device.

---

# 4. Key Difference From Chekhov / Foreshadow

A collection-return is NOT automatically Chekhov's gun.

Example:
A local restaurant appears in Act 1 and again in Act 4 because it is part of a living neighborhood.
That is **recognition**, not setup/payoff.

It becomes a narrative device only if:
- its earlier state establishes a dependency,
- a later transformation is causally/payoff-relevant.

This distinction is mandatory to preserve ordinary life.

---

# 5. Material Collection Without Loot

Good:
- recognizing the same maintenance tool family in another Habitat,
- seeing an inherited object repaired over time,
- learning why a boring old machine cannot be easily replaced,
- encountering an affordable ship-history collectible trend,
- later seeing a strategic asset transferred into new infrastructure.

Bad:
- legendary numbered artifact set,
- hidden weapons catalogue,
- protagonist collecting founder objects,
- escalating rarity grades,
- relic granting authority/power.

---

# 6. Repeat-Return Ratio — Design Direction

The setting should not maximize novelty.
Recurring recognition is valuable.

Target qualitative balance:
- recurring/familiar places and systems should carry much of the series,
- new places should usually connect to existing networks,
- late Acts should return to early elements more often than they introduce entirely new lore.

Especially after Act 5:
**return/recontextualization > new-setting novelty.**

---

# 7. Reader Memory Budget

Do not require the reader to remember dozens of item names.

High-memory tracked elements should be few:
- key family/place objects,
- major recurring strategic asset families,
- important legal/institution terms,
- core places.

Low-memory elements can return with natural contextual reminders.

Rule:
Recognition should feel rewarding even if the reader only vaguely remembers the earlier appearance.

---

# 8. Collection Engine QA

Fail if:
- more than half of collection rewards are information clues,
- every old object becomes historical evidence,
- new locations are introduced faster than familiar locations evolve,
- a protagonist physically owns most meaningful artifacts,
- Material Culture becomes a shopping/gear list,
- Act 6~7 add large new lore families instead of transforming known ones,
- the ending explicitly inventories all completed elements.

Pass if:
- ordinary familiarity accumulates,
- returns feel natural,
- some early details gain new meaning,
- some details remain ordinary forever,
- future paths emerge from already-known careers/places/assets,
- reader can feel Meridian becoming familiar and then changing.

---

# Current Verdict

`CE-H1 = SELECTED COLLECTION / COMPLETION ENGINE`

Role in series:
**secondary retention engine / world-attachment engine / late payoff amplifier**

It must not replace:
- character causality,
- main conflict,
- relationship change,
- mystery fairness.

It complements them by giving the reader a reason to enjoy learning and revisiting the civilization itself.

Status:
`DESIGN BASE PASS / EXACT TRACKED ELEMENT LEDGER DEFERRED UNTIL B/C/C-M/D/F DEEP DESIGN FILLS THE WORLD`
