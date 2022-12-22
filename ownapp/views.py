from django.shortcuts import render
from .models import OwnExerciesesOfUsers, OwnQuizzesOfUsersPython
from .forms import OwnExercisesForm, OwnQuizzesForm
from django.contrib.auth.decorators import login_required

def own_list(request):
    return render(request, 'ownapp/own/list.html', {'section':'own'})

@login_required
def own_quiz(request):
    form = OwnQuizzesForm()
    sent = False
    if request.method == 'POST':
        form = OwnQuizzesForm(request.POST)
        print(form)
        if form.is_valid():
            code_quiz = form.cleaned_data['code_quiz']
            result = form.cleaned_data['result']
            hint = form.cleaned_data['hint']
            solution = form.cleaned_data['solution']
            email = form.cleaned_data['email']
            difficulty = form.cleaned_data['difficulty']
            

            OwnQuizzesOfUsersPython.objects.create(
                code_quiz=code_quiz,
                result=result,
                hint=hint,
                solution=solution,
                email=email,
                difficulty=difficulty
            )
            sent = True
    else:
        form = OwnQuizzesForm()

    return render(request, 'ownapp/own/quizzes.html', {'form':form, 'section':'own', 'sent':sent})    

@login_required
def own_exercise(request):
    form = OwnExercisesForm()
    sent = False
    if request.method == 'POST':
        form = OwnExercisesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            result = form.cleaned_data['result']
            code_for_example = form.cleaned_data['code_for_example']
            email = form.cleaned_data['email']
            difficulty = form.cleaned_data['difficulty']

            OwnExerciesesOfUsers.objects.create(
                title=title,
                description=description,
                result=result,
                code_for_example=code_for_example,
                email=email,
                difficulty=difficulty
            )

            sent = True
    else:
        form = OwnExercisesForm()
    
    return render(request, 'ownapp/own/exercises.html', {'form':form, 'section':'own', 'sent':sent})
