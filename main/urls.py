from django.urls import path, re_path
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
    
    path("home", views.library, name="home"),
    path("map", views.map, name="map"),
    path('history', views.history, name="history"),
    path('create_post', views.create_post, name='create_post'),
    path("post_detail/<slug:slug>",views.post_detail, name="post_detail"),
    path('logout', LogoutView.as_view(), name='logout'),
    path("library", views.library, name="library"),
    path("show_resource/<int:grade>/<str:subject>/",views.show_resource, name="show_resource" ),
    path("upload_view", views.upload_view, name="upload_view"),
    path("download/<uuid:uuid>/", views.download, name = "download"),
    path("forum", views.forum, name="forum"),
    path("forum/<int:id>/", views.forum_comment, name="forum_comment"),
    path("comment/", views.comment, name="comment"),
    path("reply/", views.reply, name="reply"),
    path("fetch/", views.fetch, name="fetch"),
    path("get_forums", views.get_forums, name="get_forums"),
    path("classroom", views.classroom, name="classroom"),
    path("room", views.room, name="room"),
    path("forumLogs", views.forumLogs, name="forumLogs"),
    path("commentLogs", views.commentLogs, name="commentLogs"),
    path("logs_view", views.logs_view, name="logs_view"),
    path("deleteForum/<int:forumID>", views.deleteForum, name="deleteForum"),
    path("deleteComment/<int:commentID>",views.deleteComment, name="deleteComment"),
   
    path("subjects", views.subjects),
    
  ]