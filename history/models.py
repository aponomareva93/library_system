# -- coding: utf-8 --
from django.db import models
import datetime
from books.models import BookItem
from readers.models import Reader


class HistoryItem(models.Model):
    dateTaken = models.DateField(verbose_name="Date Taken", null=True)
    dateDue = models.DateField(verbose_name="Date Due", null=True)
    dateReturned = models.DateField(verbose_name="Date Returned", blank=True)
    fine = models.SmallIntegerField(default=0)
    isFinePaid = models.NullBooleanField(verbose_name="Is Fine Paid?", default=True)
    bookItem = models.ForeignKey(BookItem)
    reader = models.ForeignKey(Reader)

    def __str__(self):
        return '№{} {}'.format(self.bookItem.pk, self.bookItem.book.name)