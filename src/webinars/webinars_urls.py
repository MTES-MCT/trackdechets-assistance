from django.urls import path

from .api import Webinars
from .views import WebinarDetail, WebinarFeed, WebinarList, event

urlpatterns = [
    path("", WebinarList.as_view(), name="webinar_list"),
    path("<uuid:pk>", WebinarDetail.as_view(), name="webinar_detail"),
    path("feed", WebinarFeed(), name="webinar_feed"),
    path("event/<uuid:pk>", event, name="webinar_ics"),
    path("api/webinars/", Webinars.as_view(), name="api_webinars"),
]
