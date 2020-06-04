# Generated by Django 3.0.5 on 2020-05-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200518_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('c', 'Холодные закуски'), ('s', 'Салаты'), ('h', 'Горячие закуски'), ('f', 'Первые блюда'), ('t', 'Основные блюда'), ('g', 'Гарниры'), ('d', 'Десерты')], default=None, max_length=30),
        ),
    ]
