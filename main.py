#!/usr/bin/env python3
"""mockmuse-cli — a small Python CLI starter."""

SKILLS = [
    "Python",
    "JavaScript",
    "TypeScript",
    "HTML & CSS",
    "Git, GitHub, and automation",
]


def main():
    print("Hello from mock.muse 🦞")
    print("Skills:")
    for skill in SKILLS:
        print(f"- {skill}")


if __name__ == "__main__":
    main()
