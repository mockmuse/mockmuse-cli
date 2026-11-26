#!/usr/bin/env python3
"""mockmuse-cli — a small Python CLI starter for mock.muse.

Default behaviour is unchanged from the original main.py in
mockmuse/mockmuse-cli: print the greeting and the skills list.
"""

import argparse
import sys

from . import SKILLS, __version__


def greet() -> None:
    """Print the greeting and skills, exactly as the original main.py did."""
    print("Hello from mock.muse 🦞")
    print("Skills:")
    for skill in SKILLS:
        print(f"- {skill}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mockmuse",
        description="mock.muse CLI — crypto airdrops, testnets and building helpers.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"mockmuse-cli {__version__}",
    )
    parser.add_argument(
        "--skills",
        action="store_true",
        help="Print the skills list only.",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.skills:
        for skill in SKILLS:
            print(f"- {skill}")
        return 0
    greet()
    return 0


if __name__ == "__main__":
    sys.exit(main())
