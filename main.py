#!/usr/bin/env python3
"""One Emoji, One Smile — entry for make.fun's u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to /output/entry.txt: the melting face.

Why this one: a stranger reads it at first glance as melting with warmth —
overwhelmed, in the best way, by something kind. It is gently funny without
a joke that needs explaining, it works from anyone to anyone, and it is a
deliberate pick rather than the first smiley that comes to mind.
"""

import os

EMOJI = "\U0001FAE0"  # MELTING FACE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly one emoji, nothing else,
    # so the gate reads 1 character and the byte tie-break stays minimal.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
