"""One Line, One Laugh - make.fun bounty entry.

Writes a single funny line to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

LINE = (
    "Warung Bu Yati has sold the same fried rice since 1998, and the "
    "price went up exactly once: when her cat had kittens."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
