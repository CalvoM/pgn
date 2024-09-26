import sys
from pathlib import Path

import click

from .file_processing import Lexer, Parser


@click.command()
@click.option("--url", help="URL to download the PGN File from")
@click.argument("file", required=False)
def cli(file: str, url: str):
    if file and not Path(file).is_file():
        print("File provided is not a valid path.")
        sys.exit(1)
    with open(file) as f:
        content = f.read()
    toks = Lexer(content).lex()
    if toks:
        p = Parser(toks)
        games = p.parse()
        print(len(games))


def main():
    cli()
