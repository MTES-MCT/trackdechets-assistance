from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(r"formations", "webinars.urls", name="formations_hosts"),
    host(r"assistance", "content.assistance_urls", name="assistance_hosts"),
)
