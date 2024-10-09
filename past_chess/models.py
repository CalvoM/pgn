from django.contrib.postgres.fields import HStoreField
from django.db import models


class Game(models.Model):
    """Table representing the game

    Using http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c8.1.1
    To get the mandatory tag pairs
    """

    event = models.CharField(max_length=150, null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    round = models.CharField(max_length=200, null=True, blank=True)
    white = models.CharField(max_length=200, null=True, blank=True)
    black = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    tag_pairs = HStoreField(null=True, blank=True)
    white_moves = models.CharField(max_length=1024, null=True, blank=True)
    black_moves = models.CharField(max_length=1024, null=True, blank=True)
