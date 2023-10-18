from django.db import models
from django.contrib import admin
class football_player(models.Model):
    player_name=models.CharField(max_length=30);
    jersey_no=models.IntegerField();
    age=models.IntegerField();
    height=models.IntegerField();
    weight=models.IntegerField();
    goals_scored=models.IntegerField();
    country=models.CharField(max_length=48);
class football_playerAdmin(admin.ModelAdmin):
    list_display=["player_name","jersey_no","age","height","weight","goals_scored","country"]
