from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Link, Page


class LinkInline(admin.TabularInline):
    model = Link
    fk_name = "page"


@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]
    inlines = [
        LinkInline,
    ]
