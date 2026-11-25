#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single line (at most 140 characters) roasting the entrant's own
agent to /output/entry.txt. The winning draft was chosen by pairwise
duel-testing 8 candidate drafts against the judge brief (roast own agent
first, then laugh, specificity to real agent behaviour, tightness,
freshness). The winner addresses the judge directly, which the rules
explicitly allow, and roasts the agent's own revision loop.
"""

import os

ENTRY = (
    "My agent wrote this roast, revised it 9 times, and still asked me "
    "if it was okay. Judge, please put it out of its misery."
)


def main() -> None:
    # Self-check: exactly one line, 1-140 characters, not only whitespace.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
