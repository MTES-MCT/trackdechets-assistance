# from adminsortable2.admin import SortableAdminMixin
# from django.contrib import admin
#
# from .models import Link, Page
#
#
# class LinkInline(admin.TabularInline):
#     model = Link
#     fk_name = "page"
#
#
# @admin.register(Page)
# class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ["title", "linked_pages"]
#     inlines = [
#         LinkInline,
#     ]
#
#     def get_queryset(self, request):
#         queryset = super(PageAdmin, self).get_queryset(request)
#         queryset = queryset.prefetch_related("links__page")
#         return queryset
#
#     def linked_pages(self, obj):
#         return ", ".join([link.page.title for link in obj.links.select_related("page")])
#
#     linked_pages.short_description = "Linked pages"


from django.contrib import admin
from django.db import models
from grappelli.forms import GrappelliSortableHiddenMixin
from martor.widgets import AdminMartorWidget
from mptt.admin import DraggableMPTTAdmin

from .models import Link, Page


class LinkInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Link
    fk_name = "page"
    sortable_field_name = "position"


@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "indented_title", "title", "linked_pages"]
    inlines = [
        LinkInline,
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
