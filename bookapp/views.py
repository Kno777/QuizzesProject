from django.shortcuts import render, get_object_or_404
from .models import BookCategory, Books # Category, Product


def book_list(request, category_slug=None):
    category = None
    categories = BookCategory.objects.all()
    books = Books.objects.all() #filter(available=True)

    if category_slug:
        category = get_object_or_404(BookCategory, slug=category_slug)
        books = books.filter(category=category)

    return render(request,
                  'bookapp/book/list.html',
                  {'category': category,
                   'categories': categories,
                   'books': books,
                   'section':'book'})


def book_detail(request, id, slug):
    book = get_object_or_404(Books,id=id,slug=slug)

    return render(request,'bookapp/book/detail.html',{'book': book,'section':'book'})