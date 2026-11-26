#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry (round 2 resubmit).

Writes the one word describing our Wi-Fi to /output/entry.txt.
The word is fixed and deterministic — the same word every run.

The word is "Catfish": the Wi-Fi lures you in with a full-bars profile
and delivers no internet behind it. It catfished you — the promise was
fake, the disappointment is real, and the network name itself confesses
the con. Chosen over "Liar" (round 1 word, already held by an earlier
entry from another account — reusing it would share that entry's rate
and never place) and over nine other candidates in a pairwise internal
tournament (see leaderboard-top10.md and mock-judge.md).
"""

import os
import sys


def validate_word(word: str) -> None:
    """Gate: the entry must be one word of 1-20 characters.

    Fails loudly (non-zero exit) so a bad word never ships silently.
    """
    if not word or not word.strip():
        print("ERROR: entry word is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if len(word) > 20:
        print(f"ERROR: entry is {len(word)} chars, over the 20-char limit",
              file=sys.stderr)
        sys.exit(1)
    if any(ch.isspace() for ch in word):
        print("ERROR: entry must be a single word (no whitespace)",
              file=sys.stderr)
        sys.exit(1)


WORD = "Catfish"


def main() -> None:
    validate_word(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
