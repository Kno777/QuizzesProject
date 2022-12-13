from django.contrib import admin
from .models import Exercises, Exercises_Users_Answers


@admin.register(Exercises)
class AdminExercises(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'admin_correct_answer', 'id',] 
    list_filter = ['title', 'difficulty', 'id'] 
    search_fields = ['title', 'difficulty', 'id']

@admin.register(Exercises_Users_Answers)
class AdminExercises_Users_Answers(admin.ModelAdmin):
    list_display = ['user_id', 'exercise_id', 'answer', 'id',] 
    list_filter = ['user_id', 'exercise_id', 'id'] 
    search_fields = ['user_id', 'exercise_id', 'answer']
