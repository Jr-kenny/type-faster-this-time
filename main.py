#!/usr/bin/env python3
"""Type Faster This Time.

Writes one honest error message to /output/entry.txt: the brutal truth
about a session that expired while the user was still thinking, and the
form that took their answers with it.

Deterministic: the same single line every run, no network, no randomness,
no input read. The line is checked before it is written, so an overlong
or multi-line message can never reach the output file.
"""

import os

LINE = (
    "Your session expired while you were thinking, and the form took "
    "your answers with it. Log in again, and type faster this time."
)

MAX_CHARS = 200


def write_entry(path):
    """Write the single error line to path, refusing to ship an overlong one."""
    if len(LINE) > MAX_CHARS:
        raise ValueError("error line exceeds %d characters" % MAX_CHARS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


def main():
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
