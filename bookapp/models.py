from django.db import models
from django.urls import reverse


class BookCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-name', )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bookapp:book_list_by_category',
                       args=[self.slug])

class Books(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    decription = models.TextField()
    author = models.CharField(max_length=200)
    publish = models.DateTimeField(auto_now_add=True)
    download = models.FileField(blank=True, null=True, upload_to='books')
    book_image = models.ImageField(upload_to='books/books_img/%Y/%m/%d',blank=True)

    class Meta:
        ordering = ('publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookapp:book_detail',
                       args=[self.id, self.slug])