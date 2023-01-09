from rest_framework import serializers
from rest_framework.generics import ListAPIView

from .models import Webinar


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ["id", "title", "scheduled_at", "visio_link"]


class Webinars(ListAPIView):
    queryset = Webinar.objects.future()
    serializer_class = WebinarSerializer
