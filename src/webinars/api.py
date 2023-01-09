from django.urls import reverse
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from .models import Webinar


class WebinarSerializer(serializers.ModelSerializer):
    ics = serializers.SerializerMethodField()

    class Meta:
        model = Webinar
        fields = ["id", "title", "scheduled_at", "visio_link", "ics"]

    def get_ics(self, obj):
        return reverse("webinar_ics", args=[obj.pk])


class Webinars(ListAPIView):
    queryset = Webinar.objects.future()
    serializer_class = WebinarSerializer
