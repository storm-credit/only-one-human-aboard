# Technology / Infrastructure Dependency Matrix

Status: `PACKAGE H REFERENCE / QUALITATIVE DEPENDENCY MAP / NOT CANON`
Date: 2026-08-18

Purpose:
Show what depends on what without inventing exact engineering values.

Owners:
- `canon/WORLD_BIBLE-v1.md`
- `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`
- `docs/design-v2/DESTINATION-ARRIVAL-BIBLE-v0.1.md`

Exact reserve ratios, capacities and failure probabilities remain C2/P1 until final quantitative QA.

## Core Matrix

| System | Depends strongly on | Directly supports | If degraded | Hard guardrail |
|---|---|---|---|---|
| Civil fusion generation | fuel/reaction inputs, maintenance, control, thermal rejection | utilities, industry, hospitals, networks, transit | load shedding, maintenance deferral, production limits; not automatic ship death | not same scale/system as interstellar propulsion |
| Electrical distribution | generation, converters, switchgear, maintenance | buildings, pumps, clinics, transit, networks | local islanding/backup, priority loads | local storage ≠ indefinite Habitat power |
| Heat rejection | radiators/thermal trunks, external geometry, pumps, maintenance | every sustained power user | high-load work/industry/services constrained | waste heat cannot vanish |
| Atmosphere management | power, gas inventory, fans/pumps, sensors, scrubbers, maintenance | breathable environment | local isolation, ventilation restriction, evacuation if severe | citizens do not manually control ship chemistry |
| Water/reclamation | power, pumps, treatment media, sensors, biological/chemical process, maintenance | drinking, hygiene, food, industry, ecology | local restrictions, treatment rerouting, reserve use | closed loop high efficiency ≠ perfect recycling |
| Food/ecology | power, water, nutrient/feedstocks, climate/lighting, biotech, labor | nutrition, culture, biological buffers | menu/production changes, imports from stock, rationing only under real pressure | no default nutrient-paste civilization |
| Solid-material cycling | collection/logistics, sorting, energy, chemistry/fabrication | replacement parts, consumer goods, feedstock recovery | greater draw on strategic stocks / slower replacement | no universal replicator |
| Precision manufacturing | power, thermal, feedstock, metrology/calibration, software, skilled labor | sensors, pumps, medical/industrial/arrival parts | maintenance/arrival schedules slip; bottleneck persists despite bulk metal | local rock ≠ instant high-tech industry |
| Maintenance system | workforce, training, records, inspection, spares, fabrication | all physical systems | failure rate/backlog/risk rises over time | 450y survivability requires institutions, not immortal hardware |
| Transit | power, control/network, mechanical maintenance, structural/rotation interfaces | commuting, services, labor mobility | local rerouting/longer commute, economic effects | one transit fault ≠ Arrival Clock device automatically |
| Freight/logistics | routing, vehicles, power, access control, warehouses, network, labor | food, industry, medical, waste, arrival staging | queues/production/service delays | not identical to passenger network |
| Civic network | backbone, local nodes, power, software, security | media, services, transactions, personal comms | local fallback/degraded services | no single feed/master truth |
| Critical control networks | segmented links, certified systems, power, local fallback | utilities/industrial operation | local/manual/degraded operation where designed | not one flat civic internet |
| Archives/current registries | storage, migrations, schemas, permissions, integrity checks | law, identity, medicine, history | slower/partial access; provenance work needed | no omniscient one-database truth |
| AI/domain agents | models/software, sensors/data, compute, permissions, human accountability | optimization, routing, analysis, personal aid | manual/rules-based/degraded operation; decision quality may fall | no sovereign AI / no rights judgment by model alone |
| Robotics | power, maintenance, navigation/control, parts, work authorization | hazardous/repetitive/remote work | more human labor/risk/slowdown | robots do not imply secret citizen class |
| Medicine | power, water, sterile supply, labs, records, skilled staff | healthspan, acute/chronic care | triage/backlog/transfer pressure | advanced ≠ cure-all/immortality |
| Reconstruction | surviving Neural Anchor, Recovery Map, specialized clinical/rehab capacity, records, time | recovery after qualifying neural catastrophe | capacity queue or impossibility if anchor destroyed | no anchorless adult restoration |
| Education/training | staff, facilities/network, public funding, social stability | future workforce/civic life | skill pipeline/retraining slows | no AI destiny assignment |
| Public safety/emergency | local sensors/alarms, comms, access, trained teams, clinics, legal process | harm reduction, containment, investigation | slower response / greater local cost | no universal surveillance needed |
| Housing | structural/pressure commons, utilities, transit, maintenance | ordinary life/family stability | relocation/repair/temporary housing | private tenure ≠ hull sovereignty |
| Interstellar propulsion | dedicated propulsion plant, reaction mass, thermal/structural support, specialists, maintenance | voyage acceleration/deceleration | trajectory/time/maintenance constraints | does not directly steal household grid GW |
| Forward protection | sensing, sacrificial/mass layers, EM systems, maintenance | high-speed cruise survivability | risk envelope changes / repairs | no magic combat forcefield |
| Arrival bootstrap | precision capital, robots, power/thermal modules, logistics, skilled labor, local ISRU | orbit/surface/new habitat beginnings | slower external settlement | dismantling % alone does not equal colony speed |
| Local ISRU | survey, mining, power, transport, processing/refining | bulk water/oxygen/feedstock/metals/silicates | greater dependence on Meridian stores/assets | resource presence ≠ usable industrial supply chain |
| Orbital foothold | transport, power/comms, resource access, life support, Meridian support | depot/ISRU/logistics | expansion delay | not instant city |
| Surface foothold | transport, breathing/life support, power, water, habitat, medicine, logistics | long-term planetary presence | crew/rotation/scale restricted | habitable ≠ immediately open-air Earth life |
| New orbital habitat | years of material processing, industry, structures, life support, governance/population | future additional city | schedule slips first under resource constraints | not completed by series ending |

---

# High-Leverage Couplings

## Power ↔ Heat
More generation/use without rejection margin is not free usable capacity.

## Water ↔ Food ↔ Waste
Water recovery and nutrient/feedstock cycling couple domestic life to ecology, but citizens experience normal services rather than daily survival engineering.

## Manufacturing ↔ Maintenance
Strategic resilience depends on making/reconditioning parts, while precision manufacturing itself requires calibration/maintenance.

## Network ↔ Physical Control
Networks improve coordination, but critical physical systems retain segmentation/local fallback to avoid single common-mode failure.

## AI ↔ Accountability
Automation may improve operations, but rights/legal responsibility remains assigned to humans/institutions.

## Reconstruction ↔ Birth / Housing / Rehab Capacity
These can compete for some physical/social capacities, but they are not one tradable `life slot` commodity.

## Arrival ↔ Meridian Redundancy
Transferring precise capital/spares/thermal/power assets can accelerate external bootstrap while making Meridian less redundant.

## Local Bulk Resources ↔ Meridian Precision Capital
The destination eventually supplies mass; Meridian supplies early sophistication. Neither replaces the other immediately.

---

# Failure-Propagation Rule

For scene design, ask:
1. What failed locally?
2. What isolation/fallback exists?
3. What dependent service degrades first?
4. Which reserve/time/labor is consumed?
5. At what threshold does authority escalate?

Do NOT jump directly from `component fault` to `shipwide apocalypse` unless exact design supports a cascade.

---

# Exact Values Still Open

Do not infer from this matrix:
- exact MW per district,
- exact water reserve days,
- exact radiator square kilometers,
- exact network node counts,
- exact spare percentage,
- exact emergency refuge capacity,
- exact colony MW/GW sizes.

Those remain final quantitative tasks owned by Packages C/E/I and later Canon v2 consolidation.
