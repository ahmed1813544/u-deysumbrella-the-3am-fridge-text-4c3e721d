#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the text message a smart fridge sends its owner at 3am.
Stdlib only, deterministic.
"""

import os

LINE = "3am. You've opened me four times tonight. Nothing new has appeared. Go to bed."

# Gate: entry.txt must be UTF-8 text of 1-140 characters, not only whitespace.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "line fails the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
