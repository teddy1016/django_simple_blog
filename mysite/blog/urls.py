from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path('upload/', views.image_upload_view, name="upload"),
    path('', views.PostList, name="home"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]