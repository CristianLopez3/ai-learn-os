# ai-learn-os

A personal, **evidence-driven software-engineering training system** that runs inside Claude Code.
It's not a notes repo — it's an environment that teaches you, questions you, interviews you,
challenges you, grades what you actually demonstrate, and remembers your real ability over time so
every session targets your weakest, most valuable gaps.

> Goal (Principle 25): optimize for **engineering capability**, not documentation volume.
> Vision: [`initial-prompt.md`](initial-prompt.md) · Design: [`system/DESIGN.md`](system/DESIGN.md)

---

## How it works in one picture

```
You interact in a mode  ──►  Claude grades what you demonstrate  ──►  one evidence row appended
        ▲                            (evaluate-answer rubric)          to progress/evidence.jsonl
        │                                                                      │
        │                                                          deterministic reducer (state.py)
        │                                                                      ▼
   next session targets   ◄──  mastery, confidence, weaknesses,   ◄──  progress/topics/*.md
   your weakest gaps            next-review dates (recomputed)          progress/DASHBOARD.md
```

Your scores are **never guessed by the model** — they're *computed* from an append-only log of
evidence. That makes them auditable ("why is my TCP score 0.47?" → look at the evidence) and
drift-free. See [`system/DESIGN.md` §4](system/DESIGN.md).

---

## Quick start

You interact in plain language or with slash commands — both work; the commands just make intent
explicit. A good first session:

```
/assess tcp
```

This diagnoses where you actually are on a topic across all dimensions, logs evidence, and updates
the dashboard. Then check what the system now thinks:

```
/review          # shows what's weakest / most overdue and drills it
```

Open [`progress/DASHBOARD.md`](progress/DASHBOARD.md) (best in Obsidian — see below) to watch your
ability model take shape.

> **Note:** the dashboard is empty until you run your first session. Nothing is fabricated.

---

## The learning modes

| Command | What it does |
|---|---|
| `/tutor <topic>` | Teaches a topic at your level — concept-first, trade-offs, with active recall. Offers to save a knowledge note. |
| `/socratic <topic>` | Leads you to the answer through questions instead of explaining. |
| `/questions <topic> [difficulty] [count]` | Generates targeted practice questions, grades each answer. |
| `/interview <type> [topic]` | Runs a realistic mock interview (coding, backend, system-design, …) — no early answers — then debriefs. |
| `/review [topic]` | Spaced-repetition session on your weakest / overdue material, varying the format. |
| `/assess <topic>` | Multi-dimension diagnostic → scorecard, root-cause of weaknesses, next actions. |
| `/challenge <topic> [type]` | Builds a realistic, deliberately imperfect system for you to fix/extend — won't solve it for you. |
| `/path <goal> [timeframe]` | Designs a prerequisite-first learning path into `curricula/`. You initiate it; it never auto-runs. |

Every mode reads your current state before starting (so difficulty fits you) and logs evidence
after (so the model stays current). You can also just ask — "explain HTTP keep-alive", "interview
me on databases" — and the same behavior applies.

### What gets measured

Each answer is graded on the dimensions it exercises — `knowledge_depth`, `problem_solving`,
`application`, `explanation`, `interview_performance` — on a 0–1 scale calibrated to difficulty.
Topics move through a mastery ladder (`Unknown → Introduced → Learning → Practicing → Applied →
Proficient → Strong → Interview Ready → Engineering Ready`) that requires **breadth**, not one
lucky answer.

---

## A suggested learning loop

1. **Baseline** a topic with `/assess <topic>`.
2. **Learn** the weak parts with `/tutor` or `/socratic`; save durable understanding as a note.
3. **Practice** with `/questions` and `/challenge`.
4. **Pressure-test** with `/interview`.
5. **Review** regularly with `/review` — the system tells you what's due and why.
6. Ask for a `/path` when you want a structured multi-week plan toward a goal.

Do a little every day; the spaced-review scheduler keeps weak topics resurfacing until they stick.

---

## Repository layout

```
CLAUDE.md              Operating manual + intent router (auto-loaded every session)
initial-prompt.md      The original vision
README.md              This file
system/                DESIGN.md, SPEC-learning-state.md, prereqs.json (topic graph)
progress/
  evidence.jsonl       Append-only source of truth for your ability (never hand-edited)
  topics/<topic>.md    Derived per-topic state (regenerated)
  DASHBOARD.md         Derived overview, sorted by review priority (regenerated)
knowledge/             Your Obsidian knowledge base: notes by domain, [[wikilinked]]
curricula/             Learning paths you've requested
projects/              Engineering challenges and their code
reviews/               Interview & review transcripts
assessments/           Assessment session artifacts
interview-preparation/ Interview history & prep
.claude/
  commands/            The 8 mode commands
  agents/              web-researcher, grader, code-reviewer (isolated, one-shot helpers)
  skills/              learning-state, evaluate-answer, knowledge-note
```

---

## Using it with Obsidian (optional but recommended)

Open this repository as an Obsidian vault. Notes in `knowledge/` use `[[wikilinks]]` and YAML
frontmatter, so Obsidian's graph view shows how concepts connect — and the prerequisite graph in
`system/prereqs.json` mirrors those links. GitHub is the source of truth; Obsidian is the reader.

---

## Under the hood (and why it's also an AI-engineering lesson)

- **Requirements:** [Git Bash / a POSIX shell] + Python **3.12** (the repo is validated against the
  MSYS2 interpreter at `C:\Program Files\MSYS2\ucrt64\bin\python.exe`; the default Windows `python`
  is a non-functional Store stub). Scripts are **standard-library only** — no `pip install` needed.
- **The state engine** (`.claude/skills/learning-state/state.py`) is a worked example of good AI
  engineering: eval logging, a *deterministic reducer* instead of letting an LLM mutate state,
  provenance you can audit, and clean separation between "the model reasons" and "code persists
  truth." Read it — it's meant to teach.
- **Design discipline:** the original vision listed ~28 components; this build is 14, because the
  interactive modes must live in the main conversation (a subagent can't hold a dialogue) and the
  "progress/analyzer" agents were really just *views over one log*. See `system/DESIGN.md` §3.

---

## Extending it

Add components only when a concrete need appears (Principles 12 & 25). Natural next steps as you use
it: upgrade the review scheduler to full SM-2 once there's enough data, grow `system/prereqs.json`
as you study new topics, and let `/tutor` + `web-researcher` fill out `knowledge/` with real notes.
