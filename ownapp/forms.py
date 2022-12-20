from django import forms

DIFFICULTY_CHOOSE = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('Not Set', 'Not Set')
)

class OwnQuizzesForm(forms.Form):
    code_quiz = forms.TextInput()
    result = forms.CharField(max_length=255)
    hint = forms.TextInput(blank=True)
    solution = forms.TextInput(blank=True)
    email = forms.EmailField()
    difficulty = forms.CharField(max_length=50, choices=DIFFICULTY_CHOOSE)

class OwnExercisesForm(forms.Form):
    title = forms.CharField(max_length=350)
    description = forms.TextInput()
    result = forms.CharField(max_length=300)
    difficulty = forms.CharField(max_length=50, choices=DIFFICULTY_CHOOSE)
    code_for_example = forms.TextInput()
    email = forms.EmailField()