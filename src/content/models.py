import uuid

import markdown
from django.db import models


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["position"]

    def __str__(self):
        return self.title

    def markdown(self):
        return markdown.markdown(self.text)


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="links")
    text = models.CharField(max_length=200)
    link = models.ForeignKey(
        Page, blank=True, null=True, on_delete=models.SET_NULL, related_name="parents"
    )

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
