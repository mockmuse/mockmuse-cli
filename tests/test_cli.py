"""Tests for mockmuse-cli."""

from mockmuse_cli import SKILLS, __version__
from mockmuse_cli.cli import build_parser, greet, main


def test_version():
    assert __version__ == "0.1.0"


def test_skills():
    assert SKILLS == [
        "Python",
        "JavaScript",
        "TypeScript",
        "HTML & CSS",
        "Git, GitHub, and automation",
    ]


def test_greet(capsys):
    greet()
    out = capsys.readouterr().out
    assert "Hello from mock.muse" in out
    assert "- Python" in out


def test_main_returns_zero(capsys):
    assert main([]) == 0
    assert "Hello from mock.muse" in capsys.readouterr().out


def test_main_skills_only(capsys):
    assert main(["--skills"]) == 0
    out = capsys.readouterr().out
    assert "Hello from mock.muse" not in out
    assert "- Python" in out


def test_parser_has_version_flag():
    parser = build_parser()
    assert "--version" in parser.format_help()
    assert "--skills" in parser.format_help()
