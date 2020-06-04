# Generated by Django 3.0.5 on 2020-05-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_auto_20200519_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='dishes',
            field=models.ManyToManyField(help_text='Блюда, которые умеет готовить', to='restaurant.Dish'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='info',
            field=models.TextField(default='', help_text='Информация'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(help_text='Название', max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(help_text='Цена'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(help_text='Масса'),
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=models.TextField(help_text='Текст'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text='Заголовок', max_length=30),
        ),
    ]
