from collections import defaultdict

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


class PGNGame:
    def __init__(self):
        self._tags: dict[str, None | str] = defaultdict(lambda: None)

    def add_tag(self, tag_name: str, tag_value: str):
        setattr(self, tag_name, tag_value)

    def __getattr__(self, name: str):
        if name in valid_pgn_tags:
            return None
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
