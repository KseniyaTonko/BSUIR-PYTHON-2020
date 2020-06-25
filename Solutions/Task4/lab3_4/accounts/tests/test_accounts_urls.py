from django.urls import reverse, resolve


class TestAccountUrls:

    def test_signup_url(self):
        path = reverse('accounts:signup')
        assert resolve(path).view_name == 'accounts:signup'

    def test_login_url(self):
        path = reverse('accounts:login')
        assert resolve(path).view_name == 'accounts:login'

    def test_logout_url(self):
        path = reverse('accounts:logout')
        assert resolve(path).view_name == 'accounts:logout'

    def test_activation_url(self):
        path = reverse('accounts:activation', kwargs={'uidb64': '123', 'token': '123'})
        assert resolve(path).view_name == 'accounts:activation'
