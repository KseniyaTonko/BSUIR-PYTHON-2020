import six
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from accounts.forms import UserCreateForm


def signup_view(request):
    form = UserCreateForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {'form': form})
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            context = {'form': form}
            if User.objects.filter(email=email).exists():
                context["error_mail"] = "Данная почта уже зарегистрирована"
            if len(context) == 1:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False
                user.save()
                use_https = request.is_secure()
                mail_subject = 'Активация аккаунта.'
                token = account_activation_token.make_token(user)
                message = render_to_string('accounts/mail_confirm.html', {
                    'user': user,
                    'domain': '127.0.0.1:8000',
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': token,
                    'protocol': 'https' if use_https else 'http',
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request, 'accounts/verify_mail_page.html')
            return render(request, 'accounts/signup.html', context)

        context = {'form': form}
        if 'username' in form.errors.as_data():
            context["error_name"] = "Данное имя уже зарегистрировано"
        return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()


def activate_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if not user.user_profile.verified and account_activation_token.check_token(user, token):
        user.is_active = True
        user.user_profile.verified = True
        user.save()
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    return HttpResponse('Ссылка активации недействительна!')
