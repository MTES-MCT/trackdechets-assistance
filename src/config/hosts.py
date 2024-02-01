from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(r"^$", "website.urls", name="website_hosts"),
    host(r"formations", "webinars.webinars_urls", name="formations_hosts"),
    host(r"assistance", "content.assistance_urls", name="assistance_hosts"),
)
