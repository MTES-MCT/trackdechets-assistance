from django import forms
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
