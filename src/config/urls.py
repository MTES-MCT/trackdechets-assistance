from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from content.views import AnswerView, PageView

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("martor/", include("martor.urls")),
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", AnswerView.as_view(), name="answer"),
    path("page/<uuid:pk>", PageView.as_view(), name="page"),
]
