from django.urls import path, re_path
from . import views

app_name = 'ownapp'

urlpatterns = [
    path('quiz/own/list/', views.own_list, name='own_list'),
]
