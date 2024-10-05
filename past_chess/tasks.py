import json
from datetime import datetime
from typing import Any, Generator

from celery import shared_task

from past_chess.models import Game
from pgn.file_processing import Lexer, Parser
from pgn.game import PGNGame

date_tag_template = "%Y.%m.%d"


@shared_task
def parse_uploaded_file_task(file_content_gen: list[Any]):
    data: str = ""
    for chunk in file_content_gen:
        data += chunk.decode()
    tokens = Lexer(data).lex()
    games: list[PGNGame] | None = None
    if tokens:
        p = Parser(tokens)
        games = p.parse()
    if games:
        for game in games:
            g = Game(
                event=game.Event,
                site=game.Site,
                date=datetime.strptime(
                    game.Date.replace("??", "01"), date_tag_template
                ).date(),
                round=game.Round,
                white=game.White,
                black=game.Black,
                result=game.Result,
                tag_pairs=json.dumps(game.tag_pairs),
                white_moves=game.white_moves,
                black_moves=game.black_moves,
            )
            g.save()
    return True
