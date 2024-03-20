from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
import os
from django.http import HttpResponse

from . forms import CreateUserForm, LoginForm, CommentForm
#Forms es un archivo nuevo donde se guardan los formularios
from django.contrib.auth.decorators import login_required

#Modelos y funciones de autenticación
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

#Almacenar y gestionar archivos 
from django.core.files.storage import FileSystemStorage

from .forms import VacancyForm
from .models import Vacancy, Comment

from .forms import applyVacancyForm
from .models import applyVacancy

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

def apply_Vacancy(request):
    if request.method == "POST":
        form = applyVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Applied_Vacancies')
    else:
        form = applyVacancyForm()
    return render(request, 'TalentSwapApp/applyVacancy.html', {
        'form': form
    })

def Applied_Vacancies(request):
    template_name = 'TalentSwapApp/Applied_vacancies.html'
    vacancies = applyVacancy.objects.all()
    return render(request, template_name, {'vacancies': vacancies})

def delete_Vacancy(request, title):
    vacancies = applyVacancy.objects.filter(title=title)
    vacancies.delete()
    
    return render(request, 'TalentSwapApp/Applied_vacancies.html')

def vacancy_detail(request, id):
    template_name = 'TalentSwapApp/vacancy_details.html'
    vacancy = get_object_or_404(Vacancy, id=id)
    print(vacancy.title)
    print(vacancy.description)
    print(vacancy.created_on)
    comments = vacancy.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.vacancy = vacancy
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'vacancy': vacancy,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def download_file(request):
    # Ruta al archivo que deseas descargar
    file_path = 'C:/Users/ASUS/Desktop/programacionVisual/Talent-Swap (2)/Talent-Swap/TalentSwapProject/media/vacancies/GUÍA DE CONTRATO E INFORMACIÓN PERTINENTE.pdf'

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response