# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_id', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=200, blank=True)),
                ('skill_name', models.CharField(max_length=200)),
                ('member_count', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200, blank=True)),
                ('mozillian_date', models.DateTimeField(null=True, blank=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
            ],
        ),
    ]
