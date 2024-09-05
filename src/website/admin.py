from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import BannerConfiguration, FaqCard, FaqCardLink, FaqLink, StatsDigest, VideoLink


@admin.register(BannerConfiguration)
class BannerConfigurationAdmin(SingletonModelAdmin):
    list_display = ["pk", "text"]

    def has_delete_permission(self, request, obj=None) -> bool:
        return True


@admin.register(FaqLink)
class FaqLinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["label", "url", "position"]


@admin.register(StatsDigest)
class StatsDigestAdmin(admin.ModelAdmin):
    list_display = ["pk", "retrieved_at"]


@admin.register(VideoLink)
class VideoLinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["title", "url", "position"]


class FaqCardLinkInline(admin.StackedInline):
    model = FaqCardLink


@admin.register(FaqCard)
class FaqCardAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["pk", "title", "content", "position"]
    inlines = [FaqCardLinkInline]
