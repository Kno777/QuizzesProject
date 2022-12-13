from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Exercises(models.Model):
    
    DIFFICUlTY_CHOOSE = (
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard")
    )

    title = models.CharField(max_length=350)
    description = models.TextField()
    admin_correct_answer = models.CharField(max_length=300)
    difficulty = models.CharField(max_length=50, choices=DIFFICUlTY_CHOOSE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exerciseapp:exercise_detail', kwargs={'id':self.id})

class Exercises_Users_Answers(models.Model):
    """Users answer for Exercises problem!"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user_id} -> {self.exercise_id} -> {self.answer} -> {self.is_solved}"

