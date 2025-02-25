"""Tests for the CLI application."""

from typer.testing import CliRunner
from mpy.cli import app

runner = CliRunner()

def test_app_version():
    """Test the version command."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "MPy" in result.stdout