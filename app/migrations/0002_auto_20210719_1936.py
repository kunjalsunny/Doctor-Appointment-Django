# Generated by Django 3.1.4 on 2021-07-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
