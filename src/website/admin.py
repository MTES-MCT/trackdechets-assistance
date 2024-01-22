from django.contrib import admin

from .models import FaqCard, FaqCardLink, FaqLink, StatsDigest, VideoLink


@admin.register(FaqLink)
class FaqLinkAdmin(admin.ModelAdmin):
    list_display = ["label", "url", "position"]


@admin.register(StatsDigest)
class StatsDigestAdmin(admin.ModelAdmin):
    list_display = ["pk", "retrieved_at"]


@admin.register(VideoLink)
class VideoLinkAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "position"]


class FaqCardLinkInline(admin.StackedInline):
    model = FaqCardLink


@admin.register(FaqCard)
class FaqCardAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "content"]
    inlines = [FaqCardLinkInline]
