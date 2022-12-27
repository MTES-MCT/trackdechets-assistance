from request.middleware import RequestMiddleware as OriginalRequestMiddleware


class RequestMiddleware(OriginalRequestMiddleware):
    """Ignore logged-in users"""

    def process_response(self, request, response):
        if request.user.is_authenticated:
            return response
        return super().process_response(request, response)
