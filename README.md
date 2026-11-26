# mockmuse-cli 🦞

A small Python CLI starter for mock.muse.

It prints a greeting and lists the skills used across my projects — nothing more, nothing secret. It runs with the Python standard library only.

## Install

```bash
pip install mockmuse-cli
```

Requires Python 3.9 or newer. No third-party dependencies.

## Usage

```bash
mockmuse
```

Expected output:

```text
Hello from mock.muse 🦞
Skills:
- Python
- JavaScript
- TypeScript
- HTML & CSS
- Git, GitHub, and automation
```

Other commands:

```bash
mockmuse --help      # show help
mockmuse --version   # show version
mockmuse --skills    # print the skills list only
```

You can also run it as a module:

```bash
python -m mockmuse_cli
```

## Development

```bash
git clone https://github.com/mockmuse/mockmuse-cli.git
cd mockmuse-cli
pip install -e ".[dev]"
python -m pytest
```

## Skills

Python · JavaScript · TypeScript · HTML & CSS · Git / GitHub · Automation · Node.js · Playwright

Web3 (testnet-first): EVM · Solana · SUI · TRON · TON · NEAR.

## Links

- Profile: https://github.com/mockmuse
- Source: https://github.com/mockmuse/mockmuse-cli
- Website: https://mockmuse.github.io
- Web starter: https://github.com/mockmuse/mockmuse-web

## Safety

This package contains no seeds, private keys, passwords, wallet files, `.env` files, or tokens. Never add any.

Motto: DYOR on everything.
