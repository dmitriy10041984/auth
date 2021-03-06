# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(db_index=True, max_length=255, verbose_name='Login')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Avatar image')),
                ('firstname', models.CharField(blank=True, max_length=40, null=True, verbose_name='First name')),
                ('lastname', models.CharField(blank=True, max_length=40, null=True, verbose_name='Last name')),
                ('middlename', models.CharField(blank=True, max_length=40, null=True, verbose_name='Middle name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Registration date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is superuser')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фотография риелтора')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Персональное видео автора')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Об авторе')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователь',
                'db_table': 'extuser',
            },
        ),
    ]
