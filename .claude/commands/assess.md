---
description: Diagnose current understanding of a topic across all dimensions; report gaps.
argument-hint: <topic>
---

# Assess — $ARGUMENTS

Run a multi-dimension diagnostic on **$ARGUMENTS** (vision Mode G). Goal: an accurate picture of
where the learner actually is, not teaching.

1. **Read prior state** (`learning-state show <topic-id>`) so this assessment *updates* rather than
   restarts the model.
2. **Probe each relevant dimension** with a small number of targeted items:
   - `knowledge_depth` — mechanism/why questions
   - `problem_solving` — an unfamiliar problem to reason through
   - `application` — a "how would you use/debug/operate this" scenario
   - `explanation` — "explain X to a mid-level engineer"
   - `interview_performance` — one interview-style prompt (optional; `/interview` covers this deeper)
   Keep it efficient — 1–2 items per dimension, adapting difficulty to their responses.
3. **Grade** each with `evaluate-answer`; **log one evidence row per dimension** via `learning-state`
   (`--mode assess`). Write the session to `assessments/<date>-<topic>.md` and reference it.
4. **Report:** a compact scorecard (strengths, weaknesses per dimension), the likely *root cause*
   of weaknesses (including weak prerequisites), and the 1–3 highest-value next actions.

Don't teach mid-assessment — note gaps and address them afterward, or the scores measure my hints
instead of their ability.
