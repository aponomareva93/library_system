from django.contrib import admin

from books.models import Book, BookItem


admin.site.register(Book)
admin.site.register(BookItem)
