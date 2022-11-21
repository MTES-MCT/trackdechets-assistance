import uuid

import markdown
from django.db import models
from martor.models import MartorField
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    class ContactFormOptions(models.TextChoices):
        NO = "NO", "Aucun"
        CLOSED = "CLOSED", "Fermé"
        OPEN = "OPEN", "Ouvert"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    link_anchor = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Link Anchor",
        help_text="Override Title to display as link",
    )
    text = MartorField(blank=True)

    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    display_contact_form = models.CharField(
        "Affichage du formulaire de contact",
        max_length=6,
        default=ContactFormOptions.NO,
        choices=ContactFormOptions.choices,
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title

    @property
    def anchor(self):
        return self.link_anchor or self.title

    def markdown(self):
        return markdown.markdown(self.text)

    @property
    def open_form(self):
        return self.display_contact_form == self.ContactFormOptions.OPEN

    @property
    def closed_form(self):
        return self.display_contact_form == self.ContactFormOptions.CLOSED
