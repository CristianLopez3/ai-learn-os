---
name: book-extract
description: >-
  Pull a specific chapter or page range from one of the learner's catalogued books into Markdown,
  on demand, so it can be analyzed or summarized. Use when a learning path or explanation should
  draw on a book the learner owns (resources/books.md). Extracts only the pages needed via
  pdftotext and caches them locally — never bulk-converts whole books.
---

# book-extract

Gives Claude the *relevant pages* of a book on demand, without dumping hundreds of MB of
copyrighted text into the repo. The catalog (`resources/books.md`) is the index; the PDFs live in
`resources/files/<id>.pdf` (git-ignored); extracts are cached in `resources/extracts/<id>/`
(git-ignored). See `system/DESIGN.md` for why on-demand beats bulk conversion.

## When to use
- A `/path` milestone or a `/tutor` explanation should cite a book the learner owns.
- The learner asks "what does <book> say about X" or "summarize chapter N of <book>".
- Building a knowledge note grounded in a specific source.

Prefer this over reading whole books. Extract chapters, not volumes.

## Tools available
- **`pdftotext`** (poppler, on PATH) — fast, deterministic text extraction. Primary path.
- **`pdfinfo`** — page count, if present.
- **Native PDF Read** (the Read tool's `pages` param) — fallback for scanned/image-heavy pages,
  figures, or when layout fidelity matters and pdftotext output is garbled.

## Workflow

1. **Find the id** in `resources/books.md` (e.g. `ddia`).
2. **Locate the pages.** Books have no TOC metadata here. To find a chapter's page range, either
   extract the front matter (`--pages 1-25`) to read the table of contents, or use the Read tool on
   the PDF's first pages. Note: **PDF page numbers ≠ printed page numbers** (front matter offset) —
   verify by spot-checking.
3. **Extract** with the script:
   ```
   "C:\Program Files\MSYS2\ucrt64\bin\python.exe" \
     .claude/skills/book-extract/extract.py <id> --pages <first>-<last> [--layout] [--out <name>]
   ```
   - `--layout` preserves columns/tables/code alignment; omit it for flowing prose (cleaner).
   - `--stdout` prints instead of caching (good for a one-off you won't reuse).
   - `--info` shows the page count and resolved path.
   Output is cached to `resources/extracts/<id>/<name>.md`.
4. **Read the extract**, then do the real work: explain, summarize into a `knowledge-note`, or map
   it into a learning path. Cite the source as `[[<id>]] pp. <first>-<last>`.

## Notes & limits
- **EPUB** (`mastering-ml-algorithms-2e`) isn't supported by pdftotext — read it natively or skip.
- pdftotext can mangle heavy tables, math, and multi-column layouts — switch to native Read for those.
- Extracts are a **local cache** (git-ignored): copyrighted text stays off GitHub. The catalog and
  your own synthesized notes are what get committed.
- Keep extractions small and purposeful; if you find yourself pulling a whole book, reconsider.
