from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import download_file

urlpatterns = [

    path('', views.homepage, name='home'),

    path('register/', views.register, name='register'),

    path('register_company/', views.register_company, name='register_company'),

    path('register_employee/', views.register_employee, name='register_employee'),

    path('login/', views.login, name='login'),

    path('dashboard_employee/', views.dashboard_employee, name='dashboard_employee'),

    path('dashboard_company/', views.dashboard_company, name='dashboard_company'),

    path('matched_vacancies/', views.matched_vacancies, name='matched_vacancies'),

    path('logout/', views.logout, name='logout'),

    path('vacanciescompany/' , views.vacancy_listcompany, name= 'vacancy_listcompany'),

    path('vacanciesemployee/' , views.vacancy_listemployee, name= 'vacancy_listemployee'),
    

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