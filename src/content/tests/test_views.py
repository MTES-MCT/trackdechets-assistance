import pytest
from django_hosts.resolvers import reverse

from ..factories import PageFactory

pytestmark = pytest.mark.django_db


def test_contact(anon_client):
    page = PageFactory()
    anon_client.cookies["assistance_page"] = str(page.pk)
    url = reverse("contact", host="assistance_hosts")

    res = anon_client.get(url, HTTP_HOST="assistance.track.test")
    assert res.status_code == 200
    assert "Contactez-nous" in res.content.decode()
