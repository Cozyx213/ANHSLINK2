from django.urls import path, re_path
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
    
    path("home", views.home, name="home"),
    path("map", views.map, name="map"),
    path('history', views.history, name="history"),
    path('create_post', views.create_post, name='create_post'),
    path('create_forum', views.create_forum, name='create_forum'),
    path('logout', LogoutView.as_view(), name='logout'),
    path("library", views.library, name="library"),
    path("show_resource/<grade>/<subject>/",views.show_resource, name="show_resource" ),
    path("upload_view", views.upload_view, name="upload_view"),
    path("download/<uuid:uuid>/", views.download, name = "download"),
    path("forum", views.forum, name="forum"),
    path("forum/<int:id>/", views.forum_comment, name="forum_comment"),
    path("comment/", views.comment, name="comment"),
    path("reply/", views.reply, name="reply"),
    path("fetch/", views.fetch, name="fetch")
  ]