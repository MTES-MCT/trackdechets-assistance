from django.urls import path

from .views import Accessibility, Home, Legals, Partners, tech_signup

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("partenaires/", Partners.as_view(), name="partners"),
    path("mentions-legales/", Legals.as_view(), name="legals"),
    path("accessibilite/", Accessibility.as_view(), name="accessibility"),
    path("tech-signup/<str:variant>/", tech_signup, name="tech_signup"),
]
