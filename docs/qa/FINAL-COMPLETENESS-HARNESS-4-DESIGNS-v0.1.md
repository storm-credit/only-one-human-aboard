# Package I — Final Completeness Harness: 4 Designs v0.1

Status: `DESIGN COMPARISON / FINAL ENCYCLOPEDIC QA / NO PROSE`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

Purpose:
Decide how to prove that Packages A~H are not merely large, but complete enough that arbitrary scenes can be written without inventing new civilization-scale rules.

This harness does not require every restaurant name, salary figure or pressure-sector number to be frozen.
It does require all **major rule classes** to exist and interoperate.

---

# 0. Severity Vocabulary

## P0 — Freeze Blocker
A random but plausible scene requires inventing or changing a major world rule, or exposes a contradiction with locked Canon/story architecture.

Examples:
- no answer for who can order an emergency pressure lockdown,
- unclear whether losing a job removes health care,
- no coherent rule for inheritance after Reconstruction,
- a POV must know future protected truth for an episode to work,
- settlement citizenship requires Amara to be a key,
- exact-one Natural-Origin protocol reappears.

Any P0 means:
`ENCYCLOPEDIC CANON FREEZE v2 = FAIL`.

## P1 — Important Micropass Before Freeze
The major rule exists, but a bounded parameter/procedure must be tightened because inconsistency would recur.

Examples:
- refuge-capacity order,
- exact external settlement ceiling at +1y,
- destination atmospheric fractions,
- data-retention period family,
- exact civil-majority threshold if required by several episodes.

## C2 — Controlled Elastic
A detail can safely be chosen during scene design inside already-defined bounds.

Examples:
- café name,
- exact apartment floor,
- precise shirt style,
- exact salary number for a one-off employee,
- one-off game title.

## Texture Gap — Not A Rule Gap
A scene could use another named example, but existing world rules already determine how it works.

This is not a Freeze blocker.

---

# Design A — Encyclopedic Checklist Only

Method:
Check whether every planned setting-bible heading has text.

Strengths:
- simple,
- fast,
- measurable.

Fatal weakness:
A document can contain every heading and still fail when rules collide in a real scene.

Example:
`property`, `Reconstruction`, and `inheritance` may each be described separately while still contradicting one another when a reconstructed person returns after an estate settles.

Verdict:
`REJECT AS SOLE HARNESS`.

---

# Design B — Random Scene Stress Test Only

Method:
Generate 50–100 arbitrary scenes and see whether the world can answer them.

Strengths:
- close to actual prose use,
- catches hidden daily-life gaps,
- hard to game through documentation volume.

Weakness:
Randomness may miss rare but structurally important domains such as:
- protected-data authority,
- family guardianship,
- severe crime,
- post-arrival jurisdiction,
- historical provenance.

Verdict:
`STRONG COMPONENT / INSUFFICIENT ALONE`.

---

# Design C — Domain Matrix + Cross-Package Pairwise Regression

Method:
For every major domain, test interactions with every other relevant package.

Examples:
- Society × Infrastructure,
- Family × Housing,
- Economy × Disability,
- Media × Privacy,
- AI × Criminal Justice,
- History × Material Culture,
- Arrival × Citizenship,
- Character × Culture,
- Narrative Engineering × Protected Knowledge.

Strengths:
- systematic,
- good contradiction detection,
- catches rules that work alone but fail together.

Weakness:
Can become abstract spreadsheet QA and miss whether an actual day feels writable.

Verdict:
`REQUIRED CORE / NEEDS SCENE TEST`.

---

# Design D — Layered Adversarial Harness

Method:
Use four layers:

### Layer 1 — Coverage
Every major life/world domain has an owner document and rule.

### Layer 2 — Cross-Package Collision
Rules are tested in combined cases.

### Layer 3 — Random Scene / Random Citizen
Arbitrary scenes must resolve without a new major rule.

### Layer 4 — Story Regression
EP001~230, POV, Reveal, Device and ending architecture must remain valid under the encyclopedic additions.

Strengths:
- tests completeness rather than document volume,
- catches both ordinary-life and locked-story regressions,
- naturally distinguishes P0 from P1/C2.

Weakness:
Most work.

Verdict:
**`SELECTED — I-H1`**.

---

# Selected Harness — I-H1

`Coverage Matrix + Cross-Package Collision + Random Citizen/Scene + Locked Story Regression`

Pass standard:
- blocking P0 = **0**,
- every P1 has owner + bounded repair plan,
- C2 details are explicitly bounded enough not to mutate major rules,
- no rejected/superseded concept is required to make a test pass.

---

# Mandatory Test Suites

## I1 — Random Citizen Day
Can a normal citizen wake, eat, travel, work, spend money, use services, relax, communicate, and sleep without inventing a rule?

## I2 — Whole Life Cycle
Conception/birth → childcare → school → work → household/partnership/parenthood → illness/disability → retirement → death/finality/estate.

## I3 — Crime / Accident / Emergency
Theft, assault, domestic abuse, fraud, cybercrime, dangerous-tool misuse, fire, decompression, contamination, utility failure.

## I4 — Class / Poverty / Wealth / Disability
Does Civic Floor coexist with real inequality, debt, housing difference, accessibility, unemployment and social influence?

## I5 — Family Lifecycle
Sole parenthood, partnership, separation, divorce, donor conception, adoption, guardianship, child autonomy, inheritance.

## I6 — School / Work / Retirement
Education choice, apprenticeship, credentialing, job loss, retraining, essential-skill shortage, retirement.

## I7 — Media / Rumor / Privacy
News, creators, social feeds, private messaging, doxxing/re-identification, protected records, public-interest disclosure.

## I8 — Religion / Culture / Leisure
Belief/nonbelief, funeral, food, clothing, art, games, sport, holidays, intimacy, ordinary social variation.

## I9 — AI / Automation Ontology
Personal agent, industrial automation, recommendation, medical decision support, policing, courts, emergency safety, network failure.

## I10 — Arrival / Migration / Property / Jurisdiction
Who moves, who waits, land/resource access, off-ship residence, family split, representation, citizenship, local municipal growth.

## I11 — Random Object / Weapon / Heirloom / Salvage
Ordinary object ecology, dangerous tools, public-safety equipment, heritage provenance, inheritance, found property, strategic assets.

## I12 — 20 Arbitrary Scenes
At least 20 scenes across age/class/location/occupation/era must require no new major rule.

## I13 — Narrative Device / Knowledge / EP001~230 Regression
- orphan device,
- premature payoff,
- clue overload,
- POV future-knowledge leak,
- Count timing,
- PR-H1 timing,
- Human Settler timing,
- insertion/ending guardrails.

## I14 — Quantitative Sanity Gate
Determine which remaining numbers are:
- P0 physically contradictory,
- P1 required before Freeze,
- C2 safely elastic.

---

# Randomization Requirements

The harness must not only test core protagonists.
Include:
- child,
- elderly citizen,
- disabled citizen,
- low-income worker,
- affluent professional/business owner,
- shift worker,
- unemployed/retraining adult,
- sole parent,
- reconstructed person,
- crime victim,
- accused citizen,
- 1환/2환/3환 resident,
- Spine worker,
- off-ship arrival worker,
- religious and nonreligious citizens.

---

# Adversarial Rules

A test does NOT pass by saying:
- `future technology handles it`,
- `AI decides`,
- `the government has a protocol`,
- `resources are recycled`,
- `advanced medicine fixes it`.

The answer must identify the already-designed rule class and owner.

A test also does NOT fail merely because:
- exact proper noun is open,
- exact numeric amount is open,
- the scene needs a one-off supporting character,
if the major mechanism is already defined.

---

# Canon Safety Regression

Every test must reject solutions that require:
- adult origin scanner,
- Seed memory/personality programming,
- anchorless adult restoration,
- exact-one Natural-Origin protocol,
- Habitat caste,
- central AI sovereignty,
- Amara chosen authority/reproductive duty,
- mass citizenship erasure,
- civil-grid propulsion theft,
- instant mature colony,
- alien/combat takeover,
- larger late ontology twist,
- Maren judging her own family case.

---

# Decision

Use **I-H1** for Package I.

Next:
1. run I1~I11 targeted suites,
2. run 20-scene battery,
3. run I13 full story regression,
4. classify remaining quantitative items under I14,
5. issue final P0/P1/C2 ledger.

Only P0=0 permits progression to final quantitative micropasses and Encyclopedic Canon v2 consolidation.
