# MANUSCRIPT STATUS

Project: 《우주선에는 인간이 한 명뿐이다》

Pipeline:
`docs/manuscript/MANUSCRIPT-PIPELINE-v1.md`

Official rule:
Only `manuscript/accepted/` + this ledger count as completed manuscript.

---

# Current Summary

- Accepted: **0 / 230**
- Work Draft: **0**
- QA Review: **0**
- Revision Required: **0**
- Canon Review: **0**
- Recheck Required: **0**
- Published: **0**

Next eligible episode:
**EP001**

Manuscript drafting has not started because user has not explicitly requested prose.

---

# Act Progress

| Act | Episodes | Accepted | Current State |
|---|---:|---:|---|
| Act1 | EP001~028 | 0/28 | NOT_STARTED |
| Act2 | EP029~058 | 0/30 | NOT_STARTED |
| Act3 | EP059~088 | 0/30 | NOT_STARTED |
| Act4 | EP089~122 | 0/34 | NOT_STARTED |
| Act5 | EP123~156 | 0/34 | NOT_STARTED |
| Act6 | EP157~194 | 0/38 | NOT_STARTED |
| Act7 | EP195~230 | 0/36 | NOT_STARTED |

---

# Active Episode

`NONE`

When drafting starts, record:
- episode
- state
- work path
- accepted path if any
- POV
- QA result
- latest revision reason
- downstream recheck if any

---

# Episode Ledger

No episode entries yet.

Add only when an episode enters DRAFT or later state.

Recommended entry format:

```markdown
## EP001
- State: DRAFT | QA_REVIEW | REVISION_REQUIRED | QA_PASS | ACCEPTED | RECHECK_REQUIRED | CANON_REVIEW
- POV: Maren Vale
- Work: manuscript/_work/act01/EP001.md
- Accepted: manuscript/accepted/act01/EP001.md | none
- Episode QA: docs/manuscript/qa/EP001-QA.md | none
- Last updated: YYYY-MM-DD
- Notes:
```

---

# Completion Rule

Never infer completed count from:
- chat history
- `_work`
- Blueprint
- QA file alone

An episode is complete only when Accepted path + ledger both agree.
