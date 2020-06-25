from multiprocessing.pool import ThreadPool
from django.core.mail import EmailMessage
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from restaurant.models import UserProfile


class MailSender(models.Model):
    topic = models.CharField('Email Subject', max_length=100)
    message = models.TextField('Email text', null=True)
    date = models.DateField(default=timezone.now().date())
    time = models.TimeField(default=timezone.now().time())
    users = models.ManyToManyField(UserProfile, limit_choices_to={'Verified': True}, blank=False)
    check_send = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        if self.check_send is False:
            self.check_send = True
            self.send()
            self.save()
        return str(self.topic)

    def send(self):
        message = render_to_string('accounts/mail_message.html', {
            'message': self.message,
            'date': self.date,
            'time': self.time
        })
        mail_subject = self.topic
        mount = self.users.count()
        pool_executor = ThreadPool(mount)
        result = []
        for profile in self.users.all():
            to_email = profile.user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email])
            result.append(email)

        pool_executor.map(send_mail, result)


def send_mail(email):
    email.send()

