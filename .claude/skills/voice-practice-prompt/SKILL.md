---
name: voice-practice-prompt
description: >-
  Generate a self-contained prompt for practicing a topic out loud in Claude
  mobile/desktop (voice or chat), when the learner has no access to this repo
  or wants to drill verbal explanation. Pulls their real mastery/weaknesses
  from learning-state so the mobile session targets the right gap, and asks
  it to produce a debrief the learner can paste back here to log as evidence.
---

# voice-practice-prompt

Solves a real gap: this repo's modes (`/tutor`, `/interview`, etc.) only work inside
Claude Code, but the learner often wants to practice **saying the explanation out loud**
away from a keyboard — commuting, on their phone, talking through a mock interview
answer. This skill doesn't try to run a call itself (Claude Code can't). Instead it
generates a **portable, self-contained prompt** carrying enough context (topic, current
mastery, flagged weaknesses) that a fresh Claude mobile/desktop session can run a good
verbal coaching session on its own — and asks that session to end with a structured
debrief block the learner brings back here to close the loop.

## When to use

- The learner asks to "practice explaining X out loud", wants a prompt for Claude
  mobile/voice, or says they won't have repo access (traveling, phone-only) but want to
  keep practicing.
- Before a real interview, as a rehearsal on the *communication* dimension specifically —
  this skill is explanation-first, unlike `/interview` which also covers correctness/design.

## Workflow

1. **Pick the topic(s).** If the learner doesn't name one, check `learning-state due` and
   suggest the top overdue/weakest topic — don't default to whatever's easiest.
2. **Generate the prompt:**
   ```
   "C:\Program Files\MSYS2\ucrt64\bin\python.exe" \
     .claude/skills/voice-practice-prompt/generate.py <topic> [<topic2> ...] \
     [--minutes 15] [--out <name>]
   ```
   This reads the same evidence engine as `learning-state show` (imports `state.py`
   directly — no guessing at scores) and writes a ready-to-paste prompt to
   `voice-prompts/<topic>-<date>.md`, printing it too.
3. **Hand it to the learner** to copy into Claude mobile/desktop (voice mode or chat).
   The generated prompt is fully self-contained — it does not reference this repo, any
   file paths, or tools the mobile session won't have.
4. **When they return** with the mobile session's `VOICE PRACTICE DEBRIEF` block, log it
   here as real evidence — don't skip this, it's the entire point of the round-trip:
   ```
   "C:\Program Files\MSYS2\ucrt64\bin\python.exe" .claude/skills/learning-state/state.py log \
     --topic <topic> --dimension explanation --score <from debrief> --mode voice-practice \
     --notes "<from debrief>" --ref voice-prompts/<topic>-<date>.md
   ```
   One row per dimension the debrief reports.

## Notes

- `voice-prompts/` is a scratch outbox, not a knowledge store — plain text prompts, no
  secrets, safe to leave untracked or committed as the learner prefers.
- The generated prompt asks the mobile session for calibrated 0-1 scores using the same
  rubric as `evaluate-answer`, so evidence logged from a voice session is comparable to
  evidence logged in-repo.
- If the debrief is missing or vague, don't force a score — ask the learner what actually
  happened rather than inventing a number (Principle 1: grade demonstrated capability).
