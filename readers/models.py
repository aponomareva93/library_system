# -- coding: utf-8 --
from django.db import models
from django.contrib.auth.models import User


class Reader(User):
    phoneNumber = models.CharField(null=True, verbose_name="Phone number", max_length=16)
    address = models.CharField(null=True, max_length=50)

    def __str__(self):
        return '№{} {} {}: {}'.format(self.pk, self.first_name, self.last_name, self.username)