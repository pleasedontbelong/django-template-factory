import re
from django.conf import settings
from django.http import HttpResponseRedirect


class SSLRedirect(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if settings.FORCE_SSL and not self._is_secure(request):
            return self._redirect(request)

        return self.get_response(request)

    def _is_secure(self, request):
        if request.is_secure():
            return True

        # Handle the Webfaction case until this gets resolved in the request.is_secure()
        if 'HTTP_X_FORWARDED_SSL' in request.META:
            return request.META['HTTP_X_FORWARDED_SSL'] == 'on'

        return False

    def _redirect(self, request):
        if settings.DEBUG and request.method == 'POST':
            raise RuntimeError("POST to non secure site")

        newurl = re.sub(r"^http://", "https://", request.get_raw_uri())
        return HttpResponseRedirect(newurl)
