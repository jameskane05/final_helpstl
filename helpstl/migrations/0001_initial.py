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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=32, default='')),
                ('last_name', models.CharField(max_length=32, default='')),
                ('email', models.EmailField(max_length=254, default='')),
                ('phone', models.CharField(max_length=16, default='')),
                ('zip', models.CharField(max_length=8, default='')),
                ('headline', models.CharField(max_length=200, default='')),
                ('category', models.CharField(max_length=50, default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('geninfo', models.CharField(max_length=254, default='')),
            ],
        ),
    ]
