from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import download_file

urlpatterns = [

    path('', views.homepage, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('logout/', views.logout, name='logout'),

    path('vacancies/' , views.Vacancy_list, name= 'Vacancy_list'),

    path('vacancies/upload/' , views.upload_vacancy, name = 'upload_vacancy'),

    path('vacancies/applyVacancy/', views.apply_Vacancy, name = 'applyVacancy'),

    path('vacancies/Applied_Vacancies', views.Applied_Vacancies, name = 'Applied_Vacancies'),

    path('vacancies/<int:id>/detail/', views.vacancy_detail, name='vacancy_detail'),
    
    path('deleteVacancy/<title>', views.delete_Vacancy, name = 'deleteVacancy'),
    
    path('download/', download_file, name='download_file'),


]

#uso de archivos de multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)