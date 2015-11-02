# -- coding: utf-8 --
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1564), MaxValueValidator(2015)]
    )
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.author.encode('utf-8').strip(), self.name.encode('utf-8').strip())


class BookItem(models.Model):
    book = models.ForeignKey(Book)

    def __str__(self):
        return '№{} {}'.format(self.pk, self.book.name.encode('utf-8').strip())
