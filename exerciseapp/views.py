from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exercises, Exercises_Users_Answers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .forms import ExercisesUserAnswerForm
from django.contrib.auth.decorators import login_required


@login_required
def exercises_list(request):
  post_list = Exercises.objects.all()

  paginator = Paginator(post_list, 3) 
  page_number = request.GET.get('page', 1) 
  try:
    posts = paginator.page(page_number)
  except PageNotAnInteger:
    # If page_number is not an integer deliver the first page 
    posts = paginator.page(1)
  except EmptyPage:
    # If page_number is out of range deliver last page of results 
    posts = paginator.page(paginator.num_pages)
  
  return render(request,'exerciseapp/exercises/list.html', {'posts': posts})

@login_required
def exercise_detail(request, id):
  post = get_object_or_404(Exercises, id=id)
  ans = Exercises_Users_Answers.objects.all()
  try:
      solved = False    
      obj = Exercises_Users_Answers.objects.filter(exercise_id_id=id).get(user_id_id=request.user.id)
      solved = obj.is_solved
  except Exercises_Users_Answers.DoesNotExist as e:
      print(e)
        
  if request.method == 'POST':
      form = ExercisesUserAnswerForm(request.POST)
      if form.is_valid():
          ans.answer = form.cleaned_data['answer']
          if post.admin_correct_answer == ans.answer:
              messages.success(request, "Your answer is right")
              # added user answer in DB
              solved = True
              Exercises_Users_Answers.objects.create(exercise_id_id=id, user_id_id=request.user.id, answer=ans.answer, is_solved=True)
          else:
              messages.error(request, "Your answer is wrong")
  else:
      form = ExercisesUserAnswerForm()
  return render(request,'exerciseapp/exercises/detail.html',
                        {'post': post, 
                        'form':form, 
                        'ans':ans, 
                        'solved':solved
                      })