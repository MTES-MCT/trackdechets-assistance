from django import forms

from .fields import MathCaptchaField
from luhn import verify
from django.core.exceptions import ValidationError
from pyvat import is_vat_number_format_valid
from django.core.validators import FileExtensionValidator
from multiupload.fields import MultiFileField


class ValidableMultiFileField(MultiFileField):
    def run_validators(self, value):
        value = value or []

        for item in value:
            super().run_validators(item)


class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", min_length=3, max_length=100)
    email = forms.EmailField(label="Email")
    company = forms.CharField(
        label="Entreprise/Collectivité/Structure",
        required=False,
        min_length=3,
        max_length=100,
    )
    siret = forms.CharField(
        label="SIRET (ou nº TVA intracomm. pour les entreprises étrangères)",
        required=False,
    )
    subject = forms.CharField(label="Objet", min_length=3, max_length=100)
    body = forms.CharField(
        label="Question", widget=forms.Textarea(), min_length=20, max_length=3000
    )

    files = ValidableMultiFileField(
        label="Fichier(s)",
        required=False,
        min_num=0,
        max_num=5,
        max_file_size=1024 * 1024 * 2.5,
        validators=[
            FileExtensionValidator(
                ["pdf", "png", "jpg", "jpeg", "doc", "docx", "xls", "xlsx"]
            )
        ],
    )

    captcha = MathCaptchaField()

    def clean_siret(self):
        siret = self.cleaned_data["siret"].replace(" ", "")
        if not siret:
            return ""
        correct = True
        if len(siret) != 14:
            correct = False
        if not verify(siret):
            correct = False
        if not is_vat_number_format_valid(siret):
            correct = False
        if not correct:
            raise ValidationError(
                "Le numéro ne correspond ni à un siret ni à un numéro de TVA valide"
            )
        return siret
