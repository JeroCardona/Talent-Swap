from django.db import models

# Create your models here.

class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    document = models.FileField(upload_to='vacancies/')

    def __str__(self) -> str:
        return self.title