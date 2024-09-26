from collections import defaultdict
from typing import override

valid_pgn_tags = (
    "Event",
    "EventDate",
    "EventSponsor",
    "Section",
    "Stage",
    "Board",
    "Site",
    "Date",
    "Time",
    "UTCTime",
    "UTCDate",
    "TimeControl",
    "Round",
    "White",
    "Black",
    "WhiteTitle",
    "BlackTitle",
    "WhiteElo",
    "BlackElo",
    "WhiteUSCF",
    "BlackUSCF",
    "WhiteNA",
    "BlackNA",
    "WhiteType",
    "BlackType",
    "Opening",
    "ECO",
    "NIC",
    "Variation",
    "SubVariation",
    "SetUp",
    "FEN",
    "Termination",
    "Annotator",
    "Mode",
    "PlyCount",
    "Result",
)


class PGNMove:
    def __init__(self, moveobject: dict[str, str | None]):
        self._move_number = moveobject.get("move_number")
        self._white_move = moveobject.get("white_move")
        self._white_move_comment = moveobject.get("white_move_comment")
        self._black_move = moveobject.get("black_move")
        self._black_move_comment = moveobject.get("black_move_comment")

    @property
    def move_number(self):
        return self._move_number

    @property
    def white_move(self):
        return self._white_move

    @property
    def white_move_comment(self):
        return self._white_move_comment

    @property
    def black_move(self):
        return self._black_move

    @property
    def black_move_comment(self):
        return self._black_move_comment

    @override
    def __repr__(self) -> str:
        return f"{self._move_number} {self._white_move} {self._black_move}"


class PGNGame:
    def __init__(self):
        self._tags: dict[str, None | str] = defaultdict(lambda: None)
        self._moves: list[PGNMove] = list()

    def add_tag(self, tag_name: str, tag_value: str):
        setattr(self, tag_name, tag_value)

    def add_move(self, move: PGNMove):
        self._moves.append(move)

    @property
    def moves(self) -> list[PGNMove]:
        return self._moves

    def __getattr__(self, name: str):
        if name in valid_pgn_tags:
            return None
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
