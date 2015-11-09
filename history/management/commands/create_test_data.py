from datetime import date
from django.core.management.base import BaseCommand

from books.models import Book, BookItem
from readers.models import Reader
from history.models import HistoryItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = Reader.objects.get_or_create(username="Admin")[0]
        admin.set_password('Admin')
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()
        reader1 = Reader.objects.get_or_create(username="Reader1")[0]
        reader1.set_password('12345')
        reader1.save()

        book1 = Book.objects.get_or_create(name="Сердца трех", author="Дж. Лондон",
                                           year=2010, publisher="Астрель")[0]
        book_i1 = BookItem.objects.get_or_create(book=book1)[0]
        HistoryItem.objects.get_or_create(date_taken=date(2015, 11, 2), date_due=date(2015, 11, 9),
                                          book_item=book_i1, reader=reader1)
        book2 = Book.objects.get_or_create(name="По ком звонит колокол", author="Э. Хемингуэй",
                                           year=2013, publisher="Азбука")[0]
        book_i2 = BookItem.objects.get_or_create(book=book2)[0]
        HistoryItem.objects.get_or_create(date_taken=date(2015, 11, 3), date_due=date(2015, 11, 6),
                                          date_returned=date(2015, 11, 8),
                                          book_item=book_i2, reader=reader1)
        book3 = Book.objects.get_or_create(name="Дубровский", author="А.С. Пушкин",
                                           year=2008, publisher="Мир искателя")[0]
        book_i3 = BookItem.objects.get_or_create(book=book3)[0]
        HistoryItem.objects.get_or_create(date_taken=date(2015, 11, 3), date_due=date(2015, 11, 15),
                                          book_item=book_i3, reader=reader1)
        book4 = Book.objects.get_or_create(name="Толковый словарь русского языка", author="С. Ожегов",
                                           year=2015, publisher="Оникс, Мир и Образование")[0]
        book_i4 = BookItem.objects.get_or_create(book=book4)[0]
        HistoryItem.objects.get_or_create(date_taken=date(2015, 11, 1), date_due=date(2015, 11, 7),
                                          date_returned=date(2015, 11, 9),
                                          is_fine_paid=True,
                                          book_item=book_i4, reader=reader1)
