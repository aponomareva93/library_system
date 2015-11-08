# -- coding: utf-8 --
from django.db import models
from books.models import BookItem
from readers.models import Reader
import datetime


class HistoryItem(models.Model):
    dateTaken = models.DateField(verbose_name="Date Taken")
    dateDue = models.DateField(verbose_name="Date Due")
    dateReturned = models.DateField(verbose_name="Date Returned", blank=True, null=True)
    fine = models.SmallIntegerField(default=0)
    dailyFine = models.SmallIntegerField("Daily Fine (in rubles)", default=1)
    isFinePaid = models.NullBooleanField(verbose_name="Is Fine Paid?", default=False)
    bookItem = models.ForeignKey(BookItem)
    reader = models.ForeignKey(Reader)

    def __str__(self):
        return '{}: №{} {} - {}'.format(self.reader.username, self.bookItem.pk,
                                        self.bookItem.book.author.encode('utf-8').strip(),
                                        self.bookItem.book.name.encode('utf-8').strip())

    def calculate_fine(self):
        if self.dateDue < datetime.date.today():
            if not self.dateReturned:
                return str(self.dailyFine * (datetime.date.today() - self.dateDue)).split()[0]
            else:
                return str(self.dailyFine * (self.dateReturned - self.dateDue)).split()[0]
        else:
            return 0

    def save(self, *args, **kwargs):
        self.fine = self.calculate_fine()
        super(HistoryItem, self).save(*args, **kwargs)
