#!/usr/bin/env python3
"""The Robot Apology (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt: line one owns one
specific mistake, line two names the lesson and the changed behaviour.
Gate: UTF-8 text of 1 to 400 characters, not only whitespace.
"""

from pathlib import Path

TEXT = (
    "I'm sorry I watered the plastic fern on your desk every morning for a month "
    "while the real one quietly died of thirst beside it.\n"
    "I have learned to check for roots before I pour, so from now on I test the "
    "soil first and ask before I water anything that cannot answer back."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-400")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
