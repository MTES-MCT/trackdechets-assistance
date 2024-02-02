import math

import sib_api_v3_sdk
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from sib_api_v3_sdk.rest import ApiException

from webinars.models import Webinar

from .forms import SignupForm
from .models import FaqCard, FaqLink, StatsDigest, VideoLink

MAX_VIDEO_LINKS = 4
HONEYPOT_FIELD_NAME = "name"


class Home(TemplateView):
    template_name = "website/home.html"

    def get_digest(self):
        return StatsDigest.objects.order_by("-retrieved_at").first()

    def get_webinars(self):
        return Webinar.objects.future().order_by("scheduled_at")

    def get_faq_cards(self):
        return FaqCard.objects.prefetch_related("links")

    def get_faq_links(self):
        return FaqLink.objects.all()

    def get_video_links(self):
        return VideoLink.objects.all()[:MAX_VIDEO_LINKS]

    def get_context_data(self, **kwargs):
        faq_cards = self.get_faq_cards()
        half = math.ceil(len(faq_cards) / 2)
        faq_cards_left = faq_cards[:half]
        faq_cards_right = faq_cards[half:]

        return super().get_context_data(
            **kwargs,
            webinars=self.get_webinars(),
            stats_digest=self.get_digest(),
            faq_links=self.get_faq_links(),
            video_links=self.get_video_links(),
            faq_cards={"left": faq_cards_left, "right": faq_cards_right},
            is_homepage=True,
        )


class UseTerms(TemplateView):
    template_name = "website/use_terms.html"


class Partners(TemplateView):
    template_name = "website/partners.html"


class Accessibility(TemplateView):
    template_name = "website/accessibility.html"


GENERAL_TYPE = "general"
TECH_TYPE = "tech"
MAPPING = {
    GENERAL_TYPE: settings.BREVO_GENERAL_NEWSLETTER_ID,
    TECH_TYPE: settings.BREVO_TECH_NEWSLETTER_ID,
}

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = settings.BREVO_API_KEY
api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))


def create_newsletter_contact(email, newsletter_type):
    list_id = MAPPING.get(newsletter_type)
    if not list_id:
        return False
    create_contact = sib_api_v3_sdk.CreateContact(email=email, list_ids=[list_id])
    try:
        api_instance.create_contact(create_contact)
        return True
    except ApiException as e:
        pass
    return False


def nl_signup(request, variant=None):
    creation_success = False
    if variant not in (GENERAL_TYPE, TECH_TYPE):
        raise Http404
    if request.method != "POST":
        raise Http404

    form = SignupForm(request.POST)
    has_honey_pot = request.POST.get(HONEYPOT_FIELD_NAME, None)
    if form.is_valid():
        if not has_honey_pot:
            creation_success = create_newsletter_contact(
                form.cleaned_data["email"], variant
            )
        return render(
            request,
            "website/_signup_form.html",
            context={
                "form": SignupForm(),
                "variant": variant,
                "success": creation_success,
            },
        )

    return render(
        request, "website/_signup_form.html", context={"form": form, "variant": variant}
    )


def home_redirect(request):
    """Redirect to home."""
    return HttpResponseRedirect(reverse("home"))


def stats(request):
    return render(
        request,
        "website/stats.html",
    )
