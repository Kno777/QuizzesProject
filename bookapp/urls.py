from django.urls import path
from . import views

app_name = 'bookapp'

urlpatterns = [
    path('quiz/books/', views.book_list, name='book_list'), #product_list
    path('quiz/books/<slug:category_slug>/', views.book_list,name='book_list_by_category'), #product_list_by_category
    path('quiz/books/<int:id>/<slug:slug>/', views.book_detail,name='book_detail'), #product_detail
]