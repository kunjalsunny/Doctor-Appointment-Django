# Generated by Django 3.1.4 on 2021-07-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210719_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='presciption',
            field=models.CharField(default='Write here', max_length=100),
        ),
    ]
