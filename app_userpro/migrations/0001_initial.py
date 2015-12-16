# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('transcript', models.TextField(blank=True, default='')),
                ('speech', models.TextField(blank=True, default='')),
                ('feedback', models.TextField(blank=True, default='')),
            ],
        ),
    ]
