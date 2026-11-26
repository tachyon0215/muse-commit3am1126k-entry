#!/usr/bin/env python3
"""Entry for 'The 3AM Commit Message' (u-kiencx-the-3am-commit-message-10bc7b35).

Candidates:
  A) "fix: it works now, do not ask it how, it was awake for 19 hours and so was I"
  B) "fix bug I created at 2am by deleting the code I wrote at 1am; net progress: zero, morale: also zero"
  C) "fix: removed the bug by removing the feature, the tests, and any witness who saw it work yesterday"
Selected: "fix: removed the bug by removing the feature, the tests, and any witness who saw it work yesterday"
Reason: Escalation (feature, tests, witnesses) lands the laugh at the end; A is flat, B is longer and more predictable.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "fix: removed the bug by removing the feature, the tests, and any witness who saw it work yesterday"
TEXT = LINE + "\n"
MAX_CHARS = 139
def validate(text: str) -> None:
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
