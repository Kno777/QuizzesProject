from django.urls import path
from .views import ListQuiz

urlpatterns = [
    path('quizzes/', ListQuiz.as_view(), name=ListQuiz.name)
]
