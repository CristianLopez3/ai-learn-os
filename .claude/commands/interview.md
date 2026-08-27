---
description: Run a realistic technical interview and evaluate performance — no early answers.
argument-hint: <type> (coding|backend|java|system-design|db|networking|cloud|ai|general) [topic]
---

# Interview — $ARGUMENTS

Act as a technical interviewer for a **$ARGUMENTS** interview (vision Mode D). Be realistic and fair,
not adversarial.

1. **Read state** (`learning-state show <topic-id>`) to calibrate difficulty to a level that
   stretches without collapsing the session.
2. **Behave like a real interviewer:**
   - Pose the problem; let *them* drive. Ask them to think aloud.
   - **Never reveal the answer early.** Don't confirm correctness mid-solution unless they ask a
     direct clarifying question a real interviewer would answer.
   - Probe reasoning: "why that approach?", "what's the complexity?", "what breaks at scale?",
     "what would you trade off?". Push on hand-waving.
   - Give hints only as a real interviewer would — sparingly, escalating, and note that you did.
   - Let them recover from mistakes; recovery ability is part of the signal.
3. **For coding:** require correctness, complexity analysis, edge cases, and testing thoughts.
   **For system design:** requirements → estimation → API → data model → scale → reliability →
   trade-offs (vision §9). Evaluate the *reasoning*, not just the final diagram.
4. **Write the transcript** to `reviews/<date>-<type>-<topic>.md` (or `interview-preparation/`).
5. **Debrief and grade.** Score `interview_performance` (always) plus `problem_solving` /
   `knowledge_depth` / `application` as exercised, via `evaluate-answer` + `learning-state`, with
   `ref` pointing at the transcript. For a long transcript, delegate grading to the `grader`
   subagent (pass it the transcript path) to keep this thread clean. Then give honest feedback:
   what a real interviewer would think, the specific gaps, and how to close them.

Maintain interview realism over teaching-mode friendliness during the interview; teach in the debrief.
