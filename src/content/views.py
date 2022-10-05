from django.http import Http404
from django.views.generic import DetailView, TemplateView, FormView

from .models import Page
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.conf import settings


class AnswerView(TemplateView):
    template_name = "content/answer.html"

    def get_context_data(self, **kwargs):
        home_page = Page.objects.order_by("level").first()
        if not home_page:
            raise Http404
        return super().get_context_data(**kwargs, home_page_pk=home_page.pk)


class PageView(DetailView):
    model = Page
    template_name = "content/page.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = ContactForm()
        ctx.update({"form": form})
        return ctx


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("message_sent")
    template_name = "content/contact.html"

    def form_valid(self, form):
        res = super().form_valid(form)
        data = form.cleaned_data

        body = [
            f"Nom: {data['name']}",
            f"Entreprise: {data['company']}",
            f"Siret: {data['siret']}",
            f"Message: {data['body']}",
        ]
        message = EmailMessage(
            subject=form.cleaned_data["subject"],
            body="\n\n".join(body),
            from_email=form.cleaned_data["email"],
            to=[settings.MESSAGE_RECIPIENT],
        )

        if self.request.FILES:

            for uploaded_file in self.request.FILES.getlist("files"):

                message.attach(
                    uploaded_file.name, uploaded_file.read(), uploaded_file.content_type
                )

        message.send()

        return res


class MessageSentView(TemplateView):
    template_name = "content/message_sent.html"
