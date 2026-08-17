# Q1 — Ship / Habitat / Transit Geometry Quantitative Micropass v0.1

Status: `ENCYCLOPEDIC v2 P1 QUANT MICROPASS / PROVISIONAL / NOT CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

Owners:
- Core: `canon/WORLD_BIBLE-v1.md`
- Infra: `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`
- Atlas: `docs/reference-atlas/MERIDIAN-CIVIC-MAP.md`, `MERIDIAN-ENGINEERING-OVERLAY.md`

Goal:
Make recurring gravity/city/transit/emergency scenes quantitatively self-consistent without freezing meter-by-meter ship CAD.

---

# 1. Locked-Band Proposal

## Each major rotating Habitat
- effective inhabited radius: **0.9–1.1 km**
- preferred design center: **~1.0 km**
- axial inhabited length: **5–7 km**
- preferred center: **~6 km**

These remain consistent with Core v1.

## Rotation / apparent gravity
For ~1 km radius and Earth-like floor gravity:
- rotation rate: **~0.90–1.00 rpm**
- preferred center: **~0.94–0.95 rpm**
- rotation period: **~60–67 s**
- ordinary main-floor gravity: **~0.95–1.0g class**

Exact three-Habitat rates may differ slightly if structural history requires it, but no Habitat should feel like a radically different gravity civilization.

---

# 2. Rotation Math Sanity

At 1,000 m radius:

`ω = sqrt(g/r) ≈ 0.099 rad/s`

This is approximately:
- `0.946 rpm`
- period `~63.4 s`

At:
- r = 900 m → ~0.997 rpm for 1g
- r = 1,100 m → ~0.902 rpm for 1g

Verdict:
Core `~1 km radius` works cleanly for ~1 rpm class Earth-like gravity.

---

# 3. Radial Gravity Gradient

At fixed angular speed, apparent gravity scales approximately with radius.

If main floor at 1,000 m = 1.0g:
- 50 m inward/up-axis → ~0.95g
- 100 m inward → ~0.90g
- 200 m inward → ~0.80g

Design consequence:
Most ordinary residential/commercial vertical development should remain within **tens of meters radial height**, not Earth-style 500 m radial skyscrapers.

Large buildings can extend axially/circumferentially more easily than radically inward.

High radial zones can still host:
- specialized facilities,
- transit/service structures,
- low-g recreation/training,
- technical access,
but should not be treated as gravity-identical to the main urban floor.

---

# 4. Coriolis Scene Sanity

At ~0.099 rad/s:
Coriolis acceleration magnitude for radial relative motion is roughly `2ωv`.

Working feel:
- walking radial component ~1.5 m/s → ~0.30 m/s² ≈ 0.03g sideways
- fast radial lift-equivalent ~5 m/s → ~0.99 m/s² ≈ 0.10g sideways

Implication:
- ordinary residents are adapted to mild spin-direction effects,
- fast radial lifts/transitions manage speed/orientation,
- low-g sports/Spine transfer need training and restraints,
- prose can occasionally show bodily familiarity without making everyone motion-sick.

Hard:
Do not explain Coriolis in every scene.
Use only where fast radial/low-g movement makes it perceptible.

---

# 5. Gross Urban Surface

For radius ~1 km:
inner cylindrical surface area ≈ `2πRL`.

At length:
- 5 km → ~31.4 km² per Habitat
- 6 km → ~37.7 km² per Habitat
- 7 km → ~44.0 km² per Habitat

Three-Habitat total gross inner surface:
**~94–132 km²**.
Preferred center at 6 km each:
**~113 km²**.

At ~300k people:
gross population density is roughly:
**~2,300–3,200 persons/km²**,
center ~2,650/km².

This is compatible with:
- mixed urban neighborhoods,
- parks/green/water spaces,
- schools/hospitals,
- technical/service land,
- agriculture/biological infrastructure where appropriate,
especially because buildings provide multi-level floor area.

Verdict:
`PASS`.

---

# 6. Household Stock Sanity

Core target:
`~120k–130k households`.

At ~300k population:
average household occupancy order:
**~2.3–2.5 persons/household**.

This fits:
- singles,
- couples,
- families with children,
- shared households,
- elders,
- temporary/recovery housing.

Author-facing residential area band:
Average occupied private dwelling floor area may broadly sit around **~45–80 m²/household equivalent**, with wide household variation.

This yields roughly `~5.5–10.4 km²` net private dwelling floor area across the whole ship before corridors/common/service space—well within the multi-level urban geometry.

Exact unit sizes remain C2 by household/class.

---

# 7. Major Transfer-Node Order

Per rotating Habitat:
- major radial/Spine passenger transfer hubs: **~4–8 order**
- preferred planning center: **~6 major hubs**
- additional local trunk stations much more numerous
- freight/hazard interfaces partly separate.

Why this range:
- enough redundancy that one hub closure does not isolate a Habitat,
- few enough for recognizable major nodes,
- compatible with 5–7 km axial city length.

Exact hub names/locations remain Atlas C2.

---

# 8. Passenger Throughput Order

Living-world cross-Habitat commuter baseline:
`~10k–30k/day`.

Author-facing capacity target:
- each major radial hub: **~1,500–4,000 passengers/hour/direction peak design class**
- combined Spine passenger system: comfortably above ordinary daily cross-Habitat demand with incident headroom.

This means the canonical `60–120m door-to-door cross-Habitat trip` is caused primarily by:
- access/walking/local feeder,
- waits,
- radial gravity transition,
- interchange,
- destination local leg,
not a slow central express.

---

# 9. Same-Habitat Travel Bands

Author-facing scene guidance:
- same-neighborhood walk/local mobility: **~5–20 min**
- ordinary same-Habitat local/trunk trip: **~15–45 min**
- far-end same-Habitat trip: **~30–60 min class** depending on transfers
- cross-Habitat ordinary door-to-door: **~60–120 min**

These are texture bands, not timetable guarantees.

---

# 10. Engineering Isolation Sector Order

Civic neighborhoods must not equal pressure sectors.

Quantitative design band per Habitat:
- major pressure/atmospheric isolation sectors: **~30–60 order**
- typical equivalent served population per major sector: roughly **~1,500–4,000** people, highly nonuniform
- buildings/rooms contain smaller local isolation boundaries beneath this layer.

Why:
- avoids one incident threatening tens of thousands by default,
- does not require thousands of giant pressure doors,
- creates manageable emergency accounting/relocation units.

Exact topology remains Q/C2 engineering work.

---

# 11. Refuge / Evacuation Headroom

No full-Habitat vacuum evacuation doctrine is required for ordinary incidents.

Reference design requirement:
- every major populated sector has at least **two independent egress directions/routes** where geometry permits,
- adjacent independent zones + dedicated refuge/public facilities together can absorb a local sector evacuation,
- Habitat-level short-duration emergency accommodation/headroom should be **at least several percent of Habitat population**, target **~5–10% class distributed**, not one giant bunker.

For ~100k citizens/Habitat this implies aggregate distributed short-duration refuge/relocation capability on order **5k–10k people**, spread across multiple zones/facilities.

This is not equivalent to permanent spare apartments.

---

# 12. Freight Separation

Passenger and freight share transfer architecture but not every corridor/time window.

Planning direction:
- **~2–4 major heavy-freight/hazard interfaces per Habitat order** plus smaller service interfaces,
- freight capacity sized above daily city demand with maintenance/arrival surge scheduling,
- hazardous/oversize cargo can use controlled time windows/routes.

Exact tonnes/hour remain C2 until an episode requires a bottleneck.

---

# 13. Gravity / Map Writer Rules

When creating a new place:
1. state civic location first,
2. only add engineering zone if plot-relevant,
3. check radial height if low-g/Coriolis matters,
4. do not make civic district = pressure sector,
5. do not assign social class by Habitat.

---

# 14. Hostile Checks

## Could 300k fit?
Yes. Gross surface-density order is moderate urban, before multi-level building floor area.

## Does 1 rpm make people constantly sick?
A ~1 km radius greatly reduces the severe small-radius rotation problem. Residents are also lifelong adapted. Fast radial movement still deserves operational design.

## Can 60–120m cross-Hab travel coexist with only ~6 km Habitats?
Yes because travel is multi-leg and includes gravity-transition/interchange, not simply distance along a flat city.

## Does one pressure sector become a class enclave?
Forbidden. Engineering sectors cut across civic/social maps.

## Can a local incident evacuate safely?
The 30–60-sector + distributed refuge/headroom model gives a plausible scale without whole-Hab evacuation.

---

# 15. Verdict

Q1 blocking P0: **0**.

Recommended v2 quantitative band:
- radius 0.9–1.1 km, center ~1.0 km
- length 5–7 km, center ~6 km
- ~0.90–1.00 rpm, center ~0.95 rpm
- main urban gravity ~0.95–1.0g
- total three-Habitat gross inner surface ~94–132 km²
- ~4–8 major passenger radial hubs/Habitat
- ~30–60 major pressure sectors/Habitat
- distributed short-duration refuge/relocation headroom ~5–10% Habitat population class.

Status:
**`Q1 P1 = CLOSED AS PROVISIONAL QUANT BAND / PROMOTE ONLY DURING v2 CONSOLIDATION`**.
