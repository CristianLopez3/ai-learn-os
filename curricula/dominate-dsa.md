---
goal: Learn DSA and completely dominate it
target_date: 2027-01-31
created: 2026-08-27
horizon: ~22 weeks
assumed_pace: 8–12 focused hrs/week
status: proposed — iterate before starting
---

# Path — Dominate DSA by January 2027

> **What "dominate" means here.** Not "watched the videos." It means: for every core
> structure and paradigm you can (a) *implement it from scratch* correctly, (b) *pick the
> right one* under a novel problem, (c) *reason about its complexity out loud*, and (d)
> *solve a medium/hard on it under time pressure while narrating trade-offs* — i.e.
> **Interview Ready → Engineering Ready** on the mastery ladder, not just "Applied."
> That's the bar every "done when…" below is calibrated to.

## Starting point (2026-08-27)

Every DSA topic is at **Unknown** — no evidence logged yet. So this is a genuine
zero-to-mastery build, not a patch job. That's *good*: we sequence strict
prerequisite-first and let the ability model fill in as you produce evidence. The
first real numbers appear after Milestone 0.

## Your books (we use what you own)

The whole path reads from your catalogued library — no need to buy anything:

- **`[[grokking-algorithms]]`** — gentle first-pass intuition + pictures. Best *first* read per topic.
- **`[[cracking-the-coding-interview.pdf]]`** — Cracking the Coding Interview: the interview-shaped drill source. Chapter per topic + solutions.
- **`[[epi-java]]`** — Elements of Programming Interviews (Java): harder, deeper problem sets in your language.
- **`[[clrs-3e]]`** — CLRS: the rigor/proof reference. Dip in for *why* it works, don't read cover-to-cover.
- **`[[algorithm-design-manual-2e]]`** — Skiena: judgment, war stories, "which technique when."

Java is your interview language, so problems default to `[[epi-java]]`; use
`book-extract` to pull a specific chapter's pages when we scope or summarize one.

## Constraints & assumptions (correct me)

- **Pace:** I assumed **8–12 hrs/week**. Fewer → push the target or trim paradigms; more → compress.
- **Emphasis:** I weighted this **interview-first** (the word "dominate" + your interview-prep books).
  If the real goal is production/engineering mastery over interview speed, say so and I'll rebalance
  toward `/challenge` and `[[algorithm-design-manual-2e]]`.
- **Language:** Java (`[[epi-java]]`). Switchable.

---

## The sequence

Each milestone: **topics → activities (modes) → readings → done when…**. Do them in order;
the prereq graph (`system/prereqs.json`) enforces why. Check boxes as you clear them.

### Milestone 0 — Foundations (Weeks 1–2)
*Topics: `complexity-analysis`, `arrays-strings`, `hashing`*

Everything downstream is measured in Big-O; you can't "dominate" without this reflex.

- [x] `/tutor complexity-analysis` — amortized vs worst-case, space complexity, common classes.
- [ ] Read `[[grokking-algorithms]]` ch. 1 (Big-O) → `[[ctci]]` "Big O" chapter.
- [ ] `/questions complexity-analysis` — cold-analyze the Big-O of 10 given snippets.
- [ ] `/tutor arrays-strings` then `/challenge arrays-strings` — build a dynamic array; explain resize amortization.
- [ ] `/tutor hashing` — collisions, load factor, when hashing degrades to O(n).
- [ ] `/questions hashing` — 5 problems from `[[epi-java]]` (Hash Tables chapter).
- **Done when:** you can state the time/space of any snippet without hesitating, implement a
  hash map's collision handling, and score ≥0.7 on `knowledge_depth` + `problem_solving` for all three.

### Milestone 1 — Linear structures & core techniques (Weeks 3–5)
*Topics: `two-pointers-sliding-window`, `linked-lists`, `stacks-queues`*

- [ ] `/tutor two-pointers-sliding-window` — the pattern family; when a window beats nested loops.
- [ ] `/questions two-pointers-sliding-window` — 8 problems (`[[epi-java]]`, `[[ctci]]` ch. 1).
- [ ] `/challenge linked-lists` — implement singly/doubly lists; reverse, cycle-detect (Floyd), merge.
- [ ] Read `[[ctci]]` ch. 2 (Linked Lists).
- [ ] `/tutor stacks-queues` → `/challenge stacks-queues` — build both; min-stack; queue-from-stacks.
- [ ] Read `[[ctci]]` ch. 3.
- **Done when:** you reach for two-pointers/sliding-window unprompted on the right problem, and
  implement all three structures + their classic manipulations from memory (`application` ≥0.7).

### Milestone 2 — Recursion & search (Weeks 6–8)
*Topics: `recursion-backtracking`, `binary-search`, `sorting`*

The conceptual hinge of the whole path — DP and graphs are recursion in disguise.

- [ ] `/tutor recursion-backtracking` — recursion → call stack → backtracking template.
- [ ] Read `[[grokking-algorithms]]` ch. 3 (Recursion) + `[[ctci]]` ch. 8 (Recursion & DP).
- [ ] `/challenge recursion-backtracking` — subsets, permutations, N-Queens, combination sum.
- [ ] `/tutor binary-search` — the invariant; binary search *on the answer* (not just sorted arrays).
- [ ] `/questions binary-search` — 6 problems incl. rotated-array & "min feasible value" variants.
- [ ] `/tutor sorting` — merge/quick/heap; stability; when built-in vs hand-rolled. `[[grokking-algorithms]]` ch. 2 & 4; `[[clrs-3e]]` for proofs.
- [ ] `/challenge sorting` — implement mergesort + quicksort; explain the recurrence.
- **Done when:** you write a correct binary search with the invariant stated, implement two O(n log n)
  sorts, and fluently trace a recursive call tree (`explanation` ≥0.7, `problem_solving` ≥0.7).

### Milestone 3 — Hierarchical structures (Weeks 9–11)
*Topics: `trees`, `heaps`*

- [ ] `/tutor trees` — binary trees, BST invariant, all traversals (rec + iterative), balancing intuition.
- [ ] Read `[[ctci]]` ch. 4 (Trees & Graphs, trees half); `[[epi-java]]` Binary Trees + BST chapters.
- [ ] `/challenge trees` — BST insert/delete/validate; level-order; lowest common ancestor.
- [ ] `/tutor heaps` — heap property, sift up/down, heapify, priority-queue use-cases.
- [ ] `/questions heaps` — top-k, merge-k-lists, running median (two-heaps).
- **Done when:** you implement a BST + a binary heap from scratch, choose them correctly for a
  "top-k / streaming" prompt, and pass a `/interview` block on trees (`interview_performance` ≥0.65).

### Milestone 4 — Graphs (Weeks 12–14)
*Topics: `graphs`, `graph-algorithms`*

The highest-leverage interview topic and where most candidates fold. Front-loaded prereqs pay off here.

- [ ] `/tutor graphs` — representations (adj list/matrix), BFS vs DFS, when each wins.
- [ ] Read `[[grokking-algorithms]]` ch. 6 (BFS); `[[ctci]]` ch. 4 (graph half).
- [ ] `/challenge graphs` — grid/word-ladder BFS; connected components; cycle detection (directed & undirected).
- [ ] `/tutor graph-algorithms` — Dijkstra, topological sort, union-find, MST (Kruskal/Prim).
- [ ] Read `[[grokking-algorithms]]` ch. 7 (Dijkstra); `[[algorithm-design-manual-2e]]` graph chapter for judgment.
- [ ] `/challenge graph-algorithms` — course-schedule (topo), network-delay (Dijkstra), union-find on a real problem.
- **Done when:** given a word problem you can *recognize it as a graph*, pick BFS/DFS/Dijkstra/topo/union-find
  correctly, and implement it (`problem_solving` + `application` ≥0.7).

### Milestone 5 — Optimization paradigms (Weeks 15–18)
*Topics: `greedy`, `dynamic-programming`, `tries`*

- [ ] `/tutor greedy` — greedy-choice property, exchange argument, why/when greedy fails (→ DP).
- [ ] Read `[[grokking-algorithms]]` ch. 8 (Greedy); interval-scheduling classics.
- [ ] `/tutor dynamic-programming` — memoization → tabulation; identify state & transition. **Budget 2 weeks here.**
- [ ] Read `[[grokking-algorithms]]` ch. 9 (DP) → `[[ctci]]` ch. 8 → `[[epi-java]]` DP chapter (hard set).
- [ ] `/challenge dynamic-programming` — 1D (climbing/house-robber), 2D (edit-distance/LCS), knapsack, coin-change.
- [ ] `/tutor tries` + `/challenge tries` — build a trie; prefix search; word-search II (trie+DFS).
- **Done when:** you can derive a DP recurrence from a fresh prompt (state + transition + base case),
  justify greedy-vs-DP, and solve a hard DP under time (`problem_solving` ≥0.75 — the "dominate" bar).

### Milestone 6 — Integration & interview simulation (Weeks 19–22)
*Topic: `coding-interview` (rolls up everything)*

Mastery is proven under pressure with mixed, unlabelled problems — not topic-by-topic.

- [ ] `/review` twice weekly — call `learning-state due`, hit whatever's overdue/weakest first.
- [ ] `/interview` weekly — full mock, mixed topics, no early answers; judge correctness + reasoning + communication + trade-offs.
- [ ] `/challenge` a **timed mixed set** (unlabelled medium/hard) — forces topic *recognition*, the real skill.
- [ ] `/assess dsa` — final diagnostic across all 5 dimensions; produce a strengths/gaps report.
- **Done when:** ≥2 consecutive clean `/interview` sessions on unseen mediums, and the dashboard shows
  **Interview Ready+** across the core topics with no lingering weak spot flagged by `learning-state due`.

---

## How this stays honest

- After every gradeable moment, evidence lands in `progress/evidence.jsonl` and the dashboard recomputes —
  so "done when…" is checked against *demonstrated* capability, never self-report (P1).
- If `learning-state due` keeps surfacing a topic, the plan bends to it (P4) — don't just march forward.
- This is a **plan to iterate on**, not an auto-runner (§18). It won't replace your day-to-day focus
  unless you choose to follow it.

## Open questions for you

1. **Hours/week?** I assumed 8–12. Your real number reshapes the whole timeline.
2. **Interview-first or engineering-first?** Changes the weighting of `/challenge` vs `/interview` and which books lead.
3. **Java confirmed** as the working language? (Drives `[[epi-java]]` vs a swap.)
4. Want me to **generate Milestone 0 right now** (`/tutor complexity-analysis`) so you start today?
