# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_historyitem_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyitem',
            name='dateReturned',
            field=models.DateField(null=True, verbose_name=b'Date Returned', blank=True),
        ),
    ]
