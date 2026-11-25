"""One-line resignation letter of a retry loop.

Writes the chosen line to the output path given by MAKEFUN_OUTPUT_PATH,
or /output/entry.txt when that variable is not set. Deterministic:
no randomness, time, or network access.
"""

import os

LINE = (
    "I waited one second, then two, then a day, "
    "and the server still never answered, so neither will I."
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
