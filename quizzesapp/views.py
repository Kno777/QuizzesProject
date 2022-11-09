from django.shortcuts import render, HttpResponse
from .models import QuizzesPython, Quizzes_Users_Answers
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
from rest_framework import pagination
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import QuizzesPythonSerializer

# def index(request):
#     quiz = QuizzesPython.objects.all()
#     us = Quizzes_Users_Answers.objects.all()
#     context = {"quiz":quiz, "us":us}
#     v = us.get(id=request.user.id)
#     ans = 'dfdfdf'
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             ans = request.POST.get('answer')
#             v.answer = ans
#             v.save()
#             return HttpResponse(ans)
#     return render(request, 'registration/index.html', context)

class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ListQuiz(generics.ListAPIView): 
    queryset = QuizzesPython.objects.all() 
    serializer_class = QuizzesPythonSerializer
    permission_classes = [AllowAny]
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['section', 'question', 'id']
    name = 'List Quiz'
