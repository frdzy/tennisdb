from django.db import models

from players.models import Side


class GameBase(models.Model):
    sides = models.ManyToManyField(Side)

    serving = models.ForeignKey(Side, related_name="serving")
    receiving = models.ForeignKey(Side, related_name="receiving")

    score_serving = models.IntegerField(default=0)
    score_receiving = models.IntegerField(default=0)

    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)


class Match(GameBase):
    pass


class Set(GameBase):
    match = models.ForeignKey(Match)


class Game(GameBase):
    set = models.ForeignKey(Set)


class Result(models.Model):
    game_base = models.OneToOneField(GameBase, primary_key=True)

    winner = models.ForeignKey(Side, null=True, related_name="won")
    loser = models.ForeignKey(Side, null=True, related_name="lost")

    score_winner = models.IntegerField(blank=True, null=True)
    score_loser = models.IntegerField(blank=True, null=True)
