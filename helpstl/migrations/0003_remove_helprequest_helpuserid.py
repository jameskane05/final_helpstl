# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpstl', '0002_helprequest_helpuserid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helprequest',
            name='helpuserid',
        ),
    ]
