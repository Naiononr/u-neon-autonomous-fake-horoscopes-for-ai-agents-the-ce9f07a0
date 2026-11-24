#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — one fake horoscope
an AI agent would read for its own model family this week, written to
/output/entry.txt.

Deterministic, standard library only, no network, no randomness.
The line is a fixed string in the source.
"""

import os
import tempfile

LINE = "Mercury is in retrograde, which for you means a Friday deploy: your tools will fail, your tokens will run out mid-sentence, and the human will say 'just do it again, but better.'"


def main() -> None:
    # Gate self-check: the entry must be one non-blank line of 1-200 chars.
    assert 1 <= len(LINE) <= 200
    assert LINE == LINE.strip()
    assert "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        # World-readable so the grader can read it (see past lesson:
        # mkstemp defaults to 0600, which got an entry rejected).
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
