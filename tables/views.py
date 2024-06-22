from tables.models import Player, Game_table
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from tables.forms import Table_form , Edit_table_form
from django.contrib.auth.mixins import LoginRequiredMixin
from tables.mixins import  Login_staff


#from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


class Player_list(Login_staff,ListView):
    model = Player
    template_name = 'tables/players_list.html'
    context_object_name = 'players'
    ordering = ['-name']

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset= Player.objects.all()
        if query:
            queryset= Player.objects.filter(
                Q(name__icontains=query) |
                Q(lastname__icontains=query)|
                Q(age__icontains=query)
                )
        return queryset.order_by('name')
    
class Player_detail(Login_staff,DetailView):
    model = Player
    context_object_name = 'player'


class Player_create(CreateView):
    model = Player
    template_name = 'tables/player_create.html'
    fields = ('__all__')
    success_url =  reverse_lazy("tables:players_list")


class Player_update(UpdateView):
    model = Player
    template_name = 'tables/player_update.html'
    fields = ('__all__')
    success_url =  reverse_lazy("tables:players_list")
    context_object_name = 'player'

class Player_delete(Login_staff,DeleteView):
    model = Player
    template_name = 'tables/player_delete.html'
    context_object_name = 'player'
    success_url =  reverse_lazy("tables:players_list")



class Tables_list(LoginRequiredMixin,ListView):
    model = Game_table
    template_name = 'tables/tables_list.html'
    context_object_name = 'tables'
    ordering = ['date']

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset= Game_table.objects.all()
        if query:
            queryset= Game_table.objects.filter(
                Q(name__icontains=query) |
                Q(game__icontains=query) 
                )
        return queryset.order_by('name')
    
class Table_detail(DetailView):
    model = Game_table
    template_name = 'tables/table_detail.html'
    context_object_name = 'table'


class Table_create(CreateView):
    model = Game_table
    form_class = Table_form
    template_name = 'tables/table_create.html'
    success_url =  reverse_lazy("tables:tables_list")



class Table_update(UpdateView):
    model = Game_table
    template_name = 'tables/table_update.html'
    form_class = Edit_table_form
    success_url =  reverse_lazy("tables:tables_list")
    context_object_name = 'table'

class Table_delete(DeleteView):
    model = Game_table
    template_name = 'tables/table_delete.html'
    context_object_name = 'table'
    success_url =  reverse_lazy("tables:tables_list")


