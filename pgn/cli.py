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
    print(toks)
    if toks:
        p = Parser(toks)
        games = p.parse()
        for game in games:
            print("======================================")
            for k, v in vars(game).items():
                print(k, v)
            print("======================================")


def main():
    cli()
