# INFRA — GEOGRAPHY / MAP / ISOLATION ARCHITECTURE — 4 DESIGNS v0.1

Status: `ENCYCLOPEDIC v2 DESIGN COMPARISON / PACKAGE C / NOT CANON`
Date: 2026-08-17

Goal:
Create a map logic that lets the author answer `where is this?`, `how do they get there?`, `what is nearby?`, and `what closes during an emergency?` without forcing exact engineering coordinates into prose.

Existing constraints:
- three large rotating 생활환, radius ~1 km order / length ~5–7 km order, exact geometry elastic.
- central non-rotating Spine.
- 1환 includes 구시가지.
- each Habitat is socially mixed.
- cross-Habitat travel 60–120m door-to-door.
- URB-H1 neighborhoods and engineering sectors are not identical.
- TRANS-H1 requires multiple major transfer/trunk nodes.
- EMG-H1 requires bounded isolation/refuge logic.

---

# DESIGN A — ENGINEERING SECTOR MAP

Everything identified primarily by axial/circumferential/deck sector coordinates.

Pros:
- precise,
- excellent operations.

Cons:
- unreadable as a lived city,
- makes ordinary dialogue technical.

Use only as hidden engineering layer.

---

# DESIGN B — PURE CIVIC DISTRICT MAP

Only historical/neighborhood names matter.

Pros:
- strong city texture.

Cons:
- difficult emergency/maintenance consistency,
- authors can accidentally place impossible routes.

Use only as public layer.

---

# DESIGN C — DUAL-OVERLAY MAP

Civic map and engineering map coexist over the same physical topology.

Pros:
- strongest realism,
- clean Obsidian/agent retrieval,
- supports emergencies and ordinary scenes simultaneously.

Cons:
- requires disciplined crosswalk.

---

# DESIGN D — LANDMARK GRAPH ONLY

Track only important story locations and travel times, not full urban topology.

Pros:
- low design overhead.

Cons:
- insufficient for encyclopedic standard and random-scene tests.

Useful as reader/story view, not full author reference.

---

# RECOMMENDED HYBRID — MAP-H1

# `Dual Civic / Engineering Overlay + Landmark Graph + Travel-Time Matrix`

Status: `PROVISIONAL PRIORITY / NOT CANON`

## 1. Physical Orientation

For authoring purposes, each rotating Habitat should be understood as having:
- an outer high-gravity inhabited band/surface where most ordinary urban life occurs,
- axial/longitudinal direction along the Habitat's long dimension,
- circumferential direction around the rotating interior,
- radial movement inward toward lower-g service/transfer structures and ultimately rotation interfaces/Spine access.

Exact architectural geometry can vary by sector.

Hard rule:
Do not depict a 1-km-radius Habitat as supporting absurd kilometer-tall `skyscrapers` toward the axis. Gravity gradient/Coriolis and structural design matter.

Ordinary buildings are mostly modest radial height relative to Habitat radius.

---

# 2. Civic Map Layer

Reader-facing hierarchy:

`생활환 → district → neighborhood → local street/building/place`

Civic names arise from:
- history,
- landscape,
- institutions,
- local function,
- old structural names that became ordinary place names.

Exact names should be locked only when recurring.

---

# 3. Engineering Map Layer

Operations track:
- pressure sector,
- structural frame/bay,
- utility zone,
- fire/smoke zone,
- transit/service corridor,
- radial level/deck,
- access category.

These layers overlap but are not necessarily identical.

An ordinary neighborhood can span multiple engineering sectors, and one pressure sector can contain pieces of two civic neighborhoods if boundaries evolved differently.

---

# 4. Habitat District Count — ELASTIC QA RANGE

Candidate scale:
- roughly 5–8 major civic districts per Habitat,
- each containing several neighborhoods,
- total recurring named neighborhoods far fewer than total real neighborhoods.

Rationale:
At ~90k–110k residents per Habitat order, a district may contain ~12k–25k people while everyday neighborhoods remain several-thousand scale.

Do not Canonize exact counts until population/map quant pass.

---

# 5. Major Transit Nodes

Each Habitat needs multiple trunk/transfer nodes so one fault does not isolate it.

Candidate authoring rule:
- at least two independent high-capacity rotation/Spine access routes per Habitat,
- more local trunk nodes distributed along the urban length,
- freight access partly separated from primary civic transfer.

Exact number remains quantitative.

---

# 6. Radial Layers

Possible broad author-facing physical bands:

### Habitable gravity band
Homes, schools, civic streets, parks, ordinary commerce.

### Service / utility layers
Building systems, distribution trunks, storage, maintenance access.

### Reduced-g technical layers
Selected industrial/logistics/transfer functions where lower gravity is acceptable/useful.

### Axis/transfer zone
Controlled interfaces toward non-rotating Spine.

This is a gradient, not four universal deck labels.

---

# 7. 1환 Map Character

Needs at minimum recurring anchors for:
- 구시가지,
- Maren home region,
- Continuity/civic/legal work cluster,
- Noah school/youth routes,
- major hospital/education/culture access,
- at least two major transfer directions.

1환 should have both heritage density and modern rebuilt districts.

---

# 8. 2환 Map Character

Needs anchors for:
- Amara home/work ecology,
- water/reclamation interfaces,
- planted/watershed public zones,
- ordinary mixed urban neighborhoods,
- clinics/schools/commerce,
- industrial ecology separated from family space.

Do not map `green` as one giant farm belt.

---

# 9. 3환 Map Character

Needs anchors for:
- technical/industrial/logistics nodes,
- rehab/medical technical presence where useful,
- shift-service districts,
- normal family neighborhoods,
- freight/Spine interface.

Do not map the whole Habitat as industrial floor.

---

# 10. Spine Map

Spine functions may include:
- inter-Habitat passenger transfer,
- freight/logistics,
- lower/zero-g work areas,
- central technical access,
- storage/industrial/service systems,
- connections to propulsion/major structural systems where physically appropriate.

Ordinary citizens may traverse the Spine without having unrestricted access to technical zones.

---

# 11. Outer Works

Not one place.
Outer Works is an author-facing category for exterior/exposed infrastructure:
- radiators,
- sensors,
- shielding elements,
- communications,
- hull/structural access,
- exterior maintenance sites.

Access requires professional training/equipment.

---

# 12. Isolation Map

Emergency map must answer:
- which pressure doors close,
- which ventilation zones isolate,
- which routes remain open,
- nearest refuge,
- alternate transit path,
- utility bypass path.

This is machine/operations metadata, not reader exposition.

---

# 13. Travel-Time Matrix

Package H should eventually store coarse ranges among recurring nodes:
- same neighborhood,
- same district,
- cross-Habitat internal,
- to Spine transfer,
- cross-Habitat.

Narrative agents should retrieve travel-time ranges rather than invent instantaneous movement.

---

# 14. Address Crosswalk

A location note should carry both:

```yaml
civic_address: 1환 / [district] / [neighborhood] / [building]
engineering_refs:
  pressure_sector: PS-...
  utility_zone: U-...
  nearest_transit_node: ...
  nearest_refuge: ...
```

Exact IDs can be generated later after map freeze.

Do not expose raw IDs in prose unless technical context requires them.

---

# 15. Historical Layering

Maps preserve old names even when function changes.
A former industrial corridor may become housing; an old service bay may become cultural space if certified.

Historical names do not imply hidden ancient machinery under every café.

---

# 16. Property / Jurisdiction Overlay

Map can additionally link:
- municipal district,
- building/co-op/public ownership,
- restricted technical zones,
- heritage designation,
- emergency authority.

No Habitat border acts like international border.

---

# 17. Arrival Map Evolution

Late story adds new nodes outside Meridian:
- orbital industrial sites,
- resource bodies,
- surface foothold,
- transport staging.

Do not collapse these into the same local map scale.
Package E will define system-level geography and travel times.

---

# 18. Obsidian Integration

Later stable location notes should link:
- characters who live/work there,
- Package C infrastructure nodes,
- active episode cards,
- relevant objects/material culture,
- emergency/utility dependencies.

Suggested families:
- `LOC-HAB-*`
- `LOC-DIST-*`
- `LOC-NBH-*`
- `LOC-INFRA-*`

Do not mass-create names before Character/History packages lock recurring locations.

---

# PROVISIONAL JUDGMENT

Best model:
**MAP-H1 — Dual Civic / Engineering Overlay + Landmark Graph + Travel-Time Matrix**

This is sufficient to support later atlas generation without prematurely hard-locking dozens of district names.

Dependencies:
- Character F recurring locations,
- D historical place names,
- exact geometry/quant QA,
- E destination system map.
