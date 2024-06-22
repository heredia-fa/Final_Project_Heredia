from django.urls import path
from django.contrib.auth.views import LogoutView
from login.views import login_view, register, edit_user , show_profile 

app_name = 'login'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page="landing_news:landing"), name='logout'),
    path('profile/', show_profile, name='profile'),
    path('edit_profile/', edit_user, name='edit_profile')
]

