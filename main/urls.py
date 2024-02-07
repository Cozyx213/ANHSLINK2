from django.urls import path
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("map", views.map, name="map"),
    path('history', views.history, name="history"),
    path('create_post', views.create_post, name='create_post'),
    path('logout', LogoutView.as_view(), name='logout'),
    path("library", views.library, name="library"),
    path("upload_view", views.upload_view, name="upload_view"),
    path("show_resource",views.show_resource, name="show_resource" ),
    path("download/<filemname>/", views.download_file, name = "download_file")
]