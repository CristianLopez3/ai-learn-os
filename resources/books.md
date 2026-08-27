# Book & Resource Catalog

External learning resources you own, referenced by a stable **id** throughout the system.
Learning paths (`/path`), knowledge notes, and evidence rows cite these by id, e.g.
`[[ddia]] ch. 5` or `--ref "resources/books.md#ddia"`.

## How to use
1. Add one entry per book below with a kebab-case `id` (keep it short and stable).
2. When you request a `/path`, mention which books to lean on — I'll map milestones to specific
   chapters and cite them by id. If you don't specify, I'll suggest which catalogued book fits.
3. Optional: drop the actual files under `resources/files/<id>.<ext>`. Large PDFs are **git-ignored
   by default** (see `.gitignore`) so the repo stays light — the catalog is the durable record.

## Catalog

<!-- Template — copy per book:
### <id>
- **Title:**
- **Author(s):**
- **Edition/Year:**
- **Topics:** <comma-separated topic ids this maps to, e.g. databases, distributed-systems>
- **Format:** physical | pdf | epub  (file: resources/files/<id>.pdf if stored)
- **Notes:** why you're using it / how far you've read
-->

### example-book
- **Title:** _Example: replace or delete this entry_
- **Author(s):**
- **Edition/Year:**
- **Topics:**
- **Format:** physical
- **Notes:** placeholder to show the shape
