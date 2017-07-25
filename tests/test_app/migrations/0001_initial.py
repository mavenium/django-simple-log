# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

try:
    from django.contrib.postgres.fields.jsonb import JSONField
except ImportError:
    from jsonfield import JSONField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.SIMPLE_LOG_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BadLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CustomLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='action time')),
                ('user_repr', models.CharField(blank=True, max_length=1000, verbose_name='user repr')),
                ('user_ip', models.GenericIPAddressField(null=True, verbose_name='IP address')),
                ('object_id', models.TextField(blank=True, null=True, verbose_name='object id')),
                ('object_repr', models.CharField(max_length=1000, verbose_name='object repr')),
                ('action_flag', models.PositiveSmallIntegerField(choices=[(1, 'added'), (2, 'changed'), (3, 'deleted')], verbose_name='action flag')),
                ('old', JSONField(null=True, verbose_name='old values')),
                ('new', JSONField(null=True, verbose_name='new values')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='content type')),
                ('related_logs', models.ManyToManyField(blank=True, to=settings.SIMPLE_LOG_MODEL, verbose_name='related log')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('-action_time',),
                'abstract': False,
                'verbose_name': 'log entry',
                'verbose_name_plural': 'logs entries',
            },
        ),
        migrations.CreateModel(
            name='OtherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100, verbose_name='Char field')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'other entry',
                'verbose_name_plural': 'other entries',
            },
        ),
        migrations.CreateModel(
            name='SwappableLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='action time')),
                ('user_repr', models.CharField(blank=True, max_length=1000, verbose_name='user repr')),
                ('user_ip', models.GenericIPAddressField(null=True, verbose_name='IP address')),
                ('object_id', models.TextField(blank=True, null=True, verbose_name='object id')),
                ('object_repr', models.CharField(max_length=1000, verbose_name='object repr')),
                ('action_flag', models.PositiveSmallIntegerField(choices=[(1, 'added'), (2, 'changed'), (3, 'deleted')], verbose_name='action flag')),
                ('old', JSONField(null=True, verbose_name='old values')),
                ('new', JSONField(null=True, verbose_name='new values')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='content type')),
                ('related_logs', models.ManyToManyField(blank=True, to=settings.SIMPLE_LOG_MODEL, verbose_name='related log')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('-action_time',),
                'abstract': False,
                'verbose_name': 'log entry',
                'verbose_name_plural': 'logs entries',
            },
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(blank=True, max_length=100, verbose_name='Char field')),
                ('choice_field', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'One'), (2, 'Two')], default=1, null=True, verbose_name='Choice field')),
                ('fk_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_entries_fk', to='test_app.OtherModel', verbose_name='Fk field')),
                ('m2m_field', models.ManyToManyField(blank=True, related_name='test_entries_m2m', to='test_app.OtherModel', verbose_name='M2m field')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'test entry',
                'verbose_name_plural': 'test entries',
            },
        ),
        migrations.AddField(
            model_name='othermodel',
            name='m2m_field',
            field=models.ManyToManyField(blank=True, to='test_app.TestModel'),
        ),
    ]