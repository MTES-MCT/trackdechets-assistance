import httpx
from django.core.management.base import BaseCommand

from ...models import StatsDigest

DIGEST_URL = "https://statistiques.trackdechets.beta.gouv.fr/stats/digest/"


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = httpx.get(DIGEST_URL, follow_redirects=True, timeout=10)
        values = response.json()
        StatsDigest.objects.create(
            waste_weight=values.get("total_quantity_processed"),
            bsd_count=values.get("total_bsdd_created"),
            company_count=values.get("total_companies"),
        )
