from django.shortcuts import redirect, render
from django.http import Http404

EXEMPT_URLS = ['/', '/authentication/admin/', '/authentication/login/', '/authentication/signup/','/authentication/anhs/']
SPEC_URLS = ['/admin/', '/media/']

class RequestAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
  
        response = self.get_response(request)

        if response.status_code == 404:
            # using the built in
            raise Http404 
        #     return render(request, '/authentication/signup.html', status=404)
            

        if 'user_id' not in request.session and request.path not in EXEMPT_URLS and not any(request.path.startswith(url) for url in SPEC_URLS):
            print(request.path, "login")
            return redirect('/authentication/anhs/')
        # else:
        #     print("nont")
            

        # Code to be executed for each request/response after
        # the view is called.

        return response

