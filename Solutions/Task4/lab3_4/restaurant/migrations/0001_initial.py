# Generated by Django 3.0.5 on 2020-06-22 15:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('number', models.CharField(help_text='Номер телефона', max_length=30)),
                ('email', models.CharField(help_text='Адрес электронной почты', max_length=40)),
                ('position', models.CharField(default='', help_text='Должность', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='restaurant/images/')),
                ('name', models.CharField(help_text='Название', max_length=100)),
                ('info', models.TextField(default='', help_text='Информация')),
                ('weight', models.IntegerField(help_text='Масса')),
                ('price', models.IntegerField(help_text='Цена')),
                ('section', models.CharField(choices=[('Холодные закуски', 'Холодные закуски'), ('Салаты', 'Салаты'), ('Горячие закуски', 'Горячие закуски'), ('Первые блюда', 'Первые блюда'), ('Основные блюда', 'Основные блюда'), ('Гарниры', 'Гарниры'), ('Десерты', 'Десерты'), ('Напитки', 'Напитки')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='restaurant/images/%Y/%m/%d')),
                ('title', models.CharField(help_text='Заголовок', max_length=30)),
                ('text', models.TextField(help_text='Текст')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название акции', max_length=50)),
                ('info', models.TextField(help_text='Информация')),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='restaurant/images/')),
                ('first_name', models.CharField(help_text='Имя', max_length=20)),
                ('last_name', models.CharField(help_text='Фамилия', max_length=20)),
                ('position', models.CharField(help_text='Должность', max_length=40)),
                ('date', models.DateField(default=datetime.date(2018, 8, 19), help_text='Начало работы')),
                ('dishes', models.ManyToManyField(help_text='Блюда, которые умеет готовить', to='restaurant.Dish')),
            ],
        ),
    ]
