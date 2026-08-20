# V3 Episode Graph + Context Pack Spec v0.1

Logical episode note frontmatter:
```yaml
id: EP-001
type: episode
act: ACT-V3-01
volume: VOL-V3-01
subact: SA-V3-1A
beat: BEAT-V3-B01
blueprint: ../prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md
pov: C01
character_refs: []
asset_refs: []
location_refs: []
institution_refs: []
incoming_carries: []
outgoing_carries: []
```

## Retrieval
`Episode → Beat → Sub-Act → Volume → Act`, then only episode-relevant cross-links.

## Five direct bundles
1 Episode Card
2 Immediate Continuity
3 POV/Relationship State
4 World/Zone/Material State
5 Active Device/Return/Collectibility State

The graph may be deep; the prompt stays small.