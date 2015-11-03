from django.contrib import admin
from books.models import Book, BookItem


class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'author')

admin.site.register(Book, BookAdmin)
admin.site.register(BookItem)
