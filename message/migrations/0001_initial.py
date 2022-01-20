# Generated by Django 2.2.10 on 2020-09-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject:')),
                ('mail_from', models.EmailField(max_length=254, verbose_name='from:')),
                ('mail_cc', models.CharField(default='', max_length=255, verbose_name='CC:')),
                ('mail_to', models.CharField(max_length=255, verbose_name='To:')),
                ('message', models.TextField(verbose_name='Message')),
                ('attachment', models.FileField(upload_to='messages/')),
                ('module_holder', models.CharField(max_length=50)),
                ('inserted_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'email',
            },
        ),
    ]
