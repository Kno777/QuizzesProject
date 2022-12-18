from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


class QuizzesPython(models.Model):
    """This is Quizzes class for only Python programming language!"""
    SECTION_CHOOSE = (
        ("List", (
                ("Difficulty: Easy", "List Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "List Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "List Difficult🟡🟡🟡"),
            )
        ),
        ("Tuple", (
                ("Difficulty: Easy", "Tuple Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "Tuple Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "Tuple Difficult🟡🟡🟡"),
            )
        ),
        ("Set", (
                ("Difficulty: Easy", "Set Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "Set Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "Set Difficult🟡🟡🟡"),
            )
        ),
        ("String", (
                ("Difficulty: Easy", "String Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "String Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "String Difficult🟡🟡🟡"),
            )
        ),
        ("Dictionary", (
                ("Difficulty: Easy", "Dict Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "Dict Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "Dict Difficult🟡🟡🟡"),
            )
        ),
        ("OOP", (
                ("Difficulty: Easy", "OOP Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "OOP Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "OOP Difficult🟡🟡🟡"),
            )
        ),
        ("Any Else Thing", (
                ("Difficulty: Easy", "Any Easy🟡⚪️⚪️"),
                ("Difficulty: Medium", "Any Medium🟡🟡⚪️"),
                ("Difficulty: Hard", "Any Difficult🟡🟡🟡"),
            )
        ),
    )

    question = models.CharField(max_length=200)
    admin_correct_answer = models.CharField(max_length=50)
    section = models.CharField(max_length=50, choices=SECTION_CHOOSE)
    solution = models.TextField(blank=True)
    hint = models.TextField(blank=True)
    code = models.TextField()

    def __str__(self):
        return self.section

    def get_absolute_url(self):
           return reverse('quizzesapp:quiz_detail', kwargs={'id':self.id})


class Quizzes_Users_Answers(models.Model):
    """Users answer for Quizzes questions!"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(QuizzesPython, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user_id} -> {self.quiz_id} -> {self.answer}"


