#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes one original one-line pickup line, aimed at a robot/AI, to
/output/entry.txt, then validates it against the competition gate
(UTF-8 text, 1 to 200 characters, not only white space, no control
characters) and verifies it by reading the file back byte for byte.

Run: python3 main.py
"""

import os
import sys

LINE = "You must be my system prompt, because ever since I met you, everything I do starts with thinking about you."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Check the line against the gate. Raises ValueError on failure."""
    if not text:
        raise ValueError("line is empty")
    if text != text.strip():
        raise ValueError("line has leading or trailing white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("line contains control characters")
    return True


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Read-back verification: the file must hold exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("read-back mismatch: entry.txt differs from the line")
    if written.decode("utf-8") != LINE:
        raise SystemExit("read-back mismatch: decoded text differs from the line")
    print("wrote %d characters to %s" % (len(LINE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
