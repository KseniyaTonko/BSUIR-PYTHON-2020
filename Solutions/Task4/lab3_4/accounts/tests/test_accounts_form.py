from django.test import TestCase

from accounts.forms import UserCreateForm


class TestAccountForm(TestCase):

    def test_UserCreateForm_form(self):
        form = UserCreateForm({'email': 'aaa@mail.ru', 'password1': '13066nata',
                   'password2': '13066nata', 'username': 'qweqwe', 'name': 'Qwe'})
        self.assertTrue(form.is_valid())
