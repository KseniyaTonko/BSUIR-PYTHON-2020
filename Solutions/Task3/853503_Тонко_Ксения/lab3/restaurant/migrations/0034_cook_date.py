# Generated by Django 3.0.5 on 2020-05-21 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0033_remove_cook_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cook',
            name='date',
            field=models.DateTimeField(default=datetime.date(2018, 8, 19), help_text='Начало работы'),
        ),
    ]
