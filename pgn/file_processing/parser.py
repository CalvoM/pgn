# from ..game import PGNGame
from pgn.game import PGNGame

from .lexer import MoveToken, Token


class Parser:
    def __init__(self, tokens: list[Token]):
        self._tokens: list[Token] = tokens

    def parse(self) -> list[PGNGame]:
        for tok in self._tokens:
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
