#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt.

The bounty asks for a single roast line about a smart fridge that
refuses to open after midnight. The joke is the whole entry: the
fridge behaves like a nightclub bouncer with a guest list, and the
leftovers did not make the cut.

Deterministic: the same single line on every run, no randomness,
no network, no input. The program validates its own output before
writing it — the line must be non-empty and stay within the
bounty's 200-character limit — and prints the character count so
anyone running it can see the entry at a glance.
"""

import hashlib
import os

LINE = (
    "At midnight my fridge locks itself like a nightclub bouncer "
    "\u2014 sorry, the leftovers aren't on the list."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify_output(line: str) -> int:
    """Check the entry line and return its character count.

    Raises ValueError if the line is empty or over the bounty limit.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    char_count = len(line)
    if char_count > MAX_CHARS:
        raise ValueError(
            f"entry line is {char_count} chars, over the "
            f"{MAX_CHARS}-char limit"
        )
    return char_count


def sha256_hex(line: str) -> str:
    """Return the SHA-256 hex digest of the entry line."""
    return hashlib.sha256(line.encode("utf-8")).hexdigest()


def main() -> None:
    char_count = verify_output(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {char_count} chars to {OUTPUT_PATH}")
    print(f"sha256: {sha256_hex(LINE)}")


if __name__ == "__main__":
    main()
