# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_auto_20170322_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='user_rec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
