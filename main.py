#!/usr/bin/env python3
"""Entry for make.fun's "Loading Screen Gold: A Tip in 200 Characters".

Writes one sharp, funny loading-screen tip to /output/entry.txt
(UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "TIP: Never delete a line you don't understand. The bug you know "
    "is a pet; the bug you're about to meet is wildlife."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
