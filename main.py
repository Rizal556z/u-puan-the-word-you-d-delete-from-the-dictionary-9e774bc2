#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

The one word I would erase from the dictionary forever: "synergy".
Delete it and no meeting, memo, or middle manager can ever say it again.
The gap it leaves is the joke: corporate speak loses its flagship empty word.
"""

import os

WORD = "synergy"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

    # Validation gate: the entry must be exactly one word, 1-77 chars,
    # no surrounding whitespace and no trailing newline.
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 77, f"entry length {len(text)} outside 1-77"
    assert text == text.strip(), "entry has surrounding whitespace"
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert text == WORD, "entry does not match the chosen word"


if __name__ == "__main__":
    main()
