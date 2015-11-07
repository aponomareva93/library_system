# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0001_initial'),
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyitem',
            name='reader',
            field=models.ForeignKey(to='readers.Reader'),
        ),
    ]
