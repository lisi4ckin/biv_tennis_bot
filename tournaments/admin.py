from django.contrib import admin
from .models import Tournaments, Games


@admin.register(Tournaments)
class Tournaments(admin.ModelAdmin):
    list_display = ('tournament_name', 'is_finished', 'tournament_winners')


@admin.register(Games)
class Games(admin.ModelAdmin):
    list_display = ('stage', 'players', 'tournament', 'winners', 'score', 'game_date')
