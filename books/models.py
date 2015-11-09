# -- coding: utf-8 --
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField("Название", max_length=100)
    author = models.CharField("Автор(ы)", max_length=200)
    year = models.PositiveSmallIntegerField(
        "Год издания", validators=[MinValueValidator(1564), MaxValueValidator(2015)]
    )
    publisher = models.CharField("Издательство", max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.author,
                                self.name)


class BookItem(models.Model):
    book = models.ForeignKey(Book, verbose_name="Книга")

    def __str__(self):
        return '№{} {}'.format(self.pk, self.book.name)
