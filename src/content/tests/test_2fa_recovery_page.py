import pytest
from django_hosts.resolvers import reverse

from ..factories import PageFactory
from ..models import Page

pytestmark = pytest.mark.django_db


@pytest.fixture
def connexion_tree():
    """Crée l'arbre Connexion / Mot de passe avec ses 3 enfants."""
    parent = PageFactory(title="Connexion / Mot de passe")
    PageFactory(title="Mon mot de passe ne fonctionne pas", parent=parent)
    PageFactory(title="E-mail d'activation / e-mail de nouveau mot de passe non reçu", parent=parent)
    child = PageFactory(
        title="Je n'ai plus accès à mon application d'authentification",
        text=(
            "Vous avez activé la double authentification sur votre compte"
            " et vous n'avez plus accès à votre application d'authentification"
            " (téléphone perdu, application supprimée, etc.) ?\n\n"
            "**1. Essayez d'abord vos codes de récupération :**"
            " Lors de l'activation de la double authentification,"
            " des codes de récupération à usage unique vous ont été fournis.\n\n"
            "**2. Vous n'avez plus vos codes de récupération ?**"
            " il vous est possible de faire une demande de récupération manuelle"
            " auprès de notre équipe support.\n\n"
            "⚠️ **Cette procédure est exceptionnelle et encadrée.**"
        ),
        parent=parent,
        display_contact_form=Page.ContactFormOptions.CLOSED,
    )
    return {"parent": parent, "child": child}


def test_new_entry_exists_under_connexion(connexion_tree):
    """La nouvelle entrée est bien présente dans Connexion / Mot de passe."""
    parent = connexion_tree["parent"]
    children_titles = list(parent.get_children().values_list("title", flat=True))

    assert "Je n'ai plus accès à mon application d'authentification" in children_titles


def test_new_entry_is_third_child(connexion_tree):
    """La nouvelle entrée est positionnée après les deux entrées existantes."""
    parent = connexion_tree["parent"]
    children = list(parent.get_children().values_list("title", flat=True))

    assert children.index("Je n'ai plus accès à mon application d'authentification") == 2


def test_new_entry_page_renders(anon_client, connexion_tree):
    """La page s'affiche correctement avec le bon titre."""
    child = connexion_tree["child"]
    url = reverse("page", args=[child.pk], host="assistance_hosts")

    res = anon_client.get(url, HTTP_HOST="assistance.track.test")

    assert res.status_code == 200
    assert "Je n" in res.content.decode() and "ai plus acc" in res.content.decode()


def test_new_entry_shows_nous_contacter_button(anon_client, connexion_tree):
    """Le bouton Nous contacter est affiché (formulaire en mode CLOSED)."""
    child = connexion_tree["child"]
    url = reverse("page", args=[child.pk], host="assistance_hosts")

    res = anon_client.get(url, HTTP_HOST="assistance.track.test")

    assert res.status_code == 200
    assert "Nous contacter" in res.content.decode()


def test_new_entry_shows_retour_button(anon_client, connexion_tree):
    """Le bouton Retour est affiché car la page a un parent."""
    child = connexion_tree["child"]
    url = reverse("page", args=[child.pk], host="assistance_hosts")

    res = anon_client.get(url, HTTP_HOST="assistance.track.test")

    assert res.status_code == 200
    assert "Retour" in res.content.decode()


def test_nous_contacter_loads_contact_form(anon_client, connexion_tree):
    """Cliquer sur Nous contacter redirige vers le formulaire de contact."""
    child = connexion_tree["child"]
    url = reverse("contact", host="assistance_hosts")

    anon_client.cookies["assistance_page"] = str(child.pk)
    res = anon_client.get(url, HTTP_HOST="assistance.track.test")

    assert res.status_code == 200
    assert "Contactez-nous" in res.content.decode()
