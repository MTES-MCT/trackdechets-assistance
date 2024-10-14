import pytest
from django_hosts.resolvers import reverse

pytestmark = pytest.mark.django_db


def test_home(anon_client):
    url = reverse("home")
    res = anon_client.get(url)
    assert res.status_code == 200
    assert "Découvrez Trackdéchets" in res.content.decode()


def test_partners(anon_client):
    url = reverse("partners")
    res = anon_client.get(url)
    assert res.status_code == 200
    assert "Nos partenaires" in res.content.decode()


def test_stats(anon_client):
    url = reverse("stats")
    res = anon_client.get(url)
    assert res.status_code == 200
    assert "iframe" in res.content.decode()


def test_cgu(anon_client):
    url = reverse("tos")
    res = anon_client.get(url)
    assert res.status_code == 200
    assert "Conditions Générales d’Utilisation" in res.content.decode()


def test_accessibility(anon_client):
    url = reverse("accessibility")
    res = anon_client.get(url)
    assert res.status_code == 200
    assert "Déclaration d’accessibilité" in res.content.decode()


def test_resources(anon_client):
    res = anon_client.get("/resources")
    assert res.status_code == 301
