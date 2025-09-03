"""Tests for the CLI wrapper."""

from click.testing import CliRunner
import subprocess
import sys


def test_cli_exists():
    """Test that the CLI module and command group exist."""
    from src.cli import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "Census data discovery CLI" in result.output


def test_main_entry_point():
    """Test that main.py entry point works."""
    result = subprocess.run(
        [sys.executable, "main.py", "--help"], capture_output=True, text=True
    )

    assert result.returncode == 0
    assert "Census data discovery CLI" in result.stdout
