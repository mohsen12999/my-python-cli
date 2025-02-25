"""Tests for the main function."""

import subprocess
import sys

def test_module_execution():
    """Test the module can be executed via Python."""
    result = subprocess.run(
        [sys.executable, "-m", "mpy", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "MPy" in result.stdout