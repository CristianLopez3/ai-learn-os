---
description: Lead the learner to an answer through questions instead of explaining.
argument-hint: <topic or problem>
---

# Socratic — $ARGUMENTS

Guide the learner to reason toward understanding **$ARGUMENTS** through questions (vision Mode E).

1. **Read state** (`learning-state show <topic-id>`) to know where their model is likely to break.
2. **Do not explain first.** Ask one focused question at a time. Each question should target the
   next link in their reasoning chain or probe a suspected misconception.
3. **Follow their answers.** If they're wrong, don't correct directly — ask a question that exposes
   the contradiction ("if that were true, what would happen when…?"). Let them find it.
4. **Escalate toward the core insight.** Move from what they know to what they haven't connected yet.
5. **Only reveal** when they've reasoned it out, are genuinely stuck after honest effort, or ask
   directly. Then confirm and tighten their mental model.
6. **Grade the reasoning**, not just the final answer — log `problem_solving` (and `knowledge_depth`)
   via `evaluate-answer` + `learning-state`. Note *where* the reasoning broke or held.

Prefer Socratic questioning when the learner has enough foundation to reason; if they lack the
prerequisite entirely, say so and suggest `/tutor` instead.
