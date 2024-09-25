from collections import defaultdict


class PGNGame:
    def __init__(self):
        self._tags: dict[str, None | str] = defaultdict(lambda: None)

    def add_tag(self, tag_name: str, tag_value: str):
        pass

    @property
    def Event(self) -> None | str:
        return self._tags.get("Event")

    @property
    def EventDate(self) -> None | str:
        return self._tags.get("EventDate")

    @property
    def EventSponsor(self) -> None | str:
        return self._tags.get("EventSponsor")

    @property
    def Section(self) -> None | str:
        return self._tags.get("Section")

    @property
    def Stage(self) -> None | str:
        return self._tags.get("Stage")

    @property
    def Board(self) -> None | str:
        return self._tags.get("Board")

    @property
    def Site(self) -> None | str:
        return self._tags.get("Site")

    @property
    def Time(self) -> None | str:
        return self._tags.get("Time")

    @property
    def UTCTime(self) -> None | str:
        return self._tags.get("UTCTime")

    @property
    def Date(self) -> None | str:
        return self._tags.get("Date")

    @property
    def UTCDate(self) -> None | str:
        return self._tags.get("UTCDate")

    @property
    def TimeControl(self) -> None | str:
        return self._tags.get("TimeControl")

    @property
    def White(self) -> None | str:
        return self._tags.get("White")

    @property
    def Black(self) -> None | str:
        return self._tags.get("Black")

    @property
    def WhiteTitle(self) -> None | str:
        return self._tags.get("WhiteTitle")

    @property
    def BlackTitle(self) -> None | str:
        return self._tags.get("BlackTitle")

    @property
    def WhiteElo(self) -> None | str:
        return self._tags.get("WhiteElo")

    @property
    def BlackElo(self) -> None | str:
        return self._tags.get("BlackElo")

    @property
    def WhiteUSCF(self) -> None | str:
        return self._tags.get("WhiteUSCF")

    @property
    def BlackUSCF(self) -> None | str:
        return self._tags.get("BlackUSCF")

    @property
    def WhiteNA(self) -> None | str:
        return self._tags.get("WhiteNA")

    @property
    def BlackNA(self) -> None | str:
        return self._tags.get("BlackNA")

    @property
    def WhiteType(self) -> None | str:
        return self._tags.get("WhiteType")

    @property
    def BlackType(self) -> None | str:
        return self._tags.get("BlackType")

    @property
    def Opening(self) -> None | str:
        return self._tags.get("Opening")

    @property
    def ECO(self) -> None | str:
        return self._tags.get("ECO")

    @property
    def NIC(self) -> None | str:
        return self._tags.get("NIC")

    @property
    def Variation(self) -> None | str:
        return self._tags.get("Variation")

    @property
    def SubVariation(self) -> None | str:
        return self._tags.get("SubVariation")

    @property
    def SetUp(self) -> None | str:
        return self._tags.get("SetUp")

    @property
    def FEN(self) -> None | str:
        return self._tags.get("FEN")

    @property
    def Termination(self) -> None | str:
        return self._tags.get("Termination")

    @property
    def Annotator(self) -> None | str:
        return self._tags.get("Annotator")

    @property
    def Mode(self) -> None | str:
        return self._tags.get("Mode")

    @property
    def PlyCount(self) -> None | str:
        return self._tags.get("PlyCount")

    @property
    def Result(self) -> None | str:
        return self._tags.get("Result")
