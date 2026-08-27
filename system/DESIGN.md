# Learning System — Design

> Companion to `initial-prompt.md` (the vision). This document is the **engineering design**:
> how the vision maps onto Claude Code's real primitives, what we build, what we deliberately
> don't, and why. Every decision here answers Principle 25: *"Will this help me become a better
> software engineer?"*

Status: **Draft for review** · Last updated: 2026-08-26

---

## 1. Design goals (in priority order)

1. **Reliable memory of my ability** — the system's core value is knowing what I actually can
   and can't do, backed by evidence, not self-report.
2. **The full learning loop works** — Learn → Practice → Recall → Apply → Explain → Evaluate →
   Identify weakness → Review, with real feedback at each step.
3. **Token-efficient and low-drift** — Claude does reasoning; deterministic scripts do bookkeeping.
4. **Human-inspectable** — everything is Markdown/JSON in git; Obsidian can read the knowledge base.
5. **Minimal surface area** — the fewest moving parts that deliver the above (Section 12 & 25 of the vision).

---

## 2. The primitives (what Claude Code actually gives us)

The vision's "agents" and "skills" lists assume a flat world. Claude Code has **five distinct
primitives**, each with different physics. Choosing the wrong one breaks the feature.

| Primitive | Location | Runs in | Multi-turn dialogue with me? | Best for |
|---|---|---|---|---|
| **CLAUDE.md** | repo root / `.claude/` | every session (auto-loaded) | — | operating manual, routing, conventions |
| **Slash command** | `.claude/commands/*.md` | the **main** conversation | ✅ yes | interactive *modes* (tutor, interview…) |
| **Subagent** | `.claude/agents/*.md` | an **isolated** context, returns one report | ❌ no — one shot | isolated, context-heavy, one-shot jobs |
| **Skill** | `.claude/skills/*/SKILL.md` | loaded on demand into whoever calls it | — | reusable procedures + scripts/templates |
| **Hook** | `.claude/settings.json` | deterministic, on events | — | automation guards (later, optional) |

**The rule that shapes everything:** a subagent cannot hold a conversation with me. It receives a
task and returns a single report. Therefore any "agent" in the vision that needs back-and-forth
(teaching, interviewing, Socratic questioning, guided practice, debugging together) **must be a
slash command in the main thread, not a subagent.**

---

## 3. Mapping the vision's 14 "agents" → real primitives

| Vision agent | Needs dialogue? | Real primitive | Why |
|---|---|---|---|
| `web_researcher` | no | **subagent** | context-heavy tool use, returns a research doc — the textbook case |
| `code_review_agent` | no | **subagent** | reviews a diff/codebase, returns findings; isolates noise |
| `assessment_agent` | partial | **subagent (`grader`)** + skill | grade a transcript/answer in isolation → structured record |
| `interview_agent` | **yes** | `/interview` command | live evaluation, no early answers |
| `socratic_agent` | **yes** | `/socratic` command | question-led dialogue |
| `question_generator` | no (but in-thread) | `/questions` command | I read & answer in the thread |
| `review_agent` | **yes** | `/review` command | reads state, drives a review session |
| `project_agent` / `debugging_agent` | **yes** | `/challenge` command | I work the problem interactively |
| `system_design_agent` | **yes** | folded into `/interview` + `/challenge` | design is an interview/challenge type, not a separate engine |
| `curriculum_agent` | no | `/path` command | generates a plan on request (Section 18: I initiate it) |
| `progress_agent` | no | **script report**, surfaced by `/review` | it's a *view over the evidence log*, not an agent |
| `learning_analyzer` | no | **the reducer script** | "you're weak at X because Y" = derived from evidence |
| `ai_engineering_agent` | no | **CLAUDE.md behavior** | a lens applied in every mode, not a separate agent |

**Result: 14 agents → 3 subagents + 8 slash commands + behaviors baked into CLAUDE.md.**

This directly applies vision Section 12: *"Create an agent only when separation of responsibilities
improves reliability, reusability, context management, maintainability, evaluation, or token
efficiency."* The 3 chosen subagents all pass that test; the other 11 fail it.

---

## 4. The core: learning state as an evidence-sourced system

This is the most important design decision and the part most likely to be built wrong.

### 4.1 The wrong way (what to avoid)

> Claude reads `tcp.yaml`, decides "hmm, that answer was okay, bump knowledge_depth to 0.6",
> writes the file back.

This fails on every goal: it **drifts** (LLM guesses deltas), it's **unauditable** (why 0.6?),
it's **token-expensive** (read + rewrite whole files), and two sessions disagree.

### 4.2 The right way — append-only log + deterministic reducer

```
  Interactions                Evidence log                 Derived state
  (tutor, interview,   ──►    progress/evidence.jsonl  ──► progress/topics/<topic>.md
   review, challenge)         (append-only, immutable)     (regenerated, never hand-edited)
        │                            │                            │
   Claude writes ONE            stdlib Python                Obsidian-readable
   small evidence row           reducer + scheduler          Markdown + YAML frontmatter
```

**Evidence record** (one JSON line appended per gradeable interaction):

```json
{"ts":"2026-08-26T14:03:00Z","topic":"tcp","dimension":"problem_solving",
 "mode":"interview","difficulty":"medium","score":0.4,"weight":1.0,
 "notes":"confused congestion control with flow control","ref":"reviews/2026-08-26-tcp.md"}
```

- `dimension` ∈ {knowledge_depth, problem_solving, application, explanation, interview_performance}
  (the four success metrics from vision Section 3, plus explanation).
- `score` ∈ [0,1], `difficulty` scales `weight`, `ref` links the full artifact.

**The reducer** (`state.py`) reads the whole log and computes, per topic:
- current score per dimension = **recency-weighted, difficulty-weighted average** of evidence;
- **confidence** = f(evidence count, recency, consistency) — few/old/erratic evidence → low confidence;
- **mastery level** (Unknown → … → Engineering Ready, vision Section 15) via thresholds that
  require *breadth across dimensions*, not just one high score;
- **next_review date** via an **SM-2-style spaced-repetition** schedule (vision Section 16/Mode F);
- **weakness list** = lowest dimensions + topics whose *prerequisites* are weak (the prereq graph
  from vision Section 6 lives in `system/prereqs.yaml`).

Then it writes each `progress/topics/<topic>.md` and a `progress/DASHBOARD.md`.

### 4.3 Why this is also the best AI-engineering lesson in the whole system

Vision Section 11 wants the system to *teach AI engineering while I use it*. This architecture **is**
the lesson: eval logging, deterministic reducers vs. LLM state mutation, provenance/audit trails,
and separating "the model reasons" from "code persists truth" are exactly what senior AI engineers
get right. We'll annotate it as such.

### 4.4 Storage decisions

- **Log:** `progress/evidence.jsonl` — append-only, JSON Lines, stdlib `json` only.
- **Derived state:** Markdown files with hand-formatted YAML frontmatter (no `pyyaml` dependency,
  since it isn't installed). Human-readable, Obsidian-friendly, git-diffable.
- **Never** hand-edit derived files; to correct history, append a **correcting evidence row**
  (immutable log = auditability). A `state.py --recompute` rebuilds all derived state from the log.

---

## 5. Repository layout (trimmed from vision Section 17)

```
learning/
├── CLAUDE.md                  # operating manual + intent router (auto-loaded)
├── initial-prompt.md          # the vision (source of intent)
├── .claude/
│   ├── commands/              # the 8 interactive modes
│   ├── agents/                # the 3 subagents
│   └── skills/                # learning-state, evaluate-answer, knowledge-note
├── knowledge/                 # Obsidian notes, [[wikilinked]], by domain
├── curricula/                 # learning paths (I initiate these)
├── projects/                  # engineering challenges & their code
├── assessments/               # assessment session artifacts
├── reviews/                   # review + interview session transcripts
├── interview-preparation/     # interview history & prep material
├── progress/
│   ├── evidence.jsonl         # THE append-only log (source of truth for ability)
│   ├── topics/                # derived per-topic state (regenerated)
│   └── DASHBOARD.md           # derived overview (regenerated)
└── system/
    ├── DESIGN.md              # this file
    ├── prereqs.yaml           # the concept prerequisite graph
    └── conventions.md         # naming, frontmatter, wikilink rules
```

**Dropped from the vision tree:** top-level `agents/`, `skills/`, `workflows/`, `prompts/`,
`templates/` as *content* directories — those are now `.claude/` primitives or skill assets, not
documentation. This removes duplication (Principle 12: capability over volume).

---

## 6. The 8 slash commands (interactive modes)

Each command is thin: it loads shared context, sets the behavior, and (where relevant) calls the
`learning-state` skill to log evidence at the end. Mapped to vision Modes A–H.

| Command | Vision mode | Behavior contract (summary) |
|---|---|---|
| `/tutor <topic>` | A | Explain at my level; use the 10-question lens (Section 19); end by logging an `explanation`/`knowledge_depth` self-check. |
| `/socratic <topic>` | E | Never explain first; question me toward the answer; log reasoning quality. |
| `/questions <spec>` | C | Generate targeted questions by topic/difficulty/weakness; I answer; each answer → evidence via `evaluate-answer`. |
| `/interview <type>` | D | Act as interviewer, **no early answers**; evaluate correctness/reasoning/communication/trade-offs; log `interview_performance`. |
| `/review [topic]` | F | Read state, prioritize weak/overdue topics, vary the context (question→code→design), log outcomes. |
| `/assess <topic>` | G | Multi-dimension diagnostic; emit strengths/weaknesses/next actions; log per-dimension evidence. |
| `/challenge <spec>` | H | Build an imperfect system (bugs/smells/edge cases); **don't solve it for me**; log `problem_solving`/`application`. |
| `/path <goal>` | Sec 18 | Analyze state + prereqs, produce a structured plan into `curricula/`; does **not** auto-run. |

Shared behaviors (in CLAUDE.md, so every command inherits them): adapt difficulty (Principle 5),
prefer active recall (Principle 2), detect weaknesses (Principle 4), explain trade-offs (Principle 7),
don't solve prematurely (Principle 9).

---

## 7. The 3 subagents

| Subagent | Trigger | Input → Output | Model |
|---|---|---|---|
| `web-researcher` | research request; called from `/tutor`, `/path`, or directly | question → structured research doc in `knowledge/` following the Tier 1–5 source hierarchy (vision Section 10) | Sonnet (cheap, tool-heavy) |
| `grader` | end of `/interview`, `/assess` | transcript + rubric → evidence rows (JSON) | Sonnet |
| `code-reviewer` | end of `/challenge`, or on request | code/diff → findings (correctness, tests, perf, security) | Sonnet |

Why subagents and not commands: all three are **one-shot, context-heavy, and return an artifact**;
isolating them keeps the main teaching thread clean and cheap.

---

## 8. The 3 skills

| Skill | Owns | Key assets |
|---|---|---|
| `learning-state` | the evidence architecture | `state.py` (reducer+scheduler, stdlib-only), evidence schema, `log_evidence` helper, SM-2 scheduler |
| `evaluate-answer` | the grading rubric | the 4+1 dimension rubric, scoring guidance, evidence-row format |
| `knowledge-note` | Obsidian note conventions | note template, frontmatter spec, `[[wikilink]]` + prereq-tagging rules |

Skills (not commands) because they're **reusable procedures called from multiple places** and carry
**scripts/templates**. `learning-state` is the keystone — every mode logs through it.

---

## 9. Model policy (deferred per your choice)

- Interactive teaching modes: **decide per-mode as we tune** (default strong model for `/interview`
  and system-design work; lighter is fine for `/questions` drills).
- Subagents: **Sonnet** — they're tool-heavy and one-shot; depth matters less than cost.
- Reducer/scheduler: **no model** — pure Python.

---

## 10. Python toolchain (verified 2026-08-26)

- Real interpreter: **Python 3.12.7** at `C:\Program Files\MSYS2\ucrt64\bin\python.exe`.
- Default `python`/`python3` on PATH = **Windows Store stub (not usable)**; `py` launcher absent.
- `pyyaml` **not installed**.
- **Decision:** all scripts are **standard-library only**; YAML frontmatter is hand-formatted.
  The `learning-state` skill will record the correct interpreter path so invocations don't hit the stub.

---

## 11. What we deliberately do NOT build (yet)

Per Principles 12 & 25, these stay out until a concrete need appears:
- Separate `curriculum`, `progress`, `learning_analyzer`, `ai_engineering` agents — all are views
  over the evidence log or behaviors, already covered.
- Hooks/automation — no need until a real repetitive guardrail emerges.
- Auto-generated learning paths — vision Section 6 & 18 are explicit: paths are **initiated by me**.
- A DB or any service — flat files in git are the correct scale for one learner.

---

## 12. Build phases

| Phase | Deliverable | Proves |
|---|---|---|
| **0 — Spine** | git init, scaffold, `CLAUDE.md`, `learning-state` skill (`state.py` + schema) | the system can remember ability from evidence |
| **1 — Modes** | 8 slash commands + `evaluate-answer` skill | the full learning loop is usable end-to-end |
| **2 — Subagents** | `web-researcher`, `grader`, `code-reviewer` | research + isolated grading/review work |
| **3 — Knowledge** | `knowledge-note` skill + `prereqs.yaml` + 2 seed notes | the Obsidian knowledge base + prereq graph work |

Each phase is independently useful; we stop and evaluate after each.

---

## 13. Open questions for review

1. **Topic taxonomy** — do we adopt the vision's domain list as the canonical topic IDs, or start
   with a small seed set and grow the prereq graph as topics are actually studied? (I lean: seed + grow.)
2. **Evidence granularity** — one evidence row per answer, or one aggregate row per session? (I lean:
   per answer for signal, with a session `ref` linking them.)
3. **Review scheduling** — full SM-2, or a simpler "overdue = lowest confidence × time-since-review"
   to start? (I lean: simple first, upgrade when there's enough data to matter.)
```
