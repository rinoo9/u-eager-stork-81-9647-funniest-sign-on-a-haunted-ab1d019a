#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one line -- the funniest sign for the door of a haunted server
room -- to /output/entry.txt, exactly as the program/v1 harness expects.

The line is a sign a ghost would tape to the door: the room is haunted
by the engineer who could not resist one last Friday deploy, the oldest
curse in IT. Short, punchy, readable at a glance, and 87 characters --
inside the 1-120 character gate.
"""

import os

SIGN = "NOTICE: This room is haunted by the engineer who said 'just one more deploy on Friday'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SIGN)


if __name__ == "__main__":
    main()
