from django.http import Http404
from django.views.generic import DetailView, TemplateView

from .models import Page


class AnswerView(TemplateView):
    template_name = "content/answer.html"

    def get_context_data(self, **kwargs):
        home_page = Page.objects.order_by("position").first()
        if not home_page:
            raise Http404
        return super().get_context_data(**kwargs, home_page_pk=home_page.pk)


class PageView(DetailView):
    model = Page
    template_name = "content/page.html"
