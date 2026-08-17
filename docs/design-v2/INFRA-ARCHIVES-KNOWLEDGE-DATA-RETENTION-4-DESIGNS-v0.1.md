# INFRA — ARCHIVES / KNOWLEDGE / DATA RETENTION — 4 DESIGNS v0.1

Status: `ENCYCLOPEDIC v2 DESIGN COMPARISON / PACKAGE C / NOT CANON`
Date: 2026-08-17

Scope:
- civic records,
- historical archives,
- scientific/technical knowledge,
- personal records,
- legal/medical/education retention,
- provenance and chain-of-custody,
- public vs protected access,
- schema migration over 450 years,
- preservation against bit rot and institutional drift.

Existing story requirements:
- no single database contains the whole Count answer.
- legacy origin/provenance terms survive in older schemas.
- modern civic registries do not casually expose protected origin provenance.
- cross-institution audit can lawfully compute Count after verification.
- public aggregate release does not include Amara's name.

---

# DESIGN A — ONE IMMUTABLE CIVIC LEDGER

All authoritative records preserved in one append-only system.

Pros: consistency, provenance.
Cons: destroys mystery plausibility, privacy, and institutional evolution; unrealistic over 450 years.

Reject.

---

# DESIGN B — FULLY DECENTRALIZED ARCHIVE PATCHWORK

Every institution keeps its own history.

Pros: organic historical drift.
Cons: too fragile; important civilization knowledge would be lost constantly.

Reject as sole architecture.

---

# DESIGN C — FEDERATED AUTHORITATIVE RECORDS + DEEP ARCHIVAL SNAPSHOTS

Current operational registries remain domain-owned, while historical snapshots, legal archives and technical repositories preserve prior states/provenance.

Pros:
- strongest fit with Count audit,
- privacy-compatible,
- realistic schema migration,
- supports long-term preservation.

---

# DESIGN D — CURATED KNOWLEDGE COMMONS

Public/scientific/cultural knowledge is actively curated and migrated; protected personal/admin records are separately governed.

Pros: prevents digital dark age.
Cons: if overcentralized, archivists become truth priesthood.

Use as complement.

---

# RECOMMENDED HYBRID — ARC-H1

# `Federated Current Registries + Deep Versioned Archives + Curated Knowledge Commons + Protected Provenance Layers`

Status: `PROVISIONAL PRIORITY / NOT CANON`

## 1. Record Families

### R1 — Current civic registries
Examples:
- identity/citizenship,
- residence,
- family/legal status,
- current licenses/credentials.

Optimized for current administration, not complete historical truth.

### R2 — Domain records
Examples:
- medical,
- education,
- employment,
- courts,
- utilities/operations.

Owned/governed by domain institutions.

### R3 — Historical archival snapshots
Preserve prior schemas, policies, institutional states and selected record snapshots.

### R4 — Scientific/technical knowledge repositories
Engineering manuals, research, standards, models, calibration histories, mission data.

### R5 — Cultural/public knowledge commons
Literature, media, public documents, historical collections, museum/catalog material.

### R6 — Personal/private archives
Citizen-controlled or household-controlled personal materials subject to separate succession/privacy law.

---

# 2. No Single Truth Database

Hard rule:
A current registry contains what the current institution needs, not every historical attribute ever known.

Example:
Modern civic identity may not display `Natural/Bio-Origin Cognition` because the category lost ordinary administrative relevance.
Older medical/provenance/legacy legal systems may preserve related historical fields for different reasons.

This is institutional evolution, not conspiracy.

---

# 3. Schema Migration

Over 450 years, systems undergo:
- field renaming,
- category retirement,
- normalization,
- data-format migration,
- legal-purpose changes,
- provider consolidation/splits.

Best practice preserves:
- source schema,
- mapping rules,
- migration logs,
- confidence/ambiguity flags.

But not every migration is perfect.
Some historical categories cannot be mapped one-to-one into modern concepts.

This is the technical basis for IL-H1 and Count fairness.

---

# 4. Preservation

Long-term preservation uses multiple strategies:
- redundant storage locations,
- periodic integrity checks,
- format migration,
- cold/offline copies for critical knowledge,
- versioned snapshots,
- physically separated disaster copies,
- printed/physical/manual emergency references for selected safety-critical procedures.

No single data-center fire can erase civilization memory.

---

# 5. Bit Rot / Corruption

Digital preservation is active work.
Failure modes remain:
- incomplete old media recovery,
- corrupted files,
- missing metadata,
- bad migrations,
- ambiguous timestamps,
- lost context.

Critical legal claims should not depend on one conveniently corrupted secret file.

---

# 6. Public Access

Publicly accessible by default or broad access:
- laws/regulations,
- public meeting records,
- many court decisions with privacy redaction,
- historical/cultural collections,
- public statistics,
- research/public technical standards where safe,
- journalism/media archives.

Protected:
- medical files,
- minor records,
- private communications,
- sealed family matters,
- sensitive identity mappings,
- security-sensitive technical details.

---

# 7. Aggregate vs Identity Access

Critical story distinction:
A system/process may lawfully compute an aggregate count without exposing names to every analyst.

Possible architecture:
- approved query runs inside protected domain,
- result returns aggregate/statistical output,
- identity linkage remains separately permissioned,
- exceptional verification can be performed by a small authorized team with audit logs.

This directly supports Count=1 publication without government name dump.

---

# 8. Provenance / Chain of Custody

Professional records preserve:
- source,
- creation time,
- modification history,
- access history where legally required,
- signatures/authentication,
- version.

This supports PR-H1:
Maren's lawful access metadata can exist without proving criminal intent.

---

# 9. Access Logs

Not every harmless document view is public.
High-sensitivity records may retain audited access metadata.

Access logs themselves are protected records with oversight access.

No recursive universal surveillance: logging is scoped by system sensitivity.

---

# 10. Right to Correction vs Historical Integrity

Citizens can challenge inaccurate current records.
Correction does not necessarily erase the fact that an old record once existed.

Possible approach:
- current record corrected,
- prior version preserved under restricted archival provenance,
- dispute annotation retained.

This avoids both memory-hole history and permanent public scarlet letters.

---

# 11. Personal Deletion / Privacy

Citizens may delete or limit some personal/private materials and personal-agent memory.
They cannot demand deletion of every lawfully required:
- court judgment,
- vital status,
- tax/business record,
- medical safety record,
- public office act,
subject to retention/minimization rules.

Exact retention terms remain law-detail elastic until consolidation.

---

# 12. Records After Death / Reconstruction

Death changes access and succession but does not instantly erase records.

Reconstruction can require controlled access to relevant medical/continuity material.
Returning personhood does not automatically grant unrestricted access to every descendant/private file created during absence.

Property/family privacy rules still apply.

---

# 13. Knowledge Commons

Meridian actively preserves:
- Earth-origin knowledge,
- ship-born science,
- engineering experience,
- medicine,
- cultural works,
- multiple languages/traditions,
- historical failures.

A 450-year mission cannot rely on passive file accumulation; curation, education and redundancy are civilization infrastructure.

---

# 14. Technical Manuals / Live Operations

Critical systems maintain:
- current certified procedures,
- historical change logs,
- failure case library,
- calibration data,
- fallback/manual procedures.

Operators do not use 300-year-old manuals merely because they are archival.

---

# 15. Archive Specialists

Professional roles include:
- archivists,
- records engineers,
- data stewards,
- historians,
- provenance specialists,
- conservation staff.

They are not a secret priesthood.
They disagree, make mistakes, and operate under law/oversight.

---

# 16. Search AI

AI-H1 may assist:
- semantic search,
- old-language translation,
- schema crosswalk suggestions,
- duplicate detection,
- provenance tracing.

But:
- model inference is not itself legal evidence,
- ambiguous mapping remains flagged,
- protected access still requires permission,
- no model can invent missing provenance as fact.

---

# 17. Historical Public Curiosity

After Raul/public cases expose old terms, ordinary journalists/researchers can search public historical records and ask why old schemas used multiple origin fields.

They still cannot immediately retrieve protected current identities.

This supports fair pre-Reveal public curiosity.

---

# 18. Physical Archives / Artifacts

Digital archives coexist with:
- original paper/books,
- physical legal artifacts,
- analog media,
- museum objects,
- heritage equipment.

Material Culture provenance links to archival metadata but neither automatically proves the other.

---

# 19. Security-Sensitive Knowledge

Some operational details may be access-limited:
- vulnerability maps,
- security credentials,
- hazardous process specifics.

Restriction cannot be used to hide broad civic facts or suppress embarrassment without legal basis.

---

# 20. Arrival Transition

Before/after insertion:
- critical knowledge sets are replicated to new orbital/surface sites,
- local caches support communication outages,
- jurisdiction determines which records are copied vs merely referenced,
- privacy and archival continuity must survive institutional splitting.

No new settlement begins with a magical full duplicate of every protected database and no governance plan.

---

# PROVISIONAL JUDGMENT

Best model:
**ARC-H1 — Federated Current Registries + Deep Versioned Archives + Curated Knowledge Commons + Protected Provenance Layers**

This preserves:
- Count fairness,
- privacy,
- 450-year history,
- no conspiracy requirement,
- no single truth file.

Dependencies:
- exact retention law,
- historical era migration events,
- destination replication/jurisdiction,
- archive capacity/physical redundancy quant.
