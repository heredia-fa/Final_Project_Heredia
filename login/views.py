from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from login.forms import User_edit_form

# Create your views here.

def login_view(req):

    if req.method == 'POST':

        myform = AuthenticationForm(req, data=req.POST)

        if myform.is_valid():

            data = myform.cleaned_data

            user = data["username"]
            psw = data["password"]

            user = authenticate(username=user, password=psw)

            if user:
                login(req, user)
                return redirect('landing_news:landing')
            
            else:
                myform = AuthenticationForm()

                return render(req, "login/login.html", {"message": "Datos inválidos intente nuevamente", "myform":myform})
    
        else:
            myform = AuthenticationForm()

            return render(req, "login/login.html", {"message": "Datos inválidos intente nuevamente","myform":myform })
    
    else:

        myform = AuthenticationForm()

        return render(req, "login/login.html", {"myform": myform})
  

def register(req):

    if req.method == 'POST':

        myform = UserCreationForm(req.POST)

        if myform.is_valid():

            data = myform.cleaned_data

            user= data["username"]
            myform.save()
            
            messages.success(req, f'Usuario {user} creado con exito ')
            return redirect('login:login') 
        
        else:
            myform = UserCreationForm()
            return render(req, "login/register.html", {"message": "Datos inválidos" , "myform": myform})
    
    else:

        myform = UserCreationForm()

        return render(req, "login/register.html", {"myform": myform})
    

def show_profile(req):
    return render (req,"login/profile.html")
  
@login_required()
def edit_user(req):

    user = req.user

    if req.method == 'POST':

        myform = User_edit_form(req.POST, instance=req.user)

        if myform.is_valid():

            data = myform.cleaned_data

            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.set_password(data["password1"])

            user.save()

            return render(req, "login/profile.html", {"message": "Datos actualizado con éxito"})
            
        else:

            return render(req, "login/edit_user.html", {"myform": myform})
    
    else:

        myform = User_edit_form(instance=req.user)

        return render(req, "login/edit_user.html", {"myform": myform})
    

# def agregar_avatar(req):

#   if req.method == 'POST':

#     miFormulario = AvatarFormulario(req.POST, req.FILES)

#     if miFormulario.is_valid():

#       data = miFormulario.cleaned_data

#       avatar = Avatar(user=req.user, imagen=data["imagen"])
#       avatar.save()

#       return render(req, "inicio.html", {"message": "Avatar cargado con éxito"})
    
#     else:

#       return render(req, "inicio.html", {"message": "Datos inválidos"})
  
#   else:

#     miFormulario = AvatarFormulario()

#     return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})
    