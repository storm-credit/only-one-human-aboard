# Q6 — Data Retention Classes Micropass v0.1

Status: `ENCYCLOPEDIC v2 P1 DATA MICROPASS / PROVISIONAL / NOT CANON`
Date: 2026-08-18
Project: 《우주선에는 인간이 한 명뿐이다》

Owners:
- `docs/design-v2/SOCIETY-BIBLE-v0.1.md`
- `docs/design-v2/INFRASTRUCTURE-OPERATIONS-BIBLE-v0.1.md`
- `docs/design-v2/HISTORICAL-BIBLE-v0.1.md`
- `docs/narrative-engineering/EP001-230-CONTEXT-MANIFEST-REGISTRY-v0.1.md`

Goal:
Make privacy, archive survivability, Count computation, Seed provenance and Reconstruction records coexist without creating an omniscient permanent database.

Core principle:
**Retention is purpose- and record-class-specific. There is no rule that all data is kept forever, and no rule that privacy requires deletion of all legally significant provenance.**

---

# 1. Selected Retention Architecture — DATA-H1Q

Use six broad retention classes.
Exact duration varies inside each class by statute/system owner.

| Class | Typical purpose | Retention band | Examples |
|---|---|---|---|
| D0 — Ephemeral | session / transient control | seconds → days | cache, temporary sensor fusion, unsaved personal-agent context |
| D1 — Routine Operational | maintenance / service / troubleshooting | weeks → ~2 years | ordinary transit telemetry, building systems logs, routine utility traces |
| D2 — Regulated Transaction / Case | legal/accounting/audit | ~7–30 years after closure | contracts, tax records, ordinary case files, employment records, access/audit logs |
| D3 — Life-Course Protected | care / rights / longitudinal status | life + ~30–80 years class | major medical history, guardianship, education credentials, serious disability/accommodation records |
| D4 — Vital Provenance / Continuity | identity/state/provenance integrity | effectively permanent or multi-century archival | birth/death/civic identity, parentage, Seed completion provenance, major Reconstruction status, continuity-critical evidentiary metadata |
| D5 — Constitutional / Mission / Historical | civilizational memory | permanent curated archive | laws, constitutional records, mission history, schema/version maps, major institutional decisions, public historical archives |

These are **classes**, not one universal timer.

---

# 2. D0 — Ephemeral Data

Purpose:
Keep systems responsive without turning every interaction into permanent history.

Examples:
- transient personal-agent working context,
- local interface cache,
- unsaved recommendation state,
- short-lived raw sensor fusion used only for immediate control.

Typical retention:
**seconds to days**, often overwritten automatically.

Hard:
D0 cannot later be magically recovered as a perfect century-old memory of someone's ordinary day.

---

# 3. D1 — Routine Operational Data

Purpose:
- maintenance,
- performance trending,
- incident troubleshooting,
- short-term service disputes.

Examples:
- ordinary transit vehicle telemetry,
- building HVAC/water operational traces,
- routine network-performance logs,
- nonincident industrial sensor streams.

Typical retention:
**weeks to ~2 years**, often compressed/aggregated over time.

Raw high-frequency traces may be deleted while summaries remain longer.

Hard:
Engineering telemetry is not a permanent citizen-surveillance archive.

---

# 4. D2 — Regulated Transaction / Case Records

Purpose:
- taxation/accounting,
- contracts,
- workplace disputes,
- legal audit,
- ordinary civil/criminal/administrative cases,
- security/access accountability.

Typical retention:
**~7–30 years after closure**, depending seriousness and legal need.

Examples:
- ordinary business/tax files,
- employment/pay records,
- housing transaction records,
- institutional access logs,
- finalized routine court/appeal case files.

Serious public-corruption, homicide, constitutional or precedent-setting cases may be promoted to D5 historical status rather than deleted on ordinary schedule.

---

# 5. D3 — Life-Course Protected Records

Purpose:
Support one person's long-lived rights and care across a ~100-year healthspan.

Examples:
- significant longitudinal medical history,
- allergies/chronic disease,
- major psychiatric/capacity history where legally relevant,
- disability/accommodation history,
- guardianship/adoption records,
- professional credentials,
- major education records,
- long-term care directives.

Typical retention:
**for life + roughly 30–80 years class**, with strong access controls.

Not every raw clinical measurement remains forever.
Systems may retain:
- clinically meaningful summaries,
- signed directives,
- major diagnoses/interventions,
- provenance hashes/metadata,
while deleting low-value raw detail.

---

# 6. D4 — Vital Provenance / Continuity Records

Purpose:
Preserve facts whose loss could alter legal identity, lineage/parentage, developmental provenance or continuity status.

Examples:
- birth/civic identity registration,
- legal parentage/adoption identity links,
- death/legal-finality status,
- Seed prenatal completion/noncompletion verification metadata,
- provenance chain needed to classify developmental origin,
- major Reconstruction event/status,
- Neural Anchor/Recovery Map custody and legal-status metadata where applicable,
- identity-merge/split prevention metadata,
- core civil-status change history.

Retention:
**multi-century / effectively permanent archival class**.

Critical distinction:
D4 does **not** mean every raw prenatal scan or full medical chart is permanently available.
It preserves enough authenticated provenance to establish legally significant facts.

Example Seed record may preserve:
- procedure window,
- verified completion status,
- validating provider/system signatures,
- schema/version,
- chain-of-custody/provenance,
while raw developmental sensor data may be retained under shorter protected rules unless medically needed.

---

# 7. D5 — Constitutional / Mission / Historical Archive

Purpose:
Civilizational memory and future interpretability.

Permanent curated materials include:
- constitutional/legal texts and superseded versions,
- major court/reform decisions,
- mission navigation/history,
- institutional charters,
- archive schema/version documentation,
- historical classification dictionaries,
- major disaster/reform records,
- selected public cultural collections.

Critical for Count architecture:
Old `Natural/Synthetic-Origin Cognition` schemas can remain interpretable because schema migration/version maps survive even after the category disappears from ordinary civic interfaces.

Hard:
Historical archive ≠ unrestricted personally identifying source access.
Public historical knowledge and protected individual provenance remain separable.

---

# 8. Count=1 Data Path

The lawful Count requires several domains that are normally not queried together.

Minimal conceptual crosswalk:
1. **current alive civic registry** — who is currently alive,
2. **D4 developmental-origin provenance** — whether prenatal Seed completion was verified during the relevant window,
3. **D5 schema/version maps** — how legacy categories and record formats map across centuries,
4. **independent verification** — detect missing/ambiguous/false-positive records,
5. **privacy/public-interest review** — aggregate result can be released without source identity.

This architecture explains why:
- the data can exist,
- nobody casually sees the answer,
- no conspiracy is required,
- no adult scan is required,
- public Count does not automatically publish Amara's name.

---

# 9. Why The Answer Was Not Already A Dashboard

Modern ordinary systems do not need to display developmental origin because it no longer determines civic status or normal care.

Therefore:
- current civic profiles omit/de-emphasize it,
- medical systems care about specific procedures/risks, not a public origin badge,
- archive provenance remains separate,
- legal purpose limitation discourages cross-domain curiosity queries,
- historical schema knowledge becomes specialist expertise.

A legally authorized audit can reconstruct the Count.
A casual personal agent cannot.

---

# 10. Seed Refusal Privacy

A parent's prenatal Seed refusal/completion history is protected medical/reproductive provenance.

The child/adult citizen may have rights to their own relevant developmental history.
Third-party access remains purpose-bounded.

Hard:
- refusal is not public political registration,
- no public list of unseeded families,
- no ancestry search website exposes Amara automatically.

---

# 11. Reconstruction / Recovery Map Retention

Recovery Maps are highly protected medical/continuity data.

During life:
- versioned maps may be retained as medically useful longitudinal reference,
- access is clinical/purpose-limited,
- custody/integrity metadata is D4-class.

After legal finality:
- not all executable-grade/raw clinical data must remain indefinitely,
- legally/historically necessary provenance may persist,
- destruction/retention choices can reflect directives and law,
- retained record never becomes an anchorless executable person.

Hard:
`archive kept the map` does not mean `the dead can always be restored later`.

---

# 12. Personal Right To Deletion / Correction

Meridian privacy law supports meaningful rights to:
- correct false data,
- challenge inappropriate use,
- delete/minimize data where no overriding legal/medical/public-safety purpose exists,
- know/log high-risk access,
- appeal improper cross-domain processing.

But deletion is not absolute for:
- vital identity status,
- legal parentage,
- final judgments/required public records,
- safety-critical maintenance evidence,
- constitutional/historical records,
- authenticated D4 provenance necessary to prevent identity/continuity fraud.

The legal issue becomes `what purpose justifies retention/use`, not `all data permanent` versus `all data deletable`.

---

# 13. Access Logs

Sensitive domain access itself should usually create D2/D3 audit evidence.

High-risk accesses can record:
- accessor identity/role,
- legal/clinical purpose,
- time,
- record domain,
- emergency override if any.

This supports PR-H1:
Maren's lawful emergency access can later be visible without implying she illegally hacked an archive.

Exact access-log retention years remain D2/D3 subtype detail.

---

# 14. Archive Migration / 450-Year Survivability

Permanent survival relies on:
- multiple geographic/technical copies,
- schema/version documentation,
- cryptographic/integrity lineage,
- format migration,
- periodic readability audits,
- cold/offline copies for critical data,
- institutional custody transfer.

No claim that the exact original storage medium lasts 450 years.

Historical truth survives through managed migration and provenance.

---

# 15. Failure / Missing Records

Even D4/D5 archives can contain:
- damaged entries,
- migration ambiguity,
- duplicate identities,
- incomplete provider records,
- old schema uncertainty.

Therefore the Count audit must handle:
- unknown,
- ambiguous,
- false-positive candidates,
- independent verification.

Hard:
`permanent` means institutional retention intent, not metaphysical perfect information.

---

# 16. Public vs Protected Archive

One event may have multiple record layers.

Example:
A historical Seed-rights case can have:
- public decision/precedent in D5,
- redacted case summary,
- protected medical/family source records under D3/D4.

This supports a society that remembers reforms without exposing every citizen's medical history.

---

# 17. AI Access Boundary

AI/agents only receive the data permitted for their domain/purpose.

Examples:
- transit agent: D0/D1 travel/operations, not Seed provenance,
- personal agent: user-granted personal services, not hidden government archives,
- clinical AI: relevant protected medical slice, not arbitrary civic investigation,
- audit tool: specifically authorized crosswalk inputs under review,
- policing tool: legally authorized case data, not universal citizen score.

No model receives `all D0–D5` by default.

---

# 18. Retention + Memory Culture

Private families may keep personal media for generations, but private collection survival is not guaranteed by state archive policy.

This creates ordinary differences:
- some families have rich home archives,
- some lost or deleted records,
- some preserve restored physical objects instead,
- public institutions preserve only selected cultural material.

Meridian therefore has history without perfect personal memory.

---

# 19. Hard Stops

- every camera/sensor feed permanently stored,
- one searchable database containing all D0–D5,
- privacy law deletes vital provenance needed for identity integrity,
- D4 means all raw medical data public forever,
- any personal agent can query Seed origin,
- Recovery Map retention implies resurrection from file alone,
- old schema is magically self-explanatory without migration maps,
- archive loss is impossible,
- a single corrupted record decides Count=1 without independent review.

---

# 20. Verdict

Q6 blocking P0: **0**.

Provisional v2 classes:
- D0 seconds–days ephemeral,
- D1 weeks–~2y routine operational,
- D2 ~7–30y regulated transaction/case,
- D3 life + ~30–80y protected life-course,
- D4 multi-century/effectively permanent vital provenance/continuity,
- D5 permanent constitutional/mission/historical archive.

Most important story consequence:
**The Count can be reconstructable without Meridian becoming an omniscient surveillance state.**

Status:
**`Q6 P1 = CLOSED / PROMOTE ONLY DURING v2 CONSOLIDATION`**.
