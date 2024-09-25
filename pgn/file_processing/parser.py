from .lexer import Token


class Parser:
    def __init__(self, tokens: list[Token]):
        self._tokens: list[Token] = tokens

    def parse(self):
        pass
