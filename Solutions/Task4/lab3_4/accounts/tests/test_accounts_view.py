import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from accounts.views import *


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


def test_login_view(factory):
    path = reverse('accounts:login')
    request = factory.post(path)
    request.user = AnonymousUser()
    response = login_view(request)
    assert response.status_code == 200
