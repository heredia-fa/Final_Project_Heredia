from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class User_edit_form(UserChangeForm):

    password= forms.CharField(
        help_text="",
        widget= forms.HiddenInput(), required=False
    )

    password1=forms.CharField(label="Contraseña",  widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña",  widget=forms.PasswordInput)

    class Meta:
        model = User
        fields= ["first_name",  "last_name", "email"]

    def clean_password2(self):
        password1=self.cleaned_data["password1"]
        password2=self.cleaned_data["password2"]
        
        if password1 != password2:
            raise forms.ValidationError ("Las contraseñas no coinciden")
        return password2

    def __init__(self, *args, **kwargs):
        super(User_edit_form, self).__init__(*args, **kwargs)
        #self.fields['username'].label = 'Nombre de Usuario'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Correo Electrónico'    
