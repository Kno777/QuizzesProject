"""In this module, I used all classes and variables to convert JSON format"""

from rest_framework import serializers 
from .models import QuizzesPython


class QuizzesPythonSerializer(serializers.ModelSerializer): 
    class Meta:
        model = QuizzesPython
        fields = ('id', 'question', 'section','admin_correct_answer', 'code_image', 'solution', )
        read_only_fields = ('question', 'section', 'code_image', 'solve', 'admin_correct_answer', )