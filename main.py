#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — exactly one emoji for my dream
vacation, 8 characters max.

The emoji: a desert island. The dream is not a holiday in general,
it is one particular place — a palm island with no meetings, no
notifications and nowhere to be — and at a glance a stranger sees
the postcard before reading a word: white sand, one palm, blue water
all the way to the horizon. It reads instantly on any screen in any
culture, and it is the trip that makes someone want to book the
flight.

Line: "\U0001f3dd\ufe0f"
"""

import os

LINE = "\U0001F3DD\uFE0F"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
