from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Tournaments(models.Model):
    tournament_name = models.CharField(max_length=4096, null=False, blank=False)
    is_finished = models.BooleanField(default=False)
    tournament_winners = models.CharField(max_length=4096)

    class Meta:
        db_table = 'tournaments'


class Games(models.Model):
    class GameStages(models.TextChoices):
        GROUP = "Групповой этап", _("GroupStage")
        FINAL = "Финал", _("Final")
        SEMI_FINAL = "Полуфинал", _("SemiFinal")
        QUARTER_FINAL = "Четвертьфинал", _("QuarterFinal")
        FINALS_1_8 = "1/8 финала", _("1/8Final")

    stage = models.CharField(choices=GameStages.choices, default=GameStages.GROUP)
    players = models.CharField(max_length=4096, null=False, blank=False)
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    winners = models.CharField(max_length=4096, null=True, blank=True)
    score = models.CharField(max_length=255, null=True, blank=True)
    game_date = models.DateTimeField()

    class Meta:
        db_table = 'games'
