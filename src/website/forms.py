from django import forms

acceptance = "J'accepte de recevoir vos e-mails et confirme avoir pris connaissance de votre politique de confidentialité et mentions légales."


class SignupForm(forms.Form):
    email = forms.EmailField()

    # def clean(self):
    #     super().clean()
    #
    #     name = self.cleaned_data.get("name")
    #     not_a_robot = self.cleaned_data.get("not_a_robot")
    #     consent = self.cleaned_data.get("consent")
    #     if name or not_a_robot:

    # def _clean(self):
    #     super().clean()
    #     already_exists = PoiCategoryName.objects.filter(
    #         category_id=self.category_pk, language=self.cleaned_data.get("language")
    #     ).exists()
    #
    #     if already_exists:
    #         raise ValidationError("A name is already defined for this language")
    #     return self.cleaned_data
