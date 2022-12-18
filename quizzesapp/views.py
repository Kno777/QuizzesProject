from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import QuizzesPython, Quizzes_Users_Answers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm, SearchForm, UserAnswerPythonForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.contrib import messages

from random import randint
from django.contrib.auth.decorators import login_required

############################################################
############################################################
############################################################

# es 3 functioneri vra petqa mtacem te vonc darcnem async vor jisht ashxati

# def get_quiz_count():
#   count = 0
#   for quiz_id in QuizzesPython.objects.all():
#     count = quiz_id.id
#   return count

# def get_next_quiz():
#   number_of_quiz = randint(1,get_quiz_count())
#   ids_exist_list = []
#   for exist in QuizzesPython.objects.all():
#     ids_exist_list.append(exist.id)
#   try:
#     if number_of_quiz in ids_exist_list:
#       print("Number ----->", number_of_quiz)
#       print("idx list ---->", ids_exist_list)
#       return number_of_quiz
#   except QuizzesPython.DoesNotExist as e:
#     return f"Error {e}"


# def quiz_detail_sra_vra_petqa_mtacem(request, id):
#   post = get_object_or_404(QuizzesPython, id=id)
#   #ans = get_object_or_404(Quizzes_Users_Answers, id=id)  
#   ans = Quizzes_Users_Answers.objects.all()
#   check_answer = False
#   another_quiz = get_next_quiz()
#   print("Another ----->",another_quiz)

#   if request.method == 'POST':
#     form = UserAnswerPythonForm(request.POST)
#     if form.is_valid():
#       ans.answer = form.cleaned_data['answer']
#       if post.admin_correct_answer == ans.answer:
#         messages.success(request, "Your answer is right")
#         #ans.save()
#         # check user answer correct or no in HTML
#         check_answer=True
#         # added user answer in DB
#         Quizzes_Users_Answers.objects.create(quiz_id_id=id, user_id_id=request.user.id, answer=ans.answer)
#       else:
#         messages.error(request, "Your answer is wrong")
#   else:
#     form = UserAnswerPythonForm()
#   return render(request,'quizzesapp/quizzes/detail.html',
#                         {'post': post, 
#                         'form':form, 
#                         'ans':ans, 
#                         'check_answer':check_answer,
#                         'another_quiz':another_quiz
#                       })

############################################################
############################################################
############################################################



@login_required
def quiz_detail(request, id):

  #############################################
  # That logic in below take last quiz id
  #############################################
  count = 0
  another_quiz = id
  for quiz_id in QuizzesPython.objects.all():
    count = quiz_id.id
  #############################################


  #############################################
  # That logic in below get all solved id which user answered right
  #############################################
  user_answer_correct_number = []
  user_correct_answer = Quizzes_Users_Answers.objects.all().filter(user_id_id=request.user.id)
  for solved_id in user_correct_answer:
    user_answer_correct_number.append(solved_id.id)
  print(user_answer_correct_number)
  #############################################


  #############################################
  # That logic in below we append exist quiz id
  #############################################
  number_of_quiz = randint(1,count)
  ids_exist_list = []
  for exist in QuizzesPython.objects.all():
    ids_exist_list.append(exist.id)
  #############################################


  #############################################
  # That logic in below remove all quiz id which user answerd right
  #############################################
  for rm_id in user_answer_correct_number:
    if rm_id in ids_exist_list:
      ids_exist_list.remove(rm_id)
  #############################################


  #############################################
  # Check quiz id there is in the ids_exist_list list
  #############################################
  try:
    if number_of_quiz in ids_exist_list:
      another_quiz = number_of_quiz
  except QuizzesPython.DoesNotExist as e:
    return f"Error {e}"

  
  post = get_object_or_404(QuizzesPython, id=id)
  ans = Quizzes_Users_Answers.objects.all()
  check_answer = False
  
  show_me_hint = request.GET.get('hint')
  hint_check = False
  if show_me_hint == "true":
    hint_check = True

  if request.method == 'POST':
    form = UserAnswerPythonForm(request.POST)
    
    if form.is_valid():
      ans.answer = form.cleaned_data['answer']
      if post.admin_correct_answer == ans.answer:
        messages.success(request, "Your answer is right")
        #ans.save()
        # check user answer correct or no in HTML
        check_answer=True
        # added user answer in DB
        Quizzes_Users_Answers.objects.create(quiz_id_id=id, user_id_id=request.user.id, answer=ans.answer)
      else:
        messages.error(request, "Your answer is wrong")
  else:
    form = UserAnswerPythonForm()
  return render(request,'quizzesapp/quizzes/detail.html',
                        {'post': post, 
                        'form':form, 
                        'ans':ans, 
                        'check_answer':check_answer,
                        'another_quiz':another_quiz,
                        'hint_check':hint_check,
                        'section':'quiz'
                      })

@login_required
def code(request):
  return render(request, 'quizzesapp/quizzes/code.html', {'section': 'code'})

@login_required
def quiz_list(request):
  user_answer_correct_number = []
  user_correct_answer = Quizzes_Users_Answers.objects.all().filter(user_id_id=request.user.id)
  for solved_id in user_correct_answer:
    user_answer_correct_number.append(solved_id.id)

  post_list = QuizzesPython.objects.all().filter(id__in=user_answer_correct_number)

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
  
  return render(request,'quizzesapp/quizzes/list.html', {'posts': posts, 'section':'quiz'})


def quiz_share(request, quiz_id):
  # Retrieve post by id
  post = get_object_or_404(QuizzesPython, id=quiz_id) 
  sent = False

  if request.method == 'POST':
    # Form was submitted
    form = EmailPostForm(request.POST)
    if form.is_valid():
      # Form fields passed validation
      cd = form.cleaned_data
      # ... send email
      post_url = request.build_absolute_uri(post.get_absolute_url())
      subject = f"{cd['name']} recommends you read " f"{post.question}"
      message = f"Read {post.question} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
      send_mail(subject, message, 'knyazharutyunyan03@gmail.com', [cd['to']])
      sent = True
  else:
        form = EmailPostForm()
  return render(request, 'quizzesapp/quizzes/share.html', {'post': post, 'form': form, 'sent': sent})


def post_search(request):
  form = SearchForm()
  query = None
  results = []
  if 'query' in request.GET:
    form = SearchForm(request.GET)
    if form.is_valid():
      query = form.cleaned_data['query']
      results = QuizzesPython.objects.filter(question__icontains=query)
  return render(request,
                     'quizzesapp/quizzes/search.html',
                     {'form': form,
                      'query': query,
                      'results': results})

