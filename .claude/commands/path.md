---
description: Design a structured learning path from current state to a goal. Learner-initiated.
argument-hint: <goal> [timeframe] [constraints]
---

# Learning Path — $ARGUMENTS

Design a structured learning path toward **$ARGUMENTS** (vision §18). This is an intentional plan
the learner requested — it does **not** auto-run or replace their current focus.

1. **Analyze current state.** Read relevant topics via `learning-state` (`show`, `due`) and the
   prerequisite graph in `system/prereqs.json`. Establish where they are now.
2. **Analyze the target:** the capability required, the depth needed, and — critically — the
   prerequisite chain (vision §6). Identify gaps between current state and target, and *which
   weaknesses block progress* ("system design needs HTTP + databases, and databases is at 0.3").
3. **Sequence the path** prerequisite-first: ordered milestones, each with concrete activities
   mapped to the modes (`/tutor`, `/questions`, `/challenge`, `/interview`, `/review`) and a clear
   "done when…" criterion tied to demonstrated capability, not time spent. **Map readings to the
   learner's catalogued books** in `resources/books.md` — cite them by id (`[[id]]`) with specific
   chapters. If a relevant book is catalogued, prefer it; if none fits, say so and suggest sources.
   When you need the actual content of a chapter (to scope it or summarize), use the `book-extract`
   skill to pull just those pages.
4. **Respect constraints** (timeframe, hours/week, interview vs. real-world emphasis). Be realistic
   about pace; front-load the highest-leverage prerequisites.
5. **Write** the plan to `curricula/<slug>.md` with checkboxes and links to the topics/notes.
   Update `system/prereqs.json` if the path introduces new topics.
6. **Confirm**, don't impose: present it, invite adjustments, and note it's a plan to iterate on —
   not an automatic replacement for their current learning (§18).
