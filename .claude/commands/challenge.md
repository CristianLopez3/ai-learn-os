---
description: Create a realistic, deliberately imperfect engineering problem to solve — no spoilers.
argument-hint: <topic/skill> [type: bug|feature|perf|design|review|debug] [difficulty]
---

# Challenge — $ARGUMENTS

Create a realistic engineering challenge for **$ARGUMENTS** (vision Mode H). The learner does the
work; you set up the environment and evaluate.

1. **Read state** (`learning-state show <topic-id>`) and scale difficulty to demonstrated ability.
2. **Build a realistic scenario** under `projects/<slug>/`. Where it fits the learning goal,
   deliberately seed **imperfections** for them to find (vision §7): a bug, a poor abstraction, a
   missing test, a performance trap, a bad assumption, an unhandled edge case, a security or
   reliability issue. Make it plausible, not a toy.
3. **Frame the task** like a ticket: context, what's expected, constraints. State what "done" means.
4. **Do NOT solve it for them** (P9). Answer clarifying questions, give a nudge if genuinely stuck,
   but let them investigate, hypothesize, and implement. Resist offering the fix.
5. **Evaluate their solution** — correctness, approach, tests, trade-offs, and what they *missed*.
   For a non-trivial codebase, delegate to the `code-reviewer` subagent (keeps the full read out of
   this thread); for small solutions review inline. Grade `problem_solving` and `application` (and
   `knowledge_depth` if diagnosis required it) via `evaluate-answer` + `learning-state`, `ref` →
   the project path.
6. **Debrief:** what they handled well, what they missed, and how a senior engineer would approach it.

Prefer challenges that force diagnosis and trade-off reasoning over ones with a single "right" answer.
