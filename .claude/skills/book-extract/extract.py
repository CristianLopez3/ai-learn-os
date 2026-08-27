#!/usr/bin/env python3
"""book-extract — pull a page range from a catalogued book to Markdown, on demand.

Wraps poppler's `pdftotext`. Extracts only the pages you ask for (a chapter, a
section) instead of converting whole books — keeps the repo light and the text
relevant. Output is cached under resources/extracts/<id>/ (git-ignored).

Usage:
  extract.py <book-id> --pages 120-145 [--layout] [--out ch5] [--stdout]
  extract.py <book-id> --info            # page count + resolved path

Requires `pdftotext` on PATH (poppler). Standard library only otherwise.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FILES = ROOT / "resources" / "files"
EXTRACTS = ROOT / "resources" / "extracts"


def resolve(book_id: str) -> Path:
    for ext in (".pdf",):
        p = FILES / f"{book_id}{ext}"
        if p.exists():
            return p
    # epub or missing
    epub = FILES / f"{book_id}.epub"
    if epub.exists():
        sys.exit(f"error: '{book_id}' is an EPUB; pdftotext handles PDF only. "
                 f"Read it natively or convert first.")
    sys.exit(f"error: no PDF for id '{book_id}' in {FILES}. Check resources/books.md.")


def require_pdftotext() -> str:
    exe = shutil.which("pdftotext")
    if not exe:
        sys.exit("error: pdftotext not found on PATH (install poppler).")
    return exe


def page_count(exe: str, pdf: Path) -> int | None:
    # `pdfinfo` is cleaner but may be absent; parse pdftotext's last page via -l large is unreliable.
    info = shutil.which("pdfinfo")
    if not info:
        return None
    out = subprocess.run([info, str(pdf)], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if line.lower().startswith("pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def parse_pages(spec: str) -> tuple[int, int]:
    if "-" in spec:
        a, b = spec.split("-", 1)
        return int(a), int(b)
    n = int(spec)
    return n, n


def main() -> int:
    ap = argparse.ArgumentParser(prog="extract.py")
    ap.add_argument("book_id")
    ap.add_argument("--pages", help="page range, e.g. 120-145 or 42")
    ap.add_argument("--layout", action="store_true",
                    help="preserve physical layout (better for tables/code, worse for flowing prose)")
    ap.add_argument("--out", help="output basename (default: pages-A-B)")
    ap.add_argument("--stdout", action="store_true", help="print instead of caching to a file")
    ap.add_argument("--info", action="store_true", help="show page count + path, then exit")
    args = ap.parse_args()

    pdf = resolve(args.book_id)
    exe = require_pdftotext()

    if args.info:
        n = page_count(exe, pdf)
        print(f"{args.book_id}: {pdf}  (pages: {n if n else 'unknown — pdfinfo unavailable'})")
        return 0

    if not args.pages:
        sys.exit("error: --pages is required (e.g. --pages 120-145). Extract chapters, not whole books.")
    first, last = parse_pages(args.pages)

    cmd = [exe, "-f", str(first), "-l", str(last)]
    if args.layout:
        cmd.append("-layout")
    cmd += [str(pdf), "-"]  # write text to stdout
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        sys.exit(f"error: pdftotext failed: {res.stderr.strip()}")
    text = res.stdout

    header = (f"<!-- extracted from {args.book_id} (resources/books.md), pages {first}-{last} -->\n"
              f"<!-- via pdftotext{' -layout' if args.layout else ''}; copyrighted source, local use only -->\n\n")
    body = header + text

    if args.stdout:
        sys.stdout.write(body)
        return 0

    out_dir = EXTRACTS / args.book_id
    out_dir.mkdir(parents=True, exist_ok=True)
    name = args.out or f"pages-{first}-{last}"
    out_path = out_dir / f"{name}.md"
    out_path.write_text(body, encoding="utf-8")
    print(f"wrote {out_path}  ({len(text):,} chars, pages {first}-{last})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
