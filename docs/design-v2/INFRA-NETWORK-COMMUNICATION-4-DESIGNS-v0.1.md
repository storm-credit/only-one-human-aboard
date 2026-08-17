# INFRA — NETWORK / COMMUNICATION — 4 DESIGNS v0.1

Status: `ENCYCLOPEDIC v2 DESIGN COMPARISON / PACKAGE C / NOT CANON`
Date: 2026-08-17

Scope:
- local wired/wireless networks,
- personal communications,
- public internet-like services,
- institution networks,
- emergency communications,
- external/ship-to-space communication,
- identity/authentication,
- resilience and privacy.

---

# DESIGN A — ONE SHIPWIDE NETWORK FABRIC

Everything shares one highly redundant network.

Pros: simple, fast, universal.
Cons: catastrophic security/authority coupling; too easy to create omniscient data layer.

---

# DESIGN B — FULLY SEGMENTED DOMAIN NETWORKS

Health, transit, utilities, public web, government, industry all largely separate.

Pros: strong security/privacy.
Cons: poor interoperability, unrealistic civic inconvenience.

---

# DESIGN C — FEDERATED LAYERS WITH SECURE GATEWAYS

Shared civic backbone + domain segmentation + controlled cross-domain gateways + strong identity/permission layers.

Pros: best fit for AI-H1 and privacy law.
Cons: gateway governance is complex.

---

# DESIGN D — PERSONAL MESH DOMINANT

Citizen devices form decentralized peer-to-peer infrastructure.

Pros: resilient/anti-centralized.
Cons: weak fit for critical infrastructure and authoritative records.

Use as resilience supplement, not primary architecture.

---

# RECOMMENDED HYBRID — NET-H1

# `Redundant Civic Backbone + Segmented Critical Domains + Permissioned Gateways + Local Fallback`

Status: `PROVISIONAL PRIORITY / NOT CANON`

## 1. Network Layers

### Public/civic layer
- messaging,
- media,
- commerce,
- education access,
- public services,
- ordinary browsing/search.

### Institutional protected domains
- health,
- courts/legal,
- schools,
- employment/admin,
- archives,
- identity registries.

### Operational critical domains
- utilities,
- transit control,
- life support,
- structural monitoring,
- industrial systems.

### Research/sandbox domains
Used for experimentation without direct control authority over critical systems.

---

# 2. Backbone

Meridian uses multiple physical paths through Habitats/Spine:
- fiber/optical links,
- local wireless,
- hardened service trunks,
- redundant switching nodes.

Major zones can continue basic local operation during partial backbone failure.

No assumption that wireless alone carries civilization.

---

# 3. Identity / Authentication

Citizens have durable civic identities but authentication is contextual.

Possible factors:
- personal device credential,
- biometric/local physical confirmation,
- hardware secure element,
- institutional role credential,
- emergency/recovery procedures.

One stolen phone does not equal access to every system.

No biometric can reveal developmental origin where no adult origin scanner exists.

---

# 4. Permissions

Access follows least-privilege/domain role.

Examples:
- doctor can access relevant medical file, not unrestricted court archive,
- transit operator sees route/occupancy needs, not family law history,
- school sees student/guardian permissions, not protected Reconstruction provenance,
- archive researcher may see public historical corpus but not sealed identity mappings.

Cross-domain access creates an explicit logged request path.

---

# 5. Personal Messaging

Normal society supports:
- private 1:1/group messaging,
- voice/video,
- asynchronous media,
- presence/status controls,
- family/school/work groups.

Encryption/privacy is normal, but targeted lawful access may exist under due process for serious cases.
No universal plaintext government mirror.

---

# 6. Public Social Layer

Compatible with MEDIA-H1:
- interoperable feeds/communities,
- creator channels,
- journalism,
- discussion groups,
- public archives,
- local boards.

No single company/platform owns all social life.

---

# 7. Emergency Communication

Resilient channels include:
- network alerts,
- building public address,
- transit signage,
- local radio/mesh fallback,
- hardwired emergency endpoints.

Emergency messages can be geographically targeted without revealing protected identity lists.

---

# 8. Offline / Partition Modes

If one district loses backbone connectivity:
- local utility control keeps operating,
- local emergency comms remain,
- cached essential records/services support continuity,
- financial/social synchronization may delay,
- later reconciliation resolves state.

No `internet down = oxygen stops` architecture.

---

# 9. Data Synchronization

Not every database is one live global table.
Some systems use:
- authoritative central/federated registries,
- local caches,
- append-only/audited logs,
- delayed replication,
- archival snapshots.

This supports historical schema divergence without magical total inconsistency.

---

# 10. External Communications

During cruise, real-time Earth communication is impossible because of light-time distance.

Historical external communication may include:
- delayed transmissions earlier in voyage,
- scientific/navigation beacons,
- stored Earth-origin data,
- later loss/decline of meaningful two-way contact depending Package D history.

At destination:
- ship/orbit/surface communication becomes local but physically distributed,
- outages/latency between sites remain possible.

---

# 11. Timing / Clock

Critical networks share a robust shipwide time standard.
Civil 24h time and Voyage Year metadata can coexist.

Precise timing supports:
- transport,
- finance,
- archive provenance,
- legal access logs,
- sensor correlation.

---

# 12. Cybersecurity

Core principles:
- segmentation,
- signed updates,
- hardware roots of trust where appropriate,
- credential rotation,
- anomaly detection,
- physical interlocks for catastrophic functions,
- incident isolation,
- rollback/recovery.

No `one master password` for Meridian.

---

# 13. Privacy / Metadata

Even encrypted content leaves metadata risk.
Rules may limit:
- indefinite location history,
- social-graph aggregation,
- cross-domain profiling,
- warrantless historical queries.

Operational retention and civic privacy must be balanced explicitly.

---

# 14. Re-identification Risk

Count/Amara arc remains plausible because:
- aggregate Count may lawfully become public,
- separate public/semipublic facts about residence/work/family/history can be correlated,
- private identity mapping remains protected,
- media/community speculation can narrow candidates without an official name dump.

No single open endpoint says `Natural-Origin citizen = Amara`.

---

# 15. Payments / Commerce

Digital payments are ordinary over the civic network.
Offline/local transaction modes exist for temporary outages and later reconciliation.

No blockchain requirement.
No universal public ledger exposing everyone's purchases.

---

# 16. Device Ecology

Personal devices may include:
- pocket/wearable terminals,
- household displays,
- work-specific hardware,
- public interfaces,
- accessibility devices.

No requirement for one fixed physical form across all citizens.

---

# 17. Children / Guardians

Youth accounts/permissions can distinguish:
- messaging privacy,
- school notifications,
- purchases,
- travel permissions,
- emergency guardian contact.

Guardians do not automatically receive full surveillance of adolescents' every message/location.
Age and safety rules mediate access.

---

# 18. Network Governance

Core communication backbone is civic/common infrastructure.
Private/co-op providers may offer services/content but cannot own the only physical network path.

Critical-domain network operators remain regulated public/commons infrastructure.

---

# 19. Failure / Story Texture

Normal failures can cause:
- message delay,
- one service unavailable,
- building local mode,
- payment reconciliation,
- work backlog,
- transit info degradation.

Major cyber/physical network events can become serious without instantly controlling every system.

---

# PROVISIONAL JUDGMENT

Best model:
**NET-H1 — Redundant Civic Backbone + Segmented Critical Domains + Permissioned Gateways + Local Fallback**

Dependencies:
- archive architecture,
- exact retention/privacy law,
- cyber incident process,
- physical network/map topology,
- destination communication architecture.
