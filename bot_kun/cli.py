"""Console script for bot_kun."""

import sys

import click


@click.command()
def main():
    """Console script for bot_kun."""
    click.echo("Replace this message by putting your code into "
               "bot_kun.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
