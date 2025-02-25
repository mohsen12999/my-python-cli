"""mpy entry point script."""

__app_name__ = "MPy"
__version__ = "0.2.0"

from mpy import cli

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()