import uuid

import markdown
from django.db import models
from martor.models import MartorField
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    text = MartorField(blank=True)

    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title

    def markdown(self):
        return markdown.markdown(self.text)


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="links")
    text = models.CharField(max_length=200)
    target = models.ForeignKey(
        Page, blank=True, null=True, on_delete=models.SET_NULL, related_name="parents"
    )
    position = models.PositiveSmallIntegerField("Position", null=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ["position"]
