from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


# Create your views here.

def anhs(request):
    if request.method == "GET":
        return render(request, "registration/landingpage.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password= password )
        if user is not None:
            login(request, user, backend= 'authentication.backends.EmailOrUsernameModelBackend')
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "registration/login.html",{
                "message": "Invalid credentials"
            })
    return render(request, "registration/login.html")

def logout_view(request):
    return render(request, "registration/login.html")

def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This assumes the RegisterForm saves the user upon validation.
            login(request,user , backend= 'authentication.backends.EmailOrUsernameModelBackend')
            return HttpResponseRedirect(reverse('login'))  # Redirect to the home page after sign-up.
    
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {
        "form": form
    })
def enroll_view(request):
    return render(request, "registration/enroll.html")