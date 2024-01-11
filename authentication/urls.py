from django.urls import path

from . import views

urlpatterns = [
    
    path('anhs',views.anhs, name="anhs"),
    path('sign_up', views.signup_view, name="sign_up"),
    path("login", views.login_view, name="login"),
    
    
    
]