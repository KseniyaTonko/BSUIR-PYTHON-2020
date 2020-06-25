from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.user_profile.save()
        except ObjectDoesNotExist:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_profile.Verified = instance.is_active
        instance.user_profile.save()


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
    first_name = models.CharField(max_length=20, help_text='Имя', db_index=True)
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
        return reverse('cook-detail', args=[str(self.id)])

    def are_some_dishes(self):
        return len(self.dishes) > 0


class Event(models.Model):
    photo = models.ImageField(upload_to='restaurant/images/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=30, help_text='Заголовок', db_index=True)
    text = models.TextField(help_text='Текст')
    date = models.DateTimeField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])


class Stock(models.Model):
    name = models.CharField(max_length=50, help_text='Название акции', db_index=True)
    info = models.TextField(help_text='Информация')
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock-detail', args=[str(self.id)])

    def is_actual(self):
        return self.finish_date < datetime.now()


class Contact(models.Model):
    first_name = models.CharField(max_length=30, default='', db_index=True)
    last_name = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=30, help_text='Номер телефона')
    email = models.CharField(max_length=40, help_text='Адрес электронной почты')
    position = models.CharField(max_length=40, help_text='Должность', default='')

    def __str__(self):
        return self.last_name + " " + self.first_name

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])
