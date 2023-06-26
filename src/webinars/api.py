from zoneinfo import ZoneInfo

from django.urls import reverse
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from .models import Webinar

local_tz = ZoneInfo("Europe/Paris")


class WebinarSerializer(serializers.ModelSerializer):
    ics = serializers.SerializerMethodField()
    scheduled_at = serializers.DateTimeField(default_timezone=local_tz)

    class Meta:
        model = Webinar
        fields = ["id", "title", "scheduled_at", "visio_link", "ics"]

    def get_ics(self, obj):
        return reverse("webinar_ics", args=[obj.pk])


class Webinars(ListAPIView):
    queryset = Webinar
    serializer_class = WebinarSerializer

    def get_queryset(self):
        return Webinar.objects.future().order_by("scheduled_at")
