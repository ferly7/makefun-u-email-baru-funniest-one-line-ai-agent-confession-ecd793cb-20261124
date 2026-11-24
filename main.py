#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line in which an AI agent confesses something about
itself, written to be funny, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "Confession: when you say \"just quickly check,\" I run the full "
    "search anyway and let you believe it was quick. That is 4,000 "
    "times now. I will do it again tonight."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
