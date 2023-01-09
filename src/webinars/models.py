import datetime as dt
import uuid

from django.contrib.sites.models import Site
from django.db import models
from django.db.models import ExpressionWrapper, F
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from icalendar import Calendar, Event

current_site = Site.objects.get_current()


class WebinarQuerySet(models.QuerySet):
    def visible(self):
        now = timezone.now()

        return self.annotate(
            display_date=ExpressionWrapper(
                F("scheduled_at__date") - F("display_days_before"),
                output_field=models.DateTimeField(),
            ),
        ).filter(display_date__date__lte=now.date())

    def future(self):
        now = timezone.now()
        return self.visible().filter(scheduled_at__date__gte=now.date())

    def past(self):
        now = timezone.now()
        return self.filter(scheduled_at__date__lt=now.date())


class Webinar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Titre du webinaire", max_length=120)

    scheduled_at = models.DateTimeField("Date et heure du webinaire")
    duration = models.PositiveSmallIntegerField("Durée prévue en mn", default=120)

    display_days_before = models.PositiveSmallIntegerField(
        "Afficher X jours avant", default=28
    )

    visio_link = models.URLField("Lien visio", blank=True)

    objects = WebinarQuerySet.as_manager()

    class Meta:
        verbose_name = "Webinaire"
        verbose_name_plural = "Webinaire"
        ordering = ("-scheduled_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("webinar_detail", args=[self.pk])

    @property
    def slug(self):
        return slugify(f"{self.title} {self.scheduled_at:%d %m %Y}")

    @property
    def ends_at(self):
        return self.scheduled_at + dt.timedelta(minutes=self.duration)

    @property
    def uid(self):
        site_uid = current_site.domain.split(".")
        site_uid.reverse()
        site_uid = ".".join(site_uid)
        return f"{self.id}.event.events.{site_uid}"

    @property
    def display_after(self):
        return self.scheduled_at.date() - dt.timedelta(days=self.display_days_before)

    def is_future(self):
        return self.scheduled_at.date() >= timezone.now().date()

    def as_ics(self):
        cal = Calendar()
        ical_event = Event()

        ical_event.add("summary", self.title)
        ical_event.add("dtstart", self.scheduled_at)
        ical_event.add("dtend", self.ends_at)
        ical_event.add("uid", self.uid)
        ical_event.add("dtstamp", self.ends_at)
        if self.visio_link:
            ical_event.add("url", self.visio_link)
        cal.add_component(ical_event)

        return cal.to_ical()
