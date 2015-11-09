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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_taken', models.DateField(verbose_name='Дата выдачи')),
                ('date_due', models.DateField(verbose_name='Срок возврата')),
                ('date_returned', models.DateField(blank=True, verbose_name='Дата возврата', null=True)),
                ('fine', models.SmallIntegerField(verbose_name='Суммарный штраф', default=0)),
                ('daily_fine', models.SmallIntegerField(verbose_name='Ежедневный штраф (в рублях)', default=1)),
                ('is_fine_paid', models.NullBooleanField(verbose_name='Штраф оплачен?', default=False)),
                ('book_item', models.ForeignKey(to='books.BookItem')),
            ],
        ),
    ]
