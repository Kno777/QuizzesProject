from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import QuizzesPython, Quizzes_Users_Answers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def quiz_list(request):
  post_list = QuizzesPython.objects.all()

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
  
  return render(request,'quizzesapp/quizzes/list.html', {'posts': posts})

# class PostListView(ListView):
#   """
#   Alternative post list view
#   """
#   queryset = QuizzesPython.objects.all()
#   context_object_name = 'posts'
#   paginate_by = 3
#   template_name = 'quizzesapp/quizzes/list.html'

def quiz_detail(request, id):
  post = get_object_or_404(QuizzesPython, id=id)
  ans = Quizzes_Users_Answers.objects.all()
  
  return render(request,'quizzesapp/quizzes/detail.html',{'post': post})


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