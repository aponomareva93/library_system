# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTaken', models.DateField(verbose_name=b'Date Taken')),
                ('dateDue', models.DateField(verbose_name=b'Date Due')),
                ('dateReturned', models.DateField(verbose_name=b'Date Returned', blank=True)),
                ('fine', models.SmallIntegerField(default=0)),
                ('dailyFine', models.SmallIntegerField(default=1, verbose_name=b'Daily Fine (in rubles)')),
                ('isFinePaid', models.NullBooleanField(default=True, verbose_name=b'Is Fine Paid?')),
                ('bookItem', models.ForeignKey(to='books.BookItem')),
            ],
        ),
    ]
