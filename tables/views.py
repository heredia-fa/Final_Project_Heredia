from tables.models import Player, Game_table
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from tables.forms import Table_form , Edit_table_form , Player_create_form
from django.contrib.auth.mixins import LoginRequiredMixin
from tables.mixins import  Login_staff
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


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


class Player_create(LoginRequiredMixin,CreateView):
    model = Player
    template_name = 'tables/player_create.html'
    fields = ('__all__')
    success_url =  reverse_lazy("tables:players_list")

# def Player_create(req):

#     if req.method =="POST":

#         new_player_form = Player_create_form(req.POST, req.FILES)
#         new_user_form = UserCreationForm(req.POST)


#         if new_player_form.is_valid() and new_user_form.is_valid():

#             data= new_player_form.cleaned_data
#             user_data = new_user_form.cleaned_data

#             user= User(username=user_data["username"])
#             user.set_password(user_data["password1"])
#             user.save()

#             new_player = Player(
#             name = data['name'],
#             lastname = data['lastname'],
#             email = data['email'],
#             age=data['age'],
#             favorite_game=data['favorite_game'],
#             player_picture=data['player_picture'],
#             user_id=user)
#             new_player.save()

#             return render(req, "tables/player_create.html"  , {"message":"Jugador  creado con exito"})
#         else:
#             return render(req, "tables/player_create.html"  , {"message":"Datos invalidos"})
    
#     else: 
#         myform= Player_create_form()
#         userform= UserCreationForm()

#         return render(req, "tables/player_create.html"  , {"myform":myform,"userform":userform})



class Player_update(LoginRequiredMixin,UpdateView):
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



# def Player_delete(req,pk,name):

#     if req.method =="POST":
#         player= Player.objects.get(id=pk)
#         user = player.user_id
#         user.delete()
#         return redirect("tables:players_list")
    
#     else:

#         return render(req, 'tables/player_delete.html', {'pk': pk, 'name':name})
    
        
   


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
    
class Table_detail(LoginRequiredMixin,DetailView):
    model = Game_table
    template_name = 'tables/table_detail.html'
    context_object_name = 'table'


class Table_create(LoginRequiredMixin,CreateView):
    model = Game_table
    form_class = Table_form
    template_name = 'tables/table_create.html'
    success_url =  reverse_lazy("tables:tables_list")



class Table_update(LoginRequiredMixin,UpdateView):
    model = Game_table
    template_name = 'tables/table_update.html'
    form_class = Edit_table_form
    success_url =  reverse_lazy("tables:tables_list")
    context_object_name = 'table'

class Table_delete(LoginRequiredMixin,DeleteView):
    model = Game_table
    template_name = 'tables/table_delete.html'
    context_object_name = 'table'
    success_url =  reverse_lazy("tables:tables_list")


