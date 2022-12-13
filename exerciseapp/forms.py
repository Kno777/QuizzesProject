from django import forms

class SearchForm(forms.Form):
    query = forms.CharField()

class ExercisesUserAnswerForm(forms.Form):
    answer = forms.CharField()