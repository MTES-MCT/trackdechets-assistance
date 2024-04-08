import pytest

from ..factories import PageFactory

pytestmark = pytest.mark.django_db


def test_pagefactory():
    page = PageFactory()
    assert page.pk
