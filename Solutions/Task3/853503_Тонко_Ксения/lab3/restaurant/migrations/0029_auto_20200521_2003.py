# Generated by Django 3.0.5 on 2020-05-21 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0028_auto_20200521_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 20, 3, 24, 895425), help_text='Начало работы'),
        ),
    ]
