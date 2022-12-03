from django.contrib import admin
from .models import Quizzes_Users_Answers, QuizzesPython


@admin.register(QuizzesPython)
class AdminQuizzesPython(admin.ModelAdmin):
    list_display = ['question', 'section', 'admin_correct_answer', 'id',] 
    list_filter = ['question', 'section', 'id'] 
    search_fields = ['question', 'section', 'solution']

@admin.register(Quizzes_Users_Answers)
class AdminQuizzes_Users_Answers(admin.ModelAdmin):
    list_display = ['user_id', 'quiz_id', 'answer', 'id',] 
    list_filter = ['user_id', 'quiz_id', 'id'] 
    search_fields = ['user_id', 'quiz_id', 'answer']