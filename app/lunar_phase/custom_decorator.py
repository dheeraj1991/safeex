import base64

from functools import wraps
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def logged_in_or_basicauth(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        """
            The decorator checks if the user is authenticated or not,
            if not authenticated, Checks if there is a authorization header with basic auth provided.
            If both the cases fail then returns a 401 request
        """
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)

        else:
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION'].split()
                if len(auth) == 2:
                    if auth[0].lower() == "basic":
                        uname, passwd = base64.b64decode(auth[1]).decode('utf-8').split(':')
                        user = authenticate(username=uname, password=passwd)
                        if user is not None:
                            if user.is_active:
                                login(request, user)
                                request.user = user
                                return function(request, *args, **kwargs)

        # If not authenticated using both the methods
        response = HttpResponse()
        response.status_code = 401
        return response

    return wrap
