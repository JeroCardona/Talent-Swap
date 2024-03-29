from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput, PasswordInput

from .models import Vacancy, applyVacancy, Comment
# Registro de usuario (Modelo u "objeto" formulario)

class UserTypeForm(forms.Form):
    USER_CHOICES = [
        ('company', 'Company'),
        ('employee', 'Employee'),
    ]
    user_type = forms.ChoiceField(label='User Type', choices=USER_CHOICES, widget=forms.RadioSelect)

class CompanyRegistrationForm(forms.Form):
    username = forms.CharField(label='Username')
    company_name = forms.CharField(label='Company Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    company_type = forms.CharField(label='Company Type')
    information = forms.CharField(label='Information')
    

class EmployeeRegistrationForm(forms.Form):
    username = forms.CharField(label='Username')
    employee_name = forms.CharField(label='Name and Lastname')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    information = forms.CharField(label='Academic Information')
    interests = forms.CharField(label='Interests')

# Autenticación de usuario (Modelo u "objeto" formulario)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy 
        fields = ('title', 'description', 'document')

class applyVacancyForm(forms.ModelForm):
    class Meta:
        model = applyVacancy
        fields = ('title', 'name', 'profession')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')