# Generated by Django 3.0.5 on 2020-05-21 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0029_auto_20200521_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 20, 7, 28, 907010), help_text='Начало работы'),
        ),
    ]
