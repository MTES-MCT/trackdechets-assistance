from django.views.generic import DetailView, TemplateView

from .models import Page


class AnswerView(TemplateView):
    template_name = "content/answer.html"


class PageView(DetailView):
    model = Page
    template_name = "content/page.html"
