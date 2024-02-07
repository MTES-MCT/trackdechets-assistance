from django.utils.translation import gettext_lazy as _
from grappelli.dashboard import Dashboard, modules

from .settings.base import ADMIN_SLUG


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(
            modules.AppList(
                "",
                collapsible=True,
                column=1,
                css_classes=("collapse closed",),
                models=("content.*",),
            )
        )
        self.children.append(
            modules.AppList(
                "",
                collapsible=True,
                column=1,
                css_classes=("collapse closed",),
                models=("webinars.*",),
            )
        )
        self.children.append(
            modules.AppList(
                "",
                collapsible=True,
                column=1,
                css_classes=("collapse closed",),
                models=("website.*",),
            )
        )
        self.children.append(
            modules.AppList(
                _("Accounts & permissions"),
                collapsible=True,
                column=1,
                css_classes=("collapse closed grp-closed",),
                exclude=("website.*", "webinars.*", "content.*"),
            )
        )

        self.children.append(
            modules.LinkList(
                _("Links"),
                column=2,
                children=[
                    {
                        "title": _("www.trackdechets.beta.gouv.fr"),
                        "url": "https://www.trackdechets.beta.gouv.fr/",
                        "external": True,
                    },
                    {
                        "title": _("Assistance"),
                        "url": "https://assistance.trackdechets.beta.gouv.fr/",
                        "external": True,
                    },
                    {
                        "title": _("FAQ Trackdéchets"),
                        "url": "https://faq.trackdechets.fr/",
                        "external": True,
                    },
                    {
                        "title": _("Sandbox"),
                        "url": "https://sandbox.trackdechets.beta.gouv.fr/login/",
                        "external": True,
                    },
                    {
                        "title": _("Prod"),
                        "url": "https://trackdechets.beta.gouv.fr/login",
                        "external": True,
                    },
                    {
                        "title": _("Support"),
                        "url": "https://trackdechets.zammad.com/",
                        "external": True,
                    },
                    {
                        "title": _("Stats"),
                        "url": f"/{ADMIN_SLUG}/request/request/overview/",
                        "external": False,
                    },
                ],
            )
        )

        self.children.append(
            modules.RecentActions(
                _("Recent actions"),
                limit=5,
                collapsible=False,
                column=3,
            )
        )
