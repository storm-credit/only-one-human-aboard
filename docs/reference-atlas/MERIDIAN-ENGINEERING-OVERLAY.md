# Meridian Engineering / Isolation Overlay

Status: `PACKAGE H REFERENCE / NAVIGATION ONLY / NOT CANON`
Date: 2026-08-18

Purpose:
Engineering-facing topology behind the civic city.

This is deliberately separate from [Meridian Civic Map](./MERIDIAN-CIVIC-MAP.md).
A neighborhood/district is not automatically identical to a pressure, fire, utility or emergency sector.

Owner:
- `canon/WORLD_BIBLE-v1.md`
- `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`

## 1. Layer Model

```text
Civic place
   │
   ├─ building/local systems
   │    ├─ fire/smoke control
   │    ├─ local electrical distribution
   │    ├─ water/waste connections
   │    └─ local ventilation/comfort
   │
   ├─ district engineering layer
   │    ├─ utility isolation
   │    ├─ emergency routes/refuge
   │    ├─ transit/service interfaces
   │    └─ pressure/air management interfaces
   │
   ├─ Habitat strategic layer
   │    ├─ bulk atmosphere
   │    ├─ water inventory/process
   │    ├─ major distribution
   │    ├─ thermal trunks
   │    └─ structure/rotation
   │
   └─ shipwide / Spine / external layer
        ├─ generation and major distribution
        ├─ strategic stores
        ├─ inter-Habitat interfaces
        ├─ radiators / Outer Works
        ├─ propulsion-support logistics
        └─ arrival deployment staging
```

Topology is relational only. Exact sector/node counts are `C2-ELASTIC`.

---

# 2. Pressure / Atmosphere

Architecture direction:
- strategic gas inventory and processing,
- Habitat/district circulation,
- local building conditioning,
- room comfort control.

Safety principle:
localized isolation limits propagation; a room/building incident does not automatically depressurize a Habitat.

Automatic physical safeties may isolate a danger zone according to predefined conditions.
Prolonged civic restrictions remain human-reviewable.

Exact pressure-sector geometry/count: `C2-ELASTIC`.

---

# 3. Fire / Smoke / Toxic Gas

Engineering response family:
- detection,
- local suppression,
- process/power isolation,
- smoke/ventilation control,
- controlled evacuation/refuge,
- trained response.

Fire boundaries may cut across civic naming in ways citizens normally do not think about.

A map scene should not assume:
`one neighborhood = one fire sector`.

---

# 4. Water / Wastewater

Hierarchy:
- strategic inventory,
- bulk treatment/reclamation,
- Habitat/district distribution,
- building/local fixtures,
- differentiated wastewater streams,
- nutrient/feedstock recovery,
- controlled residue.

2환 has more visible watershed/reclamation identity, but water is a shipwide commons system.

Hard:
Amara is a normal skilled mid-level worker/shift lead, not sole water savior.

---

# 5. Power

Known Canon order:
- distributed civil fusion,
- multi-GW to ~10GW order,
- critical loads protected before discretionary loads,
- local storage supports bridging/safe shutdown, not indefinite Habitat operation.

Engineering topology:
`generation → strategic distribution → Habitat/district networks → building/local → critical backup/islands`.

Propulsion is a separate high-output scale.
Do not draw one household breaker panel connected directly to interstellar thrust.

---

# 6. Thermal

Every consumed power ultimately becomes heat.

Topology:
`local/building heat collection → district/Habitat thermal trunks → reuse where practical → radiator/rejection infrastructure`.

Thermal margin constrains:
- industrial schedules,
- maintenance,
- high-load services,
- arrival preparation.

Exact radiator area/margins remain final quantitative work.

---

# 7. Solid Material / Waste Cycling

Operational hierarchy:
`repair → reuse → component recovery → material recycling → feedstock conversion → secure residue`.

Hazardous streams require controlled handling.
No universal matter replicator makes logistics irrelevant.

---

# 8. Transit / Rotation Interfaces

Movement hierarchy:
- local walking/mobility,
- district transit,
- Habitat trunks,
- controlled radial transition toward lower gravity,
- rotation-to-Spine interface,
- Spine express/logistics,
- target Habitat reverse transition.

Engineering map must show `interface` conceptually rather than invent exact elevators/rings/shaft counts before quant freeze.

Low-g transition is physically real and accessibility-aware.

---

# 9. Passenger vs Freight

Passenger and freight systems overlap at service interfaces but important bulk/hazardous freight is buffered/separated where practical.

Controlled streams include:
- hazardous materials,
- waste/recycling,
- industrial components,
- strategic arrival cargo.

This permits a passenger delay without implying every freight operation stops, and vice versa.

---

# 10. Network Segmentation

NET-H1 V2-CANDIDATE:
- redundant civic backbone,
- segmented critical domains,
- permissioned gateways,
- local fallback.

Important separation:
- life-support telemetry,
- medical/provenance records,
- civic/public networks,
- personal communications,
- industrial control

are not one flat network with one omniscient search box.

Count audit requires lawful cross-domain/schema work rather than one universal query.

---

# 11. AI / Automation Placement

AI-H1 is federated/domain-bounded.

Typical roles:
- anomaly detection,
- routing/scheduling,
- predictive maintenance,
- simulations,
- operator assistance,
- bounded personal assistance,
- predefined physical safety automation.

No map node labeled `Central Ship AI` should exist as sovereign controller.

---

# 12. Maintenance / Work Control

OPS-H1:
- predictive/preventive/corrective maintenance,
- mixed public/co-op/specialist workforce,
- inspection/calibration,
- work authorization in hazardous systems,
- strategic spares,
- training/succession.

A 450-year ship survives through an economy/institution of maintenance, not miraculous original hardware.

---

# 13. Emergency Scope

EMG-H1 severity is hazard-based:
1. site/routine incident,
2. local emergency,
3. district/Habitat emergency,
4. shipwide strategic emergency.

Authority scales with physical scope and later narrows/expires.

Do not escalate every incident to shipwide command.

---

# 14. Outer Works / External Infrastructure

External engineering includes:
- forward protection,
- radiators/thermal rejection,
- sensing,
- external maintenance,
- selected industrial/staging infrastructure,
- propulsion-support geometry/logistics.

Outer Works access is specialized and controlled.

During final approach/insertion, exterior work windows can narrow without requiring catastrophe.

---

# 15. Arrival Transition Overlay

Late-voyage engineering adds:
- detachable/bootstrap equipment staging,
- strategic spare allocation,
- orbital depot/resource packages,
- small surface package,
- retained Meridian reserve floors.

Key tradeoff:
**industrial bootstrap speed vs Meridian redundancy/city capacity**, not `scrap all ship or fail`.

---

# 16. Unknown / Final-Quant Items

Remain `C2-ELASTIC` until final quantitative QA:
- exact pressure-sector count/volume,
- exact refuge capacities,
- exact transfer node count/capacity,
- exact water/gas reserve margins,
- exact electrical islanding duration,
- exact thermal reserve/radiator margins,
- exact maintenance workforce/spares ratio,
- exact rotation/radial-transfer geometry.

Do not fill these from aesthetic convenience during prose.

---

# Hard Map Guardrails

- civic map ≠ engineering map,
- no Habitat caste,
- no one-flat-network,
- no central sovereign AI,
- no whole-Habitat failure from every apartment incident,
- no perfect isolation that makes cascade risk impossible,
- no propulsion/civil-grid conflation,
- no magical self-repairing ship.
