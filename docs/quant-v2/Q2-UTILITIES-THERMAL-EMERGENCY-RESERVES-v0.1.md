# Q2 — Utilities / Thermal / Emergency Reserve Quantitative Micropass v0.1

Status: `ENCYCLOPEDIC v2 P1 QUANT MICROPASS / PROVISIONAL / NOT CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

Owners:
- `canon/WORLD_BIBLE-v1.md`
- `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`
- `docs/reference-atlas/TECH-DEPENDENCY-MATRIX.md`
- `docs/reference-atlas/MERIDIAN-ENGINEERING-OVERLAY.md`

Goal:
Provide scale bands that distinguish ordinary service disruption from true survival emergency.

---

# 1. Water Demand Band

Population:
~300,000.

Ordinary delivered domestic/service water target:
**~80–120 L/person/day equivalent**
for:
- drinking/cooking,
- showers,
- toilets/sanitation,
- laundry/cleaning,
- ordinary household/service use.

Shipwide delivered domestic flow order:
**~24,000–36,000 m³/day**.

This is not net consumption because almost all enters recovery loops.

Why this level:
Meridian is a mature comfortable city, not a ration-camp spaceship.
Efficiency comes from infrastructure/recovery rather than making every shower miserable.

---

# 2. Water Recovery / Makeup

Author-facing mature-loop recovery target:
**~98.5–99.5% class for ordinary recoverable civil-water streams**, depending on contamination/process.

At 99% of 30,000 m³/day:
net civil makeup order ~300 m³/day before agriculture/industry/process accounting.

Important:
- this does not mean whole-ship matter closure = 99% forever,
- some water becomes temporarily trapped in food/material/process/people,
- some contamination requires slow recovery or discard into controlled stock,
- agriculture/ecology and industry have their own loops.

Core rule remains:
closed loops are highly efficient but imperfect.

---

# 3. Distributed Water Buffer

Do not use one tank.

Recommended service-reserve layers:

### Building / local buffer
`hours` class for pressure stabilization/brief outage.

### District / Habitat processed-water buffer
**~24–72 hours ordinary-service-equivalent** distributed across multiple tanks/loops.

For all 300k at 80–120 L/day this is total processed-service-equivalent order:
**~24,000–108,000 m³** depending on buffer duration and service level.

Mass ~24k–108k tonnes—small compared with low-10^12 kg ship mass.

### Strategic/raw water inventory
Much larger because water also serves:
- shielding,
- ecology/agriculture,
- process feedstock,
- reserve storage.

Exact total tonnes need not be frozen; it is orders larger than day-to-day potable buffer.

---

# 4. Emergency Minimal Water

For severe local service failure, emergency human minimum is far below ordinary 80–120 L/day.

Author-facing emergency support design:
- drinking/cooking critical: **~3–5 L/person/day**
- constrained hygiene/sanitation pushes real emergency service above that.

Target rule:
A Habitat can support **at least several days to ~1 week class** of highly restricted human water needs through distributed strategic reserves even when one major processing chain is unavailable, while nonessential water uses are curtailed.

This does not preserve normal agriculture/industry at full rate.

---

# 5. Oxygen / CO2 Metabolic Order

Human metabolic order:
- O2 consumption ~0.8–0.9 kg/person/day class,
- CO2 generation ~1 kg/person/day class.

Shipwide ~300k order:
- O2 metabolism ~240–270 tonnes/day,
- CO2 production comparable few-hundred-tonnes/day class.

Meaning:
life support is a major continuous industrial/ecological flow, not a small room filter.

But the Habitat atmosphere itself is a large inventory:
one plant outage does not make breathable air vanish instantly.

Operational danger during failures often appears first through:
- CO2 buildup,
- humidity/heat,
- contaminant control,
- local circulation,
not immediate total oxygen disappearance.

---

# 6. Atmosphere Processing Redundancy

Design direction:
- multiple independent processing trains per Habitat,
- no single life-support machine whose failure kills 100k residents,
- major atmospheric isolation sectors retain local sensing/control,
- cross-Habitat reserve/help possible without making all Habitats one failure domain.

Author-facing tolerance:
Loss of the **largest single atmospheric-processing train** must be absorbable through remaining capacity + demand control + repair without immediate evacuation.

Exact plant count remains C2, but `N+1-or-better at major-function level` is required.

---

# 7. Civil Power Band

Core Canon:
`multi-GW to ~10 GW order`.

Provisional operating band:
- ordinary shipwide civil average: **~6–10 GW class**
- peak/maintenance/industrial schedule can move above average within installed capacity
- this is **separate in scale/system from interstellar propulsion power**.

Per-capita equivalent including:
- agriculture,
- industrial fabrication,
- water/air processing,
- transport,
- medical/research,
- homes/services
is tens of kW/person class—plausible for a high-energy closed industrial civilization.

---

# 8. Generation Architecture

Recommended author-facing structure:
- multiple fusion generation modules / plants,
- no single unit supplies a majority of civil power,
- loss of largest unit does not cause civilization-wide blackout,
- scheduled maintenance can be carried while preserving life-safety reserve.

Planning target:
**largest single civil generation unit <~20–25% of normal ship demand**.

This does not lock reactor count/model.

---

# 9. Power Reserve Layers

### Device / room critical backup
minutes to hours depending function.

### Building / clinic / control / communications backup
**~15–60 min immediate ride-through** plus controlled shutdown/load transfer.

### District critical microgrid/storage
**~2–6 h class** for essential loads under wider distribution disruption.

### Longer outage
Handled by:
- alternate generation/distribution,
- mobile/backup generation,
- load shedding,
- repair/isolation,
not battery-only indefinite operation.

Hard:
No Habitat-sized magic battery runs normal city loads for days.

---

# 10. Load-Shedding Hierarchy

Priority order candidate:
1. immediate life support / fire / emergency control,
2. critical medicine / communications / water-air process,
3. essential food/cold-chain/sanitation/transport,
4. ordinary homes/public services,
5. schedulable industrial/commercial high load,
6. discretionary high-load leisure/experiments.

Real emergencies may reorder locally.

Economic/political consequence:
Repeated industrial shedding creates contracts, delays and labor conflict rather than being invisible.

---

# 11. Thermal Rejection Scale

Every civil GW becomes roughly a GW of waste heat after useful work.

Ideal blackbody reference:
- 300 K → ~459 W/m²
- 350 K → ~851 W/m²

For 10 GW, ideal one-sided equivalent area alone is roughly:
- ~22 km² at 300 K,
- ~12 km² at 350 K.

Real radiators require allowances for:
- emissivity,
- view factors,
- plumbing,
- redundancy,
- sun/ship geometry,
- maintenance,
- two-sided panel behavior.

Author-facing installed effective radiator order:
**~15–40 km² class for the civil thermal system**, distributed/segmented rather than one sheet.

This is intentionally large.
It makes heat rejection a legitimate arrival and maintenance bottleneck.

---

# 12. Thermal Margin

Normal operating rule:
Do not run the entire civilization at 100% rejection capacity continuously.

Provisional planning target:
**~20–40% operational/contingency thermal headroom class** under ordinary conditions, distributed unevenly by season/maintenance/load.

Final Approach can reduce comfortable margin through:
- maintenance windows,
- geometry,
- deployment staging,
- transferred equipment,
- higher industrial demand,
without requiring the engine to steal household electricity.

---

# 13. Waste / Material Return

No universal exact recycling percentage is useful across all materials.

Use material classes:
- water/air: very high continuous recovery,
- common metals/glass: high physical recycling,
- organics/nutrients: biological/chemical recovery with losses,
- polymers/composites/electronics: variable remanufacture/reprocessing,
- hazardous residues: slow controlled treatment/storage.

Hard:
`100% recycled` is forbidden.
Accumulated contamination/loss/stock management exists.

---

# 14. Maintenance Workforce Order

Working-age population order is roughly a large majority of 300k.

Direct critical physical-infrastructure/maintenance/utility/Outer-Works/fabrication workforce target:
**~15,000–25,000 people class** across all shifts/professions.

Broader technical/logistics/industrial workforce is larger.

This supports:
- continuous inspection,
- multiple shifts,
- training/apprenticeships,
- planned outages,
- 450-year system renewal.

It avoids the trope of a few hundred engineers maintaining a city-ship alone.

---

# 15. Strategic Spare Policy — No One Percentage

Use criticality classes instead of `20% spare parts`.

## S1 — Fast-failure / line-replaceable
Typical locally stocked replacement order:
**weeks to months of expected use/failure demand**.

## S2 — Long-lead precision components
Target:
**months to low-years buffer** plus local repair/remanufacture capability.

## S3 — Strategic capital / irreplaceable production chain
Protection through:
- installed redundancy,
- preserved tooling/process recipe,
- compatible substitute paths,
- strategic material stock,
not warehouses containing centuries of complete replacement machines.

Arrival conflict focuses on moving some S2/S3 capacity out of Meridian.

---

# 16. Emergency Refuge / Life-Support Duration

Q1 distributed refuge target:
~5–10% Habitat population class short-duration relocation capacity.

Facility expectation:
Refuge/safe adjacent sectors carry independent enough:
- air handling,
- emergency water,
- sanitation,
- communication,
- basic medical support
for **hours to several days depending event**, not indefinite bunker life.

Large events trigger redistribution across wider Habitat/ship systems.

---

# 17. Ordinary Failure Classes

## Utility nuisance
minutes–hours:
- hot water loss,
- local power interruption,
- network degradation.

## Significant local incident
hours–days:
- branch contamination,
- building fire,
- transfer hub closure,
- local pressure event.

## Major Habitat operational emergency
multi-system / thousands affected:
rare, invokes broader incident command and cross-zone support.

## Shipwide strategic emergency
very rare; requires true cross-system threat.

This classification prevents every outage from becoming apocalypse.

---

# 18. Hostile Checks

### Does 30k m³/day water make closed-loop impossible?
No. It is delivered flow, not net loss. High recovery and large inventory are consistent with city-scale infrastructure.

### Is 100k m³ potable buffer too massive?
~100k tonnes is tiny compared with low-10^12 kg ship-class mass and water already used as shielding/stock.

### Can 10 GW be rejected?
Yes only with very large radiator infrastructure—precisely why thermal geometry remains a strategic limit.

### Does local backup imply batteries power the ship?
No. Storage bridges short interruptions; alternate fusion/grid capacity handles long outages.

### Can 450-year maintenance work with 15–25k direct workers?
Yes as an order-of-magnitude civilization sector, combined with automation, local fabrication and broader technical/logistics labor.

---

# 19. Verdict

Q2 blocking P0: **0**.

Recommended author-facing bands:
- domestic delivered water ~80–120 L/person/day
- recoverable civil water ~98.5–99.5% class
- processed service buffer ~24–72h ordinary-equivalent
- emergency restricted water support several days–1 week class
- civil average power ~6–10 GW class
- largest single generation unit <~20–25% demand
- local critical ride-through ~15–60 min; district essential storage ~2–6h
- effective civil radiator scale ~15–40 km² class
- normal thermal headroom ~20–40% class
- direct critical physical infrastructure workforce ~15k–25k.

Status:
**`Q2 P1 = CLOSED AS PROVISIONAL QUANT BAND / PROMOTE ONLY DURING v2 CONSOLIDATION`**.
