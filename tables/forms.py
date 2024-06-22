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
