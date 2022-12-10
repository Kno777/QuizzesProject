from django.urls import path, re_path
from . import views

app_name = 'quizzesapp'

urlpatterns = [
    path('quiz/', views.quiz_list, name='quiz_list'),
    #path('quiz/', views.PostListView.as_view(), name='quiz_list'),
    path('quiz/question/<int:id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/question/<int:quiz_id>/share/', views.quiz_share, name='quiz_share'),
    path('quiz/search/', views.post_search, name='post_search'),
    path('quiz/code/', views.code, name='code'),
]
