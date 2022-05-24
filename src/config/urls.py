from django.conf import settings
from django.contrib import admin
from django.urls import path

from content.views import AnswerView, PageView

urlpatterns = [
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", AnswerView.as_view(), name="answer"),
    path("page/<int:pk>", PageView.as_view(), name="page"),
]
