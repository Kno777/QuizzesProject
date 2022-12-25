from django.contrib import admin
from .models import BookCategory, Books

admin.site.register(Books)
admin.site.register(BookCategory)

