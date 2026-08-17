# P1 Q-DEST — Science / Logistics Hostile Red Team v0.1

Status: `P1 CLOSURE QA / PACKAGE E / PRE-CANON-v2`
Date: 2026-08-18

Target:
`docs/design-v2/P1-Q-DEST-SCIENCE-LOGISTICS-CLOSURE-v0.1.md`

---

## RT-01 — Does current astronomy actually confirm the story's rocky planet?
No.

The file explicitly separates:
- real Epsilon Indi A,
- currently confirmed distant giant Epsilon Indi Ab,
- fictional future mission-era rocky settlement world/resource families.

This avoids false real-world astronomy claims.

Verdict: `PASS`.

---

## RT-02 — Is 0.52 AU plausible around Epsilon Indi A?
Using representative modern archive values near ~0.75 M☉ / ~0.24 L☉:
- incident flux at 0.52 AU is ~0.89 Earth,
- orbital period is ~158 Earth days.

The selected ~0.50–0.54 AU / ~150–165d band is internally coherent.

Verdict: `PASS`.

---

## RT-03 — Does 29.5h rotation require tidal-lock special pleading?
No strong issue.
At ~0.52 AU around a K dwarf, the world is far enough out that a non-synchronous ~day-scale rotation is not inherently implausible.
The exact tidal/moon history remains C2.

Verdict: `PASS`.

---

## RT-04 — Is ~0.97g compatible with ordinary rocky composition?
Yes.
~1 M⊕ / ~1.015 R⊕ gives ~0.97g order with ordinary density.
The allowed ~0.9–1.1 M⊕ / ~0.98–1.05 R⊕ band avoids exotic composition.

Verdict: `PASS`.

---

## RT-05 — Does low oxygen accidentally prove a complex biosphere?
The selected atmosphere deliberately **does not** require altitude-like ~10–15% O2.
It keeps atmospheric oxygen far below safe human breathing and leaves exact fraction C2.

Therefore:
- outdoor mask/rebreather rule is stable,
- atmospheric O2 alone need not announce a mature photosynthetic biosphere,
- microbial/abiotic survey ambiguity remains possible.

Verdict: `PASS`.

---

## RT-06 — Can humans really be outside without pressure suits?
Yes if:
- ambient total pressure is roughly 85–110 kPa,
- bulk atmosphere is not acutely skin/eye-corrosive,
- breathable O2 is supplied by mask/hood/rebreather,
- thermal/weather protection is conventional environmental clothing.

Loss of breathing support is still an acute emergency.

This is physically distinct from both:
- Earth-breathable outdoors,
- Mars/vacuum full-pressure EVA.

Verdict: `PASS`.

---

## RT-07 — Is the climate overly precise without a model?
The file uses broad author-facing bands (~5–12°C global mean direction / temperate settlement regions) and leaves exact albedo/CO2/regional climate C2.

No exact climate curve is claimed.

Verdict: `PASS`.

---

## RT-08 — Is an active dynamo guaranteed?
No.
The file calls ~0.3–1 Earth field an author-facing candidate, not measured fact.
Surface habitability also benefits from near-Earth-order atmospheric column.

P1 is sufficiently closed because story only needs:
- surface long-term radiation manageable,
- orbit/resource radiation materially worse.

Exact field strength remains C2.

Verdict: `PASS`.

---

## RT-09 — Is Meridian's 30k–80k km high orbit inside the Hill sphere?
Strongly yes.
For ~Earth-mass at ~0.52 AU around ~0.75 M☉, Hill sphere is ~0.8–0.9 million km order.
30k–80k km is comfortably inside.

It also avoids absurd `giant city skims the atmosphere` imagery.

Verdict: `PASS`.

---

## RT-10 — Does the high-orbit transfer cost make surface settlement impossible?
No.
High↔low planetary orbit is few-km/s class.
Surface ascent remains expensive; descent can use atmospheric braking.

This is a feature:
- orbit first,
- surface slower,
- small Year-1 population.

Advanced future propulsion/tugs make repeated transfer possible without making it free.

Verdict: `PASS`.

---

## RT-11 — Resource Δv wording risk
Risk found:
The v0.1 M/V resource numbers say `after leaving local planetary gravity well`, which can be misread as excluding the ~1 km/s-class escape increment from high parking orbit.

Repair rule for v2 consolidation:
- treat M/V listed values as **heliocentric rendezvous leg** class,
- add roughly **~1–2 km/s local escape/capture maneuver order** depending staging/assist/vehicle,
- author-facing full mission budget from Meridian high orbit therefore remains **several-km/s class**, not the lower leg value alone.

No story architecture changes.

Verdict: `PASS WITH WORDING REPAIR REQUIRED`.

---

## RT-12 — Are volatile-rich bodies plausible near a warm inner system?
The design does not require exposed comet ice at 0.52 AU.
It explicitly allows:
- hydrated minerals,
- carbonaceous material,
- protected/interior volatiles,
- somewhat more distant/eccentric bodies.

Verdict: `PASS`.

---

## RT-13 — Are 30k–100k tonnes deployed in Year 1 too much for a tiny settlement?
Not necessarily.
This is **industrial hardware/cargo**, not housing mass per resident.
The majority can be:
- power/thermal modules,
- tugs/landers,
- shielding,
- processing equipment,
- depot structure,
- robots,
- feedstock/consumables.

At the upper band, sustained heavy cargo operations are required, so this remains an author ceiling rather than default exact total.

Recommended center:
- total external deployed mass **~40k–70k t** if an exact planning value is later needed,
- surface share **~8k–15k t**.

Verdict: `PASS AS WIDE BAND / CENTER SUGGESTED`.

---

## RT-14 — Does hundreds-MW power make external sites cities already?
No.
Early industrial bootstrap is power-heavy per resident.
Power supports:
- processing,
- oxygen/water,
- robotics,
- construction,
- vehicles,
- communications,
- shielding/thermal infrastructure.

A 300-person industrial depot can use far more power per person than a mature residential district.

Verdict: `PASS`.

---

## RT-15 — Does 250–700 simultaneous off-Meridian contradict `Meridian overwhelming majority`?
No.
Out of ~300,000 citizens, 700 is ~0.23%.
Meridian still holds >99.7% of people.

Even 1k–3k unique personnel rotated through sites over a year does not mean permanent migration.

Verdict: `PASS STRONG`.

---

## RT-16 — Does Year-1 cargo/population imply mature surface city?
No.
Surface remains:
- tens-to-low-hundreds MW industrial foothold,
- ~80–250 simultaneous people,
- controlled indoor habitats,
- breathing support outdoors,
- limited medical depth,
- weather/launch dependence.

New habitat remains construction program only.

Verdict: `PASS`.

---

## RT-17 — Does the atmosphere make local oxygen impossible?
No.
Abundant water supports electrolysis/oxygen generation once power/process equipment is online.
This reinforces local bulk-resource advantage while preserving imported precision-capital dependence.

Verdict: `PASS`.

---

## RT-18 — Does the giant confirmed planet dominate early settlement dynamics?
No.
Current confirmed Ab is distant and background-only.
The fictional inner rocky/resource architecture can be designed independently for early settlement.

Hard:
do not turn Ab into late monster-planet twist unless Canon reopened.

Verdict: `PASS`.

---

# Required Repair Before Closure

Only one wording repair is required:

### QR-1 — Resource mission Δv semantics
Change:
M/V values should not look like complete high-orbit-to-asteroid mission budgets if they exclude planetary escape/capture.

Lock:
- M and V table values = favorable **heliocentric rendezvous leg** order,
- local planet escape/capture/staging adds roughly ~1–2 km/s-class maneuver burden depending trajectory,
- full missions remain several-km/s class.

No new P0.

---

# Remaining C2

- exact atmosphere fractions,
- exact climate map,
- exact magnetic field/moons,
- exact Meridian orbit,
- exact asteroid elements/names,
- exact fleet/propulsion,
- exact cargo total within band,
- exact Year-1 census within ceiling.

---

# Verdict

Blocking P0: **0**.

P1 Q-DEST:

# `PASS WITH ONE NON-ARCHITECTURAL WORDING REPAIR`

After QR-1 is applied, Q-DEST is ready for v2 consolidation.
