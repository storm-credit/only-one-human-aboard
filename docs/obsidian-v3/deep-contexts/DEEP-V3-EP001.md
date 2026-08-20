---
id: DEEP-V3-EP001
type: deep_projected_context
episode: EP001
router: CTX-V3-EP001
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
source_snapshot: router=CTX-V3-EP001; blueprint=docs/prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1.md; mode=manual-body-preserved
stale_if_changed: router|exact_episode_blueprint|DEEP-CONTEXT-SCHEMA-v1|character-role-matrix|relationship-network|asset-roster|reveal-router
---
# DEEP-V3-EP001 — 오래된 진동

Router: [[../contexts/CTX-V3-EP001]] · Episode: [[../episodes/EP-V3-001]]

## Structural Inheritance
- series_job: 독자가 메리디언을 실제 생활권으로 믿고, 주인공의 `물리적 인과 재구성` 방법을 첫 기준선으로 학습한다.
- act_job: 미스터리보다 집/일/사람의 정상성을 먼저 만든다.
- volume_reward: work/home/community attachment + 반복해서 알아볼 실제 작업물/장소의 첫 인지.
- subact_input_state: 독자는 메리디언·주인공·권한 경계를 모른다.
- subact_target_state: 정상 고장과 정상 제도가 무엇인지 판별 가능한 기준선을 얻는다.
- beat_execution_job: 첫 구조진동 사례를 평범한 인과로 추적하며 work triangle을 세운다.
- exact_blueprint_ref: [[../../prewriting-v3/EPISODE-BLUEPRINT-ACT1-v0.1#EP001 — 오래된 진동]]
- router_ancestry_ref: `VOL-V3-01 / SA-V3-1A / BEAT-V3-B01` — router inherited, not recomputed.

## Projected Incoming
- previous_episode_forecast: `SERIES_OPEN / NONE_AUTHORIZED`.
- previous_beat_carry: `NONE_AUTHORIZED`.
- subact_entry_condition: 평범한 업무 호출이 일상 세계를 열어야 한다.
- projected_continuity: 주인공은 유명 영웅이 아니라 정상적인 손상분석관이며 현장 권한이 제한되어 있다.

## Protagonist Context
- projected_goal: 정규 shutdown을 불필요하게 넓히지 않고 진동/균열의 실제 원인층을 좁힌다.
- pov_known: 물리 손상 순서, 검사 절차, 자신의 구조안전 평가 권한.
- pov_unknown: 최초 원인이 무엇인지; 현재 표면 균열이 원인인지 결과인지.
- projected_judgment: `sensor fault`라는 쉬운 설명은 물리 흔적과 맞지 않으면 채택하지 않는다.
- direct_action_requirement: 측정·표면 흔적·하중 순서를 이용해 한 단계 upstream 원인을 찾는다.
- agency_requirement: 기술 판단과 조사 범위 선택은 주인공이 직접 소유한다.
- must_not_solve: 사람의 이동/경비 권한까지 지휘하지 않는다; 세계의 숨은 구조를 추론하지 않는다.
- flaw_pressure: Niko를 보호한다는 이유로 과통제하려는 성향.

## Character Context
- active_core: `[C01 Protagonist, C07 Gideon Park, C08 Niko Osman]`.
- C07: independent_agenda=`성급한 결론을 반증 가능한 기술 판단으로 만들기`; episode_function=`주인공 추론을 승인해주는 스승이 아니라 근거를 요구하는 독립 검수자`; projected_delta=`업무 세대 삼각형 확립`.
- C08: independent_agenda=`현장 능력을 증명하고 더 깊은 접근을 맡기`; episode_function=`제한 구역에 먼저 들어가고 싶어 하는 압력`; projected_delta=`protection/control tension seed`.
- influence_only: `NONE_AUTHORIZED`.

## Relationship Context
- C01↔C07: entry_baseline=`senior technical counterweight`; tension=`설명 없는 직감 vs 검증`; projected_target_delta=`근거를 요구하는 신뢰 규칙 형성`; absolute_forbid=`Gideon이 모든 답을 미리 아는 현자화`.
- C01↔C08: entry_baseline=`senior/junior field relation`; tension=`학습 욕구 vs 안전 접근`; projected_target_delta=`주인공의 과통제 씨앗`; absolute_forbid=`Niko를 무능한 사고유발 장치로 축소`.

## World / Location Context
- location_ref: `Old Works / L05 multi-generation structural work environment`.
- projected_function: 평범한 노동공간이자 향후 비교 기준선.
- spatial_use: 손상부·접근 통로·진단 지점이 물리적으로 분리된다.
- movement_constraints: restricted service run은 자격/안전 근거 없이 진입 불가.
- access_constraints: 주인공은 구조안전을 평가하지만 사람/보안 전체를 지휘하지 않는다.
- change_since_previous_use: `SERIES_OPEN`.
- scene_job: `능력`과 `권한한계`를 동시에 보인다.
- sensory_life_texture: 사용감 있는 산업표면, 실제 작업 동선, 평범한 일정 압력.
- projected_zone_condition: routine operation with localized vibration/crack call.

## Asset / Collectibility Context
- P01 Field Case + P02 Damage-Marking Set: lifecycle=`INTRODUCE`; user=`C01`; condition=`ordinary complete work state`; eligibility=`ELIGIBLE`; salience=`FOREGROUND as one functional work-unit`; collectibility_job=`주인공의 일하는 방식 인지`.
- M01 Structural Inspection Crawler: lifecycle=`INTRODUCE`; eligibility=`ELIGIBLE`; salience=`BACKGROUND`; collectibility_job=`NONE`.
- M02 Damage-Mapping Drone: lifecycle=`INTRODUCE`; eligibility=`ELIGIBLE`; salience=`BACKGROUND`; collectibility_job=`NONE`.
- L05 Old Works Junction: lifecycle=`RECOGNIZE`; eligibility=`ELIGIBLE`; salience=`BACKGROUND`; collectibility_job=`장소 기준선`.
- foreground_quota_check: `PASS — two props form one natural work unit; graph-active machines stay background`.

## Institution / Faction / Network Context
- Old Works work/signoff chain: projected_authority=`operations + safety signoff distributed`; resources=`crews, diagnostics, access control`; episode_change_target=`none`; independent_causality=`schedule pressure exists without protagonist`.

## Mystery / Reveal / Knowledge Fence
- world_truth_reference: `SEALED_LINK_ONLY`.
- pov_known: `routine physical failure under investigation`.
- character_known: Gideon/Niko know only local work facts.
- reader_confirmed: `주인공은 물리 인과를 추적하는 실무자이며 권한이 제한됨`.
- reader_suspected: `NONE_AUTHORIZED`.
- allowed_reveal: `NONE — no hidden-history clue`.
- forbidden_future_reveal: `regression / branching / substrate / HUMAN:1 / Outer Ark`.

## Foreshadow / MacGuffin / Payoff
- active_chain: `NONE_AUTHORIZED`.
- ordinary_event_guard: `HARD — this failure is ordinary; do not ominously narrate it as secret-system evidence`.

## Genre Engine
- primary_engine: `procedural`.
- secondary_engine: `ordinary-life`.
- action_obligation: 인과 추적의 작은 해결 재미를 제공한다.
- exposition_ceiling: 직업/도시 설명은 실제 판단과 이동에 붙는다.

## Execution Constraints
- MUST: `[physical causal reasoning on-page, authority limit visible, Gideon/Niko retain agency]`.
- TARGET: `[reader understands protagonist method without hero aura]`.
- PREFER: `[one memorable functional prop-unit]`.
- MAY: `[brief ordinary schedule pressure]`.
- FORBID: `[mystery clue, ontology hint, total shutdown melodrama, protagonist command overreach]`.

## Forecast Outgoing
- projected_relationship_delta: work triangle gains first usable baseline; C01↔C08 overcontrol seed.
- projected_knowledge_delta: surface crack expected to be recognized as downstream symptom rather than complete cause.
- projected_material_delta: work-kit and Old Works become recognizable baseline assets.
- projected_world_institution_delta: no structural change; signoff limits become reader-known.
- projected_asset_lifecycle_delta: P01/P02 recognized; M01/M02/L05 remain low-salience.
- next_episode_carry: continue one layer upstream without converting case into mystery.

## Dynamic Actual Placeholder
realized_relationship_delta: PENDING
realized_knowledge_delta: PENDING
realized_material_delta: PENDING
realized_world_institution_delta: PENDING
realized_asset_lifecycle_delta: PENDING
actual_next_episode_carry: PENDING
## Retrieval Compile Map
1. Episode Card → exact EP001 Blueprint only.
2. Immediate Continuity → Projected Incoming + JIT actual when available.
3. POV/Relationship → Protagonist + C07/C08 + two relationship edges.
4. World/Zone/Material → Old Works + work/signoff + selected material state.
5. Device/Return/Collectibility → no clue chain; P01/P02 foreground, others retrieval-only.
