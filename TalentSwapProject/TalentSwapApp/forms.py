from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput, PasswordInput

# Registro de usuario (Modelo u "objeto" formulario)

class CreateUserForm(UserCreationForm):
    interests = forms.CharField(widget=TextInput(attrs={'placeholder': 'Interests'}), required=False, max_length=500, help_text='Interests (optional)')
    information = forms.CharField(widget=TextInput(attrs={'placeholder': 'Information'}), required=False, max_length=500, help_text='User Information (optional)')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'information', 'interests']


# Autenticación de usuario (Modelo u "objeto" formulario)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())