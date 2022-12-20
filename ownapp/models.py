from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class OwnQuizzesOfUsersPython(models.Model):
    DIFFICULTY_CHOOSE = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ('Not Set', 'Not Set')
    )

    code_quiz = models.TextField()
    result = models.CharField(max_length=255)
    hint = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    email = models.EmailField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOOSE)

    def __str__(self):
        return str(self.email)
    
class OwnExerciesesOfUsers(models.Model):
    DIFFICUlTY_CHOOSE = (
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
        ('Not Set', 'Not Set')
    )

    title = models.CharField(max_length=350)
    description = models.TextField()
    result = models.CharField(max_length=300)
    difficulty = models.CharField(max_length=50, choices=DIFFICUlTY_CHOOSE)
    code_for_example = models.TextField()
    email = models.EmailField()


    def __str__(self):
        return self.title


