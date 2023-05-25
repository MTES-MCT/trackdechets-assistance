from zoneinfo import ZoneInfo

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django_ical.views import ICalFeed

from .models import Webinar

local_tz = ZoneInfo("Europe/Paris")


class WebinarList(ListView):
    queryset = Webinar
    template_name = "webinars/list.html"
    context_object_name = "webinars"

    def get_queryset(self):
        return Webinar.objects.future().order_by("scheduled_at")

    def get_past_webinars(self):
        return Webinar.objects.past()

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(
            object_list=object_list,
            **kwargs,
            past_webinars=self.get_past_webinars(),
            current_site=settings.WEBINARS_DOMAIN,
        )


class WebinarDetail(DetailView):
    model = Webinar
    template_name = "webinars/detail.html"
    context_object_name = "webinar"


def event(request, pk):
    event = Webinar.objects.get(pk=pk)
    response = HttpResponse(event.as_ics(), content_type="text/calendar; charset=utf-8")
    response["Content-Disposition"] = f"attachment; filename={event.slug}.ics"
    return response


class WebinarFeed(ICalFeed):
    product_id = "-//example.com//Example//EN"
    timezone = "Europe/Paris"
    file_name = "trackdechets_webinars.ics"

    def items(self):
        return Webinar.objects.visible()

    def item_guid(self, item):
        return item.title

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.title

    def item_start_datetime(self, item):
        return item.scheduled_at

    def item_link(self, item):
        return reverse("webinar_detail", args=[item.pk])
