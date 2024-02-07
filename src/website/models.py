from django.core.exceptions import ValidationError
from django.db import models


class Menu:
    pass


class FaqLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.URLField(max_length=256)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.label

    class Meta:
        ordering = ["position"]
        verbose_name = "Faq Link"
        verbose_name_plural = "Faq Links"


class FaqCard(models.Model):
    title = models.CharField(max_length=256, blank=True)
    content = models.TextField(blank=True)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title or self.content[:20]

    def clean(self):
        if not self.title and not self.position:
            raise ValidationError(
                "Vous devez renseigner au moins le titre ou le contenu"
            )

    class Meta:
        verbose_name = "Faq Card"
        verbose_name_plural = "Faq Cards"
        ordering = ["position"]


class IconTypeText(models.TextChoices):
    BSDD = "Bsdd", "Bsdd"
    BSDA = "Bsda", "Bsda"
    BSFF = "Bsff", "Bsff"
    BSDASRI = "Bsdasri", "Bsdasri"
    BSVHU = "Bsvhu", "Bsvhu"
    BSPAOH = "Bspaoh", "Bspaoh"


ICON_CLASS_ARROW = "fr-fi-arrow-right-line"
ICON_CLASS_BSDD = "fr-icon-bsdd"
ICON_CLASS_BSDA = "fr-icon-bsda"
ICON_CLASS_BSFF = "fr-icon-bsff"
ICON_CLASS_BSDASRI = "fr-icon-bsdasri"
ICON_CLASS_BSVHU = "fr-icon-bsvhu"
ICON_CLASS_BSPAOH = "fr-icon-bspaoh"

ICON_MAPPING = {
    IconTypeText.BSDD.value: ICON_CLASS_BSDD,
    IconTypeText.BSDA.value: ICON_CLASS_BSDA,
    IconTypeText.BSFF.value: ICON_CLASS_BSFF,
    IconTypeText.BSDASRI.value: ICON_CLASS_BSDASRI,
    IconTypeText.BSVHU.value: ICON_CLASS_BSVHU,
    IconTypeText.BSPAOH.value: ICON_CLASS_BSPAOH,
}


class FaqCardLink(models.Model):
    card = models.ForeignKey(FaqCard, on_delete=models.CASCADE, related_name="links")
    label = models.CharField(max_length=50, default="En savoir plus")
    url = models.URLField(max_length=256)
    icon_type = models.CharField(
        max_length=100, blank=True, choices=IconTypeText.choices
    )

    def __str__(self):
        return self.label

    def icon_class(self):
        return ICON_MAPPING.get(self.icon_type, ICON_CLASS_ARROW)

    class Meta:
        verbose_name = "Faq Card Link"
        verbose_name_plural = "Faq Card Links"


class VideoLink(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=256)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["position"]
        verbose_name = "Video Link"
        verbose_name_plural = "Video Links"


class StatsDigest(models.Model):
    """Retrieved from stats app to display main numbers on home page"""

    waste_weight = models.PositiveIntegerField("Waste weight")
    bsd_count = models.PositiveIntegerField("Bsd Count")
    company_count = models.PositiveIntegerField("Company Count")
    retrieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"StatDigest-{self.retrieved_at:x}"

    class Meta:
        ordering = ("-retrieved_at",)
        verbose_name = "Stat digest"
        verbose_name_plural = "Stat digests"
