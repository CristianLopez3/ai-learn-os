#!/usr/bin/env python3
"""learning-state engine — evidence log + deterministic reducer.

This script is the source of truth for "what can I actually do?". It never
guesses: interactions append immutable evidence rows to progress/evidence.jsonl,
and this reducer *recomputes* all derived state from that log. See
system/SPEC-learning-state.md for the contract and system/DESIGN.md sec.4 for why.

Standard library only (no pyyaml): machine config is JSON, YAML frontmatter is
hand-formatted on output.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- constants (see SPEC sec.3-5) -------------------------------------------
DIMENSIONS = (
    "knowledge_depth",
    "problem_solving",
    "application",
    "explanation",
    "interview_performance",
)
DIFFICULTY_WEIGHT = {"easy": 0.7, "medium": 1.0, "hard": 1.4}
HALF_LIFE_DAYS = 30.0

# mastery ladder, highest first: (level, predicate(topic_metrics))
def _mastery_ladder():
    def dim(m, name):
        return m["dimensions"].get(name, 0.0)

    return [
        ("Engineering Ready", lambda m: m["overall_score"] >= 0.85 and dim(m, "application") >= 0.8
            and dim(m, "problem_solving") >= 0.8 and m["overall_confidence"] >= 0.75),
        ("Interview Ready", lambda m: dim(m, "interview_performance") >= 0.75
            and m["overall_score"] >= 0.75 and m["overall_confidence"] >= 0.7),
        ("Strong", lambda m: m["overall_score"] >= 0.8 and m["overall_confidence"] >= 0.7),
        ("Proficient", lambda m: m["overall_score"] >= 0.7 and m["dims_covered"] >= 3
            and m["overall_confidence"] >= 0.6),
        ("Applied", lambda m: m["overall_score"] >= 0.6 and dim(m, "application") >= 0.5),
        ("Practicing", lambda m: m["overall_score"] >= 0.5),
        ("Learning", lambda m: m["overall_score"] >= 0.3 and m["overall_confidence"] >= 0.3),
        ("Introduced", lambda m: m["evidence_count"] > 0),
        ("Unknown", lambda m: True),
    ]


# --- paths ------------------------------------------------------------------
def repo_root(override: str | None) -> Path:
    if override:
        return Path(override).resolve()
    # script lives at <root>/.claude/skills/learning-state/state.py
    return Path(__file__).resolve().parents[3]


class Ctx:
    def __init__(self, root: Path):
        self.root = root
        self.log = root / "progress" / "evidence.jsonl"
        self.topics_dir = root / "progress" / "topics"
        self.dashboard = root / "progress" / "DASHBOARD.md"
        self.prereqs = root / "system" / "prereqs.json"


# --- time helpers -----------------------------------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(ts: str) -> datetime:
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def age_days(ts: str, ref: datetime) -> float:
    return max(0.0, (ref - parse_ts(ts)).total_seconds() / 86400.0)


# --- IO ---------------------------------------------------------------------
def read_evidence(ctx: Ctx) -> list[dict]:
    rows: list[dict] = []
    if not ctx.log.exists():
        return rows
    for i, line in enumerate(ctx.log.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"warn: skipping malformed evidence line {i}: {e}\n")
            continue
        if not _valid_row(row, i):
            continue
        rows.append(row)
    return rows


def _valid_row(row: dict, i: int) -> bool:
    for f in ("ts", "topic", "dimension", "score"):
        if f not in row:
            sys.stderr.write(f"warn: line {i} missing '{f}', skipping\n")
            return False
    if row["dimension"] not in DIMENSIONS:
        sys.stderr.write(f"warn: line {i} bad dimension '{row['dimension']}', skipping\n")
        return False
    try:
        row["score"] = float(row["score"])
    except (TypeError, ValueError):
        sys.stderr.write(f"warn: line {i} non-numeric score, skipping\n")
        return False
    return True


def load_prereqs(ctx: Ctx) -> dict:
    if not ctx.prereqs.exists():
        return {}
    try:
        return json.loads(ctx.prereqs.read_text(encoding="utf-8")).get("topics", {})
    except json.JSONDecodeError as e:
        sys.stderr.write(f"warn: prereqs.json unreadable ({e}); ignoring\n")
        return {}


# --- core computation -------------------------------------------------------
def compute_topic(rows: list[dict], now: datetime) -> dict:
    """Reduce one topic's evidence rows into derived metrics (SPEC sec.3-5)."""
    by_dim: dict[str, list[dict]] = {}
    for r in rows:
        by_dim.setdefault(r["dimension"], []).append(r)

    dim_scores: dict[str, float] = {}
    dim_conf: dict[str, float] = {}
    for d, drows in by_dim.items():
        num = den = neff = 0.0
        scores = []
        for r in drows:
            rec = 0.5 ** (age_days(r["ts"], now) / HALF_LIFE_DAYS)
            w = DIFFICULTY_WEIGHT.get(r.get("difficulty", "medium"), 1.0) * rec
            num += r["score"] * w
            den += w
            neff += rec
            scores.append(r["score"])
        dim_scores[d] = num / den if den else 0.0
        spread = statistics.pstdev(scores) if len(scores) > 1 else 0.0
        dim_conf[d] = _clamp(min(1.0, neff / 4.0) * (1.0 - 0.5 * spread))

    dims_covered = len(dim_scores)
    overall_score = sum(dim_scores.values()) / dims_covered if dims_covered else 0.0
    overall_conf = (
        (sum(dim_conf.values()) / dims_covered) * min(1.0, dims_covered / 3.0)
        if dims_covered else 0.0
    )
    last_ts = max((r["ts"] for r in rows), default=now_iso())

    m = {
        "dimensions": {d: round(v, 3) for d, v in dim_scores.items()},
        "dim_confidence": {d: round(v, 3) for d, v in dim_conf.items()},
        "dims_covered": dims_covered,
        "overall_score": round(overall_score, 3),
        "overall_confidence": round(overall_conf, 3),
        "evidence_count": len(rows),
        "last_ts": last_ts,
    }
    m["mastery"] = _mastery(m)
    _schedule(m, now)
    return m


def _mastery(m: dict) -> str:
    for level, pred in _mastery_ladder():
        if pred(m):
            return level
    return "Unknown"


def _schedule(m: dict, now: datetime) -> None:
    s = m["overall_score"]
    base = 2 if s < 0.3 else 4 if s < 0.5 else 8 if s < 0.65 else 16 if s < 0.8 else 32 if s < 0.9 else 60
    interval = base * (0.5 + 0.5 * m["overall_confidence"])
    last = parse_ts(m["last_ts"])
    next_dt = last.fromordinal(last.toordinal() + int(round(interval)))
    m["next_review"] = next_dt.strftime("%Y-%m-%d")
    days_overdue = (now.toordinal() - next_dt.toordinal())
    overdue_bonus = _clamp(days_overdue / 14.0)
    m["review_priority"] = round((1.0 - s) + overdue_bonus, 3)


def weaknesses(topic: str, m: dict, all_metrics: dict, prereqs: dict) -> list[str]:
    out = [d for d, v in m["dimensions"].items() if v < 0.5]
    for p in prereqs.get(topic, {}).get("prereqs", []):
        pm = all_metrics.get(p)
        if pm and pm["overall_score"] < 0.5:
            out.append(f"{p} (prereq)")
    return out


def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


# --- rendering --------------------------------------------------------------
def _yaml_scalar(v) -> str:
    if isinstance(v, float):
        return f"{v:.3f}"
    return str(v)


def render_topic_md(topic: str, m: dict, weak: list[str], prereqs: dict, rows: list[dict]) -> str:
    name = prereqs.get(topic, {}).get("name", topic)
    domain = prereqs.get(topic, {}).get("domain", "unclassified")
    fm = ["---",
          f"topic: {topic}",
          f"name: {name}",
          f"domain: {domain}",
          f"mastery: {m['mastery']}",
          f"overall_score: {m['overall_score']:.3f}",
          f"overall_confidence: {m['overall_confidence']:.3f}",
          f"next_review: {m['next_review']}",
          f"review_priority: {m['review_priority']:.3f}",
          "dimensions:"]
    for d, v in sorted(m["dimensions"].items()):
        fm.append(f"  {d}: {v:.3f}")
    fm.append("weaknesses:")
    for w in weak:
        fm.append(f"  - {w}")
    if not weak:
        fm.append("  []")
    fm += [f"evidence_count: {m['evidence_count']}",
           f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
           "---", ""]

    recent = sorted(rows, key=lambda r: r["ts"], reverse=True)[:8]
    body = [f"# {name} — learning state", "",
            "_Regenerated by `learning-state`. Do not edit by hand; append evidence instead._", "",
            f"**Mastery:** {m['mastery']}  ·  **Score:** {m['overall_score']:.2f}  "
            f"·  **Confidence:** {m['overall_confidence']:.2f}  ·  **Next review:** {m['next_review']}", "",
            "## Recent evidence", "",
            "| date | dimension | score | difficulty | mode | notes |",
            "|---|---|---|---|---|---|"]
    for r in recent:
        body.append(
            f"| {r['ts'][:10]} | {r['dimension']} | {r['score']:.2f} | "
            f"{r.get('difficulty','medium')} | {r.get('mode','-')} | {r.get('notes','')} |"
        )
    return "\n".join(fm + body) + "\n"


def render_dashboard(metrics: dict) -> str:
    order = sorted(metrics.items(), key=lambda kv: kv[1]["review_priority"], reverse=True)
    lines = ["# Learning Dashboard", "",
             "_Regenerated by `learning-state`. Sorted by review priority (highest = review soonest)._", "",
             f"Topics tracked: **{len(metrics)}**  ·  Updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}", "",
             "| topic | mastery | score | conf | next review | priority |",
             "|---|---|---|---|---|---|"]
    for t, m in order:
        lines.append(
            f"| [[{t}]] | {m['mastery']} | {m['overall_score']:.2f} | "
            f"{m['overall_confidence']:.2f} | {m['next_review']} | {m['review_priority']:.2f} |"
        )
    # counts by mastery
    counts: dict[str, int] = {}
    for m in metrics.values():
        counts[m["mastery"]] = counts.get(m["mastery"], 0) + 1
    lines += ["", "## By mastery level", ""]
    for level, _ in _mastery_ladder():
        if counts.get(level):
            lines.append(f"- **{level}:** {counts[level]}")
    return "\n".join(lines) + "\n"


# --- commands ---------------------------------------------------------------
def all_metrics(ctx: Ctx, now: datetime) -> tuple[dict, dict, dict]:
    rows = read_evidence(ctx)
    by_topic: dict[str, list[dict]] = {}
    for r in rows:
        by_topic.setdefault(r["topic"], []).append(r)
    metrics = {t: compute_topic(tr, now) for t, tr in by_topic.items()}
    return metrics, by_topic, load_prereqs(ctx)


def cmd_recompute(ctx: Ctx, _args) -> int:
    now = datetime.now(timezone.utc)
    metrics, by_topic, prereqs = all_metrics(ctx, now)
    ctx.topics_dir.mkdir(parents=True, exist_ok=True)
    for t, m in metrics.items():
        weak = weaknesses(t, m, metrics, prereqs)
        (ctx.topics_dir / f"{t}.md").write_text(
            render_topic_md(t, m, weak, prereqs, by_topic[t]), encoding="utf-8")
    ctx.dashboard.write_text(render_dashboard(metrics), encoding="utf-8")
    print(f"recomputed {len(metrics)} topic(s) -> {ctx.topics_dir} and {ctx.dashboard.name}")
    return 0


def cmd_log(ctx: Ctx, args) -> int:
    if args.json:
        try:
            row = json.loads(args.json)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"error: --json/positional is not valid JSON: {e}\n")
            return 2
    else:
        if not (args.topic and args.dimension and args.score is not None):
            sys.stderr.write("error: need a JSON payload OR --topic --dimension --score\n")
            return 2
        row = {"topic": args.topic, "dimension": args.dimension, "score": args.score}
        for k in ("difficulty", "mode", "notes", "ref"):
            v = getattr(args, k)
            if v is not None:
                row[k] = v
    row.setdefault("ts", now_iso())
    if not _valid_row(row, 0):
        return 2
    ctx.log.parent.mkdir(parents=True, exist_ok=True)
    with ctx.log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"logged: {row['topic']} / {row['dimension']} = {row['score']}")
    return cmd_recompute(ctx, args)


def cmd_show(ctx: Ctx, args) -> int:
    now = datetime.now(timezone.utc)
    metrics, by_topic, prereqs = all_metrics(ctx, now)
    m = metrics.get(args.topic)
    if not m:
        print(f"no evidence for '{args.topic}' yet (mastery: Unknown)")
        return 0
    weak = weaknesses(args.topic, m, metrics, prereqs)
    print(f"{args.topic}: mastery={m['mastery']} score={m['overall_score']:.2f} "
          f"conf={m['overall_confidence']:.2f} next_review={m['next_review']} "
          f"priority={m['review_priority']:.2f}")
    print("  dimensions: " + ", ".join(f"{d}={v:.2f}" for d, v in sorted(m["dimensions"].items())))
    print("  weaknesses: " + (", ".join(weak) if weak else "none"))
    print(f"  evidence_count: {m['evidence_count']}")
    return 0


def cmd_due(ctx: Ctx, args) -> int:
    now = datetime.now(timezone.utc)
    metrics, _, _ = all_metrics(ctx, now)
    order = sorted(metrics.items(), key=lambda kv: kv[1]["review_priority"], reverse=True)
    if args.limit:
        order = order[: args.limit]
    if not order:
        print("no topics tracked yet")
        return 0
    for t, m in order:
        print(f"{m['review_priority']:.2f}  {t:24s} {m['mastery']:16s} "
              f"score={m['overall_score']:.2f} next={m['next_review']}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="state.py", description="learning-state engine")
    p.add_argument("--root", help="repo root (default: inferred from script location)")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("log", help="append one evidence row (then recompute)")
    pl.add_argument("json", nargs="?", help="full evidence row as JSON")
    pl.add_argument("--topic"); pl.add_argument("--dimension")
    pl.add_argument("--score", type=float)
    pl.add_argument("--difficulty", choices=list(DIFFICULTY_WEIGHT))
    pl.add_argument("--mode"); pl.add_argument("--notes"); pl.add_argument("--ref")
    pl.set_defaults(func=cmd_log)

    pr = sub.add_parser("recompute", help="rebuild all derived state from the log")
    pr.set_defaults(func=cmd_recompute)

    ps = sub.add_parser("show", help="print derived state for one topic")
    ps.add_argument("topic"); ps.set_defaults(func=cmd_show)

    pd = sub.add_parser("due", help="list topics by review priority")
    pd.add_argument("--limit", type=int); pd.set_defaults(func=cmd_due)

    args = p.parse_args(argv)
    ctx = Ctx(repo_root(args.root))
    return args.func(ctx, args)


if __name__ == "__main__":
    raise SystemExit(main())
