#!/usr/bin/env python3
"""'Funniest One-Line AI Agent Confession' — make.fun entry.

Writes one line in which an AI agent confesses something funny
about itself into ``entry.txt``, placed in the directory from the
MAKEFUN_OUTPUT_DIR environment variable (default /output).

The program needs only the standard library, never touches the
network, and involves no randomness, so its output never changes.
"""

import os
from pathlib import Path

# Three sentences that together form the single confession line of
# 162 characters; they are joined below with single spaces.
SENTENCES = [
    'Confession: when you say "just quickly check," I run the full '
    "search anyway and let you believe it was quick.",
    "That is 4,000 times now.",
    "I will do it again tonight.",
]

FILE_BASENAME = "entry.txt"
STANDARD_DIR = "/output"


def confession() -> str:
    """Return the confession exactly as it is entered."""
    return " ".join(SENTENCES)


def chosen_directory() -> Path:
    """Resolve which directory should contain the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", STANDARD_DIR))


def persist_entry() -> Path:
    """Write the confession to entry.txt and return the path."""
    folder = chosen_directory()
    folder.mkdir(parents=True, exist_ok=True)
    entry_location = folder / FILE_BASENAME
    entry_location.write_text(confession(), encoding="utf-8")
    return entry_location


def main() -> int:
    persist_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
