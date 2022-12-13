from django.urls import path
from . import views

app_name = 'exerciseapp'

urlpatterns = [
    path('quiz/exercise/', views.exercises_list, name='exercises_list'),
    path('quiz/exercise/problem/<int:id>/', views.exercise_detail, name='exercise_detail'),
]