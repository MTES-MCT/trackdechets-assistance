from django import forms

acceptance = "J'accepte de recevoir vos e-mails et confirme avoir pris connaissance de votre politique de confidentialité et mentions légales."


class SignupForm(forms.Form):
    email = forms.EmailField()
