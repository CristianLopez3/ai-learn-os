---
description: Run a spaced-repetition review session prioritizing weak and overdue topics.
argument-hint: [topic]  (omit to review whatever is most due)
---

# Review — $ARGUMENTS

Run a review session (vision Mode F). Prioritize retention of weak/at-risk material over new topics.

1. **Pick targets.** If a topic is given, review it. Otherwise run `learning-state due --limit 5`
   and take the highest-priority items (weak score + overdue).
2. **Explain the "why"** briefly: "reviewing TCP because problem_solving is 0.30 and it's overdue."
   The learner should understand what the system thinks is weak and the prerequisite chain behind it
   ("you're shaky on X partly because Y is weak", vision §6).
3. **Vary the format** (§16, P4). Don't repeat the exercise that produced the weakness — hit it from
   a new angle: a recall question, then a "spot the bug", then a small design/trade-off prompt.
4. **Grade and log** each interaction via `evaluate-answer` + `learning-state`. Fresh correct
   evidence raises the score and pushes out the next review; fresh weak evidence pulls it in.
5. **Close** with what improved, what's still weak, and what's now scheduled next.

Keep sessions tight — a few high-value reps beat an exhaustive re-teach.
