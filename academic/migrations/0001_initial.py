# Generated by Django 2.2.10 on 2020-09-03 23:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_number', models.IntegerField(unique=True)),
                ('fee', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('note', models.TextField(default='No Detail')),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, unique=True)),
                ('room_number', models.IntegerField(default=0, unique=True)),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=25, unique=True)),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-section_name'],
                'db_table': 'section',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=20)),
                ('subject_code', models.CharField(max_length=25, unique=True)),
                ('subject_type', models.CharField(choices=[('Optional', 'Optional'), ('Mandatory', 'Mandatory')], max_length=25)),
                ('pass_mark', models.IntegerField()),
                ('final_mark', models.IntegerField()),
                ('note', models.TextField(default='No Detail')),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True)),
                ('school_day', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Classes')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Room')),
                ('section_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Section')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Subject')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'routine',
            },
        ),
    ]