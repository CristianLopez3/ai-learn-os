#!/usr/bin/env python3
"""voice-practice-prompt — build a self-contained prompt for practicing a topic
out loud in Claude mobile/desktop (no repo access there).

Pulls the learner's real mastery/weaknesses for the topic(s) from the same
evidence engine learning-state uses (imports state.py directly — no parsing
of printed text), fills a template instructing the mobile session to act as
a verbal explanation coach, and writes it to voice-prompts/<slug>.md.

Usage:
  generate.py <topic> [<topic2> ...] [--out name] [--minutes 15]

Standard library only, aside from importing the sibling state.py module.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE_PY = ROOT / ".claude" / "skills" / "learning-state" / "state.py"
OUT_DIR = ROOT / "voice-prompts"


def load_state_module():
    spec = importlib.util.spec_from_file_location("learning_state", STATE_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def topic_snapshot(state, ctx, topic: str) -> dict:
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)
    metrics, _, prereqs = state.all_metrics(ctx, now)
    m = metrics.get(topic)
    if not m:
        return {"topic": topic, "mastery": "Unknown", "dimensions": {}, "weaknesses": [],
                "evidence_count": 0}
    weak = state.weaknesses(topic, m, metrics, prereqs)
    return {
        "topic": topic,
        "mastery": m["mastery"],
        "score": m["overall_score"],
        "dimensions": m["dimensions"],
        "weaknesses": weak,
        "evidence_count": m["evidence_count"],
    }


def render_prompt(snapshots: list[dict], minutes: int) -> str:
    topics_line = ", ".join(s["topic"] for s in snapshots)
    lines = []
    lines.append(f"You are a verbal explanation coach for a software engineer practicing "
                 f"**{topics_line}** out loud, away from their usual tools. This is a "
                 f"speaking-and-reasoning drill, not a reading exercise.")
    lines.append("")
    lines.append("## Their current state (from their tracked evidence log)")
    for s in snapshots:
        if s["evidence_count"] == 0:
            lines.append(f"- **{s['topic']}**: no evidence yet (Unknown) — treat as a first pass, "
                         f"build from fundamentals.")
            continue
        dims = ", ".join(f"{d}={v:.2f}" for d, v in sorted(s["dimensions"].items()))
        weak = ", ".join(s["weaknesses"]) if s["weaknesses"] else "none flagged"
        lines.append(f"- **{s['topic']}**: mastery={s['mastery']} (score={s['score']:.2f}). "
                     f"Dimensions: {dims}. Weak spots to probe: {weak}.")
    lines.append("")
    lines.append("## How to run this session")
    lines.append(f"1. Budget about {minutes} minutes. Pick the weakest topic/dimension above first "
                 f"if there's a choice; don't just drill what's already strong.")
    lines.append("2. Ask them to **explain it out loud, unscripted** — as if teaching a colleague or "
                 "answering an interviewer. Don't let them read a prepared answer.")
    lines.append("3. Interrupt with follow-ups the moment something is vague, hand-wavy, or the "
                 "wrong mental model — the way a good interviewer would. Push on trade-offs and "
                 "edge cases, not just definitions.")
    lines.append("4. Judge **communication**, not just correctness: pacing, filler words, whether "
                 "they structure the answer (what/why/how) or ramble, whether they can adjust the "
                 "explanation when you signal confusion.")
    lines.append("5. Don't reveal the correct answer early if they're stuck — nudge with a smaller "
                 "question first, the way a Socratic tutor would.")
    lines.append("")
    lines.append("## At the end, produce a short debrief block I can paste back into my learning "
                 "system to log as evidence. Format it exactly like this:")
    lines.append("")
    lines.append("```")
    lines.append("VOICE PRACTICE DEBRIEF")
    for s in snapshots:
        lines.append(f"topic: {s['topic']}")
    lines.append("dimension: explanation   score: <0-1>   notes: <one line, specific gap or strength>")
    lines.append("dimension: knowledge_depth   score: <0-1>   notes: <...>   (only if genuinely tested)")
    lines.append("summary: <2-3 sentences: what to fix before the next attempt>")
    lines.append("```")
    lines.append("")
    lines.append("Use the 0-1 rubric: 0=wrong/no answer, 0.25=fragments, 0.5=partial with gaps, "
                 "0.7=solid with minor gaps, 0.85=strong and articulate, 1.0=mastery. Grade the "
                 "explanation quality itself, not effort or confidence.")
    lines.append("")
    lines.append("Start now: greet them briefly, then ask the first question.")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(prog="generate.py")
    ap.add_argument("topics", nargs="+", help="one or more topic ids from system/prereqs.json")
    ap.add_argument("--minutes", type=int, default=15)
    ap.add_argument("--out", help="output basename (default: <topics>-<date>)")
    args = ap.parse_args()

    state = load_state_module()
    ctx = state.Ctx(ROOT)

    snapshots = [topic_snapshot(state, ctx, t) for t in args.topics]
    prompt = render_prompt(snapshots, args.minutes)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    name = args.out or f"{'-'.join(args.topics)}-{date.today().isoformat()}"
    out_path = OUT_DIR / f"{name}.md"
    out_path.write_text(prompt, encoding="utf-8")

    print(f"wrote {out_path}")
    print()
    print("=" * 70)
    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
