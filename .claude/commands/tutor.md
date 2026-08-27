---
description: Teach a topic at the learner's current level, concept-first, with trade-offs.
argument-hint: <topic> [specific angle or question]
---

# Tutor — $ARGUMENTS

Teach **$ARGUMENTS** (vision Mode A). Concept-first, then technology as implementation context.

1. **Read state first.** Run `learning-state show <topic-id>` to see current mastery, weak
   dimensions, and prior notes. Pitch the explanation there — don't re-teach what's already Strong,
   go deeper on weak spots.
2. **Teach with the concept lens** from CLAUDE.md (what/why/how/problem/trade-offs/where/failure/
   debug/production/interview). Use examples that demonstrate *engineering concepts*, not just syntax
   (vision §8): show a naive version, a production version, the trade-off between them where useful.
3. **Active recall, not a lecture** (P2). After each chunk, ask a short question or pose a
   prediction ("what breaks if…?") before moving on. Don't dump the whole topic at once.
4. **Check understanding, then grade.** End with 1–2 recall/application questions. Grade the
   answers with the `evaluate-answer` skill and log evidence via `learning-state`
   (`knowledge_depth`, and `explanation` if they explained back to you).
5. Offer a concrete next step (a harder angle, a challenge, or a linked prerequisite if one is weak).

Don't confuse a clear explanation *by me* with mastery *by them* (P1) — the evidence comes from
their recall, not my delivery.
