# Generated by Django 3.0.5 on 2020-06-24 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200624_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsender',
            name='date',
            field=models.DateField(default=datetime.date(2020, 6, 24)),
        ),
        migrations.AlterField(
            model_name='mailsender',
            name='time',
            field=models.TimeField(default=datetime.time(17, 2, 5, 132004)),
        ),
    ]