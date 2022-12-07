from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


class QuizzesPython(models.Model):
    """This is Quizzes class for only Python programming language!"""
    SECTION_CHOOSE = (
        ("List", (
                ("List Easy", "List Easy🟡⚪️⚪️"),
                ("List Medium", "List Medium🟡🟡⚪️"),
                ("List Difficult", "List Difficult🟡🟡🟡"),
            )
        ),
        ("Tuple", (
                ("Tuple Easy", "Tuple Easy🟡⚪️⚪️"),
                ("Tuple Medium", "Tuple Medium🟡🟡⚪️"),
                ("Tuple Difficult", "Tuple Difficult🟡🟡🟡"),
            )
        ),
        ("Set", (
                ("Set Easy", "Set Easy🟡⚪️⚪️"),
                ("Set Medium", "Set Medium🟡🟡⚪️"),
                ("Set Difficult", "Set Difficult🟡🟡🟡"),
            )
        ),
        ("String", (
                ("String Easy", "String Easy🟡⚪️⚪️"),
                ("String Medium", "String Medium🟡🟡⚪️"),
                ("String Difficult", "String Difficult🟡🟡🟡"),
            )
        ),
        ("Dictionary", (
                ("Dict Easy", "Dict Easy🟡⚪️⚪️"),
                ("Dict Medium", "Dict Medium🟡🟡⚪️"),
                ("Dict Difficult", "Dict Difficult🟡🟡🟡"),
            )
        ),
        ("OOP", (
                ("OOP Easy", "OOP Easy🟡⚪️⚪️"),
                ("OOP Medium", "OOP Medium🟡🟡⚪️"),
                ("OOP Difficult", "OOP Difficult🟡🟡🟡"),
            )
        ),
        ("Any Else Thing", (
                ("Any Easy", "Any Easy🟡⚪️⚪️"),
                ("Any Medium", "Any Medium🟡🟡⚪️"),
                ("Any Difficult", "Any Difficult🟡🟡🟡"),
            )
        ),
    )

    question = models.CharField(max_length=200)
    admin_correct_answer = models.CharField(max_length=50)
    section = models.CharField(max_length=50, choices=SECTION_CHOOSE)
    code_image = models.ImageField(default='default.jpg', upload_to='code_photo')
    solution = models.TextField(blank=True)
    hint = models.TextField(blank=True)

    def __str__(self):
        return self.section

    def save(self, *args, **kwargs):
        super(QuizzesPython, self).save(*args, **kwargs)
        img = Image.open(self.code_image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.code_image.path)

    def get_absolute_url(self):
           return reverse('quizzesapp:quiz_detail', kwargs={'id':self.id})


class Quizzes_Users_Answers(models.Model):
    """Users answer for Quizzes questions!"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(QuizzesPython, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user_id} -> {self.quiz_id} -> {self.answer}"


