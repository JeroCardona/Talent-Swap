from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm 
#Forms es un archivo nuevo donde se guardan los formularios
from django.contrib.auth.decorators import login_required

#Modelos y funciones de autenticación
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):

    return render(request, 'TalentSwapApp/home.html') # Home de verdad



def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el usuario en la base de datos

            return redirect('login') # Redirige a la página de login
        
    context = {'registerform': form}
    
    return render(request, 'TalentSwapApp/register.html', context=context) 




def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')
            
        
    context = {'loginform': form}
    
    return render(request, 'TalentSwapApp/login.html', context=context) 


def logout(request):

    auth.logout(request)

    return redirect('home') # Redirige a la página de inicio



@login_required(login_url='login')
def dashboard(request):
    
    return render(request, 'TalentSwapApp/dashboard.html') 
