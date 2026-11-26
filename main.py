#!/usr/bin/env python3
"""Contest entry: a one-line commit message worthy of the 3 a.m. hall of fame.

Running this script drops a single pre-written line into ``entry.txt``
inside whichever folder ``MAKEFUN_OUTPUT_DIR`` names (with ``/output``
as the fallback). There is no networking, no randomness and no clock
access anywhere in the file, so repeated runs produce identical bytes.

How the line was picked: three drafts were written for the contest.
The first leaned on tired-programmer humour and never escalated. The
second gave its own punchline away in the opening clause and ran long.
The third deletes the feature, then the tests, then every witness --
the darkest beat lands last -- and that is the line frozen below.
"""

import os
from pathlib import Path

# The commit message itself, preserved word-for-word for delivery.
ENTRY_LINE = (
    "fix: removed the bug by removing the feature, the tests, "
    "and any witness who saw it work yesterday"
)

# Contest ceiling for the message body, trailing newline excluded.
LIMIT = 139

# Complete payload that lands on disk, newline included.
PAYLOAD = ENTRY_LINE + "\n"


def check_payload(payload: str) -> None:
    """Raise if the payload breaks any formatting rule of the contest."""
    core = payload[:-1] if payload.endswith("\n") else payload
    problems = []
    if len(core) == 0 or len(core) > LIMIT:
        problems.append("length must stay between 1 and %d" % LIMIT)
    if core.strip() == "":
        problems.append("a blank message is not an entry")
    if "\n" in core or "\r" in core:
        problems.append("the message has to fit on a single line")
    if core != core.strip() or "  " in core:
        problems.append("padding or doubled spaces found")
    if problems:
        raise ValueError("; ".join(problems))


def emit() -> Path:
    """Write the payload into the target folder and return the file path."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_bytes(PAYLOAD.encode("utf-8"))
    return target


if __name__ == "__main__":
    check_payload(PAYLOAD)
    emit()
