from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from mptt.admin import DraggableMPTTAdmin

from .models import Page


@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin):
    list_display = [
        "tree_actions",
        "indented_title",
        "link_anchor",
        "linked_pages",
        "display_contact_form",
    ]

    list_display_links = ("indented_title",)
    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        queryset = queryset.prefetch_related("links__page")
        return queryset

    def linked_pages(self, obj):
        return ", ".join(
            [
                link.target.title
                for link in obj.links.select_related("target")
                if link.target
            ]
        )

    linked_pages.short_description = "Linked pages"
