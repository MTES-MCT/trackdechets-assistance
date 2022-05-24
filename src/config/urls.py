from django.contrib import admin
from django.urls import path

from content.views import AnswerView, PageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", AnswerView.as_view(), name="answer"),
    path("page/<int:pk>", PageView.as_view(), name="page"),
]
