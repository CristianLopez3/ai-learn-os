---
name: learning-state
description: >-
  Read and update the learner's evidence-based ability model. Use whenever a learning
  interaction produces a gradeable signal (a question answered, an interview/assessment,
  a coding challenge, a review) OR when you need to know the learner's current mastery,
  weaknesses, or what is due for review. Appends immutable evidence and recomputes derived
  state; never hand-edit scores.
---

# learning-state

The memory of *what the learner can actually do*. Backed by an append-only evidence log and a
deterministic reducer — never by the model guessing scores. See `system/SPEC-learning-state.md`
for the full contract and `system/DESIGN.md` §4 for the rationale.

## Interpreter

The PATH `python` is a non-functional Windows Store stub. **Always** invoke the real one:

```
"C:\Program Files\MSYS2\ucrt64\bin\python.exe" "<repo>/.claude/skills/learning-state/state.py" <cmd>
```

`<repo>` is the repository root (the folder containing `progress/`). The script infers it from its
own location, so `--root` is only needed if you run it from elsewhere.

## When to READ state (before teaching / choosing what to do)

- `show <topic>` — one topic's mastery, per-dimension scores, weaknesses, next review. Cheap; read
  this before `/tutor`, `/assess`, `/interview` to pitch at the right level.
- `due --limit N` — topics ordered by review priority. Drives `/review`.

## When to WRITE evidence (after any gradeable moment)

Append **one row per gradeable answer** (per-answer granularity — better signal than session aggregates).
Fill `ref` with the path to the transcript/artifact when one exists.

```
state.py log --topic tcp --dimension problem_solving --score 0.4 \
  --difficulty hard --mode interview --notes "confused congestion vs flow control" \
  --ref reviews/2026-08-26-tcp.md
```

or a full JSON row:

```
state.py log '{"topic":"tcp","dimension":"knowledge_depth","score":0.7,"mode":"tutor"}'
```

`log` auto-fills `ts` and **recomputes automatically** — no separate step.

### Fields (see SPEC §1)
- `topic`: kebab-case id (e.g. `tcp`, `dsa-two-pointers`). New topics are fine — they grow the graph.
- `dimension`: one of `knowledge_depth`, `problem_solving`, `application`, `explanation`,
  `interview_performance`.
- `score`: 0–1. Calibrate honestly: 0=wrong/none, 0.5=partial with gaps, 0.8=solid, 1=mastery-level.
  Use the `evaluate-answer` skill's rubric when grading a real answer.
- `difficulty`: `easy`|`medium`|`hard` (weights the evidence). `mode`, `notes`, `ref`: optional context.

## Other commands
- `recompute` — rebuild all derived files from the log (rarely needed manually; `log` does it).
- Derived outputs: `progress/topics/<topic>.md` and `progress/DASHBOARD.md`. **Disposable** — regenerated.

## Rules
1. Never edit `progress/topics/*.md`, `DASHBOARD.md`, or existing lines in `evidence.jsonl`.
2. To correct a bad past grade, append a **new** correcting row (the log is immutable and auditable).
3. One topic per row. Split a mixed answer into multiple rows if it spans dimensions/topics.
4. Grade from demonstrated capability, not the learner's self-report (Principle 1).
