from django.urls import path

from . import views

urlpatterns = [
    path('',views.anhs, name="anhs"),
    path('anhs',views.anhs, name="anhs"),
    path('sign_up', views.signup_view, name="sign_up"),
    path("login_view", views.login_view, name="login_view"),
]