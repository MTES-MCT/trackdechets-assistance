import dns.resolver
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from multiupload.fields import MultiFileField

from .fields import MathCaptchaField


class ValidableMultiFileField(MultiFileField):
    def run_validators(self, value):
        value = value or []

        for item in value:
            super().run_validators(item)


class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", min_length=3, max_length=100)
    email = forms.EmailField(label="Email")
    email_confirm = forms.EmailField(
        label="Email pour vérification",
        help_text="Vérifiez bien votre email, en cas d'erreur nous ne pourrons vous répondre",
    )
    bsds = forms.CharField(
        label="Numéro(s) de Bordereau(x) concerné(s)",
        required=False,
        widget=forms.Textarea(attrs={"cols": "40", "rows": "2"}),
        min_length=8,
        max_length=300,
    )
    siret = forms.CharField(
        label="SIRET (ou nº TVA intracomm. pour les entreprises étrangères)",
        required=False,
    )
    subject = forms.CharField(label="Objet", min_length=3, max_length=100)
    body = forms.CharField(label="Question", widget=forms.Textarea(), min_length=20, max_length=3000)

    files = ValidableMultiFileField(
        label="Fichier(s)",
        required=False,
        min_num=0,
        max_num=5,
        max_file_size=1024 * 1024 * 2.5,
        validators=[FileExtensionValidator(["pdf", "png", "jpg", "jpeg", "doc", "docx", "xls", "xlsx"])],
    )

    captcha = MathCaptchaField(label="Anti robots")

    def verify_domain(self, email):
        if not email or "@" not in email:
            return False
        domain = email.split("@")[1]
        try:
            dns.resolver.resolve(domain, "MX")
        except (dns.resolver.NXDOMAIN, dns.resolver.LifetimeTimeout):
            return False
        except dns.resolver.NoNameservers:
            return True
        return True

    def clean(self):
        super().clean()
        if not self.is_valid():
            return self.cleaned_data

        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data.get("email_confirm")

        if email != email_confirm:
            self.add_error("email_confirm", ValidationError("Les emails ne correspondent pas"))
        else:
            is_domain_valid = self.verify_domain(email)
            if not is_domain_valid:
                self.add_error("email", ValidationError("Votre email semble invalide, le nom de domaine n'existe pas"))
        return self.cleaned_data
