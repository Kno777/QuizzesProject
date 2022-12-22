from django import forms
from .models import OwnQuizzesOfUsersPython, OwnExerciesesOfUsers

DIFFICULTY_CHOOSE = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('Not Set', 'Not Set')
)

class OwnQuizzesForm(forms.Form):
    code_quiz = forms.CharField(widget=forms.Textarea)
    result = forms.CharField(max_length=255)
    hint = forms.CharField(widget=forms.Textarea)
    solution = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOOSE)

    def clean_email(self):
        data = self.cleaned_data['email']
        if OwnQuizzesOfUsersPython.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data


class OwnExercisesForm(forms.Form):
    title = forms.CharField(max_length=350)
    description = forms.CharField(widget=forms.Textarea)
    result = forms.CharField(max_length=300)
    code_for_example = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOOSE)

    def clean_email(self):
        data = self.cleaned_data['email']
        if OwnExerciesesOfUsers.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data