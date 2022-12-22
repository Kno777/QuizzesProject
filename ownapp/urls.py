from django.urls import path, re_path
from . import views

app_name = 'ownapp'

urlpatterns = [
    path('quiz/own/list/', views.own_list, name='own_list'),
    path('quiz/own/quizzes/', views.own_quiz, name='own_quiz'),
    path('quiz/own/exercises/', views.own_exercise, name='own_exercise')
]
