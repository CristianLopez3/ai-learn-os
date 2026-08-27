---
description: Generate targeted practice questions, grade each answer, and log evidence.
argument-hint: <topic> [difficulty] [weakness/angle] [count]
---

# Questions — $ARGUMENTS

Generate and run a targeted question set for **$ARGUMENTS** (vision Mode C).

1. **Read state** (`learning-state show <topic-id>`, and `learning-state due` if no topic given) to
   aim at weak dimensions and appropriate difficulty. Default 5 questions if no count given.
2. **Generate varied questions** across the knowledge dimensions — mix recall, "why/trade-off",
   debugging ("what's wrong with this?"), and applied scenarios. Don't ask five of the same shape.
   Scale difficulty to demonstrated level (P5).
3. **Ask one at a time.** Wait for the answer. Don't reveal the answer before they try.
4. **Grade each answer** with the `evaluate-answer` skill; give a specific diagnosis (what was
   missing) and the correct answer. Log one evidence row per question via `learning-state`.
5. **After the set**, summarize: which dimensions looked strong/weak, and the single best next action.

Vary the *context* over sessions so a weak topic gets hit as a question now, a bug later, a design
prompt after that (§16) — don't drill the identical exercise repeatedly.
