from django.conf import settings
from django.core.mail import EmailMessage
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, TemplateView

from .forms import ContactForm
from .models import Message, Page

PAGE_COOKIE_NAME = "assistance_page"


class AnswerView(TemplateView):
    template_name = "content/wrapper.html"

    def get_context_data(self, **kwargs):
        home_page = Page.objects.order_by("level").first()
        if not home_page:
            raise Http404
        return super().get_context_data(**kwargs, home_page_pk=home_page.pk)


class PageView(DetailView):
    model = Page
    template_name = "content/page.html"
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = ContactForm()
        ctx.update({"form": form})
        return ctx

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        # set cookie on each page, used by the contact form page
        response.set_cookie(PAGE_COOKIE_NAME, self.object.pk)
        return response


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("message_sent")
    template_name = "content/contact.html"

    def form_valid(self, form):
        assistance_page_title = ""
        assistance_page_id = ""
        # get cookie to know where the message is sent from
        assistance_page_cookie_id = self.request.COOKIES.get(PAGE_COOKIE_NAME, None)
        if assistance_page_cookie_id:
            assistance_page = Page.objects.filter(id=assistance_page_cookie_id).first()
            assistance_page_title = assistance_page.title
            assistance_page_id = assistance_page_cookie_id
        res = super().form_valid(form)
        data = form.cleaned_data

        username = data["name"]
        user_email = data["email"]
        company = data.get("company", "Non renseigné")
        siret = data.get("siret", "Non renseigné")
        body_content = data["body"]
        subject = data["subject"]
        body = [
            f"Nom: {username}",
            f"Entreprise: {company}",
            f"Siret: {siret}",
            f"Page d'origine: {assistance_page_title}",
            f"Message: {body_content}",
        ]
        message = EmailMessage(
            subject=subject,
            body="\n\n".join(body),
            from_email=user_email,
            to=[settings.MESSAGE_RECIPIENT],
        )

        if self.request.FILES:

            for uploaded_file in self.request.FILES.getlist("files"):
                message.attach(
                    uploaded_file.name, uploaded_file.read(), uploaded_file.content_type
                )

        message.send()
        # Save message data
        Message.objects.create(
            username=username,
            email=user_email,
            company=company,
            siret=siret,
            subject=subject,
            message=body_content,
            origin_page_title=assistance_page_title,
            origin_page_id=assistance_page_id,
            ip=self.get_client_ip(),
        )
        return res

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")
        return ip


class MessageSentView(TemplateView):
    template_name = "content/message_sent.html"
