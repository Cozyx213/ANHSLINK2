from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("map", views.map, name="map"),
    path('history', views.history, name="history"),
    
]