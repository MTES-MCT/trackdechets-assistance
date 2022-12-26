from django.contrib import admin

from .models import Webinar


@admin.register(Webinar)
class WebinaAdmin(admin.ModelAdmin):
    list_display = ["title", "scheduled_at", "display_after"]
