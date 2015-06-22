# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('last_name', models.CharField(default='', max_length=32)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=16)),
                ('zip', models.CharField(default='', max_length=8)),
                ('headline', models.CharField(default='', max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('geninfo', models.CharField(default='', max_length=254)),
            ],
        ),
    ]
