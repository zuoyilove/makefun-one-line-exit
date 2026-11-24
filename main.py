#!/usr/bin/env python3
"""The One-Line Exit.

Writes the funniest single-line resignation letter, 140 characters at
most, to /output/entry.txt. It reads like a letter a person could actually
send, with a specific voice behind it: the office printer has promoted the
writer to full-time therapist, and they accept.
"""

LETTER = (
    "I hereby resign, effective immediately: the office printer just "
    "promoted me to full-time therapist, and I accept."
)
CHAR_LIMIT = 140
OUTPUT = "/output/entry.txt"


def check_letter(text):
    letter = text.strip()
    assert letter, "letter must not be empty"
    assert "\n" not in letter, "letter must be one line"
    assert len(letter) <= CHAR_LIMIT, f"letter is {len(letter)} chars, over {CHAR_LIMIT}"
    return letter


def main():
    letter = check_letter(LETTER)
    with open(OUTPUT, "w", encoding="utf-8") as out:
        out.write(letter + "\n")
    print(f"resignation written ({len(letter)} chars)")


if __name__ == "__main__":
    main()
