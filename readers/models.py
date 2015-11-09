# -- coding: utf-8 --
from django.db import models
from django.contrib.auth.models import User, UserManager


class Reader(User):
    phone_number = models.CharField(blank=True, verbose_name="Номер телефона", max_length=16)
    address = models.CharField(verbose_name="Адрес", blank=True, max_length=50)
    objects = UserManager()

    def __str__(self):
        return '№{} {} {}: {}'.format(
            self.pk, self.first_name,
            self.last_name,
            self.username
        )
