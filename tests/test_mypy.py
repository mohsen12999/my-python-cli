from typer.testing import CliRunner
import questionary

from mypy import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_new(mocker):
    # Mock user input from questionary
    mocker.patch.object(questionary, "select", return_value=mocker.Mock(ask=lambda: "Basic"))
    mocker.patch.object(questionary, "text", return_value=mocker.Mock(ask=lambda: "my_project"))

    # Run the CLI command
    result = runner.invoke(cli.app, ["new"])

    # Assert that the command executed successfully
    assert result.exit_code == 0
    assert "Project created." in result.stdout


def test_rq():
    result = runner.invoke(cli.app, ["rq"])
    assert result.exit_code == 0
    assert "Requirement file created." in result.stdout


def test_env():
    result = runner.invoke(cli.app, ["env"])
    assert result.exit_code == 0
    assert "Virtual environment activated." in result.stdout


def test_install():
    result = runner.invoke(cli.app, ["install"])
    assert result.exit_code == 0
    assert "Dependencies installed." in result.stdout


def test_gitignore():
    result = runner.invoke(cli.app, ["gitignore"])
    assert result.exit_code == 0
    assert ".gitignore" in result.stdout


def test_help():
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
