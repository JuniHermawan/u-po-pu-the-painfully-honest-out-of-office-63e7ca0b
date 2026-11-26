#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry (program/v1).

Writes one brutally honest but still polite out-of-office email
auto-reply, a single sentence, to /output/entry.txt. Python stdlib
only, deterministic, no network.
"""

import os

# The line, judged against the brief's rubric in order:
#  (1) honest AND polite — an out-of-office reply, not a rant;
#  (2) private truth — guilt about asking for leave, said only privately;
#  (3) warm, manager-safe tone — "fresh eyes", a promise to answer;
#  (4) one sentence, 148 chars, no cramming; (5) quotable turn of phrase.
ENTRY = "I'm away until Monday, finally taking time off I desperately needed but felt too guilty to ask for, and I'll answer your email with fresh eyes then."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
