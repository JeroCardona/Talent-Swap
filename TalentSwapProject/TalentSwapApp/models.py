from django.db import models

# Create your models here.

class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    document = models.FileField(upload_to='vacancies/')

    def __str__(self) -> str:
        return self.title
    
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
    