# Generated by Django 3.0.5 on 2020-06-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='first_name',
            field=models.CharField(db_index=True, help_text='Имя', max_length=20),
        ),
    ]
