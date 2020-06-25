from datetime import datetime

import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


@pytest.fixture
def stock(request, db):
    return mixer.blend('restaurant.Stock', finish_date=request.param)


@pytest.mark.parametrize('stock', [datetime.strptime("20100819", '%Y%m%d').date()], indirect=True)
def test_are_some_dishes(stock):
    assert stock.is_actual() is True


@pytest.mark.parametrize('stock', [datetime.strptime("20300819", '%Y%m%d').date()], indirect=True)
def test_are_some_dishes(stock):
    assert stock.is_actual() is False
