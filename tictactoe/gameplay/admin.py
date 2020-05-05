from django.contrib import admin
from .models import Move, Game
# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display =('id', 'first_player', 'second_player','status')
    list_editable = ('status', 'second_player')

admin.site.register(Move)