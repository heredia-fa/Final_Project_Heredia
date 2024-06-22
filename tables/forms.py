from django import forms
from tables.models import Game_table
from datetime import datetime


class Table_form(forms.ModelForm):

    class Meta:
        model = Game_table
        fields = ["name","game","description","date","max_players"]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class Edit_table_form(forms.ModelForm):

    class Meta:
        model = Game_table
        fields = ["name","game","description","date"]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class Player_create_form(forms.Form):

    name = forms.CharField(label= "Nombre")
    lastname = forms.CharField(label= "Apellido")
    email = forms.EmailField()
    age= forms.IntegerField(label="Edad")
    favorite_game = forms.CharField(label="Juego favorito")
    player_picture = forms.ImageField(required=False,label="Imagen")
  