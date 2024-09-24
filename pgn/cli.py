from pathlib import Path
import sys
import click

from pgn.file_processing.lexer import Lexer


@click.command()
@click.option("--url", help="URL to download the PGN File from")
@click.argument("file", required=False)
def cli(file: str, url: str):
    print(file, url)
    if file and not Path(file).is_file():
        print("File provided is not a valid path.")
        sys.exit(1)
    with open(file) as f:
        content = f.read()
    Lexer(content).lex()


def main():
    cli()
