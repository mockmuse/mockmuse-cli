# mockmuse-cli 🦞

A small Python CLI starter for mock.muse.

It prints a greeting and lists the skills used across my projects — nothing more, nothing secret. It runs with the Python standard library only.

## Run

```bash
python3 main.py
```

Expected output:

```text
Hello from mock.muse 🦞
Skills: Python, JavaScript, TypeScript, HTML & CSS, Git, GitHub, automation
```

## Structure

```text
mockmuse-cli/
├── main.py           # Entry point — prints the greeting and skills
├── requirements.txt  # Standard library only, no third-party packages
└── README.md         # This file
```

Planned structure as the CLI grows (plan-first, no deployment without a separate go-ahead):

```text
mockmuse-cli/
├── mockmuse/
│   ├── __init__.py
│   ├── cli.py        # Argument parsing
│   └── skills.py     # Skill / project listing
└── tests/
    └── test_cli.py   # Self-tests
```

## Skills

Python · JavaScript · TypeScript · HTML & CSS · Git / GitHub · Automation · Node.js · Playwright

Web3 (testnet-first): EVM · Solana · SUI · TRON · TON · NEAR.

## Links

- Profile: https://github.com/mockmuse
- Website: https://mockmuse.github.io
- Web starter: https://github.com/mockmuse/mockmuse-web

## Safety

This repo contains no seeds, private keys, passwords, wallet files, `.env` files, or tokens. Never add any.

Motto: DYOR on everything.
