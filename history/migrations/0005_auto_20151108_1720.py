# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_auto_20151108_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyitem',
            name='isFinePaid',
            field=models.NullBooleanField(default=False, verbose_name=b'Is Fine Paid?'),
        ),
    ]
