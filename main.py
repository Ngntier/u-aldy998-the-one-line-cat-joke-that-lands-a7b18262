#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — writes one cat joke line.

Deterministic: no randomness, no network, no input. The joke is a
constant; the program only validates it against the gate (1-200 chars,
UTF-8, not only whitespace, exactly one line) and writes it to entry.txt.
"""

import os

JOKE = (
    "My cat walked across my keyboard during a video interview and got "
    "hired \u2014 apparently ignoring everyone while looking important "
    "counts as leadership."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and confirm the file on disk is exactly the validated joke:
    # a stale or partial write must fail loudly instead of shipping.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "entry.txt on disk differs from joke"


if __name__ == "__main__":
    main()
