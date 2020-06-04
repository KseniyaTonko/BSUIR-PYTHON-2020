from django.contrib import admin
from restaurant.models import Dish, Cook, Event, Stock, Contact


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'position', 'date', 'display_dishes')
    fields = ['photo', ('first_name', 'last_name'), ('position', 'date'), 'dishes']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('section', 'price')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'text', 'date')
    fields = ['photo', 'title', 'text', 'date']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'start_date', 'finish_date')
    fields = ['name', 'info', ('start_date', 'finish_date')]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'number', 'email', 'position')
    fields = ['last_name', 'first_name', 'number', 'email', 'position']

