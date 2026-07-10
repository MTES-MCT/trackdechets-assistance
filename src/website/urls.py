from django.urls import path

from .views import (
    Accessibility,
    Home,
    Partners,
    UseTerms,
    LegalNotice,
    PolitiquesConfidentialites,
    home_redirect,
    nl_signup,
    stats,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("partenaires/", Partners.as_view(), name="partners"),
    path("cgu/", UseTerms.as_view(), name="tos"),
    path("mentions-legales/", LegalNotice.as_view(), name="legal_notice"),
    path("politiques-confidentialites/", PolitiquesConfidentialites.as_view(), name="politiques_confidentialites"),
    path("accessibilite/", Accessibility.as_view(), name="accessibility"),
    path("nl-signup/<str:variant>/", nl_signup, name="nl_signup"),
    path("stats/", stats, name="stats"),
    path("resources/", home_redirect),
]
