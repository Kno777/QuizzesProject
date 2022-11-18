from django.urls import path
from . import views

app_name = 'quizzesapp'

urlpatterns = [
    path('quiz/', views.quiz_list, name='quiz_list'),
    #path('quiz/', views.PostListView.as_view(), name='quiz_list'),
    path('quiz/<int:id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/share/', views.quiz_share, name='quiz_share'),
]
