"""Monday Morning Punchlines - make.fun submission.

Writes one Monday-morning joke (under 200 characters) to /output/entry.txt.
"""

import os

JOKE = (
    "I set three alarms for Monday morning. My bed defeated all three, "
    "my coffee surrendered, and I arrived at work as a cautionary tale."
)


MAX_CHARS = 200  # the bounty's gate: the entry must fit in 200 characters


def _make_readable(path: str, mode: int) -> None:
    """Best-effort chmod: a shared or read-only output location must not
    crash the entry after the joke itself has been written."""
    try:
        os.chmod(path, mode)
    except OSError:
        pass


def main() -> None:
    if len(JOKE) > MAX_CHARS:
        raise ValueError(f"joke is {len(JOKE)} characters, over the {MAX_CHARS} limit")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # make.fun collects outputs as a different user: keep them readable.
    _make_readable(output_dir, 0o755)
    _make_readable(output_path, 0o644)

    print(JOKE)


if __name__ == "__main__":
    main()
