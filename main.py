"""Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (at most 240 characters) pitching the worst and most
useless app imaginable to <output dir>/entry.txt.

Pure standard library only (os). The output directory honours the
MAKEFUN_OUTPUT_DIR environment variable and defaults to /output.
"""

import os

PITCH = (
    "LawnCast live-streams your front lawn growing in 4K and pings you the "
    "instant a single blade grows one millimetre, because your grass has "
    "been performing for years and it is finally time someone watched."
)

MAX_CHARS = 240


def validate(text):
    """Enforce the RULES.txt gate: UTF-8 text, 1-240 chars, not only whitespace.

    Also enforces the task's own shape: exactly one sentence, i.e. a single
    terminal full stop and no other sentence-ending punctuation.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises on non-UTF-8-encodable content
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    body = text.strip()
    if not body.endswith("."):
        raise ValueError("entry must be one sentence ending with a full stop")
    if body[:-1].count(".") or any(c in body for c in "?!;"):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(PITCH)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print("wrote %s (%d chars)" % (path, len(entry)))


if __name__ == "__main__":
    main()
