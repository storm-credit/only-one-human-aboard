# V3 CONTEXT PACK SPEC v0.1

Status: `PREWRITING EXECUTION INFRA / NOT CANON`
Project: 《우주선에는 인간이 한 명뿐이다》

Purpose:
Provide the minimum episode-writing context needed to execute one v3 episode without loading the entire repository or inventing new Canon.

Design principle:
**Minimum Action Agent OS — Local Context / Action Space control.**

Do NOT create 410 redundant giant context files that copy the same World/Character Bible text.
Use one episode card + small referenced slices.

---

# 0. Episode execution context — maximum direct pack

Default direct context pack contains at most **5 items**:

1. **Episode Card**
   - exact EP section in the active Act blueprint
2. **Immediate Continuity**
   - prior episode Continuity Output + current Act continuity state
3. **POV Character Slice**
   - only the active POV's profile/voice/private-life/knowledge fence
4. **World/Zone Slice**
   - only the active location/institution/system rules needed in the scene
5. **Active Narrative Device Slice**
   - only clues/payoffs/relationship arcs active in this episode

If the episode does not use a series-level device, item 5 may instead be a second active-character relationship slice.

Hard:
No `load all Canon + all character files + all reveal files` by default.

---

# 1. Authority router

Before episode execution, global authority is resolved once through:
`docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md`

Do not count the Authority Map as a direct scene-writing action after routing is resolved.

Official v2 remains official until v3 promotion; prewriting execution explicitly uses the v3 candidate branch only.

---

# 2. Episode Card source

Act blueprint files:
- Act1 `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md`
- Act2 `...ACT2-v0.1.md`
- Act3 `...ACT3-v0.1.md`
- Act4 `...ACT4-v0.1.md`
- Act5 `...ACT5-v0.1.md`
- Act6 `...ACT6-v0.1.md`
- Act7 `...ACT7-v0.1.md`
- Act8 `...ACT8-v0.1.md`
- Act9 `...ACT9-v0.1.md`

Each episode card already contains:
- POV,
- time,
- zone,
- immediate want,
- action,
- relationship,
- world movement,
- clue state,
- knowledge fence where needed,
- end turn,
- continuity output where material.

This is the primary execution source.

---

# 3. Immediate Continuity source

Use:
- previous episode card,
- current band summary,
- current Act local state.

For Acts2/6 add dedicated chronology/geography ledger:
- `V3-ACT2-CONCURRENCY-GEOGRAPHY-CAUSAL-LEDGER-v0.1.md`
- `V3-ACT6-CONCURRENCY-GEOGRAPHY-CAUSAL-LEDGER-v0.1.md`

For full-series time-sensitive scenes use:
`docs/prewriting-v3/V3-FULL-SERIES-TIMELINE-v0.1.md`

Hard:
Do not reread the whole previous Act unless a continuity contradiction appears.

---

# 4. POV Character Slice routing

Primary character authority:
`canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md`

Supporting current slices:
- `docs/design-v3/V3-CORE-CAST-MULTI-LINEAGE-MATRIX-v0.1.md`
- `docs/design-v3/V3-CORE-VOICE-PRIVATE-LIFE-SHEETS-v0.1.md`
- `docs/design-v3/V3-PROTAGONIST-FAMILY-AND-MIRA-ENDPOINT-CLOSURE-v0.1.md`
- `docs/design-v3/V3-CORE-RELATIONSHIP-NETWORK-v0.1-CANDIDATE.md`

Routing:
- ordinary scene → Character Bible + voice/private-life slice
- alternate-history testimony → multi-lineage slice
- relationship turning point → relationship network slice
- protagonist family/Mira current endpoint → closure file

Do not load all four unless the episode genuinely needs all domains.

---

# 5. World / Zone Slice routing

Use only one main world source per scene where possible.

Examples:

## Old Works / infrastructure
- experienced geography addendum
- relevant economy/work or governance authority boundary only if needed

## Transfer Belt / logistics
- geography + economy/resource slice

## home/family/school
- family/reproduction/lifecycle slice

## Civic/legal/security
- governance/law/emergency slice

## Act7 substrate reveal
- ultradense ontology consolidation + science boundary only for author accuracy

## Act8 HUMAN medical
- HUMAN biological/attrition source + medical plausibility pass

## Act9 settlement
- settlement embodiment source + Act9 science repair source

Hard:
Reader prose should not inherit author-only vocabulary merely because the source is loaded.

---

# 6. Active Narrative Device routing

Primary:
`docs/narrative-engineering/V3-REVEAL-FORESHADOW-PAYOFF-LEDGER-v0.4-CANDIDATE.md`

Secondary only if needed:
`docs/narrative-engineering/NARRATIVE-DEVICE-ATLAS-v0.3-CANDIDATE.md`

Writer constraints:
`docs/narrative-engineering/WRITER-GRAMMAR-MATRIX-v0.3-CANDIDATE.md`

Default:
Use exact active device row, not entire ledger.

Examples:
- EP041 → Arun tiny mismatch only
- EP093 → C4 trigger only
- EP213 → HUMAN:1 count field only
- EP318 → rare-memory integrity payoff only
- EP321 → uncountable-lineage scale only

---

# 7. Knowledge-fence classes

## K0 — Ordinary civic
No hidden-history knowledge.

## K1 — Local anomaly
Knows one contradiction but no mechanism.

## K2 — Multi-history evidence
Knows incompatible histories may be real; no substrate scale.

## K3 — Lineage/substrate partial
Act7 technical/rights actors after earned reveal.

## K4 — HUMAN / D3 rights operational
Act8 protected investigators/operators.

## K5 — Settlement operational
Act9 actors know current rights/settlement rules; still no author omniscience.

Hard:
A POV can know less than the current Act's reader.
No POV automatically inherits reader knowledge.

---

# 8. Secondary POV eligibility check

Before a non-protagonist POV episode:
1. does the person have an immediate want independent of exposition?
2. would honest interiority spoil a reveal before its gate?
3. does this POV add new action/consequence rather than replay?
4. is the person already seeded unless surprise is intentional?
5. does the episode preserve protagonist story primacy across the Act?

If any fail, convert to protagonist/external lens or move POV later.

---

# 9. Prose-time action-space cap

Default writer node sees no more than these direct callable actions:
1. Draft scene/episode
2. Query active Canon slice
3. Query continuity/reveal slice
4. Run episode QA
5. Record continuity/change

Total direct action space = **5**.

If more is needed:
remove unnecessary source → bundle into slice → defer research → route through QA.

Do not add new Agents merely because the project is large.

---

# 10. Post-draft episode QA package

After a draft eventually exists, run only:
1. episode-card compliance,
2. continuity check,
3. POV/knowledge-fence check,
4. clue/relationship lifecycle check,
5. style/engagement check.

Escalate to full Canon regression only if a contradiction-level change is found.

---

# 11. Context retention

Record after every accepted episode:
- changed relationship states,
- injuries/deaths,
- access/resource changes,
- clue lifecycle movements,
- public knowledge changes,
- offscreen state changes relevant to next episode.

Do not copy full episode prose into status files.

---

# 12. Current verdict

**V3 MINIMAL CONTEXT-PACK ARCHITECTURE = PASS.**

The existing detailed episode cards make 410 separate duplicate context files unnecessary at this stage.

If a future execution environment requires physical per-episode manifest files, materialize them mechanically from this spec + episode cards rather than rewriting design manually.