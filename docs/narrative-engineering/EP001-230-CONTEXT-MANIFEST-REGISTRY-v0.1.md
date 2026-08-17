# EP001~230 Context Manifest Registry v0.1

Status: `PACKAGE G DESIGN DATASET / PRE-PROSE / NOT CANON / NO SHADOW CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

## 0. Purpose

This registry is the **series-wide design dataset** for CP-H1 Context Packs.

It does NOT replace:
- `canon/WORLD_BIBLE-v1.md`
- `canon/CHARACTER_BIBLE-v1.md`
- `canon/ACT_BIBLE-v1.md`
- exact active Episode Blueprint
- exact locked POV Map
- `HARNESS-M1-TIME-AGE-v0.1.md`
- Deep Cards / Information Ladder / Foreshadow ledger.

Authority order:
`Canon → active Blueprint → locked POV Map → M1 → Deep Card → this registry → Sub-Act candidate map`.

Existing `episodes/EP-001~028.md` are authored example manifests.
EP029~230 individual Markdown splitting is **mechanical implementation work**, not a reason to duplicate design manually.
A later tool may split this registry only if it preserves every authority link/fence exactly.

## 1. Context Contract

Every episode Context Pack MUST load:
1. current core Canon needed by exact Blueprint,
2. exact Act Blueprint episode card,
3. exact locked POV row,
4. M1 exact execution clock/age,
5. current Sub-Act node,
6. only relevant character/location/world-rule nodes,
7. only episode-explicit narrative-device work from the Blueprint/Deep Card,
8. prior causal carry actually needed,
9. future constraint needed to prevent premature payoff,
10. the knowledge fence below.

### Critical rule — Sub-Act candidate ≠ episode exposure
A device listed as active in a Sub-Act is a **candidate scope only**.
It may enter an episode Context Pack only when the exact Episode Blueprint / Deep Card / locked ledger supports it.
Never auto-inherit every Sub-Act device into every episode.

## 2. Knowledge Fence Codes

- `F-BASE` — no knowledge beyond exact POV/public/local authority.
- `F-PRECOUNT` — Count, Amara uniqueness and legacy Human mapping are forbidden future knowledge; ordinary Seed/history texture only where Blueprint permits.
- `F-AUDIT-PROTECTED` — sealed-source reviewer scope only; no publication control and no free identity access.
- `F-AUDIT-PRIVACY` — disclosure/privacy architecture only; identity is not needed.
- `F-COUNT-INTERNAL` — authorized exact Count may be known; protected identity/provenance remains sealed.
- `F-COUNT-PUBLIC` — public aggregate `1`; Meaning is not yet fully explained and identity remains protected.
- `F-MEANING` — EP059~066 explanation ladder only; no later Amara-confirmation facts early.
- `F-AMARA-PRIVATE` — Amara may suspect/receive protected confirmation according to Blueprint; public identity remains sealed.
- `F-AMARA-PUBLIC` — controlled factual public confirmation only; no sovereignty/key/privilege.
- `F-PRH1-PREOPEN` — unfinished old preference material may exist, but exact draft/access/omission chain is forbidden.
- `F-PRH1-DISCOVERY` — use exact EP112~121 Deep Card sequence; no earlier/later reordering.
- `F-PRH1-AFTER` — changed family/ethics baseline; no retroactive self-acquittal.
- `F-ARRIVAL-LIGHT` — legacy arrival terminology may appear as mundane background only; no looming secret-crisis framing.
- `F-ARRIVAL-ACTIVE` — functional transition problem is active; current ship citizenship cannot be erased and Amara is not a key/sovereign.
- `F-INSERTION` — no alien/paradise reversal, engine miracle, sabotage climax, instant colony or hidden Amara authority.

## 3. Deep Card Codes

- `OPEN` → `DEEP-CARD-OPENING-EP001-020-v0.1.md`
- `COUNT` → `DEEP-CARD-COUNT-EP053-058-v0.1.md`
- `MEANING` → `DEEP-CARD-MEANING-EP059-066-v0.1.md`
- `AMARA-ID` → `DEEP-CARD-AMARA-IDENTITY-EP067-076-v0.1.md`
- `PR-H1` → `DEEP-CARD-PR-H1-EP112-122-v0.1.md`
- `FINAL-APP` → `DEEP-CARD-FINAL-APPROACH-EP140-148-v0.1.md`
- `HUMAN-SETTLER` → `DEEP-CARD-HUMAN-SETTLER-EP142-151-v0.1.md`
- `INSERT-END` → `DEEP-CARD-INSERTION-ENDING-EP207-230-v0.1.md`

All paths above are under `docs/writing-ready/`.

## 4. Universal Time Authority

Every row uses:
`docs/writing-ready/HARNESS-M1-TIME-AGE-v0.1.md`

Do not duplicate exact ages/dates here. If an old Blueprint shorthand conflicts with M1, M1 wins.

## ACT 1 — EP001~EP028

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT1-v0.1.md`
- POV authority: `docs/writing-ready/ACT1-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 001 | SA-1A | Maren | F-PRECOUNT | OPEN |
| 002 | SA-1A | Maren | F-PRECOUNT | OPEN |
| 003 | SA-1A | Noah | F-PRECOUNT | OPEN |
| 004 | SA-1A | Raul | F-PRECOUNT | OPEN |
| 005 | SA-1A | Maren | F-PRECOUNT | OPEN |
| 006 | SA-1A | Ella | F-PRECOUNT | OPEN |
| 007 | SA-1A | Jun | F-PRECOUNT | OPEN |
| 008 | SA-1A | Ella | F-PRECOUNT | OPEN |
| 009 | SA-1A | Noah | F-PRECOUNT | OPEN |
| 010 | SA-1B | Ella | F-PRECOUNT | OPEN |
| 011 | SA-1B | Maren | F-PRECOUNT | OPEN |
| 012 | SA-1B | Maren | F-PRECOUNT | OPEN |
| 013 | SA-1B | Ines | F-PRECOUNT | OPEN |
| 014 | SA-1B | Maren | F-PRECOUNT | OPEN |
| 015 | SA-1B | Ella | F-PRECOUNT | OPEN |
| 016 | SA-1B | Maren | F-PRECOUNT | OPEN |
| 017 | SA-1B | Maren | F-PRECOUNT | OPEN |
| 018 | SA-1B | Jun | F-PRECOUNT | OPEN |
| 019 | SA-1C | Noah | F-PRECOUNT | OPEN |
| 020 | SA-1C | Maren | F-PRECOUNT | OPEN |
| 021 | SA-1C | Ella | F-PRECOUNT | — |
| 022 | SA-1C | Maren | F-PRECOUNT | — |
| 023 | SA-1C | Maren | F-PRECOUNT | — |
| 024 | SA-1C | Maren | F-PRECOUNT | — |
| 025 | SA-1C | Raul | F-PRECOUNT | — |
| 026 | SA-1C | Jun | F-PRECOUNT | — |
| 027 | SA-1C | Noah | F-PRECOUNT | — |
| 028 | SA-1C | Maren | F-PRECOUNT | — |

## ACT 2 — EP029~EP058

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT2-v0.1.md`
- POV authority: `docs/writing-ready/ACT2-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 029 | SA-2A | Maren | F-PRECOUNT | — |
| 030 | SA-2A | Raul | F-PRECOUNT | — |
| 031 | SA-2A | Amara | F-PRECOUNT | — |
| 032 | SA-2A | Maren | F-PRECOUNT | — |
| 033 | SA-2A | Leo | F-PRECOUNT | — |
| 034 | SA-2A | Ella | F-PRECOUNT | — |
| 035 | SA-2A | Maren | F-PRECOUNT | — |
| 036 | SA-2A | Maren | F-PRECOUNT | — |
| 037 | SA-2B | Ines | F-PRECOUNT | — |
| 038 | SA-2B | Jun | F-PRECOUNT | — |
| 039 | SA-2B | Noah | F-PRECOUNT | — |
| 040 | SA-2B | Maren | F-PRECOUNT | — |
| 041 | SA-2B | Tomas | F-PRECOUNT | — |
| 042 | SA-2B | Leo | F-PRECOUNT | — |
| 043 | SA-2B | Amara | F-PRECOUNT | — |
| 044 | SA-2B | Maren | F-PRECOUNT | — |
| 045 | SA-2C | Tomas | F-PRECOUNT | — |
| 046 | SA-2C | Ella | F-PRECOUNT | — |
| 047 | SA-2C | Tomas | F-PRECOUNT | — |
| 048 | SA-2C | Raul | F-PRECOUNT | — |
| 049 | SA-2C | Kai | F-PRECOUNT | — |
| 050 | SA-2C | Tomas | F-PRECOUNT | — |
| 051 | SA-2C | Protected Reviewer | F-AUDIT-PROTECTED | — |
| 052 | SA-2C | Privacy Reviewer | F-AUDIT-PRIVACY | — |
| 053 | SA-2D | Raul | F-BASE | COUNT |
| 054 | SA-2D | Tomas | F-BASE | COUNT |
| 055 | SA-2D | Protected Reviewer | F-AUDIT-PROTECTED | COUNT |
| 056 | SA-2D | Maren | F-COUNT-INTERNAL | COUNT |
| 057 | SA-2D | Privacy Reviewer | F-AUDIT-PRIVACY | COUNT |
| 058 | SA-2D | Noah | F-COUNT-PUBLIC | COUNT |

## ACT 3 — EP059~EP088

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT3-v0.1.md`
- POV authority: `docs/writing-ready/ACT3-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 059 | SA-3A | Ines | F-MEANING | MEANING |
| 060 | SA-3A | Expecting Parent | F-MEANING | MEANING |
| 061 | SA-3A | Amara | F-MEANING | MEANING |
| 062 | SA-3A | Jun | F-MEANING | MEANING |
| 063 | SA-3A | Ines | F-MEANING | MEANING |
| 064 | SA-3A | Maren | F-MEANING | MEANING |
| 065 | SA-3A | Raul | F-MEANING | MEANING |
| 066 | SA-3A | Amara | F-MEANING | MEANING |
| 067 | SA-3B | Amara | F-AMARA-PRIVATE | AMARA-ID |
| 068 | SA-3B | Amara | F-AMARA-PRIVATE | AMARA-ID |
| 069 | SA-3B | False Candidate | F-AMARA-PRIVATE | AMARA-ID |
| 070 | SA-3B | Leo | F-AMARA-PRIVATE | AMARA-ID |
| 071 | SA-3B | Amara | F-AMARA-PRIVATE | AMARA-ID |
| 072 | SA-3B | Amara | F-AMARA-PRIVATE | AMARA-ID |
| 073 | SA-3B | Raul | F-AMARA-PRIVATE | AMARA-ID |
| 074 | SA-3B | Kai | F-AMARA-PRIVATE | AMARA-ID |
| 075 | SA-3B | Amara | F-AMARA-PUBLIC | AMARA-ID |
| 076 | SA-3B | Leo | F-BASE | AMARA-ID |
| 077 | SA-3C | Amara | F-BASE | — |
| 078 | SA-3C | Ines | F-BASE | — |
| 079 | SA-3C | Kai | F-BASE | — |
| 080 | SA-3C | Noah | F-BASE | — |
| 081 | SA-3C | Maren | F-BASE | — |
| 082 | SA-3C | Mina | F-BASE | — |
| 083 | SA-3C | Amara | F-BASE | — |
| 084 | SA-3C | Jun | F-BASE | — |
| 085 | SA-3C | Tomas | F-ARRIVAL-LIGHT | — |
| 086 | SA-3C | Ella | F-PRH1-PREOPEN | — |
| 087 | SA-3C | Leo | F-BASE | — |
| 088 | SA-3C | Amara | F-BASE | — |

## ACT 4 — EP089~EP122

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT4-v0.1.md`
- POV authority: `docs/writing-ready/ACT4-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 089 | SA-4A | Maren | F-BASE | — |
| 090 | SA-4A | Tomas | F-BASE | — |
| 091 | SA-4A | Ines | F-BASE | — |
| 092 | SA-4A | Amara | F-BASE | — |
| 093 | SA-4A | Noah | F-BASE | — |
| 094 | SA-4A | Ella | F-BASE | — |
| 095 | SA-4A | Ella | F-BASE | — |
| 096 | SA-4A | Jun | F-BASE | — |
| 097 | SA-4A | Leo | F-BASE | — |
| 098 | SA-4A | Leo | F-BASE | — |
| 099 | SA-4A | Tomas | F-BASE | — |
| 100 | SA-4A | Maren | F-BASE | — |
| 101 | SA-4B | Ella | F-PRH1-PREOPEN | — |
| 102 | SA-4B | Tomas | F-BASE | — |
| 103 | SA-4B | Amara | F-BASE | — |
| 104 | SA-4B | Ines | F-BASE | — |
| 105 | SA-4B | Raul | F-BASE | — |
| 106 | SA-4B | Tomas | F-ARRIVAL-LIGHT | — |
| 107 | SA-4B | Noah | F-BASE | — |
| 108 | SA-4B | Ella | F-PRH1-PREOPEN | — |
| 109 | SA-4B | Kai | F-BASE | — |
| 110 | SA-4B | Amara | F-BASE | — |
| 111 | SA-4B | Ella | F-PRH1-PREOPEN | — |
| 112 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 113 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 114 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 115 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 116 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 117 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 118 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 119 | SA-4C | Noah | F-PRH1-DISCOVERY | PR-H1 |
| 120 | SA-4C | Maren | F-PRH1-DISCOVERY | PR-H1 |
| 121 | SA-4C | Ella | F-PRH1-DISCOVERY | PR-H1 |
| 122 | SA-4C | Maren | F-PRH1-AFTER | PR-H1 |

## ACT 5 — EP123~EP156

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT5-v0.1.md`
- POV authority: `docs/writing-ready/ACT5-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 123 | SA-5A | Amara | F-BASE | — |
| 124 | SA-5A | Outer Works Lead | F-BASE | — |
| 125 | SA-5A | Ines | F-BASE | — |
| 126 | SA-5A | Kai | F-BASE | — |
| 127 | SA-5A | Jun | F-BASE | — |
| 128 | SA-5A | Maren | F-BASE | — |
| 129 | SA-5A | Amara | F-BASE | — |
| 130 | SA-5A | Raul | F-BASE | — |
| 131 | SA-5A | Asset Coordinator | F-BASE | — |
| 132 | SA-5B | Outer Works Lead | F-BASE | — |
| 133 | SA-5B | Leo | F-BASE | — |
| 134 | SA-5B | Noah | F-BASE | — |
| 135 | SA-5B | Kai | F-BASE | — |
| 136 | SA-5B | Jun | F-BASE | — |
| 137 | SA-5B | Maren | F-BASE | — |
| 138 | SA-5B | Tomas | F-BASE | — |
| 139 | SA-5B | Maren | F-BASE | — |
| 140 | SA-5B | Raul | F-BASE | FINAL-APP |
| 141 | SA-5C | Survey Lead | F-ARRIVAL-ACTIVE | FINAL-APP |
| 142 | SA-5C | Transition Registrar | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 143 | SA-5C | Raul | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 144 | SA-5C | Outer Works Lead | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 145 | SA-5C | Maren | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 146 | SA-5C | Kai | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 147 | SA-5C | Transition Registrar | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 148 | SA-5C | Maren | F-ARRIVAL-ACTIVE | FINAL-APP,HUMAN-SETTLER |
| 149 | SA-5D | Transition Registrar | F-ARRIVAL-ACTIVE | HUMAN-SETTLER |
| 150 | SA-5D | Amara | F-ARRIVAL-ACTIVE | HUMAN-SETTLER |
| 151 | SA-5D | Ordinary Claimant | F-ARRIVAL-ACTIVE | HUMAN-SETTLER |
| 152 | SA-5D | Jun | F-ARRIVAL-ACTIVE | — |
| 153 | SA-5D | Jun | F-ARRIVAL-ACTIVE | — |
| 154 | SA-5D | Maren | F-ARRIVAL-ACTIVE | — |
| 155 | SA-5D | Noah | F-ARRIVAL-ACTIVE | — |
| 156 | SA-5D | Maren | F-ARRIVAL-ACTIVE | — |

## ACT 6 — EP157~EP194

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT6-v0.2.md`
- POV authority: `docs/writing-ready/ACT6-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 157 | SA-6A | Maren | F-ARRIVAL-ACTIVE | — |
| 158 | SA-6A | Ella | F-ARRIVAL-ACTIVE | — |
| 159 | SA-6A | Noah | F-ARRIVAL-ACTIVE | — |
| 160 | SA-6A | Kai | F-ARRIVAL-ACTIVE | — |
| 161 | SA-6A | Leo | F-ARRIVAL-ACTIVE | — |
| 162 | SA-6A | Mina | F-ARRIVAL-ACTIVE | — |
| 163 | SA-6A | Raul | F-ARRIVAL-ACTIVE | — |
| 164 | SA-6A | Tomas | F-ARRIVAL-ACTIVE | — |
| 165 | SA-6A | Ines | F-ARRIVAL-ACTIVE | — |
| 166 | SA-6A | Jun | F-ARRIVAL-ACTIVE | — |
| 167 | SA-6A | Maren | F-ARRIVAL-ACTIVE | — |
| 168 | SA-6A | Maren | F-ARRIVAL-ACTIVE | — |
| 169 | SA-6A | Amara | F-ARRIVAL-ACTIVE | — |
| 170 | SA-6B | Surface Trainee | F-ARRIVAL-ACTIVE | — |
| 171 | SA-6B | Noah | F-ARRIVAL-ACTIVE | — |
| 172 | SA-6B | Mina | F-ARRIVAL-ACTIVE | — |
| 173 | SA-6B | Ella | F-ARRIVAL-ACTIVE | — |
| 174 | SA-6B | Amara | F-ARRIVAL-ACTIVE | — |
| 175 | SA-6B | Raul | F-ARRIVAL-ACTIVE | — |
| 176 | SA-6B | Jun | F-ARRIVAL-ACTIVE | — |
| 177 | SA-6B | Tomas | F-ARRIVAL-ACTIVE | — |
| 178 | SA-6B | Maren | F-ARRIVAL-ACTIVE | — |
| 179 | SA-6B | Maren | F-ARRIVAL-ACTIVE | — |
| 180 | SA-6B | Leo | F-ARRIVAL-ACTIVE | — |
| 181 | SA-6B | Maren | F-ARRIVAL-ACTIVE | — |
| 182 | SA-6C | Kai | F-ARRIVAL-ACTIVE | — |
| 183 | SA-6C | Noah | F-ARRIVAL-ACTIVE | — |
| 184 | SA-6C | Mina | F-ARRIVAL-ACTIVE | — |
| 185 | SA-6C | Amara | F-ARRIVAL-ACTIVE | — |
| 186 | SA-6C | Ella | F-ARRIVAL-ACTIVE | — |
| 187 | SA-6C | Ines | F-ARRIVAL-ACTIVE | — |
| 188 | SA-6C | Jun | F-ARRIVAL-ACTIVE | — |
| 189 | SA-6C | Raul | F-ARRIVAL-ACTIVE | — |
| 190 | SA-6C | Asset Coordinator | F-ARRIVAL-ACTIVE | — |
| 191 | SA-6C | Outer Works Lead | F-ARRIVAL-ACTIVE | — |
| 192 | SA-6C | Kai | F-ARRIVAL-ACTIVE | — |
| 193 | SA-6C | Transition Registrar | F-ARRIVAL-ACTIVE | — |
| 194 | SA-6C | Maren | F-ARRIVAL-ACTIVE | — |

## ACT 7 — EP195~EP230

- Blueprint: `docs/writing-ready/EPISODE-BLUEPRINT-ACT7-v0.1.md`
- POV authority: `docs/writing-ready/ACT7-EXECUTION-POV-MAP-v1.md`

| EP | Sub-Act | Locked POV | Knowledge Fence | Deep Card |
|---:|---|---|---|---|
| 195 | SA-7A | Raul | F-ARRIVAL-ACTIVE | — |
| 196 | SA-7A | Transition Registrar | F-ARRIVAL-ACTIVE | — |
| 197 | SA-7A | Raul | F-ARRIVAL-ACTIVE | — |
| 198 | SA-7A | Maren | F-ARRIVAL-ACTIVE | — |
| 199 | SA-7A | Maren | F-ARRIVAL-ACTIVE | — |
| 200 | SA-7A | Delayed Household | F-ARRIVAL-ACTIVE | — |
| 201 | SA-7A | Delayed Household | F-ARRIVAL-ACTIVE | — |
| 202 | SA-7A | Ella | F-ARRIVAL-ACTIVE | — |
| 203 | SA-7A | Leo | F-ARRIVAL-ACTIVE | — |
| 204 | SA-7A | Kai | F-ARRIVAL-ACTIVE | — |
| 205 | SA-7A | Outer Works Lead | F-ARRIVAL-ACTIVE | — |
| 206 | SA-7A | Transition Registrar | F-ARRIVAL-ACTIVE | — |
| 207 | SA-7B | Asset Coordinator | F-INSERTION | INSERT-END |
| 208 | SA-7B | Jun | F-INSERTION | INSERT-END |
| 209 | SA-7B | Kai | F-INSERTION | INSERT-END |
| 210 | SA-7B | Noah | F-INSERTION | INSERT-END |
| 211 | SA-7B | Ella | F-INSERTION | INSERT-END |
| 212 | SA-7B | Amara | F-INSERTION | INSERT-END |
| 213 | SA-7B | Outer Works Lead | F-INSERTION | INSERT-END |
| 214 | SA-7B | Navigation Lead | F-INSERTION | INSERT-END |
| 215 | SA-7B | Amara | F-INSERTION | INSERT-END |
| 216 | SA-7B | Maren | F-INSERTION | INSERT-END |
| 217 | SA-7B | Kai | F-INSERTION | INSERT-END |
| 218 | SA-7B | Surface Trainee | F-INSERTION | INSERT-END |
| 219 | SA-7C | Transition Registrar | F-INSERTION | INSERT-END |
| 220 | SA-7C | Ordinary Claimant | F-INSERTION | INSERT-END |
| 221 | SA-7C | Amara | F-INSERTION | INSERT-END |
| 222 | SA-7C | Amara | F-INSERTION | INSERT-END |
| 223 | SA-7C | Ella | F-INSERTION | INSERT-END |
| 224 | SA-7C | Noah | F-INSERTION | INSERT-END |
| 225 | SA-7C | Surface Trainee | F-INSERTION | INSERT-END |
| 226 | SA-7C | Raul | F-INSERTION | INSERT-END |
| 227 | SA-7C | Mina | F-INSERTION | INSERT-END |
| 228 | SA-7C | Leo | F-INSERTION | INSERT-END |
| 229 | SA-7C | Maren | F-INSERTION | INSERT-END |
| 230 | SA-7C | Maren | F-INSERTION | INSERT-END |

## 5. Locked Full-Series POV Regression

- Maren: **45**
- Ella: **27**
- Amara: **25**
- Noah: **17**
- Raul: **17**
- Jun: **15**
- Tomas: **13**
- Kai: **13**
- Leo: **12**
- Ines: **10**
- Transition Registrar: **7**
- Outer Works Lead: **6**
- Mina: **5**
- Asset Coordinator: **3**
- Surface Trainee: **3**
- Protected Reviewer: **2**
- Privacy Reviewer: **2**
- Ordinary Claimant: **2**
- Delayed Household: **2**
- Expecting Parent: **1**
- False Candidate: **1**
- Survey Lead: **1**
- Navigation Lead: **1**

Total: **230 / 230**.

Core locked totals:
- Maren 45
- Ella 27
- Amara 25
- Noah 17
- Raul 17
- Jun 15
- Tomas 13
- Kai 13
- Leo 12
- Ines 10
- Mina 5

## 6. Mechanical Split Contract

Future Claude Code / Obsidian implementation MAY generate:
`docs/narrative-engineering/episodes/EP-029.md` ... `EP-230.md`

But generated files must:
- use this registry row,
- fetch the exact Blueprint episode card rather than summarize from memory,
- fetch M1,
- fetch exact POV map,
- calculate active devices from **episode-explicit** Foreshadow/Payoff + Deep Card only,
- preserve AUTHOR / POV / PUBLIC / PROTECTED separation,
- fail closed if any authority is missing,
- never add Canon facts.

The split is not required to declare Package G **design dataset** complete.

## 7. Hard Reveal Regression Anchors

- EP056 — internal exact Count
- EP058 — public exact Count
- EP066 — Meaning explanation complete
- EP068 — protected Amara confirmation
- EP075 — controlled public confirmation
- EP112 — PR-H1 draft object reveal begins exact discovery chain
- EP117 — Ella POV confrontation
- EP120 — Maren POV professional accountability
- EP142~151 — Human Settler transition problem becomes operational
- EP216 — system insertion
- EP230 — no thesis speech / no ensemble recap from Maren.

## 8. Package-G Design Completion Claim

This registry completes the **series-wide retrieval/data-contract layer** for EP001~230.

It does not claim:
- 230 individual files already exist,
- prose exists,
- all v2 world candidates are Canon,
- implementation automation has been written.

Design status after QA:
`230/230 REGISTRY COVERAGE / INDIVIDUAL FILE SPLIT DEFERRED TO IMPLEMENTATION`.
