# Minimum Action Agent OS Adoption v0.1

Status: `ADOPTED AS WORKING METHOD / DOES NOT OVERRIDE CANON`
Project: 《우주선에는 인간이 한 명뿐이다》
Source methodology: `storm-credit/minimum-action-agent-os`

---

## 1. Scope

이 문서는 프로젝트 내용을 재설계하는 정본이 아니다.

Minimum Action Agent OS는 **어떻게 일할지**만 규정한다.
이 프로젝트의 Canon / Character / Story / Manuscript truth는 항상 이 저장소의 공식 정본이 우선한다.

기존 Agent를 총 5개 이하로 줄이지 않는다.
전체 Agent 수에는 제한을 두지 않는다.

핵심 운영 기준은:

> 각 reasoning node가 한 번에 직접 선택하는 Agent + Tool + Skill + MCP + 기타 callable action의 Local Action Space를 기본 5개 이하로 유지한다.

이 기준은 프로젝트 운영 정책이며 외부 API 하드 리밋으로 취급하지 않는다.

---

## 2. Preservation Rule

기존 다음 구조를 삭제/재작성하지 않는다.

- Canon / Spec / Freeze 문서
- manuscript
- narrative-engineering 문서
- QA / Harness
- decision / change logs
- 기존 전문 Agent

새 설계가 기존 Freeze와 충돌하면:

1. 기존 파일을 덮어쓰지 않는다.
2. `CANDIDATE` 또는 `REOPENING` 문서를 만든다.
3. 영향범위를 기록한다.
4. 독립 Critic / Red Team을 통과한 뒤에만 승격한다.

---

## 3. Local Action Space Audit

### Repository-declared custom-agent surface

| Node | Direct agents | Direct repo tools/skills declared | Count | Result |
|---|---|---:|---:|---|
| Project custom-agent layer | `episode-qa` | none declared as peer custom agents | 1 | PASS |

현재 저장소 `.claude/agents/`에는 `episode-qa.md` 하나만 존재한다.
따라서 **Agent 수를 줄이는 변경은 불필요**하다.

### Runtime caveat

Claude Code / ChatGPT / MCP 실행환경에서 실제 노출되는 built-in tool 수는 저장소 파일만으로 완전 확정할 수 없다.
따라서 runtime toolbelt가 5개를 넘는 경우에는 아래 router 규칙을 적용한다.

### Recommended reasoning topology

```text
Main
├─ Design Router
├─ Research Router
├─ Execute / Repository Update
└─ Evaluate Router
```

각 Router 아래에서만 필요한 전문 관점을 연다.

#### Design Router
최대 직접 선택:
1. World / System
2. Character / Relationship
3. Narrative / Act
4. Mystery / Foreshadow
5. Craft / Prose Grammar

#### Research Router
최대 직접 선택:
1. Reference research
2. Science / engineering plausibility
3. Genre / market comparison
4. Continuity lookup
5. Evidence verification

#### Evaluate Router
최대 직접 선택:
1. Blindspot Scan
2. Structural Critic
3. Originality / Similarity Red Team
4. Continuity / Canon regression
5. Density / Pacing Harness

이 계층은 기존 전문성을 없애지 않고 **누가 누구를 직접 볼 수 있는지**만 제한한다.

---

## 4. Required Workflow Primitives

필요할 때만 사용하며 매 작업마다 전부 강제하지 않는다.

- Intent / success condition 확인
- Blindspot Scan
- Preflight Trap Check
- 의미 있는 설계 의사결정의 4안 비교
- Reference / exemplar research
- Meta prompting
- Independent Critic / Red Team
- Harness / regression
- Plan drift 기록
- Current status / Canon update

---

## 5. Fiction-specific Execution Rule

장편 소설 작업에서는 한 reasoning node에 세계관/인물/액트/복선/문체/시장/QA를 모두 평면적으로 노출하지 않는다.

기본 순서:

```text
Project Orchestrator
→ 필요한 Domain Router 1개 선택
→ 해당 Specialist 최대 5개 안에서 작업
→ artifact 생성
→ 별도 Evaluate Router 검증
→ Canon/Status 반영
```

독립 Critic에게는 가능하면 Builder의 장황한 이유를 넘기지 않고:

- artifact
- 요구사항
- 금지사항
- acceptance criteria

만 제공한다.

---

## 6. Current v3 Redesign Application

현재 장르 엔진 재설계에서는 다음 4개 노드로 제한한다.

### Node A — Deep Design
1. World/System
2. Character Ensemble
3. Story/Act
4. Mystery/Craft

### Node B — Repository Execution
1. create candidate docs
2. change-control record
3. status routing

### Node C — Evaluation
1. structural critic
2. originality critic
3. science/logic critic
4. pacing-density harness
5. canon regression

### Node D — Promotion
1. keep candidate
2. revise candidate
3. promote v3
4. reject/rollback

---

## 7. Definition of Done

OS adoption is complete when:

- project Canon remains source of truth,
- existing Agents are preserved unless a real boundary change exists,
- runtime local action space is bounded by routers when necessary,
- v3 redesign is isolated from frozen v2 until promotion,
- independent evaluation exists,
- plan drift / Canon reopening is logged.

Current result:

**PASS — methodology adopted without rewriting existing project architecture.**
