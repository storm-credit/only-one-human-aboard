---
id: DEEP-V3-EP003
type: deep_projected_context
episode: EP003
router: CTX-V3-EP003
schema: DEEP-CONTEXT-SCHEMA-v1
context_kind: DEEP_PROJECTED
projection_semantics: FORECAST_NOT_ACTUAL
dynamic_actual: PENDING
branch_state_namespace: H-A
cross_branch_inheritance: BLOCKED_UNLESS_EXPLICIT
microbundle_compile_cap: 5
act: ACT-V3-01
volume: VOL-V3-01
subact: SA-V3-1A
beat: BEAT-V3-B01
concurrency: NONE
source_snapshot: router=CTX-V3-EP003; blueprint=docs/prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md; mode=manual-body-preserved
stale_if_changed: router|exact_episode_blueprint|DEEP-CONTEXT-SCHEMA-v1|character-role-matrix|relationship-network|asset-roster|reveal-router
---
# DEEP-V3-EP003 — 퇴근은 이동이다
Router: [[../contexts/CTX-V3-EP003]] · Episode: [[../episodes/EP-V3-003]]

## Structural Inheritance
- series_job: 직업 외 생활과 도시 이동을 주인공보다 큰 독립 시스템으로 체감시킨다.
- act_job: Meridian을 집으로 만든다.
- volume_reward: commute/home attachment + L01/M03 first recognition.
- subact_input_state: 첫 업무가 평범한 원인으로 수렴하며 schedule knock-on 발생.
- subact_target_state: 독자가 일/집/통근 기준선을 익힘.
- beat_execution_job: B01에서 work→home separation을 최초로 실제 이동으로 만든다.
- exact_blueprint_ref: [[../../prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1#EP003 — 퇴근은 이동이다]]
- router_ancestry_ref: `VOL-V3-01 / SA-V3-1A / BEAT-V3-B01`.

## Projected Incoming
- previous_episode_forecast: freight timing change가 통근에 작은 파장을 준다.
- previous_beat_carry: 주인공은 업무를 닫아도 도시 전체를 통제하지 못함.
- subact_entry_condition: ordinary consequences cross departments.
- projected_continuity: family obligation already exists independently of work.

## Protagonist Context
- projected_goal: shift delay 뒤에도 가족 약속 시간에 도착하려 한다.
- pov_known: 자신의 업무 지연과 통근 경로.
- pov_unknown: 네트워크 전체 배분 결정 및 Mira 쪽 독립 판단.
- projected_judgment: 실무 최적화만으로 개인 일정이 보호되지는 않는다.
- direct_action_requirement: crowding/missed connection 속에서 생활 동선을 선택.
- agency_requirement: 가족에게 갈지 일을 더 붙잡을지 본인이 선택.
- must_not_solve: transit/logistics system을 현장 직권으로 고치지 않는다.
- flaw_pressure: 늦음과 실무 우선 습관.

## Character Context
- active_core: `[C01]`.
- influence_only: `family household; C02 Mira/logistics network` — appearance not required.
- family independent_agenda: 주인공의 사건과 무관한 일상 일정 유지.

## Relationship Context
- C01↔family: entry_baseline=`habitual ordinary obligation`; projected_target_delta=`늦는 사람/기다리는 가족의 생활 기준선`; absolute_forbid=`가족을 향후 인질 장치처럼 도입`.
- C01↔C02: entry_baseline=`past familiarity exists but not unpacked`; projected_target_delta=`Mira decision consequences reach him before direct encounter`; absolute_forbid=`Mira를 주인공 보조자화`.

## World / Location Context
- location_ref: `Old Works → L01 Transfer Belt → Midring home`.
- projected_function: 성숙한 도시의 출퇴근/주거 리듬.
- spatial_use: 실제 환승·혼잡·연결 실패가 시간 비용을 만든다.
- movement_constraints: missed connection/crowding; no teleport.
- access_constraints: public routes governed by transit operations.
- change_since_previous_use: first full commute baseline.
- scene_job: 도시 규모와 생활성을 보여준다.
- sensory_life_texture: shift-change crowd, convenience food, ordinary housing/commute friction.
- projected_zone_condition: normal but rerouted service.

## Asset / Collectibility Context
- L01 Transfer Belt: `INTRODUCE / ELIGIBLE / FOREGROUND / collectibility_job=장소 흐름 인지`.
- M03 Utility Tug/Freight Tractor: `INTRODUCE / ELIGIBLE / BACKGROUND / collectibility_job=NONE`.
- P01: `PERSIST / HOLD` — work prop need not follow home scene foreground.

## Institution / Faction / Network Context
- transit/logistics network: projected_operating_state=`normal with freight timing knock-on`; independent_causality=`Mira office reroute exists without protagonist`.

## Mystery / Reveal / Knowledge Fence
- world_truth_reference: SEALED_LINK_ONLY.
- pov_known: ordinary commute disruption.
- character_known: family knows only his work delay; Mira/logistics knows network facts.
- reader_confirmed: city systems create independent consequences.
- reader_suspected: NONE_AUTHORIZED.
- allowed_reveal: NONE.
- forbidden_future_reveal: all lineage/ontology.

## Foreshadow / MacGuffin / Payoff
- active_chain: NONE_AUTHORIZED.
- ordinary_event_guard: HARD — commute inconvenience is not a clue.

## Genre Engine
- primary_engine: ordinary-life.
- secondary_engine: relationship.
- action_obligation: a concrete movement/time problem, not exposition tour.
- exposition_ceiling: city details only through use.

## Execution Constraints
- MUST: `[family exists as independent life, transit has real time cost, protagonist does not control reroute]`.
- TARGET: `[attachment to Meridian]`.
- PREFER: `[one clear L01 spatial memory]`.
- MAY: `[brief family message/call]`.
- FORBID: `[ominous anomaly, lore dump, tragic-family coding]`.

## Forecast Outgoing
- projected_relationship_delta: family baseline established; Mira remains independent offstage actor.
- projected_knowledge_delta: reader learns work/home separation and transit dependence.
- projected_material_delta: L01 becomes recognizable; M03 remains background.
- projected_world_institution_delta: reroute notice affects next-day access.
- projected_asset_lifecycle_delta: L01 foreground recognition; M03 low-salience introduction.
- next_episode_carry: switch causal ownership to Mira so her decision is shown independently.

## Dynamic Actual Placeholder
realized_relationship_delta: PENDING
realized_knowledge_delta: PENDING
realized_material_delta: PENDING
realized_world_institution_delta: PENDING
realized_asset_lifecycle_delta: PENDING
actual_next_episode_carry: PENDING

## Retrieval Compile Map
1 EP003 Blueprint. 2 commute/family continuity. 3 C01 + family/Mira influence. 4 L01/Midring/transit. 5 L01 only foreground; no clue chain.
