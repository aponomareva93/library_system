# -- coding: utf-8 --
from django.db import models
from books.models import BookItem
from readers.models import Reader
import datetime


class HistoryItem(models.Model):
    date_taken = models.DateField(verbose_name="Дата выдачи")
    date_due = models.DateField(verbose_name="Срок возврата")
    date_returned = models.DateField(verbose_name="Дата возврата", blank=True, null=True)
    fine = models.SmallIntegerField(verbose_name="Суммарный штраф", default=0)
    daily_fine = models.SmallIntegerField("Ежедневный штраф (в рублях)", default=1)
    is_fine_paid = models.NullBooleanField(verbose_name="Штраф оплачен?", default=False)
    book_item = models.ForeignKey(BookItem)
    reader = models.ForeignKey(Reader)

    def __str__(self):
        return '{}: №{} {} - {}'.format(
            self.reader.username, self.book_item.pk,
            self.book_item.book.author,
            self.book_item.book.name
        )

    def calculate_fine(self):
        if self.date_due < datetime.date.today():
            if not self.date_returned:
                return str(self.daily_fine * (datetime.date.today() - self.date_due)).split()[0]
            elif self.date_returned > self.date_due:
                return str(self.daily_fine * (self.date_returned - self.date_due)).split()[0]
            else:
                return 0
        else:
            return 0

    def save(self, *args, **kwargs):
        self.fine = self.calculate_fine()
        super(HistoryItem, self).save(*args, **kwargs)
