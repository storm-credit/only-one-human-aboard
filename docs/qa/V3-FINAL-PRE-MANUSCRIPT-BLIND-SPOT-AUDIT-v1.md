# V3 FINAL PRE-MANUSCRIPT BLIND-SPOT AUDIT v1

Status: `GATE AUDIT / NOT CANON / NO PROSE / NO PROMOTION`
Date: 2026-08-21
Project: 《우주선에는 인간이 한 명뿐이다》
Repository: `storm-credit/only-one-human-aboard`
Audited commit: `53b74c121a732403fb64a986ee73e1a8332ce889` (main)
Branch: `qa/final-pre-manuscript-blind-spot`

Orchestrator / final adjudicator: Claude
Independent adversarial executor: Codex CLI 0.148.0 (`codex exec`, 3 independent runs, read-only discipline, repo verified byte-identical afterward)

---

# 1. AUDIT SCOPE

This audit does **not** add design. It answers one question:

> Is the v3 architecture in a state where v3 EP001 manuscript writing can actually begin?

Explicitly out of scope and **not performed**: new worldbuilding, new Acts, 410-structure rewrite, Canon promotion, new Deep Context nodes, new supporting cast, protagonist naming, prose.

Verdict vocabulary: `GO` / `PATCH` / `NO-GO`.

Severity vocabulary:
- **P0** — writing EP001 now would break Canon / causality / branch / reveal integrity.
- **P1** — high likelihood of real damage to serialization appeal, character, genre, or early retention.
- **P2** — adjustable during writing.
- **Taste** — author preference, not a defect. Never promoted to P1 in this document.

---

# 2. SOURCES READ

## Required set
`CLAUDE.md` · `docs/NEXT-CHAT-HANDOFF.md` · `docs/current-work-status.md` · `docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md` · `docs/prewriting-v3/DEEP-CONTEXT-SCHEMA-v1.md` · `docs/obsidian-v3/deep-contexts/V3-410-DEEP-PROJECTED-CONTEXT-MANIFEST-v1.md` · `docs/qa/V3-DEEP-CONTEXT-COMPLETION-GATE-v1.md` · `docs/qa/V3-DEEP-CONTEXT-ACT-BY-ACT-QA-v1.md` · `docs/qa/V3-DEEP-CONTEXT-WHOLE-SERIES-RED-TEAM-v1.md` · `canon/ACT_BIBLE-v3.2-CANDIDATE.md` · `canon/CHARACTER_BIBLE-v3.1-CANDIDATE.md` · `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md`

## Additional set
`canon/CANON_STATUS.md` · `docs/manuscript/MANUSCRIPT-STATUS.md` · `docs/change-log.md` · `docs/change-control/PROVISIONAL-LOGLINE-vs-CANON-v2-COMPARISON.md` · `docs/change-control/CHG-052-*` · `docs/change-control/CHG-053-*` · `docs/GENRE_ENGINE_RED_TEAM-v1.md` · `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT2~9-v0.1.md` · `docs/prewriting-v3/POV-OWNERSHIP-REALLOCATION-v0.2.md` · `docs/prewriting-v3/V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1.md` · `docs/prewriting-v3/V3-MANUSCRIPT-START-READINESS-CHECKLIST-v0.1.md` · `docs/design-v3/V3-410-EPISODE-DENSITY-MAP-v0.2.md` · `docs/design-v3/V3-C2-*` · `docs/qa/V3-OBSIDIAN-GRAPH-INTEGRITY-QA-v0.1.md` · `docs/qa/V3-ACT1~9-EPISODE-BLUEPRINT-HOSTILE-QA-v0.1.md` · `docs/obsidian-v3/**` (1,427 files, bulk-scanned) · `docs/prewriting-v3/V3-COLLECTIBLE-ASSET-EXPOSURE-AND-NAMING-BUDGET-v0.1.md`

## Mechanical measurements actually executed
- 410/410 `DEEP-V3-EPxxx` and 410/410 `CTX-V3-EPxxx` node existence — verified by enumeration, 0 missing.
- 15/15 required `##` sections present in all 410 Deep sidecars.
- `NOT_SPECIFIED` / `TODO` / `FIXME` in Deep sidecars = **0**.
- 4,902 wikilink instances / 585 distinct targets / **0 unresolvable** repo-wide.
- 866 orphan notes (zero inbound wikilinks) of 1,427 notes, scoped to inbound links **originating inside `docs/obsidian-v3/`**. Widening the scan to the whole repository lowers it to 857; the conclusion is unchanged.
- 410 episode cards parsed from Act1–9 blueprints; POV, Clue, and motif fields classified.
- POV overlay v0.2 reconciled per Act (9/9 Acts reconcile exactly; total 319 + 91 = 410).

---

# 3. CLAUDE FINDINGS

| ID | Sev | Axis | Evidence | Why it breaks | Smallest fix |
|---|---|---|---|---|---|
| **C-01** | **P0** | A/B/K | `CLAUDE.md` contains **zero** occurrences of `v3`, `410`, `9 Act`, `prewriting-v3`, `design-v3`, or `V3-CURRENT-AUTHORITY-MAP`. Its §0 authority order lists only v2 files; §1 and §12 state `MANUSCRIPT IN PROGRESS`, `Accepted 10 / 230`, `First eligible episode: EP011`; §8 EP001 retrieval order names `WORLD_BIBLE-v2.md`, `CHARACTER_BIBLE-v2.md`, `ACT_BIBLE-v1.md`. `canon/CANON_STATUS.md` and `docs/manuscript/MANUSCRIPT-STATUS.md` likewise contain **zero** v3 references, and MANUSCRIPT-STATUS carries a full "EP001 Execution Contract" pointing at v2 paths. | `CLAUDE.md` is authority rank #1 and is the designed recovery entry point for a fresh session with no memory. A session that obeys it writes **v2 EP011 under the 7-Act/230 structure with Maren/Amara**, i.e. exactly the forbidden `v2 내용을 v3에 몰래 복원` failure. The only bridge to v3 is a table cell at `CLAUDE.md:409`, buried in §13. | Additive routing block in `CLAUDE.md` + one line each in `CANON_STATUS.md` / `MANUSCRIPT-STATUS.md`. Promotes nothing, changes no Canon. **APPLIED — see §14.** |
| **C-02** | **P1** | A/B/D/G | `docs/prewriting-v3/POV-OWNERSHIP-REALLOCATION-v0.2.md` header declares it "supersedes **whole-episode ownership interpretation** of individual `**POV:**` labels in Act1~9 blueprint v0.1 files". Applying its §0 rule 1 ("Episodes NOT listed as secondary-owned below are protagonist-owned"), the authoritative non-protagonist set is the `MIXED SECONDARY-OWNED` + `FULL ABSENT` bullets = **91**, so protagonist-owned = 319. Blueprint cards label only **272** as protagonist POV. The gap is **47 episodes**. Those 47 cards still read `**POV:** <secondary>`, and their Deep sidecars agree with the cards, not the overlay. The blueprint-compiled majority (`mode=blueprint-compiled`, `source_snapshot` naming only the blueprint) read e.g. `DEEP-V3-EP200:41-42` `POV: Juno/family lens` + `OFF-POV / INFLUENCE_ONLY_UNLESS_BLUEPRINT_EXPLICIT … Do not reroute success, discovery, or emotional resolution through the protagonist merely for centrality.` — identical in `DEEP-V3-EP366` and `EP408`. The few hand-authored ones differ in wording but not in effect: `DEEP-V3-EP004` is `mode=manual-body-preserved` and states `mode: INFLUENCE_ONLY / not POV`. **0 of 820** CTX/DEEP nodes reference the overlay, and the overlay is not one of the five retrieval lanes. | The documented retrieval path is `Blueprint → CTX router → Deep sidecar → max-5 payload`. A writer following it executes all 47 as secondary-POV episodes, silently reversing the change-controlled decision in `CHG-053-V3-POV-PROTAGONIST-CENTRALITY-RECALIBRATION` and dropping realized protagonist ownership from 319/410 (77.8%) to 272/410 (66.3%). It bites at **EP004** — the fourth episode. | Documentation-only precedence note naming the 47 episodes (and the 6 explicitly-retained-absent ones); enforces the overlay's own declared rule rather than creating a new one. **APPLIED — see §14.** |
| **C-03** | **P1** | C/E | `docs/change-control/PROVISIONAL-LOGLINE-vs-CANON-v2-COMPARISON.md:§3` diagnoses the author's own documented reaction: *"사용자는 미스터리 엔진이 점화되기 2화 전에 읽기를 멈췄다. '재미없다' 2회 + '장르가 다르다' 1회는 모두 같은 지점을 가리킨다."* and *"원인은 미조치 상태다."* It opens **D2 — 미스터리 실 전진 배치** (`Blueprint 조정. Canon 무변경.`), candidate: move the primer to EP005~009. `docs/change-log.md` CHG-051 records D2 as `PENDING USER DECISION`; **no later CHG executes it.** v3 then moved the opposite way: first clue PLANT = **EP022**, first mystery-thread (D05) bounded payoff = **EP028** (measured across all 42 Act1 cards; EP001–021 carry no mystery thread — `Clue:` is literally `NONE` in 19 of the 21, EP014 is an explicit *anti-mystery* payoff, EP021 permits a purely mundane false oddity), Act1 lengthened 28 → 42 episodes, and `V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1` hardens it into execution locks: *"Do not add ontology hook to make these episodes feel important."* / *"EP042 ends on an ordinary next-work state; no manufactured siren/cliffhanger."* Separately, `docs/GENRE_ENGINE_RED_TEAM-v1.md` carries an unretired verdict — **"P1 NARRATIVE-ENGINE CORRECTION REQUIRED BEFORE PROSE"**, §8 *"Act 1 — Investigation must bite earlier … Institutional friction alone is insufficient"*, target early mix Mystery 35 / Thriller 30 / Survival 20 — and its stated next gate ("bounded `ACT_BIBLE-v1 → Genre Engine Amendment` impact pass **before any further Deep Design or manuscript drafting**") has no closure record anywhere in the repo. Finally `V3-MANUSCRIPT-START-READINESS-CHECKLIST-v0.1.md:§E` now instructs *"Do not re-interview the author about: … genre"*. | This is the one place where the project's **own empirical reader evidence** points against the current design, the corrective decision was formally opened and never executed, v3 moved the ignition point ~10 episodes later in absolute terms, and the readiness checklist closes the door on re-asking. Not a taste call: it was tested and rejected by the author once. | **Cannot be patched by an auditor.** D2 is an author decision by the repo's own change-control rule. Escalated to §13/§14 as the single blocking decision. |
| **C-04** | **P2** | L | Measured: 866 / 1,427 v3 vault notes have zero inbound wikilinks — 408 `DEEP-V3-EPxxx`, 381 `CTX-V3-EPxxx`, 73 `ENTITY-*`, 4 root notes. Only **16 / 410** Deep sidecars emit a rendered `Router:` wikilink (the hand-authored subset); the 394 compiled ones carry the router only as plain-text frontmatter `source_snapshot:`, which Obsidian does not resolve. **0 / 410** `EP-V3-xxx` episode nodes link to their Deep sidecar. Only 13 wikilinks repo-wide contain `ENTITY-`, nearly all to the spec note, so all 73 collectible/institution entity nodes are graph-isolated. | The files exist and the hierarchy is logically covered, but the Obsidian **graph** is not navigable for the execution layer: no click-path EP → Deep, none EP → asset. `V3-OBSIDIAN-GRAPH-INTEGRITY-QA-v0.1.md` verifies node existence and hierarchy coverage only, and explicitly defers UI validation as "optional", so this is a declared gap rather than a contradicted claim. | Emit a `Router:`/`Deep:` link pair per node, and list entity nodes explicitly in `MOC-V3-ENTITY-STATE.md`. Mechanical, tool-generated; no design impact. Not a start blocker. |
| **C-05** | **P2** | L | `.obsidian/` exists at **repo root** (so the 860 relative cross-folder wikilinks into `docs/prewriting-v3/` resolve correctly) and is gitignored at `.gitignore:219`. `core-plugins.json` has `graph`/`backlink`/`outgoing-link` enabled. `community-plugins.json` is **absent**, so the Local REST API plugin is not installed; the `mcp-obsidian` MCP server fails with `connection refused` on `127.0.0.1:27124`. | Live Obsidian MCP inspection is unavailable this session. Vault structure itself is sound; this is an environment gap, not a repo defect. | Install/enable Obsidian Local REST API and open the vault at repo root if live MCP inspection is wanted. |
| **C-06** | **P2** | B | Seven identically-named files exist in two directories: `docs/writing-ready/EPISODE-BLUEPRINT-ACT{1..7}-v0.1.md` (v2, `EP001~028`, Maren) and `docs/prewriting-v3/EPISODE-BLUEPRINT-ACT{1..7}-v0.1.md` (v3, `EP001~042`). Both self-identify as "ACT 1 v0.1". | Path-level routing hazard for humans and agents, and it is the file `MANUSCRIPT-STATUS.md`'s EP001 Execution Contract points at. Obsidian itself is **safe**: 0 unqualified wikilinks to any colliding basename. | No rename (would break v2 history). Mitigated by the C-01 routing patch, which states the v3 path explicitly. |

---

# 4. CODEX INDEPENDENT FINDINGS

Codex ran three independent audits with no access to Claude's findings, under the instruction *"Assume this project will fail; find the evidence in this repository."*

| Codex ID | Codex Sev | Axis | Codex claim (verbatim substance) |
|---|---|---|---|
| **F-01** | P0 | A/K/B | v3 EP001 cannot begin now: `V3-CURRENT-AUTHORITY-MAP.md:25` `NOT OFFICIAL CANON / NO PROSE`; readiness checklist §D has three unchecked boxes (protagonist name, v3 promotion or explicit candidate-track order, final ≤5-source EP001 context pack); `CLAUDE.md:60-61` and `MANUSCRIPT-STATUS.md:58-62` still route to EP011. Verdict: **NO-GO**. |
| **F-02** | P1 | L | 4,902 wikilinks, **0 broken**, but **866 orphan notes** — 408 deep-contexts, 381 contexts, 73 entities, 4 root. `MOC-V3-CONTEXT-PACK.md:11-12` links only `CTX-V3-EP001 → … → CTX-V3-EP410` as an ellipsis range rather than real links; `MOC-V3-ENTITY-STATE.md:18` links only the snapshot spec. |
| **E-01** | P2 | E | Act 1 has clue cadence and qualitative guardrails but **no documented false-lead / ordinary-cause / genuine-clue ratio**. The only numeric ratio target found is for the final 60 episodes (`V3-410-EPISODE-DENSITY-MAP-v0.2:986-990`). Auditability gap, not a story blocker. |
| **I-01** | P1 | I | Formula-fatigue cluster at the Act6→Act7 seam. Worst run **EP276–289**, densest window **EP278–287**: anomaly / record / procedure / institution / unknown stacked for ~14 consecutive episodes. Cited `EPISODE-BLUEPRINT-ACT7-v0.1.md:120-125, 130-135, 154-159`. |
| **J-01** | P2 | J | `EPISODE-BLUEPRINT-ACT9-v0.1.md:42-43` — *"Exact gestation/arrival clock remains a final timeline-regression item"*; `:495-500` makes EP408 a "timeline-dependent birth/first-life milestone"; `V3-ACT9-EPISODE-BLUEPRINT-HOSTILE-QA-v0.1.md:94-99` carries an open **Timeline gate** with three unmet items. |

Codex per-axis verdicts: chunk 1 (A/B/K/L) **NO-GO**; chunk 2 (C–G) **PATCH**; chunk 3 (H/I/J) **PATCH**.

Codex counts as submitted: P0 = 1, P1 = 2, P2 = 2, Taste = 0.

---

# 5. DISAGREEMENTS — CLAUDE ↔ CODEX

| # | Item | Codex | Claude adjudication |
|---|---|---|---|
| 1 | **F-01 as a P0 defect** | P0 / NO-GO | **REJECTED as a finding.** The three unchecked boxes are the project's *intended* Gates A/B/D, deliberately held for explicit author authorization (`NEXT-CHAT-HANDOFF §9`, `V3-CURRENT-AUTHORITY-MAP §10`). A gate correctly holding closed is the system working, not a defect. Codex was not told these gates were intentional — correct behaviour for an independent auditor, but it is a category error. Reclassified to §13 Prerequisites. Codex's NO-GO verdict therefore does not stand on this basis. |
| 2 | **F-02 severity** | P1 | **ACCEPTED as P2.** Numbers independently reproduced exactly (866/408/381/73). Downgraded because it blocks graph *navigation*, not *writing*: `DEEP-V3-EP001` is self-contained and reachable by path, and `V3-OBSIDIAN-GRAPH-INTEGRITY-QA-v0.1.md` already scopes UI validation as optional. |
| 3 | **I-01 severity** | P1 | **ACCEPTED as P1, re-scoped.** Verified by reading EP280–290 directly: EP281/284/286/287/288/289/290 repeat one move — *an inherited rule/record whose origin cannot be traced* — varied only by domain, with End Turns of the shape "another domain shows the same pattern" six times consecutively. Real. But it is ~280 episodes away and is a Blueprint-grade adjustment, so it is **not** an EP001 start blocker. Filed as fix-before-Act7-lock. |
| 4 | **E-01** | P2 | **ACCEPTED as P2, with credit adjustment.** A Fair Red Herring architecture *does* exist (`NARRATIVE-DEVICE-ATLAS-v0.2/v0.3 §6/§14`, `FORESHADOW-PAYOFF-LEDGER-4-DESIGNS-v0.1 §10`, device class S5), so the design is not absent — only unsurfaced per episode. My own count: **8 / 410** cards carry an explicit false-lead, against 77 explicit `Clue: NONE` ordinary episodes. Auditability gap confirmed. |
| 5 | **C-02 (POV precedence conflict)** | **Missed initially** | Codex chunk 2 read `DEEP-V3-EP004` and cited it *approvingly* as proof of good secondary-character agency, without noticing that `POV-OWNERSHIP-REALLOCATION-v0.2` lists EP004 as converted to protagonist-owned. Claude-only finding. |
| 6 | **C-03 (mystery ignition regression)** | **Missed** | Neither Codex run traced `change-log.md` CHG-051 → `PROVISIONAL-LOGLINE-vs-CANON-v2-COMPARISON.md` D2 → v3 Act1 clue schedule. Codex chunk 2 observed "Mystery proper starts later by design: D05 at EP022" and marked it **OK** because it matched the density map — i.e. it verified internal consistency but not consistency with the project's own recorded reader-failure evidence. Claude-only finding. |
| 7 | **Size of the C-02 conflict set** | caught Claude's error | **CODEX WAS RIGHT; CLAUDE CORRECTED.** Claude's first patch listed **42** episodes, extracted mechanically from the `## Converted to protagonist-owned mixed structure` sections. That extraction was polluted: the `Reason:` prose inside those sections contains *negative* statements — Act3 "EP098 remains fully absent", Act5 "EP206 remains fully absent", Act7 "EP295 and EP301 are retained as full absence", Act9 "EP371 alone opens the final Act away from protagonist" — and Act5/Act7 list their converted episodes as prose rather than bullets. On re-verification Codex rejected the patch, naming 7 false inclusions (EP098, EP111, EP206, EP295, EP301, EP371, EP372) and 12 omissions (Act6 ×6, Act7 ×6). Recomputed from the overlay's §0 rule 1 instead of by extraction, the correct set is **47**, with exact closure: 272 blueprint-protagonist + 47 = 319. §3.1 was rewritten accordingly. |
| 8 | **319 / 77.8% POV figure** | not raised | Claude initially suspected an arithmetic error (per-Act rows appear to over-count by the `Full absent` column). **Self-corrected: no defect.** `Full absent` is a documented subset of `Secondary-owned`; all 9 Acts reconcile exactly and 319 + 91 = 410. Recorded here because the near-miss shows the figure is easy to misread. |

---

# 6. VERIFIED SEVERITY LEDGER

| ID | Severity | Owner | State |
|---|---|---|---|
| C-01 | **P0** | Claude | **CLOSED** by routing patch (§14) |
| C-02 | **P1** | Claude | **CLOSED** by precedence patch (§14) |
| C-03 | **P1** | — | **OPEN — AUTHOR DECISION REQUIRED (D2)** |
| I-01 | P1 | Codex | OPEN — deferred to Act7 lock, not a start blocker |
| C-04 / F-02 | P2 | both | OPEN — mechanical, non-blocking |
| C-05 | P2 | Claude | OPEN — environment, non-blocking |
| C-06 | P2 | Claude | Mitigated by C-01 patch |
| E-01 | P2 | Codex | OPEN — non-blocking |
| J-01 | P2 | Codex | OPEN — deferred to Act9 lock |

**Counts after adjudication: P0 = 1 (closed) · P1 = 3 (2 closed, 1 open author decision) · P2 = 5 · Taste = 0.**

No Taste item was promoted to P1. Codex's F-01 was demoted out of the ledger entirely with reasons stated.

---

# 7. FIRST-10-EPISODE FUN GATE

**Measured, not asserted.**

- All 10 cards carry a complete `Immediate Want / A-Plot / Relationship / World / Clue / End Turn / Continuity Output` set. **10/10 have a real end-turn hook**, none of which is a manufactured cliffhanger.
- Genre engines EP001–010: procedural ×4, ordinary-life ×2, civic-social ×1, relationship ×1, survival ×2. First survival payload = **EP008** (`MI-08` industrial accident, trapped worker), sustained EP008–014.
- No mystery clue exists before **EP022**. Precisely: EP001–EP021 carry no mystery thread; `Clue:` is literally `NONE` in 19 of those 21, EP014 is an explicit **anti-mystery** payoff ("PAYOFF of ordinary-accident expectation: sometimes nothing deeper is hiding"), and EP021 permits "NONE or purely mundane false oddity". First PLANT = **EP022**; first mystery-thread (D05) bounded payoff = **EP028**.
- The slow ignition is not an oversight: `V3-SCENE-REWARD-AND-REVEAL-OVERLAY-v0.1` sets EP001–014 reading promise to *"this protagonist is satisfying to watch at work"* and forbids adding an ontology hook.

**Gate result: CONDITIONAL PASS.** Per-episode craft is strong and each episode pays something. The unresolved risk is not episode quality but **ignition timing**, which is C-03 and belongs to the author.

# 8. MYSTERY / THRILLER / SURVIVAL GATE

Clue lifecycle across all 410 cards: `NONE (ordinary)` 77 · `PLANT` 28 · `REINFORCE` 81 · `PAYOFF` 75 · `AFTERSHOCK` 18 · `held OPEN` 1 · explicit `FALSE LEAD` 8 · device-coded other 122.

- "Everything looks like foreshadowing" risk: **not present.** 77 episodes are explicitly ordinary, and every Deep sidecar carries `ordinary_event_guard: HARD`.
- "Reader guesses too early": **not present.** Act1 reveal fence forbids objective confirmation of regression / branching / substrate / HUMAN:1 / Outer Ark.
- "Withholding fatigue" (`알 것 같지만 아직 설명 안 함`): **not present** — only 9/410 episodes end in a held-open state.
- Weakness: explicit false leads are sparse and the count is method-dependent — 8/410 by strict `Clue:`-field classification, 11/410 by Codex's broader red-herring keyword net (EP059, EP066, EP089, EP134, EP177, EP187, EP192, EP208, EP219, EP282, EP326). Either way it is ~2–3%, and no Act1 clue-ratio ledger exists (E-01, P2).

**Gate result: PASS with P2.** The thriller/survival promise itself starts at EP008; only the *mystery* thread is late (C-03).

# 9. CHARACTER AGENCY GATE

- Protagonist has a documented flaw with a scheduled cost: `flaw_pressure: Niko를 보호한다는 이유로 과통제하려는 성향` (DEEP-V3-EP001) → *"by EP027 protagonist's overcontrol causes a durable minor relationship cost"* (scene reward overlay). Not a passive observer, not omni-competent: EP001 `must_not_solve` fences him from commanding people or inferring hidden structure; EP010 turns on his *lack* of authority.
- Secondary cast carry independent agendas that operate in scenes, not spec sheets: Mira owns EP019 and Juno owns EP017 wholly in the protagonist's absence (both are overlay-retained `FULL ABSENT`, not among the 47 converted); Gideon is defined as `근거를 요구하는 독립 검수자` with an explicit `absolute_forbid: Gideon이 모든 답을 미리 아는 현자화`; Niko owns EP026 career stakes; Selene/Rafi own command and medical boundaries. Codex independently reached the same conclusion.
- Ensemble overload is bounded: `active_core` target ≤3 + influence-only, per the cross-system red team patch.

**Gate result: PASS**, contingent on C-02 (the 47-episode POV precedence conflict, now patched) — otherwise the ensemble reverts by default and the recalibration decision is silently lost.

# 10. CONTEXT OVERLOAD GATE

- Max-5 rule is real, not aspirational: every one of the 410 Deep sidecars ends in a fixed five-lane `Retrieval Compile Map`.
- EP001 is genuinely writable from `Blueprint card + DEEP-V3-EP001` alone — verified by reading both in full. Independently confirmed by Codex.
- Information load is disciplined: EP001–010 introduce only **8 reader-facing proper nouns** (Gideon, Juno, Mira, Niko, Selene / Old Works, Transfer Belt, Midring), against a documented ceiling of 19 active + 1 reserve. Codex measured ~8 asset targets + 6 character anchors + 3 places independently.
- `must understand` vs `just feel it` is separated by `FOREGROUND / BACKGROUND / HOLD` salience tags.
- Real overload risk is **not** volume but **layer precedence**: the POV overlay sits outside the five lanes (C-02).

**Gate result: PASS after C-02 patch.**

# 11. ACT7~8 GENRE-DRIFT GATE

- The guard exists in text (`Act guard: Action/evidence before ontology.` in all 48 Act7 sidecars; `HUMAN provenance is not personhood.` in all 43 Act8 sidecars) and Codex sampled 15 late sidecars and found it held.
- Structural anti-lecture gates confirmed at `EPISODE-BLUEPRINT-ACT7-v0.1.md:43-51` and `ACT8:47-49, 549-558`.
- Institutional-conflict motif does peak in Act8 (51% of episodes by Claude's per-episode measure; Codex's broader keyword set puts it at 35/43). The two methods disagree on magnitude but agree on direction.
- **Real defect found: I-01**, the EP276–289 seam, independently verified by Claude reading EP280–290.
- Honest limitation: the "two consecutive summarizable episodes = FAIL" rule is asserted in QA but there is **no per-episode genre-engine ledger for EP029–410** — those 382 nodes carry only a constant Act-guard line plus an identical `causal diversity guard` sentence. The rule is therefore not mechanically checkable. Recorded as an auditability observation, not inflated to a finding.

**Gate result: PASS for start; PATCH required before Act7 drafting.**

# 12. ENDING GATE

- EP406–410 read directly. No new mystery is planted: `Clue: NONE` (EP407, EP409), `no new clue. Payoff/aftershock only.` (EP410), `End State: future remains genuinely open; no thesis monologue, no cliffhanger alien reveal.`
- The quiet is deliberate and documented (`+1 / earned cautious hope`, `V3-C2-TONE-VIOLENCE-ROMANCE-ENDING-PALETTE-v0.1:196-217`) — **Taste, not a defect.**
- EP408 hands HUMAN:1 its first lived record as a child under ordinary care, with `no speech, key, authority or supernatural reaction` — the de-collectification guard holds.
- Open: **J-01**, the Act9 Timeline gate (gestation clock unlocked).

**Gate result: PASS with P2.**

---

# 13. MANUSCRIPT START PREREQUISITES

## MUST be settled before v3 EP001 prose

1. **Gate A — explicit v3 Canon promotion** (or an explicit author order to write from the candidate track). Author-only.
2. **Gate B — protagonist final name.** Author-only. Leading C2 candidate `루카스 베르너`; Canon may record `TBD` without blocking promotion, but prose cannot start on a placeholder.
3. **D2 — mystery-ignition decision (C-03).** Author-only. Either (a) execute D2 and move the first primer earlier, (b) formally close D2 with a recorded rationale for why v3's later ignition is now correct, or (c) formally retire `GENRE_ENGINE_RED_TEAM-v1`. Any of the three is acceptable; leaving all three undone is not, because it silently repeats a tested failure.
4. **Final EP001 ≤5-source context pack assembly.** Mechanical, ~minutes, no decision content.

## Safe to settle JIT during writing

- Family / district / payment surface labels (architecture already fixed).
- Violence and romance presentation levels (documented defaults exist).
- C-04 Obsidian link emission; C-05 MCP bridge; E-01 Act1 clue ledger.
- Dynamic Actual continuity fields — intentionally `PENDING`, correctly so.

## Deferred to their own Act locks

- **I-01** before Act7 drafting. **J-01** before Act9 lock.

---

# 14. CHANGES MADE ON THIS BRANCH

Two documentation-only patches. **No Canon promoted. No Blueprint card edited. No Deep Context node created or altered. No protagonist name set. No prose.**

1. **`CLAUDE.md`** — additive `§0.5 V3 TRACK POINTER` block, plus a v3 qualifier on the `10 / 230` and `EP011` statements in §1/§12; one-line v3 pointers added to `canon/CANON_STATUS.md` and `docs/manuscript/MANUSCRIPT-STATUS.md`. *Why required:* without it, authority rank #1 routes a fresh session into v2 EP011 and has no path to v3 at all (C-01, P0).
2. **`docs/design-v3/V3-CURRENT-AUTHORITY-MAP.md`** — new `§3.1 POV OWNERSHIP PRECEDENCE` section naming all 47 conflicted episodes, the 6 episodes the overlay explicitly *retains* as fully absent, and the reproducible derivation method — stating that `POV-OWNERSHIP-REALLOCATION-v0.2` governs where a card or Deep sidecar disagrees. *Why required:* enforces the overlay's own already-declared precedence, which no execution node currently references (C-02, P1). This creates no new decision.
3. **`docs/change-log.md`** — CHG-054 recording this audit and both patches, per `CLAUDE.md §13` plan-drift rule.

---

# 15. CODEX RE-VERIFICATION OF THE PATCH

Four further Codex runs were given the patched working tree and instructed to be adversarial and to try to
disprove the audit's own numbers. The patch was **rejected three times** before acceptance.

| Round | Codex verdict | What it caught |
|---|---|---|
| 1 | REJECTED | C-02 enforcement list was **42**, extracted from `## Converted…` sections whose `Reason:` prose contains *negative* statements. 7 false inclusions, 12 omissions. Also disproved four numeric claims in the audit doc. |
| 2 | REJECTED | Confirmed the corrected **47** reconciles exactly, but found §3.1 overstated that all 47 sidecars are blueprint-compiled (EP004 is `manual-body-preserved`), and three stale "42" strings remained. |
| 3 | REJECTED | Found a Korean double-negative in §3.1 that inverted its own claim ("0개가 참조하지 **않는다**"), a surviving EP004 misstatement, an internal contradiction where the audit doc used EP004 as an example of secondary agency while §3.1 converts it, and an unqualified payoff claim in CHG-054. |
| 4 | **ACCEPTED** | Final sweep clean; no disprovable claim remaining; audit doc and §3.1 mutually consistent. |

Result of round 1, retained for the record:

- **C-01 — CLOSED.** Codex independently confirmed the pre-patch state (`git show main:CLAUDE.md | grep -ci v3` = 0, same for `CANON_STATUS.md` and `MANUSCRIPT-STATUS.md`), confirmed the patch gives an unambiguous v3 path, and confirmed it promotes nothing and alters no Canon rule or v2 record.
- **C-02 — REOPENED, then fixed.** Codex confirmed the underlying conflict is real but proved the 42-episode list wrong (see §5 row 7). §3.1 was rewritten with the corrected 47 and a reproducible derivation method.
- **Collateral damage — none.** Codex confirmed the diff touches no Episode Blueprint card, no `DEEP-V3`/`CTX-V3` node, and no `canon/*BIBLE*` file.
- **Fact-checks Codex disproved, now corrected in this document:** the "first payoff EP028" phrasing (EP014 carries an anti-mystery payoff), the "EP001–021 all `Clue: NONE`" phrasing (EP014 and EP021 are not literal `NONE`), the false-lead count (method-dependent, 8 or 11), and the orphan-count scope (866 vault-internal / 857 repo-wide).
- **Fact-checks Codex confirmed:** 410 deep nodes, 410 ctx nodes, 8 proper nouns in EP001–010, first clue PLANT at EP022, 77 `Clue: NONE` episodes, and the full per-Act reconciliation of the POV overlay.

Every correction above is incorporated. This section is retained rather than deleted so the audit's own
error rate is visible to the next reader: **the first draft of this audit contained one wrong episode list
and four wrong numeric claims**, all caught by independent adversarial verification rather than by the
author. That is the intended function of the Codex role in this process, and it is the reason the
`GO / PATCH / NO-GO` verdict below should be read as evidence-backed rather than self-certified.

---

# FINAL VERDICT

# **B. PATCH — TARGETED FIXES REQUIRED**

Reasoning, stated against the evidence rather than toward a preferred answer:

- **Not `GO`.** One P0 (C-01) was live at audit time, and one P1 (C-03) remains open and is not an auditor's to close. The v3 architecture is genuinely strong — 410/410 nodes real, 15/15 schema sections, 0 broken links, 0 placeholder holes, EP001 concretely writable, information load disciplined, ending guards holding — but "strong architecture" is not the same as "cleared to start".
- **Not `NO-GO`.** Codex chunk 1 returned NO-GO, but its sole P0 was the intended Gates A/B/D holding closed, which is the system working correctly. No structural reopening is warranted: no evidence was found that the 9-Act / 410-episode structure, the ontology, the reveal lifecycle, or the character architecture needs to be reopened. Every confirmed defect is a routing, precedence, bookkeeping, or single-decision item.
- The two patchable items are patched. The remaining blocker is **one author decision (D2)**, plus the two standing gates the author already owns.

## This audit does NOT authorize

- v3 Canon promotion
- protagonist final-name selection
- manuscript drafting

Those remain separate, explicit, author-only gates, unchanged by this document.
