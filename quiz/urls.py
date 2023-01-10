from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


urlpatterns = [
    path('quizzes/', views.QuizzesList.as_view())
]
