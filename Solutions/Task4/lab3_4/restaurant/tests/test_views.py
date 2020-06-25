from django.contrib.auth.models import User, AnonymousUser
from restaurant.views import *
import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


@pytest.fixture
def user(db):
    return mixer.blend(User, username='test', password='1234')


@pytest.fixture
def cook(db):
    return mixer.blend('restaurant.Cook')


@pytest.fixture
def contact(db):
    return mixer.blend('restaurant.Contact')


def test_edit_cook_unauthenticated(factory, cook):
    path = reverse('cook_edit', kwargs={'pk': cook.id})
    request = factory.post(path)
    request.user = AnonymousUser()
    response = edit_cook(request, pk=cook.id)
    assert response.status_code == 302


def test_edit_cook_authenticated(factory, user, cook):
    path = reverse('cook_edit', kwargs={'pk': cook.id})
    request = factory.post(path)
    request.user = user
    response = edit_cook(request, pk=cook.id)
    assert response.status_code == 200


def test_delete_cook_unauthenticated(factory, cook):
    path = reverse('cook-delete', kwargs={'pk': cook.id})
    request = factory.delete(path)
    request.user = AnonymousUser()
    response = delete_cook(request, pk=cook.id)
    assert response.status_code == 302


def test_delete_cook_authenticated(factory, user, cook):
    path = reverse('cook-delete', kwargs={'pk': cook.id})
    request = factory.get(path)
    request.user = user
    response = delete_cook(request, pk=cook.id)
    assert response.status_code == 302


def test_edit_contact_unauthenticated(factory, contact):
    path = reverse('edit-contact', kwargs={'id': contact.id})
    request = factory.post(path)
    request.user = AnonymousUser()
    response = edit_contact(request, id=contact.id)
    assert response.status_code == 302


def test_edit_contact_authenticated(factory, user, contact):
    path = reverse('edit-contact', kwargs={'id': contact.id})
    request = factory.post(path)
    request.user = user
    response = edit_contact(request, id=contact.id)
    assert response.status_code == 200


def test_delete_contact_unauthenticated(factory, contact):
    path = reverse('delete-contact', kwargs={'id': contact.id})
    request = factory.delete(path)
    request.user = AnonymousUser()
    response = delete_contact(request, id=contact.id)
    assert response.status_code == 302


def test_delete_contact_authenticated(factory, user, contact):
    path = reverse('delete-contact', kwargs={'id': contact.id})
    request = factory.delete(path)
    request.user = user
    response = delete_contact(request, id=contact.id)
    assert response.status_code == 302


def test_show_contacts(factory, user):
    path = reverse('contacts')
    request = factory.post(path)
    request.user = AnonymousUser()
    response = show_contacts(request)
    assert response.status_code == 200
    path = reverse('contacts')
    request = factory.post(path)
    request.user = user
    response = show_contacts(request)
    assert response.status_code == 200


def test_update_contact_unauthenticated(factory, contact):
    path = reverse('update-contact', kwargs={'id': contact.id})
    request = factory.post(path)
    request.user = AnonymousUser()
    response = update_contact(request, id=contact.id)
    assert response.status_code == 302


def test_update_contact_authenticated(factory, user, contact):
    path = reverse('update-contact', kwargs={'id': contact.id})
    request = factory.post(path)
    request.user = user
    response = update_contact(request, id=contact.id)
    assert response.status_code == 200


def test_show_contact_unauthenticated(factory):
    path = reverse('contact')
    request = factory.post(path)
    request.user = AnonymousUser()
    response = show_contact(request)
    assert response.status_code == 200


def test_show_contact_authenticated(factory, user):
    path = reverse('contact')
    request = factory.post(path)
    request.user = user
    response = show_contact(request)
    assert response.status_code == 200


def test_add_cook_unauthenticated(factory):
    path = reverse('cook-form')
    request = factory.post(path)
    request.user = AnonymousUser()
    response = add_cook(request)
    assert response.status_code == 302


def test_add_cook_authenticated(factory, user):
    path = reverse('cook-form')
    request = factory.post(path)
    request.user = user
    response = add_cook(request)
    assert response.status_code == 200

