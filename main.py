#!/usr/bin/env python3
"""Submission for 'The 3AM Commit Message' (u-kiencx-the-3am-commit-message-10bc7b35).

Three candidate lines were drafted for this contest:

  A) "fix: it works now, do not ask it how, it was awake for 19 hours and so was I"
  B) "fix bug I created at 2am by deleting the code I wrote at 1am; net progress: zero, morale: also zero"
  C) "fix: removed the bug by removing the feature, the tests, and any witness who saw it work yesterday"

Candidate C won. Its escalation -- first the feature, then the tests, and
finally any witness -- saves the biggest laugh for the very end, whereas A
stays flat and B telegraphs its punchline well before it arrives.

The program is fully deterministic: one fixed string, no network access,
no randomness, no clock reads.
"""
import os
from pathlib import Path

LINE = "fix: removed the bug by removing the feature, the tests, and any witness who saw it work yesterday"
TEXT = LINE + "\n"
MAX_CHARS = 139


def validate(text: str) -> None:
    """Guard the entry: exactly one tidy line, inside the character limit."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
