# Generated by Django 4.1.1 on 2022-10-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0006_alter_page_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="display_contact_form",
            field=models.CharField(
                choices=[("NO", "Aucun"), ("CLOSED", "Fermé"), ("OPEN", "Ouvert")],
                default="NO",
                max_length=6,
                verbose_name="Affichage du formulaire de contact",
            ),
        ),
    ]
