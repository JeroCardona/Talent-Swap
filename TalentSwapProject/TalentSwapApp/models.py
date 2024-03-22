from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    information = models.TextField()

class Employee(User):
    # Agrega el campo related_name para evitar conflictos con los grupos y permisos de usuario
    groupsemployee = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    employee_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    interests = models.TextField()
    employee_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.employee_name 

class Company(User):
    # Agrega el campo related_name para evitar conflictos con los grupos y permisos de usuario
    groupscompany = models.ManyToManyField(
        'auth.Group',
        related_name='company_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    company_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='company_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.company_name

class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='vacancies/')
    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.title
    
class applyVacancy(models.Model):
    title = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    profession = models.CharField(max_length = 300)  

    def __str__(self):
        return 'applyVacancy {} by {}'.format(self.title, self.name, self.profession)
    
class Comment(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)