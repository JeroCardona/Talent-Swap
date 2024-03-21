from django.contrib import admin
from .models import Vacancy, Comment, applyVacancy

# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'document', 'id')
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(applyVacancy)
class applyVacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'profession')
    list_filter = ('title', 'name', 'profession')
    search_fields = ('title', 'name', 'profession')
