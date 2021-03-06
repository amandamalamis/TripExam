# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pexam2', '0006_auto_20180821_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='joining',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='joining',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='trip_id',
        ),
        migrations.DeleteModel(
            name='Joining',
        ),
        migrations.AddField(
            model_name='join',
            name='join_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_trip', to='pexam2.Job'),
        ),
        migrations.AddField(
            model_name='join',
            name='join_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_trip', to='pexam2.User'),
        ),
    ]
