# Entity State Snapshot Spec v0.1

```yaml
id: STATE-<ENTITY>-<RANGE>
type: entity_state
entity: <stable id>
state_from: EPxxx
state_to: EPyyy
parent_act: ACT-V3-xx
parent_subact: SA-V3-xA
physical_state: ...
social_state: ...
relationship_state: ...
ownership_custody: ...
knowledge_state: ...
resource_access: ...
collectibility_state: INTRODUCE|RECOGNIZE|RECONTEXTUALIZE|TRANSFORM|PERSIST|HOLD|NO-CHEKHOV|OFFSTAGE
next_transition: EPzzz
```

Hard:
- state changes need evidence from blueprint/ledger,
- same face does not imply same current-life relationship,
- no future knowledge leaks backward,
- NO-CHEKHOV remains a valid explicit state.