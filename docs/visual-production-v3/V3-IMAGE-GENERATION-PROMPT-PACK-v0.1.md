# V3 IMAGE GENERATION PROMPT PACK v0.1

Status: `PRODUCTION PROMPT SPEC / NOT CANON / NO PROSE / TOOL-AGNOSTIC`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. 목적

이 문서는 특정 이미지 생성기 하나에 종속되지 않는 **재사용 가능한 프롬프트 구조**를 정의한다.

핵심:
- 외부 작품 이름을 최종 프롬프트의 필수조건으로 쓰지 않는다.
- 외부 인물/작품은 연구 단계에서만 참고한다.
- 실제 생성 프롬프트는 Meridian-native 설명으로 다시 작성한다.
- Identity Lock과 Shot/State를 분리한다.

---

# 1. UNIVERSAL STYLE LOCK

아래 블록은 특별한 이유가 없는 한 모든 캐릭터/기체/배경 concept QA에 공통 적용한다.

```text
2D semi-real animation / game-concept illustration,
clean controlled line art,
moderate realistic anatomy and material detail,
not photorealistic,
not chibi,
not exaggerated superhero anatomy,
production concept-art presentation,
clear silhouette readability,
functional industrial/civic design,
subtle future technology integrated into lived everyday use,
no franchise logos,
no real-company branding,
no excessive cinematic effects during neutral QA.
```

Negative:

```text
photoreal portrait,
hyper-detailed skin pores,
aged beyond specified age,
all characters sharing the same handsome/pretty face,
combat armor,
weapon-centric design,
military tactical fantasy,
humanoid battle mecha,
fighter-jet styling for utility machines,
neon cyberpunk default,
sterile white sci-fi everywhere,
dark metal corridor everywhere,
RPG rarity glow,
faction-color coding as primary identity,
text-heavy fake infographic,
unreadable AI gibberish labels.
```

---

# 2. CHARACTER — NEUTRAL CONCEPT SHEET TEMPLATE

## Input fields

```text
ASSET_ID:
ROLE:
AGE_BAND:
BODY:
FACE_GEOMETRY:
JAW_CHEEK:
NOSE:
EYES_BROWS:
HAIR_MASS:
POSTURE:
CORE_CLOTHING:
KEY_PROP:
MATERIAL_ANCHOR:
COLLISION_AVOID:
SPOILER_CLASS:
```

## Master prompt

```text
Create a neutral 2D semi-real character concept sheet for [ASSET_ID].

ROLE / LIFE:
[ROLE]

IDENTITY LOCK:
- apparent age: [AGE_BAND]
- body structure: [BODY]
- face geometry: [FACE_GEOMETRY]
- jaw/cheek structure: [JAW_CHEEK]
- nose structure: [NOSE]
- eyes/brows: [EYES_BROWS]
- hair mass/silhouette: [HAIR_MASS]
- posture/movement baseline: [POSTURE]
- core clothing construction: [CORE_CLOTHING]
- key professional/personal prop: [KEY_PROP]
- material anchor: [MATERIAL_ANCHOR]

DIFFERENTIATION:
Must not collapse toward [COLLISION_AVOID].
Face and body must remain distinguishable even with hair color and clothing color removed.
Do not use ethnicity as costume shorthand.
Do not force a nationality unless explicitly defined.

PRESENTATION:
- light neutral background
- flat honest concept lighting
- one full-body neutral standing view
- one large face close-up
- one 3/4 or side profile
- one small ordinary-work pose
- one prop/equipment detail if relevant
- minimal labels only
- no dramatic poster composition

STYLE:
[UNIVERSAL STYLE LOCK]

AVOID:
[UNIVERSAL NEGATIVE]
```

---

# 3. C01 PROTAGONIST — CURRENT CALIBRATION CARD

Status: `STYLE CALIBRATION ONLY / FINAL FACE TBD`

```text
ROLE:
late-30s hull/ship damage analyst; civilian technical field specialist.

AGE:
37~39 apparent.

BODY:
lean practical adult body; active field worker, not soldier, not athlete-model.

FACE:
long-oval to lightly rectangular adult face; attractive but grounded; no idol perfection; no heavy aging; clean-shaven or near-clean.

ENERGY:
calm, observant, skeptical, methodical; still has forward-moving protagonist energy.

POSTURE:
neutral standing posture is relaxed; during inspection he leans forward and reads surfaces with concentrated attention.

CLOTHING:
short practical field jacket, work trousers, robust work shoes/boots; equipment attachment should read professional, not tactical combat.

PROP:
narrow hard field case / damage-analysis kit.

CURRENT STYLE CALIBRATION:
retain the clean readability of Proposal A and the field-worker solidity of Proposal C.
Do not copy either sample face.
Do not fix ethnicity or nationality from the sample.

HARD AVOID:
looks 45+,
photoreal actor portrait,
heavy beard,
special-forces harness,
hero armor,
Korean/East-Asian default without reason,
exact likeness of a real actor.
```

---

# 4. CHARACTER — SAME-FACE QA TEMPLATE

Generate characters under intentionally restrictive conditions.

```text
Create a neutral comparison concept for [CHARACTER].
Use the exact same light, background, camera distance, neutral fitted gray work layer, and expression intensity used for the comparison set.
Do not use signature clothing, dramatic hair styling, jewelry, props, or color to rescue identity.
Show:
- front neutral head
- 3/4 head
- side profile
- shoulder-up neutral silhouette
- simple full-body silhouette

Identity must come from bone/mass/proportion/posture, not styling.
```

Required first comparison set:
- C01 Protagonist
- C13 Arun
- C07 Gideon
- C11 Ivo

---

# 5. MACHINE — NEUTRAL FAMILY SHEET TEMPLATE

## Input fields

```text
ASSET_ID:
ROLE:
MASS_CENTER:
MOVEMENT_OR_ANCHOR:
MANIPULATOR_LOGIC:
PAYLOAD_LOGIC:
INTERFACE_LINEAGE:
SILHOUETTE_HOOK:
SCALE_CUE:
COLLISION_AVOID:
STATE:
```

## Master prompt

```text
Create a neutral 2D semi-real industrial machine concept sheet for [ASSET_ID].

FUNCTION:
[ROLE]

IDENTITY LOCK:
- center of mass: [MASS_CENTER]
- movement/anchoring: [MOVEMENT_OR_ANCHOR]
- manipulator logic: [MANIPULATOR_LOGIC]
- payload/access logic: [PAYLOAD_LOGIC]
- shared Meridian interface ancestry: [INTERFACE_LINEAGE]
- unmistakable silhouette hook: [SILHOUETTE_HOOK]
- scale cue: [SCALE_CUE]

CURRENT STATE:
[STATE]

DIFFERENTIATION:
Must not visually collapse toward [COLLISION_AVOID].
Its job should be readable without color, logo, model number, weapon, or cockpit glamour.

PRESENTATION:
- light neutral background
- grayscale or muted neutral colors
- 3/4 view
- side view
- top/front silhouette if useful
- one functional detail/cutaway
- one scale reference
- no cinematic action scene

AVOID:
weapon mounts,
combat-mecha proportions,
fighter nose/canopy,
hero cockpit,
random greeble overload,
color-only family identity.
```

---

# 6. FIRST MACHINE QA CARDS

## M01 Structural Crawler

```text
low and wide body,
multiple clamps/contact points,
short close-work tools,
body visually hugs structure,
maintenance access visible,
not spider-monster styling,
not mapping-drone silhouette.
```

## M02 Mapping Drone

```text
light flat tri-lobed/plate-like mass,
sensor field dominates,
minimal heavy manipulation,
clear aerial/local-guided sensor role,
not barrier-drone folding panel,
not weapon drone.
```

## M03 Utility Tug

```text
load/coupling geometry dominates,
workhorse proportions,
obvious rear/side hitch or cargo interface,
repairable industrial body,
not sleek van,
not rescue-skiff casualty geometry.
```

## M04 Rescue Skiff

```text
protected central volume organized around casualty access,
patient cradle/module interfaces visible,
rapid-access doors/arms,
medical/rescue function before style,
not freight tractor,
not armored personnel carrier.
```

---

# 7. ENVIRONMENT — RECOGNITION SHEET TEMPLATE

## Input fields

```text
ASSET_ID:
PRIMARY_USE:
GEOMETRY:
DOMINANT_MOTION:
PUBLIC_PRIVATE_RATIO:
LIGHT:
MATERIAL_AGE:
ACOUSTIC_IMPLICATION:
LANDMARK_HOOK:
MERIDIAN_SHARED_ANCESTRY:
COLLISION_AVOID:
```

## Master prompt

```text
Create a 2D semi-real environment concept sheet for [ASSET_ID], part of the same long-lived civic civilization called Meridian.

FUNCTION:
[PRIMARY_USE]

IDENTITY LOCK:
- spatial geometry: [GEOMETRY]
- dominant movement/use: [DOMINANT_MOTION]
- public/private ratio: [PUBLIC_PRIVATE_RATIO]
- light logic: [LIGHT]
- material age: [MATERIAL_AGE]
- implied sound/activity: [ACOUSTIC_IMPLICATION]
- landmark hook: [LANDMARK_HOOK]
- shared Meridian ancestry: [MERIDIAN_SHARED_ANCESTRY]

Must remain visibly one civilization while being immediately distinguishable from [COLLISION_AVOID].

PRESENTATION:
- one wide establishing view
- one human-scale eye-level view
- one detail/material vignette
- ordinary people doing ordinary activities
- avoid cinematic disaster unless state block requests it
- no text labels required to identify the place

AVOID:
biome palette coding,
identical metal corridors,
empty architectural showroom,
every surface glowing,
cyberpunk neon default,
Old Works industrial language copied into every district.
```

---

# 8. FIRST ENVIRONMENT QA CARDS

## L01 Transfer
- layered passenger bridges above/around freight flows
- directional movement visible in architecture
- high-wear surfaces
- crowd/vehicle rhythm

## L02 Midring
- human-scale shared courtyard
- balconies + school route + small services + seating
- personalized repair/history
- domestic sound and irregular movement

## L03 Garden
- broad engineered lightwell
- open vertical volume
- terraces, leisure, planting, movement
- structural skeleton still visible

## L04 Med/University
- patients + students + families + clinicians coexist
- rehabilitation/training/teaching visible
- civic/public medical place, not lab

## L05 Old Works
- multiple generations of panels/adapters/repairs
- tight service geometry
- physical work markings
- old does not mean dirty ruin; it means layered maintained history

---

# 9. PROP SHEET TEMPLATE

```text
Create a 2D semi-real prop design plate for [PROP_ID].
Show closed/idle state, in-use state, and one material/detail breakdown.
The object must look like something people actually handle, maintain, repair, lose, replace, and personalize.
Do not make it mystical, luxurious, weapon-like, or universally important unless the story explicitly requires it.
Show wear derived from [OWNER/ROLE/STATE].
```

---

# 10. COLLECTIBILITY FAMILY COMPARISON TEMPLATE

```text
Create a lineage comparison sheet for [FAMILY_ID].
Show only meaningful states/generations authorized by the Asset Manifest.
Each version must share unmistakable family interface ancestry while differing for real function, era, scarcity, repair history, or settlement adaptation.
Do not use rarity colors, cosmetic skins, power-rank labels, or arbitrary upgraded armor.
Presentation should make the viewer want to inspect ancestry and use history rather than compare combat stats.
```

---

# 11. SHOT / STATE BLOCK TEMPLATE

Identity Lock는 유지하고 아래만 컷별로 교체한다.

```text
SHOT:
- camera:
- framing:
- pose/action:
- expression:
- environment:
- light:

STATE:
- Act/time:
- wear/damage:
- temporary equipment change:
- emotional condition:
- spoiler class:
```

---

# 12. PROMPT QA BEFORE GENERATION

생성 전에 반드시 확인:

1. Identity Lock이 포함됐나?
2. 외부 작품명 없이도 디자인이 설명되나?
3. 특정 실존인물 얼굴 복사를 요구하지 않나?
4. 다른 자산과의 collision-avoid가 적혔나?
5. 나이/체형이 의복보다 먼저 정의됐나?
6. 기체는 기능이 실루엣을 만드는가?
7. 장소는 색을 지워도 구분되는가?
8. 이번 생성이 정말 필요한가?
9. 생성 결과를 Visual QA에 넣을 계획이 있는가?

하나라도 NO면 프롬프트를 먼저 수정한다.

---

# FINAL

이 Prompt Pack의 목표는 `한 번 예쁜 그림 생성`이 아니라 **다른 생성도구/다른 시점/다른 작업자에서도 같은 디자인 언어를 재현하는 것**이다.
