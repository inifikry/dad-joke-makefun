#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Dad Joke Showdown".

Writes the exact dad joke to /output/entry.txt.
"""

import os

JOKE = "My son asked why I tell so many dad jokes. I told him it's my puns-ibility as a father."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
