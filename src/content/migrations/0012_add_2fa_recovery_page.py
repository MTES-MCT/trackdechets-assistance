from django.db import migrations

TEXT = """Vous avez activé la double authentification sur votre compte et vous n'avez plus accès à votre application d'authentification (téléphone perdu, application supprimée, etc.) ?

**1. Essayez d'abord vos codes de récupération :** Lors de l'activation de la double authentification, des codes de récupération à usage unique vous ont été fournis. Depuis l'écran de connexion, cliquez sur "Je n'ai pas accès à l'application" et saisissez l'un de ces codes pour récupérer l'accès à votre compte.

**2. Vous n'avez plus vos codes de récupération ?** Si vous n'avez plus accès à votre application d'authentification et que vous n'avez pas conservé vos codes de récupération, il vous est possible de faire une demande de récupération manuelle auprès de notre équipe support.

⚠️ **Cette procédure est exceptionnelle et encadrée. Elle implique un délai incompressible de 48 heures avant toute réinitialisation, ainsi qu'une notification aux membres administrateurs de votre établissement.**"""

PAGE_TITLE = "Je n'ai plus accès à mon application d'authentification"
PARENT_TITLE = "Connexion / Mot de passe"


def add_page(apps, schema_editor):
    # Import the real model to benefit from MPTT's tree management
    from content.models import Page

    parent = Page.objects.filter(title=PARENT_TITLE).first()
    if parent is None:
        return

    if Page.objects.filter(title=PAGE_TITLE).exists():
        return

    Page.objects.create(
        title=PAGE_TITLE,
        text=TEXT,
        parent=parent,
        display_contact_form="CLOSED",
    )


def remove_page(apps, schema_editor):
    from content.models import Page

    Page.objects.filter(title=PAGE_TITLE).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0011_message_bsds"),
    ]

    operations = [
        migrations.RunPython(add_page, remove_page),
    ]
