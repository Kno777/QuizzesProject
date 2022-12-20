from django.contrib import admin
from .models import OwnQuizzesOfUsersPython, OwnExerciesesOfUsers


@admin.register(OwnQuizzesOfUsersPython)
class AdminOwnQuizzesPython(admin.ModelAdmin):
    list_display = ['result', 'difficulty', 'email', 'id',] 
    list_filter = ['difficulty', 'id'] 
    search_fields = ['solution', 'email']

@admin.register(OwnExerciesesOfUsers)
class AdminOwnExercises(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'result', 'id',] 
    list_filter = ['title', 'difficulty', 'id'] 
    search_fields = ['title', 'difficulty', 'id']
