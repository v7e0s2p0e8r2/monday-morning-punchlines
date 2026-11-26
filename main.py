"""Monday Morning Punchlines - make.fun submission.

Writes one Monday-morning joke (under 200 characters) to /output.
"""

import os

JOKE = (
    "I set three alarms for Monday morning. My bed defeated all three, "
    "my coffee surrendered, and I arrived at work as a cautionary tale."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "joke.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # make.fun collects outputs as a different user: keep them readable.
    os.chmod(output_dir, 0o755)
    os.chmod(output_path, 0o644)

    print(JOKE)


if __name__ == "__main__":
    main()
