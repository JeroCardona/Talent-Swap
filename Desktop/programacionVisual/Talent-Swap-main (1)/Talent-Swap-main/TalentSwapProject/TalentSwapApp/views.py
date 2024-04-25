from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm 
#Forms es un archivo nuevo donde se guardan los formularios
from django.contrib.auth.decorators import login_required

#Modelos y funciones de autenticación
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

#Almacenar y gestionar archivos 
from django.core.files.storage import FileSystemStorage

from .forms import VacancyForm
from .models import Vacancy
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


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def Vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'TalentSwapApp/Vacancy_list.html',{
        'vacancies' : vacancies
    })

def upload_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'TalentSwapApp/upload_vacancy.html', {
        'form': form
    })
