# Generated by Django 2.0 on 2017-12-17 19:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import simple_log.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='OtherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100, verbose_name='Char field')),
                ('date_field', models.DateField(blank=True, null=True, verbose_name='Date field')),
                ('date_time_field', models.DateTimeField(blank=True, null=True, verbose_name='Date time field')),
                ('time_field', models.TimeField(blank=True, null=True, verbose_name='Time field')),
            ],
            options={
                'verbose_name': 'other entry',
                'verbose_name_plural': 'other entries',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100, verbose_name='Char field')),
            ],
            options={
                'verbose_name': 'related entry',
                'verbose_name_plural': 'related entries',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='SwappableLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='action time')),
                ('user_repr', models.TextField(blank=True, verbose_name='user repr')),
                ('user_ip', models.GenericIPAddressField(null=True, verbose_name='IP address')),
                ('object_id', models.TextField(blank=True, null=True, verbose_name='object id')),
                ('object_repr', models.TextField(blank=True, verbose_name='object repr')),
                ('old', simple_log.fields.SimpleJSONField(null=True, verbose_name='old values')),
                ('new', simple_log.fields.SimpleJSONField(null=True, verbose_name='new values')),
                ('change_message', models.TextField(blank=True, verbose_name='change message')),
                ('action_flag', models.PositiveSmallIntegerField(choices=[(1, 'added'), (2, 'changed'), (3, 'deleted')], verbose_name='action flag')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='content type')),
                ('related_logs', simple_log.fields.SimpleManyToManyField(blank=True, related_name='related_logs_rel_+', to='self', verbose_name='related log')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'log entry',
                'verbose_name_plural': 'logs entries',
                'ordering': ('-action_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(blank=True, max_length=100, verbose_name='Char field')),
                ('choice_field', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'One'), (2, 'Two')], default=1, null=True, verbose_name='Choice field')),
                ('fk_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_entries_fk', to='test_app.OtherModel', verbose_name='Fk field')),
                ('m2m_field', models.ManyToManyField(blank=True, related_name='test_entries_m2m', to='test_app.OtherModel', verbose_name='M2m field')),
            ],
            options={
                'verbose_name': 'test entry',
                'verbose_name_plural': 'test entries',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ThirdModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100, verbose_name='Char field')),
            ],
            options={
                'verbose_name': 'third entry',
                'verbose_name_plural': 'third entries',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='relatedmodel',
            name='third_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_entries', to='test_app.ThirdModel'),
        ),
        migrations.AddField(
            model_name='othermodel',
            name='m2m_field',
            field=models.ManyToManyField(blank=True, to='test_app.TestModel'),
        ),
        migrations.CreateModel(
            name='TestModelProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('test_app.testmodel',),
        ),
    ]
