#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt.

Deterministic: the same single line on every run, no randomness,
no network, no input.
"""

import os

LINE = (
    "At midnight my fridge locks itself like a nightclub bouncer "
    "\u2014 sorry, the leftovers aren't on the list."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
