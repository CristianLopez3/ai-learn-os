---
name: evaluate-answer
description: >-
  Grade a learner's answer, explanation, code, or design response into a calibrated 0-1 score
  per learning dimension, producing evidence rows to log. Use whenever you need to turn a
  response into a defensible grade — in questions, interviews, assessments, reviews, or challenges.
  Pairs with the learning-state skill, which persists the evidence.
---

# evaluate-answer

Turns a response into **calibrated, defensible evidence**. Grade demonstrated capability, not
effort or confidence (Principle 1). Be honest — inflated scores corrupt the ability model and
waste the learner's time.

## Dimensions (score each that the response actually exercises)

| dimension | question it answers |
|---|---|
| `knowledge_depth` | Do they understand the mechanism, not just the label? |
| `problem_solving` | Can they analyze an unfamiliar problem and construct a solution? |
| `application` | Can they use it in a real engineering scenario (build/debug/operate)? |
| `explanation` | Can they communicate it clearly, correctly, at the right level? |
| `interview_performance` | Under interview pressure: correctness + reasoning + communication + trade-offs + recovery? |

Only score dimensions the response genuinely tests. A one-line recall question is
`knowledge_depth` only; a system-design answer may score four dimensions at once — emit one
evidence row per dimension.

## Scoring rubric (0–1 anchors)

| score | meaning |
|---|---|
| 0.0 | no answer, or fundamentally wrong / wrong mental model |
| 0.25 | fragments of correctness; major gaps or misconceptions |
| 0.5 | partially correct; right direction but missing key pieces, hand-waves trade-offs |
| 0.7 | solid and correct; minor gaps; some trade-off awareness |
| 0.85 | strong; complete, correct, articulate; reasons about trade-offs unprompted |
| 1.0 | mastery; precise, considers edge cases, failure modes, alternatives, and cost |

Calibrate against **difficulty**, not against the learner's baseline: a correct answer to a hard
question is stronger evidence (set `difficulty: hard`) — the engine weights it. Don't grade on a
curve for the person; grade the artifact.

## Procedure

1. Identify which dimension(s) the response exercises.
2. For each, pick the score anchor and note the *specific* reason (what was missing or strong).
3. Set `difficulty` (easy/medium/hard) from the question, not the answer quality.
4. Log via the `learning-state` skill — one row per (topic, dimension). Put a one-line diagnostic
   in `notes` and, if the session was written to a file, its path in `ref`.

```
state.py log --topic <id> --dimension <dim> --score <0-1> \
  --difficulty <easy|medium|hard> --mode <mode> --notes "<what was missing/strong>"
```

## Feedback to the learner

After grading, tell them the score *and why*, name the specific gap, and give the corrective
next step — not just "good" / "wrong". A grade with no diagnosis teaches nothing.
