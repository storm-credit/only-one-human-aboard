# V3 ACT-ASSET CONTEXT PACK PATCH v0.1

Status: `EXECUTION PATCH / NOT CANON / NO PROSE`
Date: 2026-08-20
Project: 《우주선에는 인간이 한 명뿐이다》

Targets:
- `V3-ACT-TO-ASSET-DEPLOYMENT-OVERLAY-v0.1.md` section 0
- preserves `V3-CONTEXT-PACK-SPEC-v0.1.md` as governing context-cap authority.

Reason:
The first wording of the Act→Asset Overlay could be misread as adding character/relationship/place/material slices as separate direct context items and therefore exceeding the existing **5-item direct context pack**.

This patch supersedes that interpretation.

---

# Correct direct pack — MAX 5

1. **Episode Card**
   - exact current episode card.

2. **Immediate Continuity**
   - previous Continuity Output + current local chronology/state.

3. **POV / Relationship Microbundle**
   - active POV character slice,
   - at most the relationship delta(s) necessary for the scene,
   - selected from the Character→Act matrix.
   - This is ONE direct pack item, not one item per person.

4. **World / Zone / Material Microbundle**
   - one active location/institution rule slice,
   - plus only the machine/prop/place material details needed to stage current action.
   - The Act→Asset Overlay is used to choose the asset(s), but the selected material is bundled into this ONE scene-world item.

5. **Active Narrative Device / Return Microbundle**
   - exact reveal/payoff/relationship lifecycle row if active,
   - if an exact C01~C15 material return chain is active, include only that current chain segment here,
   - if no narrative device is active, this slot may instead carry one secondary-character or material-return slice.

Hard:
- direct context items remain <=5,
- 64-asset roster is NEVER a direct pack item,
- whole Act matrix is NEVER loaded into scene drafting after routing is resolved,
- whole character bible / whole asset roster / whole reveal ledger are not loaded by default.

---

# Routing workflow

Before drafting:
1. Use Act→Asset Overlay as a **router**, outside direct scene context.
2. Select the one or two material families actually active.
3. Bundle them into slot 4 or slot 5.
4. Discard the rest of the Act pool from direct context.

Example EP001:
1 Episode Card EP001
2 Immediate Continuity/opening state
3 C01 protagonist POV/work slice
4 Old Works + M01 crawler + P01/P02 field-material microbundle
5 active soft clue/relationship device only if needed

Example EP271-class neutral corridor:
1 episode card
2 Act6 continuity/geography
3 current POV + owned relationship decision
4 corridor/route/logistics material microbundle (L01/M03/P04)
5 neutral-corridor causal handoff + relevant reveal/relationship state

No extra `Mira slot`, `Juno slot`, `tug slot`, `route-tag slot` is created merely because all are causally relevant.

---

# Final

# **5-SLOT MINIMUM ACTION CONTEXT CAP PRESERVED**

The deep Act/asset maps are routing indexes, not context payloads.
