from django.urls import path
from . import views

app_name = 'exerciseapp'

urlpatterns = [
    path('quiz/exercise/', views.test, name='test')
]