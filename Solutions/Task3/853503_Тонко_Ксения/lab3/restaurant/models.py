from datetime import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Dish(models.Model):
    photo = models.ImageField(upload_to='restaurant/images/', blank=True)
    name = models.CharField(max_length=100, help_text='Название')
    info = models.TextField(default='', help_text='Информация')
    weight = models.IntegerField(help_text='Масса')
    price = models.IntegerField(help_text='Цена')
    SECTION = (
        ('Холодные закуски', 'Холодные закуски'),
        ('Салаты', 'Салаты'),
        ('Горячие закуски', 'Горячие закуски'),
        ('Первые блюда', 'Первые блюда'),
        ('Основные блюда', 'Основные блюда'),
        ('Гарниры', 'Гарниры'),
        ('Десерты', 'Десерты'),
        ('Напитки', 'Напитки'),
    )
    section = models.CharField(max_length=30, choices=SECTION)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish-detail', args=[str(self.id)])

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class Cook(models.Model):
    photo = models.ImageField(upload_to='restaurant/images/', blank=True)
    first_name = models.CharField(max_length=20, help_text='Имя')
    last_name = models.CharField(max_length=20, help_text='Фамилия')
    position = models.CharField(max_length=40, help_text='Должность')
    dishes = models.ManyToManyField(Dish, help_text='Блюда, которые умеет готовить')
    date = models.DateField(default=datetime.strptime("20180819", '%Y%m%d').date(), help_text='Начало работы')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def display_dishes(self):
        return ', '.join([dish.name for dish in self.dishes.all()[:3]])

    display_dishes.short_description = 'Dishes'

    def get_absolute_url(self):
        return reverse('cook-detail', args=[str(self.id)])  # cook-detail


class Event(models.Model):
    photo = models.ImageField(upload_to='restaurant/images/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=30, help_text='Заголовок')
    text = models.TextField(help_text='Текст')
    date = models.DateTimeField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])


class Stock(models.Model):
    name = models.CharField(max_length=50, help_text='Название акции')
    info = models.TextField(help_text='Информация')
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock-detail', args=[str(self.id)])


class Contact(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=30, help_text='Номер телефона')
    email = models.CharField(max_length=40, help_text='Адрес электронной почты')
    position = models.CharField(max_length=40, help_text='Должность', default='')

    def __str__(self):
        return self.last_name + " " + self.first_name

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])
