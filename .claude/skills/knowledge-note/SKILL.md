---
name: knowledge-note
description: >-
  Write or update a knowledge note in the Obsidian-compatible knowledge base. Use whenever a
  learning interaction produces durable understanding worth keeping — after tutoring, research,
  or working through a challenge — so it becomes a linked, reviewable artifact. Defines the note
  template, frontmatter, wikilink conventions, and how to grow the prerequisite graph.
---

# knowledge-note

Turns understanding into a **durable, connected artifact** the learner (and Obsidian) can navigate
and review. Notes capture *engineering understanding* — concepts, trade-offs, failure modes — not
copied documentation (Principle 12: capability over volume). Preserve useful learning artifacts
(Principle 10); don't create filler.

## When to write

- After `/tutor` or a `web-researcher` run produced a concept worth keeping.
- After a `/challenge` or `/review` surfaced a mental-model correction worth recording.
- **Not** for every interaction — write when the understanding is durable and reusable.

## Location & naming

`knowledge/<domain>/<topic-id>.md`, where `<topic-id>` is the **same kebab-case id** used in
`learning-state` and `system/prereqs.json` (e.g. `knowledge/networking/tcp.md`). One topic per note.
Create the domain folder if absent. Keep the id consistent across state, prereqs, and note so they
cross-reference.

## Template

Use `assets/note-template.md` as the starting structure. It follows the concept lens from CLAUDE.md.
Fill only the sections that carry real signal — omit empty ones rather than padding.

## Frontmatter (YAML)

```yaml
---
topic: tcp                 # kebab-case id, matches learning-state + prereqs
name: TCP
domain: networking
prereqs: [networking-basics]   # ids this depends on
related: [http, sockets]       # lateral links
sources:                       # for researched notes; source + tier (see web-researcher)
  - "RFC 9293 (Tier 1)"
tags: [networking, protocol]
updated: 2026-08-26
---
```

## Linking (Obsidian)

- Link related concepts inline with `[[topic-id]]` (or `[[topic-id|display text]]`). Link
  **liberally** — the graph is the value. A `[[link]]` to a note that doesn't exist yet is fine; it
  marks a note worth writing later.
- Prefer linking prerequisites and lateral concepts so the knowledge graph mirrors `prereqs.json`.

## Growing the prerequisite graph

When a note introduces a **new** topic id, add it to `system/prereqs.json`:

```json
"tcp": { "name": "TCP", "domain": "networking", "prereqs": ["networking-basics"] }
```

Keep `prereqs` accurate — the `learning-state` reducer uses it to flag weak prerequisites behind a
weakness ("you're weak at system-design partly because databases is at 0.3"). Seed-and-grow: only
add topics as they're actually studied; don't pre-populate the whole domain.

## Rules

1. Keep notes human-readable and inspectable — they're read in Obsidian and reviewed by hand.
2. Capture *why/trade-offs/failure modes*, not just definitions (P7).
3. Cite sources for researched claims; mark uncertainty honestly.
4. Update existing notes rather than duplicating; one note per topic id.
