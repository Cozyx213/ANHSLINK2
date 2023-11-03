from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.template import RequestContext

# Create your views here.

def home (request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"main/home.html")
def map(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"main/map.html")
    
def history(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"main/history.html")


def not_found(request, exception):
    response = render(request, 'main/404.html')
    response.status_code = 404
    return response
    