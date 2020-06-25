from multiprocessing.dummy import Queue, Process

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.views import account_activation_token
from restaurant.models import *


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


def send_emails(modeladmin, request, queryset):
    messages = Queue()
    for user in queryset:
        process = Process(target=send_email, args=(user, messages))
        process.start()
        messages.get().send()
        process.join()


def send_email(user, messages):
    email_subject = 'Код активации'
    token = account_activation_token.make_token(user)
    message = render_to_string('accounts/mail_confirm.html', {
        'user': user,
        'domain': '127.0.0.1:8000',
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': token,
        'protocol': 'http',
    })
    to_email = user.email
    email = EmailMessage(
        email_subject,
        message,
        to=[to_email]
    )
    messages.put(email)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    actions = [send_emails]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
