#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the office-joke entry to /output/entry.txt (make.fun program/v1)."""
import os

JOKE = (
    "I set my out-of-office to reply to every email with "
    "'Per my last email,' and by Monday it had been promoted to my manager."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
