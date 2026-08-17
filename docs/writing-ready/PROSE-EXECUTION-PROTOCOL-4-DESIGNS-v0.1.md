# Prose Execution Protocol — 4 Designs v0.1

Status: `POST-WRITING-READY EXECUTION DESIGN / NO PROSE YET`

Project:
《우주선에는 인간이 한 명뿐이다》

Prerequisite state:
- DESIGN FREEZE = PASSED
- CANON FREEZE = PASSED
- WRITING READY = PASSED

Purpose:
본문을 쓰기 전에 **어떤 방식으로 230화 Blueprint를 실제 문장으로 실행할 것인지** 정한다.
Story/Canon을 다시 설계하는 문서가 아니다.

Must solve:
- POV/person
- narrative distance
- episode length
- scene count/rhythm
- exposition/jargon
- dialogue density
- opening/closing hooks
- character voice
- humor/downtime
- anti-AI prose
- after-draft QA

---

# Design A — Maren-Only First Person

## Core
전편 마렌 1인칭.
독자는 마렌이 보는 것만 본다.

## Typical Execution
- 1 POV / entire series
- very close narrative distance
- 2~4 scenes / episode
- internal thought can carry legal/continuity reasoning

## Strengths
- 주인공 목소리가 강해짐.
- 웹소설 초반 몰입이 빠름.
- 복잡한 SF 세계를 한 사람의 이해범위로 제한하기 쉬움.
- 독자가 마렌의 결함과 자기합리화를 직접 체험 가능.

## Weaknesses
- Canon이 의도적으로 만든 non-Maren causality와 충돌.
- Amara family autonomy가 대부분 `Maren이 나중에 들은 이야기`가 됨.
- Noah의 성장 14년, Ella의 독립회복, Jun/Outer Works, Raul의 win/cost를 현장감 있게 보여주기 어려움.
- Information Ladder가 마렌의 접근범위에 과도하게 종속될 수 있음.
- 후반 문명 규모가 커질수록 1인칭 정보운반이 작위적.

## Anti-AI
강한 개인 목소리는 장점이나, 마렌이 모든 세계설명을 내적으로 정확히 정리하면 오히려 `해설자 주인공` 위험.

## Verdict
`REJECT AS BASE`

사용 가능 요소:
마렌 POV 회차에서는 높은 내적 밀도와 제한된 자기합리화를 가져온다.

---

# Design B — Maren-Dominant Close Third Limited

## Core
3인칭 제한시점.
마렌이 약 70~80%의 회차를 차지하고 나머지만 다른 인물 POV.
한 화 안에서는 POV를 바꾸지 않는다.

## Strengths
- 1인칭보다 세계확장에 유리.
- 마렌 중심 주인공성이 매우 선명.
- 제한적으로 Amara/Ella/Noah를 직접 보여줄 수 있음.
- SF 설명을 POV 지식수준에 맞출 수 있음.

## Weaknesses
- 230화 Blueprint의 실제 causal ownership보다 마렌 비중이 높아질 위험.
- 독자가 `다른 인물 회차 = 특별회차`라고 받아들여 Amara pre-Reveal에 스포트라이트가 생길 수 있음.
- Ella/Noah/Jun/Raul이 결국 마렌 subplot처럼 보일 수 있음.

## Best Use
상업적 주인공 밀도를 최우선할 때.

## Verdict
`STRONG BUT TOO MAREN-CENTRIC`

---

# Design C — Causal-Owner Single-POV Close Third

## Core
**한 화 = 한 POV**.
POV는 그 화에서 가장 중요한 선택을 실제로 내리는 `causal owner`에게 준다.

Maren remains plurality/central anchor, but not an artificial majority.

Target long-series POV share guideline, not quota:
- Maren ~45~55%
- Ella/Noah combined ~15~20%
- Amara/household ~10~15%
- Raul/Jun/Ines/Tomas/others ~15~25%

Exact distribution follows Blueprint causality, not percentage bookkeeping.

## Narrative Distance
Close third limited.

Default:
- 감정/감각/즉시 판단은 가까이
- 세계설명/역사개관은 멀어지지 않음
- narrator never knows more than active POV unless clearly ordinary public fact

## Strengths
- M2 non-Maren causality와 가장 정확히 맞음.
- Amara가 Reveal 전에도 `미스터리 인물`이 아니라 자기 일상을 사는 POV가 될 수 있음.
- Noah의 12→26세 성장에 실제 주체성 부여.
- Raul win/cost, Jun place conflict, Ella independent recovery를 직접 보여줌.
- 정보계단에서 `누가 무엇을 모르는가`를 문체 자체가 지킴.

## Weaknesses
- 독자가 POV 전환에 익숙해져야 함.
- 주변인까지 모두 POV를 주면 앙상블 산만함.
- 각 인물의 문장 리듬/관찰대상을 실제로 다르게 써야 함.

## Guardrail
POV를 `정보를 보여주기 위해` 선택하지 않는다.
**선택/손실의 소유자**가 누구인지로 결정.

## Verdict
`CURRENT BEST BASE`

---

# Design D — Scene-Rotating Cinematic Third

## Core
한 화 안에서도 2~3명 POV 전환 가능.
장면 단위로 카메라를 이동.

## Strengths
- 사회적 사건을 넓게 보여주기 쉬움.
- insertion / Count / 대형 공공사건에서 규모감 강함.
- 한 화에 여러 관계축을 동시에 움직일 수 있음.

## Weaknesses
- 웹소설 화 단위 감정집중 약화.
- POV switch가 많은 AI 생성 장면처럼 느껴질 위험.
- 한 사건을 모두의 반응으로 설명하는 redundancy 발생.
- short scenes + cliffhangers의 기계적 조립 위험.
- 정보공개 timing 실수 가능성 증가.

## Verdict
`REJECT AS DEFAULT`

Exception candidate:
아주 제한된 insertion/public-event 회차에서만 별도 설계승인 후 사용할 수 있음.

---

# Comparison

| Axis | A 1인칭 | B Maren 3인칭 | C Causal-owner | D Scene-rotate |
|---|---:|---:|---:|---:|
| protagonist clarity | 5 | 5 | 4 | 3 |
| ensemble autonomy | 1 | 3 | 5 | 5 |
| info fairness | 4 | 4 | 5 | 3 |
| long-series flexibility | 2 | 4 | 5 | 4 |
| anti-AI naturalism | 4 | 4 | 5 | 2 |
| Amara pre-Reveal safety | 2 | 3 | 5 | 3 |
| Noah 14y growth | 2 | 3 | 5 | 4 |
| webnovel readability | 5 | 5 | 4~5 | 3 |

Recommended base:
**C**.

---

# Recommended Hybrid — PEP-H1

Base:
**Causal-Owner Single-POV Close Third**.

Take from B:
Maren remains the most frequent POV and default anchor when causal ownership is genuinely shared.

Take from A:
Maren POV allows stronger internal contradiction/self-justification than other POVs.

Do NOT take from D by default:
No scene-level head hopping.

---

# 1. POV Rules — PEP-H1

## Default
- one POV character per episode
- third-person limited
- no mid-episode POV switch

## POV Selection Priority
1. who makes the irreversible choice?
2. who pays the immediate emotional/material cost?
3. who knows the least/most appropriate amount for information fairness?
4. if tied, prefer Maren as series anchor

## POV Cannot Be Chosen Because
- `reader needs exposition`
- `this character knows the answer`
- `we have not seen them recently`

## Supporting POV Cap
Do not casually create one-off POVs.
Core/recurring POV pool priority:
Maren / Ella / Noah / Raul / Ines / Jun / Amara / selected Amara household / Tomas when institutionally necessary.

---

# 2. Narrative Distance

Default distance:
**close-medium**.

Allowed to move closer during:
- embarrassment
- family conflict
- physical work/medical pressure
- irreversible choice

Allowed to move slightly wider during:
- place transition
- time-skip reorientation
- public procedural context

Forbidden:
- omniscient paragraph explaining the hidden true meaning before POV knows it
- essay-like narrator judging `what humanity really is`
- constant italicized internal monologue

Rule:
**thought should appear as perception/decision pressure more often than explicit self-analysis.**

---

# 3. Episode Length / Scene Count

Platform-neutral Korean webnovel execution target:

## Standard Episode
- roughly **5,500~7,500 Korean characters including spaces** candidate
- 2~4 substantial scenes

## High-Pressure / Major Payoff
- up to ~8,500 characters if necessary
- length increase must buy action/relationship payoff, not explanation

## Shorter Bridge/Downtime
- ~4,800~6,000 possible
- cannot feel like half an episode

These are execution targets, not Canon.
If publishing platform requirements differ, adapt mechanically without changing scene function.

### Scene Rule
Each scene must change at least one:
- immediate plan
- access/status
- relationship temperature
- physical constraint
- public/private knowledge

A scene that only explains is merged into an active scene.

---

# 4. Episode Rhythm

Default 3-beat macro:
1. **pressure arrives / existing carry activates**
2. **character acts and discovers cost**
3. **choice changes baseline / hook opens next pressure**

Do not force every episode into exactly three visible scenes.

Rhythm mix across 5~8 episodes should include:
- family/private
- work/institution
- physical/material
- social/public
- downtime/humor

No 5-episode run of pure meeting/hearing/archive work unless hostile QA explicitly approves.

---

# 5. Opening Rule

Opening must begin with **present pressure**, not world explanation.

Preferred opening types:
- someone already doing a job and something is off
- interrupted routine
- practical deadline
- interpersonal mismatch
- physical inconvenience/failure
- consequence arriving from previous choice

Avoid repeated:
- message notification
- official summons
- report arriving
- `Maren stared at the screen`

First paragraph jargon budget:
**0~1 unfamiliar term**.

---

# 6. Ending / Hook Rule

Hook categories rotate:
- decision made
- cost revealed
- relationship fracture/shift
- physical state changes
- access gained/lost
- public consequence begins
- expectation reversed
- quiet emotional reframe

Notification/audit/request hook is allowed but cannot dominate.

Hard rule:
**the hook should usually be caused by something already done, not random new information dropping from above.**

Not every episode needs a shock cliffhanger.
Some episodes can end on an irreversible quiet decision.

---

# 7. Dialogue Density

Default target:
**roughly 35~55% dialogue by visible page feel**, not counted mechanically.

Family/downtime may be higher.
Institution/technical episodes may be lower.

Dialogue rule:
- characters do not deliver complete essays
- interruptions/avoidance/misunderstanding allowed
- people may answer adjacent questions
- repeated idea should be shortened, not restated elegantly

Forbidden:
A says thesis → B gives perfect counterthesis → A synthesizes.

---

# 8. Exposition / Jargon Budget

## Early Active Terms
- 시드
- 연속성
- 복원

Do not stack technical definition on first mention if action already implies function.

## Rule of Need
Explain only the amount required for the **current choice**.

## Per Scene
Prefer max 1 genuinely new technical/institutional concept.

## Per Episode
Two new terms is warning; three requires explicit necessity.

## Reveal Exception
Meaning cluster can explain more, but each explanation must alter what someone can do/claim/fear.

No glossary paragraphs inside prose.

---

# 9. Character Voice Enforcement

## Maren
- notices contradiction/order/process first
- shorter decision sentences under stress
- becomes more formal when emotional
- care appears as logistics before words

## Ella
- notices people, memory, social texture
- longer associative speech
- reconnects before analyzing

## Noah
- early: avoids direct adult framing, notices peers/options/escape routes
- later voice matures without becoming Raul-lite

## Raul
- public speech sharply reframes
- private speech looser, observational, teasing/gossipy

## Tomas
- speaks in delays/trades/consequences
- not cryptic wise elder

## Ines
- body/function/time first
- cuts abstraction quickly

## Jun
- place/history/person examples
- not poetic nostalgia machine

## Amara
- turns public abstraction into household/work consequence
- do not repeat `I am not your symbol` speeches

---

# 10. Anti-AI Imperfection Budget

Every episode should contain at least some ordinary human texture, but not as checklist theater.

Possible textures:
- someone misremembers a minor fact
- practical annoyance
- badly timed joke
- selfish shortcut
- boring errand
- physical fatigue
- social awkwardness
- irrelevant preference
- small incompetence
- unfinished sentence / avoidance

Do not make every named character maximally articulate and morally self-aware.

Characters may misunderstand themselves.

---

# 11. Description Rule

Prioritize:
1. objects characters use
2. movement/path/queue/maintenance
3. body state
4. social use of space
5. sensory detail that affects action

De-prioritize:
- generic cinematic panoramas
- repeated `vast station` awe
- decorative sci-fi inventory lists

Each Habitat should feel different through **routine**, not adjective palette alone.

---

# 12. Science / Law Explanation Rule

Technical accuracy supports stakes but does not become textbook display.

When a rule matters:
`problem → wrong assumption → practical correction → consequence`
preferred over
`definition → history → exceptions → decision`.

Law should appear as:
- who can do what now
- who must wait
- whose status changes
- what can be appealed
not statute recital.

---

# 13. Time-Skip Prose Rule

Major skips must re-anchor at least 3 of 5 quickly:
- character age/life stage
- relationship state
- job/residence
- ship/arrival clock
- visible material change

Do not open with a chronology summary paragraph if a changed routine can show the passage.

---

# 14. Reveal Prose Rule

## Count
Show factual layer first.
Do not narrate moral conclusion.

## Meaning
Within locked EP059~066 sequence:
- explain biological bodies
- explain developmental origin
- explain what Seed cannot do
- explain current civic personhood

## Amara
Pre-Reveal scenes contain no ominous body/instinct cue.
After confirmation, her ordinary problems continue.

---

# 15. After-Draft Episode QA

After every drafted episode, verify:

### Blueprint
- primary choice preserved?
- irreversible consequence preserved?
- next carry preserved?

### Canon
- no new world rule silently invented?
- no forbidden technology/power?

### POV
- one POV only?
- knowledge boundary respected?

### Voice
- could another core character say these lines unchanged?

### Exposition
- any paragraph exists only to explain?

### Hook
- consequence-driven rather than random notification?

### Anti-AI
- dialogue too complete/symmetric?
- every detail suspiciously meaningful?
- characters too self-aware?

If Canon-impact failure appears:
**STOP — do not patch prose around it.**
Run change control.

---

# 16. Batch QA

Every 5 drafted episodes:
- reward/hook repetition
- scene-type balance
- dialogue voice collision
- jargon accumulation
- Maren POV dominance
- ordinary-life texture

Every Sub-Act end:
- baseline actually changed?
- planned payoff delivered?
- relationship direction changed?
- next Sub-Act pressure caused rather than appended?

Every Act end:
- Reader Promise still same work?
- P1 guardrails review
- Canon regression spot-check

---

# 17. P1 Execution Guardrails From Final Hostile QA

1. opening 20: title promise visible but not lecture-driven
2. legacy Human cannot read as semantic cheat
3. Amara cannot repeat one refusal speech
4. Act5 cannot become engineering committee fiction
5. Human Settler must feel like known legal stack becoming operational
6. insertion must feel climactic without disaster gimmick
7. dialogue cannot become same-writer/perfect-agent exchange

PEP-H1 directly addresses all seven.

---

# 18. Red-Team Questions Before Lock

1. Does single-POV-per-episode weaken episodes whose causal owner changes mid-way?
2. Does ~45~55% Maren POV still feel like clear protagonist?
3. Is 5.5k~7.5k character target enough for social SF without exposition compression?
4. Does strict one-new-concept-per-scene make Meaning cluster too artificial?
5. Could ordinary imperfection become another mechanical checklist?
6. Does no scene-level POV switching reduce insertion scale?
7. Can minor supporting POVs proliferate through 230 episodes?

Preliminary answer:
all manageable with guardrails; requires dedicated Red Team before protocol lock.

---

# Verdict

**PEP-H1 Causal-Owner Single-POV Close Third + Maren Anchor = CURRENT RECOMMENDED PROSE EXECUTION PROTOCOL.**

Status:
`PROVISIONAL EXECUTION PRIORITY / NO PROSE YET`
