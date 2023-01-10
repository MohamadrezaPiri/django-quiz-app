from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    autocomplete_fields = ['category']
    search_fields = ['title']


class AnswerInline(admin.TabularInline):
    model = models.Answer
    fields = ['answer_text', 'is_right']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz']
    list_display = ['title', 'quiz', 'date_updated']
    inlines = [AnswerInline]
    autocomplete_fields = ['quiz']


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']
