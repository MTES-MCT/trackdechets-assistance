from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from mptt.admin import DraggableMPTTAdmin
from request.admin import RequestAdmin
from request.models import Request

from .models import Page

admin.site.unregister(Request)


@admin.register(Page)
class PageAdmin(DraggableMPTTAdmin):
    list_display = [
        "tree_actions",
        "indented_title",
        "display_contact_form",
    ]

    list_display_links = ("indented_title",)
    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }


@admin.register(Request)
class CustomRequestAdmin(RequestAdmin):
    list_filter = ("path",)
    search_fields = ("path",)
