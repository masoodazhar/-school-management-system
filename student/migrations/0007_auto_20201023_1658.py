# Generated by Django 2.2.10 on 2020-10-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20201023_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculateresults',
            name='clear_status',
        ),
        migrations.AlterField(
            model_name='calculateresults',
            name='marks',
            field=models.CharField(default='undeclared', max_length=20),
        ),
    ]
