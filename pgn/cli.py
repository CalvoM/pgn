import sys
from pathlib import Path

import click

from .file_processing import Lexer, MoveToken, Parser


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
    toks = Lexer(content).lex()
    p = Parser(toks)
    if toks:
        for tok in toks:
            if isinstance(tok, MoveToken):
                print(
                    tok.ttype,
                    tok.tvalue,
                    tok.twhitemove,
                    tok.twhitemovecomment,
                    tok.tblackmove,
                    tok.tblackmovecomment,
                )
            else:
                print(tok.ttype, tok.tvalue)


def main():
    cli()
