from django.contrib import admin
from tables.models import *


class Game_table_Admin(admin.ModelAdmin):
  list_display = ["name" , "game" ,"date" ,"max_players"]

class Player_Admin(admin.ModelAdmin):
  list_display = ["name", "lastname", "email", "age"]


# Register your models here.

admin.site.register(Player,Player_Admin)
admin.site.register(Game_table,Game_table_Admin)
