# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=100)),
                ('author', models.CharField(verbose_name='Автор(ы)', max_length=200)),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год издания', validators=[django.core.validators.MinValueValidator(1564), django.core.validators.MaxValueValidator(2015)])),
                ('publisher', models.CharField(verbose_name='Издательство', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('book', models.ForeignKey(verbose_name='Книга', to='books.Book')),
            ],
        ),
    ]
