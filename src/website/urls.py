from django.urls import path

from .views import Accessibility, Home, Partners, UseTerms, nl_signup

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("partenaires/", Partners.as_view(), name="partners"),
    path("cgu/", UseTerms.as_view(), name="use_terms"),
    path("accessibilite/", Accessibility.as_view(), name="accessibility"),
    path("nl-signup/<str:variant>/", nl_signup, name="nl_signup"),
]
