from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Link, Page


class LinkInline(admin.TabularInline):
    model = Link
    fk_name = "page"


@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["title", "linked_pages"]
    inlines = [
        LinkInline,
    ]

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        queryset = queryset.prefetch_related("links__page")
        return queryset

    def linked_pages(self, obj):
        return ", ".join([link.page.title for link in obj.links.select_related("page")])

    linked_pages.short_description = "Linked pages"
